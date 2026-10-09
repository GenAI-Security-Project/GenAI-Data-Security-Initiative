"""
Checks CVE, GHSA, CWE, MITRE ATLAS, OWASP Top 10 and NIST AI 100-2
identifiers.

ERROR: a field whose whole value is meant to be one of these IDs but is
       malformed (e.g. "CVE-24-1234"); a CVE year in the future; a CWE ID
       that is not in reference_data/cwe_ids.csv; an ATLAS technique ID that
       is not in reference_data/mitre_atlas_techniques.csv; an OWASP Top 10
       ID with an edition year (LLM01:2026, ASI01:2026) that is not in
       reference_data/owasp_top10.csv; a NIST AI 100-2 ID (NISTAML.018) not
       in reference_data/nist_ai_100_2.csv. ATLAS, CWE, OWASP and NIST IDs
       are checked wherever they appear, including free text.
WARN:  a CWE that MITRE has deprecated, or an ATLAS ID that a later ATLAS
       release retired (merged into another technique); an OWASP ID with
       no edition year (LLM03 was Supply Chain in 2025 and is Excessive
       Agency in 2026, so a bare ID is ambiguous); something in free text that starts
       like an ID but is malformed (often a placeholder such as CVE-XXXX-XXXX).

CVE and GHSA IDs are format-checked only: there is no offline list to check
that they exist. Framework control IDs (ISO, NIST, CIS) are not checked; see
reference_data/SOURCES.md.

Usage:
    python crossref_validator.py --file ../../datasets/exploit_dataset/entries/AML.T0051.json
    python crossref_validator.py                # every dataset
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date
from functools import lru_cache
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, REFERENCE_DIR, WARN, Finding, add_target_args,
    ensure_utf8_stdout, load_json, print_findings, resolve_targets, walk_strings,
)

CHECK = "crossref"

# (name, strict full form, loose "starts like one" form)
ID_KINDS = (
    ("CVE", re.compile(r"CVE-(\d{4})-\d{4,}"), re.compile(r"\bCVE-[A-Za-z0-9-]+")),
    ("GHSA", re.compile(r"GHSA(-[23456789cfghjmpqrvwx]{4}){3}"), re.compile(r"\bGHSA-[A-Za-z0-9-]+")),
    ("CWE", re.compile(r"CWE-\d+"), re.compile(r"\bCWE-[A-Za-z0-9]+")),
    ("ATLAS", re.compile(r"AML\.T\d{4}(\.\d{3})?"), re.compile(r"\bAML\.T[A-Za-z0-9.]*[A-Za-z0-9]")),
)


@lru_cache(maxsize=None)
def atlas_status() -> dict[str, str]:
    with open(REFERENCE_DIR / "mitre_atlas_techniques.csv", newline="", encoding="utf-8") as fh:
        return {row["technique_id"]: row["status"] for row in csv.DictReader(fh)}


@lru_cache(maxsize=None)
def owasp_ids() -> frozenset[str]:
    with open(REFERENCE_DIR / "owasp_top10.csv", newline="", encoding="utf-8") as fh:
        return frozenset(row["id"] for row in csv.DictReader(fh))


OWASP_RE = re.compile(r"\b(?:LLM|ASI)\d{2}(?::\d{4})?\b")


def check_owasp(path: Path, pointer: str, value: str) -> list[Finding]:
    findings = []
    for m in OWASP_RE.finditer(value):
        token = m.group(0)
        if ":" not in token:
            findings.append(Finding(WARN, CHECK, path, pointer,
                                    f"{token} has no edition year; write {token}:2025 or {token}:2026"))
        elif token not in owasp_ids():
            findings.append(Finding(ERROR, CHECK, path, pointer,
                                    f"{token} is not an OWASP Top 10 entry (not in reference_data/owasp_top10.csv)"))
    return findings


@lru_cache(maxsize=None)
def nist_aml_ids() -> frozenset[str]:
    with open(REFERENCE_DIR / "nist_ai_100_2.csv", newline="", encoding="utf-8") as fh:
        return frozenset(row["id"] for row in csv.DictReader(fh))


NIST_RE = re.compile(r"NISTAML\.\d+")


def check_nist(path: Path, pointer: str, value: str) -> list[Finding]:
    return [Finding(ERROR, CHECK, path, pointer,
                    f"{m.group(0)} is not a NIST AI 100-2e2025 identifier (not in reference_data/nist_ai_100_2.csv)")
            for m in NIST_RE.finditer(value) if m.group(0) not in nist_aml_ids()]


@lru_cache(maxsize=None)
def cwe_status() -> dict[str, str]:
    with open(REFERENCE_DIR / "cwe_ids.csv", newline="", encoding="utf-8") as fh:
        return {row["cwe_id"]: row["status"] for row in csv.DictReader(fh)}


def _check_id(kind: str, value: str, m: re.Match) -> tuple[str, str] | None:
    """(level, message) for a well-formed ID that is still wrong, else None."""
    if kind == "CVE" and int(m.group(1)) > date.today().year:
        return ERROR, f"{value}: CVE year is in the future"
    if kind == "CWE":
        status = cwe_status().get(value)
        if status is None:
            return ERROR, f"{value} is not a CWE ID (not in reference_data/cwe_ids.csv)"
        if status == "Deprecated":
            return WARN, f"{value} is deprecated by MITRE; use the CWE it points to"
    if kind == "ATLAS":
        status = atlas_status().get(value)
        if status is None:
            return ERROR, f"{value} is not a MITRE ATLAS technique (not in reference_data/mitre_atlas_techniques.csv)"
        if status == "retired":
            return WARN, f"{value} was retired by MITRE ATLAS; check the ATLAS changelog for the technique that replaced it"
    return None


def check_data(path: Path, data) -> list[Finding]:
    findings: list[Finding] = []
    for pointer, _key, value in walk_strings(data):
        findings += check_owasp(path, pointer, value)
        findings += check_nist(path, pointer, value)
        stripped = value.strip()
        whole_value = False
        for kind, strict, loose in ID_KINDS:
            if not loose.fullmatch(stripped):
                continue
            # The whole value is meant to be an ID of this kind.
            whole_value = True
            m = strict.fullmatch(stripped)
            if not m:
                findings.append(Finding(ERROR, CHECK, path, pointer, f"{stripped!r} is not a well-formed {kind} ID"))
            elif problem := _check_id(kind, stripped, m):
                findings.append(Finding(problem[0], CHECK, path, pointer, problem[1]))
        if whole_value:
            continue
        for kind, strict, loose in ID_KINDS:
            for token in loose.finditer(value):
                text = token.group(0)
                m = strict.match(text)
                if not m or m.end() != len(text):
                    # "CVE-2024-1234-style" or a sub-technique suffix is not malformed.
                    if m and kind in ("CVE", "GHSA", "CWE") and text[m.end()] == "-":
                        text = m.group(0)
                    else:
                        findings.append(Finding(WARN, CHECK, path, pointer, f"{text!r} looks like a {kind} ID but is not well-formed"))
                        continue
                if problem := _check_id(kind, m.group(0), m):
                    findings.append(Finding(problem[0], CHECK, path, pointer, problem[1]))
    return findings


def check_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check CVE, GHSA, CWE, MITRE ATLAS, OWASP Top 10 and NIST AI 100-2 identifiers")
    add_target_args(parser)
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    findings = [f for p in files for f in check_file(p)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
