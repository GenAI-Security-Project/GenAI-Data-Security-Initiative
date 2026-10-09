"""Tests for dsgai_mapping_check.py and the DSGAI reference lists."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import dsgai_mapping_check as dm  # noqa: E402
from validators._common import ERROR, REFERENCE_DIR, TAXONOMY_PATH, WARN, load_taxonomy_ids  # noqa: E402

VALID = load_taxonomy_ids()
P = Path("entry.json")


def check(data):
    return dm.check_data(P, data, VALID)


def test_valid_mapping():
    assert check({"dsgai_mapping": [f"DSGAI{n:02d}" for n in range(1, 7)]}) == []


def test_invalid_dsgai_id():
    [f] = check({"dsgai_mapping": ["DSGAI01", "DSGAI99"]})
    assert f.level == ERROR and "DSGAI99" in f.message and f.location == "/dsgai_mapping/1"


def test_unknown_id_in_free_text():
    [f] = check({"notes": "Related to DSGAI22."})
    assert f.level == ERROR and "DSGAI22" in f.message


def test_mapping_value_must_be_an_id():
    [f] = check({"risks": [{"dsgai_id": "Sensitive Data Leakage"}]})
    assert f.level == ERROR and f.location == "/risks/0/dsgai_id"


def test_internal_slugs_are_not_dsgai_ids():
    assert check({"related": ["DSGAI-VULN-2024-x", "DSGAI-EXP-y"]}) == []


def test_duplicate_and_overlong_mappings_warn():
    findings = check({"dsgai_mapping": ["DSGAI01", "DSGAI01"]})
    assert [f.level for f in findings] == [WARN]
    findings = check({"dsgai_mapping": [f"DSGAI{n:02d}" for n in range(1, 9)]})
    assert [f.level for f in findings] == [WARN]


def test_record_dsgai_ids_reads_nested_risks():
    record = {"dsgai_mapping": ["DSGAI01"], "risks_identified": [{"dsgai_id": "DSGAI14"}],
              "existing_controls": [{"addresses_dsgai": ["DSGAI02"]}]}
    assert dm.record_dsgai_ids(record) == {"DSGAI01", "DSGAI14"}


def test_reference_lists_agree():
    """dsgai_entries.json (read by the Turkish validator) matches the shared taxonomy."""
    shared = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))["entries"]
    legacy = json.loads((REFERENCE_DIR / "dsgai_entries.json").read_text(encoding="utf-8"))
    assert [(e["id"], e["name"]) for e in shared] == [(e["id"], e["name"]) for e in legacy]
    assert [e["id"] for e in shared] == [f"DSGAI{n:02d}" for n in range(1, 22)]
