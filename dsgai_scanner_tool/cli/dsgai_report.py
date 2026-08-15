#!/usr/bin/env python3
"""Deterministic DSGAI HTML report renderer.

Renders `DSGAI-scan.json` to a self-contained HTML report — by code, from the
checkpoint, so the structure is fixed and testable. The LLM contributes only
designated prose (executive summary, remediation) injected as data via --prose.

Rendered with the standard library (styles live in templates/report.css and are
inlined) — no Jinja2 runtime dependency, matching the scanner's zero-dependency
ethos. STRICT mode renders stable file IDs (F07:12) and writes the ID->path map
to DSGAI-filemap.json (gitignore it); --internal renders full paths.

Usage:
  python cli/dsgai_report.py DSGAI-scan.json [--out dsgai-reports/report.html]
                                             [--prose prose.json] [--filemap DSGAI-filemap.json]
"""
import argparse
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(os.path.dirname(HERE), "templates", "report.css")

CTRL_CLASS = {"FAIL": "fail", "WARN": "warn", "PASS": "pass",
              "NOT VALIDATED": "nv", "NOT APPLICABLE": "na",
              "VENDOR ATTESTATION REQUIRED": "vendor"}
FIND_CLASS = {"fail": "fail", "warn": "warn", "pass_signal": "pass",
              "count": "nv", "info": "nv"}
ATTRIBUTION = (
    "Based on OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026) "
    "by the OWASP GenAI Data Security Initiative, led by Emmanuel Guilherme Junior. "
    "Report content CC BY-SA 4.0; scanner code Apache-2.0."
)


def esc(s):
    return html.escape(str(s), quote=True)


def build_filemap(cp):
    """Assign F01.. IDs to distinct paths in first-appearance (sorted) order."""
    paths = []
    for f in cp["findings"] + cp.get("suppressed", []):
        if f["path"] not in paths:
            paths.append(f["path"])
    paths.sort()
    return {p: f"F{i + 1:02d}" for i, p in enumerate(paths)}


def loc(f, filemap, internal):
    # In STRICT mode, a filemap miss must NOT fall back to the real path — that
    # would leak it into the "shareable" report. Use a placeholder (audit L3).
    p = f["path"] if internal else filemap.get(f["path"], "<unmapped>")
    redacted = " (value redacted)" if f.get("classification") == "value_bearing" else ""
    return f"{esc(p)}:{esc(f['line'])}{esc(redacted)}"  # escape line too (defense-in-depth)


