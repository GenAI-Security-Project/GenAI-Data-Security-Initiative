"""
Checks the datasets against live external sources. Network access needed;
CI runs it weekly (datasets-online-checks workflow), not on pull requests,
so an outage elsewhere never blocks a contribution.

ERROR: a CVE ID that the CVE Program (cveawg.mitre.org) does not know or
       has REJECTED; a GHSA ID GitHub has withdrawn; a
       cited URL that is gone (404/410) or whose host does not resolve; a
       CVE in the CISA Known Exploited Vulnerabilities catalog whose
       vulnerability entry does not say exploit_available:
       exploited_in_the_wild. (atlas.mitre.org links are not fetched: that
       site answers 404 for every technique page.)
WARN:  a GHSA ID not in GitHub's global Advisory Database (it may be a
       repository advisory, which the global database never lists); a URL
       that answers with another error (403, 429, 5xx, timeouts:
       often bot-blocking, so a person should look); an exploit entry
       whose related CVE is in KEV while exploited_in_the_wild is "no" or
       "unknown".

For every dead link the report includes the Wayback Machine's closest
snapshot, if any, to replace it with. The report also lists each CVE's EPSS
v4 score and percentile (FIRST) and KEV status; those change daily, so they
are reported, not stored in the data.

Usage:
    python online_check.py
    python online_check.py --skip-links --summary report.md
    GITHUB_TOKEN=... python online_check.py      # GHSA lookups need a token
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, WARN, Finding, ensure_utf8_stdout, load_dataset_records,
    print_findings, record_id, walk_strings,
)

CHECK = "online"
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,}\b")
GHSA_RE = re.compile(r"\bGHSA(?:-[23456789cfghjmpqrvwx]{4}){3}\b")
URL_RE = re.compile(r"^https?://\S+$")
USER_AGENT = "OWASP-GenAI-Data-Security-Initiative-dataset-checks/1.0 (+https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative)"
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
TIMEOUT = 25
# Hosts whose HTTP status says nothing about the page. atlas.mitre.org is a
# single-page app on GitHub Pages: every technique URL, real or not, answers
# 404 with the same app shell. ATLAS IDs are checked against MITRE's data by
# crossref_validator instead.
UNCHECKABLE_HOSTS = {"atlas.mitre.org"}


def http_get(url: str, headers: dict[str, str] | None = None) -> tuple[int, bytes]:
    """(status, body); status 0 means the host could not be reached."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310 - http(s) only, checked by callers
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, b""


def collect(datasets_root: Path):
    """Where each CVE, GHSA and URL is cited: {id: [(path, pointer), ...]}."""
    cves: dict[str, list] = {}
    ghsas: dict[str, list] = {}
    urls: dict[str, list] = {}
    records = load_dataset_records(datasets_root)
    for items in records.values():
        for path, rec in items:
            for pointer, _key, value in walk_strings(rec):
                for m in CVE_RE.finditer(value):
                    cves.setdefault(m.group(0), []).append((path, pointer))
                for m in GHSA_RE.finditer(value):
                    ghsas.setdefault(m.group(0), []).append((path, pointer))
                url = value.strip()
                if URL_RE.match(url) and urllib.parse.urlsplit(url).hostname not in UNCHECKABLE_HOSTS:
                    urls.setdefault(url, []).append((path, pointer))
    return records, cves, ghsas, urls


def cve_state(cve: str) -> str:
    status, body = http_get(f"https://cveawg.mitre.org/api/cve/{cve}")
    if status == 404:
        return "NOT_FOUND"
    if status != 200:
        return f"UNREACHABLE ({status})"
    return json.loads(body).get("cveMetadata", {}).get("state", "UNKNOWN")


def ghsa_state(ghsa: str, token: str | None) -> str:
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    status, body = http_get(f"https://api.github.com/advisories/{ghsa}", headers)
    if status == 404:
        return "NOT_FOUND"
    if status != 200:
        return f"UNREACHABLE ({status})"
    return "WITHDRAWN" if json.loads(body).get("withdrawn_at") else "PUBLISHED"


def url_status(url: str) -> int:
    return http_get(url)[0]


