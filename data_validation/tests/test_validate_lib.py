"""Tests for datasets/_shared/validate_lib.py, the core of the dataset validators."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "datasets" / "_shared"))

import validate_lib  # noqa: E402

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["item_id", "date_added"],
    "properties": {"item_id": {"type": "string"}, "date_added": {"type": "string", "format": "date"},
                   "dsgai_mapping": {"type": "array"}},
}


def make(tmp_path: Path, entries: dict[str, dict]) -> Path:
    (tmp_path / "schema.json").write_text(json.dumps(SCHEMA))
    (tmp_path / "entries").mkdir()
    for name, entry in entries.items():
        (tmp_path / "entries" / f"{name}.json").write_text(json.dumps(entry))
    return tmp_path


def run(tmp_path, capsys, **kwargs) -> tuple[int, str]:
    code = validate_lib.run(tmp_path, id_field="item_id", **kwargs)
    return code, capsys.readouterr().out


def test_valid_entries_pass(tmp_path, capsys):
    make(tmp_path, {"A-1": {"item_id": "A-1", "date_added": "2026-01-01", "dsgai_mapping": ["DSGAI01"]}})
    assert run(tmp_path, capsys) == (0, "OK: 1 entries validated against schema.\n")


@pytest.mark.parametrize("entry,expected", [
    ({"item_id": "A-1"}, "'date_added' is a required property"),
    ({"item_id": "A-1", "date_added": "2026-13-01"}, "is not a 'date'"),
    ({"item_id": "A-1", "date_added": "2026-01-01", "dsgai_mapping": ["DSGAI99"]}, "dsgai_mapping 'DSGAI99' not in taxonomy"),
    ({"item_id": "A-1", "date_added": "2026-01-01", "risks": [{"dsgai_id": "DSGAI00"}]}, "risks/0/dsgai_id: dsgai_id 'DSGAI00'"),
    ({"item_id": "B-2", "date_added": "2026-01-01"}, "does not match the file name"),
])
def test_each_rule_fails(tmp_path, capsys, entry, expected):
    make(tmp_path, {"A-1": entry})
    code, out = run(tmp_path, capsys)
    assert code == 1 and expected in out


def test_duplicate_ids(tmp_path, capsys):
    make(tmp_path, {"A-1": {"item_id": "A-1", "date_added": "2026-01-01"},
                    "A-2": {"item_id": "A-1", "date_added": "2026-01-01"}})
    code, out = run(tmp_path, capsys)
    assert code == 1 and "is also used by A-1.json" in out


def test_extra_rule(tmp_path, capsys):
    make(tmp_path, {"A-1": {"item_id": "A-1", "date_added": "2026-01-01"}})
    code, out = run(tmp_path, capsys, extra=lambda entry, path: ["custom problem"])
    assert code == 1 and "A-1.json: custom problem" in out


def test_empty_entries(tmp_path, capsys):
    (tmp_path / "schema.json").write_text(json.dumps(SCHEMA))
    assert run(tmp_path, capsys, allow_empty=True)[0] == 0
    assert run(tmp_path, capsys)[0] == 1


@pytest.mark.parametrize("dataset,mutate,expected", [
    ("exploit_dataset", lambda e: e.update(mitre_atlas_mapping=[]), "mitre_atlas_mapping does not include it"),
    ("vulnerability_dataset", lambda e: e.update(cve_id="CVE-2000-0001"), "does not match cve_id"),
])
def test_dataset_specific_rules_still_fire(tmp_path, dataset, mutate, expected):
    """Run the real validate.py on a copy with one entry broken."""
    import subprocess
    copy = tmp_path / "datasets"
    shutil.copytree(ROOT / "datasets" / "_shared", copy / "_shared")
    shutil.copytree(ROOT / "datasets" / dataset, copy / dataset)
    entry_path = sorted((copy / dataset / "entries").glob("CVE-*.json" if dataset == "vulnerability_dataset" else "AML.*.json"))[0]
    entry = json.loads(entry_path.read_text(encoding="utf-8"))
    mutate(entry)
    entry_path.write_text(json.dumps(entry), encoding="utf-8")
    proc = subprocess.run([sys.executable, "validate.py"], cwd=copy / dataset, capture_output=True, text=True)
    assert proc.returncode == 1 and expected in proc.stdout
