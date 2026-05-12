"""Evaluation harness for the classifier pipeline.

Computes P@k, R@k, MAP, R-Precision with 95% bootstrap CIs against the
frozen test split. Compares bi-encoder baseline vs. cross-encoder reranker.

Usage:
    python -m classifier.eval_harness
    python -m classifier.eval_harness --rerank
    python -m classifier.eval_harness --rerank --verbose
"""

import argparse
import json
import sys
import time
from collections import defaultdict

import numpy as np
from sentence_transformers import SentenceTransformer

from .config import (
    BIENCODER_MODEL, EMBEDDING_DIM, INDEX_DIR, SPLITS_DIR,
    K_VALUES, BOOTSTRAP_SEED, BOOTSTRAP_N,
)
from .data_loader import load_entries, load_controls, build_query


def load_test_split() -> dict[str, set[tuple[str, str]]]:
    """Load test split as {entry_id: set of (framework, control_id)}."""
    test_path = SPLITS_DIR / "test.json"
    if not test_path.exists():
        print("ERROR: Test split not found. Run split_maker first.")
        sys.exit(1)
    test = json.loads(test_path.read_text("utf-8"))
    ground_truth = defaultdict(set)
    for item in test:
        ground_truth[item["entry_id"]].add(
            (item["framework"], item["control_id"])
        )
    return dict(ground_truth)


def load_index():
    """Load FAISS index and metadata."""
    import faiss
    index_path = INDEX_DIR / "controls.index"
    meta_path = INDEX_DIR / "controls_meta.json"
    if not index_path.exists():
        print("ERROR: Index not found. Run index_builder first.")
        sys.exit(1)
    index = faiss.read_index(str(index_path))
    meta = json.loads(meta_path.read_text("utf-8"))
    return index, meta


def retrieve_candidates(entry: dict, index, meta, model,
                        top_k: int = 50) -> list[dict]:
    """Bi-encoder retrieval of top-k candidates."""
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
            "text": f"{m['framework']} -- {m['control_id']}: {m['title']}",
        })
    return candidates


# ── Metrics ──────────────────────────────────────────────────────────────────

def precision_at_k(retrieved: list[tuple], relevant: set[tuple], k: int) -> float:
    """Fraction of top-k that are relevant."""
    top = retrieved[:k]
    if not top:
        return 0.0
    return sum(1 for r in top if r in relevant) / k


def recall_at_k(retrieved: list[tuple], relevant: set[tuple], k: int) -> float:
    """Fraction of relevant items found in top-k."""
    if not relevant:
        return 0.0
    top = retrieved[:k]
    return sum(1 for r in top if r in relevant) / len(relevant)


def average_precision(retrieved: list[tuple], relevant: set[tuple]) -> float:
    """Average precision for a single query (for MAP computation)."""
    if not relevant:
        return 0.0
    hits = 0
    sum_prec = 0.0
    for i, r in enumerate(retrieved):
        if r in relevant:
            hits += 1
            sum_prec += hits / (i + 1)
    return sum_prec / len(relevant) if relevant else 0.0


def r_precision(retrieved: list[tuple], relevant: set[tuple]) -> float:
    """Precision at R, where R = number of relevant items."""
    r = len(relevant)
    if r == 0:
        return 0.0
    top_r = retrieved[:r]
    return sum(1 for item in top_r if item in relevant) / r


