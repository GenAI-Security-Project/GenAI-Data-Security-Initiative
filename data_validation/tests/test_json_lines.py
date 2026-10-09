"""Tests for json_lines.py and the runner's GitHub annotations."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_all_checks  # noqa: E402
from validators.json_lines import pointer_line  # noqa: E402

TEXT = """{
  "id": "X-1",
  "tricky": "a \\" quote, a } and a ] inside",
  "list": [
    "first",
    {"inner": ["q",
               "r"]}
  ],
  "a/b": 1
}"""


def test_pointer_lines():
    assert pointer_line(TEXT, "/id") == 2
    assert pointer_line(TEXT, "/list/0") == 5
    assert pointer_line(TEXT, "/list/1/inner/1") == 7
    assert pointer_line(TEXT, "/a~1b") == 9
    assert pointer_line(TEXT, "<root>") == 1
    assert pointer_line(TEXT, "/missing") is None


def test_annotation_format(tmp_path):
    f = tmp_path / "e.json"
    f.write_text(TEXT)
    line = run_all_checks.annotation("ERROR", f, "/list/1/inner/1", "dsgai", "bad: value, 100%")
    assert line.startswith("::error file=") and ",line=7,title=dsgai::bad: value, 100%25" in line


def test_validator_output_is_annotated(tmp_path):
    (tmp_path / "entries").mkdir()
    (tmp_path / "entries" / "e.json").write_text(TEXT)
    out = "e.json: list/1/inner/1: 'r' is not valid\nunrelated line\n\nFAIL: 1 issue(s) across 1 entries."
    [line] = run_all_checks.validator_annotations(tmp_path / "validate.py", out)
    assert "entries/e.json,line=7" in line.replace("\\", "/") and line.endswith("::'r' is not valid")
