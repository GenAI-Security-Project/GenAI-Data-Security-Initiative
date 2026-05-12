<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : EU Artificial Intelligence Act (EU AI Act)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × EU AI Act

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [EU Artificial Intelligence Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
(Regulation EU 2024/1689), which entered into force August 1, 2024.

The EU AI Act is the world's first comprehensive binding legal framework
for AI. It applies to any provider, deployer, importer, or distributor
placing AI systems on the EU market or putting them into service in the EU
— regardless of where the organisation is headquartered. Non-compliance
carries fines up to €35 million or 7% of global annual turnover.

---

## Compliance timeline — act now

| Date | Obligation |
|---|---|
| February 2, 2025 | Prohibited AI practices ban in force |
| August 2, 2025 | GPAI model obligations apply — transparency, copyright, systemic risk |
| August 2, 2026 | **High-risk AI system obligations apply** — conformity assessment, technical documentation, human oversight |
| August 2, 2027 | Additional high-risk system obligations for specific sectors |

**August 2026 is 4 months away.** If your LLM system qualifies as
high-risk, conformity assessment requirements are live in August.
This file maps each OWASP LLM Top 10 entry to the specific EU AI Act
articles and obligations that apply.

---

## Risk classification — where do LLMs sit?

| Classification | Definition | LLM examples |
|---|---|---|
| Prohibited (Art. 5) | Banned regardless of safeguards | Social scoring, real-time biometric surveillance, subliminal manipulation |
| High-risk (Annex III) | Permitted with strict obligations | LLMs in employment decisions, credit scoring, education assessment, critical infrastructure, law enforcement, justice |
| GPAI model (Art. 51–55) | General purpose AI model obligations | Any LLM with >10^25 FLOPs training compute (systemic risk tier) or released via API/open weights |
| Limited risk (Art. 50) | Transparency obligations only | Chatbots, deepfake generators — must disclose AI nature |
| Minimal risk | No specific obligations | Most narrow-purpose AI tools |

**GPAI note:** Most commercially deployed LLMs fall under GPAI obligations
from August 2025. All providers must publish technical documentation,
comply with copyright law, and implement information security policies.
Systemic risk models (GPT-4 class and above) face additional adversarial
testing and incident reporting obligations.

---

## Quick-reference summary

| ID | Name | Severity | Primary EU AI Act Articles | Applies to | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | Art. 9, Art. 15, Art. 55(1)(b) | High-risk · GPAI systemic | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | Art. 10, Art. 13, Art. 17, GDPR intersection | High-risk · GPAI · Limited risk | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | Art. 9, Art. 17, Art. 25, Art. 53(1)(a) | High-risk · GPAI | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | Art. 9, Art. 10, Art. 15, Art. 55(1)(b) | High-risk · GPAI systemic | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Hardening |
| LLM06 | Excessive Agency | High | Art. 9, Art. 14, Art. 29 | High-risk · GPAI | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | Art. 13, Art. 17, Art. 53(1)(b) | High-risk · GPAI · Limited risk | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | Art. 9, Art. 10, Art. 15 | High-risk · GPAI | Hardening–Advanced |
| LLM09 | Misinformation | Medium | Art. 13, Art. 50, Art. 55(1)(a) | All tiers | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Hardening |

---

## Audience tags

- **CISO / governance** — full file, primary EU AI Act compliance reference
- **Legal / compliance officer** — Articles mapping, risk classification, fines
- **DPO (Data Protection Officer)** — LLM02, LLM04, LLM07 GDPR intersection
- **Security engineer** — Art. 9 and Art. 15 entries per vulnerability
- **Developer** — Art. 15 technical robustness requirements
- **Auditor** — Art. 17 quality management, Art. 9 risk management
- **OT engineer** — LLM01, LLM04, LLM10 critical infrastructure provisions

---

## Key articles reference

| Article | Title | Relevance |
|---|---|---|
| Art. 5 | Prohibited AI practices | Banned capabilities — know before building |
| Art. 9 | Risk management system | Mandatory for high-risk: identify, analyse, evaluate, mitigate risks |
| Art. 10 | Data and data governance | Training data quality, relevance, freedom from errors, privacy |
| Art. 13 | Transparency and information provision | Users must understand capabilities and limitations |
| Art. 14 | Human oversight | Meaningful human oversight over high-risk AI system outputs |
| Art. 15 | Accuracy, robustness, and cybersecurity | Technical measures for resilience against adversarial attack |
| Art. 17 | Quality management system | Documentation, procedures, post-market monitoring |
| Art. 25 | Responsibilities along the AI value chain | Provider and deployer obligations — who is responsible for what |
| Art. 29 | Obligations of deployers | Deployer-specific requirements including human oversight and monitoring |
| Art. 50 | Transparency obligations for certain AI systems | Disclosure that output is AI-generated — chatbots, deepfakes |
| Art. 51 | Classification as GPAI model | Definition of general purpose AI model |
| Art. 53 | Obligations for GPAI model providers | Technical documentation, copyright compliance, information security |
| Art. 55 | Obligations for systemic risk GPAI models | Adversarial testing, incident reporting, cybersecurity measures |
| Art. 72 | Fines for non-compliance | Up to €35M or 7% global turnover |

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical
**Applies to:** High-risk AI systems · GPAI models with systemic risk

Malicious instructions in input or processed content manipulate LLM
behaviour, bypassing safety controls. The EU AI Act directly mandates
cybersecurity and robustness measures for high-risk systems and
adversarial testing for systemic risk GPAI models — both directly
applicable to prompt injection.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Providers of high-risk AI must implement a risk management system covering all reasonably foreseeable risks | Prompt injection must be identified, analysed, and mitigated in the risk management system |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI systems must be resilient to adversarial inputs and attempts to alter outputs or performance | Robustness against prompt injection is a technical compliance requirement — not optional |
| Art. 55(1)(b) — Systemic risk GPAI | Providers of systemic risk GPAI models must conduct adversarial testing to identify and mitigate systemic risks | Prompt injection adversarial testing is a binding obligation for systemic risk models |

#### Compliance obligations by tier

**Foundational — applies to all LLM deployments**
- Art. 50 (limited risk): If your LLM is a chatbot, disclose to
  users they are interacting with AI — this baseline applies even
  before prompt injection mitigations
- Document prompt injection as a foreseeable risk in your Art. 9
  risk management system if deploying a high-risk system
- Implement basic input validation and prompt structure enforcement
  as part of Art. 15 cybersecurity measures

**Hardening — required for high-risk AI systems (from Aug 2026)**
- Art. 9: Maintain documented risk treatment for prompt injection —
  controls, residual risk acceptance, review cadence
- Art. 15: Implement and document technical robustness measures
  including adversarial input detection and filtering
- Art. 17: Include prompt injection controls in quality management
  system documentation — auditable evidence required

**Advanced — required for systemic risk GPAI models (from Aug 2025)**
- Art. 55(1)(b): Conduct and document adversarial testing covering
  prompt injection — results must be available to the AI Office on
  request
- Art. 55: Implement incident reporting for serious incidents
  involving prompt injection — notify the AI Office without
  undue delay
- Establish red team programme specifically for prompt injection
  documented as part of Art. 55 cybersecurity measures

#### Fines exposure
Violation of Art. 15 technical requirements for high-risk systems:
up to **€15 million or 3% of global turnover**. Violation of Art. 55
systemic risk obligations: up to **€35 million or 7% of global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Rebuff | Open-source | https://github.com/protectai/rebuff |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage
- Other frameworks: NIST AI RMF MS-2.5 · MITRE ATLAS AML.T0051 · ISO 42001 6.1.2

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High
**Applies to:** High-risk AI systems · GPAI models · Limited risk systems · GDPR intersection

LLMs expose PII, financial data, or proprietary information through
outputs. This sits at the intersection of the EU AI Act and GDPR —
both apply simultaneously and both impose binding obligations on
providers and deployers.

**GDPR intersection:** Where sensitive information disclosed by an LLM
includes personal data, GDPR Articles 5, 25 (data protection by design),
and 32 (security of processing) apply in addition to the EU AI Act.
Non-compliance with both simultaneously is possible from a single
incident.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Training data for high-risk AI must be relevant, representative, free of errors, and complete — must address privacy | Privacy-preserving training data practices are a compliance requirement for high-risk LLMs |
| Art. 13 — Transparency | Users must receive information about capabilities, limitations, and conditions of use | Disclosure of potential data disclosure risks is a transparency obligation |
| Art. 17 — Quality management | Documented quality management system including post-market monitoring | Post-market monitoring must detect and respond to sensitive disclosure incidents |
| Art. 53(1)(a) — GPAI documentation | GPAI providers must maintain technical documentation including training data governance | Data governance for GPAI training data is a binding documentation obligation from Aug 2025 |

#### Compliance obligations by tier

**Foundational — applies to all LLM deployments**
- Art. 13 (all risk tiers): Document and communicate to users what
  data the LLM has access to and what data may appear in outputs —
  this is a baseline transparency obligation
- Art. 50: If deploying a chatbot, disclose AI nature and ensure
  users understand the system may produce outputs based on their data

**Hardening — required for high-risk AI systems**
- Art. 10: Implement and document data governance for training data —
  data sources, quality controls, privacy measures, and bias mitigation
- Art. 17: Establish post-market monitoring for sensitive disclosure
  incidents — detection, logging, and response procedures documented
- Implement output scanning for PII and sensitive patterns as a
  technical Art. 15 cybersecurity measure

**Advanced — required for GPAI models (from Aug 2025)**
- Art. 53(1)(a): Maintain technical documentation covering training
  data governance — available to the AI Office on request
- GDPR Art. 25: Implement data protection by design — differential
  privacy in training, RAG access controls, output redaction
- Establish machine unlearning capability as Art. 17 post-market
  monitoring enables response to GDPR erasure requests intersecting
  with model training data

#### Fines exposure
GDPR violations: up to **€20 million or 4% of global turnover**.
EU AI Act Art. 17 quality management failures: up to
**€15 million or 3% of global turnover**.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Private AI | Commercial | https://private-ai.com |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance & Lifecycle, DSGAI08 Non-Compliance & Regulatory Violations
- Other frameworks: ISO 27701 · NIST AI RMF GV-1.6 · GDPR Art. 5/25/32

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High
**Applies to:** High-risk AI systems · GPAI models

Third-party model weights, datasets, libraries, and plugins introduce
risks the deployer inherits. The EU AI Act explicitly addresses supply
chain responsibilities — distributing obligations between providers,
deployers, importers, and distributors.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Supply chain risks must be identified and mitigated in the risk management system | Third-party component risks are in scope for Art. 9 risk management |
| Art. 17 — Quality management | Quality management must cover supply chain controls | Documented supply chain security procedures required |
| Art. 25 — Value chain responsibilities | Responsibilities distributed along the AI value chain between providers and deployers | Providers must document what deployers inherit — deployers must verify |
| Art. 53(1)(a) — GPAI documentation | GPAI providers must document training data governance including third-party sources | Third-party training data provenance is a GPAI documentation obligation |

#### Compliance obligations by tier

**Foundational — applies to all LLM deployments**
- Art. 25: Understand and document your position in the AI value
  chain — are you a provider, deployer, or both? Each carries
  distinct obligations
- Maintain a basic inventory of all third-party components used
  in your LLM deployment

**Hardening — required for high-risk AI systems**
- Art. 9: Include supply chain risks in your formal risk management
  system — third-party components assessed before production use
- Art. 17: Establish documented supply chain security procedures —
  component verification, version pinning, integrity checking
- Art. 25: Document what obligations flow downstream to deployers —
  include in contractual arrangements

**Advanced — required for GPAI models**
- Art. 53(1)(a): Document all training data sources including
  third-party datasets — provenance, quality assessment, copyright
  status, and privacy compliance
- Implement ML SBOM generation as part of Art. 53 technical
  documentation — available to the AI Office on request
- Establish supply chain incident response — what happens when a
  third-party component is compromised post-deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST AI RMF MP-5.1 · NIST SP 800-218A · ISO 42001 8.4

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical
**Applies to:** High-risk AI systems · GPAI models with systemic risk

Adversaries corrupt training data or model weights. The EU AI Act
mandates data governance, quality controls, and adversarial robustness
testing — all directly applicable to poisoning prevention and detection.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Data poisoning must be identified as a foreseeable risk and mitigated | Poisoning attack scenarios required in Art. 9 risk assessment |
| Art. 10 — Data and data governance | Training data must be subject to appropriate governance practices — relevant, representative, free of errors | Data quality controls preventing poisoning are a compliance requirement |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI must be resilient to attempts to alter performance through data manipulation | Technical robustness against poisoning is a binding Art. 15 requirement |
| Art. 55(1)(b) — Systemic risk GPAI adversarial testing | Systemic risk GPAI providers must conduct adversarial testing to identify model-level risks | Poisoning detection is in scope for Art. 55 adversarial testing |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Establish data governance policy for all training data —
  source validation, quality assessment, and lineage documentation
  are baseline requirements for high-risk systems
- Document data poisoning as a foreseeable risk in Art. 9 risk
  management system

**Hardening — required for high-risk AI systems**
- Art. 10: Implement technical data quality controls — anomaly
  detection on training datasets, source allowlisting, lineage
  tracking — documented as Art. 17 quality management evidence
- Art. 15: Implement and document adversarial robustness measures
  against training data manipulation — auditable evidence required
- Establish model rollback capability as part of Art. 17 post-market
  monitoring response procedures

**Advanced — required for systemic risk GPAI models**
- Art. 55(1)(b): Conduct adversarial testing covering poisoning
  attack scenarios — document results, available to AI Office
- Art. 55: Implement incident reporting for serious poisoning
  incidents — notify AI Office without undue delay
- Apply differential privacy in training as an Art. 10 data
  governance measure — document privacy budget

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · ISO 42001 8.4 · MITRE ATLAS AML.T0032

---

### LLM05 — Insecure Output Handling

**Severity:** High
**Applies to:** High-risk AI systems · GPAI models

LLM output passed to downstream systems without validation enables
injection attacks. The EU AI Act requires accuracy and robustness
of high-risk AI outputs and mandates quality management systems
covering post-market monitoring of output incidents.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Output handling risks identified and mitigated | Insecure output handling included in risk management system |
| Art. 15 — Accuracy, robustness, cybersecurity | Accurate, robust outputs resilient to misuse | Output validation and sanitisation are Art. 15 technical requirements |
| Art. 17 — Quality management | Documented procedures covering output quality | Post-market monitoring of output handling incidents required |

#### Compliance obligations by tier

**Foundational**
- Art. 9: Document insecure output handling as a foreseeable risk
  in your risk management system — assign treatment controls
- Treat all LLM output as untrusted input to downstream systems —
  encoding, validation, and sanitisation mandatory

**Hardening — required for high-risk AI systems**
- Art. 15: Implement and document technical output security measures —
  schema validation, sanitisation, encoding — as auditable evidence
- Art. 17: Establish post-market monitoring for output handling
  incidents — detection, logging, and response procedures
- Include output injection scenarios in conformity assessment
  testing evidence

**Advanced**
- Conduct DAST on all interfaces consuming LLM output — include
  results in Art. 17 quality management documentation
- Deploy dedicated output security layer documented as Art. 15
  cybersecurity measure
- Art. 17: Include output security in product change management
  procedures — any change to output handling triggers re-testing

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures
- Other frameworks: NIST AI RMF MS-2.6 · OWASP ASVS V5 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High
**Applies to:** High-risk AI systems · GPAI models

LLMs with excessive autonomy execute unintended actions when
manipulated. The EU AI Act places explicit human oversight obligations
on high-risk AI systems — Article 14 is the most directly applicable
article in the entire regulation to this vulnerability.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Autonomy-related risks identified and mitigated | Excessive agency scenarios required in risk management system |
| Art. 14 — Human oversight | High-risk AI systems designed to allow effective human oversight — ability to pause, stop, and override | Human-in-the-loop requirements are a binding Art. 14 compliance obligation |
| Art. 29 — Deployer obligations | Deployers must ensure human oversight as instructed by provider | Deployers cannot waive Art. 14 human oversight requirements |

#### Compliance obligations by tier

**Foundational**
- Art. 14: Implement ability for human operators to pause, stop, or
  override LLM actions — this is mandatory for high-risk systems
  and cannot be waived by deployers under Art. 29
- Document autonomy limits in Art. 13 transparency documentation —
  users must understand what the system can and cannot do autonomously

**Hardening — required for high-risk AI systems**
- Art. 14: Implement and document effective human oversight measures —
  what actions require approval, who can override, how overrides
  are logged — auditable evidence required for conformity assessment
- Art. 9: Map all tool and API integrations against risk levels in
  the risk management system — least-privilege controls documented
- Art. 29: Provide deployers with documented human oversight
  instructions — deployers are legally obligated to follow them

**Advanced**
- Art. 17: Include human oversight effectiveness in post-market
  monitoring — measure override rates, intervention effectiveness
- Formally specify permitted action boundaries as part of Art. 9
  risk management — machine-verifiable where possible
- Red team exercises testing human oversight effectiveness — document
  results as Art. 17 quality management evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: NIST AI RMF GV-1.7 · AIUC-1 B006/C · ISO 42001 6.1.2

---

### LLM07 — System Prompt Leakage

**Severity:** High
**Applies to:** High-risk AI systems · GPAI models · Limited risk systems

System prompt extraction reveals internal instructions and security
controls. The EU AI Act imposes transparency obligations on all
AI systems and documentation obligations on high-risk and GPAI systems —
both of which create a tension with system prompt confidentiality
that must be actively managed.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 13 — Transparency | Users must receive sufficient information about the AI system — but this does not require disclosing system prompts | Transparency obligation must be met without exposing security-sensitive system prompt content |
| Art. 17 — Quality management | Configuration management documented | System prompt versions, access controls, and change procedures are quality management artefacts |
| Art. 53(1)(b) — GPAI transparency | GPAI providers must publish summaries of training data and model capabilities | Published summaries must not inadvertently expose security-sensitive configuration |

#### Compliance obligations by tier

**Foundational**
- Art. 13: Comply with transparency obligations without disclosing
  security-sensitive system prompt content — the obligation is to
  explain system capabilities and limitations, not expose internals
- Classify system prompts as sensitive configuration artefacts
  subject to access controls — document in Art. 17 quality management

**Hardening — required for high-risk AI systems**
- Art. 17: Implement system prompt version control and change
  management procedures — auditable evidence of who changed what
  and when required for conformity assessment
- Include prompt extraction testing in conformity assessment
  evidence — demonstrate that transparency obligations can be met
  without leaking security controls
- Art. 13: Document and test the boundary between what is disclosed
  for transparency and what is protected as security configuration

**Advanced**
- Art. 53(1)(b): For GPAI models, ensure capability summaries and
  technical documentation published under Art. 53 do not reveal
  security-sensitive configuration
- Implement system prompt tokenisation as Art. 15 cybersecurity
  measure — document as technical robustness control
- Conduct adversarial prompt extraction red team exercises and
  document results as Art. 17 quality management evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: NIST AI RMF GV-1.6 · AIUC-1 B003/B009 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium
**Applies to:** High-risk AI systems · GPAI models

Embedding store vulnerabilities enable retrieval manipulation and
information inference. The EU AI Act addresses this through data
governance and technical robustness requirements for high-risk systems
whose outputs rely on retrieval-augmented generation.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Embedding and retrieval risks identified and mitigated | Vector store attack scenarios included in risk management system |
| Art. 10 — Data and data governance | Data quality controls applied to all data in scope — including RAG corpora | Quality controls on embedding generation and vector store ingestion required |
| Art. 15 — Accuracy, robustness, cybersecurity | Technical robustness against adversarial manipulation | Embedding manipulation resistance is an Art. 15 technical requirement |

#### Compliance obligations by tier

**Foundational**
- Art. 10: Apply data quality controls to all content entering
  vector stores — classification, validation, and access controls
  are Art. 10 requirements for high-risk RAG systems
- Document vector store risks in Art. 9 risk management system

**Hardening — required for high-risk AI systems**
- Art. 15: Implement technical controls for embedding integrity —
  access controls, anomaly detection, encryption — documented as
  Art. 15 cybersecurity measures
- Art. 10: Audit RAG data scope regularly — over-permissive indexes
  are both a security risk and an Art. 10 data governance failure
- Include embedding manipulation scenarios in conformity assessment
  testing evidence

**Advanced**
- Conduct embedding inversion red team exercises — document results
  as Art. 17 quality management evidence
- Implement differential privacy in embedding generation for
  sensitive corpora — document as Art. 15 technical measure
- Art. 17: Establish vector store integrity monitoring in post-market
  monitoring programme

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-3.3 · AIUC-1 A · ISO 27701

---

### LLM09 — Misinformation

**Severity:** Medium
**Applies to:** All risk tiers — transparency obligations apply universally

LLMs generate plausible but false content. The EU AI Act's transparency
and accuracy obligations apply broadly — Article 50 creates baseline
disclosure requirements for all chatbots and AI-generated content,
and Article 13 requires high-risk systems to be sufficiently accurate.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 13 — Transparency | High-risk AI system information must include accuracy metrics and known limitations | Hallucination rates and accuracy limitations must be disclosed to deployers and users |
| Art. 50 — Transparency for certain AI systems | AI-generated content must be marked as such — chatbots must disclose AI nature | Mandatory AI disclosure prevents users from treating hallucinated content as authoritative human output |
| Art. 55(1)(a) — Systemic risk GPAI | Systemic risk GPAI providers must assess and mitigate risks including disinformation | Misinformation risk assessment and mitigation is a binding obligation for systemic risk models |

#### Compliance obligations by tier

**Foundational — applies to all LLM deployments**
- Art. 50: All chatbot deployments must disclose to users that they
  are interacting with an AI system — this is a universal obligation
  regardless of risk tier, in force from August 2025
- Art. 50: AI-generated content that could be mistaken for human
  content must be marked as AI-generated — deepfakes explicitly
  included

**Hardening — required for high-risk AI systems**
- Art. 13: Include accuracy metrics and known limitations in
  technical documentation provided to deployers — deployers must
  understand hallucination rates before deployment
- Implement RAG grounded on verified sources — document as Art. 9
  risk mitigation for misinformation risk
- Art. 17: Establish post-market monitoring for misinformation
  incidents — detection and correction procedures documented

**Advanced — required for systemic risk GPAI models**
- Art. 55(1)(a): Conduct and document risk assessment for
  disinformation and misinformation — implement mitigations,
  available to AI Office on request
- Art. 55: Report serious incidents involving AI-generated
  disinformation to the AI Office without undue delay
- Deploy automated fact-checking for high-stakes output domains —
  document as Art. 55 systemic risk mitigation measure

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: NIST AI RMF GV-1.7/MS-4.1 · AIUC-1 F · ENISA

---

### LLM10 — Unbounded Consumption

**Severity:** Medium
**Applies to:** High-risk AI systems · GPAI models

Adversarial inputs cause resource exhaustion or denial of service.
The EU AI Act requires high-risk AI systems to be resilient and
available, with documented quality management covering operational
continuity.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Availability risks identified and mitigated | Resource exhaustion and DoS scenarios included in risk management system |
| Art. 15 — Accuracy, robustness, cybersecurity | High-risk AI must remain available under adversarial conditions | Technical resilience against denial-of-service attacks is an Art. 15 requirement |
| Art. 17 — Quality management | Operational continuity procedures documented | Post-market monitoring and incident response for availability failures required |

#### Compliance obligations by tier

**Foundational**
- Art. 9: Document resource exhaustion as a foreseeable risk —
  include in risk management system with treatment controls assigned
- Implement rate limiting per user, session, and API key —
  basic Art. 15 cybersecurity measure

**Hardening — required for high-risk AI systems**
- Art. 15: Implement and document technical resilience measures —
  rate limiting, token limits, cost budgets — as Art. 15 cybersecurity
  evidence for conformity assessment
- Art. 17: Establish post-market monitoring for availability
  incidents — SLA metrics, incident detection, and response
  procedures documented
- Define and document RTO/RPO for high-risk LLM services as
  Art. 17 quality management requirements

**Advanced**
- Art. 15: Conduct adversarial cost-maximisation testing — document
  results as robustness evidence
- Implement adaptive rate limiting with real-time load awareness —
  document as Art. 15 cybersecurity measure
- Art. 17: Include availability SLAs in post-market monitoring
  programme — reviewed quarterly against actual operational data

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: NIST AI RMF MG-3.2 · ISA/IEC 62443 SR 7.1 (OT) · CWE-400

---

## Compliance readiness checklist

Use this checklist to assess your current EU AI Act posture
against the OWASP LLM Top 10:

### August 2025 — GPAI obligations (already in force)

- [ ] Determine if your LLM qualifies as a GPAI model (Art. 51)
- [ ] If GPAI: publish technical documentation (Art. 53(1)(a))
- [ ] If GPAI: implement copyright compliance policy (Art. 53(1)(c))
- [ ] If GPAI: establish information security policy (Art. 53)
- [ ] If systemic risk: register with EU AI Office (Art. 55)
- [ ] If systemic risk: adversarial testing programme live (Art. 55(1)(b))
- [ ] All chatbots: AI disclosure implemented (Art. 50)

### August 2026 — High-risk obligations (4 months away)

- [ ] Determine if your LLM qualifies as high-risk (Annex III)
- [ ] Art. 9 risk management system documented and live
- [ ] Art. 10 data governance policy documented
- [ ] Art. 13 technical documentation complete
- [ ] Art. 14 human oversight measures implemented and tested
- [ ] Art. 15 cybersecurity and robustness measures documented
- [ ] Art. 17 quality management system operational
- [ ] Conformity assessment completed (self-assessment or third-party)
- [ ] EU Declaration of Conformity signed
- [ ] CE marking applied (where applicable)
- [ ] Registration in EU AI database completed

---

## Implementation priority aligned to EU AI Act

| Phase | Priority | Articles | Deadline |
|---|---|---|---|
| 1 — Immediate | Classify your system, implement Art. 50 chatbot disclosure | Art. 50, Art. 51 | Already required |
| 2 — Urgent | GPAI documentation, copyright compliance, security policy | Art. 53 | Aug 2025 — already past |
| 3 — Critical | High-risk conformity assessment, Art. 9/14/15/17 | Art. 9, 14, 15, 17 | Aug 2026 |
| 4 — Ongoing | Post-market monitoring, incident reporting, AI Office engagement | Art. 17, Art. 55 | Continuous |

---

## References

- [EU AI Act full text (Regulation EU 2024/1689)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- [EU AI Act Implementation Guide — European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [NIST AI RMF — EU AI Act crosswalk](https://airc.nist.gov)
- [ISO 42001 — AI management systems](https://www.iso.org/standard/81230.html)
- [ENISA — EU AI Act guidance](https://www.enisa.europa.eu)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with compliance checklist | OWASP GenAI Data Security Initiative |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
