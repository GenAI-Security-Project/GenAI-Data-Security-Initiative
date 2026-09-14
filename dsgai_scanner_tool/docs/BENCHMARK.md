# DSGAI Scanner — Precision Benchmark (methodology + labeling kit)

> **Status: HAND-OFF.** The finding sheets are prepared by tooling; the
> **hand-labeling and the per-rule precision numbers are a maintainer task**
> (they require human judgment and a responsible-disclosure decision). This file
> is the methodology and the template — fill the `label:` and `notes:` columns,
> then compute precision with the snippet below. **This document is what
> separates "interesting project" from "tool AppSec teams adopt."**

## Responsible-handling rule (read first)

If the benchmark surfaces a **real, live vulnerability in a public repo**, do
**not** publish that finding here. Follow the monorepo's
[`SECURITY.md`](../../SECURITY.md) disclosure process first, and exclude the
finding from the public sheet until it is resolved. The benchmark measures the
*scanner's precision*, not a list of who is vulnerable.

## Candidate corpus (record exact commit SHAs)

Pick 5–10 public GenAI repos spanning frameworks and maturity. Suggested mix
(confirm each is still representative before running):

- 2–3 popular **LangChain** example/starter apps.
- 1–2 **LlamaIndex** example apps.
- 1–2 production-grade OSS **agents** (e.g. an MCP server, a RAG service).
- 1 **non-Python** GenAI service (JS/Go/C#) to exercise the ecosystem work.

For each: record `repo`, `commit_sha`, `scanned_at`, and the `ruleset_version`
(from `DSGAI-scan.json`) so the run is reproducible.

## How to run (deterministic, $0)

```bash
for repo in <list>; do
  git -C "$repo" rev-parse HEAD                          # record the SHA
  python cli/dsgai_scan.py scan "$repo" --no-cve \
    --json-out "bench/$(basename "$repo").json" --format none
done
```

Use `--no-cve` for the precision benchmark (CVE precision is measured separately
against OSV ground truth). Merge the `findings` arrays into the labeling sheet.

## Labeling sheet template

One row per finding. Fill `label` (TP / FP) and `notes` by inspecting the file.

```yaml
# bench/labels.yaml
- repo: owner/name
  commit: <sha>
  rule_id: P02.1
  control: DSGAI02
  path: <path>
  line: <n>
  status: fail
  label: TP        # TP (true positive) | FP (false positive)
  notes: ""        # why; for value-bearing, DO NOT paste the secret
```

## Per-rule precision (run after labeling)

```python
import yaml, collections
rows = yaml.safe_load(open("bench/labels.yaml"))
by_rule = collections.defaultdict(lambda: [0, 0])   # rule -> [TP, FP]
for r in rows:
    by_rule[r["rule_id"]][0 if r["label"] == "TP" else 1] += 1
print(f"{'rule':8} {'TP':>4} {'FP':>4} {'precision':>10}")
for rule, (tp, fp) in sorted(by_rule.items()):
    prec = tp / (tp + fp) if (tp + fp) else float("nan")
    print(f"{rule:8} {tp:>4} {fp:>4} {prec:>10.2f}")
```

## Feeding results back

- For rules with low precision, **lower `confidence`** (or tighten the PCRE with a
  fixture case) in `rules/dsgai-rules.yaml` and note the change here.
- Publish the aggregate table (per-rule TP/FP/precision) and the methodology.
  **Never** publish an unresolved live finding (see the responsible-handling rule).

## Results

_To be filled after labeling._

| Rule | TP | FP | Precision |
|---|---|---|---|
| _pending_ | | | |
