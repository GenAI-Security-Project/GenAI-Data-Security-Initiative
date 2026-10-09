"""
Line numbers for JSON pointers, so findings can be annotated on the exact
line of a pull request diff. The standard json module does not report
positions, so this walks the text with a small scanner that understands
just enough JSON (strings, nesting) to find where each value starts.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_WS = " \t\r\n"


def _skip_ws(text: str, i: int) -> int:
    while i < len(text) and text[i] in _WS:
        i += 1
    return i


def _string_end(text: str, i: int) -> int:
    """Index just past the string that starts at text[i] == '"'."""
    i += 1
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == '"':
            return i + 1
        i += 1
    return i


def _value_end(text: str, i: int) -> int:
    """Index just past the JSON value that starts at i."""
    c = text[i]
    if c == '"':
        return _string_end(text, i)
    if c in "{[":
        depth = 0
        while i < len(text):
            c = text[i]
            if c == '"':
                i = _string_end(text, i)
                continue
            if c in "{[":
                depth += 1
            elif c in "}]":
                depth -= 1
                if depth == 0:
                    return i + 1
            i += 1
        return i
    while i < len(text) and text[i] not in ",}]" + _WS:
        i += 1
    return i


def _child_start(text: str, i: int, token: str) -> int | None:
    """Start of the child `token` (object key or array index) of the container at i."""
    i = _skip_ws(text, i)
    if i >= len(text) or text[i] not in "{[":
        return None
    is_object = text[i] == "{"
    i += 1
    index = 0
    while True:
        i = _skip_ws(text, i)
        if i >= len(text) or text[i] in "}]":
            return None
        if is_object:
            key_end = _string_end(text, i)
            key = json.loads(text[i:key_end])
            i = _skip_ws(text, key_end) + 1  # past ':'
            i = _skip_ws(text, i)
            if key == token:
                return i
        else:
            if str(index) == token:
                return i
            index += 1
        i = _skip_ws(text, _value_end(text, i))
        if i < len(text) and text[i] == ",":
            i += 1


def pointer_line(text: str, pointer: str) -> int | None:
    """1-based line where the value at a JSON pointer ("/a/0/b") starts."""
    if pointer in ("", "<root>"):
        return 1
    i: int | None = _skip_ws(text, 0)
    for raw in pointer.lstrip("/").split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        i = _child_start(text, i, token)
        if i is None:
            return None
    return text.count("\n", 0, i) + 1


@lru_cache(maxsize=256)
def _text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def line_for(path: Path, pointer: str) -> int | None:
    try:
        return pointer_line(_text(str(path)), pointer)
    except (OSError, ValueError, IndexError):
        return None
