<!--
  GenAI Security Crosswalk — Shared Reference
  File    : shared/GLOSSARY.md
  Purpose : Unified terminology across all three source lists and all frameworks
  Version : 2026-Q1
  License : CC BY-SA 4.0
-->

# Glossary

Unified definitions used consistently across the LLM Top 10 2025,
Agentic Top 10 2026, and DSGAI 2026 mappings. Where a term is defined
differently across frameworks, we note the variance.

---

## A

**A2A (Agent-to-Agent communication)**
Direct communication between two autonomous AI agents, typically via a
protocol such as Google A2A or MCP. A2A channels are an attack surface
for spoofing, replay, and agent-in-the-middle attacks (ASI07).

**Agent**
An autonomous or semi-autonomous AI system that uses an LLM to perceive
its environment, plan, make decisions, and execute actions — often using
external tools, memory, and other agents. Distinct from a simple LLM
that only generates text responses.

**Agent Goal Hijack**
The redirection of an agent's objectives or decision logic by an attacker,
typically through prompt injection, poisoned content, or crafted tool
outputs. See ASI01.

**AIVSS (AI Vulnerability Scoring System)**
OWASP's scoring framework for AI vulnerabilities, extending CVSS v4.0
with ten agentic amplifier factors. Reference: https://aivss.owasp.org

**AIUC-1**
The world's first AI agent security, safety and reliability certification
standard. Covers six domains: Data & Privacy (A), Security (B), Safety (C),
Reliability (D), Accountability (E), Society (F).
Reference: https://www.aiuc-1.com

**Agentic supply chain**
The set of runtime components an agent depends on: tools, MCP servers,
prompt templates, model files, plugins, external agents. Unlike traditional
software supply chains, agentic supply chains are often loaded dynamically
at runtime. See ASI04.

---

## B

**Blast radius**
The scope of systems, data, and processes affected when a vulnerability
is exploited. In agentic AI, blast radius is amplified by autonomy,
tool access breadth, and multi-agent orchestration.

**Buy / Build / Both**
Scope annotation used in all mapping entries indicating whether a control
is addressed through vendor capability (Buy), internal engineering (Build),
or requires both.

---

## C

**Cascading failure**
A failure in one component that propagates through connected systems,
amplifying in scope. In multi-agent workflows, a single compromised agent
or poisoned memory entry can cascade across all downstream agents. See ASI08.

**Context window**
The combined input space visible to an LLM at inference time: system
prompt, user input, RAG results, tool outputs, conversation history.
Critically, the context window aggregates data from multiple trust domains
into a single flat namespace with no internal access control (DSGAI01).

**Crosswalk**
A mapping between two or more frameworks or taxonomies showing which
controls, clauses, or entries correspond. This repo is a crosswalk
between OWASP GenAI lists and industry security frameworks.

---

## D

**Data poisoning**
The injection of malicious, misleading, or corrupted data into training
datasets, RAG stores, or agent memory to alter model or agent behaviour.
See LLM04, ASI06, DSGAI04.

**DBoM (Dataset Bill of Materials)**
A structured inventory of all data used in training, fine-tuning, or
retrieval — including sources, lineage, and provenance. The data analog
of a Software Bill of Materials (SBOM).

**DSGAI**
OWASP GenAI Data Security Risks and Mitigations 2026. 21 entries
(DSGAI01–DSGAI21) covering the full GenAI data security lifecycle.
Reference: https://genai.owasp.org

---

## E

**Embedding**
A numerical vector representation of text, images, or other data,
used for semantic search and retrieval in RAG systems. Embeddings
are a data security surface — they can leak information about source
content and are vulnerable to inversion attacks. See LLM08, DSGAI13.

---

## F

**Foundational / Hardening / Advanced**
The three implementation tiers used in this repo, aligned to the DSGAI
2026 crawl-walk-run model. Foundational = basic hygiene every deployment
should have. Hardening = defence-in-depth for mature teams.
Advanced = cutting-edge for high-risk or high-maturity environments.

---

## G

**Goal hijack**
See Agent Goal Hijack.

**Guardrail**
A technical or procedural control that constrains agent or model
behaviour within defined safe boundaries. Guardrails operate independently
of the model's internal logic.

---

## H

**HITL (Human-in-the-Loop)**
Here's the build order that maximizes impact — based on search traffic, community need, and urgency.