def compute_metrics(all_retrieved: dict[str, list[tuple]],
                    ground_truth: dict[str, set[tuple]],
                    k_values: list[int]) -> dict:
    """Compute all metrics across queries."""
    # Only evaluate entries that appear in both retrieved and ground truth
    entry_ids = sorted(set(all_retrieved.keys()) & set(ground_truth.keys()))
    n = len(entry_ids)

    if n == 0:
        return {"n_queries": 0, "error": "No overlapping entries"}

    results = {"n_queries": n}

    for k in k_values:
        p_scores = [precision_at_k(all_retrieved[eid], ground_truth[eid], k) for eid in entry_ids]
        r_scores = [recall_at_k(all_retrieved[eid], ground_truth[eid], k) for eid in entry_ids]
        results[f"P@{k}"] = float(np.mean(p_scores))
        results[f"R@{k}"] = float(np.mean(r_scores))

    ap_scores = [average_precision(all_retrieved[eid], ground_truth[eid]) for eid in entry_ids]
    rp_scores = [r_precision(all_retrieved[eid], ground_truth[eid]) for eid in entry_ids]
    results["MAP"] = float(np.mean(ap_scores))
    results["R-Precision"] = float(np.mean(rp_scores))

    return results


def bootstrap_ci(all_retrieved: dict[str, list[tuple]],
                 ground_truth: dict[str, set[tuple]],
                 k_values: list[int],
                 n_bootstrap: int = BOOTSTRAP_N,
                 seed: int = BOOTSTRAP_SEED) -> dict:
    """Compute 95% bootstrap confidence intervals for all metrics."""
    rng = np.random.RandomState(seed)
    entry_ids = sorted(set(all_retrieved.keys()) & set(ground_truth.keys()))
    n = len(entry_ids)

    if n == 0:
        return {}

    # Collect per-query metric arrays
    metric_arrays = {}
    for k in k_values:
        metric_arrays[f"P@{k}"] = np.array([
            precision_at_k(all_retrieved[eid], ground_truth[eid], k) for eid in entry_ids
        ])
        metric_arrays[f"R@{k}"] = np.array([
            recall_at_k(all_retrieved[eid], ground_truth[eid], k) for eid in entry_ids
        ])
    metric_arrays["MAP"] = np.array([
        average_precision(all_retrieved[eid], ground_truth[eid]) for eid in entry_ids
    ])
    metric_arrays["R-Precision"] = np.array([
        r_precision(all_retrieved[eid], ground_truth[eid]) for eid in entry_ids
    ])

    # Bootstrap
    cis = {}
    for metric_name, arr in metric_arrays.items():
        boot_means = np.array([
            np.mean(rng.choice(arr, size=n, replace=True))
            for _ in range(n_bootstrap)
        ])
        lo, hi = np.percentile(boot_means, [2.5, 97.5])
        cis[metric_name] = {
            "mean": float(np.mean(arr)),
            "ci_lo": float(lo),
            "ci_hi": float(hi),
        }

    return cis


# ── Main evaluation ─────────────────────────────────────────────────────────

