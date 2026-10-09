"""Tests for anonymization_scanner.py."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import anonymization_scanner as an  # noqa: E402
from validators._common import WARN  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def kinds(value: str) -> set[str]:
    return {k for k, _ in an.scan_value(value)}


def test_clean_entry():
    assert an.scan_file(FIXTURES / "valid_incident.json") == []


def test_pii_detected():
    findings = an.scan_file(FIXTURES / "incident_with_pii.json")
    assert findings and all(f.level == WARN for f in findings)
    found = " ".join(f.message for f in findings)
    for kind in ("email address", "private ip address", "openai-style key"):
        assert kind in found


@pytest.mark.parametrize("value,kind", [
    ("contact jane.doe@realcorp.io", "email address"),
    ("key AKIAABCDEFGHIJKLMNOP", "aws access key id"),
    ("token ghp_abcdefghijklmnopqrstuvwxyz0123", "github token"),
    ("-----BEGIN RSA PRIVATE KEY-----", "private key block"),
    ("password=hunter2!", "secret-looking assignment"),
    ("db at db01.prod.corp", "internal hostname"),
    ("see /home/alice/.ssh", "user home path"),
    ("callback to http://8.8.8.8/x", "public ip address"),
    ("listening on 8.8.4.4:8080", "public ip address"),
    ("SSN 123-45-6789", "us social security number"),
])
def test_patterns(value, kind):
    assert kind in kinds(value)


@pytest.mark.parametrize("value", [
    "mail admin@example.com or ops@service.test",
    "documentation address 192.0.2.10 and 203.0.113.5:443",
    "cloud metadata endpoint 169.254.169.254",
    "fixed in versions 23.12.4.0 through 24.7.4.1",
    "API_KEY=<REDACTED>",
    "API_KEY=[SYNTHETIC_KEY]",
    "<API_KEY>",
    "password: ...",
])
def test_safe_values_are_not_flagged(value):
    assert kinds(value) == set()


def test_long_matches_are_redacted_in_messages():
    [f] = an.check_data(Path("e.json"), {"k": "sk-proj-abcdefghijklmnopqrstuvwx"})
    assert "abcdefghijklmnop" not in f.message
