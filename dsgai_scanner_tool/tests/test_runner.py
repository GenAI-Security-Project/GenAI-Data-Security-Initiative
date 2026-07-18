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
         "--sarif", str(spath), "--format", "none", "--no-cve"],  # deterministic (no network)
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


def _import_cli():
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_scan
    return dsgai_scan


def test_suppression_suppresses_exactly_one(tmp_path):
    ds = _import_cli()
    f = tmp_path / "x.py"
    f.write_text(
        'A = "sk-proj-FAKE00000000000000000000000000"  # dsgai-ignore: P02.9 reason="known test value"\n'
        'B = "sk-proj-FAKE11111111111111111111111111"\n', encoding="utf-8")
    files = [(str(f), "x.py")]
    supp = ds.load_suppressions(files)
    findings = [
        {"control": "DSGAI02", "rule_id": "P02.9", "path": "x.py", "line": 1, "status": "fail"},
        {"control": "DSGAI02", "rule_id": "P02.9", "path": "x.py", "line": 2, "status": "fail"},
    ]
    active, suppressed = ds.split_suppressed(findings, supp)
    assert len(suppressed) == 1 and len(active) == 1
    assert suppressed[0]["suppressed_reason"] == "known test value"


def test_baseline_gating():
    ds = _import_cli()
    known = {"control": "DSGAI02", "rule_id": "P02.1", "path": "a.py", "line": 7, "status": "fail"}
    fresh = {"control": "DSGAI04", "rule_id": "P04.1", "path": "b.py", "line": 1, "status": "fail"}
    baseline = {ds.finding_fp(known)}
    assert ds.finding_fp(known) in baseline      # known finding is baselined
    assert ds.finding_fp(fresh) not in baseline  # a new finding gates


@pytest.mark.skipif(not os.environ.get("DSGAI_CVE_LIVE"),
                    reason="set DSGAI_CVE_LIVE=1 to run the live OSV CVE test")
def test_cve_langchain_exploitable(tmp_path):
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_cve
    req = tmp_path / "requirements.txt"
    req.write_text("langchain==0.1.0\n", encoding="utf-8")
    disc = [(str(req), "requirements.txt")]
    cves = dsgai_cve.enrich(disc, refresh=True)
    if not cves:
        pytest.skip("OSV unreachable")
    assert any(c["status"] == "EXPLOITABLE" for c in cves)
    assert dsgai_cve.enrich(disc, offline=True) == cves  # cache → deterministic


@requires_rg
def test_report_renders_without_leaking(scan, tmp_path):
    """Golden structural test: the rendered report has the required sections,
    uses file IDs in STRICT mode, and contains no fixture secret substring."""
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_report
    cp_path = tmp_path / "cp.json"
    cp_path.write_text(json.dumps(scan["json"]), encoding="utf-8")
    out = tmp_path / "r.html"
    dsgai_report.main([str(cp_path), "--out", str(out),
                       "--filemap", str(tmp_path / "fm.json")])
    html_out = out.read_text(encoding="utf-8")
    for anchor in ("Compliance dashboard", "Findings", "CVE advisories",
                   "Residual risk", "Guilherme"):
        assert anchor in html_out, f"missing report section: {anchor}"
    assert "FAKE" not in html_out, "report leaked a fixture secret"
    # STRICT mode → file IDs, not raw fixture paths
    assert "F0" in html_out and "system_prompt.py" not in html_out


