"""Fine-tune BGE bi-encoder on domain-specific calibration data.

Uses contrastive learning (MultipleNegativesRankingLoss) to teach the
encoder that security-domain pairs like "Art. 15 — accuracy, robustness
and cybersecurity" ↔ "LLM01 Prompt Injection" are semantically related,
even when surface text doesn't overlap.

Usage:
    python -m classifier.finetune
    python -m classifier.finetune --epochs 10 --output classifier/models/bge-finetuned
    python -m classifier.finetune --eval-only  # evaluate without training
"""

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from sentence_transformers import (
    SentenceTransformer,
    InputExample,
    losses,
    evaluation,
)
from torch.utils.data import DataLoader

from .config import (
    BIENCODER_MODEL,
    SPLITS_DIR,
    CLASSIFIER_DIR,
    SPLIT_SEED,
)
from .data_loader import build_query, load_controls


DEFAULT_OUTPUT = CLASSIFIER_DIR / "models" / "bge-finetuned"
DEFAULT_EPOCHS = 5
DEFAULT_BATCH_SIZE = 16
DEFAULT_LR = 2e-5
DEFAULT_WARMUP_RATIO = 0.1


def load_calibration_pairs() -> list[InputExample]:
    """Load calibration split and build contrastive training pairs.

    Each calibration item gives us a (query, positive_passage) pair.
    MultipleNegativesRankingLoss uses in-batch negatives, so we don't
    need explicit hard negatives.
    """
    cal_path = SPLITS_DIR / "calibration.json"
    if not cal_path.exists():
        print("ERROR: calibration.json not found. Run split_maker first.")
        sys.exit(1)

    cal = json.loads(cal_path.read_text("utf-8"))
    controls_lookup = {}
    for c in load_controls():
        controls_lookup[(c.framework, c.control_id)] = c

    examples = []
    for item in cal:
        # Query = OWASP entry description
        query = build_query(item["entry_id"], item["entry_name"], item["severity"])

        # Positive = matching control text
        key = (item["framework"], item["control_id"])
        ctrl = controls_lookup.get(key)
        if ctrl:
            positive = ctrl.text
        else:
            # Fallback: construct from calibration data
            positive = f"{item['framework']} — {item['control_id']}: {item['control_name']}"

        examples.append(InputExample(texts=[query, positive]))

    return examples


def build_eval_pairs() -> tuple[list[str], list[str], list[float]]:
    """Build evaluation pairs from test split (sample for speed)."""
    test_path = SPLITS_DIR / "test.json"
    if not test_path.exists():
        return [], [], []

    test = json.loads(test_path.read_text("utf-8"))
    controls_lookup = {}
    for c in load_controls():
        controls_lookup[(c.framework, c.control_id)] = c

    rng = random.Random(SPLIT_SEED)

    # Group by entry
    entry_controls = defaultdict(list)
    for item in test:
        entry_controls[item["entry_id"]].append(item)

    queries = []
    passages = []
    scores = []

    for entry_id, items in entry_controls.items():
        if not items:
            continue
        sample_item = items[0]
        query = build_query(sample_item["entry_id"], sample_item["entry_name"],
                            sample_item["severity"])

        # Positives (sample up to 5)
        positives = rng.sample(items, min(5, len(items)))
        for item in positives:
            key = (item["framework"], item["control_id"])
            ctrl = controls_lookup.get(key)
            text = ctrl.text if ctrl else f"{item['framework']} — {item['control_id']}: {item['control_name']}"
            queries.append(query)
            passages.append(text)
            scores.append(1.0)

        # Negatives: random controls from other entries
        other_items = [t for t in test if t["entry_id"] != entry_id]
        neg_sample = rng.sample(other_items, min(5, len(other_items)))
        for item in neg_sample:
            key = (item["framework"], item["control_id"])
            ctrl = controls_lookup.get(key)
            text = ctrl.text if ctrl else f"{item['framework']} — {item['control_id']}: {item['control_name']}"
            queries.append(query)
            passages.append(text)
            scores.append(0.0)

    return queries, passages, scores


