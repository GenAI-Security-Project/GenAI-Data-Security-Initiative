"""Tests for metadata_check.py (SPDX licences, BCP 47 language tags)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import metadata_check as mc  # noqa: E402
from validators._common import ERROR, WARN  # noqa: E402


def levels(data) -> list[str]:
    return [f.level for f in mc.check_data(Path("e.json"), data)]


@pytest.mark.parametrize("value,ids", [
    ("CC-BY-4.0", ["CC-BY-4.0"]),
    ("cc-by-4.0", ["CC-BY-4.0"]),
    ("MIT OR Apache-2.0", ["MIT", "Apache-2.0"]),
    ("(MIT AND BSD-3-Clause)", ["MIT", "BSD-3-Clause"]),
    ("Apache-2.0 WITH LLVM-exception", ["Apache-2.0", "LLVM-exception"]),
    ("GPL-2.0-only", ["GPL-2.0-only"]),
    ("Creative Commons Attribution 4.0 International (CC BY 4.0)", ["CC-BY-4.0"]),
    ("Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)", ["CC-BY-SA-4.0"]),
])
def test_licences_that_resolve(value, ids):
    assert mc.resolve_license(value) == (ids, [])


@pytest.mark.parametrize("value", ["CC BY 4.0", "my own license", "MIT WITH MIT",
                                   "Creative Commons Attribution 4.0 International (CC BY-SA 4.0)"])
def test_licences_that_do_not(value):
    found, problems = mc.resolve_license(value)
    assert found == [] and problems


def test_deprecated_licence_warns():
    assert levels({"license": "GPL-2.0"}) == [WARN]


@pytest.mark.parametrize("tag", ["tr", "en", "kmr", "pt-BR", "zh-Hant", "zh-Hant-TW", "es-419", "en-us"])
def test_language_tags_that_pass(tag):
    assert mc.check_language(tag) is None


@pytest.mark.parametrize("tag,level", [("xx", ERROR), ("tr-en", ERROR), ("english", ERROR), ("en_US", ERROR), ("iw", WARN)])
def test_language_tags_that_fail(tag, level):
    assert mc.check_language(tag)[0] == level


def test_field_selection():
    assert levels({"source_license_url": "https://creativecommons.org/licenses/by/4.0/",
                   "source_language_label": "tr-en", "language": "tr", "languages": ["tr", "en"]}) == []
    assert levels({"adaptation_license": "nonsense", "encoded_payload_language": "zz"}) == [ERROR, ERROR]
