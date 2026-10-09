"""Tests for cvss_score.py, the in-house CVSS v3.x and v4.0 scorer."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators.cvss_score import CVSSError, base_score  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_v4_matches_the_first_reference_calculator():
    """500 vectors (base, threat and environmental metrics) scored by cvss40.js."""
    reference = json.loads((FIXTURES / "cvss40_reference_scores.json").read_text(encoding="utf-8"))
    assert len(reference) == 500
    mismatches = [(v, s, base_score(v)) for v, s in reference if base_score(v) != s]
    assert mismatches == []


@pytest.mark.parametrize("vector,score", [
    # Published NVD/CNA scores
    ("CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H", 8.8),
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H", 9.6),
    ("CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N", 6.4),
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N", 9.3),
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N", 7.5),
    ("CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", 9.8),
    ("CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:N", 0.0),
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O", 9.8),  # temporal metrics don't change the base
    ("CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N", 9.3),
])
def test_known_scores(vector, score):
    assert base_score(vector) == score


@pytest.mark.parametrize("vector", [
    "CVSS:3.1/AV:X/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",   # bad value
    "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H",       # missing A
    "CVSS:3.1/AV:N/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",  # duplicate
    "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N",  # missing SA
    "CVSS:2.0/AV:N",
    "AV:N/AC:L/Au:N/C:P/I:P/A:P",
])
def test_invalid_vectors(vector):
    with pytest.raises(CVSSError):
        base_score(vector)
