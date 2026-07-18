# Changelog — DSGAI Scanner Tool v0.3

All notable changes for the v0.3 line. This file is appended by every merged PR.
v0.3 releases when Phases 0–2 of the improvement plan are complete.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) loosely;
dates are ISO-8601. The previous line is recorded in [`CHANGES_v0.2.md`](CHANGES_v0.2.md).

## [Unreleased]

### Added
- Contributor infrastructure: `[scanner]` GitHub issue-form templates (false-positive,
  false-negative, new-rule, bug), scanner `CONTRIBUTING.md`, public `ROADMAP.md`, and
  this changelog scaffold. (PR-01)
- Repo hygiene: **Non-goals** section in the README, root `CODEOWNERS` for
  `dsgai_scanner_tool/`, path-filtered `scanner-lint.yml` CI (shellcheck + yamllint +
  internal-link check), a deterministic markdown internal-link checker
  (`scripts/check_md_links.py`), and a `.gitattributes` forcing LF on scripts/YAML so
  Windows checkouts can't ship CRLF that breaks Linux CI. (PR-02)
- **Rules as data**: all 106 detection patterns extracted verbatim from the skill's
  Step 2 into `rules/dsgai-rules.yaml` (source of truth), validated by
  `rules/rules.schema.json`, compiled to `rules/dsgai-rules.json` by
  `build/build_rules_json.py`. Compound logic (`subtract`, `requires_nearby`,
  `exclude_globs`, `gated_on`) and per-rule `classification`/`signal`/`confidence` are
  encoded. `rules/README.md` documents the format. Skill Step 2 now marks the YAML as
  canonical. (PR-03)

- **Fixture app + known-answer sheet**: `tests/fixtures/vulnerable-app/` — a small,
  intentionally-vulnerable multi-language GenAI app (Python + JS), all secrets fake and
  canonical. `tests/expected-findings.yaml` pins every finding to an exact line (25
  findings, resolved through `subtract`/`requires_nearby`), plus `must_not_flag` negative
  cases and `known_false_negatives` (unquoted `.env`, `xoxb-` token, JS endpoint) with
  the PR that fixes each. Includes the confirmed P02.1 false negative and P12.1 false
  positive as tracked `known_bug`s, and an adversarial `docs/NOTES.md` prompt-injection
  fixture. `tests/regen_expected.py` regenerates/verifies line-pins;
  `.github/secret_scanning.yml` ignores the fixture fakes. (PR-04)
- **Deterministic runner**: `cli/dsgai_scan.py` — a single-file, stdlib-only-at-runtime
  CLI that runs the ruleset via `rg --pcre2` and emits `DSGAI-scan.json` + SARIF 2.1.0 +
  a table summary, identically every run. Value-bearing rules run location-only
  (`rg -o --replace ''`) so secrets never leave ripgrep; findings carry no match content
  by construction. Implements `subtract`/`requires_nearby`/`exclude_globs`/`gated_on`,
  per-control classification, `--scope`/`--exclude`, `SOURCE_DATE_EPOCH`, and `scan` /
  `detect` / `doctor` subcommands with CI-friendly exit codes. `tests/test_runner.py`
  (9 tests) asserts every PCRE compiles, the fixture scan matches the answer sheet
  exactly, SARIF validity, and the redaction guarantee. `requirements-dev.txt` +
  dependabot `pip` for the scanner. (PR-05)
- **Checkpoint schema + CI self-test**: `schemas/dsgai-scan.schema.json` formalizes
  `DSGAI-scan.json` and **forbids** `match_text`/`content`/`value`/`raw_grep_output` on
  every finding (`"field": false`), making the redaction guarantee machine-checkable.
  The CLI self-validates its checkpoint (stdlib) before writing and gained a
  cache-invalidation check (`checkpoint_is_valid`: reuse only at current HEAD, clean
  tree, matching ruleset). New `.github/workflows/scanner-selftest.yml` installs
  ripgrep, runs pytest, and validates the ruleset + a fixture scan against their schemas
  — the gate that makes external rule PRs safely mergeable. The PCRE compile check now
  keys on rg's exit code (catches PCRE2 errors the old substring check missed). (PR-06)

- **Skill rewrite** (`dsgai_scanner_tool.md`) — the skill is now a CLI-first
  orchestrator, not the engine. Adds a mandatory **Trust & Environment Preamble**
  (repo content is untrusted; scanner-directed instructions are recorded as a note and
  ignored — verified injection-immune on the deterministic path), a **Step 1.5**
  CLI-first flow with an in-context fallback and `engine:` header, the value-bearing
  **`rg -o --replace ''`** protocol (secret never leaves ripgrep), **STRICT-mode file
  IDs** (`F07:12`) with a gitignored `DSGAI-filemap.json`, an **evidence-citation**
  requirement (no status without rule IDs + locations), **timestamped reports** under
  `dsgai-reports/`, checkpoint cache-invalidation, and `compatible_cli` frontmatter.
  (PR-07)

- **Hardened GitHub Action** (`integrations/dsgai-scan.yml`): split into a **`scan`**
  job (deterministic CLI only — no secrets, no LLM, no egress; runs on fork PRs; emits
  SARIF + checkpoint) and an optional **`narrate`** job (Claude Code with a reduced
  toolset `Read,Write,Edit,Bash` — no WebFetch/WebSearch — rendering from the checkpoint;
  skipped on forks). Closes the exfiltration channel where untrusted PR content met an
  agent holding both secrets and egress. All actions pinned by full SHA; scanner fetched
  from a pinned upstream commit; SARIF uploaded via Code Scanning (guarded off forks).
  Fixed the push-gate bug — gating is now driven by the `DSGAI_FAIL_ON` repo variable
  (empty = report-only), not force-gated on every push. (PR-08)

### Changed
- Honest-language pass across the skill: every "safe to share/commit/store" replaced
  with "designed to minimize disclosure" + a residual-risk note. (PR-07)
- `DSGAI-samplereport.png` compressed from ~5.0 MB to ~0.35 MB (14×) as an interim fix;
  full regeneration from the fixture app lands in PR-09. (PR-02)

### Fixed
- _nothing yet_
