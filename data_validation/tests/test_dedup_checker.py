"""Tests for dedup_checker.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import dedup_checker as dd  # noqa: E402
from validators._common import ERROR, WARN  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_near_duplicate_pair_flagged_paraphrase_not():
    records, errors = dd.load_records([FIXTURES / "duplicate_pair.json"])
    assert errors == [] and len(records) == 3
    findings = dd.check_records(records)
    assert [(f.level, f.message.split()[0]) for f in findings] == [(WARN, "INC-0011")]
    assert "INC-0010" in findings[0].message


def test_duplicate_id_is_an_error(tmp_path):
    for name, text in (("a.json", "one thing entirely"), ("b.json", "something else")):
        (tmp_path / name).write_text(json.dumps({"exploit_id": "AML.T0051", "description": text}))
    findings = dd.check_dataset(tmp_path)
    assert [f.level for f in findings] == [ERROR]


def test_example_json_is_skipped(tmp_path):
    entry = {"vulnerability_id": "CVE-2024-0001", "description": "x" * 50}
    (tmp_path / "example.json").write_text(json.dumps(entry))
    (tmp_path / "entries").mkdir()
    (tmp_path / "entries" / "CVE-2024-0001.json").write_text(json.dumps(entry))
    assert dd.check_dataset(tmp_path) == []


def test_shared_boilerplate_is_ignored(tmp_path):
    licence = "Adapted from a CC BY 4.0 source dataset; see the collection README for attribution."
    texts = ["alpha beta gamma delta epsilon", "zeta eta theta iota kappa",
             "lambda mu nu xi omicron", "pi rho sigma tau upsilon"]
    for i, t in enumerate(texts):
        (tmp_path / f"{i}.json").write_text(json.dumps({"id": f"T-{i}", "licence": licence, "prompt": t * 3}))
    assert dd.check_dataset(tmp_path) == []


def test_new_file_mode_only_reports_pairs_with_the_new_file(tmp_path):
    same = "the same long description of an issue that two old entries share by mistake"
    for i in range(2):
        (tmp_path / f"old{i}.json").write_text(json.dumps({"id": f"O-{i}", "description": same}))
    new = tmp_path / "new.json"
    new.write_text(json.dumps({"id": "N-1", "description": "an unrelated and entirely different description here"}))
    records, _ = dd.load_records(sorted(tmp_path.glob("*.json")))
    assert dd.check_records(records, new={new}) == []
    assert len(dd.check_records(records)) == 1
