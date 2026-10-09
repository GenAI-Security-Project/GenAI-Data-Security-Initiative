"""
CVSS base scores for v3.0, v3.1 and v4.0 vectors, standard library only.

v3.x follows the formulas in the FIRST CVSS v3.0 and v3.1 specifications
(section 7.1 and Appendix A). v4.0 is a port of cvss40.js, the FIRST
reference calculator (https://github.com/RedHatProductSecurity/cvss-v4-calculator,
Copyright FIRST, Red Hat, and contributors, BSD-2-Clause; the licence is in
LICENSE-cvss-v4-calculator.txt and its lookup tables are in
cvss40_tables.json). tests/test_cvss_score.py checks the port against 500
vectors scored by the reference implementation.

Written in-house because the common Python package for this is LGPL, which
the repository's dependency policy does not allow.
"""
from __future__ import annotations

import json
import math
from functools import cache
from itertools import product
from pathlib import Path


class CVSSError(ValueError):
    """The vector is not a valid CVSS vector."""


def _parse(vector: str, prefix: str, allowed: dict[str, list[str]], required: list[str]) -> dict[str, str]:
    parts = vector.strip().split("/")
    if parts[0] != prefix:
        raise CVSSError(f"must start with {prefix}/")
    metrics: dict[str, str] = {}
    for part in parts[1:]:
        key, sep, value = part.partition(":")
        if not sep or key not in allowed:
            raise CVSSError(f"unknown metric {part!r}")
        if key in metrics:
            raise CVSSError(f"metric {key} given twice")
        if value not in allowed[key]:
            raise CVSSError(f"{key}:{value} is not an allowed value (expected one of {', '.join(allowed[key])})")
        metrics[key] = value
    missing = [k for k in required if k not in metrics]
    if missing:
        raise CVSSError(f"missing base metric(s) {', '.join(missing)}")
    return metrics


# ---- CVSS v3.0 / v3.1 -------------------------------------------------------

V3_ALLOWED = {
    "AV": ["N", "A", "L", "P"], "AC": ["L", "H"], "PR": ["N", "L", "H"], "UI": ["N", "R"],
    "S": ["U", "C"], "C": ["H", "L", "N"], "I": ["H", "L", "N"], "A": ["H", "L", "N"],
    # Temporal and environmental metrics are accepted but do not change the base score.
    "E": ["X", "U", "P", "F", "H"], "RL": ["X", "O", "T", "W", "U"], "RC": ["X", "U", "R", "C"],
    "CR": ["X", "L", "M", "H"], "IR": ["X", "L", "M", "H"], "AR": ["X", "L", "M", "H"],
    "MAV": ["X", "N", "A", "L", "P"], "MAC": ["X", "L", "H"], "MPR": ["X", "N", "L", "H"],
    "MUI": ["X", "N", "R"], "MS": ["X", "U", "C"], "MC": ["X", "N", "L", "H"],
    "MI": ["X", "N", "L", "H"], "MA": ["X", "N", "L", "H"],
}
V3_BASE = ["AV", "AC", "PR", "UI", "S", "C", "I", "A"]
_AV = {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2}
_AC = {"L": 0.77, "H": 0.44}
_PR_UNCHANGED = {"N": 0.85, "L": 0.62, "H": 0.27}
_PR_CHANGED = {"N": 0.85, "L": 0.68, "H": 0.5}
_UI = {"N": 0.85, "R": 0.62}
_CIA = {"H": 0.56, "L": 0.22, "N": 0.0}


def _roundup_31(x: float) -> float:
    """v3.1 Appendix A Roundup, which avoids floating-point artefacts."""
    i = round(x * 100000)
    return i / 100000.0 if i % 10000 == 0 else (math.floor(i / 10000) + 1) / 10.0


def _roundup_30(x: float) -> float:
    return math.ceil(x * 10) / 10


