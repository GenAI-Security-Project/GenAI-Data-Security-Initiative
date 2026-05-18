# DSGAI Scanner — v0.2 Release Notes

**Release date:** May 2026
**Previous version:** v0.1 (April 2026)

A complete revision driven by a hard audit of v0.1. Eleven defects fixed across correctness, completeness, security, and developer experience. Three new distribution surfaces added.

---

## 🔴 Critical fixes (v0.1 was broken)

### Install path now works
The v0.1 README told users to install `GenAIDataSecurity.md` and invoke `/GenAIDataSecurity`. The actual file was `dsgai_scanner_tool.md`, so the literal install commands failed. v0.2 aligns all install commands and invocations to the actual filename: `cp dsgai_scanner_tool.md ~/.claude/commands/` → `/dsgai_scanner_tool`.

### All 21 control scans now defined
v0.1 promised 21 controls and listed all 21 in the classification table, but only **15** had actual scan pattern blocks. The 6 silently missing scans were DSGAI08 (Regulatory Compliance), DSGAI09 (Multimodal), DSGAI10 (Synthetic Data), DSGAI16 (IDE Plugin), DSGAI17 (Resilience), DSGAI19 (Data Labeling).

v0.2 adds explicit pattern blocks for all 6, with classification, file scope, and pass/fail criteria.

---

## 🛡️ Privacy & obfuscation hardening

### Strict obfuscation by default + `--internal` flag
v0.1 stated "value-bearing matches must never appear in the report" but enforced this only at report-write time — the raw grep output (containing the actual secret) flowed through Claude's context and into the on-disk checkpoint. v0.2:

- Adds a mandatory **VALUE-BEARING SCAN PROTOCOL** (Steps V1–V6) that uses files-only search modes first, defers content search until after path triage, and explicitly forbids writing matched lines to any persistent tool call.
- Introduces **two obfuscation modes**:
  - 🛡️ **STRICT** (default, no flag): filename + line only (`config.py:12`), intermediate directories dropped, value-bearing match content never displayed. Safe to share with auditors, attach to tickets, commit to public repos.
  - 🔓 **INTERNAL** (`--internal` flag): full relative path restored for team-internal use; value-bearing content *still* never displayed.
- Adds a **defense-in-depth secret sweep** on every STRUCTURAL match — if the matched line accidentally contains a secret-pattern, it's redacted as if value-bearing.
- Pins the `DSGAI-scan.json` schema: forbids `match_text`, `raw_grep_output`, `content`, `value` fields; in STRICT mode omits `path_internal` entirely so the checkpoint itself is shareable.

### VENDOR ATTESTATION REQUIRED status
v0.1 had a `[BUY]` scope mechanism documented but no controls were actually tagged BUY, and the BUY-handling branch never fired. v0.2 introduces a new finding status — **VENDOR ATTESTATION REQUIRED** — for controls (or BUY-portions of BOTH-tagged controls) where the code scan cannot determine compliance. Each such finding emits a callout listing the specific attestations to request from the vendor (SOC 2 report, training data retention policy, abuse detection documentation, etc).

---

## 🔧 Correctness fixes

### Search patterns now portable PCRE
v0.1 patterns mixed `\s`, `{n,m}`, and other PCRE features with a `grep -rn` invocation that implied POSIX grep — patterns would silently fail on basic grep. v0.2:

- Explicitly documents the **PCRE prerequisite** at the top of Step 2
- Patterns rewritten and labeled `P##.#` for traceability
- Each scan block lists pattern, file scope, and classification separately — engine-agnostic

### Noisy patterns narrowed
Patterns that matched generic identifiers (`open(`, `query`, `search`, `generate`, `complete`, `.insert(`, `.update(`) and produced useless noise were narrowed to AI-specific contexts:
- DSGAI05 RAG ingestion: `(loader\.load\(|ingest_document\(|add_documents\(|PyPDFLoader|...)` instead of `open(`
- DSGAI11 vector queries: requires AI-namespace context (`similarity_search`, `as_retriever`)
- DSGAI12 DDL detection: excludes `(migrations|fixtures|tests)` paths from FAIL classification
- DSGAI18 LLM calls: scoped to known SDK invocation patterns
- DSGAI21 KB writes: requires vector-store-SDK proximity, not generic `.insert(`

