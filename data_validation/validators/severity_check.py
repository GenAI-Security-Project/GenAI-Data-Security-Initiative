"""
Checks CVSS scores against their vectors and the qualitative rating against
the FIRST rating scale, in any record's "severity" object.

ERROR: a CVSS v3.x or v4.0 vector that does not parse; a score that differs
       from the base score its vector produces (by more than 0.05); a
       qualitative rating that is not the FIRST band of the CVSS score
       (None 0.0, Low 0.1-3.9, Medium 4.0-6.9, High 7.0-8.9,
       Critical 9.0-10.0). The v4.0 score sets the band when both are given.
WARN:  a score with no vector, so it cannot be checked.

Scores are computed with the `cvss` package (FIRST CVSS v3.0, v3.1, v4.0).

Usage:
    python severity_check.py --dataset ../../datasets/vulnerability_dataset/
    python severity_check.py                    # every dataset
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, WARN, Finding, add_target_args, ensure_utf8_stdout,
    iter_records, load_json, print_findings, resolve_targets,
)

CHECK = "severity"
TOLERANCE = 0.05


def first_band(score: float) -> str:
    """FIRST CVSS qualitative severity rating scale (same for v3.x and v4.0)."""
    if score == 0:
        return "None"
    if score < 4.0:
        return "Low"
    if score < 7.0:
        return "Medium"
    if score < 9.0:
        return "High"
    return "Critical"


def _computed(version: str, vector: str) -> float:
    from cvss import CVSS3, CVSS4
    return float(CVSS4(vector).base_score if version == "v4" else CVSS3(vector).base_score)


def check_severity(path: Path, pointer: str, sev: dict) -> list[Finding]:
    findings: list[Finding] = []
    loc = f"{pointer}/severity"
    scores: dict[str, float] = {}
    for version in ("v3", "v4"):
        score, vector = sev.get(f"cvss_{version}_score"), sev.get(f"cvss_{version}_vector")
        if vector is not None:
            try:
                computed = _computed(version, vector)
            except Exception as exc:  # the cvss package raises its own error types per version
                findings.append(Finding(ERROR, CHECK, path, f"{loc}/cvss_{version}_vector", f"not a valid CVSS vector: {exc}"))
                continue
            if score is None:
                scores[version] = computed
            elif abs(computed - float(score)) > TOLERANCE:
                findings.append(Finding(ERROR, CHECK, path, f"{loc}/cvss_{version}_score",
                                        f"score {score} does not match its vector, which gives {computed}"))
        elif score is not None:
            findings.append(Finding(WARN, CHECK, path, f"{loc}/cvss_{version}_score",
                                    "score has no vector, so it cannot be checked; add the vector"))
        if isinstance(score, (int, float)):
            scores[version] = float(score)
    qualitative = sev.get("qualitative")
    basis = "v4" if "v4" in scores else "v3" if "v3" in scores else None
    if basis and isinstance(qualitative, str):
        band = first_band(scores[basis])
        if qualitative != band:
            findings.append(Finding(ERROR, CHECK, path, f"{loc}/qualitative",
                                    f"{qualitative!r} but the CVSS {basis} score {scores[basis]} is {band!r} on the FIRST scale"))
    return findings


def check_data(path: Path, data) -> list[Finding]:
    findings: list[Finding] = []
    for pointer, record in iter_records(data):
        sev = record.get("severity")
        if isinstance(sev, dict):
            findings += check_severity(path, pointer, sev)
    return findings


def check_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check CVSS scores, vectors and qualitative ratings")
    add_target_args(parser)
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    findings = [f for p in files for f in check_file(p)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
