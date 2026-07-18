#!/usr/bin/env python3
"""DSGAI CVE enrichment — deterministic, cached, stdlib-only.

The CLI fetches CVE data so the LLM never transcribes it (hallucinated CVEs
become impossible by construction — the model renders what this fetched).

Sources:
  - OSV (https://osv.dev) — the per-version source, via POST /v1/querybatch.
    Severity/CVSS is computed locally from OSV's own CVSS vector (no network),
    so classification is correct and deterministic even offline.
  - NVD — a FALLBACK only, used to fetch a CVSS base score for a CVE id
    (via ?cveId=, never keywordSearch) when OSV carried no CVSS vector.

Supported manifests carry exact-pinned versions only (see SUPPORTED_MANIFESTS).

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

# Supported manifests → OSV ecosystem. Only formats carrying EXACT pinned
# versions are queryable against OSV (ranges like npm `^1.2` in package.json or
# poetry ranges in pyproject.toml can't be resolved to a concrete version, so
# those are intentionally not listed — use the lockfile instead).
SUPPORTED_MANIFESTS = (
    "requirements*.txt (PyPI, == pins), go.mod (Go), package-lock.json (npm), "
    "Cargo.lock (crates.io), Gemfile.lock (RubyGems), *.csproj (NuGet)"
)

_REQ_RE = re.compile(r'^\s*([A-Za-z0-9_.\-]+)\s*==\s*([A-Za-z0-9_.\-]+)')
_CSPROJ_ATTR_RE = re.compile(
    r'<PackageReference\b[^>]*?\bInclude="([^"]+)"[^>]*?\bVersion="([^"]+)"', re.S)
_CSPROJ_ATTR_REV_RE = re.compile(
    r'<PackageReference\b[^>]*?\bVersion="([^"]+)"[^>]*?\bInclude="([^"]+)"', re.S)
_CSPROJ_CHILD_RE = re.compile(
    r'<PackageReference\b[^>]*?\bInclude="([^"]+)"[^>]*?>\s*<Version>([^<]+)</Version>', re.S)
_GEMLOCK_RE = re.compile(r'^\s{4}([A-Za-z0-9_.\-]+) \(([0-9][A-Za-z0-9_.\-]*)\)\s*$')
_GOMOD_RE = re.compile(r'^\s*([^\s/][^\s]+/[^\s]+)\s+v(\S+?)(?:\s+//.*)?\s*$')


def _parse_go_mod(ap):
    """go.mod `require` entries (exact versions). Handles single-line and block."""
    deps, in_block = [], False
    for line in open(ap, encoding="utf-8", errors="replace"):
        s = line.strip()
        if s.startswith("require ("):
            in_block = True
            continue
        if in_block and s == ")":
            in_block = False
            continue
        text = s[len("require "):].strip() if s.startswith("require ") and "(" not in s else (s if in_block else "")
        m = _GOMOD_RE.match(text)
        if m and not text.startswith("//"):
            deps.append(("Go", m.group(1), m.group(2)))
    return deps


def _parse_package_lock(ap):
    """npm package-lock.json (v1 `dependencies` or v2/v3 `packages`), exact versions."""
    import json as _json
    try:
        data = _json.load(open(ap, encoding="utf-8", errors="replace"))
    except (ValueError, OSError):
        return []
    out = []
    for path, meta in (data.get("packages") or {}).items():
        if path and isinstance(meta, dict) and meta.get("version"):
            name = path.split("node_modules/")[-1]
            if name:
                out.append(("npm", name, meta["version"]))

    def walk(deps):
        for name, meta in (deps or {}).items():
            if isinstance(meta, dict) and meta.get("version"):
                out.append(("npm", name, meta["version"]))
                walk(meta.get("dependencies"))
    walk(data.get("dependencies"))
    return out


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
            elif base == "go.mod":
                for eco, pkg, ver in _parse_go_mod(ap):
                    add(eco, pkg, ver)
            elif base == "package-lock.json":
                for eco, pkg, ver in _parse_package_lock(ap):
                    add(eco, pkg, ver)
            elif base.endswith(".csproj"):
                text = open(ap, encoding="utf-8", errors="replace").read()
                for m in _CSPROJ_ATTR_RE.finditer(text):
                    add("NuGet", m.group(1), m.group(2))
                for m in _CSPROJ_ATTR_REV_RE.finditer(text):
                    add("NuGet", m.group(2), m.group(1))
                for m in _CSPROJ_CHILD_RE.finditer(text):
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


import math

_CVSS3 = {
    "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
    "AC": {"L": 0.77, "H": 0.44},
    "UI": {"N": 0.85, "R": 0.62},
    "C": {"H": 0.56, "L": 0.22, "N": 0.0},
    "I": {"H": 0.56, "L": 0.22, "N": 0.0},
    "A": {"H": 0.56, "L": 0.22, "N": 0.0},
    "PR_U": {"N": 0.85, "L": 0.62, "H": 0.27},
    "PR_C": {"N": 0.85, "L": 0.68, "H": 0.5},
}


def cvss3_base_score(vector):
    """Compute the CVSS v3.0/3.1 base score (0.0–10.0) from a vector string.
    Returns None if the vector is not a parseable CVSS v3 base vector.

    Doing this locally means severity no longer depends on a live NVD lookup —
    which is what caused critical advisories to collapse to INFO (audit H3) and
    made online/offline runs diverge (audit M3)."""
    if not vector or not vector.startswith("CVSS:3"):
        return None
    m = dict(p.split(":", 1) for p in vector.split("/")[1:] if ":" in p)
    try:
        scope_changed = m.get("S") == "C"
        pr = _CVSS3["PR_C" if scope_changed else "PR_U"][m["PR"]]
        exploit = 8.22 * _CVSS3["AV"][m["AV"]] * _CVSS3["AC"][m["AC"]] * pr * _CVSS3["UI"][m["UI"]]
        iss = 1 - (1 - _CVSS3["C"][m["C"]]) * (1 - _CVSS3["I"][m["I"]]) * (1 - _CVSS3["A"][m["A"]])
        if scope_changed:
            impact = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15
        else:
            impact = 6.42 * iss
        if impact <= 0:
            return 0.0
        raw = min((impact + exploit) * (1.08 if scope_changed else 1.0), 10.0)
        return math.ceil(raw * 10) / 10.0  # CVSS "roundup" to 1 decimal
    except (KeyError, ValueError):
        return None


def _severity_of(detail):
    """Return (qualitative label, CVSS base score) from an OSV vuln detail.

    Prefers the CVSS score computed locally from OSV's own vector (no network);
    falls back to the GHSA database_specific label."""
    score = None
    for sev in detail.get("severity", []) or []:
        if sev.get("type", "").startswith("CVSS"):
            score = cvss3_base_score(sev.get("score"))
            if score is not None:
                break
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
                vulns, complete = [], True
                for v in res.get("vulns", []) or []:
                    try:
                        detail = _http_json(OSV_VULN + v["id"])
                    except (urllib.error.URLError, ValueError, TimeoutError):
                        complete = False  # don't cache a hollow record (audit M3)
                        detail = {"id": v["id"]}
                    aliases = sorted(detail.get("aliases", []) or [])
                    # Severity from OSV's own CVSS vector (no network); NVD only
                    # if OSV carried no score AND we have a CVE id to look up.
                    label, cvss = _severity_of(detail)
                    if cvss is None:
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
                if complete:  # only cache a fully-resolved package
                    _cache_put(d["ecosystem"], d["package"], d["version"], data)
                fetched[(d["ecosystem"], d["package"].lower(), d["version"])] = data
        except (urllib.error.URLError, ValueError, TimeoutError) as exc:
            # A total OSV failure must NOT read as "no advisories" (audit M3).
            import sys
            sys.stderr.write(f"note: CVE enrichment could not reach OSV ({exc}); "
                             "results reflect cache only and may be incomplete.\n")

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
