<!--
  OWASP GenAI Crosswalk
  File    : RATIONALE.md
  Purpose : Rationale behind all framework mappings — what was included, why, and how
  Version : 2026-Q1
  License : CC BY-SA 4.0
-->

# Mapping Rationale

This document explains the reasoning behind the OWASP GenAI Crosswalk: why each framework was selected, how the mappings were constructed, and the methodology that ties it all together.

---

## 1. The Problem This Solves

Organisations deploying GenAI (LLMs, agents, RAG pipelines) face a fragmented control landscape. No single document answered: **"Which controls from framework X address GenAI vulnerability Y?"** Security teams were left cross-referencing dozens of PDFs manually, often missing coverage gaps or duplicating effort across compliance programmes.

The Crosswalk provides a single, structured, machine-readable answer to that question — across 41 OWASP vulnerabilities and 20 industry frameworks.

---

## 2. Source Lists — What We Map From

The Crosswalk maps **from** three OWASP source lists that together cover the full GenAI attack surface:

| Source List | Entries | Scope | Why Included |
|---|---|---|---|
| **OWASP LLM Top 10 2025** | LLM01–LLM10 | Core LLM application risks (prompt injection, data leakage, supply chain, etc.) | The foundational OWASP list for LLM risks; widest industry adoption; the starting point for any GenAI security programme. |
| **OWASP Agentic Top 10 2026** | ASI01–ASI10 | Autonomous agent risks (goal hijack, tool misuse, privilege escalation, cascading failures, etc.) | Agents introduce qualitatively different risks — autonomy, tool access, multi-agent orchestration, persistent memory — that the LLM Top 10 was not designed to cover. |
| **OWASP GenAI Data Security 2026** | DSGAI01–DSGAI21 | Data lifecycle risks (training data poisoning, embedding leakage, model theft, PII in context, etc.) | Data is the through-line of every GenAI system. DSGAI covers the full data lifecycle from ingestion through training, inference, storage, and deletion — filling the gap between the application-level LLM/Agentic lists and data governance requirements. |

**Cross-references** link related entries across all three lists (e.g., LLM01 Prompt Injection ↔ ASI01 Agent Goal Hijack ↔ DSGAI01 Sensitive Data Leakage), so practitioners can trace a single risk across application, agent, and data dimensions.

---

## 3. Frameworks — What We Map To

### 3.1 Selection Criteria

Every framework was selected based on at least two of the following:

1. **Regulatory mandate** — Required by law or industry regulation (EU AI Act, DORA, PCI DSS, FedRAMP)
2. **Certification/audit requirement** — Used in formal audits or certifications (ISO 27001, ISO 42001, SOC 2, AIUC-1)
3. **Industry adoption** — Widely adopted as a voluntary best practice (NIST CSF, CIS Controls, OWASP ASVS)
4. **AI-specific coverage** — Purpose-built for AI or ML security (NIST AI RMF, MITRE ATLAS, MAESTRO, NIST SP 800-218A)
5. **Domain-specific necessity** — Required for specific deployment contexts (ISA/IEC 62443 and NIST SP 800-82 for OT/ICS; DORA for financial sector; NHI Top 10 for non-human identities)
6. **Practitioner demand** — Frequently requested by the OWASP GenAI community

### 3.2 Framework-by-Framework Rationale

#### Threat Modelling & Adversarial Taxonomy

| Framework | Why Included |
|---|---|
| **MITRE ATLAS** | The only structured adversarial technique taxonomy for ML/AI systems. Provides technique IDs (AML.T0051, etc.) that allow defenders to map vulnerabilities to specific adversarial TTPs. Essential for red teams and threat intel. |
| **STRIDE** | Classic Microsoft threat modelling methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege). Applied to LLM and agentic contexts so teams using STRIDE can incorporate GenAI threats into existing threat models without adopting a new framework. |
| **CWE/CVE** | Maps each OWASP entry to its root-cause weakness (CWE) and known confirmed vulnerabilities (CVE). Bridges GenAI risks to the traditional vulnerability management ecosystem — scanners, SIEM rules, and patch management workflows already speak CWE/CVE. |

