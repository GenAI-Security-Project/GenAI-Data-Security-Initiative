"""
Finds duplicate records within a dataset.

ERROR: two records in one dataset with the same ID.
WARN:  two records whose text is identical, or whose word-trigram (Jaccard)
       similarity is at least the threshold (default 0.8). Similar is not
       necessarily wrong: a reviewer decides.

A record's text is its string values of 40 characters or more, minus URLs
and minus any string that appears in more than half of the dataset's records
(shared provenance or licence text would otherwise make every pair look
alike). example.json files are skipped: they copy a real entry on purpose.
Similarity is lexical only; paraphrases are not caught.

Usage:
    python dedup_checker.py                                   # every dataset
    python dedup_checker.py --dataset ../../datasets/exploit_dataset/
    python dedup_checker.py --file new_entry.json --dataset ../../datasets/exploit_dataset/
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter
from itertools import combinations
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, WARN, Finding, ensure_utf8_stdout, iter_data_files,
    iter_records, load_json, print_findings, record_id, walk_strings,
)

CHECK = "dedup"
DEFAULT_THRESHOLD = 0.8
MIN_TEXT_LEN = 40
URL_RE = re.compile(r"^\w+://\S+$")
WORD_RE = re.compile(r"\w+")


class Record:
    def __init__(self, path: Path, pointer: str, data: dict):
        self.path = path
        self.pointer = pointer
        self.id = record_id(data)
        self.strings = [
            v for _p, _k, v in walk_strings(data)
            if len(v) >= MIN_TEXT_LEN and not URL_RE.match(v.strip())
        ]
        self.text = ""
        self.shingles: frozenset[tuple[str, ...]] = frozenset()

    @property
    def label(self) -> str:
        return self.id or f"{self.path.name}{self.pointer}"


def _normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def _shingles(text: str) -> frozenset[tuple[str, ...]]:
    words = WORD_RE.findall(text)
    if len(words) < 3:
        return frozenset([tuple(words)]) if words else frozenset()
    return frozenset(zip(words, words[1:], words[2:]))


def load_records(files: list[Path]) -> tuple[list[Record], list[Finding]]:
    records, findings = [], []
    for path in files:
        if path.name == "example.json":
            continue
        data, err = load_json(path, CHECK)
        if err:
            findings.append(err)
            continue
        records.extend(Record(path, ptr, rec) for ptr, rec in iter_records(data))
    # Drop boilerplate: strings shared by more than half of the records, in
    # the whole dataset or in one folder of it (a sub-collection such as one
    # contributor's cases repeats its own provenance text in every file).
    groups: dict[Path | None, list[Record]] = {None: records}
    for r in records:
        groups.setdefault(r.path.parent, []).append(r)
    common: set[str] = set()
    for group in groups.values():
        if len(group) >= 4:
            counts = Counter(s for r in group for s in set(r.strings))
            common |= {s for s, n in counts.items() if n > len(group) / 2}
    for r in records:
        r.text = _normalize(" ".join(s for s in r.strings if s not in common))
        r.shingles = _shingles(r.text)
    return records, findings


def check_records(records: list[Record], threshold: float = DEFAULT_THRESHOLD,
                  new: set[Path] | None = None) -> list[Finding]:
    """Findings for duplicate IDs and similar text. With new, only pairs involving a new file."""
    findings: list[Finding] = []
    by_id: dict[str, Record] = {}
    for r in records:
        if r.id is None:
            continue
        first = by_id.setdefault(r.id, r)
        if first is not r and (new is None or r.path in new or first.path in new):
            findings.append(Finding(ERROR, CHECK, r.path, r.pointer,
                                    f"ID {r.id} is also used by {first.path.name}{first.pointer}"))
    for a, b in combinations(records, 2):
        if new is not None and a.path not in new and b.path not in new:
            continue
        if not a.shingles or not b.shingles:
            continue
        if a.text == b.text:
            score = 1.0
        else:
            score = len(a.shingles & b.shingles) / len(a.shingles | b.shingles)
        if score >= threshold:
            findings.append(Finding(WARN, CHECK, b.path, b.pointer,
                                    f"{b.label} is {score:.0%} similar to {a.label} ({a.path.name}); possible duplicate"))
    return findings


def check_dataset(dataset: Path, threshold: float = DEFAULT_THRESHOLD) -> list[Finding]:
    records, findings = load_records(iter_data_files(dataset))
    return findings + check_records(records, threshold)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Find duplicate records within a dataset")
    parser.add_argument("--dataset", action="append", default=[],
                        help="Dataset directory (repeatable; default: every dataset)")
    parser.add_argument("--file", action="append", default=[],
                        help="New file(s) to compare against --dataset (repeatable)")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                        help=f"Similarity that counts as a possible duplicate (default {DEFAULT_THRESHOLD})")
    args = parser.parse_args(argv)
    for p in args.dataset + args.file:
        if not Path(p).exists():
            print(f"Not found: {p}")
            return 2
    if args.file and len(args.dataset) != 1:
        print("--file needs exactly one --dataset to compare against")
        return 2
    datasets = [Path(d).resolve() for d in args.dataset] or sorted(
        p for p in DATASETS_ROOT.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")))
    findings: list[Finding] = []
    if args.file:
        new = {Path(f).resolve() for f in args.file}
        records, findings = load_records(sorted(set(iter_data_files(datasets[0])) | new))
        findings += check_records(records, args.threshold, new)
    else:
        for d in datasets:
            findings += check_dataset(d, args.threshold)
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
