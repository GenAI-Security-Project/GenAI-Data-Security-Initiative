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


def test_nested_validator_is_found_and_tests_dir_is_not(tmp_path, monkeypatch, capsys):
    root = make_tree(tmp_path, {"a": None})
    (root / "a" / "sub").mkdir()
    (root / "a" / "sub" / "validate.py").write_text(FAILING)
    (root / "a" / "tests").mkdir()
    (root / "a" / "tests" / "validate.py").write_text(FAILING)
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main(["--no-shared"]) == 1
    out = capsys.readouterr().out
    assert "FAIL          a/sub" in out
    assert "1 validator(s) ran, 1 failed, 0 dataset(s) have no validator yet" in out


def test_validator_timeout_is_an_error(tmp_path):
    d = tmp_path / "slow"
    d.mkdir()
    (d / "validate.py").write_text("import time\ntime.sleep(10)\n")
    status, output = run_all_checks.run_validator(d, timeout=0.5)
    assert status == "ERROR" and "timed out" in output


def test_shared_check_error_fails_the_run(tmp_path, monkeypatch, capsys):
    root = make_tree(tmp_path, {"a": None})
    (root / "a" / "entry.json").write_text('{"id": "X-1", "dsgai_mapping": ["DSGAI99"]}')
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main([]) == 1
    out = capsys.readouterr().out
    assert "FAIL          a (1 file(s), 1 error(s), 1 warning(s))" in out  # warning: no schema
    assert "DSGAI99 is not in the DSGAI taxonomy" in out


def test_warnings_pass_unless_strict(tmp_path, monkeypatch):
    root = make_tree(tmp_path, {"a": PASSING})
    (root / "a" / "entry.json").write_text('{"id": "X-1", "contact": "jane@realcorp.io"}')
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main([]) == 0
    assert run_all_checks.main(["--strict"]) == 1


def test_files_covered_by_a_dataset_validator_skip_the_shared_schema_check(tmp_path, monkeypatch, capsys):
    root = make_tree(tmp_path, {"a": PASSING})
    (root / "a" / "entry.json").write_text('{"id": "X-1"}')
    monkeypatch.setattr(run_all_checks, "DATASETS_ROOT", root)
    assert run_all_checks.main([]) == 0
    assert "no schema found" not in capsys.readouterr().out