#### AI Governance & Risk Management

| Framework | Why Included |
|---|---|
| **NIST AI RMF 1.0** | The US federal standard for AI risk management. Its GOVERN/MAP/MEASURE/MANAGE taxonomy structures AI risk from policy through technical controls. Required for US federal AI deployments; widely adopted by enterprises as voluntary best practice. |
| **ISO/IEC 42001:2023** | The first international AI management system standard. Provides certifiable requirements for AI governance, risk, and compliance. Increasingly required in procurement and regulatory contexts (EU AI Act references management system approaches). |
| **AIUC-1** | The first AI agent security, safety, and reliability certification standard. Six domains (Data & Privacy, Security, Safety, Reliability, Accountability, Society) directly address agentic risks that generic frameworks miss. |

#### Regulatory & Compliance

| Framework | Why Included |
|---|---|
| **EU AI Act** | Regulation (EU) 2024/1689 — the world's first comprehensive AI regulation. High-risk AI systems and GPAI models face binding obligations (Articles 6–72). The August 2026 enforcement deadline makes this the most urgent mapping for any EU-market deployment. |
| **DORA (EU 2022/2554)** | The Digital Operational Resilience Act applies to financial entities using AI. Adds ICT risk management, incident reporting, third-party oversight, and resilience testing obligations on top of general AI regulation. Included because financial services is one of the largest GenAI adoption sectors. |
| **FedRAMP** | Federal Risk and Authorization Management Programme. Any AI system operating in US government cloud environments must meet FedRAMP requirements. Maps GenAI risks to the FedRAMP security control baseline (derived from NIST SP 800-53). |
| **PCI DSS v4.0** | Payment Card Industry Data Security Standard. AI systems processing, storing, or transmitting cardholder data must comply. Maps GenAI risks to PCI DSS requirements for organisations deploying AI in payment and financial contexts. |

#### Information Security & Cybersecurity Foundations

| Framework | Why Included |
|---|---|
| **ISO/IEC 27001:2022** | The most widely certified information security standard globally. Maps GenAI risks to Annex A controls so organisations can extend their existing ISMS to cover AI deployments without building a parallel control framework. |
| **NIST CSF 2.0** | The Cybersecurity Framework's Identify/Protect/Detect/Respond/Recover + new Govern function. Provides a common language for cybersecurity risk that most US enterprises already use. GenAI mappings allow integration into existing CSF-based programmes. |
| **CIS Controls v8.1** | Prioritised, actionable security controls with Implementation Groups (IG1/IG2/IG3). Popular with mid-market organisations that need prescriptive guidance. Maps GenAI risks to specific CIS safeguards with IG-level implementation guidance. |
| **SOC 2 Trust Services Criteria** | Required for SaaS and cloud service providers. Maps GenAI risks to Trust Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy) so AI-powered SaaS companies can address GenAI risks within their existing SOC 2 audit scope. |

#### Application Security & Secure Development

| Framework | Why Included |
|---|---|
| **OWASP ASVS 4.0.3** | Application Security Verification Standard with three levels (L1/L2/L3). Maps GenAI risks to specific verification requirements so development teams can test for AI-specific vulnerabilities using the same ASVS methodology they use for traditional web apps. |
| **OWASP SAMM v2.0** | Software Assurance Maturity Model. Maps GenAI risks to maturity practices across Governance, Design, Implementation, Verification, and Operations. Helps organisations measure and improve their AI security programme maturity over time. |
| **NIST SP 800-218A** | Secure Software Development Framework extension for AI. Maps GenAI risks to AI-specific secure development practices (PW/PS/RV). The authoritative US guidance for secure AI SDLC — directly applicable to developer workflows. |

#### OT/ICS Security

| Framework | Why Included |
|---|---|
| **ISA/IEC 62443** | The international standard for industrial automation and control system security. Zone/conduit model, security levels, and foundational requirements (FR/SR). Included because AI is increasingly deployed in OT environments (predictive maintenance, autonomous control) where safety and availability outweigh confidentiality. |
| **NIST SP 800-82 Rev 3** | OT/ICS-specific guidance with SP 800-53 control mappings. Pairs with ISA/IEC 62443 to provide complete OT security coverage. Essential for organisations deploying AI in critical infrastructure. |

