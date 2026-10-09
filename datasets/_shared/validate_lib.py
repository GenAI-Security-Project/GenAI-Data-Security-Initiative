"""Shared core of the dataset validators (datasets/*/validate.py).

Each dataset's validate.py calls run() with what is particular to it: where
its schema is, which field is the entry ID, and any extra rules a schema
cannot express. run() does the rest the same way for every dataset:

  * every entries/*.json validates against the schema, with "format"
    (dates, URIs) enforced
  * every DSGAI ID (dsgai_mapping, dsgai_id, addresses_dsgai, at any depth)
    is in datasets/_shared/dsgai_taxonomy.json
  * the entry ID matches the file name, and no two entries share an ID
  * output: one line per problem, then "OK: ..." or "FAIL: ..."; exit code
    0 on success, 1 on any problem, 2 when jsonschema is not installed

Standard library plus jsonschema only, so a dataset can still be checked
with nothing but `pip install jsonschema`.
"""
from __future__ import annotations

import json
import sys
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any

SHARED = Path(__file__).resolve().parent
TAXONOMY_PATH = SHARED / "dsgai_taxonomy.json"
DSGAI_KEYS = {"dsgai_mapping", "dsgai_id", "addresses_dsgai"}

Extra = Callable[[dict, Path], list[str]]


def load_taxonomy_ids() -> set[str]:
    data = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    return {e["id"] for e in data.get("entries", [])}


def dsgai_references(obj: Any, pointer: str = "") -> Iterator[tuple[str, str, Any]]:
    """(pointer, key, value) for every value under a DSGAI key, at any depth."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            here = f"{pointer}/{key}"
            if key in DSGAI_KEYS:
                for i, item in enumerate(value if isinstance(value, list) else [value]):
                    yield (f"{here}/{i}" if isinstance(value, list) else here), key, item
            else:
                yield from dsgai_references(value, here)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            yield from dsgai_references(item, f"{pointer}/{i}")


def run(root: Path, *, id_field: str, schema_path: Path | None = None,
        allow_empty: bool = False, extra: Extra | None = None) -> int:
    """Validate root/entries/*.json. Returns the process exit code."""
    try:
        from jsonschema import validators
    except ImportError:
        sys.stderr.write("jsonschema not installed. Run: pip install jsonschema\n")
        return 2

    schema = json.loads((schema_path or root / "schema.json").read_text(encoding="utf-8"))
    cls = validators.validator_for(schema)
    validator = cls(schema, format_checker=cls.FORMAT_CHECKER)
    taxonomy_ids = load_taxonomy_ids()

    entries_dir = root / "entries"
    entry_files = sorted(entries_dir.glob("*.json")) if entries_dir.is_dir() else []
    if not entry_files:
        if allow_empty:
            print(f"OK: no entries yet in {entries_dir.name}/.")
            return 0
        sys.stderr.write(f"No entries found in {entries_dir}\n")
        return 1

    errors: list[str] = []
    seen: dict[str, str] = {}
    for path in entry_files:
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON — {e}")
            continue

        for err in validator.iter_errors(entry):
            loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
            errors.append(f"{path.name}: {loc}: {err.message}")

        for pointer, key, value in dsgai_references(entry):
            if value not in taxonomy_ids:
                errors.append(f"{path.name}: {pointer.lstrip('/')}: {key} {value!r} not in taxonomy")

        entry_id = entry.get(id_field) if isinstance(entry, dict) else None
        if isinstance(entry_id, str):
            if entry_id != path.stem:
                errors.append(f"{path.name}: {id_field} {entry_id!r} does not match the file name")
            if entry_id in seen:
                errors.append(f"{path.name}: {id_field} {entry_id!r} is also used by {seen[entry_id]}")
            seen.setdefault(entry_id, path.name)

        if extra is not None and isinstance(entry, dict):
            errors += [f"{path.name}: {message}" for message in extra(entry, path)]

    if errors:
        for line in errors:
            print(line)
        print(f"\nFAIL: {len(errors)} issue(s) across {len(entry_files)} entries.")
        return 1

    print(f"OK: {len(entry_files)} entries validated against schema.")
    return 0


def main_for(file: str, **kwargs) -> None:
    """Entry point for a dataset's validate.py: run() on its folder and exit."""
    sys.exit(run(Path(file).resolve().parent, **kwargs))
