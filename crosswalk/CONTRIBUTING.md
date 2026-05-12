<!--
  OWASP GenAI Crosswalk
  File    : CONTRIBUTING.md
  Version : 2026-Q1
  License : CC BY-SA 4.0
-->

# Contributing

Thank you for helping make this resource better for the entire community.
This repo is maintained by the
[OWASP GenAI Data Security Initiative](https://genai.owasp.org) and
welcomes contributions from security engineers, framework experts,
researchers, and practitioners at any experience level.

---

## What you can contribute

- **New framework mappings** � a framework not yet covered
- **Control updates** � a framework has released a new version
- **Incident references** � a real-world incident that illustrates a vulnerability
- **Tool additions** � an open-source tool relevant to a mapping entry
- **OT/ICS specifics** � industrial context for any mapping entry
- **Translations** � see `/i18n/` for language stubs
- **Bug fixes** — broken links, incorrect control IDs, typos
- **Framework submissions** — use the [Submit-a-Standard](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/#/submit) page to submit a new framework for automated mapping

---

## Submit a Standard (automated)

The fastest way to add a new framework:

1. Go to [Submit-a-Standard](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/#/submit) in the web app
2. Paste your framework controls as JSON (see `data/framework-schema.json` for the schema)
3. The classifier pipeline automatically proposes mappings to all 41 OWASP entries
4. A PR is opened for review — use the [Review page](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/#/review) to accept/reject

You can also submit via the [GitHub Issue template](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/issues/new?template=submit-framework.yml).

---

## Before you start

1. Check [open issues](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/issues)
   � your contribution may already be in progress
2. For new framework files, open an issue first to confirm scope
3. Read [`shared/SEVERITY.md`](shared/SEVERITY.md) before assigning severity ratings
4. Read [`shared/GLOSSARY.md`](shared/GLOSSARY.md) for consistent terminology

---

## File template

Every mapping file must follow this structure:
```
1. Header comment block (source list, framework, version, license)
2. H1 title: "[Source list] � [Framework]"
3. One-paragraph description of the framework
4. Framework domain/control summary table
5. Quick-reference summary table (ID, Name, Severity, Controls, Tier, Scope)
6. Audience tags
7. Detailed mappings � one H3 section per vulnerability:
   - Severity
   - Description (2 sentences max)
   - Real-world reference (if known)
   - Framework control table (Control, ID, Description, Tier, Scope)
   - Mitigations by tier (Foundational / Hardening / Advanced)
   - Tools table (Name, Type, Link)
   - Cross-references (other source lists + other frameworks)
8. Implementation priority table
9. References
10. Changelog table
11. Footer link
```

Copy [`agentic-top10/Agentic_AIUC1.md`](agentic-top10/Agentic_AIUC1.md)
as your starting template � it is the reference implementation.

---

## Pull request process

1. Fork the repo
2. Create a branch: `git checkout -b feat/framework-name` or `fix/broken-link`
3. Make your changes following the file template
4. Verify all links work
5. Add a changelog entry at the bottom of any file you modify
6. Update `data/` JSON if you are modifying a mapping entry
7. Open a PR using the PR template � fill in every checklist item

PRs without a source/evidence link will be held for review until one is provided.

---

## Severity ratings

Do not change severity ratings without citing one of:
- An AIVSS score from [aivss.owasp.org](https://aivss.owasp.org)
- A CVSS score from an associated CVE
- The OWASP source list definition with a direct link

See [`shared/SEVERITY.md`](shared/SEVERITY.md) for full guidance.

---

## Data layer

If your contribution adds or changes a mapping entry, please also update
the corresponding JSON file in `/data/`. The schema is in
[`data/schema.json`](data/schema.json). This keeps the machine-readable
layer in sync with the markdown.

---

## Code of conduct

This project follows the
[OWASP Code of Conduct](https://owasp.org/www-policy/operational/code-of-conduct.html).
All contributors are expected to engage respectfully and constructively.

---

## Recognition

All contributors are credited in the repo
[contributors graph](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk/graphs/contributors)
and in release notes. Significant contributions will be highlighted in
the OWASP GenAI Data Security Initiative acknowledgements.

---

## Questions

Open a [GitHub Discussion](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk/discussions)
or reach out via the
[OWASP GenAI Security Project](https://genai.owasp.org/contact/).

---

*Thank you for contributing to open-source AI security.*