def finetune(
    output_path: Path = DEFAULT_OUTPUT,
    epochs: int = DEFAULT_EPOCHS,
    batch_size: int = DEFAULT_BATCH_SIZE,
    lr: float = DEFAULT_LR,
    warmup_ratio: float = DEFAULT_WARMUP_RATIO,
) -> SentenceTransformer:
    """Fine-tune the bi-encoder on calibration data."""
    print("=" * 60)
    print("  GenAI Security Crosswalk — Bi-encoder Fine-tuning")
    print("=" * 60)

    # Load base model
    print(f"\nLoading base model: {BIENCODER_MODEL}")
    model = SentenceTransformer(BIENCODER_MODEL)

    # Load training data
    print("Loading calibration pairs...")
    train_examples = load_calibration_pairs()
    print(f"  {len(train_examples)} training pairs")

    if not train_examples:
        print("ERROR: No training examples found.")
        sys.exit(1)

    train_loader = DataLoader(
        train_examples, shuffle=True, batch_size=batch_size
    )

    # Loss: MultipleNegativesRankingLoss (in-batch negatives)
    loss = losses.MultipleNegativesRankingLoss(model)

    # Evaluator
    print("Building evaluation pairs...")
    q, p, s = build_eval_pairs()
    evaluator = None
    if q:
        evaluator = evaluation.EmbeddingSimilarityEvaluator(
            q, p, s,
            name="crosswalk-test",
            show_progress_bar=False,
        )
        print(f"  {len(q)} evaluation pairs ({sum(1 for x in s if x > 0)} pos, {sum(1 for x in s if x == 0)} neg)")

    # Train
    warmup_steps = int(len(train_loader) * epochs * warmup_ratio)
    print(f"\nTraining for {epochs} epochs, batch_size={batch_size}, lr={lr}")
    print(f"  Warmup steps: {warmup_steps}")
    print(f"  Total steps: {len(train_loader) * epochs}")

    output_path.mkdir(parents=True, exist_ok=True)

    model.fit(
        train_objectives=[(train_loader, loss)],
        epochs=epochs,
        warmup_steps=warmup_steps,
        optimizer_params={"lr": lr},
        evaluator=evaluator,
        evaluation_steps=len(train_loader),  # eval every epoch
        output_path=str(output_path),
        show_progress_bar=True,
    )

    print(f"\nModel saved to {output_path}")
    print("\nTo use the fine-tuned model for classification:")
    print(f"  1. Update BIENCODER_MODEL in config.py to '{output_path}'")
    print("  2. Rebuild index: python -m classifier.index_builder --force")
    print("  3. Re-run eval:   python -m classifier.eval_harness")

    return model


def main():
    parser = argparse.ArgumentParser(
        description="Fine-tune BGE bi-encoder on crosswalk calibration data"
    )
    parser.add_argument(
        "--output", type=str, default=str(DEFAULT_OUTPUT),
        help="Output path for fine-tuned model"
    )
    parser.add_argument("--epochs", type=int, default=DEFAULT_EPOCHS)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--lr", type=float, default=DEFAULT_LR)
    parser.add_argument("--warmup-ratio", type=float, default=DEFAULT_WARMUP_RATIO)
    parser.add_argument(
        "--eval-only", action="store_true",
        help="Only run evaluation, no training"
    )
    args = parser.parse_args()

    if args.eval_only:
        print("Building evaluation pairs...")
        q, p, s = build_eval_pairs()
        if not q:
            print("No evaluation data found.")
            sys.exit(1)

        print(f"Loading model: {BIENCODER_MODEL}")
        model = SentenceTransformer(BIENCODER_MODEL)
        evaluator = evaluation.EmbeddingSimilarityEvaluator(
            q, p, s, name="crosswalk-eval", show_progress_bar=True
        )
        score = evaluator(model)
        print(f"Evaluation score (cosine similarity): {score:.4f}")
        return

    finetune(
        output_path=Path(args.output),
        epochs=args.epochs,
        batch_size=args.batch_size,
        lr=args.lr,
        warmup_ratio=args.warmup_ratio,
    )


if __name__ == "__main__":
    main()
