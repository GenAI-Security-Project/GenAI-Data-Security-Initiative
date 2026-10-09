"""Tests for online_check.py with every HTTP call stubbed (no network)."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qc_tools import online_check as oc  # noqa: E402
from validators._common import ERROR, TAXONOMY_PATH, WARN  # noqa: E402


def make_tree(tmp_path: Path) -> Path:
    root = tmp_path / "datasets"
    (root / "_shared").mkdir(parents=True)
    shutil.copy(TAXONOMY_PATH, root / "_shared" / "dsgai_taxonomy.json")
    vuln = root / "vulnerability_dataset" / "entries"
    vuln.mkdir(parents=True)
    entries = {
        "CVE-2024-0001": {"exploit_available": "public_poc",
                          "source_urls": ["https://ok.example.org/a", "https://atlas.mitre.org/techniques/AML.T0051"]},
        "CVE-2024-0002": {"exploit_available": "none_known", "source_urls": ["https://gone.example.org/b"]},
        "CVE-2024-0003": {"exploit_available": "exploited_in_the_wild", "source_urls": ["https://blocked.example.org/c"],
                          "notes": "see GHSA-cfgh-jmpq-rvwx and GHSA-2345-6789-cfgh"},
    }
    for cve, extra in entries.items():
        (vuln / f"{cve}.json").write_text(json.dumps({"vulnerability_id": cve, **extra}))
    return root


def fake_http(url: str, headers=None):
    responses = {
        "https://cveawg.mitre.org/api/cve/CVE-2024-0001": (200, {"cveMetadata": {"state": "PUBLISHED"}}),
        "https://cveawg.mitre.org/api/cve/CVE-2024-0002": (200, {"cveMetadata": {"state": "REJECTED"}}),
        "https://cveawg.mitre.org/api/cve/CVE-2024-0003": (200, {"cveMetadata": {"state": "PUBLISHED"}}),
        "https://api.github.com/advisories/GHSA-cfgh-jmpq-rvwx": (200, {"withdrawn_at": "2026-01-01T00:00:00Z"}),
        "https://ok.example.org/a": (200, {}),
        "https://gone.example.org/b": (404, {}),
        "https://blocked.example.org/c": (403, {}),
        oc.KEV_URL: (200, {"catalogVersion": "2026.10.08", "vulnerabilities": [{"cveID": "CVE-2024-0001"}]}),
    }
    if url.startswith("https://archive.org/wayback/available"):
        return 200, json.dumps({"archived_snapshots": {"closest": {"available": True, "url": "http://web.archive.org/x"}}}).encode()
    if url.startswith("https://api.first.org/data/v1/epss"):
        return 200, json.dumps({"data": [{"cve": "CVE-2024-0001", "epss": "0.5", "percentile": "0.99"}]}).encode()
    if urlsplit(url).hostname == "atlas.mitre.org":
        raise AssertionError("atlas.mitre.org must not be fetched")
    status, body = responses.get(url, (404, {}))
    return status, json.dumps(body).encode()


def test_online_findings(tmp_path, monkeypatch):
    monkeypatch.setattr(oc, "http_get", fake_http)
    findings, summary = oc.run(make_tree(tmp_path))

    def level_of(fragment: str) -> str:
        [match] = [f.level for f in findings if fragment in f.message]
        return match

    assert level_of("CVE-2024-0002 is rejected in the CVE Program") == ERROR
    assert level_of("GHSA-cfgh-jmpq-rvwx is withdrawn") == ERROR
    assert level_of("GHSA-2345-6789-cfgh is not in the global GitHub Advisory Database") == WARN
    assert level_of("dead link (HTTP 404): https://gone.example.org/b; archived copy: http://web.archive.org/x") == ERROR
    assert level_of("link answers HTTP 403") == WARN
    assert level_of("CVE-2024-0001 is in CISA KEV") == ERROR
    assert len(findings) == 6  # nothing for the published CVEs, the live link, or atlas.mitre.org
    assert "| CVE-2024-0001 | yes | **yes** | 0.5000 | 99.00% |" in summary


def test_skip_links(tmp_path, monkeypatch):
    monkeypatch.setattr(oc, "http_get", fake_http)
    findings, summary = oc.run(make_tree(tmp_path), skip_links=True)
    assert not any("link" in f.message for f in findings)
    assert "links skipped" in summary
