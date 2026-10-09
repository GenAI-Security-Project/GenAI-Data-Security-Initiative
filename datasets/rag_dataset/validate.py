"""Validate every entry in ./entries/ against the RAG schema.

Usage: python validate.py
Exit code 0 on success (including when there are no entries yet), 1 on any
validation failure, 2 when jsonschema is missing.
Requires: jsonschema (pip install jsonschema)

The schema is data_validation/schemas/rag.schema.json, the only schema for
this dataset. Beyond the schema this checks that document_id matches the
file name, that no two entries share a document_id, and that every
dsgai_mapping value is in datasets/_shared/dsgai_taxonomy.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write("jsonschema not installed. Run: pip install jsonschema\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT.parent.parent / "data_validation" / "schemas" / "rag.schema.json"
ENTRIES_DIR = ROOT / "entries"
TAXONOMY_PATH = ROOT.parent / "_shared" / "dsgai_taxonomy.json"
ID_FIELD = "document_id"


def load_taxonomy_ids() -> set[str]:
    data = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    return {e["id"] for e in data.get("entries", [])}


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    taxonomy_ids = load_taxonomy_ids()

    entry_files = sorted(ENTRIES_DIR.glob("*.json")) if ENTRIES_DIR.is_dir() else []
    if not entry_files:
        print(f"OK: no entries yet in {ENTRIES_DIR.name}/.")
        return 0

    errors: list[str] = []
    seen: dict[str, str] = {}
    for path in entry_files:
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON — {e}")
            continue

        for err in validator.iter_errors(entry):
            loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
            errors.append(f"{path.name}: {loc}: {err.message}")

        for dsgai_id in entry.get("dsgai_mapping", []):
            if dsgai_id not in taxonomy_ids:
                errors.append(f"{path.name}: dsgai_mapping {dsgai_id!r} not in taxonomy")

        entry_id = entry.get(ID_FIELD)
        if isinstance(entry_id, str):
            if entry_id != path.stem:
                errors.append(f"{path.name}: {ID_FIELD} {entry_id!r} does not match the file name")
            if entry_id in seen:
                errors.append(f"{path.name}: {ID_FIELD} {entry_id!r} is also used by {seen[entry_id]}")
            seen.setdefault(entry_id, path.name)

    if errors:
        for line in errors:
            print(line)
        print(f"\nFAIL: {len(errors)} issue(s) across {len(entry_files)} entries.")
        return 1

    print(f"OK: {len(entry_files)} entries validated against schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