def cvss3_base_score(vector: str) -> float:
    version = vector.strip().split("/")[0]
    if version not in ("CVSS:3.0", "CVSS:3.1"):
        raise CVSSError("must start with CVSS:3.0/ or CVSS:3.1/")
    m = _parse(vector, version, V3_ALLOWED, V3_BASE)
    roundup = _roundup_31 if version == "CVSS:3.1" else _roundup_30
    changed = m["S"] == "C"
    iss = 1 - (1 - _CIA[m["C"]]) * (1 - _CIA[m["I"]]) * (1 - _CIA[m["A"]])
    impact = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15 if changed else 6.42 * iss
    pr = (_PR_CHANGED if changed else _PR_UNCHANGED)[m["PR"]]
    exploitability = 8.22 * _AV[m["AV"]] * _AC[m["AC"]] * pr * _UI[m["UI"]]
    if impact <= 0:
        return 0.0
    if changed:
        return roundup(min(1.08 * (impact + exploitability), 10))
    return roundup(min(impact + exploitability, 10))


# ---- CVSS v4.0 (port of the FIRST reference calculator) ---------------------

@cache
def _v4_tables() -> dict:
    return json.loads((Path(__file__).resolve().parent / "cvss40_tables.json").read_text(encoding="utf-8"))


def _v4_allowed() -> dict[str, list[str]]:
    t = _v4_tables()["METRICS"]
    return {k: v for cat in ("BASE", "THREAT", "ENVIRONMENTAL", "SUPPLEMENTAL") for k, v in t[cat].items()}


def _effective(m: dict[str, str], metric: str) -> str:
    worst_case = {"E": "A", "CR": "H", "IR": "H", "AR": "H"}
    if m.get(metric, "X") == "X" and metric in worst_case:
        return worst_case[metric]
    modified = m.get("M" + metric, "X")
    if modified != "X":
        return modified
    return m[metric]


def _equivalent_classes(m: dict[str, str]) -> str:
    e = lambda k: _effective(m, k)  # noqa: E731
    av, pr, ui = e("AV"), e("PR"), e("UI")
    if av == "N" and pr == "N" and ui == "N":
        eq1 = 0
    elif (av == "N" or pr == "N" or ui == "N") and av != "P":
        eq1 = 1
    else:
        eq1 = 2
    eq2 = 0 if e("AC") == "L" and e("AT") == "N" else 1
    vc, vi, va = e("VC"), e("VI"), e("VA")
    if vc == "H" and vi == "H":
        eq3 = 0
    elif vc == "H" or vi == "H" or va == "H":
        eq3 = 1
    else:
        eq3 = 2
    if e("MSI") == "S" or e("MSA") == "S":
        eq4 = 0
    elif e("SC") == "H" or e("SI") == "H" or e("SA") == "H":
        eq4 = 1
    else:
        eq4 = 2
    eq5 = {"A": 0, "P": 1, "U": 2}[e("E")]
    eq6 = 0 if (e("CR") == "H" and vc == "H") or (e("IR") == "H" and vi == "H") or (e("AR") == "H" and va == "H") else 1
    return f"{eq1}{eq2}{eq3}{eq4}{eq5}{eq6}"


def _round_half_up(value: float) -> float:
    return math.floor((value + 1e-6) * 10 + 0.5) / 10


