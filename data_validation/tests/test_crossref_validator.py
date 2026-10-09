"""Tests for crossref_validator.py."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import crossref_validator as cr  # noqa: E402
from validators._common import ERROR, WARN  # noqa: E402

P = Path("entry.json")


def levels(data) -> list[str]:
    return [f.level for f in cr.check_data(P, data)]


@pytest.mark.parametrize("value", [
    "CVE-2024-3568", "GHSA-jfh8-c2jp-5v3q", "CWE-79", "CWE-1426", "AML.T0051", "AML.T0051.001",
])
def test_well_formed_known_ids_pass(value):
    assert levels({"id": value}) == []


@pytest.mark.parametrize("value", ["CVE-24-1234", "CVE-2024-12", "GHSA-xxxx-yyyy", "CWE-abc", "AML.T51"])
def test_malformed_whole_value_is_an_error(value):
    assert levels({"id": value}) == [ERROR]


def test_future_cve_year():
    assert levels({"cve_id": f"CVE-{date.today().year + 1}-0001"}) == [ERROR]


def test_unknown_cwe_and_atlas():
    assert levels({"cwe_ids": ["CWE-999999"]}) == [ERROR]
    assert levels({"mitre_atlas_mapping": ["AML.T9999"]}) == [ERROR]


def test_deprecated_cwe_and_retired_atlas_warn():
    assert levels({"cwe_ids": ["CWE-1"]}) == [WARN]
    assert levels({"mitre_atlas_mapping": ["AML.T0019"]}) == [WARN]


def test_ids_in_free_text():
    assert levels({"notes": "Maps to AML.T0051 and CWE-79, see CVE-2024-3568."}) == []
    assert levels({"notes": "Like AML.T9999."}) == [ERROR]
    assert levels({"notes": "Placeholder CVE-XXXX-XXXX in a template."}) == [WARN]
    assert levels({"url": "https://atlas.mitre.org/techniques/AML.T0051"}) == []


def test_reference_tables_are_complete():
    assert len(cr.atlas_status()) > 150
    assert cr.atlas_status()["AML.T0051"] == "current"
    assert len(cr.cwe_status()) > 1000
    assert cr.cwe_status()["CWE-79"] != "Deprecated"


def test_owasp_ids():
    assert levels({"owasp_llm_top10_mapping": ["LLM03:2025", "LLM04:2026"]}) == []
    assert levels({"owasp_agentic_top10_mapping": ["ASI10:2026"]}) == []
    assert levels({"notes": "maps to LLM11:2026"}) == [ERROR]
    assert levels({"notes": "an old LLM01:2024 reference"}) == [ERROR]
    assert levels({"notes": "OWASP LLM03 (Supply Chain)"}) == [WARN]
