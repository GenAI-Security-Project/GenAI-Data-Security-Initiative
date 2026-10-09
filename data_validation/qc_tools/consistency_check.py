"""
Cross-validates references between datasets.

ERROR: a record cites one of the initiative's own IDs (DSGAI-VULN-...,
       DSGAI-EXP-..., DSGAI-RA-...) that no record in the matching dataset
       has. These are internal links, so a dangling one is always a mistake:
       a typo, or a renamed or removed entry.

Also printed, as a note rather than a finding: how many CVE IDs cited by
exploit entries have no vulnerability entry of their own. The vulnerability
dataset is not meant to hold every CVE, so this is a list of candidates for
new entries, not an error.

Usage:
    python consistency_check.py
    python consistency_check.py --datasets ../../datasets/
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, Finding, ensure_utf8_stdout, load_dataset_records,
    print_findings, record_id, walk_strings,
)

CHECK = "consistency"
INTERNAL_ID_RE = re.compile(r"DSGAI-(VULN|EXP|RA)-[A-Za-z0-9._-]+")
TARGET_DATASET = {"VULN": "vulnerability_dataset", "EXP": "exploit_dataset", "RA": "riskassessment_dataset"}
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,}")


def check(datasets_root: Path = DATASETS_ROOT) -> tuple[list[Finding], list[str]]:
    """(findings, CVE IDs cited by exploits that have no vulnerability entry)."""
    records = load_dataset_records(datasets_root)
    ids = {name: {record_id(r) for _p, r in items} for name, items in records.items()}
    findings: list[Finding] = []
    for name, items in records.items():
        for path, rec in items:
            own = record_id(rec)
            for pointer, _key, value in walk_strings(rec):
                m = INTERNAL_ID_RE.fullmatch(value.strip())
                if not m or value.strip() == own:
                    continue
                target = TARGET_DATASET[m.group(1)]
                if value.strip() not in ids.get(target, set()):
                    findings.append(Finding(ERROR, CHECK, path, pointer,
                                            f"{value.strip()} is not an entry in {target}"))
    vuln_ids = ids.get("vulnerability_dataset", set())
    missing = sorted({
        v.strip()
        for _p, rec in records.get("exploit_dataset", [])
        for _ptr, key, v in walk_strings(rec)
        if key == "related_vulnerabilities" and CVE_RE.fullmatch(v.strip()) and v.strip() not in vuln_ids
    })
    return findings, missing


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check cross-dataset references")
    parser.add_argument("--datasets", default=str(DATASETS_ROOT), help="Root datasets directory")
    args = parser.parse_args(argv)
    root = Path(args.datasets)
    if not root.is_dir():
        print(f"Directory not found: {args.datasets}")
        return 2
    findings, missing = check(root.resolve())
    if missing:
        print(f"Note: {len(missing)} CVE(s) cited by exploit entries have no vulnerability entry: {', '.join(missing)}")
    return print_findings(findings, root.resolve().parent)


if __name__ == "__main__":
    sys.exit(main())
