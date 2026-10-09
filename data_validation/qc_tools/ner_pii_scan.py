"""
Finds personal and organisation names that regex patterns cannot, using
named-entity recognition (Microsoft Presidio on a spaCy English model).

WARN only: NER is probabilistic, and a reviewer decides. It runs on the
datasets whose contribution rules require anonymization:

  incident_dataset                   person and organisation names (its
                                     README forbids both)
  riskassessment_dataset,
  agentdataflow_toolexchange_traces,
  rag_dataset                        person names

To keep precision usable on technical text, a hit counts only when the
model is at least 85% confident and the text looks like a proper name: two
or more capitalised words ("Jane Doe", "Acme Corp"), never an acronym such
as "PII" or "EU". Reviewed false positives go in
reference_data/ner_allowlist.txt. The prompt-injection datasets are not scanned: they are
mostly Turkish, and the English model would only produce noise.

Optional dependencies, kept out of requirements.txt so the core checks
stay single-dependency:  pip install -r requirements-ner.txt

Usage:
    python ner_pii_scan.py
    python ner_pii_scan.py --dataset ../../datasets/incident_dataset/
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, REFERENCE_DIR, WARN, Finding, ensure_utf8_stdout, iter_data_files,
    load_json, print_findings, walk_strings,
)

CHECK = "ner-pii"
MODEL = "en_core_web_sm"
SCORE_THRESHOLD = 0.85
MIN_TEXT_LEN = 15
# Two or more capitalised words: a proper name, not an acronym or a single word.
PROPER_NAME_RE = re.compile(r"^[A-Z][a-z]+(?:[ '-][A-Z][a-z]+)+$")
ALLOWLIST_PATH = REFERENCE_DIR / "ner_allowlist.txt"
SCOPE = {
    "incident_dataset": ["PERSON", "ORGANIZATION"],
    "riskassessment_dataset": ["PERSON"],
    "agentdataflow_toolexchange_traces": ["PERSON"],
    "rag_dataset": ["PERSON"],
}


def load_allowlist() -> set[str]:
    """Reviewed false positives (reference_data/ner_allowlist.txt)."""
    lines = ALLOWLIST_PATH.read_text(encoding="utf-8").splitlines()
    return {line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")}


def build_analyzer():
    from presidio_analyzer import AnalyzerEngine
    from presidio_analyzer.nlp_engine import NlpEngineProvider
    config = {
        "nlp_engine_name": "spacy",
        "models": [{"lang_code": "en", "model_name": MODEL}],
        "ner_model_configuration": {
            "model_to_presidio_entity_mapping": {"PERSON": "PERSON", "ORG": "ORGANIZATION"},
            "labels_to_ignore": [],
        },
    }
    engine = NlpEngineProvider(nlp_configuration=config).create_engine()
    return AnalyzerEngine(nlp_engine=engine, supported_languages=["en"])


def scan_data(path: Path, data, entities: list[str], analyzer, allow: set[str] | None = None) -> list[Finding]:
    allow = load_allowlist() if allow is None else allow
    findings: list[Finding] = []
    for pointer, _key, value in walk_strings(data):
        if len(value) < MIN_TEXT_LEN or value.startswith(("http://", "https://")):
            continue
        seen: set[str] = set()
        for r in analyzer.analyze(value, language="en", entities=entities, score_threshold=SCORE_THRESHOLD):
            text = value[r.start:r.end].strip()
            if PROPER_NAME_RE.match(text) and text not in seen and text not in allow:
                seen.add(text)
                kind = "person" if r.entity_type == "PERSON" else "organisation"
                findings.append(Finding(WARN, CHECK, path, pointer, f"looks like a real {kind} name: {text!r}"))
    return findings


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="NER scan for person and organisation names")
    parser.add_argument("--dataset", action="append", default=[],
                        help="Dataset directory (repeatable; default: the datasets that require anonymization)")
    args = parser.parse_args(argv)
    try:
        analyzer = build_analyzer()
    except (ImportError, OSError) as exc:
        print(f"NER scan needs its optional dependencies: pip install -r requirements-ner.txt ({exc})")
        return 2
    targets = [Path(d).resolve() for d in args.dataset] or [DATASETS_ROOT / name for name in SCOPE]
    allow = load_allowlist()
    findings: list[Finding] = []
    files = 0
    for dataset in targets:
        entities = SCOPE.get(dataset.name, ["PERSON"])
        if not dataset.is_dir():
            continue
        for path in iter_data_files(dataset):
            data, err = load_json(path, CHECK)
            files += 1
            findings += [err] if err else scan_data(path, data, entities, analyzer, allow)
    print(f"Checked {files} file(s)")
    print_findings(findings, DATASETS_ROOT.parent)
    return 0


if __name__ == "__main__":
    sys.exit(main())