def render(cp, prose, internal):
    css = open(CSS, encoding="utf-8").read()
    filemap = {} if internal else build_filemap(cp)
    mode = "INTERNAL" if internal else "STRICT"
    scope = cp.get("scan_scope", ".")
    incremental = scope.startswith("diff:")

    badges = [f"Framework {esc(cp['framework'])}", f"Engine {esc(cp['engine'])}",
              f"Ruleset {esc(cp['ruleset_version'])}", f"Scope {esc(scope)}",
              f"Scanned {esc(cp['scanned_at'])}"]
    mode_icon = "\U0001F513" if internal else "\U0001F6E1"
    mode_cls = "warnmode" if internal else ""
    b_html = f'<span class="badge {mode_cls}">{mode_icon} {mode}</span>'
    b_html += "".join(f'<span class="badge">{b}</span>' for b in badges)
    if incremental:
        b_html += '<span class="badge warnmode">INCREMENTAL — not a full assessment</span>'

    # Compliance dashboard
    dash = []
    for c in sorted(cp["controls"]):
        st = cp["controls"][c]
        cls = CTRL_CLASS.get(st, "nv")
        dash.append(f'<div class="ctrl {cls}"><div class="cid">{esc(c)}</div>'
                    f'<span class="st {cls}">{esc(st)}</span></div>')

    # Findings
    rows = []
    for f in cp["findings"]:
        if f["status"] not in ("fail", "warn"):
            continue
        cls = FIND_CLASS.get(f["status"], "nv")
        tag = " · baselined" if f.get("baselined") else ""
        rows.append(f'<tr><td><span class="st {cls}">{esc(f["status"].upper())}</span></td>'
                    f'<td>{esc(f["control"])}</td><td><code>{esc(f["rule_id"])}</code></td>'
                    f'<td>{loc(f, filemap, internal)}{esc(tag)}</td></tr>')
    findings_html = ("<table><tr><th>Status</th><th>Control</th><th>Rule</th><th>Location</th></tr>"
                     + "".join(rows) + "</table>") if rows else "<p>No FAIL/WARN findings.</p>"

    # CVEs
    cve_rows = []
    for c in cp.get("cves", []):
        cvss = c.get("cvss")
        cve_rows.append(f'<tr class="cve {esc(c["status"])}"><td>{esc(c["status"])}</td>'
                        f'<td><code>{esc(c["package"])}=={esc(c["version"])}</code></td>'
                        f'<td>{esc(c["id"])}</td><td>{esc(cvss if cvss is not None else "—")}</td>'
                        f'<td>{esc(c.get("summary", ""))}</td></tr>')
    cve_html = ("<table><tr><th>Status</th><th>Package</th><th>Advisory</th><th>CVSS</th><th>Summary</th></tr>"
                + "".join(cve_rows) + "</table>") if cve_rows else "<p>No advisories.</p>"

    # Suppressed
    sup_rows = []
    for f in cp.get("suppressed", []):
        sup_rows.append(f'<tr class="suppressed"><td><code>{esc(f["rule_id"])}</code></td>'
                        f'<td>{loc(f, filemap, internal)}</td>'
                        f'<td>{esc(f.get("suppressed_reason", ""))}</td></tr>')
    sup_html = ("<h2>Suppressed</h2><table><tr><th>Rule</th><th>Location</th><th>Reason</th></tr>"
                + "".join(sup_rows) + "</table>") if sup_rows else ""

    # Filemap section (strict only, and only listed here for the reader — the
    # ID->path map is written to DSGAI-filemap.json, never the shareable report).
    exec_summary = esc(prose.get("executive_summary",
                                 "Automated DSGAI compliance scan. Review FAIL findings first."))
    remediation = esc(prose.get("remediation", "See per-control remediation guidance."))

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DSGAI Compliance Report</title>
<style>{css}</style></head>
<body><div class="wrap">
<header class="rpt"><h1>OWASP DSGAI 2026 Compliance Report</h1>
<div class="badges">{b_html}</div></header>

<div class="residual"><strong>Residual risk:</strong> STRICT mode is designed to minimize
disclosure (file IDs + line numbers only; value-bearing matches never shown). It is not a
guarantee the report is public-safe — the existence and location of failing controls is
itself information. Handle it like any security assessment.</div>

<h2>Executive summary</h2><p>{exec_summary}</p>
<h2>Compliance dashboard</h2><div class="dash">{''.join(dash)}</div>
<h2>Findings</h2>{findings_html}
<h2>Remediation</h2><p>{remediation}</p>
<h2>CVE advisories</h2>{cve_html}
{sup_html}
<footer class="rpt">{esc(ATTRIBUTION)}</footer>
</div></body></html>
"""


def main(argv):
    ap = argparse.ArgumentParser(prog="dsgai_report")
    ap.add_argument("checkpoint")
    ap.add_argument("--out", default=None)
    ap.add_argument("--prose", default=None, help="JSON with executive_summary/remediation")
    ap.add_argument("--filemap", default="DSGAI-filemap.json")
    ap.add_argument("--internal", action="store_true")
    args = ap.parse_args(argv)

    cp = json.load(open(args.checkpoint, encoding="utf-8"))
    prose = json.load(open(args.prose, encoding="utf-8")) if args.prose else {}
    html_out = render(cp, prose, args.internal)

    out = args.out or os.path.join("dsgai-reports", "DSGAI-report.html")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html_out)
    if not args.internal:
        fmap = build_filemap(cp)
        with open(args.filemap, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({v: k for k, v in fmap.items()}, fh, indent=2, sort_keys=True)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