#### Architectural & Layered Models

| Framework | Why Included |
|---|---|
| **MAESTRO (CSA)** | Cloud Security Alliance's 7-layer agentic AI threat model. Maps threats to architectural layers (Foundation Models, Data Operations, Agent Frameworks, Tools, Deployment, Orchestration, Interaction). The only framework that provides layer-by-layer threat attribution — critical for understanding where in the stack a vulnerability originates, propagates, and impacts. |
| **ENISA Multilayer Framework** | EU Agency for Cybersecurity's multilayer AI cybersecurity framework (L1/L2/L3). Provides EU-aligned layered security guidance that complements the EU AI Act regulatory requirements with practical technical controls. |

#### Identity & Non-Human Entities

| Framework | Why Included |
|---|---|
| **OWASP NHI Top 10** | Non-Human Identities Top 10. Agents, service accounts, API keys, and machine identities are the dominant identity surface in agentic AI. This mapping addresses the unique risks of non-human identity management — credential sprawl, over-privileged service accounts, secret leakage — that traditional IAM frameworks underserve. |

#### Testing

| Framework | Why Included |
|---|---|
| **OWASP AI Testing Guide (AITG)** | Structured test cases mapped to each OWASP entry. Bridges the gap between "what to protect against" (the vulnerability) and "how to verify it" (the test procedure). |

---

## 4. Mapping Methodology

### 4.1 Unit of Mapping

Each mapping links **one OWASP vulnerability entry** to **one or more framework controls**. The grain is:

```
[Vulnerability ID] → [Framework] → [Control ID] + [Control Name] + [Tier] + [Scope] + [Notes]
```

Example: `LLM01 → NIST AI RMF 1.0 → GV-1.7 (Policies for trustworthy AI) / Foundational / Both`

### 4.2 How Mappings Were Constructed

1. **Vulnerability analysis** — Each OWASP entry was decomposed into its attack vectors, impacts, and required mitigations based on the official OWASP source list definitions.

2. **Control identification** — For each framework, controls were identified that directly address one or more of: the attack vector, the impact, or the required mitigation. The authoritative framework text (standard, regulation, specification) was the source — not secondary summaries.

3. **Relevance filtering** — Only controls with a clear, defensible connection to the vulnerability were included. "Tangentially related" controls were excluded to keep mappings actionable rather than exhaustive.

4. **Tier assignment** — Each control mapping was assigned an implementation tier:

   | Tier | Criteria | Typical Timeline |
   |---|---|---|
   | **Foundational** | Essential baseline — every deployment needs this regardless of maturity | Sprint 0–1 (immediate) |
   | **Hardening** | Defence-in-depth for mature security programmes | Quarter 1–2 |
   | **Advanced** | Cutting-edge, high-risk, or high-maturity environments only | Quarter 3+ |

   Tier assignment is based on: implementation complexity, dependency on other controls, cost, and how commonly the control is already present in production environments.

5. **Scope assignment** — Each mapping was tagged with deployment scope:

   | Scope | Meaning |
   |---|---|
   | **Buy** | Addressed by vendor/platform capability (e.g., cloud provider guardrails) |
   | **Build** | Requires internal engineering effort |
   | **Both** | Needs vendor capability AND internal implementation |

6. **Cross-referencing** — Each entry was linked to related entries in the other two source lists, enabling practitioners to trace risks across LLM application, agentic, and data security dimensions.

7. **Incident grounding** — Where available, real-world incidents (50 documented in the crosswalk) were linked to entries to validate that the vulnerability and mapped controls are not theoretical.

8. **Tool mapping** — Open-source and commercial tools (70+) were mapped to entries, providing practitioners with immediate actionable testing and mitigation options.

### 4.3 Severity Rating Methodology

Severity ratings follow the unified scale defined in `shared/SEVERITY.md`:

