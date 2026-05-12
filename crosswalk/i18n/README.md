# Translations — i18n

This directory contains community-contributed translations of the
OWASP GenAI Crosswalk mapping files.

Translations make this security guidance accessible to practitioners
who work in languages other than English — expanding the reach of
OWASP GenAI security research to the global community.

---

## Available translations

| Language | Code | Status | Maintainer |
|---|---|---|---|
| Spanish | `es/` | ?? Planned — contributions welcome | Open |
| Portuguese | `pt/` | ?? Planned — contributions welcome | Open |

To add your language, see **Contributing a translation** below.

---

## Directory structure

Each language gets its own subdirectory using the ISO 639-1 two-letter
language code. The directory structure mirrors the root repository:
```
i18n/
+-- README.md               ? this file
+-- es/                     ? Spanish
¦   +-- README.md           ? Spanish repo overview
¦   +-- llm-top10/
¦   ¦   +-- LLM_NISTAIRMF.md
¦   ¦   +-- ...
¦   +-- agentic-top10/
¦   +-- dsgai-2026/
+-- pt/                     ? Portuguese
    +-- README.md
    +-- llm-top10/
    +-- agentic-top10/
    +-- dsgai-2026/
```

---

## Translation priorities

Not all files need to be translated simultaneously. Start with the
highest-impact files:

### Tier 1 — Translate first

| File | Reason |
|---|---|
| `llm-top10/LLM_NISTAIRMF.md` | Highest usage — US and global practitioners |
| `llm-top10/LLM_EUAIAct.md` | August 2026 deadline — EU practitioners need this |
| `agentic-top10/Agentic_EUAIAct.md` | Same — EU AI Act agentic compliance |
| `dsgai-2026/DSGAI_EUAIAct.md` | Same — EU AI Act data security compliance |

### Tier 2 — Translate next

| File | Reason |
|---|---|
| `llm-top10/LLM_ISO27001.md` | Globally certified standard — broadest applicability |
| `shared/RECIPES.md` | Implementation patterns — most actionable for engineers |
| `shared/TOOLS.md` | Tool catalogue — widely referenced |

### Tier 3 — Complete coverage

All remaining mapping files in `llm-top10/`, `agentic-top10/`,
`dsgai-2026/`, and `shared/`.

---

## Contributing a translation

### Step 1 — Check for existing work

Before starting, check open pull requests and issues for your language
to avoid duplicating effort.

### Step 2 — Create the directory structure
```
i18n/<lang-code>/
+-- README.md
+-- llm-top10/
+-- agentic-top10/
+-- dsgai-2026/
```

### Step 3 — Translation standards

- Translate all body text, headings, and table content
- **Do not translate** file names, control IDs (LLM01, ASI01, DSGAI01),
  framework names (ISO 27001, NIST AI RMF), or code blocks
- Preserve the original file's structure — heading levels, table format,
  section order
- In the translated file header comment, add:
```
  Translation: <Language> (<ISO 639-1 code>)
  Translated by: <Your name or handle>
  Source version: <date of original file you translated from>
```
- Add a note at the top of each translated file linking to the English
  original:
```markdown
  > **Note:** This is a community translation.
  > The authoritative English version is at
  > [`llm-top10/LLM_NISTAIRMF.md`](../../llm-top10/LLM_NISTAIRMF.md).
  > If there is any conflict between this translation and the English
  > original, the English version takes precedence.
```

### Step 4 — Open a pull request

- PR title: `i18n(<lang>): translate <filename>`
- PR body: list which files you translated and the source version date
- At least one native speaker review is strongly recommended before merge

### Step 5 — Maintenance

Translations may become outdated when the English source files are
updated. If you maintain a translation, watch this repository for
changes to files you have translated and open update PRs as needed.

---

## Language codes

Use ISO 639-1 two-letter codes for directory names:

| Language | Code |
|---|---|
| Spanish | `es` |
| Portuguese | `pt` |
| French | `fr` |
| German | `de` |
| Japanese | `ja` |
| Korean | `ko` |
| Chinese (Simplified) | `zh-hans` |
| Chinese (Traditional) | `zh-hant` |
| Italian | `it` |
| Dutch | `nl` |

To add a language not listed here, open an issue first to confirm
there is a maintainer committed to keeping the translation current.

---

## Questions

Open a GitHub issue with the label `i18n` for any questions about
translations or this directory.

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
