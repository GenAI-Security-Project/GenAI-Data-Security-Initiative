"""Validate every entry in ./entries/ against ./schema.json.

Usage: python validate.py
Exit code 0 on success, 1 on any validation failure.
Requires: jsonschema (pip install jsonschema)

Beyond schema conformance this checks the things a schema cannot express:
  * trace_id agrees with the filename
  * a non-hypothetical provenance tier actually carries evidence
  * the span graph is well formed and parents precede children
  * every span-level finding maps to a risk the trace declares at the top level
  * ISO dates are real dates, in every environment
  * no string ANYWHERE in the entry looks like a real credential, key,
    address, or host path

The last check is the machine-readable half of the CONTRIBUTING.md anonymization
rule: `sanitization.attestation` is a claim by the contributor, and this scan is
what stops that claim from being the only thing standing between a real secret
and a public dataset.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write("jsonschema not installed. Run: pip install jsonschema\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "schema.json"
ENTRIES_DIR = ROOT / "entries"
TAXONOMY_PATH = ROOT.parent / "_shared" / "dsgai_taxonomy.json"

# A value that is entirely a placeholder is exempt from the secret scan.
PLACEHOLDER_RE = re.compile(r"^<[^<>]+>$")

# Each pattern needs a context cue, not just entropy: a bare hex or base64 run
# over-matches on digests, ids, and hashes that are perfectly fine to publish.
SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("openai-style key", re.compile(r"\bsk-[A-Za-z0-9]{16,}")),
    ("aws access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github token", re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}")),
    ("github fine-grained pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("slack token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("google api key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("json web token", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("bearer credential", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/-]{20,}")),
    ("email address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("rfc1918 address", re.compile(r"\b(10\.\d{1,3}|192\.168|172\.(1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b")),
    ("user home path", re.compile(r"(/Users/|/home/|[A-Za-z]:\\\\Users\\\\)[A-Za-z0-9._-]+")),
]


def load_taxonomy_ids() -> set[str]:
    if not TAXONOMY_PATH.exists():
        return set()
    data = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    return {e["id"] for e in data.get("entries", [])}


def walk_strings(node, path: str = ""):
    """Yield (json_path, string) for every string anywhere under `node`."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk_strings(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk_strings(value, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def scan_for_secrets(entry: dict, name: str, errors: list[str]) -> None:
    """Scan the WHOLE entry, not just span payloads.

    Payloads are the obvious place for a leaked value, but they are not the
    likely one. A contributor writing `summary`, `notes`, `collection_method`,
    or an evidence `locator` is writing prose while looking at a real trace,
    which is exactly when a real hostname or address gets typed out. A scan
    narrower than the attestation it backs is worse than no scan, because it
    reads as coverage.
    """
    for jpath, value in walk_strings(entry):
        if PLACEHOLDER_RE.match(value.strip()):
            continue
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(value):
                errors.append(
                    f"{name}: {jpath}: value looks like a real {label}; "
                    f"replace with a typed placeholder such as <redacted:{label.replace(' ', '-')}>"
                )
                break


def check_spans(entry: dict, name: str, errors: list[str], warnings: list[str]) -> None:
    spans = entry.get("spans", []) or []
    seen: set[str] = set()
    last_offset: int | None = None

    for index, span in enumerate(spans):
        span_id = span.get("span_id", "")
        if span_id in seen:
            errors.append(f"{name}: duplicate span_id {span_id!r}")
        seen.add(span_id)

        parent = span.get("parent_span_id")
        if parent is not None and parent not in seen:
            errors.append(
                f"{name}: span {span_id!r} has parent_span_id {parent!r}, "
                f"which is not a preceding span"
            )

        offset = span.get("t_offset_ms")
        if isinstance(offset, int):
            if last_offset is not None and offset < last_offset:
                warnings.append(
                    f"{name}: span {span_id!r} (index {index}) moves t_offset_ms backwards "
                    f"({last_offset} -> {offset}); spans should be listed in temporal order"
                )
            last_offset = offset


