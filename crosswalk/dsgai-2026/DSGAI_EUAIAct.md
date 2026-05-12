<!--
  GenAI Security Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01–DSGAI21)
  Framework   : EU Artificial Intelligence Act (EU AI Act) — Regulation EU 2024/1689
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × EU AI Act

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [EU Artificial Intelligence Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
(Regulation EU 2024/1689).

The DSGAI risks describe the data security attack surface specific to
GenAI systems — where the EU AI Act creates direct binding obligations
that intersect. Unlike the LLM Top 10 EU AI Act mapping (which addresses
vulnerability-level obligations), this file maps data-lifecycle risks to
the specific articles governing data governance, privacy, robustness,
and operational security across the full GenAI data pipeline.

Key intersections: Article 10 (data governance) maps to the entire
DSGAI taxonomy. Article 15 (robustness and cybersecurity) maps to
integrity and pipeline risks. The GDPR runs in parallel for any DSGAI
entry involving personal data — both apply simultaneously.

---

## Compliance timeline reminder

| Date | Obligation relevant to DSGAI |
|---|---|
| August 2, 2025 | GPAI model obligations — technical documentation, copyright, security policy (Art. 53) |
| August 2, 2026 | **High-risk AI system obligations** — data governance (Art. 10), robustness (Art. 15), quality management (Art. 17) |
| Continuous | GDPR parallel obligations on all personal data in GenAI pipelines |

**August 2026 is 4 months away.** If your GenAI system is high-risk,
data governance and cybersecurity obligations under Art. 10 and Art. 15
apply in August. This file shows exactly which DSGAI risks map to those
obligations.

---

## Quick-reference summary

| ID | Name | Severity | Primary EU AI Act Articles | Applies to | Tier |
|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | Art. 10, Art. 15, Art. 53(1)(a) | High-risk · GPAI · GDPR | Foundational–Advanced |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Advanced |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | Art. 9, Art. 25, Art. 29 | All tiers | Foundational–Hardening |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | Art. 10, Art. 15, Art. 55(1)(b) | High-risk · GPAI systemic | Hardening–Advanced |
| DSGAI05 | Data Integrity & Validation Failures | High | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Hardening |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | Art. 9, Art. 25, Art. 53(1)(a) | High-risk · GPAI | Foundational–Hardening |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | Art. 10, Art. 17, Art. 53(1)(a) | High-risk · GPAI | Foundational–Advanced |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | Art. 9, Art. 17, Art. 72 | All tiers | Foundational–Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | Art. 10, Art. 15, Art. 53(1)(a) | High-risk · GPAI · GDPR | Hardening–Advanced |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | Art. 10, Art. 53(1)(a) · GDPR | High-risk · GPAI · GDPR | Hardening–Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | Art. 10, Art. 15, Art. 17 | High-risk · GPAI · GDPR | Foundational–Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Advanced |
| DSGAI13 | Vector Store Platform Security | High | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Hardening |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | Art. 10, Art. 17 · GDPR | High-risk · GPAI · GDPR | Foundational–Hardening |
| DSGAI15 | Over-Broad Context Windows | High | Art. 10, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Hardening |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | Art. 9, Art. 14, Art. 29 | High-risk · GPAI | Foundational–Hardening |
| DSGAI17 | Data Availability & Resilience Failures | High | Art. 15, Art. 17, Art. 5.30 | High-risk · GPAI | Foundational–Advanced |
| DSGAI18 | Inference & Data Reconstruction | High | Art. 10, Art. 15 · GDPR Art. 25 | High-risk · GPAI · GDPR | Hardening–Advanced |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | Art. 10, Art. 25 · GDPR Art. 28 | High-risk · GPAI · GDPR | Foundational–Hardening |
| DSGAI20 | Model Exfiltration & IP Replication | High | Art. 15, Art. 53(1)(a), Art. 17 | High-risk · GPAI | Hardening–Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | Art. 10, Art. 15, Art. 55(1)(a) | High-risk · GPAI systemic | Hardening–Advanced |

---

## Audience tags

- **CISO / governance** — full file, EU AI Act compliance for GenAI data security
- **DPO** — DSGAI01, DSGAI09, DSGAI10, DSGAI14, DSGAI18, DSGAI19 — GDPR intersection entries
- **Legal / compliance officer** — articles mapping, fines exposure, compliance checklist
- **ML / AI engineer** — Art. 10 data governance entries, Art. 15 robustness entries
- **Security engineer** — Art. 15 and Art. 17 entries
- **Auditor** — Art. 17 quality management, conformity assessment evidence requirements
- **OT engineer** — DSGAI04, DSGAI12, DSGAI17 critical infrastructure provisions

---

## Key articles reference

| Article | Title | DSGAI relevance |
|---|---|---|
| Art. 9 | Risk management system | Risk identification and mitigation for high-risk AI — all DSGAI entries |
| Art. 10 | Data and data governance | Training data quality, relevance, privacy — core to DSGAI01–DSGAI10, DSGAI18–DSGAI19 |
| Art. 13 | Transparency | Capabilities, limitations, and data handling disclosed to deployers and users |
| Art. 14 | Human oversight | Meaningful human oversight over high-risk AI outputs — DSGAI12, DSGAI16, DSGAI21 |
| Art. 15 | Accuracy, robustness, cybersecurity | Technical resilience — core to DSGAI04, DSGAI05, DSGAI12, DSGAI13, DSGAI17, DSGAI20 |
| Art. 17 | Quality management system | Documented procedures and post-market monitoring — all high-risk entries |
| Art. 25 | Value chain responsibilities | Provider and deployer obligations — DSGAI03, DSGAI06, DSGAI19 |
| Art. 29 | Deployer obligations | Human oversight and monitoring requirements — DSGAI03, DSGAI16 |
| Art. 50 | Transparency for certain AI systems | AI disclosure — DSGAI21 disinformation context |
| Art. 53 | GPAI model obligations | Technical documentation, copyright, security — DSGAI01, DSGAI04, DSGAI07, DSGAI09 |
| Art. 55 | Systemic risk GPAI obligations | Adversarial testing, incident reporting — DSGAI04, DSGAI21 |
| Art. 72 | Fines | Up to €35M or 7% global turnover |
| GDPR Art. 25 | Data protection by design | Privacy-by-design for all personal data in GenAI — DSGAI01, DSGAI09, DSGAI10, DSGAI18 |

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical
**Applies to:** High-risk · GPAI models · GDPR (where personal data)

Sensitive data leaks from GenAI systems through model outputs, RAG
retrieval, embedding exposure, or observability pipelines. This sits
at the intersection of the EU AI Act and GDPR — Art. 10 mandates data
governance for training data, Art. 15 mandates cybersecurity, and GDPR
Art. 25 mandates privacy by design, all simultaneously.

**GDPR intersection:** Any leakage involving personal data triggers GDPR
Art. 5 (data minimisation), Art. 25 (privacy by design), and Art. 32
(security of processing) in addition to EU AI Act obligations. Both can
be violated by a single incident.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training data must be relevant, representative, and subject to appropriate privacy measures | Data governance controls preventing sensitive data ingestion and memorisation are Art. 10 requirements |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI must be resilient and implement cybersecurity measures | Output scanning, DLP, and access controls on RAG retrieval are Art. 15 technical requirements |
| Art. 53(1)(a) — GPAI documentation | GPAI providers must maintain technical documentation including training data governance | Data governance for training data — sources, quality, privacy measures — is a GPAI documentation obligation |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 13 (all tiers): Disclose to deployers and users what data
  the system processes and what may appear in outputs — baseline
  transparency obligation regardless of risk tier
- GDPR Art. 25: Implement data protection by design — access
  controls on RAG retrieval, output redaction, and data
  minimisation are privacy-by-design requirements

**Hardening — high-risk AI systems (from Aug 2026)**
- Art. 10: Implement and document data governance for all training
  data — sources, quality controls, privacy measures, and bias
  mitigation — auditable evidence required for conformity assessment
- Art. 15: Implement and document technical cybersecurity measures —
  output scanning, DLP, access-controlled retrieval — as Art. 15
  robustness evidence
- Art. 17: Establish post-market monitoring for data leakage
  incidents — detection, logging, and response procedures documented

**Advanced — GPAI models (from Aug 2025)**
- Art. 53(1)(a): Maintain technical documentation on training
  data governance — available to the AI Office on request
- Implement machine unlearning readiness as Art. 10 data governance
  measure — versioned data-to-model linkage for erasure response
- GDPR Art. 25: Differential privacy in training documented
  as privacy-by-design technical measure

#### Fines exposure
Art. 10/15 violations for high-risk systems: up to **€15M or 3% global
turnover**. GDPR Art. 25 violations: up to **€20M or 4% global turnover**.
Both can apply to the same incident.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |
| Private AI | Commercial | https://private-ai.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 · ISO 27701 · NIST AI RMF GV-1.6

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical
**Applies to:** High-risk · GPAI models

AI agents inherit and cache credentials that, when compromised, expose
all systems the agent has access to. The EU AI Act addresses this through
risk management, cybersecurity, and quality management obligations — all
directly applicable to identity and access controls in agentic systems.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Credential exposure must be identified as a foreseeable risk and mitigated | Agent credential lifecycle included in Art. 9 risk management system |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures protecting against credential theft and misuse | Short-lived credentials, NHI inventory, and access controls are Art. 15 requirements |
| Art. 17 — Quality management | Documented procedures for credential management and incident response | Agent identity governance procedures documented in quality management system |

#### Compliance obligations by tier

**Foundational**
- Art. 9: Document agent credential exposure as a foreseeable
  risk in the risk management system — assign treatment controls
  and review cadence for each agentic deployment

**Hardening — high-risk AI systems**
- Art. 15: Implement and document technical credential
  security measures — short-lived tokens, NHI inventory,
  JIT access — as Art. 15 cybersecurity evidence
- Art. 17: Establish agent credential incident response
  procedures — rotation, containment, lateral movement
  assessment — documented in quality management system

**Advanced — GPAI models**
- Art. 53: Include agent identity architecture in GPAI
  technical documentation — how agents acquire, use, and
  expire credentials
- Art. 15: Implement PKI-backed agent identities as advanced
  Art. 15 cybersecurity measure — document as conformity
  assessment evidence

#### Fines exposure
Art. 15 cybersecurity violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Teleport | Open-source/Commercial | https://goteleport.com |
| SPIFFE / SPIRE | Open-source | https://spiffe.io |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.8.2/A.5.16 · OWASP NHI Top 10 · NIST AI RMF GV-1.6

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High
**Applies to:** All tiers — value chain obligations apply universally

Employees use unapproved GenAI SaaS tools, creating ungoverned data
flows outside formal security and procurement governance. The EU AI Act
distributes responsibility across the value chain — deployers cannot
waive their obligations by claiming ignorance of shadow AI usage within
their organisation.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Shadow AI usage is a foreseeable risk requiring mitigation in the risk management system | Ungoverned AI tool usage mapped and treated in Art. 9 risk assessment |
| Art. 25 — Value chain responsibilities | Organisations deploying AI are responsible for AI used within their operations | Shadow AI use by employees does not exempt the deployer from AI Act obligations triggered by that use |
| Art. 29 — Deployer obligations | Deployers must use AI systems as instructed and ensure appropriate oversight | Deployers have affirmative obligations to prevent and detect shadow AI usage |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 29: Deployers have affirmative obligations — cannot claim
  shadow AI is outside scope if employees use it in the course
  of their work on behalf of the organisation
- Art. 25: Understand your position in the AI value chain
  for all AI tools used within the organisation — approved
  and shadow alike

**Hardening — all deployers**
- Art. 9: Include shadow AI usage in your risk management
  system — assess what data flows exist, what obligations are
  triggered, and what controls are in place
- Art. 29: Implement monitoring and controls sufficient to
  detect shadow AI usage — acceptable use policy, DLP,
  endpoint controls — documented as Art. 29 deployer obligations

**Advanced**
- Art. 25: Integrate AI tool approval into procurement — all
  AI-capable tools assessed before adoption, not after
- Art. 29: Establish continuous shadow AI discovery and
  response capability — detected shadow AI triggers immediate
  data impact assessment and vendor data deletion request

#### Fines exposure
Art. 29 deployer obligation violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Zscaler (CASB) | Commercial | https://www.zscaler.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.10/A.5.23 · NIST AI RMF GV-1.7

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical
**Applies to:** High-risk · GPAI models · GPAI systemic risk

Adversaries corrupt training data, model weights, or supply chain
components. The EU AI Act directly mandates data governance, adversarial
testing, and incident reporting — all directly applicable to poisoning
prevention, detection, and response.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training data must be subject to governance practices — relevant, representative, free of errors | Data quality controls and provenance requirements preventing poisoning are binding Art. 10 obligations |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI must be resilient to attempts to alter performance through data manipulation | Technical robustness against poisoning is a binding Art. 15 requirement with conformity assessment evidence |
| Art. 55(1)(b) — Systemic risk GPAI adversarial testing | Systemic risk GPAI providers must conduct adversarial testing to identify and mitigate systemic risks | Poisoning detection adversarial testing is a binding obligation for systemic risk models |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Establish data governance policy for all training
  data — source validation, quality assessment, and lineage
  documentation are baseline Art. 10 requirements for high-risk
- Document data poisoning as a foreseeable risk in Art. 9
  risk management system with treatment controls assigned

**Hardening — high-risk AI systems**
- Art. 10: Implement technical data quality controls —
  anomaly detection, source allowlisting, lineage tracking —
  documented as Art. 10 compliance evidence for conformity
  assessment
- Art. 15: Implement adversarial robustness against training
  data manipulation — backdoor detection, differential privacy,
  model rollback — documented as Art. 15 technical measures
- Art. 17: Establish model rollback procedures in quality
  management system — tested and documented

**Advanced — systemic risk GPAI models**
- Art. 55(1)(b): Conduct and document adversarial testing
  covering poisoning attack scenarios — results available
  to AI Office on request
- Art. 55: Implement incident reporting for serious poisoning
  incidents — notify AI Office without undue delay
- Art. 10: Apply differential privacy in training as a
  documented data governance measure

#### Fines exposure
Art. 10 data governance violations: up to **€15M or 3% global turnover**.
Art. 55 systemic risk violations: up to **€35M or 7% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI04 Supply Chain, ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.27/A.8.29 · NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High
**Applies to:** High-risk · GPAI models

Adversarially crafted payloads passing syntactic validation corrupt
training sets or exploit snapshot import path traversal. The EU AI Act
requires robustness and quality management covering all data ingestion
interfaces.

**Real-world references:**
- CVE-2024-3584 (Qdrant) — path traversal via poisoned snapshot
  import achieved arbitrary file write on vector DB host

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Ingestion integrity risks identified and mitigated | Data ingestion attack surfaces included in Art. 9 risk management |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI resilient against adversarial input manipulation | Secure ingestion interfaces and path traversal prevention are Art. 15 requirements |
| Art. 17 — Quality management | Documented procedures for data ingestion and pipeline integrity | Ingestion validation procedures and CVE patching documented in quality management |

#### Compliance obligations by tier

**Foundational**
- Art. 9: Document ingestion integrity risks in risk management
  system — identify which endpoints accept external data,
  rate by exposure and impact
- Patch CVE-2024-3584 and equivalent vector database
  vulnerabilities — treat as Art. 15 cybersecurity requirement

**Hardening — high-risk AI systems**
- Art. 15: Implement and document technical ingestion security —
  schema and semantic validation, path traversal prevention,
  snapshot import hardening — as Art. 15 conformity evidence
- Art. 17: Include ingestion security testing in quality
  management — fuzz testing schedule, CVE patching cadence,
  anomaly detection coverage documented

**Advanced**
- Art. 15: Conduct adversarial ingestion testing as standard
  pre-deployment gate — results documented as Art. 15 evidence
- Sandbox all snapshot import operations — document as
  Art. 15 cybersecurity measure in conformity assessment

#### Fines exposure
Art. 15 violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| Pandera | Open-source | https://pandera.readthedocs.io |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28 · NIST AI RMF MS-3.3 · CWE-20

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange Risks

**Severity:** High
**Applies to:** High-risk · GPAI models

AI tools, plugins, and MCP servers receive full context payloads with
no data minimisation. The EU AI Act addresses this through value chain
responsibility obligations — providers must document what deployers
inherit, and deployers must verify.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Third-party tool data exchange risks identified and mitigated | All tool integrations assessed in Art. 9 risk management |
| Art. 25 — Value chain responsibilities | Providers document obligations flowing to deployers; deployers verify | Tool data exchange obligations explicitly distributed along the value chain |
| Art. 53(1)(a) — GPAI documentation | GPAI providers document all third-party integrations | Tool and plugin data exchange documented in GPAI technical documentation |

#### Compliance obligations by tier

**Foundational**
- Art. 25: Understand and document your position in the AI
  value chain for all tool integrations — what obligations
  you hold as provider vs deployer
- Implement data minimisation for tool payloads — tools
  receive only minimum context required for their function

**Hardening — high-risk AI systems**
- Art. 9: Include all tool integrations in risk management
  system — data exchanged, retention, training use, and
  sub-processor chain per integration
- Art. 25: Document tool provider obligations in contractual
  arrangements — what the deployer inherits and must verify
- Art. 17: Establish tool provider security assessment process
  in quality management — annual review cadence

**Advanced — GPAI models**
- Art. 53(1)(a): Document all tool integrations in GPAI
  technical documentation — available to AI Office on request
- Implement contractual right-to-audit for all strategic
  tool providers as Art. 25 value chain control

#### Fines exposure
Art. 25 value chain violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · NIST AI RMF MP-5.1

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High
**Applies to:** High-risk · GPAI models

GenAI creates derived data assets outside traditional governance —
embeddings, summaries, agent traces — with no automatic propagation
of classification labels, retention policies, or erasure obligations.
The EU AI Act makes data governance a binding legal requirement for
high-risk systems and GPAI models, not a best practice.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | High-risk AI training data subject to governance — relevant, representative, privacy-preserving | Data governance policy covering the full AI data lifecycle is an Art. 10 compliance requirement |
| Art. 17 — Quality management | Documented quality management system including data handling procedures | Data lifecycle procedures — classification, retention, deletion — documented in quality management |
| Art. 53(1)(a) — GPAI documentation | GPAI providers maintain technical documentation including training data governance | Full data governance documentation for GPAI training data is a binding Art. 53 obligation |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Extend data governance to all GenAI data assets —
  training corpora, embedding stores, RAG indexes, agent memory,
  observability logs — classification and retention for all

**Hardening — high-risk AI systems**
- Art. 10: Document and implement data governance procedures
  covering the full GenAI lifecycle — classification propagation,
  retention schedules, deletion workflows — as Art. 10 conformity
  evidence
- Art. 17: Include data lifecycle procedures in quality management
  system — auditable evidence of classification propagation,
  retention compliance, and deletion completion

**Advanced — GPAI models**
- Art. 53(1)(a): Maintain comprehensive training data governance
  documentation — all sources, quality assessments, privacy
  measures, and provenance documented and available to AI Office
- Implement machine unlearning readiness as Art. 10 data
  governance measure — erasure obligations enforceable across
  the full derived asset chain

#### Fines exposure
Art. 10 violations: up to **€15M or 3% global turnover**.
Art. 53 GPAI documentation violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| OpenMetadata | Open-source | https://open-metadata.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · NIST AI RMF GV-1.6 · ISO 27701

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High
**Applies to:** All tiers — directly addresses the EU AI Act itself

Non-compliance with the EU AI Act is itself the risk this entry
addresses. The most common paths to violation: deploying a high-risk
AI system without a conformity assessment, training on personal data
without lawful basis, and failing to implement the human oversight
required by Art. 14. This entry maps compliance failures to their
specific articles and fine exposure.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Mandatory risk management system for high-risk AI | Absence of a documented risk management system is an Art. 9 violation |
| Art. 17 — Quality management | Documented quality management system including post-market monitoring | Absence of a quality management system is an Art. 17 violation |
| Art. 72 — Fines | Graduated fines based on violation type | Understanding fine exposure is the starting point for compliance prioritisation |

#### Compliance obligations by tier — fine exposure map

**Prohibited AI (Art. 5)** — maximum fines:
- Violation of prohibited practice ban (Art. 5): up to
  **€35M or 7% global turnover** — highest tier
- Examples: social scoring systems, real-time biometric
  surveillance in public, subliminal manipulation

**High-risk AI violations (Art. 9–17)** — second tier:
- Art. 10 data governance violations: **€15M or 3%**
- Art. 13 transparency violations: **€15M or 3%**
- Art. 14 human oversight violations: **€15M or 3%**
- Art. 15 robustness/cybersecurity violations: **€15M or 3%**
- Art. 17 quality management violations: **€15M or 3%**

**GPAI model violations (Art. 53–55)** — second tier:
- Art. 53 documentation violations: **€15M or 3%**
- Art. 55 systemic risk obligation violations: **€35M or 7%**

**Incorrect information to authorities** — third tier:
- Art. 72(3): up to **€7.5M or 1.5% global turnover**

#### Compliance readiness by tier

**Immediate — already required**
- Determine if any of your AI systems qualify as GPAI models
  under Art. 51 — GPAI obligations apply from Aug 2025
- If GPAI: publish technical documentation, copyright policy,
  and implement information security policy (Art. 53)
- All chatbot deployments: implement AI disclosure (Art. 50)

**Urgent — August 2026**
- Classify all AI systems against Annex III high-risk categories
- Complete conformity assessment for any high-risk system
- Implement Art. 9 risk management, Art. 10 data governance,
  Art. 14 human oversight, Art. 15 cybersecurity, Art. 17
  quality management for all high-risk deployments
- Sign EU Declaration of Conformity and apply CE marking

**Ongoing**
- Post-market monitoring under Art. 17
- Incident reporting to national authorities
- Annual review of risk classification as system evolves

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| EU AI Office guidance | Reference | https://digital-strategy.ec.europa.eu/en/policies/ai-office |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.5.31 · ISO 42001 · NIST AI RMF GV-4.2

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High
**Applies to:** High-risk · GPAI models · GDPR (special category data)

Multimodal AI systems process passport photos, medical images, voice
recordings, and biometric data — Art. 10 requires data governance
covering all input modalities, and GDPR Article 9 imposes heightened
obligations on special category data processed in multimodal pipelines.

**GDPR Art. 9 intersection:** Images of documents containing biometric
or health data, transcriptions of medical consultations, and other
special category data processed by multimodal AI systems require
explicit consent or another Art. 9 lawful basis — distinct from the
general lawful basis for standard personal data.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Data governance covers all input modalities — images, audio, video — not only text | Multimodal input governance is an Art. 10 requirement for high-risk systems processing such inputs |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures covering all data channels including multimodal inputs | DLP and access controls on multimodal pipelines are Art. 15 requirements |
| Art. 53(1)(a) — GPAI documentation | Technical documentation covers all input modalities processed by the model | Multimodal data governance documented in GPAI technical documentation |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Extend data governance to all input modalities —
  classification and handling requirements for images, audio,
  and video equal to text inputs
- GDPR Art. 9: Identify all special category data processed
  by multimodal systems — establish lawful basis for each
  category before deployment

**Hardening — high-risk AI systems**
- Art. 10: Implement and document multimodal data governance —
  classification propagation from source modality to all
  derived forms (OCR output, transcripts, embeddings) — as
  Art. 10 conformity evidence
- Art. 15: Implement DLP and redaction on multimodal extraction
  pipelines — documented as Art. 15 cybersecurity measure

**Advanced — GPAI models**
- Art. 53(1)(a): Document multimodal data governance in GPAI
  technical documentation — available to AI Office on request
- GDPR Art. 25: Implement data protection by design for
  multimodal pipelines — PII detection on extracted content,
  automated deletion after purpose served

#### Fines exposure
Art. 10 violations: up to **€15M or 3% global turnover**.
GDPR Art. 9 violations: up to **€20M or 4% global turnover**.

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11/A.8.12 · ISO 27701 · GDPR Art. 9

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium
**Applies to:** High-risk · GPAI models · GDPR

Synthetic data and anonymisation techniques are used to satisfy privacy
requirements — but the EU AI Act requires that training data governance
ensures data is "free from errors" and that privacy measures are
effective, not merely claimed.

**GDPR intersection:** Anonymisation under GDPR requires data to be
irreversibly de-identified. If synthetic data can be re-identified,
it was never anonymous under GDPR — the original personal data
obligations continue to apply.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training data must be subject to appropriate data governance — privacy measures must be effective | Anonymisation effectiveness is an Art. 10 data governance requirement, not a self-certification |
| Art. 53(1)(a) — GPAI documentation | GPAI training data governance documented — privacy measures included | Synthetic data generation methodology and re-identification risk assessment documented for GPAI |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Treat anonymisation as an Art. 10 data governance
  requirement — effectiveness must be demonstrated, not assumed
- GDPR Recital 26: Verify that anonymisation meets the legal
  standard of irreversibility — technical anonymisation may
  not satisfy the GDPR standard

**Hardening — high-risk AI systems**
- Art. 10: Document anonymisation methodology and quality
  controls — re-identification risk assessment included in
  Art. 10 conformity evidence
- Conduct formal re-identification risk testing before
  using synthetic datasets in production training

**Advanced — GPAI models**
- Art. 53(1)(a): Include synthetic data governance in GPAI
  technical documentation — generation methodology, quality
  thresholds, re-identification risk assessment
- Apply differential privacy with documented privacy budget —
  demonstrate Art. 10 compliance against a measurable standard

#### Fines exposure
Art. 10 violations: up to **€15M or 3% global turnover**.
GDPR violations from failed anonymisation: up to **€20M or 4%**.

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Reconstruction
- Other frameworks: ISO 27001 A.5.34/A.8.11 · ISO 27701 · GDPR Recital 26

---

### DSGAI11 — Cross-Context & Multi-User Conversation Bleed

**Severity:** High
**Applies to:** High-risk · GPAI models · GDPR

Session isolation failures allow one user's context to leak into
another's responses. This is both an Art. 15 cybersecurity failure
and a GDPR Art. 32 security of processing failure when personal
data is involved.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Data governance covering multi-tenant deployments — session isolation as a data handling requirement | Session isolation controls are an Art. 10 data governance obligation for multi-user deployments |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures preventing cross-session data exposure | Session isolation and tenant separation are Art. 15 technical requirements |
| Art. 17 — Quality management | Post-market monitoring detecting and responding to session bleed incidents | Cross-session leakage detection in post-market monitoring programme |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Implement strict session isolation as an Art. 10
  data handling requirement — one user's context cannot
  be retrieved by any other user in the same deployment
- GDPR Art. 32: Implement appropriate technical measures
  ensuring security of processing — session isolation is
  a GDPR security of processing requirement for any
  personal data in multi-user deployments

**Hardening — high-risk AI systems**
- Art. 15: Implement and document session isolation controls —
  per-user RAG namespaces, KV cache isolation, conversation
  history access controls — as Art. 15 cybersecurity evidence
- Art. 17: Include session isolation testing in post-market
  monitoring — cross-tenant access scenarios tested on each
  significant deployment change

**Advanced**
- Art. 15: Conduct adversarial cross-tenant testing as standard
  security evaluation — document results as Art. 15 conformity
  evidence
- GDPR Art. 32: Implement cryptographic session isolation for
  highest-risk tenants — per-tenant encryption keys as
  additional security of processing measure

#### Fines exposure
Art. 15 violations: up to **€15M or 3% global turnover**.
GDPR Art. 32 violations: up to **€20M or 4% global turnover**.

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · NIST AI RMF MS-2.5 · GDPR Art. 32

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical
**Applies to:** High-risk · GPAI models

LLM-to-SQL and LLM-to-Graph interfaces collapse the security boundary
between user input and database logic. The EU AI Act's human oversight
(Art. 14) and cybersecurity (Art. 15) obligations are directly applicable
— LLM-generated destructive queries executing autonomously are an Art. 14
human oversight failure and an Art. 15 cybersecurity failure simultaneously.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | LLM gateway risks identified and mitigated | All LLM-to-database interfaces mapped in Art. 9 risk management |
| Art. 14 — Human oversight | High-risk AI designed to allow effective human oversight — ability to pause, stop, and override | LLM-generated destructive database queries executing autonomously are an Art. 14 human oversight failure |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures protecting against adversarial misuse | Least-privilege execution, query allowlisting, and SQL injection prevention are Art. 15 requirements |
| Art. 17 — Quality management | Documented procedures for LLM gateway security | Security testing procedures and query log retention documented in quality management |

#### Compliance obligations by tier

**Foundational**
- Art. 9: Map all LLM-to-database interfaces in risk management
  system — privilege level, query scope, and data exposure
  per interface documented
- Art. 14: Implement human oversight controls for LLM gateway —
  destructive operations (DELETE, DROP, bulk INSERT) require
  human approval before execution

**Hardening — high-risk AI systems**
- Art. 15: Implement and document technical LLM gateway
  security — least-privilege execution, read-only defaults,
  query allowlisting — as Art. 15 cybersecurity evidence
- Art. 14: Document human oversight mechanisms for LLM
  gateway — what requires approval, who approves, how
  overrides are logged — required for conformity assessment
- Art. 17: Include LLM gateway security testing in quality
  management — SQL injection, privilege escalation, bulk
  extraction scenarios on schedule

**Advanced**
- Art. 15: Deploy query analysis layer as advanced Art. 15
  cybersecurity measure — document as conformity evidence
- Art. 14: Implement automated human-in-the-loop triggers
  for high-risk query patterns — document as Art. 14
  human oversight mechanism

#### Fines exposure
Art. 14 human oversight violations: up to **€15M or 3% global turnover**.
Art. 15 cybersecurity violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Semgrep | Open-source | https://semgrep.dev |
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Immuta | Commercial | https://www.immuta.com |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · NIST AI RMF MS-2.5 · CWE-89

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High
**Applies to:** High-risk · GPAI models

Vector databases store sensitive embeddings with weaker default security
posture than traditional databases. The EU AI Act requires cybersecurity
measures for high-risk AI infrastructure — vector stores are in scope
as components of the AI system.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Vector store security risks identified and mitigated | All vector store deployments assessed in Art. 9 risk management |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI infrastructure protected against cybersecurity risks | RBAC, encryption, and CVE patching for vector stores are Art. 15 requirements |
| Art. 17 — Quality management | Post-market monitoring covering AI infrastructure components | Vector store security monitoring in post-market monitoring programme |

#### Compliance obligations by tier

**Foundational**
- Art. 9: Map all vector store deployments in Art. 9 risk
  management — RBAC status, encryption, CVE exposure,
  and network access controls per deployment

**Hardening — high-risk AI systems**
- Art. 15: Implement and document vector store security
  measures — RBAC, encryption, CVE patching, network
  isolation — as Art. 15 cybersecurity conformity evidence
- Art. 17: Include vector store security in post-market
  monitoring — patch cadence, access log review, anomaly
  detection coverage documented

**Advanced**
- Art. 15: Conduct adversarial vector store testing — document
  results as Art. 15 robustness evidence for conformity
  assessment
- Art. 17: Implement automated vector store integrity monitoring
  as part of post-market monitoring programme

#### Fines exposure
Art. 15 violations: up to **€15M or 3% global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant (with API key auth) | Open-source | https://qdrant.tech |

#### Cross-references
- LLM Top 10: LLM08 Vector & Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · NIST AI RMF MS-2.5 · CWE-284

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High
**Applies to:** High-risk · GPAI models · GDPR

Observability pipelines capture sensitive content — including personal
data — with weaker access controls and longer retention than production
systems. The EU AI Act requires post-market monitoring under Art. 17,
but this monitoring infrastructure must itself comply with data
governance requirements under Art. 10 and GDPR.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Data governance applies to all data in AI system scope — including telemetry and monitoring data | Telemetry data governance — classification, access controls, retention — is an Art. 10 requirement |
| Art. 17 — Quality management | Post-market monitoring required — but the monitoring infrastructure must itself be secured | Telemetry security is both an Art. 17 obligation and an Art. 10 data governance requirement |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Apply data governance to telemetry — classify
  captured data at the same level as the content it contains,
  implement access controls and retention limits
- Art. 17 requires post-market monitoring — implement it in
  a way that does not create secondary data exposure through
  inadequately protected observability stores

**Hardening — high-risk AI systems**
- Art. 10: Implement least-logging defaults and document
  as Art. 10 data minimisation measure — full payload
  capture only with explicit business justification
- Art. 17: Include telemetry security in quality management
  system — access controls, retention limits, and redaction
  documented as post-market monitoring infrastructure controls

**Advanced**
- Art. 10: Implement telemetry data lifecycle management —
  short TTL for debug traces, automated deletion, documented
  as Art. 10 data governance measure
- GDPR Art. 32: Implement encryption and access controls
  on all telemetry containing personal data — document as
  security of processing measure

#### Fines exposure
Art. 10 violations: up to **€15M or 3% global turnover**.
GDPR Art. 32 violations: up to **€20M or 4% global turnover**.

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15/A.8.12 · ISO 27701 · GDPR Art. 32

---

### DSGAI15 — Over-Broad Context Windows & Prompt Over-Sharing

**Severity:** High
**Applies to:** High-risk · GPAI models

Context windows aggregate data from multiple trust domains into a
single flat namespace with no internal access control. The EU AI Act
requires both data governance (Art. 10) and cybersecurity (Art. 15)
for the data processed within AI system context windows.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Data governance applies to all data in AI system scope — including context window content | Context window data governance — minimum content, classification tracking — is Art. 10 requirement |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity against adversarial exploitation of context window content | Context minimisation and access controls are Art. 15 cybersecurity measures |
| Art. 17 — Quality management | Post-market monitoring covering context window exploitation incidents | Context window security in post-market monitoring programme |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Track classification of all content entering context
  windows — highest classification drives handling requirement
  for the entire response — Art. 10 data governance requirement

**Hardening — high-risk AI systems**
- Art. 15: Implement context minimisation as Art. 15
  cybersecurity measure — minimum-necessary content injection,
  documented as conformity evidence
- Art. 17: Include context window exploitation scenarios in
  post-market monitoring — alert on cross-trust-domain
  aggregation patterns

**Advanced**
- Art. 15: Implement trust-domain-aware context assembly as
  advanced Art. 15 cybersecurity measure — document as
  conformity evidence
- Conduct red team exercises targeting context window
  exploitation — results documented as Art. 15 robustness
  evidence

#### Fines exposure
Art. 10/15 violations: up to **€15M or 3% global turnover**.

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: ISO 27001 A.8.3 · NIST AI RMF MS-2.5 · AIUC-1 A/B005

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High
**Applies to:** High-risk · GPAI models

Browser-integrated AI assistants access sensitive data across all
open tabs and local files. The EU AI Act's human oversight obligations
(Art. 14) and deployer requirements (Art. 29) directly address the
governance of AI agents operating on behalf of users in endpoint
environments.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Endpoint AI agent risks identified and mitigated | Browser and endpoint agent deployments assessed in Art. 9 risk management |
| Art. 14 — Human oversight | High-risk AI designed to allow human oversight — users must be able to stop and override | Users must be able to pause and override endpoint AI agents — Art. 14 human oversight requirement |
| Art. 29 — Deployer obligations | Deployers ensure human oversight as instructed by provider | Deployers responsible for ensuring endpoint AI agents operate within Art. 14 human oversight scope |

#### Compliance obligations by tier

**Foundational**
- Art. 14: Implement ability for users to pause and override
  endpoint AI agents — mandatory for high-risk systems,
  cannot be waived by deployers under Art. 29
- Art. 29: Deployers must follow provider human oversight
  instructions for endpoint AI — including approved extension
  lists and permission scoping

**Hardening — high-risk AI systems**
- Art. 14: Document human oversight mechanisms for endpoint
  AI — pause/stop controls, override capability, user
  notification — required for conformity assessment
- Art. 9: Include endpoint agent risks in risk management
  system — data access scope, exfiltration paths, malicious
  update vectors documented

**Advanced**
- Art. 15: Conduct adversarial testing of approved endpoint
  AI agents before organisation-wide deployment — document
  as Art. 15 robustness evidence
- Art. 29: Establish vendor security requirements for all
  endpoint AI providers — include in deployer obligations
  contractual framework

#### Fines exposure
Art. 14 violations: up to **€15M or 3% global turnover**.
Art. 29 deployer violations: up to **€15M or 3% global turnover**.

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · NIST AI RMF GV-1.7

---

### DSGAI17 — Data Availability & Resilience Failures in AI Pipelines

**Severity:** High
**Applies to:** High-risk · GPAI models

RAG pipelines fail silently when vector stores degrade — returning
stale information as if current. In OT and critical infrastructure
environments, this failure mode can propagate from the AI layer into
physical process decisions. The EU AI Act's robustness obligations
(Art. 15) and business continuity requirements are directly applicable.

**OT critical note:** For AI systems in critical infrastructure —
classified as high-risk under Annex III — Art. 15 robustness and
availability obligations carry heightened weight. Silent degradation
producing incorrect operational guidance is an Art. 15 failure with
potential Art. 5 implications if safety systems are affected.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI must remain accurate and available under adverse conditions | Vector store redundancy, circuit breakers, and staleness detection are Art. 15 requirements |
| Art. 17 — Quality management | Post-market monitoring covering availability and resilience | AI pipeline availability monitoring in quality management and post-market monitoring programme |

#### Compliance obligations by tier

**Foundational**
- Art. 15: Implement health checks on vector store freshness —
  alert when index staleness exceeds threshold before silent
  misinformation reaches users — basic Art. 15 requirement

**Hardening — high-risk AI systems**
- Art. 15: Implement and document technical resilience measures —
  vector store redundancy, circuit breakers, graceful degradation —
  as Art. 15 conformity evidence
- Art. 17: Include AI pipeline availability in post-market
  monitoring — SLA metrics, incident detection, and response
  procedures documented in quality management system

**Advanced**
- Art. 15: Conduct adversarial availability testing — vector
  store saturation and failover scenarios — document as
  Art. 15 robustness evidence
- For critical infrastructure deployments: treat availability
  failures as Art. 15 Annex III compliance failures —
  include in conformity assessment scope

#### Fines exposure
Art. 15 violations: up to **€15M or 3% global turnover**.
Annex III critical infrastructure failures: potential Art. 5
review if safety systems affected.

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6 (OT) · NIST SP 800-82 (OT)

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High
**Applies to:** High-risk · GPAI models · GDPR Art. 25

Adversaries reconstruct sensitive training data through membership
inference and model inversion attacks. The EU AI Act requires training
data privacy measures (Art. 10) and cybersecurity (Art. 15) — both
directly applicable to inference attack resistance. GDPR Art. 25
requires privacy by design including resistance to inference attacks.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training data privacy measures required — protecting sensitive data used in training | Differential privacy and inference attack resistance are Art. 10 data governance requirements |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures protecting against attacks including inference attacks | Output rate limiting, confidence score suppression, and embedding encryption are Art. 15 requirements |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Assess inference attack risk as part of data
  governance — membership inference and model inversion
  in scope alongside direct disclosure risks
- GDPR Art. 25: Privacy by design must include inference
  attack resistance for systems processing personal data
  in training

**Hardening — high-risk AI systems**
- Art. 10: Implement differential privacy in training as
  Art. 10 privacy measure — document privacy budget
  as conformity evidence
- Art. 15: Implement confidence score suppression and output
  rate limiting as Art. 15 cybersecurity measures
- Conduct membership inference red team exercises —
  document results as Art. 15 robustness evidence

**Advanced — GPAI models**
- Art. 53(1)(a): Document inference attack resistance
  measures in GPAI technical documentation — available
  to AI Office on request
- Implement machine unlearning readiness as Art. 10 data
  governance measure — erasure obligations enforceable
  even after training

#### Fines exposure
Art. 10/15 violations: up to **€15M or 3% global turnover**.
GDPR Art. 25 violations: up to **€20M or 4% global turnover**.

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · ISO 27701 · NIST AI RMF GV-1.6 · MITRE ATLAS AML.T0024

---

### DSGAI19 — Human-in-the-Loop & Labeler Overexposure

**Severity:** Medium
**Applies to:** High-risk · GPAI models · GDPR Art. 28

Human annotators and HITL reviewers access sensitive model inputs
during labelling. The EU AI Act requires data governance for training
data (Art. 10), and GDPR Art. 28 requires processor agreements with
all labelling vendors who process personal data.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training data governance includes human annotation workflows | Labeller data access controls and data minimisation are Art. 10 requirements for high-risk training data |
| Art. 25 — Value chain responsibilities | Labelling vendors are part of the AI value chain — obligations distributed accordingly | Labelling vendor security requirements and contractual controls are Art. 25 value chain obligations |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Apply data minimisation to labelling tasks —
  annotators access only minimum content for their annotation,
  documented as Art. 10 data governance measure
- GDPR Art. 28: All labelling vendors processing personal data
  must be covered by a GDPR-compliant data processing agreement

**Hardening — high-risk AI systems**
- Art. 10: Document labelling data governance in Art. 10
  compliance evidence — anonymisation procedures, access
  controls, retention limits, and contractor obligations
- Art. 25: Include labelling vendor requirements in value
  chain documentation — what obligations they hold and how
  compliance is verified

**Advanced — GPAI models**
- Art. 53(1)(a): Include HITL data governance in GPAI
  technical documentation — labelling workflow privacy
  measures documented and available to AI Office
- Implement synthetic data for labelling where possible —
  document as Art. 10 data minimisation measure

#### Fines exposure
Art. 10 violations: up to **€15M or 3% global turnover**.
GDPR Art. 28 violations: up to **€20M or 4% global turnover**.

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34/A.6.3 · NIST AI RMF GV-1.6 · GDPR Art. 28

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High
**Applies to:** High-risk · GPAI models

Adversaries reconstruct a functional model replica through systematic
querying. The EU AI Act requires cybersecurity measures (Art. 15) and
technical documentation protecting model IP (Art. 53) — both applicable
to model extraction defence.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures protecting AI system integrity | API rate limiting, output perturbation, and extraction monitoring are Art. 15 requirements |
| Art. 53(1)(a) — GPAI documentation | GPAI technical documentation includes model architecture and capability details | Technical documentation must be protected — model extraction enables circumvention of documentation obligations |
| Art. 17 — Quality management | Post-market monitoring covering security incidents | Model extraction detection in post-market monitoring programme |

#### Compliance obligations by tier

**Foundational**
- Art. 15: Implement rate limiting as basic Art. 15 cybersecurity
  measure — systematic extraction requires high query volumes
- Monitor for extraction patterns — anomalous query diversity
  and high-volume confidence score harvesting

**Hardening — high-risk AI systems**
- Art. 15: Implement and document output perturbation and
  extraction monitoring as Art. 15 cybersecurity measures —
  conformity assessment evidence
- Art. 17: Include model extraction detection in post-market
  monitoring — response procedures defined and tested

**Advanced — GPAI models**
- Art. 53(1)(a): Implement model watermarking — enables
  detection of replicated model usage in the wild,
  protects technical documentation integrity
- Art. 15: Conduct model extraction red team exercises —
  document results as robustness evidence for AI Office

#### Fines exposure
Art. 15 violations: up to **€15M or 3% global turnover**.
Art. 53 GPAI documentation violations: up to **€15M or 3%**.

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Reconstruction
- Other frameworks: ISO 27001 A.5.12/A.8.3 · MITRE ATLAS AML.T0016 · NIST AI RMF MS-2.5

---

### DSGAI21 — Disinformation & Integrity Attacks via Data Poisoning

**Severity:** High
**Applies to:** High-risk · GPAI models · GPAI systemic risk

Adversaries inject false content into trusted retrieval sources so AI
systems surface it as authoritative output. The EU AI Act directly
mandates disinformation risk assessment for systemic risk GPAI models
(Art. 55(1)(a)) and data integrity controls for all high-risk systems
(Art. 10/15).

**Real-world references:**
- Grok RAG incident (2025) — production RAG system surfaced
  externally introduced false information as authoritative output

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training and retrieval data free from errors — source integrity required | RAG corpus integrity controls and source verification are Art. 10 requirements |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI accurate and resilient against adversarial data manipulation | Source trust scoring and ingestion validation are Art. 15 robustness requirements |
| Art. 55(1)(a) — Systemic risk GPAI | Systemic risk GPAI providers must assess and mitigate risks including disinformation | Disinformation risk assessment and RAG integrity controls are binding Art. 55 obligations |
| Art. 50 — Transparency | AI-generated content that could be mistaken as human must be disclosed | Disinformation risk amplified when users cannot distinguish AI-generated content — Art. 50 applies |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 50: If your system generates content that could be
  mistaken for human-authored output, disclose the AI nature —
  universal obligation regardless of risk tier
- Art. 10: Implement source integrity controls for all retrieval
  corpora — document as Art. 10 data governance measure

**Hardening — high-risk AI systems**
- Art. 10: Implement and document source trust tiering and
  ingestion anomaly detection as Art. 10 data governance
  and Art. 15 robustness evidence for conformity assessment
- Art. 15: Include RAG poisoning scenarios in adversarial
  testing — results documented as Art. 15 conformity evidence
- Art. 17: Include disinformation incident response in quality
  management — source quarantine, index rebuild, user notification

**Advanced — systemic risk GPAI models**
- Art. 55(1)(a): Conduct and document disinformation risk
  assessment — implement mitigations, available to AI Office
- Art. 55: Report serious disinformation incidents to the
  AI Office without undue delay
- Implement adversarial integrity evaluation as standard
  pre-deployment gate — document as Art. 55 compliance measure

#### Fines exposure
Art. 10/15 violations: up to **€15M or 3% global turnover**.
Art. 55 systemic risk violations: up to **€35M or 7% global turnover**.
Art. 50 transparency violations: up to **€7.5M or 1.5% global turnover**.

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.5.7/A.8.27 · NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0045

---

## DSGAI × EU AI Act compliance checklist

### August 2025 — GPAI obligations (already past)

- [ ] Determine if any GenAI systems qualify as GPAI models (Art. 51)
- [ ] If GPAI: technical documentation published (Art. 53(1)(a)) — covers DSGAI01/04/07/09
- [ ] If GPAI: information security policy implemented (Art. 53)
- [ ] If GPAI: copyright compliance policy published (Art. 53(1)(c))
- [ ] If systemic risk GPAI: registered with AI Office
- [ ] If systemic risk GPAI: adversarial testing programme live (Art. 55(1)(b)) — covers DSGAI04/21
- [ ] All chatbots and AI-generated content: Art. 50 disclosure implemented

### August 2026 — High-risk obligations (4 months away)

- [ ] Classify all GenAI systems against Annex III high-risk categories
- [ ] Art. 9 risk management system documented and live — covers all DSGAI entries
- [ ] Art. 10 data governance policy implemented — covers DSGAI01/04/07/09/10/11/14/18/19/21
- [ ] Art. 13 technical documentation complete — capabilities, limitations, data handling
- [ ] Art. 14 human oversight implemented and tested — covers DSGAI12/16
- [ ] Art. 15 cybersecurity measures documented — covers DSGAI02/04/05/12/13/17/20
- [ ] Art. 17 quality management system operational including post-market monitoring
- [ ] Conformity assessment completed
- [ ] EU Declaration of Conformity signed
- [ ] Registration in EU AI database completed

### Ongoing

- [ ] Art. 17 post-market monitoring active and reporting
- [ ] Art. 55 incident reporting capability tested (systemic risk GPAI)
- [ ] Annual risk classification review as systems evolve
- [ ] GDPR parallel obligations reviewed with DPO for all personal data entries

---

## Implementation priority aligned to EU AI Act

| Phase | DSGAI entries | Articles | Deadline |
|---|---|---|---|
| 1 — Immediate | DSGAI08 — understand your obligations | Art. 5/51/72 — classification and fines | Now |
| 2 — Urgent | DSGAI01/04/07 — GPAI data governance | Art. 53(1)(a) | Aug 2025 — already past |
| 3 — Critical | DSGAI02/05/12/13/17/20 — cybersecurity | Art. 15 | Aug 2026 |
| 4 — Critical | DSGAI01/09/10/11/14/18/19 — data governance | Art. 10 | Aug 2026 |
| 5 — Critical | DSGAI12/16 — human oversight | Art. 14 | Aug 2026 |
| 6 — Ongoing | DSGAI21 — disinformation systemic risk | Art. 55(1)(a) | Continuous |

---

## References

- [EU AI Act full text (Regulation EU 2024/1689)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [EU AI Act and GDPR interaction guidance — EDPB](https://www.edpb.europa.eu)
- [ISO 42001 — AI management systems](https://www.iso.org/standard/81230.html)
- [ENISA AI Act implementation guidance](https://www.enisa.europa.eu)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries with compliance checklist | OWASP GenAI Data Security Initiative |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
