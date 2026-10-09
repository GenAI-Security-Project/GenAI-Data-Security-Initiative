"""Tests for run_all_checks.py against throwaway dataset trees."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_all_checks  # noqa: E402

PASSING = "import sys\nsys.exit(0)\n"
FAILING = "import sys\nprint('entries/X.json: <root>: bad')\nsys.exit(1)\n"


def make_tree(tmp_path: Path, scripts: dict[str, str | None]) -> Path:
    root = tmp_path / "datasets"
    (root / "_shared").mkdir(parents=True)
    for name, body in scripts.items():
        d = root / name
        d.mkdir()
        if body is not None:
            (d / "validate.py").write_text(body)
    return root


def test_all_pass(tmp_path, monkeypatch, capsys):
    root = make_tree(tmp_path, {"a": PASSING, "b": PASSING, "c": None})
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main([]) == 0
    out = capsys.readouterr().out
    assert "2 validator(s) ran, 0 failed, 1 dataset(s) have no validator yet" in out
    assert "_shared" not in out


def test_one_failure_fails_the_run_and_shows_why(tmp_path, monkeypatch, capsys):
    root = make_tree(tmp_path, {"a": PASSING, "b": FAILING})
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main([]) == 1
    out = capsys.readouterr().out
    assert "FAIL          b" in out
    assert "entries/X.json: <root>: bad" in out


def test_single_dataset(tmp_path, monkeypatch):
    root = make_tree(tmp_path, {"a": PASSING, "b": FAILING})
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main(["--dataset", str(root / "a")]) == 0
    assert run_all_checks.main(["--dataset", str(root / "b")]) == 1


def test_nothing_to_run_is_not_a_pass(tmp_path, monkeypatch):
    root = make_tree(tmp_path, {"a": None})
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main([]) == 2


def test_missing_directory(tmp_path):
    assert run_all_checks.main(["--dataset", str(tmp_path / "nope")]) == 2
