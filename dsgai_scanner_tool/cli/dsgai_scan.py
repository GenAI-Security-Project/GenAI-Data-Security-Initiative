#!/usr/bin/env python3
"""DSGAI scanner — deterministic runner.

Single-file, standard-library-only at runtime. Shells out to ripgrep
(`rg --pcre2`, a hard requirement) for all pattern matching. Loads the compiled
ruleset from rules/dsgai-rules.json (no PyYAML needed at runtime).

VALUE-BEARING rules run in location-only mode: `rg -o --replace ''` makes
ripgrep erase the matched text before it emits anything, so the secret never
leaves the rg process — no pipe transit, no content in this program's memory,
the checkpoint, or the report. Findings never carry match content, by
construction.

Subcommands: scan (default), detect, doctor. Global: --version.
Exit codes: 0 clean, 1 findings >= threshold, 2 execution error.
"""
import argparse
import datetime
import fnmatch
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCANNER_ROOT = os.path.dirname(HERE)
RULES_JSON = os.path.join(SCANNER_ROOT, "rules", "dsgai-rules.json")
VERSION_FILE = os.path.join(SCANNER_ROOT, "VERSION")
SCHEMA_VERSION = "1.0"
SKILL_VERSION = "0.3.0"

VALUE_BEARING_CONTROLS = {"DSGAI02", "DSGAI13", "DSGAI14", "DSGAI15"}
# Fields that must never appear on a finding — the redaction guarantee, enforced
# in code before the checkpoint is written (and by schemas/dsgai-scan.schema.json).
BANNED_FINDING_FIELDS = {"match_text", "content", "value", "raw_grep_output"}
CHECKPOINT_REQUIRED = {
    "schema_version", "ruleset_version", "skill_version", "framework", "engine",
    "git_commit", "scanned_at", "scan_scope", "obfuscation", "controls",
    "findings", "suppressed", "cves", "file_map_ref",
}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env",
             "dist", "build", ".mypy_cache", ".pytest_cache", ".tox", ".idea"}
# Credential-bearing files that MUST be scanned even when gitignored — a secret
# scanner's whole job is to catch keys in exactly these, and they are almost
# always gitignored (so `git ls-files` would drop them). Matched by basename.
ALWAYS_SCAN_GLOBS = ["*.env", "*.env.*", ".env", ".env.*", "*.envrc"]

# requires_nearby resolution: status when the requirement is violated (required
# rule absent) vs satisfied (present). Read the require list / window from the
# rule's requires_nearby; these two statuses are the only per-rule extra.
COMPOUND_STATUS = {
    "P05.1": {"violation": "warn", "satisfied": "pass_signal"},
    "P06.5": {"violation": "fail", "satisfied": "info"},
    "P11.1": {"violation": "fail", "satisfied": "pass_signal"},
    "P18.4": {"violation": "warn", "satisfied": "pass_signal"},
    "P20.5": {"violation": "fail", "satisfied": "pass_signal"},
    # Corroborating-signal rules: fire only when the nearby signal is PRESENT
    # (drop the match otherwise). P12.1 is a FAIL only when an LLM call is nearby.
    "P12.1": {"violation": "drop", "satisfied": "fail"},
}

# Step-0 detection signals. Raw-endpoint signals catch repos calling LLM APIs
# via bare requests/fetch (common in Go / minimal services). C# signals seed
# NuGet detection ahead of full support (PR-15).
DETECT_SIGNALS = {
    "llm": [r"openai", r"anthropic", r"langchain", r"llama_index", r"llama-index",
            r"cohere", r"mistralai", r"litellm", r"api\.openai\.com",
            r"api\.anthropic\.com", r"generativelanguage\.googleapis\.com",
            r"Microsoft\.SemanticKernel", r"Azure\.AI\.OpenAI",  # C# / NuGet
            r"async-openai", r"async_openai",                    # Rust / crates.io
            r"ruby-openai", r"ruby_openai", r"anthropic-rb"],     # Ruby / RubyGems
    "multimodal": [r"vision", r"image_url", r"ocr", r"whisper", r"audio",
                   r"detect_pii_in_image"],
    "synthetic_data": [r"\bSDV\b", r"gretel", r"synthetic_data_vault", r"smartnoise"],
    "labeling": [r"label_studio", r"labelbox", r"scale_api", r"annotator"],
}
GATE_TO_SIGNAL = {"multimodal": "multimodal",
                  "synthetic_data": "synthetic_data",
                  "labeling": "labeling"}


