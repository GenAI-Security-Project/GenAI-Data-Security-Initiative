"""Cross-encoder reranker for candidate control mappings.

Takes bi-encoder top-N candidates and reranks using a cross-encoder model
that scores (query, document) pairs jointly.

Usage:
    from classifier.reranker import rerank
    reranked = rerank(query, candidates, top_k=10)
"""

from sentence_transformers import CrossEncoder

from .config import CROSSENCODER_MODEL

# Lazy-loaded singleton
_model: CrossEncoder | None = None


def _get_model() -> CrossEncoder:
    global _model
    if _model is None:
        _model = CrossEncoder(CROSSENCODER_MODEL, max_length=512)
    return _model


def rerank(query: str, candidates: list[dict], top_k: int = 10) -> list[dict]:
    """Rerank candidates using cross-encoder.

    Args:
        query: The query string (entry description).
        candidates: List of dicts with at least 'title', 'framework', 'control_id'.
                    Each should have a 'text' or we build it from fields.
        top_k: Number of results to return after reranking.

    Returns:
        Reranked list of candidates with updated scores and ranks.
    """
    if not candidates:
        return []

    model = _get_model()

    # Build (query, document) pairs
    pairs = []
    for c in candidates:
        doc = c.get("text")
        if not doc:
            parts = []
            if c.get("framework"):
                parts.append(c["framework"])
            if c.get("control_id"):
                parts.append(c["control_id"])
            if c.get("title"):
                parts.append(c["title"])
            if c.get("description"):
                parts.append(c["description"])
            if c.get("function"):
                parts.append(f"Function: {c['function']}")
            doc = " — ".join(parts) if parts else c.get("control_id", "")
        pairs.append((query, doc))

    # Score all pairs
    scores = model.predict(pairs)

    # Attach scores and sort
    scored = []
    for i, c in enumerate(candidates):
        entry = dict(c)
        entry["rerank_score"] = float(scores[i])
        entry["biencoder_score"] = c.get("score", 0.0)
        scored.append(entry)

    scored.sort(key=lambda x: x["rerank_score"], reverse=True)

    # Assign new ranks and trim
    for i, entry in enumerate(scored[:top_k]):
        entry["rank"] = i + 1
        entry["score"] = entry["rerank_score"]

    return scored[:top_k]
