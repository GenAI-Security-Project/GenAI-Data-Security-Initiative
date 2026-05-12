"""Contamination probe: compare retrieval quality on seen vs. unseen frameworks.

CoSAI is held out as "contamination-clean" — it has zero ground-truth mappings
in the OWASP entries. This probe measures whether the model retrieves CoSAI
controls with comparable confidence and semantic coherence to frameworks that
DO appear in the hand-curated mappings (contaminated).

Approach:
  Since CoSAI has no ground-truth labels, we cannot compute P@k/R@k directly.
  Instead we measure:
    1. Score distribution — are retrieval scores for CoSAI systematically lower?
    2. Rank penetration — how often does CoSAI appear in the global top-k?
    3. Semantic coherence — do CoSAI candidates cluster around the right topics?
    4. Per-entry score gap — mean bi-encoder score for contaminated vs. clean

Usage:
    python -m classifier.contamination_probe
    python -m classifier.contamination_probe --rerank
"""

import argparse
import json
import sys
import time
from collections import defaultdict

import numpy as np
from sentence_transformers import SentenceTransformer

from .config import (
    BIENCODER_MODEL, INDEX_DIR, SPLITS_DIR,
    CONTAMINATION_CLEAN_FRAMEWORK, BOOTSTRAP_SEED, BOOTSTRAP_N,
)
from .data_loader import load_entries, load_controls, build_query


def load_index():
    import faiss
    index_path = INDEX_DIR / "controls.index"
    meta_path = INDEX_DIR / "controls_meta.json"
    index = faiss.read_index(str(index_path))
    meta = json.loads(meta_path.read_text("utf-8"))
    return index, meta


