# DSGAI Scanner — licensing notes

> **⚠️ DRAFT — awaiting OWASP GenAI Data Security Initiative leadership sign-off.**
> This dual-licensing split touches the initiative's licensing posture and **must
> not be merged** without explicit sign-off. See "Maintainer checkpoint" below.

## Why a split?

CC BY-SA 4.0 is a **content** license. Creative Commons themselves advise against
using it for software, and its ShareAlike obligation trips corporate open-source
review, which would discourage adoption of the executable tooling. So the scanner
is dual-licensed by **kind of artifact**:

| Kind | License | What it covers |
|---|---|---|
| **Derived OWASP framework text** | **CC BY-SA 4.0** | Control descriptions, the README's framework content, report boilerplate describing the 21 risks, the changelog's framework prose. This is derived from the OWASP DSGAI 2026 framework and inherits its license and attribution. |
| **Original executable code** | **Apache-2.0** | `cli/`, `build/`, `tests/`, `scripts/`, `integrations/*.sh|*.yml|*.toml`, `schemas/`, `templates/`, `dist/`. Original work; permissive so it can be adopted and embedded freely. |

Full texts: [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt),
[`LICENSES/CC-BY-SA-4.0.txt`](LICENSES/CC-BY-SA-4.0.txt).

## Path → license map

| Path | License | SPDX header? |
|---|---|---|
| `cli/**/*.py` | Apache-2.0 | yes |
| `build/**/*.py` | Apache-2.0 | yes |
| `tests/**/*.py` | Apache-2.0 | yes |
| `scripts/**/*.py` | Apache-2.0 | yes |
| `integrations/*.sh` | Apache-2.0 | yes |
| `integrations/*.yml`, `integrations/gitleaks/*.toml` | Apache-2.0 | yes |
| `.github/workflows/scanner-*.yml` | Apache-2.0 | yes |
| `schemas/*.json`, `rules/*.schema.json`, `rules/dsgai-rules.json` | Apache-2.0 | JSON can't carry a comment; covered by this file |
| `templates/*` | Apache-2.0 | where the format allows |
| `dist/dsgai.semgrep.yaml` | Apache-2.0 | generated; covered by this file |
| `rules/atlas-map.yaml` | Apache-2.0 | yes |
| `dsgai_scanner_tool.md`, `dsgai_scanner_prompt.md` (framework prose) | CC BY-SA 4.0 | attribution preserved in-file |
| `README.md` (framework content) | CC BY-SA 4.0 | — |
| `CHANGES_v0.*.md`, `ROADMAP.md`, `CONTRIBUTING.md` | CC BY-SA 4.0 | — |

## Gray zone — `rules/dsgai-rules.yaml` (⚠️ name this explicitly to OWASP)

`rules/dsgai-rules.yaml` is genuinely ambiguous. Its **control mappings and mitigation
keywords derive from the CC BY-SA framework text**, while its **PCRE pattern
implementations are original code**. Apache-2.0 for the whole file is *arguable, not
obvious*. Two defensible options for leadership to choose:

1. **Whole file Apache-2.0** (treated as code), noting the framework-derived fields.
2. **YAML rules file CC BY-SA 4.0**; the generated `rules/dsgai-rules.json` + all other
   code Apache-2.0. *(This is the conservative fallback.)*

This file's licensing is the single decision that most needs an explicit call.

## Attribution (unchanged by this split)

Neither license removes attribution. The OWASP GenAI Data Security Initiative
attribution and the Emmanuel Guilherme Junior / Harish Ramachandran credits remain
intact wherever they currently appear.

## Maintainer checkpoint (blocking)

Confirm this split — **and specifically the `rules/dsgai-rules.yaml` decision above** —
with OWASP GenAI Data Security Initiative leadership before merging. Do not merge
without explicit sign-off.
