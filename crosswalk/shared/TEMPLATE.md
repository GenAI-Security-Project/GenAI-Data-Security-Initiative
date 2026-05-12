<!--
  OWASP GenAI Crosswalk
  Source list : [REPLACE: OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
               | OWASP Top 10 for Agentic AI Applications 2026 (ASI01-ASI10)
               | OWASP GenAI Data Security Risks 2026 (DSGAI01-DSGAI21)]
  Framework   : [REPLACE: Framework Name vX.Y]
  Version     : [REPLACE: YYYY-QN]
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# [Source List] × [Framework Name]

Mapping the [[Source List]]([source-list-url])
to the [[Framework Name]]([framework-url]) —
[one-sentence description of what the framework is and who uses it].

---

## Why [Framework] for [source list topic]

[2–4 paragraphs explaining why this framework is relevant for the source
list being mapped. Answer: who uses this framework? What decisions does
this mapping enable that no other existing mapping covers? What is unique
about the pairing?]

---

## [Framework] structure

[Table or list summarising the framework's components (clauses, domains,
controls, functions, layers) that are relevant to this mapping.]

| Component | Description | Relevance |
|---|---|---|
| [e.g., Domain A] | [What it covers] | [Why it matters for this source list] |

---

## Quick-reference summary

[One row per source list entry. Include: ID, Name, Severity, Primary framework
controls/sections, and Tier.]

| ID | Name | Severity | Primary [Framework] Controls | Tier |
|---|---|---|---|---|
| [e.g., LLM01] | [Name] | Critical/High/Medium/Low | [Controls] | Foundational–Advanced |

---

## Target audience

| Role | Sections to prioritise |
|---|---|
| [e.g., Security engineer] | [Sections] |
| [e.g., Compliance / GRC] | [Sections] |

---

## Detailed mappings

[One section per source list entry. Use the pattern below for each entry.]

---

### [ID] — [Entry Name]

[2–3 sentence description of the vulnerability/risk from the perspective of
this framework — what does the framework "see" when it looks at this risk?]

#### [Framework] mapping

| [Framework control/section] | [How it applies] | [Evidence/Mitigation] |
|---|---|---|
| [Control ID and name] | [Specific application to this risk] | [What to do] |

#### Three-tier mitigations

**Tier 1 — Immediate (pre-production gate):**
- [Actionable control — specific and implementable today]
- [Actionable control]

**Tier 2 — Short-term (first 30 days):**
- [Control requiring configuration or process change]
- [Control]

**Tier 3 — Strategic:**
- [Programme-level or architectural control]
- [Control]

#### Cross-references

- LLM Top 10: [LLMxx (Name)] / N/A
- Agentic: [ASIxx (Name)] / N/A
- DSGAI: [DSGAIxx (Name)] / N/A
- See also: [linked file(s)] — [what the link adds]

---

[Repeat the section above for each entry in the source list.]

---

## Implementation priority table

| Priority | [Framework] components | [Source list] entries addressed |
|---|---|---|
| P1 — Pre-production gate | [Controls] | [IDs] |
| P2 — First 30 days | [Controls] | [IDs] |
| P3 — 60-day milestone | [Controls] | [IDs] |
| P4 — Programme maturity | [Controls] | [IDs] |

---

## References

- [[Framework Name] official documentation]([url])
- [[Source list] — OWASP]([url])
- [Related mapping file(s) in this repo]
- [shared/RECIPES.md](../shared/RECIPES.md) — [relevant pattern name if applicable]

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | [YYYY-MM-DD] | Initial release — full mapping [IDs] to [Framework] |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
