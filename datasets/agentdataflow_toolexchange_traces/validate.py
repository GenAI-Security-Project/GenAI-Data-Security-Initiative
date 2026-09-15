"""Validate ./example.json and every entry in ./entries/ against ./schema.json.

Usage: python validate.py
Exit code 0 on success, 1 on any validation failure.
Requires: jsonschema (pip install jsonschema)

Beyond schema conformance this checks the things a schema cannot express:
  * trace_id agrees with the filename
  * a non-hypothetical provenance tier actually carries evidence, and each
    evidence citation looks like the kind (doi/cve/ghsa/url) it claims to be
  * the span graph is well formed: no duplicate span_id, and every
    parent_span_id names a span that strictly precedes it (not itself, not a
    later one)
  * spans are listed in non-decreasing t_offset_ms order
  * every span-level finding maps to a risk the trace declares at the top level
  * date_added, date_observed, and every span timestamp are real ISO 8601
    values, in every environment - not only where optional format-checker
    packages happen to be installed
  * no string ANYWHERE in the entry looks like a real credential, key,
    internal hostname, RFC1918 address, home directory path, or credential
    -shaped key=value assignment, and no string carries two or more distinct
    addresses that look like real routable public IPv4 addresses

What this does NOT check, because it cannot be checked mechanically: whether
a `provenance.evidence` citation actually says what its `supports` field
claims, and whether that source is one the contributor owns or controls
(disallowed by the README's provenance rule). Both are reviewer judgment
calls, the same as the sanitization judgment a reviewer already makes on
every entry.

The secret and IP scans are the machine-readable half of the CONTRIBUTING.md
anonymization rule: `sanitization.attestation` is a claim by the contributor,
and this scan is what stops that claim from being the only thing standing
between a real secret and a public dataset. It is pattern-based and will
miss anything that does not match one of the patterns below; it is a floor,
not a guarantee.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
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
    # .local is excluded on purpose: mDNS hostnames of this shape show up in
    # legitimate lab and CTF write-ups, not only in production. .internal,
    # .corp, .lan, and .intra are conventions with no ordinary public use.
    ("internal hostname", re.compile(r"\b[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)+\.(?:internal|corp|lan|intra)\b", re.IGNORECASE)),
    # A key=value or key: value assignment for a credential-shaped field
    # name, wherever it was typed - payload or prose. Excludes the case
    # where the value itself is already a placeholder.
    ("secret-looking assignment", re.compile(r"\b(?:password|passwd|secret|api[_-]?key|access[_-]?key|client[_-]?secret)\s*[:=]\s*(?!<)\S{4,}", re.IGNORECASE)),
    # macOS/Linux only. The Windows arm this used to carry was written
    # against a double backslash (r"[A-Za-z]:\\\\Users\\\\..."), which a
    # JSON string decodes to a single backslash per separator, so it could
    # never match a real entry. Dropped rather than shipped as a check that
    # cannot fire; re-add as r"[A-Za-z]:\\Users\\[^\s\"]+" for real coverage.
    ("user home path", re.compile(r"(/Users/|/home/)[A-Za-z0-9._-]+")),
]

# A single non-loopback, non-RFC1918 IPv4 address is weak evidence on its
# own - plenty of legitimate strings contain four dot-separated numbers
# under 256 that are not addresses. This instead looks for two or more
# DISTINCT such addresses in one string, which is closer to the shape of
# someone pasting real network detail than of an incidental number. The
# RFC 5737 documentation ranges (192.0.2.0/24, 198.51.100.0/24,
# 203.0.113.0/24) are excluded outright: they are the correct way to write
# a fake-but-obviously-fake IP in an example, and this dataset should not
# penalize using them.
_IPV4_RE = re.compile(r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b")


def _is_routable_public_ip(octets: tuple[int, int, int, int]) -> bool:
    a, b, c, d = octets
    if any(o > 255 for o in (a, b, c, d)):
        return False
    if a == 10 or a == 127:
        return False
    if a == 192 and b == 168:
        return False
    if a == 172 and 16 <= b <= 31:
        return False
    if a == 192 and b == 0 and c == 2:  # 192.0.2.0/24 (TEST-NET-1)
        return False
    if a == 198 and b == 51 and c == 100:  # 198.51.100.0/24 (TEST-NET-2)
        return False
    if a == 203 and b == 0 and c == 113:  # 203.0.113.0/24 (TEST-NET-3)
        return False
    if a == 0 or a >= 224:  # this-network / multicast / reserved
        return False
    return True


def scan_for_public_ip_clusters(entry: dict, name: str, errors: list[str]) -> None:
    for jpath, value in walk_strings(entry):
        if PLACEHOLDER_RE.match(value.strip()):
            continue
        found = {m.group(0) for m in _IPV4_RE.finditer(value) if _is_routable_public_ip(tuple(int(g) for g in m.groups()))}
        if len(found) >= 2:
            errors.append(
                f"{name}: {jpath}: value contains {len(found)} distinct addresses that look like "
                f"real routable IPv4 addresses ({', '.join(sorted(found))}); use RFC 5737 documentation "
                f"addresses (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) or a typed placeholder instead"
            )


# An identifier typed as a kind has to look like that kind, or the type field is
# decoration. Types with no single canonical form (advisory, publication,
# vendor_changelog, dataset, registry_record) are left unchecked on purpose.
CITATION_FORMATS: dict[str, tuple[re.Pattern[str], str]] = {
    "doi": (re.compile(r"^10\.\d{4,9}/\S+$"), "a bare DOI (expected form: 10.xxxx/yyyy)"),
    "cve": (re.compile(r"^CVE-\d{4}-\d{4,}$"), "a CVE id (expected form: CVE-YYYY-NNNNN)"),
    "ghsa": (
        re.compile(r"^GHSA-[23456789cfghjmpqrvwx]{4}-[23456789cfghjmpqrvwx]{4}-[23456789cfghjmpqrvwx]{4}$"),
        "a GHSA id (expected form: GHSA-xxxx-xxxx-xxxx)",
    ),
    "url": (re.compile(r"^https?://\S+$"), "an absolute http(s) URL"),
}


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


def check_spans(entry: dict, name: str, errors: list[str]) -> None:
    spans = entry.get("spans", []) or []
    seen: set[str] = set()
    last_offset: int | None = None

    for index, span in enumerate(spans):
        span_id = span.get("span_id", "")
        if span_id in seen:
            errors.append(f"{name}: duplicate span_id {span_id!r}")

        # Checked against the parents seen BEFORE this span, so a span
        # cannot claim itself (or a later span) as its own parent - only a
        # strictly preceding one, which is what "parent precedes child"
        # requires.
        parent = span.get("parent_span_id")
        if parent is not None and parent not in seen:
            errors.append(
                f"{name}: span {span_id!r} has parent_span_id {parent!r}, "
                f"which is not a preceding span"
            )

        seen.add(span_id)

        offset = span.get("t_offset_ms")
        if isinstance(offset, int):
            if last_offset is not None and offset < last_offset:
                errors.append(
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
        rule = CITATION_FORMATS.get(item.get("type", ""))
        if rule is None:
            continue
        pattern, expected = rule
        citation = item.get("citation", "")
        if not pattern.match(citation):
            errors.append(
                f"{name}: provenance.evidence[{i}].citation {citation!r} is typed "
                f"{item['type']!r} but is not {expected}"
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

    # spans[].timestamp is "format": "date-time" in the schema, which is the
    # other field this dataset actually expects contributors to fill in with
    # a real value (an observed or lab trace has wall-clock times; a derived
    # or hypothetical one usually does not). The jsonschema format checker
    # only validates date-time when the optional rfc3339-validator package is
    # installed, so this is hand-rolled the same way date_added is, rather
    # than trusting the schema to have caught it.
    for index, span in enumerate(entry.get("spans", []) or []):
        ts = span.get("timestamp")
        if ts is None:
            continue
        try:
            datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        except (ValueError, TypeError):
            span_id = span.get("span_id", f"index {index}")
            errors.append(
                f"{name}: span {span_id!r} timestamp {ts!r} is not an ISO 8601 date-time"
            )


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        schema, format_checker=Draft202012Validator.FORMAT_CHECKER
    )
    taxonomy_ids = load_taxonomy_ids()

    errors: list[str] = []
    warnings: list[str] = []
    if not taxonomy_ids:
        warnings.append(
            f"{TAXONOMY_PATH} not found or empty - dsgai_mapping values were NOT "
            f"cross-checked against the shared taxonomy this run"
        )
    entry_files = sorted(ENTRIES_DIR.glob("*.json")) if ENTRIES_DIR.exists() else []

    # The worked example is validated too. An example that does not validate is
    # a trap for the next contributor, and it is the only thing to validate
    # while entries/ is still empty, so an empty dataset is a pass and not an
    # error.
    example_path = ROOT / "example.json"
    if not entry_files and not example_path.exists():
        sys.stderr.write(f"Nothing to validate: no entries in {ENTRIES_DIR}, no example.json\n")
        return 1
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
        check_spans(entry, name, errors)
        check_findings(entry, name, errors)
        check_dates(entry, name, errors)
        scan_for_secrets(entry, name, errors)
        scan_for_public_ip_clusters(entry, name, errors)

    for line in warnings:
        print(f"WARN  {line}")

    if errors:
        for line in errors:
            print(f"ERROR {line}")
        print(f"\nFAIL: {len(errors)} issue(s) across {len(checked)} files.")
        return 1

    if entry_files:
        print(f"OK: {len(entry_files)} entries + example.json validated against schema.")
    else:
        print("OK: example.json validated against schema. entries/ is empty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
