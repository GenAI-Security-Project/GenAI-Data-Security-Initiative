# Changelog — DSGAI Scanner Tool v0.3

All notable changes for the v0.3 line. This file is appended by every merged PR.
v0.3 releases when Phases 0–2 of the improvement plan are complete.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) loosely;
dates are ISO-8601. The previous line is recorded in [`CHANGES_v0.2.md`](CHANGES_v0.2.md).

## [Unreleased]

### Added
- **Benchmark methodology + announcement drafts** (PR-16 hand-off). `docs/BENCHMARK.md`
  (corpus selection, deterministic run steps, a labeling-sheet template, a per-rule
  precision snippet, and the responsible-disclosure rule for live findings) and
  `docs/ANNOUNCEMENT-DRAFTS.md` (Slack / mailing-list / call-for-reports / lightning-talk).
  The benchmark **execution + labeling** and the `scanner-v0.4.0` release remain
  maintainer tasks.
- **Ecosystem expansion + rule-pack export** (PR-15).
  - **C# / Rust / Ruby**: detection signals (Semantic Kernel/Azure.AI.OpenAI, async-openai,
    ruby-openai); CVE manifest parsing for **NuGet** (`*.csproj`), **crates.io**
    (`Cargo.lock`), **RubyGems** (`Gemfile.lock`) via OSV; credential coverage extended to
    `*.cs`/`*.rs`/`*.rb`/`*.csproj` (13 DSGAI02/13 rules), with C#/Rust/Ruby fixture cases.
  - **`build/export_semgrep.py` → `dist/dsgai.semgrep.yaml`**: exports the 85 STRUCTURAL
    rules as a Semgrep pack (value-bearing excluded by design) so incumbent toolchains
    carry the DSGAI framework. Generated from the rules YAML; drift is a CI failure.
- **Templated report, single-sourced prompt variant, static ATLAS map** (PR-14).
  - `cli/dsgai_report.py` + `templates/report.css`: the HTML report is now rendered
    **by code** from the checkpoint (deterministic, testable), with a golden structural
    test. The LLM contributes only prose (executive summary / remediation) via `--prose`.
    STRICT mode renders file IDs (`F07:12`) and writes `DSGAI-filemap.json`;
    accessibility — every status carries a symbol + text label, not colour alone.
  - **Sample PNG regenerated** from the fixture app via the new renderer + headless
    Chrome (~45 KB, fully reproducible, zero real-repo disclosure).
  - `build/generate_prompt_variant.py`: `dsgai_scanner_prompt.md` is now generated from
    the skill (frontmatter + `cc-only` blocks stripped) — drift is a CI failure
    (`--check`), single-sourced so the two variants can't diverge.
  - `rules/atlas-map.yaml`: static MITRE ATLAS technique→control map; the skill's live
    `site:atlas.mitre.org` searches are removed in favour of it.
- **CVE pipeline, suppressions, baseline, incremental scanning** (PR-12).
  - CVE fetching moved into the CLI (`cli/dsgai_cve.py`, stdlib urllib): OSV
    `querybatch` is the per-version source, NVD enriches CVSS by `cveId` only (no
    `keywordSearch`). Cached at `~/.dsgai/cve-cache/` (24h TTL, `--refresh-cve`);
    online and offline runs are byte-identical. **The LLM never transcribes CVE data.**
  - Inline `# dsgai-ignore: P##.# reason="…"` suppressions — surfaced in a visible
    `suppressed` section, never silently dropped; a reason is required.
  - `baseline` subcommand + `--baseline` — gate only on findings not in the baseline.
  - `--diff <ref>` incremental scans (files changed vs a ref), labelled
    "INCREMENTAL — not a full assessment".
  - New `cve` subcommand; `--exclude`/`--diff`/`--baseline` wired through the skill and
    the Action (which now fetches `dsgai_cve.py`). CVE enrichment reaches CI Job 1 with
    no WebFetch. `langchain==0.1.0` yields real OSV advisories incl. EXPLOITABLE.
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

- **README truth pass**: reflects the deterministic-CLI + LLM-orchestration architecture,
  two engine modes, SARIF/Code Scanning, timestamped reports, file-ID strict mode, and
  a **Cost & runtime** section ($0 CLI-only mode, fork-PR behavior, `--diff` marked
  v0.4). Adds a Contributing quick-start ("found a wrong result? that's a contribution").
  Skill version badge → v0.3. (PR-09)

- **Pre-commit: gitleaks pack + portable fallback** (PR-10). New
  `integrations/gitleaks/dsgai.toml` — a gitleaks rule pack covering the DSGAI
  credential set (quote-optional named assignments + raw token prefixes: Slack `xoxb-`,
  GitHub `ghp_`/`github_pat_`, Google `AIza`, AWS `AKIA`, Anthropic/OpenAI project keys,
  JWT) with an allowlist for `tests/fixtures/**`, lockfiles, minified JS, and snapshots.
  `pre-commit-hook.md` now recommends gitleaks as primary. The bespoke
  `dsgai-secret-scan.sh` fallback is fixed for portability: `mapfile` → a bash-3.2-safe
  `while read -d ''` loop, `grep -zE` → a `case` filter, quote-optional pattern (catches
  the unquoted-`.env` miss), plus a token-prefix branch — shellcheck clean.

### Changed
- Honest-language pass across the skill **and README**: every "safe to share/commit/store"
  replaced with "designed to minimize disclosure" + a residual-risk note — the Phase-2
  overclaim gate now passes repo-wide. (PR-07, PR-09)
- Sample-report image caption now states it is interim and will be regenerated from the
  public fixture app once the deterministic report template lands (PR-14). (PR-09)
- `DSGAI-samplereport.png` compressed from ~5.0 MB to ~0.35 MB (14×) as an interim fix;
  full regeneration from the fixture app lands in PR-09. (PR-02)

### Fixed
- **Confirmed false negative** (unquoted `.env` key): P02.1–P02.5 and P13.4 are now
  quote-optional, and a new **P02.9** catches raw token literals (`sk-proj-`, `sk-ant-`,
  `ghp_`, `github_pat_`, `xox[baprs]-`, `AIza`, `AKIA`, JWT) assigned to *any* variable
  name. The fixture `.env` and the JS `xoxb-` token are now caught. (PR-11)
- **Confirmed false positive** (innocent webhook flagged as LLM SQL injection): **P12.1**
  rewritten to LLM-signal variable names and gated on an LLM call within 30 lines
  (`requires_nearby.pattern`, confidence `medium`). `webhook.py` no longer fires;
  `sql_agent.py` still does. Both Appendix A commands verified. The CLI gained
  `requires_nearby.pattern` support and a `drop` outcome for corroborating-signal rules.
  Zero `known_bug` markers remain in the answer sheet. (PR-11)
