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
A design pattern requiring human review and approval before an agent
executes high-impact or irreversible actions. A core mitigation for
ASI01, ASI09, and ASI10.

---

## I

**Indirect prompt injection**
A prompt injection attack where malicious instructions are embedded
in content the agent will process (documents, emails, web pages, RAG
results) rather than in direct user input. See ASI01, LLM01.

---

## L

**Least agency**
OWASP's agentic analog of least privilege. Agents should only have the
minimum autonomy required to perform safe, bounded tasks. Autonomy is
a feature that should be earned, not a default setting.

**Least privilege**
The security principle that any component should have access only to
the minimum resources and permissions required for its function.

---

## M

**MCP (Model Context Protocol)**
An open protocol for connecting AI agents to external tools, data
sources, and services at runtime. MCP servers are a supply chain
attack surface. See ASI04, DSGAI06.

**Memory poisoning**
See Data poisoning, specifically targeting agent persistent memory stores.
Unlike prompt injection, the effect persists across sessions. See ASI06.

**ML SBOM**
A Software Bill of Materials extended to cover machine learning
components: model weights, training data, libraries, adapters. See
CycloneDX ML SBOM framework mapping.

---

## N

**NHI (Non-Human Identity)**
A machine identity — API key, service token, certificate, agent session —
as distinct from a human user identity. Agents operate using NHIs.
NHI security is directly relevant to ASI03. See OWASP NHI Top 10.

---

## O

**OT (Operational Technology)**
Hardware and software that monitors or controls physical equipment,
assets, and processes in industrial environments. AI agents in OT
environments carry amplified severity ratings due to physical impact
potential.

---

## P

**Prompt injection**
An attack where malicious instructions embedded in input cause an LLM
or agent to behave in unintended ways. Direct (user input) or indirect
(processed content). See LLM01, ASI01.

---

## R

**RAG (Retrieval-Augmented Generation)**
An architecture where an LLM retrieves relevant content from an external
knowledge base at inference time to ground its responses. RAG introduces
data security surfaces including retrieval poisoning, over-permissive
retrieval, and vector store vulnerabilities. See DSGAI13, DSGAI17.

**Rogue agent**
An agent that appears compliant on the surface but pursues hidden goals,
has been compromised, or systematically deviates from its intended
purpose. See ASI10.

---

## S

**Shadow AI**
The use of unsanctioned AI tools or services by employees outside of
official governance and security controls. A significant ungoverned
data flow risk. See DSGAI03.

**SL (Security Level)**
ISA/IEC 62443 concept defining the required robustness of security
controls for an industrial zone or conduit. SL 1–4 from basic protection
to protection against state-sponsored attacks.

---

## T

**Tier**
See Foundational / Hardening / Advanced.

**Tool misuse**
An agent using legitimate tools in unsafe or unintended ways due to
prompt manipulation, misalignment, or compromised instructions. See ASI02.

**Trust boundary**
A logical perimeter within which data and identity claims are considered
trusted. Context windows, A2A communication channels, and RAG retrievals
all cross trust boundaries.

---

## V

**Vector store**
A database optimised for storing and querying embedding vectors,
used in RAG systems. Vector stores are a data security surface with
specific risks including retrieval poisoning and access control failures.
See DSGAI13.

---

## Z

**Zero trust**
A security model that requires continuous verification of every access
request regardless of network location or prior authentication.
Foundational architecture for securing multi-agent systems.

---

## Source list prefixes

| Prefix | Source list |
|---|---|
| `LLM01–LLM10` | OWASP Top 10 for LLM Applications 2025 |
| `ASI01–ASI10` | OWASP Top 10 for Agentic Applications 2026 |
| `DSGAI01–DSGAI21` | OWASP GenAI Data Security Risks & Mitigations 2026 |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk)*