- **Base severity** — drawn directly from the OWASP source list definition or assessed using OWASP AIVSS methodology
- **Agentic amplifiers** — AIVSS adds ten agentic factors (autonomy level, tool access breadth, multi-agent orchestration, memory persistence, human oversight absence, OT/physical access) that can raise effective severity by 1–4 levels
- **No severity change without evidence** — ratings cannot be changed without citing an AIVSS score, a CVSS score from an associated CVE, or the OWASP source list definition

### 4.4 Quality Controls

- **Authoritative sources only** — mappings cite the actual framework text, not secondary interpretations
- **Schema validation** — all machine-readable entries (JSON) are validated against `data/schema.json` using `scripts/validate.js`
- **Source-of-truth model** — Markdown files are authoritative; JSON is derived via `scripts/generate.js`; both must stay in sync
- **Contribution review** — PRs require source/evidence links; severity changes require AIVSS/CVSS/OWASP citation
- **Consistent terminology** — all entries use the unified glossary (`shared/GLOSSARY.md`)

---

## 5. What Was Deliberately Excluded

| Exclusion | Reason |
|---|---|
| **Frameworks with no public specification** | Cannot be independently verified or contributed to |
| **Deprecated framework versions** | Mappings target current versions only (e.g., NIST CSF 2.0 not 1.1, PCI DSS 4.0 not 3.2.1) |
| **Tangential controls** | Controls only loosely related to a vulnerability were excluded to keep mappings actionable |
| **Vendor-specific implementation guides** | The crosswalk maps to framework controls, not to specific vendor products or configurations |
| **Risk ratings without evidence** | No severity or tier assignment was made without a defensible basis in the source material |

---

## 6. How to Read a Mapping Entry

Each mapping file follows the structure defined in `shared/TEMPLATE.md`:

1. **Header** — source list, framework, version, license
2. **Framework overview** — what the framework is and why it matters for this source list
3. **Quick-reference table** — one row per vulnerability with primary controls and tier
4. **Detailed mappings** (one section per vulnerability):
   - Severity rating
   - 2-sentence description
   - Real-world incident reference (where known)
   - Control mapping table (Control, ID, Description, Tier, Scope)
   - Mitigations by tier (Foundational → Hardening → Advanced)
   - Applicable tools
   - Cross-references to other source lists and frameworks
5. **Implementation priority table**
6. **References and changelog**

---

## 7. Design Decisions

### Why 20 frameworks and not fewer?

GenAI deployments span multiple compliance domains simultaneously. An AI chatbot processing payments in the EU must satisfy EU AI Act, PCI DSS, ISO 27001, and potentially DORA — all at once. Mapping to only "the top 5" frameworks would leave most practitioners with gaps. The 20-framework set covers the realistic compliance landscape.

### Why three source lists instead of one combined list?

LLM application risks, agentic risks, and data security risks are distinct problem domains with different audiences, threat models, and mitigations. A prompt injection attack on a chatbot (LLM01) is a fundamentally different problem from an agent's tool misuse (ASI05) or training data poisoning (DSGAI04). Keeping them separate preserves clarity; cross-references provide the linkage.

### Why the Foundational/Hardening/Advanced tier model?

Not every organisation can implement every control on day one. The tier model provides a **crawl → walk → run** implementation path that matches how security programmes mature in practice. It answers: "If I can only do three things this sprint, which three?"

### Why Buy/Build/Both scope tags?

Security teams need to know whether a control is something they configure in their vendor platform, something they build internally, or something that requires both. This distinction drives procurement decisions, staffing plans, and implementation timelines.

### Why machine-readable JSON alongside Markdown?

Markdown serves human readers. JSON serves automation — compliance report generation, GRC platform import (OSCAL), SIEM/SOAR integration (STIX 2.1), and programmatic querying. Both are necessary for the crosswalk to be useful across the full range of practitioner workflows.

---

## 8. Maintenance & Evolution

- New framework versions trigger mapping updates (tracked in changelogs at the bottom of each file)
- New OWASP source list entries trigger new mappings across all frameworks
- New real-world incidents are added to `data/incidents.json` and linked to affected entries
- Community contributions follow the process in `CONTRIBUTING.md`
- The crosswalk is versioned (`2026-Q1` currently) and published as an npm package for programmatic consumption

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) — maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
