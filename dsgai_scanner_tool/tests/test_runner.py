"""Self-test for the DSGAI deterministic runner.

Covers PR-05 acceptance:
  (a) every rule's PCRE compiles under `rg --pcre2`
  (b) a full fixture scan matches expected-findings.yaml exactly, incl.
      must_not_flag and known_bug bookkeeping
  (c) SARIF output is structurally valid 2.1.0
  (d) findings carry no match content (value-bearing redaction guarantee)
Plus: the CLI source always passes --replace for value-bearing rules, and the
compiled JSON stays in sync with the YAML source.
"""
import json
import os
import shutil
import subprocess
import sys

import pytest
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCANNER = os.path.dirname(HERE)
CLI = os.path.join(SCANNER, "cli", "dsgai_scan.py")
FIXTURE = os.path.join(HERE, "fixtures", "vulnerable-app")
SHEET = os.path.join(HERE, "expected-findings.yaml")
RULES_YAML = os.path.join(SCANNER, "rules", "dsgai-rules.yaml")
RULES_JSON = os.path.join(SCANNER, "rules", "dsgai-rules.json")
BANNED_FIELDS = {"match_text", "content", "value", "raw_grep_output"}


def _rg():
    return os.environ.get("DSGAI_RG") or shutil.which("rg") or shutil.which("rg.exe")


requires_rg = pytest.mark.skipif(_rg() is None, reason="ripgrep (rg) not installed")


@pytest.fixture(scope="module")
def sheet():
    with open(SHEET, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@pytest.fixture(scope="module")
def scan(tmp_path_factory):
    out = tmp_path_factory.mktemp("scan")
    jpath = out / "DSGAI-scan.json"
    spath = out / "scan.sarif"
    env = dict(os.environ, SOURCE_DATE_EPOCH="1700000000")
    proc = subprocess.run(
        [sys.executable, CLI, "scan", FIXTURE, "--json-out", str(jpath),
         "--sarif", str(spath), "--format", "none"],
        capture_output=True, text=True, env=env)
    assert proc.returncode in (0, 1), proc.stderr
    return {"json": json.loads(jpath.read_text(encoding="utf-8")),
            "sarif": json.loads(spath.read_text(encoding="utf-8"))}


def _rules():
    return json.loads(open(RULES_JSON, encoding="utf-8").read())["rules"]


@requires_rg
def test_all_pcres_compile():
    rg = _rg()
    bad = []
    for r in _rules():
        p = subprocess.run([rg, "--pcre2", "-q", "-e", r["pcre"]],
                           input="x\n", capture_output=True, text=True)
        if p.returncode >= 2 and "regex parse error" in p.stderr:
            bad.append(r["id"])
    assert not bad, f"PCREs failed to compile: {bad}"


@requires_rg
def test_scan_matches_sheet_exactly(scan, sheet):
    def key(f):
        return (f["control"], f["rule_id"], f["path"], f["line"], f["status"])
    scanned = {key(f) for f in scan["json"]["findings"]}
    expected = {key(f) for f in sheet["findings"]}
    assert scanned == expected, (
        f"missing={sorted(expected - scanned)} extra={sorted(scanned - expected)}")


@requires_rg
def test_must_not_flag(scan, sheet):
    produced = {(f["rule_id"], f["path"]) for f in scan["json"]["findings"]
                if f["status"] in ("fail", "warn")}
    for neg in sheet.get("must_not_flag", []):
        if neg.get("pending_until"):
            continue  # known_bug still present until that PR
        assert (neg["rule_id"], neg["path"]) not in produced, neg


@requires_rg
def test_known_bugs_are_tracked(scan, sheet):
    # Every known_bug in the sheet must currently be produced (baseline behavior).
    def key(f):
        return (f["rule_id"], f["path"], f["line"])
    produced = {key(f) for f in scan["json"]["findings"]}
    for f in sheet["findings"]:
        if f.get("known_bug"):
            assert key(f) in produced, f"known_bug no longer produced: {f}"


@requires_rg
def test_no_match_content_in_findings(scan):
    for f in scan["json"]["findings"]:
        assert not (BANNED_FIELDS & set(f)), f"finding leaks content: {f}"
    # value-bearing findings exist and are still content-free
    vb = [f for f in scan["json"]["findings"] if f["classification"] == "value_bearing"]
    assert vb, "expected at least one value-bearing finding in the fixture"


@requires_rg
def test_no_secret_substring_in_outputs(scan):
    blob = json.dumps(scan["json"]) + json.dumps(scan["sarif"])
    assert "FAKE" not in blob, "a fixture fake-secret substring leaked into output"


@requires_rg
def test_sarif_structure(scan):
    s = scan["sarif"]
    assert s["version"] == "2.1.0"
    run = s["runs"][0]
    driver = run["tool"]["driver"]
    assert driver["name"] == "dsgai-scan"
    assert len(driver["rules"]) == len(_rules())
    for res in run["results"]:
        assert res["ruleId"]
        assert res["level"] in ("error", "warning", "note")
        loc = res["locations"][0]["physicalLocation"]
        assert loc["artifactLocation"]["uri"]
        assert loc["region"]["startLine"] >= 1


def test_value_bearing_execution_always_replaces():
    """Source-level guard: value-bearing rules must run in location-only mode."""
    src = open(CLI, encoding="utf-8").read()
    # the value_bearing branch in run_rule must add --replace ''
    assert '"--replace", ""' in src or "'--replace', ''" in src
    idx = src.index('classification"] == "value_bearing"')
    window = src[idx:idx + 200]
    assert "--replace" in window, "value-bearing branch does not pass --replace"


def test_rules_json_in_sync():
    from_yaml = yaml.safe_load(open(RULES_YAML, encoding="utf-8"))
    rebuilt = json.dumps(from_yaml, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    current = open(RULES_JSON, encoding="utf-8").read()
    assert current == rebuilt, "rules/dsgai-rules.json is stale; run build/build_rules_json.py"
