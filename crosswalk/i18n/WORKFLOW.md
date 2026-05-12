<!--
  OWASP GenAI Crosswalk
  Document  : Translation Workflow
  Version   : 1.0.0 — 2026-03-27
  License   : CC BY-SA 4.0
-->

# Translation Workflow

Guidelines for translating OWASP GenAI Crosswalk mapping files into
languages other than English.

---

## Supported languages

| Code | Language   | Folder      | Status      |
|------|------------|-------------|-------------|
| `es` | Spanish    | `i18n/es/`  | Accepting PRs |
| `fr` | French     | `i18n/fr/`  | Accepting PRs |
| `pt` | Portuguese | `i18n/pt/`  | Accepting PRs |

To propose a new language, open an issue with the label `i18n` before
starting work.

---

## File naming convention

Translated files mirror the English filename with a language-code suffix
inserted before the extension:

```
English:    llm-top10/LLM_NISTAI.md
Spanish:    i18n/es/LLM_NISTAI.md
French:     i18n/fr/LLM_NISTAI.md
Portuguese: i18n/pt/LLM_NISTAI.md
```

Do not create sub-folders within a language folder. All translated files
for a given language live flat inside `i18n/<code>/`.

---

## Translation scope

### What to translate

- Prose paragraphs (descriptions, justifications, mitigations)
- Table cell content (except IDs and control codes — see below)
- Section headings and labels
- The Changelog `change` field

### What NOT to translate

| Item | Reason |
|---|---|
| Vulnerability IDs (`LLM01`, `ASI03`, `DSGAI09`) | Machine-readable keys |
| Framework control IDs (`AML.T0054`, `AC-3`, `6.1.2`) | Authoritative identifiers |
| URLs | Links must remain intact |
| Code blocks and `jq` / shell examples | Must remain runnable |
| HTML comment headers | Tooling parses these |
| The `<!--` / `-->` comment block at the top | License/metadata block |

---

## Contributor workflow

### Step 1 — claim a file

Open an issue or comment on an existing i18n issue to claim a file.
This prevents duplicate translation effort.

Label the issue: `i18n`, `lang:<code>` (e.g., `i18n`, `lang:es`).

### Step 2 — fork and branch

```bash
git checkout -b i18n/es/LLM_NISTAI
```

Use the naming pattern `i18n/<code>/<filename>` for your branch.

### Step 3 — translate

Copy the English source file into `i18n/<code>/` and translate it
following the scope rules above.

Add a translation notice at the top of the file, inside the HTML
comment block:

```html
<!--
  ...existing header fields...
  Translation : es — Spanish
  Translated by: <Your Name or GitHub handle>
  Source revision: <git SHA of the English file you translated>
-->
```

### Step 4 — add a sync note to the Changelog

At the bottom Changelog table, append a row:

```markdown
| 1.0.0-es | 2026-03-27 | Spanish translation — synced to English SHA abc1234 |
```

### Step 5 — open a PR

- Title: `[i18n][es] Translate LLM_NISTAI.md`
- Body: reference the claim issue; note the English SHA you translated from
- Label: `i18n`, `lang:es`
- Assign to: `@emmanuelgjr` for review

---

## Reviewer checklist

When reviewing a translation PR:

- [ ] File is in the correct `i18n/<code>/` folder
- [ ] Filename matches the English source exactly
- [ ] HTML comment header includes `Translation` and `Source revision` fields
- [ ] Vulnerability IDs and control IDs are unchanged
- [ ] All URLs are present and unmodified
- [ ] Changelog row added with correct English SHA
- [ ] No machine-translated content without human review notation
  (acceptable if the translator notes it; flag for native-speaker review)

---

## Keeping translations in sync

When the English source file is updated:

1. The maintainer adds the label `i18n-needs-update` to the relevant
   translated files via issue or PR comment.
2. The translation maintainer (if named) updates the translated file and
   bumps the `Source revision` SHA in the HTML comment.
3. If no one claims the update within 30 days, the file is marked
   `[OUTDATED]` in the first line of the file body (below the HTML
   comment) until a sync PR is merged.

---

## Machine translation policy

Machine-translated drafts are accepted **only** when:

1. The PR description clearly states "Machine-translated draft — needs
   native-speaker review."
2. A native speaker has reviewed or is listed as a requested reviewer.
3. The HTML comment includes `Translation-method: machine-assisted`.

PRs marked as machine-translated will not be merged until a fluent
reviewer approves the content.

---

## References

- [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/) —
  translations are derivative works and must carry the same license
- [shared/TEMPLATE.md](../shared/TEMPLATE.md) — English file template
- [GOVERNANCE.md](../GOVERNANCE.md) — maintainer roles and PR review SLOs

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial translation workflow document |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
