"""Tests for date_check.py."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators import date_check as dc  # noqa: E402
from validators._common import ERROR  # noqa: E402

TODAY = date(2026, 10, 9)


def levels(data) -> list[str]:
    return [f.level for f in dc.check_data(Path("e.json"), data, TODAY)]


def test_valid_dates_pass():
    assert levels({"date_added": "2026-05-18", "date_reported": "2024-06-01",
                   "spans": [{"timestamp": "2025-01-01T10:00:00Z"}]}) == []


def test_tomorrow_is_allowed_for_time_zones():
    assert levels({"date_added": "2026-10-10"}) == []


def test_future_and_malformed_dates():
    assert levels({"date_added": "2026-10-12"}) == [ERROR]
    assert levels({"date_added": "18/05/2026"}) == [ERROR]
    assert levels({"date_reported": "2024-13-01"}) == [ERROR]


def test_documented_after_added():
    assert levels({"date_added": "2025-01-01", "date_documented": "2025-02-01"}) == [ERROR]
    assert levels({"date_added": "2025-01-01", "date_reported": "2024-12-31"}) == []


def test_placeholders_are_exempt():
    assert levels({"payload": {"updated_at": "<synthetic:iso8601>"}}) == []


def test_non_date_keys_are_ignored():
    assert levels({"update": "soon", "dated_reference": "n/a"}) == []


def test_order_message_names_the_offending_date():
    [f] = dc.check_data(Path("e.json"), {"date_added": "2025-01-01", "date_documented": "2025-02-01"}, TODAY)
    assert f.message == "date_documented 2025-02-01 is after date_added 2025-01-01"
