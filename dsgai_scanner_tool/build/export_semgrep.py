#!/usr/bin/env python3
"""Export the STRUCTURAL DSGAI rules as a Semgrep pack.

Strategic point: this makes incumbent toolchains carriers of the DSGAI framework
— distribution, not competition. Generated from rules/dsgai-rules.yaml so it
can't drift (CI runs `--check`). Value-bearing rules are intentionally excluded
(their whole point is that the match content must never be surfaced, which a
generic Semgrep pack cannot guarantee).

  python build/export_semgrep.py            # write dist/dsgai.semgrep.yaml
  python build/export_semgrep.py --check     # CI: fail if the pack is stale
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / "rules" / "dsgai-rules.yaml"
OUT = ROOT / "dist" / "dsgai.semgrep.yaml"
SEVERITY = {"fail": "ERROR", "warn": "WARNING"}


def yq(s):
    return "'" + s.replace("'", "''") + "'"


def render():
    import yaml
    data = yaml.safe_load(RULES.read_text(encoding="utf-8"))
    out = [
        "# DSGAI STRUCTURAL rules as a Semgrep pack.",
        "# GENERATED from rules/dsgai-rules.yaml by build/export_semgrep.py — do not edit.",
        "# Value-bearing rules are excluded by design (their matches must never surface).",
        "rules:",
    ]
    for r in data["rules"]:
        if r["classification"] != "structural":
            continue
        sev = SEVERITY.get(r["signal"], "INFO")
        includes = ", ".join(yq(g) for g in r["file_globs"])
        # Semgrep pattern-regex runs against whole-file text; force multiline so a
        # line-anchored rule (e.g. P04.4's `^`) matches on any line, not just
        # file start (audit L7).
        pcre = r["pcre"]
        if ("^" in pcre or "$" in pcre) and not pcre.startswith("(?m)"):
            pcre = "(?m)" + pcre
        out += [
            f"  - id: dsgai-{r['id']}",
            f"    languages: [generic]",
            f"    severity: {sev}",
            f"    message: {yq(r['control'] + ' ' + r['id'] + ': ' + r['description'])}",
            f"    patterns:",
            f"      - pattern-regex: {yq(pcre)}",
            f"    paths:",
            f"      include: [{includes}]",
            f"    metadata:",
            f"      dsgai_control: {r['control']}",
            f"      dsgai_rule: {r['id']}",
            f"      confidence: {r['confidence']}",
            f"      framework: {yq(r['framework'])}",
        ]
    return "\n".join(out) + "\n"


def main(argv):
    rendered = render()
    if "--check" in argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            sys.stderr.write("dist/dsgai.semgrep.yaml is out of date. Run: "
                             "python build/export_semgrep.py\n")
            return 1
        print("dist/dsgai.semgrep.yaml is up to date.")
        return 0
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8", newline="\n")
    n = rendered.count("  - id: dsgai-")
    print(f"wrote {OUT} ({n} structural rules)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
