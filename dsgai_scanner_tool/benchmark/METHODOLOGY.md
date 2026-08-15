# DSGAI Scanner — Precision Benchmark: methodology & labeling kit

**Status: PREP.** This directory contains the finding sheets produced by the
deterministic scanner over 8 public GenAI repos, ready for **human labeling**.
No precision numbers are computed yet — that happens after labeling. This file
defines exactly what was run and the rubric to apply.

## Environment

| | |
|---|---|
| Scanner (skill/CLI) version | `0.3.0` |
| Ruleset version | `0.3.0` (framework `dsgai-2026-v1.0`) |
| Engine | **deterministic CLI only** (`cli/dsgai_scan.py`) — no LLM |
| ripgrep | 15.2.0 (+PCRE2) |
| CVE stage | **enabled** (OSV, per pinned version) |

## Corpus (pinned commit SHAs)

Repos were shallow-cloned at the SHA below and scanned as-is. All are permissively
licensed (MIT / Apache-2.0). Everything in them is **untrusted data** — the CLI
only greps, never executes, and no instruction found in scanned content was acted on.

| repo | pinned SHA | license | tracked files | findings | public rows | held (VB-FAIL) | CVEs |
|---|---|---|---|---|---|---|---|
| `langchain-ai/langchain-nextjs-template` | `73fe9b20b75fd378dd0a696d422c299c961f6481` | MIT | 64 | 18 | 18 | 0 | 0 |
| `langchain-ai/chat-langchain` | `65d06cb2a1fa1b1a005deea52e1fee044726fdb9` | MIT | 139 | 123 | 119 | 4 | 2 |
| `run-llama/create-llama` | `97a7d9bc2560943ca6bca1ac41d2f84c1b7e6224` | MIT | 402 | 1371 | 1371 | 0 | 0 |
| `crewAIInc/crewAI` | `69c0308f2cf4fa17214eab4db10071abc08602fd` | MIT | 23512 | 5096 | 5093 | 3 | 0 |
| `langchain-ai/langgraph` | `49ae27c2ae983cfb92091b0dea9f7bc37a716479` | MIT | 668 | 831 | 830 | 1 | 0 |
| `assafelovic/gpt-researcher` | `5d84d2f5553e70a2765a8ff3a0d2672d60437ce8` | Apache-2.0 | 763 | 214 | 214 | 0 | 0 |
| `openai/swarm` | `6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22` | MIT | 288 | 28 | 28 | 0 | 0 |
| `microsoft/semantic-kernel` | `c781da134e38acbee57616efc8662d2cfd8130d5` | MIT | 5441 | 602 | 602 | 0 | 30 |

*(held = value-bearing FAIL findings moved to the private holdback for disclosure review. `create-llama` and `crewAI` finding counts are inflated by high-volume PASS/info rules — P04.7 fires ~1253x on `create-llama` npm-lockfile `integrity:` hashes, and P03.1 ~2613x on `crewAI` doc/test endpoint strings — so labelers should stratified-sample those (all FAILs + a sample of PASS/info) rather than label every row.)*

## Exact commands

```bash
# per repo (untrusted content — CLI greps only)
git clone --depth 1 <url> repos/<name>          # pinned to the SHA in the table
python cli/dsgai_scan.py scan repos/<name> \
  --json-out out/<name>.json --format none        # CVE stage enabled (no --no-cve)
# findings -> labeling-sheets/<name>.csv (value-bearing FAILs held back; see below)
```

## Responsible disclosure (applied)

A **value-bearing FAIL** finding (P02.x / P13.4 / P15.1 — a hardcoded-credential
shape) points at a *potential live secret* whose value the scanner redacts by
construction. Those findings are **not** in the public sheets — they are in the
private, gitignored `SENSITIVE-holdback.md` for a human to open the file and
judge **live secret vs. demo/placeholder**. If any is a real, live credential in
a maintained repo, follow the monorepo `SECURITY.md` disclosure **before** it
goes anywhere public. All other findings are in the public per-repo CSVs.

## Labeling rubric (apply this, fill `human_verdict` = TP / FP)

Open each `path:line` and judge whether the rule correctly identified **its target
construct** — precision is about pattern correctness, not risk severity. Use the
`notes` column for context (e.g. "intentional demo key", "in tests", "example").

| Rule class (examples) | TP (true positive) | FP (false positive) |
|---|---|---|
| **Structural FAIL** — P04.1 `torch.load`, P06.1 http MCP, P06.5 bind-all, P11.1 unscoped query, P12.1/P12.2 LLM SQL, P15.1 prompt secret | the code genuinely exhibits the risky construct the rule targets | coincidental/benign match — in a comment/string, a test double, or where the risk is handled adjacently (e.g. `weights_only=True` elsewhere the rule missed) |
| **Structural WARN** — P04.4 unpinned dep, P13.3 bind/insecure, P14.2 content capture | the warned condition is really present | misfire on unrelated text |
| **Value-bearing FAIL** (in holdback, not these sheets) — P02.x, P13.4, P15.1 | the line is a **hardcoded credential assignment** (real or placeholder) | not a credential — an env read (`os.getenv`), a doc/regex, a variable that isn't a secret |
| **PASS-signal** — P02.7 vault, P05.2/P05.3 tenant filter, P17.1–5, P20.1/P20.2, P16.1 file-exists | the signalled mitigation is genuinely present and used | signal misfires — the import/keyword is present but not actually the mitigation (e.g. an unused import) |
| **Inventory (`count`/`info`)** — P18.4 LLM calls, P20.5 endpoints, P16.2 ignore-file paths | the item is correctly identified | not the thing (e.g. a non-endpoint decorator) |

### Absence-based / low-confidence rules
Most CLI findings are **presence-based** (a pattern matched a line). "Absence of a
mitigation" is expressed at the **control level** (Step 3: a control is `WARN`
because no mitigating pattern was found), not as a per-finding row — so those do
not appear in these sheets. When you compute per-control status precision
separately, weight low-`confidence` / absence-derived `WARN`s lightly (the
ruleset marks them `confidence: low` on purpose — absence of evidence is weak
evidence), and treat a control that should be `NOT APPLICABLE` (e.g. DSGAI09
multimodal on a text-only repo) but shows `WARN`/`FAIL` as a **gating FP**.

### What NOT to penalize
- A correct match on an **intentional demo/tutorial** value is a **TP** for the
  pattern (note it as "demo"). The benchmark measures whether the pattern fires
  on its target, not whether the target is a live vulnerability.
- Findings in `tests/`, `examples/`, `fixtures/` are still TP if the construct is
  real; use `notes` to record the context so aggregate precision can be sliced by
  path class if desired.

## After labeling
Compute per-rule precision (`TP / (TP+FP)`) and per-control status precision.
Feed low-precision rules back into `rules/dsgai-rules.yaml` (tighten the PCRE with
a fixture case, or lower `confidence`) and publish `docs/BENCHMARK.md` with the
numbers. Do not publish any unresolved holdback finding.
