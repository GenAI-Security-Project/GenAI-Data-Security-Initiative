# Contributing to the DSGAI Scanner Tool

The DSGAI scanner is a Claude Code skill (plus a deterministic CLI, landing across
v0.3) that audits GenAI applications against the 21 [OWASP GenAI Data Security
controls](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/).
It gets more useful every time someone runs it on a real repo and tells us what it
got wrong. That is the single most valuable thing you can do here.

> This file covers the **scanner subproject** (`dsgai_scanner_tool/`). For the wider
> initiative, see the [repository-root CONTRIBUTING](../CONTRIBUTING.md).

## Fastest way to help

1. Run the scan on one of your own GenAI repos.
2. When it flags something wrong, or misses something real, open an issue with the
   [scanner templates](../.github/ISSUE_TEMPLATE/):
   - **[scanner] False positive** — it flagged safe code.
   - **[scanner] False negative** — it missed a real problem.
   - **[scanner] Propose a new rule** — a control needs coverage it doesn't have.
   - **[scanner] Bug** — anything else (rendering, CLI, CI, flags).

**Every accepted false-positive / false-negative report becomes a permanent test case
in the public fixture corpus, credited to you.** You don't have to write any code to
make the tool measurably better — a good repro is the contribution.

> Never paste real credentials into an issue or a fixture. Use obviously fake,
> canonical values (e.g. `sk-proj-FAKE00000000000000000000000000`).

## Contributing a rule

Detection rules are moving from prose in `dsgai_scanner_tool.md` into data at
`rules/dsgai-rules.yaml`, validated by `rules/rules.schema.json`. **(Landing soon —
tracked by PR-03.)** Until that lands, describe your rule in a
[new-rule issue](../.github/ISSUE_TEMPLATE/scanner-new-rule.yml) using the format below;
once the YAML rule format ships, this section will point at `rules/README.md`.

Every rule needs:

- **A control mapping** — one of `DSGAI01`–`DSGAI21`.
- **A PCRE pattern** — PCRE2 syntax, runs under `rg --pcre2`. Give it in a fenced code
  block, never a markdown table cell (`\|` becomes a literal pipe when the file is read
  back and silently breaks alternation).
- **A classification** (see below).
- **At least one positive and one negative test snippet.** No exceptions — a rule
  without a negative case has no defined precision.

### STRUCTURAL vs VALUE-BEARING

This classification controls *how* a rule executes and *what may appear in a report*.

| Class | The match is… | Report may show the matched line? | Execution |
|---|---|---|---|
| **STRUCTURAL** | a code shape — a call, a missing import, a missing decorator, an architectural gap. Contains no runtime secret. | Yes | normal `rg` match |
| **VALUE-BEARING ⚠️** | a line whose *content is* a credential, key, secret, connection string, or PII. | **Never** — not in the report, checkpoint, or any persisted tool call, even if the value looks fake. | location-only: `rg -n -o --replace '' --pcre2` so ripgrep erases the match before emitting `path:line:` |

The four VALUE-BEARING controls today are **DSGAI02, DSGAI13, DSGAI14, DSGAI15**. If
your rule matches lines that could contain secret material, it is VALUE-BEARING — when
in doubt, classify up.

### Running the self-test locally

Once the test infrastructure lands (PR-04/PR-05/PR-06):

```bash
pip install pyyaml pytest
pytest dsgai_scanner_tool/tests/ -q
```

The suite compiles every rule's PCRE, scans the fixture app, and checks the result
against `tests/expected-findings.yaml`. **Rule PRs are only safely reviewable once this
infrastructure exists** — if you draft a rule PR before then, that's welcome, just
expect it to sit until the fixtures land (see the `blocked-on-phase-1` label).

## Code contributions

- **Branch naming:** `improve/pr-NN-short-slug` for planned work, or a short descriptive
  slug otherwise. Never commit to `main`.
- **Conventional commits:** `fix:`, `feat:`, `docs:`, `ci:`, `test:`, `refactor:`.
- **Shell scripts** must be `shellcheck` clean and portable (bash 3.2 / macOS included —
  no `mapfile`, `readarray`, `${var,,}`, or GNU-only `grep` flags).
- **CI must be green** — the scanner has path-filtered lint and self-test workflows.

## What we will NOT merge

The scanner has deliberate limits that keep it maintainable and trustworthy. See the
[Non-goals section of the README](README.md#non-goals) — please read it before
proposing large additions, so your effort lands somewhere we can accept it.

## Recognition

Contributors are credited by handle in every release note. **Recurring contributors are
invited to become co-maintainers** — this project explicitly wants to grow its
maintainer base, and consistent, high-quality contributors are how that happens. If you
land a few accepted issues or PRs, expect an invitation.
