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
RULES_SCHEMA = os.path.join(SCANNER, "rules", "rules.schema.json")
SCAN_SCHEMA = os.path.join(SCANNER, "schemas", "dsgai-scan.schema.json")
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
        # rg exit codes: 0 match, 1 no match, >=2 error (incl. any regex/PCRE2
        # compile failure — the message differs between engines, so key on the
        # exit code, not a substring).
        if p.returncode >= 2:
            bad.append((r["id"], p.stderr.strip()[:120]))
    assert not bad, f"PCREs failed to compile: {bad}"


@requires_rg
def test_compile_check_catches_a_broken_pattern():
    """Guard the guard: a deliberately invalid PCRE must be detected, so a
    corrupted rule really does fail CI."""
    rg = _rg()
    p = subprocess.run([rg, "--pcre2", "-q", "-e", "(unterminated[class"],
                       input="x\n", capture_output=True, text=True)
    assert p.returncode >= 2


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


@requires_rg
def test_checkpoint_validates_against_schema(scan):
    jsonschema = pytest.importorskip("jsonschema")
    schema = json.loads(open(SCAN_SCHEMA, encoding="utf-8").read())
    jsonschema.validate(scan["json"], schema)


def test_scan_schema_rejects_match_text():
    """The redaction guarantee is machine-checkable: a finding carrying match
    content must be rejected by the checkpoint schema."""
    jsonschema = pytest.importorskip("jsonschema")
    schema = json.loads(open(SCAN_SCHEMA, encoding="utf-8").read())
    bad = {
        "schema_version": "1.0", "ruleset_version": "0.3.0", "skill_version": "0.3.0",
        "framework": "dsgai-2026-v1.0", "engine": "deterministic-cli",
        "git_commit": None, "scanned_at": "2023-11-14T22:13:20+00:00",
        "scan_scope": ".", "obfuscation": "strict", "controls": {},
        "findings": [{
            "control": "DSGAI02", "rule_id": "P02.1", "path": "config.py",
            "line": 7, "status": "fail", "classification": "value_bearing",
            "match_text": "sk-proj-LEAKED",
        }],
        "cves": [], "file_map_ref": None,
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, schema)


def test_rules_validate_against_schema():
    jsonschema = pytest.importorskip("jsonschema")
    rules = yaml.safe_load(open(RULES_YAML, encoding="utf-8"))
    schema = json.loads(open(RULES_SCHEMA, encoding="utf-8").read())
    jsonschema.validate(rules, schema)


def test_cli_self_guard_rejects_leaked_finding():
    """The CLI's runtime (stdlib) self-check must refuse to write a checkpoint
    whose finding carries match content — independent of jsonschema."""
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_scan
    cp = {k: v for k, v in zip(dsgai_scan.CHECKPOINT_REQUIRED,
                               [None] * len(dsgai_scan.CHECKPOINT_REQUIRED))}
    cp["findings"] = [{"rule_id": "P02.1", "path": "x", "match_text": "sk-LEAK"}]
    with pytest.raises(ValueError):
        dsgai_scan.self_validate_checkpoint(cp)


def test_rules_json_in_sync():
    from_yaml = yaml.safe_load(open(RULES_YAML, encoding="utf-8"))
    rebuilt = json.dumps(from_yaml, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    current = open(RULES_JSON, encoding="utf-8").read()
    assert current == rebuilt, "rules/dsgai-rules.json is stale; run build/build_rules_json.py"