def test_prompt_variant_in_sync():
    import subprocess
    r = subprocess.run([sys.executable,
                        os.path.join(SCANNER, "build", "generate_prompt_variant.py"),
                        "--check"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_semgrep_pack_in_sync():
    r = subprocess.run([sys.executable,
                        os.path.join(SCANNER, "build", "export_semgrep.py"), "--check"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_cve_multi_ecosystem_parse(tmp_path):
    """Offline: manifest parsing recognises every supported ecosystem, including
    go.mod / package-lock.json (audit H2) and awkward .csproj layouts."""
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_cve
    (tmp_path / "Cargo.lock").write_text(
        '[[package]]\nname = "async-openai"\nversion = "0.18.0"\n', encoding="utf-8")
    (tmp_path / "Gemfile.lock").write_text(
        "GEM\n  specs:\n    ruby-openai (6.3.1)\n", encoding="utf-8")
    (tmp_path / "app.csproj").write_text(
        '<Project><ItemGroup>'
        '<PackageReference Version="1.0.0" Include="Azure.AI.OpenAI" />'          # reversed attrs
        '<PackageReference Include="Child.Pkg"><Version>2.0.0</Version></PackageReference>'
        '</ItemGroup></Project>', encoding="utf-8")
    (tmp_path / "go.mod").write_text(
        "module x\nrequire (\n\tgithub.com/foo/bar v1.2.3\n)\n", encoding="utf-8")
    (tmp_path / "package-lock.json").write_text(
        '{"packages":{"node_modules/axios":{"version":"0.21.0"}}}', encoding="utf-8")
    names = ("Cargo.lock", "Gemfile.lock", "app.csproj", "go.mod", "package-lock.json")
    disc = [(str(tmp_path / n), n) for n in names]
    deps = dsgai_cve.parse_dependencies(disc)
    ecos = {d["ecosystem"] for d in deps}
    assert {"crates.io", "RubyGems", "NuGet", "Go", "npm"} <= ecos
    # both awkward .csproj forms parsed
    nuget = {d["package"] for d in deps if d["ecosystem"] == "NuGet"}
    assert {"Azure.AI.OpenAI", "Child.Pkg"} <= nuget


def test_cvss3_base_score():
    """CVSS v3.1 base scores computed locally from the OSV vector (audit H3)."""
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_cve
    assert dsgai_cve.cvss3_base_score("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H") == 9.8
    assert dsgai_cve.cvss3_base_score("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N") == 5.3
    assert dsgai_cve.cvss3_base_score("not-a-vector") is None
    # a critical advisory with only an OSV vector (NVD unavailable) is EXPLOITABLE,
    # not INFO — the bug this fixes.
    assert dsgai_cve.classify(None, 9.8) == "EXPLOITABLE"


def test_atlas_map_valid():
    amap = yaml.safe_load(open(os.path.join(SCANNER, "rules", "atlas-map.yaml"),
                               encoding="utf-8"))
    assert amap["atlas_version"]
    ctrl_re = __import__("re").compile(r"^DSGAI[0-9]{2}$")
    for t in amap["techniques"]:
        assert t["id"].startswith("AML.")
        assert all(ctrl_re.match(c) for c in t["controls"])


@requires_rg
def test_gitignored_env_is_still_scanned(tmp_path):
    """Real-world layout: a `.env` is gitignored + untracked. A secret scanner
    MUST still scan it — regression test for the discovery bug where git
    ls-files silently dropped it (the committed fixture .env masked this)."""
    repo = tmp_path / "realrepo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    (repo / ".gitignore").write_text(".env\n", encoding="utf-8")
    (repo / ".env").write_text(
        "OPENAI_API_KEY=sk-proj-FAKE00000000000000000000000000\n", encoding="utf-8")
    (repo / "app.py").write_text("x = 1\n", encoding="utf-8")
    env = dict(os.environ)
    subprocess.run(["git", "add", ".gitignore", "app.py"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "user.email=a@b.c", "-c", "user.name=t",
                    "commit", "-qm", "init"], cwd=repo, check=True)
    out = tmp_path / "s.json"
    subprocess.run([sys.executable, CLI, "scan", str(repo), "--no-cve",
                    "--json-out", str(out), "--format", "none"], env=env)
    cp = json.loads(out.read_text(encoding="utf-8"))
    env_findings = [f for f in cp["findings"] if ".env" in f["path"]]
    assert env_findings, "gitignored .env credential was not scanned"
    assert cp["controls"]["DSGAI02"] == "FAIL"


def test_rg_arg_batching():
    """Files are split into batches under the command-line budget so a large
    repo can't blow the OS arg limit (audit H4)."""
    ds = _import_cli()
    files = [("/some/long/abs/path/module_%04d.py" % i, "m%d.py" % i) for i in range(5000)]
    batches = list(ds._batches(files))
    assert len(batches) > 1, "5000 files should split into multiple rg batches"
    for b in batches:
        assert sum(len(f[0]) + 1 for f in b) <= ds._ARG_BUDGET or len(b) == 1
    assert sum(len(b) for b in batches) == len(files)  # no file dropped


def test_checkpoint_is_valid_logic(tmp_path):
    """Exercise the cache-invalidation helper (a stale ruleset invalidates)."""
    ds = _import_cli()
    repo = tmp_path / "r"
    repo.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    (repo / "a.txt").write_text("x", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "-c", "user.email=a@b.c", "-c", "user.name=t",
                    "commit", "-qm", "i"], cwd=repo, check=True)
    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    cp = {"git_commit": head, "ruleset_version": "0.3.0"}
    assert ds.checkpoint_is_valid(cp, str(repo), "0.3.0") is True
    assert ds.checkpoint_is_valid(cp, str(repo), "9.9.9") is False   # ruleset drift
    assert ds.checkpoint_is_valid({"git_commit": "deadbeef", "ruleset_version": "0.3.0"},
                                  str(repo), "0.3.0") is False        # HEAD mismatch


def test_report_no_path_leak_on_filemap_miss(tmp_path):
    """STRICT report must never fall back to a real path, and must escape the
    line number (audit L3)."""
    sys.path.insert(0, os.path.join(SCANNER, "cli"))
    import dsgai_report
    # a finding whose path is NOT in the (empty) filemap, with a malicious line
    f = {"path": "app/secret/config.py", "line": "1<script>",
         "classification": "structural"}
    rendered = dsgai_report.loc(f, {}, internal=False)
    assert "app/secret/config.py" not in rendered   # no real-path leak
    assert "unmapped" in rendered                    # placeholder (HTML-escaped)
    assert "<script>" not in rendered               # line escaped


def test_rules_json_in_sync():
    from_yaml = yaml.safe_load(open(RULES_YAML, encoding="utf-8"))
    rebuilt = json.dumps(from_yaml, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    current = open(RULES_JSON, encoding="utf-8").read()
    assert current == rebuilt, "rules/dsgai-rules.json is stale; run build/build_rules_json.py"
