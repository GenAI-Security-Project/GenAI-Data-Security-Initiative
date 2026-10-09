"""
Checks licence and language metadata against their standards.

Licences (fields named "license", "licence" or ending in "_license"):
ERROR: a value that does not resolve to exactly one licence on the SPDX
       License List. Accepted forms: an SPDX ID or expression
       ("CC-BY-4.0", "MIT OR Apache-2.0"), or an SPDX full name, optionally
       followed by its short form in parentheses ("Creative Commons
       Attribution 4.0 International (CC BY 4.0)"). The ID is preferred.
WARN:  an SPDX ID the list has deprecated.

Languages (fields named "language", "languages" or ending in "_language"):
ERROR: a value that is not a well-formed BCP 47 tag whose language, script
       and region subtags are in the IANA Language Subtag Registry
       ("tr", "kmr", "pt-BR", "zh-Hant").
WARN:  a deprecated subtag.
Fields ending in "_label" are not checked: they carry a source's own label
verbatim.

Usage:
    python metadata_check.py --dataset ../../datasets/promptinj_dataextraction_testcases/
    python metadata_check.py                    # every dataset
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from functools import cache
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT,
    ERROR,
    REFERENCE_DIR,
    WARN,
    Finding,
    add_target_args,
    ensure_utf8_stdout,
    load_json,
    print_findings,
    resolve_targets,
    walk_strings,
)

CHECK = "metadata"
LICENSE_KEY_RE = re.compile(r"^(licen[cs]e|.*_licen[cs]e)$", re.IGNORECASE)
LANGUAGE_KEY_RE = re.compile(r"^(language|languages|.*_language)$", re.IGNORECASE)
# language[-script][-region], the subset of BCP 47 these datasets need;
# variants, extensions and private-use tags are rejected as malformed.
BCP47_RE = re.compile(r"^(?P<language>[A-Za-z]{2,3})(?:-(?P<script>[A-Za-z]{4}))?(?:-(?P<region>[A-Za-z]{2}|\d{3}))?$")


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


@cache
def spdx() -> dict[str, dict]:
    """Lookups over the SPDX License List: by ID (case-insensitive, as SPDX
    specifies), by normalized ID (for short forms such as "CC BY 4.0" in
    parentheses), and by normalized full name."""
    by_id: dict[str, tuple[str, str, bool]] = {}
    by_norm_id: dict[str, tuple[str, str, bool]] = {}
    by_name: dict[str, tuple[str, str, bool]] = {}
    with open(REFERENCE_DIR / "spdx_licenses.csv", newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            entry = (row["spdx_id"], row["type"], row["deprecated"] == "true")
            by_id[row["spdx_id"].lower()] = entry
            if row["type"] == "license":
                by_norm_id.setdefault(_norm(row["spdx_id"]), entry)
                by_name.setdefault(_norm(row["name"]), entry)
    return {"id": by_id, "norm_id": by_norm_id, "name": by_name}


@cache
def subtags() -> dict[tuple[str, str], bool]:
    """{(type, lowercased subtag): deprecated}."""
    with open(REFERENCE_DIR / "language_subtags.csv", newline="", encoding="utf-8") as fh:
        return {(r["type"], r["subtag"].lower()): r["deprecated"] == "true" for r in csv.DictReader(fh)}


def resolve_license(value: str) -> tuple[list[str], list[str]]:
    """(SPDX IDs the value names, problems). An expression may name several."""
    t = spdx()
    text = value.strip()
    # "Full Name (Short Form)": both halves must name the same licence.
    m = re.fullmatch(r"(.+?)\s*\(([^()]+)\)", text)
    if m and _norm(m.group(1)) in t["name"]:
        full = t["name"][_norm(m.group(1))][0]
        short = t["norm_id"].get(_norm(m.group(2)))
        if short and short[0] != full:
            return [], [f"{m.group(1)!r} is {full} but {m.group(2)!r} is {short[0]}"]
        return [full], []
    if _norm(text) in t["name"]:
        return [t["name"][_norm(text)][0]], []
    found, problems = [], []
    after_with = False
    for token in re.split(r"\s+|[()]", text):
        if not token or token in ("AND", "OR"):
            continue
        if token == "WITH":  # noqa: S105 - the SPDX operator, not a password
            after_with = True
            continue
        hit = t["id"].get(token.lower()) or t["id"].get(token.rstrip("+").lower())
        wanted = "exception" if after_with else "license"
        after_with = False
        if hit is None or hit[1] != wanted:
            return [], [f"{value!r} is not an SPDX licence ID, expression or full name (e.g. CC-BY-4.0)"]
        found.append(hit[0])
        if hit[2]:
            problems.append(f"{hit[0]} is deprecated on the SPDX License List")
    return found, problems


def check_language(tag: str) -> tuple[str, str] | None:
    """(level, message) for a bad tag, else None."""
    m = BCP47_RE.match(tag.strip())
    if not m:
        return ERROR, f"{tag!r} is not a BCP 47 language tag (e.g. tr, en-GB, zh-Hant)"
    known = subtags()
    for kind in ("language", "script", "region"):
        part = m.group(kind)
        if part is None:
            continue
        key = (kind, part.lower())
        if key not in known:
            return ERROR, f"{tag!r}: {part!r} is not a {kind} subtag in the IANA Language Subtag Registry"
        if known[key]:
            return WARN, f"{tag!r}: the {kind} subtag {part!r} is deprecated in the IANA registry"
    return None


def check_data(path: Path, data) -> list[Finding]:
    findings: list[Finding] = []
    for pointer, key, value in walk_strings(data):
        if key is None or key.lower().endswith("_label") or value.strip().startswith(("http://", "https://")):
            continue
        if LICENSE_KEY_RE.match(key):
            found, problems = resolve_license(value)
            level = WARN if found else ERROR
            findings += [Finding(level, CHECK, path, pointer, p) for p in problems]
        elif LANGUAGE_KEY_RE.match(key):
            problem = check_language(value)
            if problem:
                findings.append(Finding(problem[0], CHECK, path, pointer, problem[1]))
    return findings


def check_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check licences (SPDX) and language tags (BCP 47)")
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
