# DSGAI Scanner v0.3 — announcement drafts

> **Hand-off: the agent drafts, the maintainer posts.** Review, adjust the links
> (fill the `<...>` placeholders), and post. All four items are optional but the
> "call for scan reports" doubles as contributor recruitment + the benchmark
> dataset.

## 1. OWASP GenAI Slack post

> 🛡️ **DSGAI Scanner v0.3 is out.** The OWASP DSGAI compliance scanner now has a
> **deterministic engine** — a stdlib Python CLI runs the 21-control ruleset via
> ripgrep and emits reproducible findings + SARIF (GitHub Code Scanning), while
> the Claude Code skill orchestrates and writes the report. Highlights: rules as
> data (107 patterns), a public vulnerable-fixture test corpus with CI, secrets
> that never leave ripgrep (structural redaction), a hardened two-job Action
> (safe on fork PRs), a gitleaks pre-commit pack, and a Semgrep export so your
> existing toolchain can carry the framework. **Found a wrong result? That's a
> contribution** — file an FP/FN issue and it becomes a permanent test case.
> Repo: <link to dsgai_scanner_tool/> · Release: <scanner-v0.3.0 link>

## 2. Initiative mailing list

> Subject: DSGAI Scanner v0.3 — deterministic engine, CI-gated, ecosystem support
>
> The DSGAI scanner reached v0.3. The headline change is architectural: pattern
> matching is now deterministic and reproducible (a compliance report that
> changes run-to-run is an opinion, not evidence), owned by a single-file
> stdlib CLI; the LLM's job is orchestration, judgment, and prose. We added a
> public test corpus + self-test CI (so external rule PRs are safe to merge),
> structural secret redaction, a hardened GitHub Action, a gitleaks pack, CVE
> enrichment with no hallucination risk, and C#/Rust/Ruby coverage plus a Semgrep
> export. Full changelog: <CHANGES_v0.3 link>. We'd love scan reports (below).

## 3. Call for scan reports (recruits contributors + builds the benchmark)

> **Run the DSGAI scanner on your GenAI repo and tell us what it got wrong.**
> `python cli/dsgai_scan.py scan .` ($0, no LLM) or the Claude Code skill. Every
> false-positive / false-negative you file with the
> [templates](<ISSUE_TEMPLATE link>) becomes a permanent, credited test case —
> and feeds the precision benchmark. Recurring contributors are invited as
> co-maintainers. No code required to help.

## 4. Lightning-talk abstract (AppSec Global / regional CFP, ~10 min)

> **Title:** A deterministic compliance scanner for GenAI apps — and why the LLM
> shouldn't do the matching
>
> **Abstract:** GenAI apps leak secrets, execute model-generated SQL, and skip
> tenant isolation in ways generic SAST misses. We built an OWASP DSGAI 2026
> compliance scanner and learned the hard way that letting an LLM do the pattern
> matching produces reports that change run-to-run. v0.3 splits the concern: a
> tiny deterministic engine owns matching (reproducible, redaction-guaranteed by
> construction — secrets never leave ripgrep); the model orchestrates and writes
> prose, always citing evidence. Live demo: we scan an intentionally-vulnerable
> fixture app, show the SARIF land in Code Scanning, and watch a prompt-injection
> file in the repo have exactly zero effect on the result. 10 minutes, one scan,
> a lot of opinions about trusting AI with security evidence.
