"""The incident dataset's disclosure rule (datasets/incident_dataset/schema.json) and INDEX.md builder."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

DATASET = Path(__file__).resolve().parents[2] / "datasets" / "incident_dataset"
SCHEMA = json.loads((DATASET / "schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=Draft202012Validator.FORMAT_CHECKER)

BASE = {
    "incident_id": "INC-0001",
    "title": "Chat history of other users shown after a caching bug",
    "date": "2023-03-20",
    "summary": "A caching bug in a hosted chatbot showed some users the titles of other users' conversations.",
    "dsgai_mapping": ["DSGAI11"],
    "attack_vector": "Software defect in a shared cache",
    "data_types_affected": ["pii"],
    "impact": "Conversation titles and some payment details of other users were exposed.",
}
PUBLIC = {**BASE, "disclosure": "public", "affected_organizations": ["Example Vendor Inc."],
          "source_urls": ["https://vendor.example/blog/incident-report"]}
ANONYMIZED = {**BASE, "disclosure": "anonymized", "source": "Anonymized self-report"}


def errors(entry: dict) -> list[str]:
    return [e.message for e in VALIDATOR.iter_errors(entry)]


def test_public_entry_may_name_the_affected_organization():
    assert errors(PUBLIC) == []


def test_anonymized_entry_without_names_is_valid():
    assert errors(ANONYMIZED) == []


def test_public_entry_requires_sources():
    entry = {k: v for k, v in PUBLIC.items() if k != "source_urls"}
    assert errors(entry) == ["'source_urls' is a required property"]


def test_anonymized_entry_cannot_name_organizations():
    assert errors({**ANONYMIZED, "affected_organizations": ["Example Vendor Inc."]})


def test_disclosure_is_required_and_closed():
    assert "'disclosure' is a required property" in errors(BASE)
    assert errors({**BASE, "disclosure": "partial"})


@pytest.mark.parametrize("field, value", [
    ("source_urls", ["not a url"]),
    ("source_urls", []),
    ("contributor", {"name": "Jane Doe", "affiliation": "Example Corp"}),
    ("vendor_link", "https://vendor.example"),
    ("precision", "week"),
])
def test_rejects_bad_or_unknown_fields(field, value):
    assert errors({**PUBLIC, field: value})


def load_build_index():
    spec = importlib.util.spec_from_file_location("incident_build_index", DATASET / "build_index.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_index_lists_entries_newest_first_with_escaped_cells():
    bi = load_build_index()
    older = {**ANONYMIZED, "incident_id": "INC-0002", "date": "2022-01-01", "precision": "year"}
    newer = {**PUBLIC, "title": "Leak | with a pipe", "crosswalk_id": "INC-006"}
    text = bi.render([older, newer])
    rows = [line for line in text.splitlines() if line.startswith("| [INC-")]
    assert [r.split("]")[0] for r in rows] == ["| [INC-0001", "| [INC-0002"]
    assert r"Leak \| with a pipe" in rows[0] and "Example Vendor Inc." in rows[0] and "INC-006" in rows[0]
    assert "| 2022 |" in rows[1] and "*anonymized*" in rows[1]
    assert "**2 incidents** (1 public, 1 anonymized)." in text


def test_committed_index_is_up_to_date():
    assert load_build_index().main(["--check"]) == 0