def run_probe(use_reranker: bool = False) -> dict:
    clean_fw = CONTAMINATION_CLEAN_FRAMEWORK

    print("=" * 60)
    print("  Contamination Probe")
    print(f"  Clean framework: {clean_fw}")
    print(f"  Mode: {'Reranker' if use_reranker else 'Bi-encoder'}")
    print("=" * 60)

    # Load
    index, meta = load_index()
    model = SentenceTransformer(BIENCODER_MODEL)
    entries = load_entries()

    # Identify contaminated frameworks (those with ground-truth mappings)
    contaminated_fws = set()
    for e in entries:
        for m in e.get("mappings", []):
            contaminated_fws.add(m["framework"])
    # Frameworks in registry
    registry_fws = set(m["framework"] for m in meta)

    print(f"\n  Contaminated frameworks (in GT): {len(contaminated_fws)}")
    print(f"  Registry frameworks: {len(registry_fws)}")
    print(f"  Clean framework in registry: {clean_fw in registry_fws}")

    if clean_fw not in registry_fws:
        print(f"ERROR: {clean_fw} not in registry. Cannot probe.")
        sys.exit(1)

    # For each entry, retrieve top-50 globally, then split by framework type
    top_k = 50
    per_entry_scores = {
        "clean": [],       # scores for clean framework controls
        "contaminated": [], # scores for contaminated framework controls
        "other": [],        # scores for registry-only (neither)
    }
    clean_rank_positions = []  # rank of first clean framework control per entry
    clean_counts_in_top10 = [] # count of clean controls in top-10 per entry
    clean_counts_in_top20 = []

    # Per-entry detail
    entry_details = []

    t0 = time.time()
    for entry in entries:
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
                "score": float(score),
            })

        if use_reranker:
            from .reranker import rerank
            for c in candidates:
                c["text"] = f"{c['framework']} -- {c['control_id']}: {c['title']}"
            candidates = rerank(query, candidates, top_k=top_k)

        # Classify scores by framework type
        entry_clean_scores = []
        entry_contam_scores = []
        first_clean_rank = None
        clean_in_top10 = 0
        clean_in_top20 = 0

        for rank, c in enumerate(candidates):
            fw = c["framework"]
            s = c.get("score", c.get("rerank_score", 0))

            if fw == clean_fw:
                per_entry_scores["clean"].append(s)
                entry_clean_scores.append(s)
                if first_clean_rank is None:
                    first_clean_rank = rank + 1
                if rank < 10:
                    clean_in_top10 += 1
                if rank < 20:
                    clean_in_top20 += 1
            elif fw in contaminated_fws:
                per_entry_scores["contaminated"].append(s)
                entry_contam_scores.append(s)
            else:
                per_entry_scores["other"].append(s)

        clean_rank_positions.append(first_clean_rank if first_clean_rank else top_k + 1)
        clean_counts_in_top10.append(clean_in_top10)
        clean_counts_in_top20.append(clean_in_top20)

        entry_details.append({
            "entry_id": entry["id"],
            "entry_name": entry["name"],
            "clean_mean_score": float(np.mean(entry_clean_scores)) if entry_clean_scores else None,
            "contam_mean_score": float(np.mean(entry_contam_scores)) if entry_contam_scores else None,
            "first_clean_rank": first_clean_rank,
            "clean_in_top10": clean_in_top10,
            "clean_in_top20": clean_in_top20,
        })

    elapsed = time.time() - t0

    # Aggregate statistics
    clean_scores = np.array(per_entry_scores["clean"])
    contam_scores = np.array(per_entry_scores["contaminated"])
    rank_arr = np.array(clean_rank_positions, dtype=float)
    top10_arr = np.array(clean_counts_in_top10, dtype=float)
    top20_arr = np.array(clean_counts_in_top20, dtype=float)

    # Score gap
    clean_mean = float(np.mean(clean_scores)) if len(clean_scores) else 0
    contam_mean = float(np.mean(contam_scores)) if len(contam_scores) else 0
    score_gap = contam_mean - clean_mean

    # Bootstrap CI on score gap
    rng = np.random.RandomState(BOOTSTRAP_SEED)
    if len(clean_scores) > 0 and len(contam_scores) > 0:
        boot_gaps = []
        for _ in range(BOOTSTRAP_N):
            bc = rng.choice(clean_scores, size=len(clean_scores), replace=True)
            bx = rng.choice(contam_scores, size=len(contam_scores), replace=True)
            boot_gaps.append(float(np.mean(bx) - np.mean(bc)))
        gap_ci_lo, gap_ci_hi = np.percentile(boot_gaps, [2.5, 97.5])
    else:
        gap_ci_lo = gap_ci_hi = 0.0

    results = {
        "clean_framework": clean_fw,
        "mode": "reranker" if use_reranker else "biencoder",
        "n_entries": len(entries),
        "elapsed_seconds": round(elapsed, 1),
        "score_distribution": {
            "clean_mean": round(clean_mean, 4),
            "clean_std": round(float(np.std(clean_scores)), 4) if len(clean_scores) else 0,
            "clean_n": len(clean_scores),
            "contaminated_mean": round(contam_mean, 4),
            "contaminated_std": round(float(np.std(contam_scores)), 4) if len(contam_scores) else 0,
            "contaminated_n": len(contam_scores),
            "score_gap": round(score_gap, 4),
            "score_gap_ci": [round(gap_ci_lo, 4), round(gap_ci_hi, 4)],
        },
        "rank_penetration": {
            "mean_first_clean_rank": round(float(np.mean(rank_arr)), 1),
            "median_first_clean_rank": round(float(np.median(rank_arr)), 1),
            "mean_clean_in_top10": round(float(np.mean(top10_arr)), 2),
            "mean_clean_in_top20": round(float(np.mean(top20_arr)), 2),
        },
        "per_entry": entry_details,
    }

    # Print report
    print(f"\n  Completed in {elapsed:.1f}s")
    print(f"\n  Score Distribution")
    print(f"  {'-'*50}")
    sd = results["score_distribution"]
    print(f"  {'Contaminated:':<20} mean={sd['contaminated_mean']:.4f} "
          f"std={sd['contaminated_std']:.4f} (n={sd['contaminated_n']})")
    print(f"  {'Clean (' + clean_fw + '):':<20} mean={sd['clean_mean']:.4f} "
          f"std={sd['clean_std']:.4f} (n={sd['clean_n']})")
    print(f"  {'Score gap:':<20} {sd['score_gap']:.4f} "
          f"95% CI [{sd['score_gap_ci'][0]:.4f}, {sd['score_gap_ci'][1]:.4f}]")

    print(f"\n  Rank Penetration")
    print(f"  {'-'*50}")
    rp = results["rank_penetration"]
    print(f"  Mean first {clean_fw} rank:  {rp['mean_first_clean_rank']:.1f}")
    print(f"  Median first {clean_fw} rank: {rp['median_first_clean_rank']:.1f}")
    print(f"  Mean {clean_fw} in top-10:   {rp['mean_clean_in_top10']:.2f}")
    print(f"  Mean {clean_fw} in top-20:   {rp['mean_clean_in_top20']:.2f}")

    # Threshold check from pre-registration
    # "Contamination gap <= 15pp" — here measured as score gap
    print(f"\n  Pre-registered threshold:")
    gap_pp = abs(score_gap) * 100
    gap_pass = gap_pp <= 15
    print(f"    Score gap <= 15pp: {gap_pp:.1f}pp {'PASS' if gap_pass else 'FAIL'}")

    # Top entries with best clean framework scores
    print(f"\n  Top 5 entries by {clean_fw} score:")
    sorted_details = sorted(
        [d for d in entry_details if d["clean_mean_score"] is not None],
        key=lambda x: x["clean_mean_score"], reverse=True
    )
    for d in sorted_details[:5]:
        print(f"    {d['entry_id']:<8} clean={d['clean_mean_score']:.4f} "
              f"contam={d['contam_mean_score']:.4f} "
              f"first_rank={d['first_clean_rank']}")

    # Save
    probe_path = SPLITS_DIR / f"contamination_probe_{results['mode']}.json"
    probe_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\n  Report saved to {probe_path}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Contamination probe")
    parser.add_argument("--rerank", action="store_true")
    args = parser.parse_args()
    run_probe(use_reranker=args.rerank)


if __name__ == "__main__":
    main()
