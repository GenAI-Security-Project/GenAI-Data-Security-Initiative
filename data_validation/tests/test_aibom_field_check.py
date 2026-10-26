"""Tests for aibom_field_check.py, against the pinned AIBOM Generator field table."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import aibom_field_check as ab  # noqa: E402
from validators._common import DATASETS_ROOT, ERROR, iter_data_files  # noqa: E402

P = Path("entry.json")


def row(field, control_id="MAP 2.3"):
    return {"framework_alignments": [
        {"framework": "NIST AI RMF 1.0", "control_id": control_id, "alignment_status": "satisfied", "aibom_field": field},
    ]}


def test_rows_without_the_key_are_not_checked():
    assert ab.check_data(P, {"framework_alignments": [{"control_id": "PR.DS-05", "alignment_status": "satisfied"}]}) == []


@pytest.mark.parametrize("field", ["datasets", "metric", "safetyRiskAssessment", "bomFormat"])
def test_a_registry_field_passes(field):
    assert ab.check_data(P, row(field)) == []


def test_unknown_field_fails_with_a_suggestion():
    [f] = ab.check_data(P, row("dataset"))
    assert f.level == ERROR and "'dataset' is not a field" in f.message and "did you mean 'datasets'" in f.message
    assert f.location == "/framework_alignments/0/aibom_field"


def test_unknown_field_without_a_near_match_fails_without_a_suggestion():
    [f] = ab.check_data(P, row("zzzzzz"))
    assert f.level == ERROR and "did you mean" not in f.message


@pytest.mark.parametrize("field", ["paper", "vcs", "website"])
def test_a_field_the_generator_never_writes_fails(field):
    [f] = ab.check_data(P, row(field))
    assert f.level == ERROR and "never writes" in f.message


@pytest.mark.parametrize("value", [None, 3, ["datasets"], {"id": "datasets"}])
def test_a_non_string_value_fails(value):
    [f] = ab.check_data(P, row(value))
    assert f.level == ERROR and "expected a field id" in f.message


def test_every_cited_row_is_found_at_any_depth():
    data = {"a": row("datasets"), "b": [row("nope"), row("also-nope")]}
    assert [f.location for f in ab.check_data(P, data)] == [
        "/b/0/framework_alignments/0/aibom_field",
        "/b/1/framework_alignments/0/aibom_field",
    ]


def test_table_matches_the_registry_shape():
    fields = ab.generator_fields()
    assert len(fields) >= 50 and {"datasets", "metric", "safetyRiskAssessment"} <= set(fields)
    assert all(r["rule"] and r["tier"] and r["cyclonedx_path"] for r in fields.values())
    assert {k for k, r in fields.items() if r["cyclonedx_path"] == ab.NOT_WRITTEN} == {"paper", "vcs", "website"}


def test_every_keyed_row_in_the_datasets_passes():
    findings = []
    for path in iter_data_files(DATASETS_ROOT):
        findings += ab.check_data(path, json.loads(path.read_text(encoding="utf-8")))
    assert findings == []


def test_cli_on_a_file(tmp_path, capsys):
    path = tmp_path / "entry.json"
    path.write_text(json.dumps(row("paper")), encoding="utf-8")
    assert ab.main(["--file", str(path)]) == 1
    assert "never writes 'paper'" in capsys.readouterr().out