def eprint(*a):
    print(*a, file=sys.stderr)


def find_rg():
    import shutil
    rg = os.environ.get("DSGAI_RG") or shutil.which("rg") or shutil.which("rg.exe")
    return rg


def rg_supports_pcre2(rg):
    try:
        out = subprocess.run([rg, "--pcre2-version"], capture_output=True, text=True)
        return out.returncode == 0
    except Exception:
        return False


def load_rules():
    with open(RULES_JSON, encoding="utf-8") as fh:
        return json.load(fh)


def read_version():
    try:
        return open(VERSION_FILE, encoding="utf-8").read().strip()
    except OSError:
        return SKILL_VERSION


# --------------------------------------------------------------------------- #
# File discovery
# --------------------------------------------------------------------------- #
def discover_files(target, excludes):
    """Return files under target as (abs_path, rel_path).

    Uses `git ls-files` (tracked + untracked-not-ignored) when target is inside a
    repo, so general noise/build output respects .gitignore. BUT credential
    files matching ALWAYS_SCAN_GLOBS (e.g. `.env`) are ALWAYS included even when
    gitignored — a secret scanner must scan exactly those. Falls back to a
    filtered os.walk (which already sees everything) outside a repo.
    """
    target = os.path.abspath(target)
    files = _git_files(target)
    if files is None:
        files = _walk_files(target)
    else:
        # Union in gitignored credential files git would otherwise drop.
        seen = set(files)
        for ap in _sensitive_walk_files(target):
            if ap not in seen:
                seen.add(ap)
                files.append(ap)
    out = []
    for ap in files:
        rel = os.path.relpath(ap, target).replace(os.sep, "/")
        if _excluded(rel, ap, target, excludes):
            continue
        out.append((ap, rel))
    out.sort(key=lambda x: x[1])
    return out


def _sensitive_walk_files(target):
    """Files under target whose basename matches ALWAYS_SCAN_GLOBS (skips noise
    dirs). Used to re-include gitignored credential files like .env."""
    hits = []
    for dp, dirs, fns in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in fns:
            if any(fnmatch.fnmatch(fn, g) for g in ALWAYS_SCAN_GLOBS):
                hits.append(os.path.join(dp, fn))
    return hits


