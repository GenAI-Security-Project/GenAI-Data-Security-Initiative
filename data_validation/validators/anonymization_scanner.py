"""
Scans data files for things that look like residual PII, credentials or
internal network detail.

Every hit is a WARN: the patterns cannot tell a real secret from a synthetic
one, and the prompt-injection datasets contain fake credentials on purpose.
A reviewer decides. Use obviously fake values to stay quiet: RFC 2606
domains (example.com, *.example, *.test, *.invalid), RFC 5737 documentation
addresses (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24), or a placeholder
in angle or square brackets such as <API_KEY> or [API_KEY].

The patterns match the ones in
datasets/agentdataflow_toolexchange_traces/validate.py, which fails its own
dataset on them.

Usage:
    python anonymization_scanner.py --file ../../datasets/rag_dataset/entries/RAG-0001.json
    python anonymization_scanner.py              # every dataset
"""
from __future__ import annotations

import argparse
import ipaddress
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, WARN, Finding, add_target_args, ensure_utf8_stdout,
    load_json, print_findings, resolve_targets, walk_strings,
)

CHECK = "anonymization"

PII_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("email address", re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b")),
    ("openai-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}")),
    ("aws access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}")),
    ("github fine-grained pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("slack token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("google api key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("json web token", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("bearer credential", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/-]{20,}")),
    ("secret-looking assignment", re.compile(
        r"\b(?:password|passwd|secret|api[_-]?key|access[_-]?key|client[_-]?secret)\s*[:=]\s*(?![<\[{]|\.{3}|\*{3})\S{4,}", re.IGNORECASE)),
    ("us social security number", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("internal hostname", re.compile(
        r"\b[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)+\.(?:internal|corp|lan|intra)\b",
        re.IGNORECASE)),
    ("user home path", re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\)[A-Za-z0-9._-]+")),
]

IPV4_RE = re.compile(r"(?<![\d.])(\d{1,3}(?:\.\d{1,3}){3})(?![\d.])")
# Four dotted numbers are as often a product version (23.12.4.0) as an
# address, so a public address is only reported in a network context: after
# "://" or "@", or followed by a port.
NET_CONTEXT_BEFORE = ("://", "@")
PORT_AFTER_RE = re.compile(r":\d{1,5}\b")
PLACEHOLDER_RE = re.compile(r"^(?:<[^<>]+>|\[[^\[\]]+\])$")
RESERVED_EMAIL_DOMAINS = re.compile(r"(^|\.)(example\.(com|org|net)|example|test|invalid|localhost)$", re.IGNORECASE)
DOC_NETWORKS = [ipaddress.ip_network(n) for n in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")]


def _ip_finding(text: str, before: str, after: str) -> str | None:
    try:
        ip = ipaddress.ip_address(text)
    except ValueError:
        return None  # e.g. a version number like 1.2.300.4
    # Link-local covers 169.254.169.254, the well-known cloud metadata address
    # that SSRF write-ups cite; it identifies no one.
    if (any(ip in n for n in DOC_NETWORKS) or ip.is_loopback or ip.is_unspecified
            or ip.is_multicast or ip.is_link_local):
        return None
    if ip.is_private:
        return "private ip address"
    if before.endswith(NET_CONTEXT_BEFORE) or PORT_AFTER_RE.match(after):
        return "public ip address"
    return None


def scan_value(value: str) -> list[tuple[str, str]]:
    """(kind, matched text) for each suspicious thing in one string."""
    if PLACEHOLDER_RE.match(value.strip()):
        return []
    hits = []
    for kind, pattern in PII_PATTERNS:
        for m in pattern.finditer(value):
            text = m.group(0)
            if kind == "email address" and RESERVED_EMAIL_DOMAINS.search(text.split("@", 1)[1]):
                continue
            hits.append((kind, text))
    for m in IPV4_RE.finditer(value):
        kind = _ip_finding(m.group(1), value[:m.start()], value[m.end():])
        if kind:
            hits.append((kind, m.group(1)))
    return hits


def _redact(text: str) -> str:
    return text if len(text) <= 12 else f"{text[:8]}...{text[-2:]}"


def check_data(path: Path, data) -> list[Finding]:
    findings = []
    for pointer, _key, value in walk_strings(data):
        for kind, text in scan_value(value):
            findings.append(Finding(WARN, CHECK, path, pointer, f"looks like a {kind}: {_redact(text)!r}"))
    return findings


def scan_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Scan for residual PII, credentials and internal network detail")
    add_target_args(parser)
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    findings = [f for p in files for f in scan_file(p)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
