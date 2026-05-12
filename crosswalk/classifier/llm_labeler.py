"""LLM-as-SME pseudo-labeler using Claude for bulk relevance judgments.

Uses few-shot examples from the calibration set to judge whether a candidate
framework control is relevant to an OWASP GenAI vulnerability entry.

Usage:
    python -m classifier.llm_labeler --source LLM01 --top-k 20
    python -m classifier.llm_labeler --batch --top-k 10 --output labels.json

Requires ANTHROPIC_API_KEY environment variable.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from .config import SPLITS_DIR, CLASSIFIER_DIR
from .data_loader import load_entries, load_controls, build_query

# Few-shot template
SYSTEM_PROMPT = """\
You are an expert security frameworks analyst specializing in AI/ML security.
Your task is to judge whether a specific framework control is relevant to
mitigating a given OWASP GenAI vulnerability.

A control is RELEVANT if implementing it would directly help prevent, detect,
or respond to the vulnerability described. A control is NOT RELEVANT if it
only has a tangential or indirect connection.

Respond with a JSON object:
{
  "relevant": true or false,
  "confidence": 0.0 to 1.0,
  "reasoning": "one sentence explanation"
}"""


def build_few_shot_examples(n: int = 5) -> list[dict]:
    """Load few-shot examples from the calibration split."""
    cal_path = SPLITS_DIR / "calibration.json"
    if not cal_path.exists():
        print("ERROR: Calibration split not found. Run split_maker first.")
        sys.exit(1)

    cal = json.loads(cal_path.read_text("utf-8"))

    # Pick diverse examples: mix of relevant (from curated mappings = all relevant)
    # and we'll construct negative examples by mismatching
    examples = []

    # Positive examples (curated mappings are ground truth relevant)
    for item in cal[:n]:
        examples.append({
            "role": "user",
            "content": (
                f"Vulnerability: {item['entry_id']} — {item['entry_name']} "
                f"(Severity: {item['severity']})\n"
                f"Control: {item['framework']} — {item['control_id']}: "
                f"{item['control_name']}\n"
                f"Is this control relevant to mitigating this vulnerability?"
            ),
        })
        examples.append({
            "role": "assistant",
            "content": json.dumps({
                "relevant": True,
                "confidence": 0.95,
                "reasoning": f"{item['control_id']} directly addresses "
                             f"{item['entry_name'].lower()} through "
                             f"{item['tier'].lower()} controls.",
            }),
        })

    return examples


def label_candidate(client, entry: dict, candidate: dict,
                    few_shot: list[dict]) -> dict:
    """Label a single candidate using the LLM."""
    user_msg = (
        f"Vulnerability: {entry['id']} — {entry['name']} "
        f"(Severity: {entry['severity']})\n"
        f"Control: {candidate['framework']} — {candidate['control_id']}: "
        f"{candidate['title']}\n"
        f"Is this control relevant to mitigating this vulnerability?"
    )

    messages = few_shot + [{"role": "user", "content": user_msg}]

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    text = response.content[0].text.strip()
    # Parse JSON from response
    try:
        # Handle potential markdown wrapping
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        result = json.loads(text)
    except json.JSONDecodeError:
        result = {"relevant": False, "confidence": 0.0,
                  "reasoning": f"Parse error: {text[:100]}"}

    return {
        "entry_id": entry["id"],
        "framework": candidate["framework"],
        "control_id": candidate["control_id"],
        "title": candidate["title"],
        "relevant": result.get("relevant", False),
        "confidence": result.get("confidence", 0.0),
        "reasoning": result.get("reasoning", ""),
    }


def label_batch(source_id: str | None = None, top_k: int = 10,
                output_path: str | None = None) -> list[dict]:
    """Label candidates for one or all entries."""
    try:
        import anthropic
    except ImportError:
        print("ERROR: pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Set ANTHROPIC_API_KEY environment variable.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    few_shot = build_few_shot_examples(5)
    entries = load_entries()

    if source_id:
        entries = [e for e in entries if e["id"] == source_id]
        if not entries:
            print(f"ERROR: Entry '{source_id}' not found.")
            sys.exit(1)

    # Import classify to get candidates
    from .classify import load_index
    from sentence_transformers import SentenceTransformer
    import numpy as np
    from .config import BIENCODER_MODEL

    index, meta = load_index()
    model = SentenceTransformer(BIENCODER_MODEL)

    all_labels = []
    total = len(entries)

    for i, entry in enumerate(entries):
        query = build_query(entry["id"], entry["name"], entry["severity"])
        q_emb = model.encode([query], normalize_embeddings=True)
        q_emb = np.array(q_emb, dtype=np.float32)

        search_k = min(top_k, index.ntotal)
        scores, indices = index.search(q_emb, search_k)

        candidates = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < 0:
                continue
            m = meta[idx]
            candidates.append({
                "framework": m["framework"],
                "control_id": m["control_id"],
                "title": m["title"],
                "function": m.get("function"),
                "score": float(score),
            })

        print(f"[{i+1}/{total}] {entry['id']}: labeling {len(candidates)} candidates...")

        for cand in candidates:
            label = label_candidate(client, entry, cand, few_shot)
            all_labels.append(label)
            # Rate limiting
            time.sleep(0.2)

    # Output
    if output_path:
        Path(output_path).write_text(
            json.dumps(all_labels, indent=2), encoding="utf-8"
        )
        print(f"\nWritten {len(all_labels)} labels to {output_path}")
    else:
        print(json.dumps(all_labels, indent=2))

    # Summary
    relevant = sum(1 for l in all_labels if l["relevant"])
    avg_conf = sum(l["confidence"] for l in all_labels) / len(all_labels) if all_labels else 0
    print(f"\nSummary: {relevant}/{len(all_labels)} relevant "
          f"({relevant/len(all_labels)*100:.1f}%), avg confidence: {avg_conf:.2f}")

    return all_labels


def main():
    parser = argparse.ArgumentParser(description="LLM pseudo-labeler for control relevance")
    parser.add_argument("--source", default=None, help="OWASP entry ID (omit for all)")
    parser.add_argument("--top-k", type=int, default=10, help="Candidates per entry")
    parser.add_argument("--output", default=None, help="Output JSON path")
    args = parser.parse_args()

    label_batch(args.source, args.top_k, args.output)


if __name__ == "__main__":
    main()
