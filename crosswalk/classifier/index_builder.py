"""Build FAISS index over all framework controls using BGE bi-encoder.

Usage:
    python -m classifier.index_builder [--force]
"""

import json
import sys
import time
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from .config import BIENCODER_MODEL, EMBEDDING_DIM, INDEX_DIR
from .data_loader import load_controls


def build_index(force: bool = False) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    index_path = INDEX_DIR / "controls.index"
    meta_path = INDEX_DIR / "controls_meta.json"

    if index_path.exists() and not force:
        print(f"Index already exists at {index_path}. Use --force to rebuild.")
        return

    # Load controls
    controls = load_controls()
    if not controls:
        print("ERROR: No controls found. Run 'node scripts/generate.js' first.")
        sys.exit(1)

    print(f"Loaded {len(controls)} controls from {len(set(c.framework for c in controls))} frameworks")

    # Build texts
    texts = [c.text for c in controls]
    meta = [
        {
            "framework": c.framework,
            "control_id": c.control_id,
            "title": c.title,
            "function": c.function,
        }
        for c in controls
    ]

    # Encode
    print(f"Loading model: {BIENCODER_MODEL}")
    model = SentenceTransformer(BIENCODER_MODEL)

    print("Encoding controls...")
    t0 = time.time()
    embeddings = model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True,  # BGE uses cosine sim = inner product on normalized
    )
    elapsed = time.time() - t0
    print(f"Encoded {len(embeddings)} controls in {elapsed:.1f}s")

    # Build FAISS index (inner product on normalized vectors = cosine similarity)
    embeddings_np = np.array(embeddings, dtype=np.float32)
    assert embeddings_np.shape == (len(controls), EMBEDDING_DIM), \
        f"Shape mismatch: {embeddings_np.shape} vs ({len(controls)}, {EMBEDDING_DIM})"

    index = faiss.IndexFlatIP(EMBEDDING_DIM)
    index.add(embeddings_np)

    # Save
    faiss.write_index(index, str(index_path))
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(f"Written {index_path} ({index.ntotal} vectors)")
    print(f"Written {meta_path} ({len(meta)} entries)")


if __name__ == "__main__":
    force = "--force" in sys.argv
    build_index(force=force)
