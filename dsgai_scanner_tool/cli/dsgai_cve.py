#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""DSGAI CVE enrichment — deterministic, cached, stdlib-only.

The CLI fetches CVE data so the LLM never transcribes it (hallucinated CVEs
become impossible by construction — the model renders what this fetched).

Sources:
  - OSV (https://osv.dev) — the only per-version source, via POST /v1/querybatch.
  - NVD — used SOLELY to enrich a known CVE id with CVSS via ?cveId= (never
    keywordSearch, which returns junk for names like "ai"/"instructor").

Cache: ~/.dsgai/cve-cache/<ecosystem>/<package>@<version>.json, 24h TTL.
`--refresh-cve` ignores the cache; `offline=True` uses cache only (no network).
"""
import json
import os
import re
import time
import urllib.error
import urllib.request

OSV_BATCH = "https://api.osv.dev/v1/querybatch"
OSV_VULN = "https://api.osv.dev/v1/vulns/"
NVD_CVE = "https://services.nvd.nist.gov/rest/json/cves/2.0"
CACHE_TTL = 24 * 3600
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".dsgai", "cve-cache")

# Minimal ecosystem detection from manifest filename → OSV ecosystem.
ECOSYSTEMS = {
    "requirements.txt": "PyPI", "requirements": "PyPI", "pyproject.toml": "PyPI",
    "package.json": "npm", "go.mod": "Go", "Cargo.toml": "crates.io",
    "Gemfile.lock": "RubyGems",
}

_REQ_RE = re.compile(r'^\s*([A-Za-z0-9_.\-]+)\s*==\s*([A-Za-z0-9_.\-]+)')
_CSPROJ_RE = re.compile(r'<PackageReference\s+Include="([^"]+)"\s+Version="([^"]+)"')
_GEMLOCK_RE = re.compile(r'^\s{4}([A-Za-z0-9_.\-]+) \(([0-9][A-Za-z0-9_.\-]*)\)\s*$')


def _parse_cargo_lock(ap):
    deps, name = [], None
    for line in open(ap, encoding="utf-8", errors="replace"):
        s = line.strip()
        if s.startswith("name = "):
            name = s.split('"')[1] if '"' in s else None
        elif s.startswith("version = ") and name:
            deps.append(("crates.io", name, s.split('"')[1]))
            name = None
    return deps


def _cache_path(eco, pkg, ver):
    safe = re.sub(r'[^A-Za-z0-9_.\-]', '_', f"{pkg}@{ver}")
    return os.path.join(CACHE_DIR, re.sub(r'[^A-Za-z0-9_.\-]', '_', eco), safe + ".json")


def _cache_get(eco, pkg, ver, refresh):
    if refresh:
        return None
    p = _cache_path(eco, pkg, ver)
    try:
        if time.time() - os.path.getmtime(p) <= CACHE_TTL:
            return json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return None


def _cache_put(eco, pkg, ver, data):
    p = _cache_path(eco, pkg, ver)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, sort_keys=True)


def parse_dependencies(discovered):
    """Return [{ecosystem, package, version}] from pinned manifest entries.

    `discovered` is a list of (abs_path, rel_path). Only exact-pinned entries are
    queried (OSV needs a concrete version).
    """
    deps, seen = [], set()

    def add(eco, pkg, ver):
        key = (eco, pkg.lower(), ver)
        if key not in seen:
            seen.add(key)
            deps.append({"ecosystem": eco, "package": pkg, "version": ver})

    for ap, rel in discovered:
        base = os.path.basename(rel)
        try:
            if base.startswith("requirements") and base.endswith(".txt"):
                for line in open(ap, encoding="utf-8", errors="replace"):
                    if line.lstrip().startswith("#"):
                        continue
                    m = _REQ_RE.match(line)
                    if m:
                        add("PyPI", m.group(1), m.group(2))
            elif base == "Cargo.lock":
                for eco, pkg, ver in _parse_cargo_lock(ap):
                    add(eco, pkg, ver)
            elif base == "Gemfile.lock":
                for line in open(ap, encoding="utf-8", errors="replace"):
                    m = _GEMLOCK_RE.match(line.rstrip("\n"))
                    if m:
                        add("RubyGems", m.group(1), m.group(2))
            elif base.endswith(".csproj"):
                for m in _CSPROJ_RE.finditer(open(ap, encoding="utf-8", errors="replace").read()):
                    add("NuGet", m.group(1), m.group(2))
        except OSError:
            continue
    return deps


def _http_json(url, data=None, timeout=20):
    headers = {"Content-Type": "application/json", "User-Agent": "dsgai-scan"}
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers=headers, method="POST" if data is not None else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _severity_of(detail):
    """Extract a coarse severity + CVSS score from an OSV vuln detail."""
    score = None
    for sev in detail.get("severity", []) or []:
        if sev.get("type", "").startswith("CVSS"):
            # OSV gives a vector; we keep the label from DB-specific fields below.
            score = sev.get("score")
    # database_specific severity label (GHSA gives HIGH/CRITICAL/…)
    label = (detail.get("database_specific", {}) or {}).get("severity")
    return label, score


def classify(label, cvss):
    """EXPLOITABLE for high/critical (CVSS >= 7 or CRITICAL/HIGH label);
    VULNERABLE for anything else with a severity; INFO if wholly unknown."""
    if (cvss is not None and cvss >= 7.0) or label in ("CRITICAL", "HIGH"):
        return "EXPLOITABLE"
    if (cvss is not None) or label in ("MODERATE", "MEDIUM", "LOW"):
        return "VULNERABLE"
    return "INFO"


def enrich_cvss_nvd(cve_id, offline, timeout=20):
    """Fetch CVSS base score for a CVE id from NVD (cveId only). None on failure."""
    if offline or not cve_id.startswith("CVE-"):
        return None
    try:
        data = _http_json(f"{NVD_CVE}?cveId={cve_id}", timeout=timeout)
        for v in data.get("vulnerabilities", []):
            metrics = v.get("cve", {}).get("metrics", {})
            for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
                if metrics.get(key):
                    return metrics[key][0]["cvssData"].get("baseScore")
    except (urllib.error.URLError, ValueError, KeyError, TimeoutError):
        return None
    return None


def enrich(discovered, offline=False, refresh=False):
    """Return a list of CVE finding dicts (deterministic order).

    Each: {package, version, ecosystem, id, aliases, summary, status, cvss}.
    Cached per {ecosystem, package, version}; second run needs no network.
    """
    deps = parse_dependencies(discovered)
    results = []
    uncached = []
    cache_map = {}
    for d in deps:
        c = _cache_get(d["ecosystem"], d["package"], d["version"], refresh)
        if c is not None:
            cache_map[(d["ecosystem"], d["package"].lower(), d["version"])] = c
        else:
            uncached.append(d)

    fetched = {}
    if uncached and not offline:
        try:
            queries = [{"package": {"name": d["package"], "ecosystem": d["ecosystem"]},
                        "version": d["version"]} for d in uncached]
            batch = _http_json(OSV_BATCH, {"queries": queries})
            for d, res in zip(uncached, batch.get("results", [])):
                vulns = []
                for v in res.get("vulns", []) or []:
                    try:
                        detail = _http_json(OSV_VULN + v["id"])
                    except (urllib.error.URLError, ValueError, TimeoutError):
                        detail = {"id": v["id"]}
                    aliases = sorted(detail.get("aliases", []) or [])
                    label, _ = _severity_of(detail)
                    # NVD enriches CVSS for known CVE ids; stored in cache so
                    # offline re-runs are byte-identical to the online run.
                    cvss = None
                    for aid in [detail.get("id", v["id"])] + aliases:
                        if aid.startswith("CVE-"):
                            cvss = enrich_cvss_nvd(aid, offline=False)
                            if cvss is not None:
                                break
                    vulns.append({
                        "id": detail.get("id", v["id"]),
                        "aliases": aliases,
                        "summary": (detail.get("summary") or "")[:300],
                        "cvss": cvss,
                        "status": classify(label, cvss),
                    })
                data = {"vulns": vulns}
                _cache_put(d["ecosystem"], d["package"], d["version"], data)
                fetched[(d["ecosystem"], d["package"].lower(), d["version"])] = data
        except (urllib.error.URLError, ValueError, TimeoutError):
            pass  # network failure → whatever is cached still renders

    merged = dict(cache_map)
    merged.update(fetched)
    for d in deps:
        key = (d["ecosystem"], d["package"].lower(), d["version"])
        for v in merged.get(key, {}).get("vulns", []):
            # cvss/status come from the cache (populated at fetch time) so an
            # offline re-run is byte-identical to the online run that seeded it.
            results.append({
                "package": d["package"], "version": d["version"],
                "ecosystem": d["ecosystem"], "id": v["id"],
                "aliases": v.get("aliases", []), "summary": v.get("summary", ""),
                "status": v.get("status", "INFO"), "cvss": v.get("cvss"),
            })
    results.sort(key=lambda x: (x["package"], x["version"], x["id"]))
    return results