Build sequence
Sprint 1 — Foundation (right now)
These files are referenced by everything else. Do them first.
OrderFileWhy first1shared/SEVERITY.mdEvery mapping file references it — severity definitions, AIVSS alignment2shared/GLOSSARY.mdUnified terms across LLM/ASI/DSGAI — stops contributor confusion3CONTRIBUTING.mdNeeded before anyone can fork and add to this4llm-top10/LLM_MITREATLAS.mdMost-used threat framework, highest search traffic
Sprint 2 — Highest traffic mappings
OrderFileWhy5agentic-top10/Agentic_MITREATLAS.mdCompletes the ATLAS pair6llm-top10/LLM_NISTAIRMF.mdMost required by enterprise/government7llm-top10/LLM_EUAIAct.mdAugust 2026 deadline — most urgent regulatory file8agentic-top10/Agentic_EUAIAct.mdAgents are explicitly in scope for EU AI Act
Sprint 3 — Data security core
OrderFileWhy9dsgai-2026/DSGAI_ISO27001.mdMost-certified standard globally10dsgai-2026/DSGAI_NISTAIRMF.mdUS federal alignment11dsgai-2026/DSGAI_EUAIAct.mdRegulatory trifecta complete
Sprint 4 — OT/ICS (your specialty)
OrderFileWhy12llm-top10/LLM_ISA62443.mdYour differentiator — nobody else has this done right13agentic-top10/Agentic_ISA62443.mdAgentic AI in OT is the frontier14llm-top10/LLM_NISTSP80082.mdPairs with 62443 for complete OT coverage
Sprint 5 — Fill out remaining frameworks
Everything else in alphabetical batches using the template.

Practical rhythm
Each session we do 2–3 files. I generate the full content, you paste into terminal, commit, push. Keeps momentum without burnout.
Today's session target: Sprint 1 files 1–3, then start file 4.
Ready — I'll generate shared/SEVERITY.md now:
powershell@'
<!--
  GenAI Security Crosswalk — Shared Reference
  File    : shared/SEVERITY.md
  Purpose : Severity definitions used consistently across all mapping files
  Version : 2026-Q1
  License : CC BY-SA 4.0
-->

# Severity definitions

All mapping files in this repo use a four-level severity scale aligned to
[OWASP AIVSS](https://aivss.owasp.org), CVSS v4.0, and OWASP GenAI project
definitions. Use this file as the single source of truth when rating or
reviewing any entry.

---

## Scale

| Level | Colour code | AIVSS / CVSS range | Definition |
|---|---|---|---|
| **Critical** | RED | 9.0 – 10.0 | Exploitation is trivial or already observed in the wild. Direct, immediate impact on confidentiality, integrity, or availability of systems or data. Autonomous agent blast radius means a single compromise can affect entire workflows or physical systems. Requires immediate remediation. |
| **High** | ORANGE | 7.0 – 8.9 | Exploitation is realistic with moderate attacker capability. Significant impact on one or more security properties. May require chaining with another vulnerability to reach full impact. Remediate within current sprint or release cycle. |
| **Medium** | YELLOW | 4.0 – 6.9 | Exploitation requires specific conditions or attacker access. Partial or indirect impact. Often a contributing factor in attack chains rather than a standalone exploit path. Plan remediation within the quarter. |
| **Low** | BLUE | 0.1 – 3.9 | Limited exploitability or impact in isolation. Typically informational, configuration, or defence-in-depth concern. Address in normal maintenance cycles. |

---

## AIVSS agentic amplifiers

The OWASP AI Vulnerability Scoring System adds ten agentic factors on top of
CVSS v4.0 base scores. These amplifiers raise effective severity when an
agentic system is in scope:

| Amplifier | Effect on severity |
|---|---|
| Autonomy level (high) | +1 to +2 severity steps |
| Tool access (broad) | +1 severity step |
| Multi-agent orchestration | +1 severity step |
| Memory persistence | +0.5 severity step |
| Human oversight (none) | +1 severity step |
| OT / physical system access | +2 severity steps |

**Example:** A Medium-rated prompt injection vulnerability (CVSS 5.5) in an
agent with high autonomy, broad tool access, and no human oversight can reach
an effective severity of Critical (9.0+) under AIVSS scoring.

---

## Severity in this repo

Every mapping entry carries:

- A **base severity** drawn from the OWASP source list definition
- An **agentic severity** where the vulnerability applies to agent contexts
- An **OT severity** where the vulnerability applies to OT/ICS environments

When these differ, all three are shown. When the source list does not define
severity explicitly, we apply AIVSS methodology and note the basis.

---

## Consistency rules for contributors

When submitting a new mapping or updating an existing one:

1. Do not change severity ratings without citing a source (AIVSS score,
   CVE CVSS score, or OWASP source list definition)
2. If a real-world incident changes the practical severity of an entry,
   add an incident reference and update with a changelog entry
3. OT severity must be assessed separately — do not assume IT severity
   translates directly to OT contexts
4. Agentic amplifiers must be noted explicitly when they affect the rating

---

## References

- [OWASP AIVSS](https://aivss.owasp.org)
- [CVSS v4.0 specification](https://www.first.org/cvss/v4-0/)
- [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk)*
