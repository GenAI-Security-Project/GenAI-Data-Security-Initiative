"""Tests for schema_validator.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import schema_validator  # noqa: E402
from validators._common import DATASETS_ROOT, ERROR, SCHEMAS_DIR, WARN  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
VULN_SCHEMA = DATASETS_ROOT / "vulnerability_dataset" / "schema.json"


def test_valid_vulnerability():
    assert schema_validator.validate_file(FIXTURES / "valid_vulnerability.json", VULN_SCHEMA) == []


def test_invalid_vulnerability():
    findings = schema_validator.validate_file(FIXTURES / "invalid_vulnerability.json", VULN_SCHEMA)
    messages = " ".join(f.message for f in findings)
    assert all(f.level == ERROR for f in findings)
    assert "'title' is a required property" in messages
    assert "not_a_valid_component" in messages


def test_valid_incident_against_fallback_schema():
    assert schema_validator.validate_file(FIXTURES / "valid_incident.json", SCHEMAS_DIR / "incident.schema.json") == []


def test_finds_schema_from_dollar_schema(tmp_path):
    (tmp_path / "schema.json").write_text(json.dumps({"type": "object", "required": ["x"]}))
    entries = tmp_path / "entries"
    entries.mkdir()
    entry = entries / "e.json"
    entry.write_text(json.dumps({"$schema": "../schema.json"}))
    findings = schema_validator.validate_file(entry, dataset_root=tmp_path)
    assert [f.message for f in findings] == ["'x' is a required property"]


def test_finds_nearest_schema_json(tmp_path):
    (tmp_path / "schema.json").write_text(json.dumps({"type": "object", "required": ["x"]}))
    sub = tmp_path / "entries"
    sub.mkdir()
    (sub / "e.json").write_text(json.dumps({"x": 1}))
    assert schema_validator.find_schema(sub / "e.json", {"x": 1}, tmp_path) == tmp_path / "schema.json"


def test_fallback_schema_for_rag_dataset():
    rag = DATASETS_ROOT / "rag_dataset"
    assert schema_validator.find_schema(rag / "entries" / "RAG-0001.json", {}, rag) == SCHEMAS_DIR / "rag.schema.json"


def test_missing_schema_is_an_error(tmp_path):
    entry = tmp_path / "e.json"
    entry.write_text(json.dumps({"$schema": "./nope.json"}))
    [finding] = schema_validator.validate_file(entry, dataset_root=tmp_path)
    assert finding.level == ERROR and "schema not found" in finding.message


def test_no_schema_is_a_warning(tmp_path):
    entry = tmp_path / "e.json"
    entry.write_text("{}")
    [finding] = schema_validator.validate_file(entry, dataset_root=tmp_path)
    assert finding.level == WARN


def test_relative_ref_between_schema_files(tmp_path):
    (tmp_path / "inner.json").write_text(json.dumps({"type": "object", "required": ["y"]}))
    (tmp_path / "outer.json").write_text(json.dumps({"$schema": "https://json-schema.org/draft/2020-12/schema",
                                                     "$ref": "inner.json"}))
    entry = tmp_path / "e.json"
    entry.write_text("{}")
    findings = schema_validator.validate_file(entry, tmp_path / "outer.json")
    assert [f.message for f in findings] == ["'y' is a required property"]


@pytest.mark.parametrize("example", sorted(DATASETS_ROOT.glob("*/example.json")), ids=lambda p: p.parent.name)
def test_dataset_examples_pass_their_schema(example):
    assert schema_validator.validate_file(example, dataset_root=example.parent) == []


@pytest.mark.parametrize("stub", ["exploit", "vulnerability", "riskassessment", "agentdataflow_trace"])
def test_superseded_stub_schemas_resolve_to_dataset_schema(stub):
    """data_validation/schemas/<stub>.schema.json $refs the dataset-local schema."""
    example = next(DATASETS_ROOT.glob(f"{stub.split('_')[0]}*/example.json"))
    assert schema_validator.validate_file(example, SCHEMAS_DIR / f"{stub}.schema.json") == []
