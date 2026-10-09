"""Guards that keep schemas and validators on current standards.

They fail when a schema falls behind the reference tables, when a schema is
not JSON Schema 2020-12, or when a dataset validator stops enforcing
"format" (dates, URIs).
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import DATASETS_ROOT, REFERENCE_DIR, SCHEMAS_DIR  # noqa: E402

DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
# Contributor-maintained schema for one sub-collection; its own validator owns it.
CONTRIBUTOR_SCHEMAS = {"contrastive_testcase.schema.json"}

OWASP = list(csv.DictReader(open(REFERENCE_DIR / "owasp_top10.csv", newline="", encoding="utf-8")))
LLM_IDS = sorted(r["id"] for r in OWASP if r["list"] == "LLM")
ASI_IDS = sorted(r["id"] for r in OWASP if r["list"] == "ASI")
NIST_IDS = [r["id"] for r in csv.DictReader(open(REFERENCE_DIR / "nist_ai_100_2.csv", newline="", encoding="utf-8"))]
MAPPING_SCHEMAS = [DATASETS_ROOT / d / "schema.json"
                   for d in ("exploit_dataset", "vulnerability_dataset", "agentdataflow_toolexchange_traces")]


def all_schemas() -> list[Path]:
    found = list(SCHEMAS_DIR.glob("*.schema.json")) + list(DATASETS_ROOT.glob("*/schema.json"))
    found += [p for p in DATASETS_ROOT.rglob("*.schema.json") if "fixtures" not in p.parts]
    return sorted(set(found))


@pytest.mark.parametrize("path", all_schemas(), ids=lambda p: p.name if p.name != "schema.json" else p.parent.name)
def test_schema_is_valid_2020_12(path):
    if path.name in CONTRIBUTOR_SCHEMAS:
        pytest.skip("contributor-maintained sub-collection schema")
    schema = json.loads(path.read_text(encoding="utf-8"))
    assert schema.get("$schema") == DRAFT_2020_12
    if "$ref" not in schema:
        Draft202012Validator.check_schema(schema)


@pytest.mark.parametrize("path", MAPPING_SCHEMAS, ids=lambda p: p.parent.name)
def test_owasp_enums_match_reference_table(path):
    props = json.loads(path.read_text(encoding="utf-8"))["properties"]
    assert sorted(props["owasp_llm_top10_mapping"]["items"]["enum"]) == LLM_IDS
    assert sorted(props["owasp_agentic_top10_mapping"]["items"]["enum"]) == ASI_IDS
    assert props["nist_aml_mapping"]["items"]["enum"] == NIST_IDS


def test_owasp_table_is_complete_and_crosswalked():
    for edition in ("2025", "2026"):
        assert [r["id"] for r in OWASP if r["list"] == "LLM" and r["edition"] == edition] == \
            [f"LLM{n:02d}:{edition}" for n in range(1, 11)]
    assert ASI_IDS == [f"ASI{n:02d}:2026" for n in range(1, 11)]
    equivalents = [r["equivalent_2025"] for r in OWASP if r["edition"] == "2026" and r["list"] == "LLM"]
    assert sorted(equivalents) == [f"LLM{n:02d}:2025" for n in range(1, 11)]  # a one-to-one crosswalk


@pytest.mark.parametrize("validate", sorted(DATASETS_ROOT.glob("*/validate.py")), ids=lambda p: p.parent.name)
def test_dataset_validators_enforce_format(validate):
    """Without a format checker, "format": "date" and "uri" are never checked.

    A validator either builds its own (agentdataflow) or uses the shared core,
    which does."""
    source = validate.read_text(encoding="utf-8")
    uses_shared = "from validate_lib import" in source
    assert uses_shared or re.search(r"format_checker\s*=", source), f"{validate} has no format checker"
    if uses_shared:
        lib = (DATASETS_ROOT / "_shared" / "validate_lib.py").read_text(encoding="utf-8")
        assert re.search(r"format_checker\s*=", lib)


def test_nist_table_matches_the_publication():
    """The 30 NISTAML identifiers of NIST AI 100-2e2025, objectives first in each group."""
    assert len(NIST_IDS) == 30 == len(set(NIST_IDS))
    objectives = [i for i in NIST_IDS if len(i.split(".")[1]) == 2]
    assert objectives == ["NISTAML.01", "NISTAML.02", "NISTAML.03", "NISTAML.04", "NISTAML.05"]


def test_every_published_dataset_has_croissant_metadata():
    """A dataset folder with records needs a croissant.json (build_croissant.py makes it)."""
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "croissant"))
    from build_croissant import DATASETS
    with_records = {p.parent.name for p in DATASETS_ROOT.glob("*/*.json")} | \
                   {p.parents[1].name for p in DATASETS_ROOT.glob("*/entries/*.json")} | \
                   {p.parents[2].name for p in DATASETS_ROOT.glob("*/*/cases/*.json")}
    with_records -= {"_shared"}
    assert with_records <= set(DATASETS), f"no Croissant description for {sorted(with_records - set(DATASETS))}"
    for name in DATASETS:
        assert (DATASETS_ROOT / name / "croissant.json").is_file(), name


def test_citation_version_is_semver():
    text = (DATASETS_ROOT.parent / "CITATION.cff").read_text(encoding="utf-8")
    assert re.search(r'^version: "\d+\.\d+\.\d+"$', text, re.M)
