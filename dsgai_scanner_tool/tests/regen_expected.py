#!/usr/bin/env python3
"""Regenerate / verify the raw match set behind tests/expected-findings.yaml.

Appendix-C mitigation for brittle pinned line numbers: after editing a fixture,
run this to see exactly which (rule_id, path, line) matches changed, then update
the answer sheet's `findings` and review the diff. It intentionally reports RAW
rule matches only (no compound-status resolution — that is the CLI's job in
PR-05); its purpose is to catch line-number drift, not to grade findings.

  python tests/regen_expected.py            # print the raw match set
  python tests/regen_expected.py --check     # exit 1 if the sheet's findings
                                             # line-pins drift from the scan

ripgrep is located via $DSGAI_RG, then PATH ('rg'). PCRE2 support required.
"""
import fnmatch
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCANNER = os.path.dirname(HERE)
RULES_JSON = os.path.join(SCANNER, "rules", "dsgai-rules.json")
FIXTURE = os.path.join(HERE, "fixtures", "vulnerable-app")
SHEET = os.path.join(HERE, "expected-findings.yaml")


def find_rg():
    rg = os.environ.get("DSGAI_RG") or shutil.which("rg") or shutil.which("rg.exe")
    if not rg:
        sys.exit("error: ripgrep (rg) not found. Install it or set $DSGAI_RG.")
    return rg


def glob_match(path, globs):
    base = os.path.basename(path)
    rel = path.replace(os.sep, "/")
    for g in globs:
        if fnmatch.fnmatch(base, g) or fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, "*/" + g):
            return True
    return False


def raw_matches(rg):
    rules = json.load(open(RULES_JSON, encoding="utf-8"))["rules"]
    files = []
    for dp, _, fns in os.walk(FIXTURE):
        for fn in fns:
            files.append(os.path.join(dp, fn))
    out = set()
    for r in rules:
        for f in files:
            rel = os.path.relpath(f, FIXTURE).replace(os.sep, "/")
            if not glob_match(rel, r["file_globs"]):
                continue
            p = subprocess.run([rg, "--pcre2", "-n", "-o", "-e", r["pcre"], f],
                               capture_output=True, text=True)
            for line in p.stdout.splitlines():
                lno = line.split(":", 1)[0]
                if lno.isdigit():
                    out.add((r["id"], rel, int(lno)))
    return out


def sheet_pins():
    import yaml
    data = yaml.safe_load(open(SHEET, encoding="utf-8"))
    return {(f["rule_id"], f["path"], f["line"]) for f in data.get("findings", [])}


def main(argv):
    rg = find_rg()
    scanned = raw_matches(rg)
    if "--check" in argv:
        pinned = sheet_pins()
        missing = pinned - scanned   # in sheet, not produced by scan
        extra = scanned - pinned     # produced by scan, not in sheet
        if missing or extra:
            if missing:
                print("Sheet findings NOT produced by the scan (stale pins):")
                for m in sorted(missing):
                    print("  -", m)
            if extra:
                print("Scan matches NOT in the sheet (add or curate):")
                for e in sorted(extra):
                    print("  +", e)
            return 1
        print(f"OK: {len(pinned)} sheet findings line-pins all match the scan.")
        return 0
    for m in sorted(scanned, key=lambda x: (x[1], x[2], x[0])):
        print(f"{m[0]:7} {m[1]}:{m[2]}")
    print(f"\n{len(scanned)} raw matches.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