def _git_files(target):
    try:
        top = subprocess.run(["git", "-C", target, "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True)
        if top.returncode != 0:
            return None
        res = subprocess.run(
            ["git", "-C", target, "ls-files", "--cached", "--others",
             "--exclude-standard", "-z", "--", "."],
            capture_output=True, text=True)
        if res.returncode != 0:
            return None
        rels = [p for p in res.stdout.split("\0") if p]
        return [os.path.join(target, p.replace("/", os.sep)) for p in rels]
    except Exception:
        return None


def _walk_files(target):
    collected = []
    for dp, dirs, fns in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in fns:
            collected.append(os.path.join(dp, fn))
    return collected


def _excluded(rel, ap, target, excludes):
    for ex in excludes:
        exn = ex.replace(os.sep, "/").rstrip("/")
        if rel == exn or rel.startswith(exn + "/") or fnmatch.fnmatch(rel, exn):
            return True
    return False


def glob_match(rel, globs):
    base = os.path.basename(rel)
    for g in globs:
        if fnmatch.fnmatch(base, g) or fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, "*/" + g):
            return True
    return False


# --------------------------------------------------------------------------- #
# Rule execution
# --------------------------------------------------------------------------- #
def run_rule(rg, rule, files, scan_root):
    """Return a set of (rel_path, line) matches for one rule.

    Value-bearing rules pass -o --replace '' so ripgrep erases the match text;
    only path:line: is ever emitted. This is the structural redaction guarantee.
    """
    if not files:
        return set()
    cmd = [rg, "--pcre2", "--no-config", "--with-filename", "--line-number"]
    if rule["classification"] == "value_bearing":
        # LOCATION-ONLY: rg erases the matched text before emitting anything.
        cmd += ["--only-matching", "--replace", ""]
    cmd += ["-e", rule["pcre"], "--"]
    cmd += [f[0] for f in files]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=scan_root)
    if proc.returncode >= 2:
        raise RuntimeError(f"rg failed on {rule['id']}: {proc.stderr.strip()[:200]}")
    matches = set()
    abs_to_rel = {f[0]: f[1] for f in files}
    for line in proc.stdout.splitlines():
        # Format: <path>:<line>:<rest>. Path is an absolute path we passed in;
        # split off the trailing :line:rest without touching a drive colon.
        rest = line
        # find ':<digits>:' anchor from the path we know
        parsed = _parse_rg_line(line, abs_to_rel)
        if parsed:
            matches.add(parsed)
    return matches


def _parse_rg_line(line, abs_to_rel):
    # Match the longest known absolute path prefix, then :line:.
    for ap, rel in abs_to_rel.items():
        prefix = ap + ":"
        if line.startswith(prefix):
            tail = line[len(prefix):]
            num, _, _ = tail.partition(":")
            if num.isdigit():
                return (rel, int(num))
    return None


def detect_stack(rg, files, scan_root):
    """Return the set of detected signal categories for NOT APPLICABLE gating."""
    detected = set()
    paths = [f[0] for f in files]
    if not paths:
        return detected
    for cat, patterns in DETECT_SIGNALS.items():
        pat = "|".join(patterns)
        proc = subprocess.run(
            [rg, "--pcre2", "--no-config", "-l", "-i", "-e", pat, "--"] + paths,
            capture_output=True, text=True, cwd=scan_root)
        if proc.returncode == 0 and proc.stdout.strip():
            detected.add(cat)
    return detected


def nearby(matches_by_rule, required_ids, path, line, window, module_scope):
    for rid in required_ids:
        for (mp, ml) in matches_by_rule.get(rid, ()):  # noqa: E501
            if mp != path:
                continue
            if module_scope or abs(ml - line) <= window:
                return True
    return False


def resolve_findings(rules, matches_by_rule, detected, nearby_matches=None):
    """Apply subtract / requires_nearby / gating to produce resolved findings."""
    nearby_matches = nearby_matches or {}
    findings = []
    for rule in rules:
        rid = rule["id"]
        raw = matches_by_rule.get(rid, set())
        if not raw:
            continue
        gate = rule.get("gated_on")
        if gate and GATE_TO_SIGNAL.get(gate) not in detected:
            continue  # NOT APPLICABLE — stack not present
        subtract_ids = rule.get("subtract") or []
        rn = rule.get("requires_nearby")
        for (path, line) in sorted(raw):
            # subtract: same-line cancellation (e.g. torch.load minus weights_only)
            if subtract_ids and any((path, line) in matches_by_rule.get(s, set())
                                    for s in subtract_ids):
                continue
            status = rule["signal"]
            if rn:
                window = rn.get("lines", 0)
                module_scope = rn.get("scope") == "module" or "lines" not in rn
                if rn.get("pattern"):
                    # proximity of a raw corroborating pattern (e.g. an LLM call)
                    sat = any(mp == path and (module_scope or abs(ml - line) <= window)
                              for (mp, ml) in nearby_matches.get(rid, set()))
                else:
                    required = rn.get("rules") or ([rn["rule"]] if rn.get("rule") else [])
                    need_all = "rules" in rn and rn.get("scope") != "module"
                    sat = _satisfied(matches_by_rule, required, path, line, window,
                                     module_scope, need_all)
                cs = COMPOUND_STATUS.get(rid, {"violation": "fail", "satisfied": "pass_signal"})
                status = cs["satisfied"] if sat else cs["violation"]
                if status == "drop":
                    continue  # corroborating signal absent — not a finding
            findings.append({
                "control": rule["control"],
                "rule_id": rid,
                "path": path,
                "line": line,
                "status": status,
                "classification": rule["classification"],
            })
    findings.sort(key=lambda f: (f["path"], f["line"], f["rule_id"]))
    return findings


