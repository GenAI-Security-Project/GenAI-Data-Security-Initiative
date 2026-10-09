"""
Checks the dates in every record make sense.

ERROR: a date field (date_added, date_documented, date_reported,
       date_observed, updated_at, timestamp, or any key starting with
       "date") that is not an ISO 8601 date or date-time; a date in the
       future; a record documented, reported or observed after it was added.
       A value that is wholly a placeholder (<synthetic:iso8601>) is exempt.

Runs offline. Schemas declare most of these as "format": "date", but a
schema cannot compare two fields or know today's date.

Usage:
    python date_check.py --dataset ../../datasets/vulnerability_dataset/
    python date_check.py                        # every dataset
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, Finding, add_target_args, ensure_utf8_stdout,
    iter_records, load_json, print_findings, resolve_targets, walk_strings,
)

CHECK = "dates"
DATE_KEY_RE = re.compile(r"^(date($|_)|.*_date$|updated_at$|created_at$|timestamp$)")
# A value that is entirely a placeholder such as <synthetic:iso8601> is exempt,
# as in the agentdataflow traces' synthetic payloads.
PLACEHOLDER_RE = re.compile(r"^<[^<>]+>$")
# Fields that describe something that happened before the entry was added.
BEFORE_ADDED = ("date_documented", "date_reported", "date_observed")


def parse_date(value: str) -> date | None:
    """The calendar date of an ISO 8601 date or date-time, or None."""
    text = value.strip()
    try:
        if len(text) == 10:
            return date.fromisoformat(text)
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def check_data(path: Path, data, today: date | None = None) -> list[Finding]:
    # One day of slack: an entry written today in UTC+14 is still "today".
    latest = (today or datetime.now(timezone.utc).date()) + timedelta(days=1)
    findings: list[Finding] = []
    for pointer, key, value in walk_strings(data):
        if key is None or not DATE_KEY_RE.match(key) or PLACEHOLDER_RE.match(value.strip()):
            continue
        parsed = parse_date(value)
        if parsed is None:
            findings.append(Finding(ERROR, CHECK, path, pointer, f"{value!r} is not an ISO 8601 date"))
        elif parsed > latest:
            findings.append(Finding(ERROR, CHECK, path, pointer, f"{value} is in the future"))
    for pointer, record in iter_records(data):
        added = parse_date(record["date_added"]) if isinstance(record.get("date_added"), str) else None
        if added is None:
            continue
        for key in BEFORE_ADDED:
            value = record.get(key)
            when = parse_date(value) if isinstance(value, str) else None
            if when is not None and when > added:
                findings.append(Finding(ERROR, CHECK, path, f"{pointer}/{key}",
                                        f"{key} {value} is after date_added {record['date_added']}"))
    return findings


def check_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check dates are valid, not in the future, and in order")
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
