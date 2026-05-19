"""Validate every entry in ./entries/ against ./schema.json.

Usage: python validate.py
Exit code 0 on success, 1 on any validation failure.
Requires: jsonschema (pip install jsonschema)
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
SCHEMA_PATH = ROOT / "schema.json"
ENTRIES_DIR = ROOT / "entries"
TAXONOMY_PATH = ROOT.parent / "_shared" / "dsgai_taxonomy.json"


def load_taxonomy_ids() -> set[str]:
    if not TAXONOMY_PATH.exists():
        return set()
    data = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    return {e["id"] for e in data.get("entries", [])}


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    taxonomy_ids = load_taxonomy_ids()

    errors: list[str] = []
    entry_files = sorted(ENTRIES_DIR.glob("*.json"))
    if not entry_files:
        sys.stderr.write(f"No entries found in {ENTRIES_DIR}\n")
        return 1

    for path in entry_files:
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON — {e}")
            continue

        for err in validator.iter_errors(entry):
            loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
            errors.append(f"{path.name}: {loc}: {err.message}")

        if taxonomy_ids:
            seen_dsgai: set[str] = set()
            for risk in entry.get("risks_identified", []):
                seen_dsgai.add(risk.get("dsgai_id", ""))
                if risk.get("dsgai_id") not in taxonomy_ids:
                    errors.append(
                        f"{path.name}: risks_identified.dsgai_id "
                        f"{risk.get('dsgai_id')!r} not in taxonomy"
                    )

            for control in entry.get("existing_controls", []):
                for did in control.get("addresses_dsgai", []) or []:
                    if did not in taxonomy_ids:
                        errors.append(
                            f"{path.name}: existing_controls.addresses_dsgai "
                            f"{did!r} not in taxonomy"
                        )
            for gap in entry.get("control_gaps", []):
                for did in gap.get("addresses_dsgai", []) or []:
                    if did not in taxonomy_ids:
                        errors.append(
                            f"{path.name}: control_gaps.addresses_dsgai "
                            f"{did!r} not in taxonomy"
                        )

    if errors:
        for line in errors:
            print(line)
        print(f"\nFAIL: {len(errors)} issue(s) across {len(entry_files)} entries.")
        return 1

    print(f"OK: {len(entry_files)} entries validated against schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
