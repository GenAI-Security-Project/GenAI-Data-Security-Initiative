"""
Validates every datasets/*/croissant.json with mlcroissant and loads each
record set through it, checking the record count matches the CSV it reads.
A file that validates but cannot actually load its data fails here.

    python check_croissant.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

DATASETS_ROOT = Path(__file__).resolve().parents[2] / "datasets"


def main() -> int:
    import mlcroissant as mlc
    failures = 0
    files = sorted(DATASETS_ROOT.glob("*/croissant.json"))
    for path in files:
        meta = json.loads(path.read_text(encoding="utf-8"))
        try:
            dataset = mlc.Dataset(jsonld=str(path))
        except mlc.ValidationError as exc:
            print(f"FAIL  {path.parent.name}: {exc}")
            failures += 1
            continue
        for record_set in meta.get("recordSet", []):
            rs_id = record_set["@id"]
            file_id = record_set["field"][0]["source"]["fileObject"]["@id"]
            with open(path.parent / file_id, newline="", encoding="utf-8") as fh:
                expected = sum(1 for _ in csv.DictReader(fh))
            loaded = sum(1 for _ in dataset.records(record_set=rs_id))
            status = "PASS" if loaded == expected else "FAIL"
            failures += status == "FAIL"
            print(f"{status}  {path.parent.name}/{rs_id}: {loaded} record(s) loaded, {expected} expected")
        if not meta.get("recordSet"):
            print(f"PASS  {path.parent.name}: metadata valid (no record set)")
    print(f"{len(files)} Croissant file(s), {failures} failure(s)")
    return 1 if failures or not files else 0


if __name__ == "__main__":
    sys.exit(main())
