# DSGAI Scanner Tool — Roadmap

This is the public roadmap for the DSGAI scanner. It turns the internal improvement
plan into work anyone can pick up.

> **Status (v0.3 shipped):** Phases 1–3 are complete and released as `scanner-v0.3.0`. Phase 4 is in progress — templating, ecosystems, and the Semgrep export have landed; the **license split** (needs OWASP leadership sign-off) and the **precision benchmark** (needs maintainer labeling) are the remaining gated items.

> **Want one of these? Comment on the tracking issue and claim it.** Each unstarted
> item below links to a GitHub issue. Rule and precision work is labelled
> `blocked-on-phase-1` until the test corpus and self-test CI land — you can draft it
> now, it just can't merge until then.

Status legend: ✅ done · 🚧 in progress · ⬜ not started

## Phase 1 — Trust foundation (determinism, tests, schemas)

A compliance report that changes run-to-run on identical input is an opinion, not
evidence. This phase makes pattern matching deterministic and testable, so everything
after it is verifiable.

- ✅ **Rules as data** — extract every detection pattern into `rules/dsgai-rules.yaml`
  with a JSON Schema, so rules are reviewable data instead of prose.
- ✅ **Fixture app + known-answer sheet** — a small, intentionally vulnerable
  multi-language GenAI app that is the test corpus, the demo, and the contributor
  on-ramp.
- ✅ **Deterministic runner** — a stdlib Python CLI that runs the rules via ripgrep and
  emits findings JSON + SARIF, identically every run.
- ✅ **Checkpoint schema + self-test CI** — a formal, redaction-checkable output schema
  and the CI gate that makes external rule PRs safe to merge.

## Phase 2 — Secure the pipeline itself

A security scanner that is itself a prompt-injection vector or a secret-leak channel is
a liability. This phase closes those.

- ✅ **Skill rewrite** — the LLM becomes the orchestrator; the deterministic engine owns
  pattern matching. Adds an untrusted-content trust preamble, structural secret
  redaction, stable file IDs, and honest language about what the report guarantees.
- ✅ **Harden the GitHub Action** — split scanning (no secrets, runs on forks) from
  narration (restricted tools), pin actions by SHA, and fix the push-gate behaviour.
- ✅ **README truth pass + lighter sample image** — every claim matches reality; the
  ~5 MB sample screenshot is replaced with a small one from the public fixture app.
- ✅ **Pre-commit: gitleaks rule pack** — ship a battle-tested gitleaks pack, keep a
  portable no-dependency fallback script.

## Phase 3 — Precision

- ✅ **Pattern precision wave 1** — fix confirmed false positives/negatives (unquoted
  `.env` keys, the innocent-webhook SQL false positive), add per-rule confidence levels.
- ✅ **CVE pipeline rework** — move CVE fetching into the CLI (no hallucinated CVEs),
  add caching, inline suppressions with reasons, a baseline for CI gating, and
  incremental `--diff` scans.

## Phase 4 — Professional polish

- 🚧 **License split + SPDX headers** — content stays CC BY-SA 4.0; executable code
  moves to Apache-2.0 (pending OWASP leadership sign-off).
- ✅ **Single-source variants + templated report + static ATLAS map** — generate the
  tool-neutral prompt variant from the skill, render reports deterministically from a
  template, and ship a static MITRE ATLAS technique map.
- ✅ **Ecosystem expansion** — C#/NuGet, Rust, Ruby coverage, plus Semgrep and gitleaks
  rule-pack exports so incumbent toolchains carry the DSGAI framework.
- 🚧 **Benchmark + published precision report** — run against public GenAI repos,
  hand-label, and publish per-rule precision. This is what separates "interesting
  project" from "tool AppSec teams adopt".

---

*The roadmap follows the initiative's improvement plan. Checkboxes are updated as work
merges; each item's tracking issue carries the detail and the discussion.*
