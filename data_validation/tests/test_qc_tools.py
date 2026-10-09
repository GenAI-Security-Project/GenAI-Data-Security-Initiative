"""Tests for the QC tools against throwaway dataset trees."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qc_tools import anomaly_detector, bias_report, consistency_check  # noqa: E402
from validators._common import ERROR, TAXONOMY_PATH  # noqa: E402


def make_tree(tmp_path: Path, datasets: dict[str, list[dict]]) -> Path:
    root = tmp_path / "datasets"
    (root / "_shared").mkdir(parents=True)
    shutil.copy(TAXONOMY_PATH, root / "_shared" / "dsgai_taxonomy.json")
    for name, records in datasets.items():
        entries = root / name / "entries"
        entries.mkdir(parents=True)
        for i, rec in enumerate(records):
            (entries / f"{i}.json").write_text(json.dumps(rec))
    return root


def test_bias_report_counts_and_gaps(tmp_path):
    root = make_tree(tmp_path, {"vulnerability_dataset": [
        {"vulnerability_id": "V-1", "dsgai_mapping": ["DSGAI01"], "severity": {"qualitative": "High"}},
        {"vulnerability_id": "V-2", "dsgai_mapping": ["DSGAI01", "DSGAI02"], "severity": {"qualitative": "Low"}},
    ]})
    report = bias_report.build_report(root)
    assert "| DSGAI01 | Sensitive Data Leakage | 2 | 2 |" in report
    assert "DSGAI entries no record maps to: DSGAI03" in report
    assert "**severity**: High 1 (50%), Low 1 (50%)" in report


def test_anomaly_detector_flags_concentration_and_outliers(tmp_path):
    records = [{"id": f"R-{i}", "dsgai_mapping": ["DSGAI01"], "severity": "High"} for i in range(11)]
    records.append({"id": "R-big", "dsgai_mapping": [f"DSGAI{n:02d}" for n in range(1, 9)], "severity": "Low"})
    root = make_tree(tmp_path, {"d": records})
    messages = [f.message for f in anomaly_detector.detect(root)]
    assert any("map to DSGAI01" in m for m in messages)
    assert any(m.startswith("R-big maps to 8") for m in messages)
    assert any(m.startswith("severity is 'High'") for m in messages)


def test_anomaly_detector_skips_small_datasets(tmp_path):
    root = make_tree(tmp_path, {"d": [{"id": "R-1", "dsgai_mapping": ["DSGAI01"]}]})
    assert anomaly_detector.detect(root) == []


def test_consistency_check_dangling_internal_reference(tmp_path):
    root = make_tree(tmp_path, {
        "vulnerability_dataset": [{"vulnerability_id": "DSGAI-VULN-real"}, {"vulnerability_id": "CVE-2024-0001"}],
        "exploit_dataset": [{"exploit_id": "DSGAI-EXP-a",
                             "related_vulnerabilities": ["DSGAI-VULN-real", "DSGAI-VULN-typo", "CVE-2024-0001", "CVE-2024-9999"]}],
    })
    findings, missing_cves = consistency_check.check(root)
    assert [(f.level, f.message) for f in findings] == [(ERROR, "DSGAI-VULN-typo is not an entry in vulnerability_dataset")]
    assert missing_cves == ["CVE-2024-9999"]


def test_qc_tools_run_on_the_real_datasets():
    """The real datasets have no dangling internal references and every DSGAI entry is covered."""
    findings, _ = consistency_check.check()
    assert findings == []
    assert "DSGAI entries no record maps to: none." in bias_report.build_report()
