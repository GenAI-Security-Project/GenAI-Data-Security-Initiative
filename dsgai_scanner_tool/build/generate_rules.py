#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""One-time bootstrap: extract DSGAI scanner patterns from dsgai_scanner_tool.md
Step 2 into rules/dsgai-rules.yaml.

Patterns are copied VERBATIM (bug-for-bug faithful — fixes come in PR-11 as
reviewable diffs). Classification, signal, confidence, and compound logic
(subtract / requires_nearby / exclude_globs / gated_on / notes) are augmented
from the skill's prose and the improvement plan's Appendix B seeds.

After this bootstrap runs, rules/dsgai-rules.yaml is the hand-maintained source
of truth; the skill prose becomes descriptive. Re-running would overwrite manual
edits, so it is kept only for provenance / audit.

Usage: python build/generate_rules.py > rules/dsgai-rules.yaml
"""
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "dsgai_scanner_tool.md"
VALUE_BEARING_CONTROLS = {2, 13, 14, 15}
FRAMEWORK = "dsgai-2026-v1.0"
RULESET_VERSION = "0.3.0"

HEADER_RE = re.compile(r'^### DSGAI(\d{2}) Scan .*\[(STRUCTURAL|VALUE-BEARING)')
FILES_RE = re.compile(r'^Files:\s*(.+)$')
# Pattern line: ID  <desc up to first colon>: <pcre to EOL>.  ':' separator is
# the FIRST colon — no rule description contains an internal colon.
PAT_RE = re.compile(r'^(P\d{2}\.\d+)\s+(.+?):\s+(.+?)\s*$')
GLOB_RE = re.compile(r'`([^`]+)`')

# Signal overrides for rules whose FAIL/PASS status comes from prose, not a
# marker in the description text.
SIGNAL_OVERRIDE = {
    "P02.1": "fail", "P02.2": "fail", "P02.3": "fail",
    "P02.4": "fail", "P02.5": "fail",
}

# Compound logic and gating, transcribed from the Step 2 prose notes.
SUBTRACT = {"P04.1": ["P04.2"]}
REQUIRES_NEARBY = {
    "P05.1": {"rules": ["P05.2", "P05.3"], "scope": "module"},
    "P06.5": {"rule": "P06.2", "scope": "module", "absent": True},
    "P11.1": {"rule": "P11.2", "lines": 15},
    "P18.4": {"rule": "P18.5", "lines": 10},
    "P20.5": {"rules": ["P20.1", "P20.2"], "lines": 15},
}
EXCLUDE_GLOBS = {
    "P12.6": ["**/migrations/**", "**/fixtures/**", "**/tests/**", "**/test/**"],
}
GATED_ON = {
    "P09.1": "multimodal", "P09.2": "multimodal", "P09.3": "multimodal",
    "P09.4": "multimodal", "P09.5": "multimodal",
    "P10.1": "synthetic_data", "P10.2": "synthetic_data", "P10.3": "synthetic_data",
    "P10.4": "synthetic_data", "P10.5": "synthetic_data",
    "P19.1": "labeling", "P19.2": "labeling", "P19.3": "labeling", "P19.4": "labeling",
}
# Free-text prose that resists full formalization at import time (refined later).
NOTES = {
    "P07.1": "Absence of P07.1-P07.4 in a multi-tenant or PII-handling repo = WARN.",
    "P08.1": "Absence of P08.1-P08.6 in a production GenAI service = WARN; "
             "absence in a high-risk EU AI Act use case = FAIL.",
    "P09.5": "Absence = note only (advanced control); P09.1-P09.4 absence in a "
             "multimodal pipeline = WARN.",
    "P10.1": "Synthetic data pipeline without any of P10.1/P10.2/P10.4 = FAIL.",
    "P12.6": "DDL in migrations/fixtures/tests is benign — excluded from FAIL.",
    "P14.4": "May contain inline PII in the format string — treated as VALUE-BEARING.",
    "P16.1": "Filename-existence check (not content grep). Absence in a repo with "
             ".env or secrets/ = WARN.",
    "P16.2": "Matched inside any AI-ignore file.",
    "P17.1": "LLM-calling module with none of P17.1-P17.5 = WARN.",
    "P21.2": "P21.2 in an agent module without P21.3 = WARN.",
}
# P16 rules carry a mode prefix ('filename match:' / 'in any ignore file:') in
# the pcre slot; strip it to the bare regex.
MODE_PREFIX_RE = re.compile(r'^(filename match|in any ignore file):\s*')


def slugify(text):
    text = re.sub(r'\([^)]*\)', '', text)          # drop (FAIL)/(PASS)/... markers
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text or "rule"


def derive_signal(pid, desc):
    if pid in SIGNAL_OVERRIDE:
        return SIGNAL_OVERRIDE[pid]
    d = desc.lower()
    if "fail" in d:
        return "fail"
    if "warn" in d:
        return "warn"
    if "pass" in d:
        return "pass_signal"
    if "count" in d:
        return "count"
    return "info"


def derive_confidence(pid, control, signal, pcre):
    # Value-bearing credential-literal FAILs are the high-confidence anchors.
    if control in VALUE_BEARING_CONTROLS and signal == "fail":
        return "high"
    if signal == "warn":
        return "low"          # heuristic / absence-adjacent — weak evidence
    if signal in ("pass_signal", "count"):
        return "medium"       # an import is not proof of correct use
    if signal == "fail":
        return "medium"       # structural heuristic FAILs (e.g. P12.1, P17.6)
    return "low"              # bare detection/info


def yaml_scalar(s):
    """Single-quote a scalar for YAML, escaping embedded single quotes."""
    return "'" + s.replace("'", "''") + "'"


def emit_list(vals):
    return "[" + ", ".join(yaml_scalar(v) for v in vals) + "]"


def main():
    # Ensure UTF-8 output regardless of the platform console codepage (Windows
    # defaults to cp1252, which corrupts em-dashes / non-ASCII on redirect).
    try:
        sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    except AttributeError:
        pass
    lines = SKILL.read_text(encoding="utf-8").splitlines()
    control = None
    classification = None
    file_globs = []
    in_fence = False
    rules = []
    unparsed = []

    # Only scan Step 2 (between its header and Step 3).
    start = next(i for i, l in enumerate(lines) if l.startswith("## Step 2:"))
    end = next(i for i, l in enumerate(lines) if l.startswith("## Step 3:"))

    for raw in lines[start:end]:
        line = raw.rstrip("\n")
        m = HEADER_RE.match(line)
        if m:
            control = int(m.group(1))
            classification = "value_bearing" if control in VALUE_BEARING_CONTROLS else "structural"
            file_globs = []
            in_fence = False
            continue
        fm = FILES_RE.match(line)
        if fm:
            file_globs = GLOB_RE.findall(fm.group(1))
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence and control is not None:
            pm = PAT_RE.match(line)
            if not pm:
                if line.strip():
                    unparsed.append(line)
                continue
            pid, desc, pcre = pm.group(1), pm.group(2).strip(), pm.group(3)
            pcre = MODE_PREFIX_RE.sub("", pcre).strip()
            signal = derive_signal(pid, desc)
            rules.append({
                "id": pid,
                "control": f"DSGAI{control:02d}",
                "name": slugify(desc),
                "classification": classification,
                "signal": signal,
                "confidence": derive_confidence(pid, control, signal, pcre),
                "pcre": pcre,
                "file_globs": list(file_globs),
                "exclude_globs": EXCLUDE_GLOBS.get(pid, []),
                "framework": FRAMEWORK,
                "description": desc,
                "subtract": SUBTRACT.get(pid),
                "requires_nearby": REQUIRES_NEARBY.get(pid),
                "gated_on": GATED_ON.get(pid),
                "notes": NOTES.get(pid),
            })

    if unparsed:
        sys.stderr.write("UNPARSED LINES:\n" + "\n".join(unparsed) + "\n")

    # Emit YAML by hand (deterministic ordering, faithful quoting of PCREs).
    out = []
    out.append("# DSGAI scanner detection rules — source of truth.")
    out.append("# Generated once from dsgai_scanner_tool.md Step 2 by build/generate_rules.py,")
    out.append("# then hand-maintained. Validated by rules/rules.schema.json (see rules/README.md).")
    out.append(f"ruleset_version: '{RULESET_VERSION}'")
    out.append(f"framework: '{FRAMEWORK}'")
    out.append("rules:")
    for r in rules:
        out.append(f"  - id: {r['id']}")
        out.append(f"    control: {r['control']}")
        out.append(f"    name: {r['name']}")
        out.append(f"    classification: {r['classification']}")
        out.append(f"    signal: {r['signal']}")
        out.append(f"    confidence: {r['confidence']}")
        out.append(f"    pcre: {yaml_scalar(r['pcre'])}")
        out.append(f"    file_globs: {emit_list(r['file_globs'])}")
        out.append(f"    exclude_globs: {emit_list(r['exclude_globs'])}")
        out.append(f"    framework: '{r['framework']}'")
        out.append(f"    description: {yaml_scalar(r['description'])}")
        if r["subtract"]:
            out.append(f"    subtract: {emit_list(r['subtract'])}")
        if r["requires_nearby"]:
            rn = r["requires_nearby"]
            parts = []
            if "rule" in rn:
                parts.append(f"rule: {rn['rule']}")
            if "rules" in rn:
                parts.append("rules: " + emit_list(rn["rules"]))
            if "lines" in rn:
                parts.append(f"lines: {rn['lines']}")
            if "scope" in rn:
                parts.append(f"scope: {rn['scope']}")
            if rn.get("absent"):
                parts.append("absent: true")
            out.append("    requires_nearby: {" + ", ".join(parts) + "}")
        if r["gated_on"]:
            out.append(f"    gated_on: {r['gated_on']}")
        if r["notes"]:
            out.append(f"    notes: {yaml_scalar(r['notes'])}")
    sys.stdout.write("\n".join(out) + "\n")
    sys.stderr.write(f"\nExtracted {len(rules)} rules.\n")


if __name__ == "__main__":
    main()