### CVE enrichment fixed
- **NVD URL bug fixed:** v0.1 passed `cvssV3Severity=HIGH&cvssV3Severity=CRITICAL` — NVD honors only one. v0.2 issues two parallel calls per package.
- **GitHub Advisory URL fixed:** v0.1 fetched the unfiltered global feed (useless). v0.2 uses `?affects=<package>&ecosystem=<eco>`.
- **Go ecosystem added** to OSV queries (v0.1 listed Go as a target language but never queried `"ecosystem": "Go"`).
- **NVD rate-limit handling** documented, with `NVD_API_KEY` support.
- **GitHub `Authorization` header** documented for 5000 req/hour limit.
- **MITRE ATLAS split** from CVE sources — it documents attack techniques, not CVEs. Now renders in its own subsection of Section 1; not counted in Section 2 CVE totals.

### Report scaffolding fixed
- Duplicate item numbers (`4.` / `4.`, `11.` / `11.`) renumbered.
- Direct contradiction in Styling — v0.1 said both "always visible, no collapse JS" and "Interactive: collapsible finding cards (click to expand), filter buttons" — resolved: no collapse JS, no filter buttons, all cards always visible. Aligns with PDF-first design.
- **Windows `start DSGAI-report.html`** command added (v0.1 had only `open` / `xdg-open`).

### YAML frontmatter
v0.1 had none. v0.2 adds frontmatter with `description`, `argument-hint`, and `allowed-tools` so Claude Code can surface the skill correctly and lock down its tool access.

---

## 🚀 New distribution surfaces

### GitHub Action template
`integrations/dsgai-scan.yml` — runs the scan on every PR, uploads the report as an artifact, posts a PR comment summary with FAIL/WARN/PASS/CVE counts, and (optionally) fails the build on FAIL-class findings. Drop-in copy, supports `NVD_API_KEY` and `GITHUB_TOKEN` secrets for higher API rate limits.

### Pre-commit hook recipe
`integrations/pre-commit-hook.md` — sub-second pre-commit hook that runs only the DSGAI02 hardcoded-credential subset, blocking secret commits before they hit git history. Available in three flavors: pre-commit framework, plain git hook, Husky.

### Plain-prompt variant for non-Claude tools
`dsgai_scanner_prompt.md` — tool-neutral version stripped of Claude-Code-specific instructions (no Grep output modes, no parallel tool calls, no Write/Edit three-part protocol). Paste into Cursor, GitHub Copilot Chat, ChatGPT, or Gemini. Includes consolidated PCRE pattern bundle.

---

## 📊 What stayed the same

- All 21 control definitions, risk descriptions, mitigations — unchanged content
- BUILD / BUY / BOTH scope tagging philosophy
- Structural vs Value-Bearing classification system (now properly enforced)
- PDF-first HTML report design
- OWASP attribution and CC BY-SA 4.0 licensing
- Three-part Write/Edit protocol for context-safe report generation

---

## 🔄 Migration from v0.1

**For end users:**
1. Replace your existing `~/.claude/commands/dsgai_scanner_tool.md` with the v0.2 file.
2. Invocation is unchanged: `/dsgai_scanner_tool`. New flags: `--internal`, `--no-cve`.
3. Reports generated by v0.2 are STRICT-redacted by default. If you have a pipeline that expected full paths, add `--internal` or update the pipeline.

**For OWASP project maintainers:**
1. Commit v0.2 of all files to `dsgai_scanner_tool/`.
2. The `integrations/` directory is new — verify CI workflows reference the correct path.
3. The plain-prompt variant (`dsgai_scanner_prompt.md`) is a separate distribution artifact — link from the OWASP project page.

---

## Audit trail

Fixes in this release were derived from a hard audit identifying 11 defects across 4 severity tiers:

| Severity | Count | Examples |
|---|---|---|
| 🔴 Critical | 2 | Install path broken; 6 of 21 scans missing |
| 🟠 High | 5 | Styling contradiction; duplicate numbering; value-bearing leak risk; POSIX-incompatible patterns; noisy patterns |
| 🟡 Medium | 4 | CVE enrichment URL bugs; BUY scope dead code; Windows command gap; skill-vs-slash-command terminology |
| 🟢 Low | several | CVE freshness; sample image size; performance claim qualification |

All are addressed in v0.2. The Critical and High items are user-visible and were blocking the skill from working as documented.

---

## License

CC BY-SA 4.0. OWASP GenAI Data Security Initiative, led by Emmanuel Guilherme Junior. Skill adaptation by Harish Ramachandran. v0.2 revisions contributed via the [GenAI-Security-Project/GenAI-Data-Security-Initiative](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative) repo.
