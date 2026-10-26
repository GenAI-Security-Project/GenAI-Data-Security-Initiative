"""
Checks that a framework mapping row keyed on an AIBOM field names a field the
OWASP AIBOM Generator can actually write.

A row in framework_alignments (or any object with a "control_id") may carry

    "aibom_field": "datasets"

an id from the generator's src/models/field_registry.json. The row then says
which field of a generated CycloneDX AIBOM evidences the control. The ids come
from reference_data/aibom_fields.csv, a table regenerated from the registry at
a recorded commit (see reference_data/SOURCES.md). A row that no field
evidences carries instead

    "aibom_field_none": "deployment-control"

with one of the reasons in REASONS (defined in the dataset's schema.json).

ERROR: the value is not a string; the id is not in the registry; the registry
       lists the field with no CycloneDX location, so the generator never
       writes it into the BOM; the reason is not one of REASONS; the row
       carries both keys.
The inclusion rule and tier are not judged: a field written only
"include_if_available" is still a valid key, because the generator emits it
whenever the model's source has the data.

Usage:
    python aibom_field_check.py --file ../../datasets/riskassessment_dataset/entries/X.json
    python aibom_field_check.py                # every dataset
"""
from __future__ import annotations

import argparse
import csv
import difflib
import sys
from functools import cache
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT,
    ERROR,
    REFERENCE_DIR,
    Finding,
    add_target_args,
    ensure_utf8_stdout,
    load_json,
    print_findings,
    resolve_targets,
)

CHECK = "aibom"
KEY = "aibom_field"
NONE_KEY = "aibom_field_none"
REASONS = ("deployment-control", "runtime-behaviour", "no-registry-field")
TABLE = "aibom_fields.csv"
NOT_WRITTEN = "none"


@cache
def generator_fields() -> dict[str, dict[str, str]]:
    """Field id to its registry row (cyclonedx_path, rule, tier, description)."""
    with open(REFERENCE_DIR / TABLE, newline="", encoding="utf-8") as fh:
        return {row["field_id"]: row for row in csv.DictReader(fh)}


def iter_keyed_rows(obj: Any, pointer: str = ""):
    """(pointer, row) for every object that carries aibom_field or aibom_field_none."""
    if isinstance(obj, dict):
        if KEY in obj or NONE_KEY in obj:
            yield pointer, obj
        for k, v in obj.items():
            yield from iter_keyed_rows(v, f"{pointer}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_keyed_rows(v, f"{pointer}/{i}")


def check_reason(path: Path, pointer: str, row: dict) -> list[Finding]:
    reason = row[NONE_KEY]
    if reason in REASONS:
        return []
    allowed = ", ".join(REASONS)
    return [Finding(ERROR, CHECK, path, f"{pointer}/{NONE_KEY}", f"{reason!r} is not a reason; expected one of {allowed}")]


def check_row(path: Path, pointer: str, row: dict) -> list[Finding]:
    if KEY in row and NONE_KEY in row:
        return [Finding(ERROR, CHECK, path, pointer, f"the row carries both {KEY} and {NONE_KEY}; keep one")]
    if NONE_KEY in row:
        return check_reason(path, pointer, row)
    where = f"{pointer}/{KEY}"
    field = row[KEY]
    if not isinstance(field, str):
        return [Finding(ERROR, CHECK, path, where, "expected a field id from the AIBOM Generator's field_registry.json")]
    fields = generator_fields()
    entry = fields.get(field)
    if entry is None:
        near = difflib.get_close_matches(field, fields, n=1)
        hint = f"; did you mean {near[0]!r}?" if near else ""
        return [Finding(ERROR, CHECK, path, where, f"{field!r} is not a field in the AIBOM Generator's field_registry.json{hint}")]
    if entry["cyclonedx_path"] == NOT_WRITTEN:
        message = f"the generator never writes {field!r} to its CycloneDX output (no location in the registry)"
        return [Finding(ERROR, CHECK, path, where, message)]
    return []


def check_data(path: Path, data: Any) -> list[Finding]:
    return [f for pointer, row in iter_keyed_rows(data) for f in check_row(path, pointer, row)]


def check_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check mapping rows keyed on AIBOM Generator field ids")
    add_target_args(parser)
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    findings = [f for p in files for f in check_file(p)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
