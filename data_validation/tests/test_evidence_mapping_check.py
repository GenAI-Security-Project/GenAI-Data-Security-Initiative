"""Tests for evidence_mapping_check.py, against the pinned agent-evidence-vectors corpora."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import evidence_mapping_check as em  # noqa: E402
from validators._common import ERROR, WARN  # noqa: E402

P = Path("entry.json")


def row(control_id="MCP03", status="satisfied", **records):
    cited = {"package": "agent-evidence-vectors", "corpus": "vectors-mcp-owasp", **records}
    return {"framework_alignments": [
        {"framework": "OWASP MCP Top 10", "control_id": control_id, "alignment_status": status, "test_records": cited},
    ]}


def test_rows_without_test_records_are_not_checked():
    assert em.check_data(P, {"framework_alignments": [{"control_id": "PR.DS-05", "alignment_status": "satisfied"}]}) == []


def test_cited_requirement_that_tests_the_control_passes():
    assert em.check_data(P, row(requirement="MCPVS-1")) == []


def test_requirement_that_tests_another_control_fails():
    [f] = em.check_data(P, row(control_id="MCP01", requirement="MCPVS-1"))
    assert f.level == ERROR and "MCPVS-1 tests MCP03, not MCP01" in f.message
    assert f.location == "/framework_alignments/0/test_records"


def test_unknown_requirement_fails():
    [f] = em.check_data(P, row(requirement="MCPVS-999"))
    assert f.level == ERROR and "not in the vectors-mcp-owasp registry" in f.message


def test_withdrawn_requirement_fails(monkeypatch):
    monkeypatch.setattr(em, "registry", lambda corpus: {"MCPVS-1": {"id": "MCPVS-1", "status": "withdrawn", "top10": ["MCP03"]}})
    [f] = em.check_data(P, row(requirement="MCPVS-1"))
    assert f.level == ERROR and "withdrawn" in f.message


def test_corpus_not_shipped_fails():
    data = row()
    data["framework_alignments"][0]["test_records"]["corpus"] = "vectors-does-not-exist"
    [f] = em.check_data(P, data)
    assert f.level == ERROR and "ships no corpus 'vectors-does-not-exist'" in f.message


def test_corpus_without_a_reference_reader_fails():
    # Shipped, but the package's reference verifier has no reader for it, so nothing is judged.
    data = row(control_id="DE.AE-02")
    data["framework_alignments"][0]["test_records"]["corpus"] = "vectors-delegation-lifecycle"
    [f] = em.check_data(P, data)
    assert f.level == ERROR and "does not replay clean" in f.message


def test_failing_replay_fails(monkeypatch):
    monkeypatch.setattr(em, "replay", lambda corpus: (False, "FAIL v0485d4e3a7045da5 reject"))
    [f] = em.check_data(P, row(requirement="MCPVS-1"))
    assert f.level == ERROR and "FAIL v0485d4e3a7045da5" in f.message


@pytest.mark.parametrize("status", ["missing", "not_applicable"])
def test_records_on_an_unsupported_row_warn(status):
    [f] = em.check_data(P, row(status=status, requirement="MCPVS-1"))
    assert f.level == WARN and status in f.message


@pytest.mark.parametrize("cited", [
    "vectors-mcp-owasp",
    {"corpus": "vectors-mcp-owasp"},
    {"package": "other-package", "corpus": "vectors-mcp-owasp"},
    {"package": "agent-evidence-vectors"},
])
def test_malformed_citation_fails(cited):
    [f] = em.check_data(P, {"framework_alignments": [{"control_id": "MCP03", "test_records": cited}]})
    assert f.level == ERROR and "expected" in f.message


def test_package_not_installed_fails(monkeypatch):
    monkeypatch.setattr(em, "package_version", lambda: None)
    [f] = em.check_data(P, row(requirement="MCPVS-1"))
    assert f.level == ERROR and "is not installed" in f.message


def test_each_corpus_replays_once():
    em.replay.cache_clear()
    em.check_data(P, {"a": row(requirement="MCPVS-1"), "b": row(requirement="MCPVS-2")})
    info = em.replay.cache_info()
    assert info.misses == 1 and info.hits == 1


def test_cli_on_a_file(tmp_path, capsys):
    import json

    path = tmp_path / "entry.json"
    path.write_text(json.dumps(row(control_id="MCP01", requirement="MCPVS-1")), encoding="utf-8")
    assert em.main(["--file", str(path)]) == 1
    assert "MCPVS-1 tests MCP03, not MCP01" in capsys.readouterr().out