def cvss4_base_score(vector: str) -> float:
    """The CVSS v4.0 score of a vector (CVSS-B, -BT, -BE or -BTE per its metrics)."""
    allowed = _v4_allowed()
    base = list(_v4_tables()["METRICS"]["BASE"])
    m = _parse(vector, "CVSS:4.0", allowed, base)
    for k, values in allowed.items():
        m.setdefault(k, values[0])
    # No impact on the vulnerable or any subsequent system scores 0.
    if all(_effective(m, k) == "N" for k in ("VC", "VI", "VA", "SC", "SI", "SA")):
        return 0.0

    t = _v4_tables()
    lookup, levels = t["LOOKUP_TABLE"], t["METRIC_LEVELS"]
    max_composed, max_severity = t["MAX_COMPOSED"], t["MAX_SEVERITY"]
    macro = _equivalent_classes(m)
    value = lookup[macro]
    eq1, eq2, eq3, eq4, eq5, eq6 = (int(c) for c in macro)

    def score_of(*eqs: int):
        return lookup.get("".join(str(x) for x in eqs))

    lower_eq1 = score_of(eq1 + 1, eq2, eq3, eq4, eq5, eq6)
    lower_eq2 = score_of(eq1, eq2 + 1, eq3, eq4, eq5, eq6)
    if eq3 == 1 and eq6 == 1 or eq3 == 0 and eq6 == 1:
        lower_eq3eq6 = score_of(eq1, eq2, eq3 + 1, eq4, eq5, eq6)
    elif eq3 == 1 and eq6 == 0:
        lower_eq3eq6 = score_of(eq1, eq2, eq3, eq4, eq5, eq6 + 1)
    elif eq3 == 0 and eq6 == 0:
        left = score_of(eq1, eq2, eq3, eq4, eq5, eq6 + 1)
        right = score_of(eq1, eq2, eq3 + 1, eq4, eq5, eq6)
        candidates = [s for s in (left, right) if s is not None]
        # Math.max with a missing (NaN) operand is NaN in the reference.
        lower_eq3eq6 = max(candidates) if len(candidates) == 2 else None
    else:
        lower_eq3eq6 = score_of(eq1, eq2, eq3 + 1, eq4, eq5, eq6 + 1)
    lower_eq4 = score_of(eq1, eq2, eq3, eq4 + 1, eq5, eq6)
    lower_eq5 = score_of(eq1, eq2, eq3, eq4, eq5 + 1, eq6)

    eq_maxes = [
        max_composed["eq1"][str(eq1)],
        max_composed["eq2"][str(eq2)],
        max_composed["eq3"][str(eq3)][str(eq6)],
        max_composed["eq4"][str(eq4)],
        max_composed["eq5"][str(eq5)],
    ]
    # The first highest-severity vector of the MacroVector that the scored
    # vector does not exceed on any metric; as in the reference, the last one
    # tried is used if none qualifies.
    distances: dict[str, float] = {}
    for parts in product(*eq_maxes):
        max_vector = dict(p.split(":") for p in "".join(parts).strip("/").split("/"))
        distances = {k: levels[k][_effective(m, k)] - levels[k][max_vector[k]] for k in levels}
        if all(dist >= 0 for dist in distances.values()):
            break

    step = 0.1
    current = {
        "eq1": distances["AV"] + distances["PR"] + distances["UI"],
        "eq2": distances["AC"] + distances["AT"],
        "eq3eq6": sum(distances[k] for k in ("VC", "VI", "VA", "CR", "IR", "AR")),
        "eq4": distances["SC"] + distances["SI"] + distances["SA"],
    }
    depth = {
        "eq1": max_severity["eq1"][str(eq1)] * step,
        "eq2": max_severity["eq2"][str(eq2)] * step,
        "eq3eq6": max_severity["eq3eq6"][str(eq3)][str(eq6)] * step,
        "eq4": max_severity["eq4"][str(eq4)] * step,
    }
    normalized, n_lower = 0.0, 0
    for key, lower in (("eq1", lower_eq1), ("eq2", lower_eq2), ("eq3eq6", lower_eq3eq6), ("eq4", lower_eq4)):
        if lower is not None:
            n_lower += 1
            normalized += (value - lower) * (current[key] / depth[key])
    if lower_eq5 is not None:
        n_lower += 1  # EQ5's proportion is always 0
    mean = normalized / n_lower if n_lower else 0.0
    return _round_half_up(max(0.0, min(10.0, value - mean)))


def base_score(vector: str) -> float:
    """Base score of any CVSS v3.0, v3.1 or v4.0 vector."""
    if vector.startswith("CVSS:4.0/"):
        return cvss4_base_score(vector)
    if vector.startswith(("CVSS:3.0/", "CVSS:3.1/")):
        return cvss3_base_score(vector)
    raise CVSSError("must start with CVSS:3.0/, CVSS:3.1/ or CVSS:4.0/")