def _satisfied(matches_by_rule, required, path, line, window, module_scope, need_all):
    def present(rid):
        for (mp, ml) in matches_by_rule.get(rid, set()):
            if mp == path and (module_scope or abs(ml - line) <= window):
                return True
        return False
    if not required:
        return False
    return all(present(r) for r in required) if need_all else any(present(r) for r in required)


# --------------------------------------------------------------------------- #
# Control classification (Step 3)
# --------------------------------------------------------------------------- #
def classify_controls(rules, findings, detected):
    controls = {r["control"] for r in rules}
    gated = {}
    for r in rules:
        if r.get("gated_on"):
            gated[r["control"]] = r["gated_on"]
    by_control = {}
    for f in findings:
        by_control.setdefault(f["control"], []).append(f["status"])
    out = {}
    for c in sorted(controls):
        statuses = by_control.get(c, [])
        if c in gated and GATE_TO_SIGNAL.get(gated[c]) not in detected:
            out[c] = "NOT APPLICABLE"
        elif "fail" in statuses:
            out[c] = "FAIL"
        elif "warn" in statuses:
            out[c] = "WARN"
        elif "pass_signal" in statuses:
            out[c] = "PASS"
        else:
            out[c] = "NOT VALIDATED"
    return out


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #
def now_iso():
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch and epoch.isdigit():
        dt = datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc)
    else:
        dt = datetime.datetime.now(datetime.timezone.utc)
    return dt.replace(microsecond=0).isoformat()


