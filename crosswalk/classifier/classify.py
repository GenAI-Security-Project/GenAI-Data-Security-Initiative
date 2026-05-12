"""Classify: retrieve top-k framework controls for an OWASP entry.

Usage:
    python -m classifier.classify --source LLM01 --target "NIST AI RMF 1.0" --top-k 10
    python -m classifier.classify --source LLM01 --top-k 20
    python -m classifier.classify --source LLM01 --all-frameworks --top-k 5
    python -m classifier.classify --source LLM01 --json
"""

import argparse
import json
import sys

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from .config import BIENCODER_MODEL, EMBEDDING_DIM, INDEX_DIR, DEFAULT_TOP_K
from .data_loader import load_entries, build_query


def load_index():
    index_path = INDEX_DIR / "controls.index"
    meta_path = INDEX_DIR / "controls_meta.json"
    if not index_path.exists():
        print("ERROR: Index not found. Run 'python -m classifier.index_builder' first.")
        sys.exit(1)
    index = faiss.read_index(str(index_path))
    meta = json.loads(meta_path.read_text("utf-8"))
    return index, meta


def classify(source_id: str, target_framework: str | None = None,
             top_k: int = DEFAULT_TOP_K, output_json: bool = False,
             use_reranker: bool = False) -> list[dict]:
    """Retrieve top-k candidate controls for an OWASP entry."""
    # Load entry
    entries = load_entries()
    entry = next((e for e in entries if e["id"] == source_id), None)
    if not entry:
        print(f"ERROR: Entry '{source_id}' not found.")
        sys.exit(1)

    # Load index
    index, meta = load_index()

    # Build query
    query = build_query(entry["id"], entry["name"], entry["severity"])

    # Encode query
    model = SentenceTransformer(BIENCODER_MODEL)
    q_emb = model.encode([query], normalize_embeddings=True)
    q_emb = np.array(q_emb, dtype=np.float32)

    # Search — retrieve more for reranking or framework filtering
    search_k = top_k * 5 if (target_framework or use_reranker) else top_k
    if use_reranker:
        search_k = max(search_k, 50)
    search_k = min(search_k, index.ntotal)
    scores, indices = index.search(q_emb, search_k)

    # Build results
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0:
            continue
        m = meta[idx]
        if target_framework and m["framework"] != target_framework:
            continue
        results.append({
            "rank": len(results) + 1,
            "framework": m["framework"],
            "control_id": m["control_id"],
            "title": m["title"],
            "function": m["function"],
            "score": round(float(score), 4),
            "text": f"{m['framework']} -- {m['control_id']}: {m['title']}",
        })
        if not use_reranker and len(results) >= top_k:
            break

    # Cross-encoder reranking
    if use_reranker and results:
        from .reranker import rerank
        results = rerank(query, results, top_k=top_k)

    # Remove internal fields from output
    for r in results:
        r.pop("text", None)

    # Check against existing mappings
    existing = {
        (m["framework"], m["control_id"])
        for m in entry.get("mappings", [])
    }
    for r in results:
        r["curated"] = (r["framework"], r["control_id"]) in existing

    # Output
    output = {
        "source": source_id,
        "source_name": entry["name"],
        "severity": entry["severity"],
        "target_framework": target_framework,
        "top_k": top_k,
        "query": query,
        "candidates": results,
    }

    if output_json:
        print(json.dumps(output, indent=2))
    else:
        print(f"\n  {source_id}: {entry['name']} (Severity: {entry['severity']})")
        if target_framework:
            print(f"  Target: {target_framework}")
        print(f"  Top-{top_k} candidates:\n")
        print(f"  {'Rank':<5} {'Score':<8} {'Framework':<25} {'Control':<15} {'Title':<40} {'Curated'}")
        print(f"  {'-'*5} {'-'*8} {'-'*25} {'-'*15} {'-'*40} {'-'*7}")
        for r in results:
            curated_mark = "  *" if r["curated"] else ""
            print(f"  {r['rank']:<5} {r['score']:<8.4f} {r['framework'][:24]:<25} "
                  f"{r['control_id'][:14]:<15} {r['title'][:39]:<40} {curated_mark}")
        print()

    return results


def main():
    parser = argparse.ArgumentParser(description="Classify OWASP entries to framework controls")
    parser.add_argument("--source", required=True, help="OWASP entry ID (e.g. LLM01)")
    parser.add_argument("--target", default=None, help="Target framework name (optional)")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K, help=f"Number of candidates (default {DEFAULT_TOP_K})")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--rerank", action="store_true", help="Use cross-encoder reranker")
    args = parser.parse_args()

    classify(args.source, args.target, args.top_k, args.json, args.rerank)


if __name__ == "__main__":
    main()
