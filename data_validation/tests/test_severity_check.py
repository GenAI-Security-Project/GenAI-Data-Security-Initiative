"""Tests for severity_check.py."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import severity_check as sc  # noqa: E402
from validators._common import ERROR, WARN  # noqa: E402

V3 = "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H"  # 8.8 High
V4 = "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N"  # 9.3 Critical


def levels(sev: dict) -> list[str]:
    return [f.level for f in sc.check_data(Path("e.json"), {"severity": sev})]


@pytest.mark.parametrize("score,band", [(0.0, "None"), (0.1, "Low"), (3.9, "Low"), (4.0, "Medium"),
                                        (6.9, "Medium"), (7.0, "High"), (8.9, "High"), (9.0, "Critical"), (10.0, "Critical")])
def test_first_bands(score, band):
    assert sc.first_band(score) == band


def test_consistent_v3_and_v4_pass():
    assert levels({"qualitative": "High", "cvss_v3_score": 8.8, "cvss_v3_vector": V3}) == []
    assert levels({"qualitative": "Critical", "cvss_v4_score": 9.3, "cvss_v4_vector": V4}) == []


def test_score_not_matching_vector():
    assert levels({"qualitative": "High", "cvss_v3_score": 8.1, "cvss_v3_vector": V3}) == [ERROR]


def test_qualitative_outside_band():
    """The case found in the vulnerability dataset: 8.8 labelled Critical."""
    assert levels({"qualitative": "Critical", "cvss_v3_score": 8.8, "cvss_v3_vector": V3}) == [ERROR]


def test_v4_score_sets_the_band():
    sev = {"qualitative": "Critical", "cvss_v3_score": 8.8, "cvss_v3_vector": V3, "cvss_v4_score": 9.3, "cvss_v4_vector": V4}
    assert levels(sev) == []


def test_invalid_vector():
    assert levels({"qualitative": "High", "cvss_v3_vector": "CVSS:3.1/AV:X"}) == [ERROR]


def test_vector_without_score_still_sets_band():
    assert levels({"qualitative": "Low", "cvss_v3_vector": V3}) == [ERROR]


def test_score_without_vector_warns():
    assert levels({"qualitative": "High", "cvss_v3_score": 8.8}) == [WARN]


def test_no_cvss_is_fine():
    assert levels({"qualitative": "High"}) == []