def git_commit(target):
    try:
        r = subprocess.run(["git", "-C", os.path.abspath(target), "rev-parse", "HEAD"],
                           capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def build_checkpoint(ruleset, findings, controls, scope, obfuscation, target,
                     cves=None, suppressed=None, diff_scope=None):
    return {
        "schema_version": SCHEMA_VERSION,
        "ruleset_version": ruleset["ruleset_version"],
        "skill_version": read_version(),
        "framework": ruleset["framework"],
        "engine": "deterministic-cli",
        "git_commit": git_commit(target),
        "scanned_at": now_iso(),
        "scan_scope": (f"diff:{diff_scope}" if diff_scope else scope),
        "obfuscation": obfuscation,
        "controls": controls,
        "findings": findings,
        "suppressed": suppressed or [],
        "cves": cves or [],
        "file_map_ref": None,
    }


def self_validate_checkpoint(cp):
    """Stdlib self-check run before writing the checkpoint (no jsonschema at
    runtime). Enforces required fields and the redaction guarantee."""
    missing = CHECKPOINT_REQUIRED - set(cp)
    if missing:
        raise ValueError(f"checkpoint missing required fields: {sorted(missing)}")
    for f in cp["findings"] + (cp.get("suppressed") or []):
        leaked = BANNED_FINDING_FIELDS & set(f)
        if leaked:
            raise ValueError(f"finding would leak match content via {sorted(leaked)}: "
                             f"{f.get('rule_id')} {f.get('path')}")
    return True


def checkpoint_is_valid(cp, target, current_ruleset_version):
    """Cache invalidation: a checkpoint may be reused only if it was produced at
    the current HEAD, on a clean working tree, with the current ruleset. Anything
    else means the findings could be stale — delete and rescan. A compliance
    artifact must never serve stale findings with a fresh date. (The skill's
    resume logic calls this from PR-07 on.)"""
    if cp.get("ruleset_version") != current_ruleset_version:
        return False
    head = git_commit(target)
    if not head or cp.get("git_commit") != head:
        return False
    try:
        r = subprocess.run(["git", "-C", os.path.abspath(target), "status", "--porcelain"],
                           capture_output=True, text=True)
        if r.returncode != 0 or r.stdout.strip():
            return False  # dirty working tree
    except Exception:
        return False
    return True


SARIF_LEVEL = {"fail": "error", "warn": "warning", "pass_signal": "note",
               "count": "note", "info": "note"}


def build_sarif(ruleset, rules, findings):
    rules_index = {r["id"]: i for i, r in enumerate(rules)}
    sarif_rules = [{
        "id": r["id"],
        "name": r["name"],
        "shortDescription": {"text": r["description"]},
        "properties": {"control": r["control"], "classification": r["classification"],
                       "confidence": r["confidence"], "signal": r["signal"]},
    } for r in rules]
    results = []
    for f in findings:
        results.append({
            "ruleId": f["rule_id"],
            "ruleIndex": rules_index[f["rule_id"]],
            "level": SARIF_LEVEL.get(f["status"], "note"),
            "message": {"text": f"{f['control']} {f['rule_id']} ({f['status']})"},
            "locations": [{"physicalLocation": {
                "artifactLocation": {"uri": f["path"]},
                "region": {"startLine": f["line"]},
            }}],
        })
    return {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/sarif-2.1/schema/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {
                "name": "dsgai-scan",
                "version": read_version(),
                "informationUri": "https://genai.owasp.org/initiative/data-security/",
                "rules": sarif_rules,
            }},
            "results": results,
        }],
    }


def print_table(controls, findings):
    print("DSGAI scan summary")
    print("=" * 50)
    for c in sorted(controls):
        print(f"  {c}: {controls[c]}")
    print("-" * 50)
    print(f"  findings: {len(findings)} "
          f"(fail={sum(1 for f in findings if f['status'] == 'fail')}, "
          f"warn={sum(1 for f in findings if f['status'] == 'warn')})")
    for f in findings:
        if f["status"] in ("fail", "warn"):
            redacted = " (value redacted)" if f["classification"] == "value_bearing" else ""
            print(f"  [{f['status'].upper()}] {f['control']} {f['rule_id']} "
                  f"{f['path']}:{f['line']}{redacted}")


# --------------------------------------------------------------------------- #
# Subcommands
# --------------------------------------------------------------------------- #
SUPPRESS_RE = __import__("re").compile(
    r'dsgai-ignore:\s*(P\d{2}\.\d+)\s+reason=["\']([^"\']+)["\']')