def run_eval(use_reranker: bool = False, verbose: bool = False,
             output_path: str | None = None) -> dict:
    """Run full evaluation pipeline."""
    print("=" * 60)
    print(f"  OWASP GenAI Crosswalk — Classifier Evaluation")
    print(f"  Mode: {'Bi-encoder + Cross-encoder reranker' if use_reranker else 'Bi-encoder baseline'}")
    print("=" * 60)

    # Load data
    print("\nLoading test split...")
    ground_truth = load_test_split()
    print(f"  {len(ground_truth)} entries with ground truth")
    total_gt = sum(len(v) for v in ground_truth.values())
    print(f"  {total_gt} total ground-truth mappings")

    print("Loading index...")
    index, meta = load_index()
    print(f"  {index.ntotal} controls indexed")

    print(f"Loading bi-encoder: {BIENCODER_MODEL}")
    bi_model = SentenceTransformer(BIENCODER_MODEL)

    reranker = None
    if use_reranker:
        from .reranker import rerank
        from .config import CROSSENCODER_MODEL
        print(f"Loading cross-encoder: {CROSSENCODER_MODEL}")
        # Warm up the reranker model
        from .reranker import _get_model
        _get_model()
        reranker = rerank

    entries = load_entries()
    # Only eval entries in ground truth
    eval_entries = [e for e in entries if e["id"] in ground_truth]
    print(f"\nEvaluating {len(eval_entries)} entries...")

    all_retrieved = {}
    t0 = time.time()

    for i, entry in enumerate(eval_entries):
        # Bi-encoder retrieval (top-50 for reranking headroom)
        retrieve_k = 50 if use_reranker else max(K_VALUES)
        candidates = retrieve_candidates(entry, index, meta, bi_model, retrieve_k)

        if use_reranker and reranker:
            query = build_query(entry["id"], entry["name"], entry["severity"])
            candidates = reranker(query, candidates, top_k=max(K_VALUES))

        # Extract (framework, control_id) tuples in rank order
        retrieved_tuples = [
            (c["framework"], c["control_id"]) for c in candidates
        ]
        all_retrieved[entry["id"]] = retrieved_tuples

        if verbose and (i + 1) % 10 == 0:
            print(f"  [{i+1}/{len(eval_entries)}]")

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s")

    # Compute metrics
    print("\nComputing metrics...")
    metrics = compute_metrics(all_retrieved, ground_truth, K_VALUES)

    print("Computing 95% bootstrap CIs (10,000 resamples)...")
    cis = bootstrap_ci(all_retrieved, ground_truth, K_VALUES)

    # Report
    mode = "reranker" if use_reranker else "biencoder"
    report = {
        "mode": mode,
        "model": BIENCODER_MODEL,
        "n_queries": metrics["n_queries"],
        "n_controls": index.ntotal,
        "n_ground_truth_mappings": total_gt,
        "elapsed_seconds": round(elapsed, 1),
        "metrics": metrics,
        "confidence_intervals": cis,
    }

    print("\n" + "=" * 60)
    print(f"  RESULTS ({mode})")
    print("=" * 60)
    print(f"\n  Queries: {metrics['n_queries']}")
    print(f"  Ground truth mappings: {total_gt}")
    print()

    # Table header
    header = f"  {'Metric':<15} {'Value':>8} {'95% CI':>20}"
    print(header)
    print(f"  {'-'*15} {'-'*8} {'-'*20}")

    for k in K_VALUES:
        for prefix in ["P", "R"]:
            key = f"{prefix}@{k}"
            val = metrics.get(key, 0)
            ci = cis.get(key, {})
            ci_str = f"[{ci.get('ci_lo', 0):.4f}, {ci.get('ci_hi', 0):.4f}]" if ci else ""
            print(f"  {key:<15} {val:>8.4f} {ci_str:>20}")

    for key in ["MAP", "R-Precision"]:
        val = metrics.get(key, 0)
        ci = cis.get(key, {})
        ci_str = f"[{ci.get('ci_lo', 0):.4f}, {ci.get('ci_hi', 0):.4f}]" if ci else ""
        print(f"  {key:<15} {val:>8.4f} {ci_str:>20}")

    print()

    # Check against pre-registered thresholds
    print("  Pre-registered thresholds:")
    r10 = metrics.get("R@10", 0)
    map_val = metrics.get("MAP", 0)
    r10_pass = r10 >= 0.50
    map_pass = map_val >= 0.25
    print(f"    R@10 >= 0.50: {r10:.4f} {'PASS' if r10_pass else 'FAIL'}")
    print(f"    MAP  >= 0.25: {map_val:.4f} {'PASS' if map_pass else 'FAIL'}")
    print()

    # Save report
    if output_path:
        from pathlib import Path
        Path(output_path).write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"  Report saved to {output_path}")
    else:
        default_path = SPLITS_DIR / f"eval_report_{mode}.json"
        default_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"  Report saved to {default_path}")

    return report


def main():
    parser = argparse.ArgumentParser(description="Eval harness for classifier pipeline")
    parser.add_argument("--rerank", action="store_true", help="Use cross-encoder reranker")
    parser.add_argument("--verbose", action="store_true", help="Show progress")
    parser.add_argument("--output", default=None, help="Output report path")
    args = parser.parse_args()

    run_eval(use_reranker=args.rerank, verbose=args.verbose, output_path=args.output)


if __name__ == "__main__":
    main()
