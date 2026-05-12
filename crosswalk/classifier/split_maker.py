"""Create SHA-pinned calibration/test splits for evaluation.

Usage:
    python -m classifier.split_maker
"""

import hashlib
import json
import sys
from collections import Counter

from .config import (
    SPLITS_DIR, SPLIT_SEED, CALIBRATION_SIZE,
    CONTAMINATION_CLEAN_FRAMEWORK,
)
from .data_loader import load_mappings


def mapping_hash(m) -> str:
    """Deterministic hash for a mapping instance."""
    key = f"{m.entry_id}::{m.framework}::{m.control_id}"
    return hashlib.sha256(key.encode()).hexdigest()


def make_splits() -> None:
    SPLITS_DIR.mkdir(parents=True, exist_ok=True)
    meta_path = SPLITS_DIR / "split_meta.json"

    if meta_path.exists():
        print(f"Splits already exist at {meta_path}. Delete to regenerate.")
        return

    mappings = load_mappings()
    print(f"Total mappings: {len(mappings)}")

    # Separate contamination-clean mappings
    clean = [m for m in mappings if m.framework == CONTAMINATION_CLEAN_FRAMEWORK]
    evaluable = [m for m in mappings if m.framework != CONTAMINATION_CLEAN_FRAMEWORK]

    print(f"Contamination-clean ({CONTAMINATION_CLEAN_FRAMEWORK}): {len(clean)}")
    print(f"Evaluable (non-clean): {len(evaluable)}")

    # Sort by hash for deterministic ordering
    evaluable_hashed = [(mapping_hash(m), m) for m in evaluable]
    evaluable_hashed.sort(key=lambda x: x[0])

    # Stratified split: hash-based deterministic partition
    # Take first CALIBRATION_SIZE as calibration, rest as test
    cal_size = min(CALIBRATION_SIZE, len(evaluable_hashed) // 3)
    calibration = evaluable_hashed[:cal_size]
    test = evaluable_hashed[cal_size:]

    # Verify no leakage
    cal_keys = {h for h, _ in calibration}
    test_keys = {h for h, _ in test}
    assert cal_keys.isdisjoint(test_keys), "LEAKAGE: calibration and test overlap!"

    # Verify clean framework not in calibration
    cal_fws = {m.framework for _, m in calibration}
    assert CONTAMINATION_CLEAN_FRAMEWORK not in cal_fws, \
        f"LEAKAGE: {CONTAMINATION_CLEAN_FRAMEWORK} in calibration!"

    # Stats
    def split_stats(items):
        by_source = Counter(m.source_list for _, m in items)
        by_sev = Counter(m.severity for _, m in items)
        by_fw = Counter(m.framework for _, m in items)
        return {
            "count": len(items),
            "by_source_list": dict(by_source),
            "by_severity": dict(by_sev),
            "by_framework": dict(by_fw.most_common(10)),
        }

    meta = {
        "seed": SPLIT_SEED,
        "hash_algorithm": "sha256",
        "hash_key_format": "{entry_id}::{framework}::{control_id}",
        "contamination_clean_framework": CONTAMINATION_CLEAN_FRAMEWORK,
        "calibration": split_stats(calibration),
        "test": split_stats(test),
        "clean": {
            "count": len(clean),
            "by_source_list": dict(Counter(m.source_list for m in clean)),
        },
    }

    # Write split files
    def write_split(name, items):
        path = SPLITS_DIR / f"{name}.json"
        data = [
            {
                "hash": h,
                "entry_id": m.entry_id,
                "entry_name": m.entry_name,
                "source_list": m.source_list,
                "severity": m.severity,
                "framework": m.framework,
                "control_id": m.control_id,
                "control_name": m.control_name,
                "tier": m.tier,
                "scope": m.scope,
                "notes": m.notes,
            }
            for h, m in items
        ]
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"Written {path} ({len(data)} mappings)")

    write_split("calibration", calibration)
    write_split("test", test)
    write_split("clean", [(mapping_hash(m), m) for m in clean])

    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Written {meta_path}")
    print(f"\nSplit summary:")
    print(f"  Calibration: {meta['calibration']['count']}")
    print(f"  Test:        {meta['test']['count']}")
    print(f"  Clean:       {meta['clean']['count']}")


if __name__ == "__main__":
    make_splits()