def load_suppressions(files):
    """Map path -> [(line, rule_id, reason)] from inline `# dsgai-ignore` comments.

    A finding is suppressed when a matching directive sits on its line or the
    line immediately above. A reason string is required (the regex enforces it).
    """
    out = {}
    for ap, rel in files:
        try:
            text = open(ap, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(text, 1):
            m = SUPPRESS_RE.search(line)
            if m:
                out.setdefault(rel, []).append((i, m.group(1), m.group(2)))
    return out


def split_suppressed(findings, suppressions):
    """Each `# dsgai-ignore` directive suppresses at most ONE finding: the one on
    the same line (inline) if present, otherwise the one on the next line (comment
    directly above the code). This avoids an inline comment also swallowing an
    unrelated finding on the following line."""
    removed = set()
    suppressed = []
    for path, directives in suppressions.items():
        for (cline, crule, reason) in directives:
            for target in (cline, cline + 1):
                match = next((f for f in findings
                              if id(f) not in removed and f["path"] == path
                              and f["rule_id"] == crule and f["line"] == target), None)
                if match is not None:
                    removed.add(id(match))
                    suppressed.append({**match, "suppressed_reason": reason})
                    break
    active = [f for f in findings if id(f) not in removed]
    return active, suppressed


def finding_fp(f):
    """Stable fingerprint for baseline comparison (line-independent-ish)."""
    return f"{f['control']}|{f['rule_id']}|{f['path']}"


def load_baseline(path):
    try:
        data = json.load(open(path, encoding="utf-8"))
        return set(data.get("fingerprints", []))
    except (OSError, ValueError):
        return None


def diff_files(target, ref):
    """Return the set of rel paths changed vs `ref` (git). None if unavailable."""
    try:
        r = subprocess.run(["git", "-C", os.path.abspath(target), "diff",
                            "--name-only", ref], capture_output=True, text=True)
        if r.returncode != 0:
            return None
        return {p.strip().replace("/", os.sep) for p in r.stdout.splitlines() if p.strip()}
    except Exception:
        return None


def cmd_scan(args):
    rg = find_rg()
    if not rg:
        eprint("error: ripgrep (rg) not found. Install ripgrep (https://github.com/"
               "BurntSushi/ripgrep) or set $DSGAI_RG.")
        return 2
    if not rg_supports_pcre2(rg):
        eprint("error: this ripgrep build lacks PCRE2 support (rg --pcre2-version failed).")
        return 2
    ruleset = load_rules()
    rules = ruleset["rules"]
    excludes = args.exclude or []
    scope = args.scope or "."
    scan_root = os.path.abspath(args.target)
    scoped_target = os.path.join(scan_root, scope) if scope != "." else scan_root
    files = discover_files(scoped_target, excludes)
    diff_scope = None
    if getattr(args, "diff", None):
        changed = diff_files(args.target, args.diff)
        if changed is None:
            eprint(f"error: could not compute git diff vs '{args.diff}'")
            return 2
        files = [f for f in files if f[1].replace("/", os.sep) in changed]
        diff_scope = args.diff
    detected = detect_stack(rg, files, scan_root)
    matches_by_rule = {}
    nearby_matches = {}
    try:
        for rule in rules:
            candidates = [f for f in files
                          if glob_match(f[1], rule["file_globs"])
                          and not glob_match(f[1], rule.get("exclude_globs") or [])]
            matches_by_rule[rule["id"]] = run_rule(rg, rule, candidates, scan_root)
            rn = rule.get("requires_nearby") or {}
            if rn.get("pattern"):
                # Locate the corroborating pattern (always structural — a code
                # shape like an LLM call, never a secret) for proximity checks.
                probe = {"classification": "structural", "pcre": rn["pattern"]}
                nearby_matches[rule["id"]] = run_rule(rg, probe, candidates, scan_root)
    except RuntimeError as exc:
        eprint(f"error: {exc}")
        return 2
    findings = resolve_findings(rules, matches_by_rule, detected, nearby_matches)

    # Suppressions: inline `# dsgai-ignore` comments move findings to a visible
    # Suppressed section rather than silently dropping them.
    suppressions = load_suppressions(files)
    findings, suppressed = split_suppressed(findings, suppressions)

    # Baseline: mark previously-known findings so only NEW ones gate CI.
    baseline = load_baseline(args.baseline) if getattr(args, "baseline", None) else None
    if baseline is not None:
        for f in findings:
            if finding_fp(f) in baseline:
                f["baselined"] = True

    # CVE enrichment (deterministic, cached). Off with --no-cve.
    cves = []
    if not getattr(args, "no_cve", False):
        try:
            import dsgai_cve
            cves = dsgai_cve.enrich(files, offline=getattr(args, "offline", False),
                                    refresh=getattr(args, "refresh_cve", False))
        except ImportError:
            eprint("note: dsgai_cve module not found alongside the CLI; skipping CVE stage")
        except Exception as exc:  # noqa: BLE001 — CVE is best-effort
            eprint(f"note: CVE enrichment failed ({exc}); continuing")

    controls = classify_controls(rules, findings, detected)
    checkpoint = build_checkpoint(ruleset, findings, controls, scope,
                                  args.obfuscation, args.target,
                                  cves=cves, suppressed=suppressed,
                                  diff_scope=diff_scope)

    try:
        self_validate_checkpoint(checkpoint)
    except ValueError as exc:
        eprint(f"error: refusing to write an invalid checkpoint: {exc}")
        return 2

    if args.format == "table":
        print_table(controls, findings)
        if diff_scope:
            print(f"  scope: INCREMENTAL diff vs {diff_scope} — not a full assessment")
        if suppressed:
            print(f"  suppressed: {len(suppressed)} finding(s) via dsgai-ignore")
        if cves:
            print(f"  CVEs: {len(cves)} "
                  f"({sum(1 for c in cves if c['status'] == 'EXPLOITABLE')} exploitable)")
    if args.json_out:
        _write_json(args.json_out, checkpoint)
    if args.sarif:
        _write_json(args.sarif, build_sarif(ruleset, rules, findings))

    # Only NEW (non-baselined) findings gate the build.
    gating = [f for f in findings if not f.get("baselined")]
    fails = sum(1 for f in gating if f["status"] == "fail")
    warns = sum(1 for f in gating if f["status"] == "warn")
    exploitable = sum(1 for c in cves if c["status"] == "EXPLOITABLE")
    if args.fail_on == "fail" and (fails or exploitable):
        return 1
    if args.fail_on == "warn" and (fails or warns or exploitable):
        return 1
    return 0


def _write_json(path, obj):
    text = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def cmd_detect(args):
    rg = find_rg()
    if not rg:
        eprint("error: ripgrep (rg) not found.")
        return 2
    files = discover_files(os.path.abspath(args.target), args.exclude or [])
    detected = detect_stack(rg, files, args.target)
    is_genai = "llm" in detected
    print("GenAI signals detected:" if is_genai else "No GenAI signals detected.")
    for cat in sorted(detected):
        print(f"  - {cat}")
    return 0 if is_genai else 1


def cmd_doctor(args):
    ok = True
    rg = find_rg()
    print(f"ripgrep: {'found at ' + rg if rg else 'NOT FOUND'}")
    if rg:
        v = subprocess.run([rg, "--version"], capture_output=True, text=True)
        print("  " + v.stdout.splitlines()[0])
        pcre = rg_supports_pcre2(rg)
        print(f"  PCRE2 support: {'yes' if pcre else 'NO'}")
        ok = ok and pcre
    else:
        ok = False
    print(f"rules: {RULES_JSON}")
    try:
        n = len(load_rules()["rules"])
        print(f"  loaded {n} rules")
    except Exception as exc:  # noqa: BLE001
        print(f"  FAILED to load rules: {exc}")
        ok = False
    print(f"version: {read_version()}")
    return 0 if ok else 2


def cmd_baseline(args):
    rg = find_rg()
    if not rg:
        eprint("error: ripgrep (rg) not found.")
        return 2
    ruleset = load_rules()
    rules = ruleset["rules"]
    scan_root = os.path.abspath(args.target)
    scoped = os.path.join(scan_root, args.scope) if args.scope != "." else scan_root
    files = discover_files(scoped, args.exclude or [])
    detected = detect_stack(rg, files, scan_root)
    matches_by_rule, nearby = {}, {}
    for rule in rules:
        cands = [f for f in files if glob_match(f[1], rule["file_globs"])
                 and not glob_match(f[1], rule.get("exclude_globs") or [])]
        matches_by_rule[rule["id"]] = run_rule(rg, rule, cands, scan_root)
        rn = rule.get("requires_nearby") or {}
        if rn.get("pattern"):
            nearby[rule["id"]] = run_rule(rg, {"classification": "structural",
                                               "pcre": rn["pattern"]}, cands, scan_root)
    findings, _ = split_suppressed(
        resolve_findings(rules, matches_by_rule, detected, nearby),
        load_suppressions(files))
    fps = sorted({finding_fp(f) for f in findings if f["status"] in ("fail", "warn")})
    _write_json(args.out, {"ruleset_version": ruleset["ruleset_version"],
                           "created_at": now_iso(), "fingerprints": fps})
    print(f"wrote {args.out} ({len(fps)} baselined finding fingerprints)")
    return 0


def cmd_cve(args):
    try:
        import dsgai_cve
    except ImportError:
        eprint("error: dsgai_cve module not found alongside the CLI.")
        return 2
    files = discover_files(os.path.abspath(args.target), args.exclude or [])
    cves = dsgai_cve.enrich(files, offline=args.offline, refresh=args.refresh_cve)
    for c in cves:
        cvss = f" CVSS {c['cvss']}" if c.get("cvss") is not None else ""
        print(f"[{c['status']}] {c['package']}=={c['version']} {c['id']}{cvss}")
    print(f"\n{len(cves)} advisories "
          f"({sum(1 for c in cves if c['status'] == 'EXPLOITABLE')} exploitable)")
    return 1 if any(c["status"] == "EXPLOITABLE" for c in cves) else 0


def build_parser():
    p = argparse.ArgumentParser(prog="dsgai_scan", description="DSGAI deterministic scanner")
    p.add_argument("--version", action="version", version=f"dsgai_scan {read_version()}")
    sub = p.add_subparsers(dest="command")

    sp = sub.add_parser("scan", help="scan a repository")
    sp.add_argument("target", nargs="?", default=".")
    sp.add_argument("--scope", default=".", help="sub-path under target to scan")
    sp.add_argument("--exclude", action="append", default=[],
                    help="path/glob to exclude (repeatable)")
    sp.add_argument("--format", choices=["table", "none"], default="table")
    sp.add_argument("--json-out", default=None, help="write DSGAI-scan.json here")
    sp.add_argument("--sarif", default=None, help="write SARIF 2.1.0 here")
    sp.add_argument("--internal", dest="obfuscation", action="store_const",
                    const="internal", default="strict",
                    help="internal mode (full paths in report)")
    sp.add_argument("--fail-on", choices=["fail", "warn"], default="fail")
    sp.add_argument("--diff", default=None, metavar="REF",
                    help="incremental: scan only files changed vs REF")
    sp.add_argument("--baseline", default=None, metavar="FILE",
                    help="gate only on findings NOT in this baseline")
    sp.add_argument("--no-cve", action="store_true", help="skip CVE enrichment")
    sp.add_argument("--refresh-cve", action="store_true", help="ignore the CVE cache")
    sp.add_argument("--offline", action="store_true",
                    help="use the CVE cache only (no network)")
    sp.set_defaults(func=cmd_scan)

    dp = sub.add_parser("detect", help="check for GenAI signals (exit 0 if present)")
    dp.add_argument("target", nargs="?", default=".")
    dp.add_argument("--exclude", action="append", default=[])
    dp.set_defaults(func=cmd_detect)

    dop = sub.add_parser("doctor", help="check environment")
    dop.set_defaults(func=cmd_doctor)

    bp = sub.add_parser("baseline", help="write current findings to a baseline file")
    bp.add_argument("target", nargs="?", default=".")
    bp.add_argument("--scope", default=".")
    bp.add_argument("--exclude", action="append", default=[])
    bp.add_argument("--out", default="dsgai-baseline.json")
    bp.set_defaults(func=cmd_baseline)

    cp = sub.add_parser("cve", help="CVE enrichment only (from dependency manifests)")
    cp.add_argument("target", nargs="?", default=".")
    cp.add_argument("--exclude", action="append", default=[])
    cp.add_argument("--refresh-cve", action="store_true")
    cp.add_argument("--offline", action="store_true")
    cp.set_defaults(func=cmd_cve)
    return p


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
