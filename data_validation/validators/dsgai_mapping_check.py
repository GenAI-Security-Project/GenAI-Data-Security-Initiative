"""
Verifies DSGAI ID references against datasets/_shared/dsgai_taxonomy.json.

ERROR: a DSGAI ID that is not in the taxonomy, wherever it appears (a
       mapping field or free text), or a dsgai_mapping value that is not a
       DSGAI ID at all.
WARN:  the same ID listed twice in one mapping, or a mapping with more IDs
       than MAX_MAPPINGS (usually a sign the entry was mapped to everything
       that looked related rather than to the risks it actually shows).

Whether a mapping is the right one is a reviewer judgment; this only catches
what can be checked mechanically.

Usage:
    python dsgai_mapping_check.py --file ../../datasets/rag_dataset/entries/RAG-0001.json
    python dsgai_mapping_check.py                # every dataset
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT,
    ERROR,
    WARN,
    Finding,
    add_target_args,
    ensure_utf8_stdout,
    iter_records,
    load_json,
    load_taxonomy_ids,
    print_findings,
    resolve_targets,
    walk_strings,
)

CHECK = "dsgai"
# DSGAI followed directly by digits. Slugs such as DSGAI-VULN-... do not match.
DSGAI_TOKEN_RE = re.compile(r"\bDSGAI(\d+)\b")
# Keys whose values must each be exactly one DSGAI ID.
MAPPING_KEYS = {"dsgai_mapping", "dsgai_id", "addresses_dsgai"}
# Keys that say which risks a record shows (addresses_dsgai is a control's
# coverage, not a risk the record shows). Used by the QC reports.
RISK_KEYS = {"dsgai_mapping", "dsgai_id"}
MAX_MAPPINGS = 6


def record_dsgai_ids(record) -> set[str]:
    """DSGAI IDs a record maps to, wherever in it they are listed."""
    return {v.strip() for _p, k, v in walk_strings(record) if k in RISK_KEYS}


def check_data(path: Path, data, valid_ids: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for pointer, key, value in walk_strings(data):
        if key in MAPPING_KEYS and not DSGAI_TOKEN_RE.fullmatch(value.strip()):
            findings.append(Finding(ERROR, CHECK, path, pointer, f"{value!r} is not a DSGAI ID (expected DSGAI01-DSGAI21)"))
            continue
        for m in DSGAI_TOKEN_RE.finditer(value):
            if m.group(0) not in valid_ids:
                findings.append(Finding(ERROR, CHECK, path, pointer, f"{m.group(0)} is not in the DSGAI taxonomy"))
    for pointer, record in iter_records(data):
        mapping = record.get("dsgai_mapping")
        if not isinstance(mapping, list):
            continue
        seen = set()
        for value in mapping:
            if value in seen:
                findings.append(Finding(WARN, CHECK, path, f"{pointer}/dsgai_mapping", f"{value} is listed more than once"))
            seen.add(value)
        if len(seen) > MAX_MAPPINGS:
            findings.append(Finding(WARN, CHECK, path, f"{pointer}/dsgai_mapping",
                                    f"maps to {len(seen)} DSGAI entries; check each is a risk the entry actually shows"))
    return findings


def check_file(path: Path, valid_ids: set[str] | None = None) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data, valid_ids if valid_ids is not None else load_taxonomy_ids())


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Verify DSGAI ID references")
    add_target_args(parser)
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    valid = load_taxonomy_ids()
    findings = [f for p in files for f in check_file(p, valid)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