def wayback_snapshot(url: str) -> str | None:
    status, body = http_get("https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe=""))
    if status != 200:
        return None
    closest = json.loads(body).get("archived_snapshots", {}).get("closest") or {}
    return closest.get("url") if closest.get("available") else None


def epss_scores(cves: list[str]) -> dict[str, tuple[float, float]]:
    scores: dict[str, tuple[float, float]] = {}
    for i in range(0, len(cves), 100):
        status, body = http_get("https://api.first.org/data/v1/epss?cve=" + ",".join(cves[i:i + 100]))
        if status == 200:
            for row in json.loads(body).get("data", []):
                scores[row["cve"]] = (float(row["epss"]), float(row["percentile"]))
    return scores


def kev_catalog() -> tuple[str, set[str]]:
    status, body = http_get(KEV_URL)
    if status != 200:
        return "unavailable", set()
    data = json.loads(body)
    return data.get("catalogVersion", "?"), {v["cveID"] for v in data["vulnerabilities"]}


def run(datasets_root: Path = DATASETS_ROOT, skip_links: bool = False, token: str | None = None):
    """(findings, summary markdown)."""
    records, cves, ghsas, urls = collect(datasets_root)
    findings: list[Finding] = []

    def cite(where, level, message):
        path, pointer = where[0]
        more = f" (and {len(where) - 1} more citation(s))" if len(where) > 1 else ""
        findings.append(Finding(level, CHECK, path, pointer, message + more))

    with ThreadPoolExecutor(max_workers=8) as pool:
        cve_states = dict(zip(cves, pool.map(cve_state, cves)))
        ghsa_states = dict(zip(ghsas, pool.map(lambda g: ghsa_state(g, token), ghsas)))
        link_states = {} if skip_links else dict(zip(urls, pool.map(url_status, urls)))

    for cve, state in sorted(cve_states.items()):
        if state in ("NOT_FOUND", "REJECTED"):
            cite(cves[cve], ERROR, f"{cve} is {state.replace('_', ' ').lower()} in the CVE Program")
        elif state.startswith("UNREACHABLE"):
            cite(cves[cve], WARN, f"{cve}: CVE Services {state.lower()}")
    for ghsa, state in sorted(ghsa_states.items()):
        if state == "WITHDRAWN":
            cite(ghsas[ghsa], ERROR, f"{ghsa} is withdrawn in the GitHub Advisory Database")
        elif state == "NOT_FOUND":
            cite(ghsas[ghsa], WARN, f"{ghsa} is not in the global GitHub Advisory Database; "
                                    "if it is a repository advisory, cite its github.com/<owner>/<repo>/security/advisories URL")
        elif state.startswith("UNREACHABLE"):
            cite(ghsas[ghsa], WARN, f"{ghsa}: GitHub API {state.lower()}")
    dead = sorted(u for u, s in link_states.items() if s in (0, 404, 410))
    snapshots = {}
    if dead:
        with ThreadPoolExecutor(max_workers=4) as pool:
            snapshots = dict(zip(dead, pool.map(wayback_snapshot, dead)))
    for url, status in sorted(link_states.items()):
        if status in (0, 404, 410):
            reason = "host does not resolve or refuses connections" if status == 0 else f"HTTP {status}"
            snap = snapshots.get(url)
            hint = f"; archived copy: {snap}" if snap else "; no Wayback Machine snapshot"
            cite(urls[url], ERROR, f"dead link ({reason}): {url}{hint}")
        elif status >= 400:
            cite(urls[url], WARN, f"link answers HTTP {status} (may be bot-blocking): {url}")

    kev_version, kev = kev_catalog()
    vuln_cves = set()
    for path, rec in records.get("vulnerability_dataset", []):
        cid = rec.get("cve_id") or (record_id(rec) if (record_id(rec) or "").startswith("CVE-") else None)
        if not cid:
            continue
        vuln_cves.add(cid)
        if cid in kev and rec.get("exploit_available") != "exploited_in_the_wild":
            findings.append(Finding(ERROR, CHECK, path, "/exploit_available",
                                    f"{cid} is in CISA KEV (catalog {kev_version}) but exploit_available is "
                                    f"{rec.get('exploit_available')!r}; set it to 'exploited_in_the_wild'"))
    for path, rec in records.get("exploit_dataset", []):
        in_kev = [c for c in rec.get("related_vulnerabilities", []) if c in kev]
        if in_kev and rec.get("exploited_in_the_wild") in ("no", "unknown"):
            findings.append(Finding(WARN, CHECK, path, "/exploited_in_the_wild",
                                    f"related {', '.join(in_kev)} in CISA KEV, but exploited_in_the_wild is "
                                    f"{rec['exploited_in_the_wild']!r}"))

    epss = epss_scores(sorted(cves))
    lines = ["## Exploitation signals", "",
             f"CISA KEV catalog {kev_version}; EPSS v4 from FIRST (api.first.org), as of this run.", "",
             "| CVE | In vulnerability dataset | CISA KEV | EPSS | EPSS percentile |", "|---|---|---|---|---|"]
    for cve in sorted(cves, key=lambda c: -epss.get(c, (0, 0))[0]):
        score, pct = epss.get(cve, (None, None))
        lines.append(f"| {cve} | {'yes' if cve in vuln_cves else 'no'} | {'**yes**' if cve in kev else 'no'} | "
                     f"{'' if score is None else f'{score:.4f}'} | {'' if pct is None else f'{pct:.2%}'} |")
    checked = f"{len(cves)} CVE(s), {len(ghsas)} GHSA(s), " + ("links skipped" if skip_links else f"{len(urls)} link(s)")
    summary = "\n".join([f"# Online dataset checks", "", f"Checked {checked}.", ""] + lines) + "\n"
    return findings, summary


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check datasets against live CVE, GHSA, link, KEV and EPSS sources")
    parser.add_argument("--datasets", default=str(DATASETS_ROOT), help="Root datasets directory")
    parser.add_argument("--skip-links", action="store_true", help="Do not fetch cited URLs")
    parser.add_argument("--summary", help="Also write a Markdown report (EPSS/KEV table) to this file")
    args = parser.parse_args(argv)
    root = Path(args.datasets)
    if not root.is_dir():
        print(f"Directory not found: {args.datasets}")
        return 2
    findings, summary = run(root.resolve(), args.skip_links, os.environ.get("GITHUB_TOKEN"))
    if args.summary:
        Path(args.summary).write_text(summary, encoding="utf-8")
    return print_findings(findings, root.resolve().parent)


if __name__ == "__main__":
    sys.exit(main())
