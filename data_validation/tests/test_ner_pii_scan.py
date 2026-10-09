"""Tests for ner_pii_scan.py's filtering, with a stub in place of Presidio."""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qc_tools import ner_pii_scan as ner  # noqa: E402


@dataclass
class Hit:
    entity_type: str
    start: int
    end: int
    score: float = 0.9


class StubAnalyzer:
    """Returns every occurrence of the configured words, like a model would."""

    def __init__(self, words: dict[str, str]):
        self.words = words

    def analyze(self, text, language, entities, score_threshold):
        hits = []
        for word, kind in self.words.items():
            i = text.find(word)
            if i >= 0 and kind in entities:
                hits.append(Hit(kind, i, i + len(word)))
        return hits


ANALYZER = StubAnalyzer({"Jane Doe": "PERSON", "Acme Corp": "ORGANIZATION", "PII": "ORGANIZATION",
                         "Model Bulletin": "PERSON", "Bias": "PERSON"})
TEXT = {"summary": "Jane Doe at Acme Corp leaked PII; see the Model Bulletin on Bias handling."}


def messages(entities):
    return [f.message for f in ner.scan_data(Path("e.json"), TEXT, entities, ANALYZER, allow={"Model Bulletin"})]


def test_people_and_organisations_in_incident_scope():
    assert messages(["PERSON", "ORGANIZATION"]) == [
        "looks like a real person name: 'Jane Doe'", "looks like a real organisation name: 'Acme Corp'"]


def test_acronyms_single_words_and_allowlisted_text_are_ignored():
    assert messages(["PERSON"]) == ["looks like a real person name: 'Jane Doe'"]


def test_allowlist_file_parses():
    assert "Model Bulletin" in ner.load_allowlist()
    assert not any(line.startswith("#") for line in ner.load_allowlist())
