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

### Changed
- `DSGAI-samplereport.png` compressed from ~5.0 MB to ~0.35 MB (14×) as an interim fix;
  full regeneration from the fixture app lands in PR-09. (PR-02)

### Fixed
- _nothing yet_