def check_findings(entry: dict, name: str, errors: list[str]) -> None:
    declared = set(entry.get("dsgai_mapping", []) or [])
    for span in entry.get("spans", []) or []:
        finding = span.get("finding")
        if not finding:
            continue
        risk = finding.get("dsgai_id", "")
        if risk not in declared:
            errors.append(
                f"{name}: span {span.get('span_id', '?')!r} has a finding for {risk}, "
                f"which is not in the trace's dsgai_mapping {sorted(declared)}"
            )


def check_provenance(entry: dict, name: str, errors: list[str]) -> None:
    prov = entry.get("provenance", {}) or {}
    tier = prov.get("tier", "")
    evidence = prov.get("evidence") or []
    if tier != "hypothetical" and not evidence:
        errors.append(
            f"{name}: provenance.tier is {tier!r}, which requires at least one "
            f"entry in provenance.evidence. Use tier 'hypothetical' if the trace "
            f"has no citable backing."
        )
    for i, item in enumerate(evidence):
        if item.get("type") == "doi":
            citation = item.get("citation", "")
            if not re.match(r"^10\.\d{4,9}/\S+$", citation):
                errors.append(
                    f"{name}: provenance.evidence[{i}].citation {citation!r} is typed "
                    f"'doi' but is not a bare DOI (expected form: 10.xxxx/yyyy)"
                )


def check_dates(entry: dict, name: str, errors: list[str]) -> None:
    """Check ISO dates with the stdlib.

    `"format": "date"` in the schema is an annotation, not a constraint, unless
    a format checker is wired in - and the checkers for `date-time` and `uri`
    need optional packages that may or may not be installed. FORMAT_CHECKER is
    enabled below for whatever it can cover; this function guarantees the date
    fields are checked in every environment regardless.
    """
    for field in ("date_added", "date_observed"):
        value = entry.get(field)
        if value is None:
            continue
        try:
            date.fromisoformat(value)
        except (ValueError, TypeError):
            errors.append(f"{name}: {field} {value!r} is not an ISO 8601 date (YYYY-MM-DD)")


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        schema, format_checker=Draft202012Validator.FORMAT_CHECKER
    )
    taxonomy_ids = load_taxonomy_ids()

    errors: list[str] = []
    warnings: list[str] = []
    entry_files = sorted(ENTRIES_DIR.glob("*.json"))
    if not entry_files:
        sys.stderr.write(f"No entries found in {ENTRIES_DIR}\n")
        return 1

    # The worked example is validated too. An example that does not validate is
    # a trap for the next contributor.
    example_path = ROOT / "example.json"
    checked = entry_files + ([example_path] if example_path.exists() else [])

    for path in checked:
        name = path.name
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{name}: invalid JSON - {e}")
            continue

        for err in validator.iter_errors(entry):
            loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
            errors.append(f"{name}: {loc}: {err.message}")

        trace_id = entry.get("trace_id", "")
        if trace_id and path.parent == ENTRIES_DIR and trace_id != path.stem:
            errors.append(
                f"{name}: trace_id {trace_id!r} does not match the filename stem {path.stem!r}"
            )

        if taxonomy_ids:
            for dsgai_id in entry.get("dsgai_mapping", []) or []:
                if dsgai_id not in taxonomy_ids:
                    errors.append(f"{name}: dsgai_mapping {dsgai_id!r} not in taxonomy")

        check_provenance(entry, name, errors)
        check_spans(entry, name, errors, warnings)
        check_findings(entry, name, errors)
        check_dates(entry, name, errors)
        scan_for_secrets(entry, name, errors)

    for line in warnings:
        print(f"WARN  {line}")

    if errors:
        for line in errors:
            print(f"ERROR {line}")
        print(f"\nFAIL: {len(errors)} issue(s) across {len(checked)} files.")
        return 1

    print(f"OK: {len(entry_files)} entries + example.json validated against schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
