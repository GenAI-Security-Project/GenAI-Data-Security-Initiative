<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : NIST AI Risk Management Framework (AI RMF 1.0)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × NIST AI RMF

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
and its companion [NIST AI RMF Playbook](https://airc.nist.gov/Docs/2).

The NIST AI RMF is the primary governance framework for trustworthy AI
in the United States and is widely adopted globally by enterprises,
government agencies, and critical infrastructure operators. It organises
AI risk management across four core functions — GOVERN, MAP, MEASURE,
MANAGE — each with subcategories that map directly to LLM security controls.
US federal agencies are required to align with the AI RMF under Executive
Order 14110. It is the foundational framework for enterprise AI governance
programmes and pairs directly with NIST CSF 2.0 for organisations already
using the cybersecurity framework.

---

## AI RMF core functions

| Function | Purpose | Key subcategories |
|---|---|---|
| GOVERN (GV) | Policies, accountability, culture, and oversight for AI risk | GV-1 Policies · GV-2 Accountability · GV-3 Workforce · GV-4 Organisational teams · GV-5 Policies for AI |
| MAP (MP) | Identifying and categorising AI risks in context | MP-1 Context · MP-2 Risk categorisation · MP-3 AI system impact · MP-4 Risk tolerance · MP-5 Interdependencies |
| MEASURE (MS) | Analysing and assessing identified AI risks | MS-1 Risk measurement · MS-2 Testing and evaluation · MS-3 Data quality · MS-4 Feedback |
| MANAGE (MG) | Prioritising and treating AI risks | MG-1 Risk treatment · MG-2 Risk response · MG-3 Residual risk · MG-4 Risk monitoring |

---

## Quick-reference summary

| ID | Name | Severity | Primary AI RMF Subcategories | Tier | Scope |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | GV-1.7, MP-2.3, MS-2.5, MG-2.2 | Foundational–Advanced | Both |
| LLM02 | Sensitive Information Disclosure | High | GV-1.6, MP-2.3, MS-2.6, MG-2.4 | Foundational–Advanced | Both |
| LLM03 | Supply Chain Vulnerabilities | High | GV-1.6, MP-5.1, MS-2.5, MG-3.2 | Foundational–Hardening | Both |
| LLM04 | Data and Model Poisoning | Critical | MP-2.3, MS-2.5, MS-3.3, MG-2.2 | Hardening–Advanced | Both |
| LLM05 | Insecure Output Handling | High | MS-2.5, MS-2.6, MG-2.2, GV-1.7 | Foundational–Hardening | Build |
| LLM06 | Excessive Agency | High | GV-1.7, MP-2.3, MS-2.5, MG-2.2 | Foundational–Hardening | Build |
| LLM07 | System Prompt Leakage | High | GV-1.6, MS-2.6, MG-2.4, MP-2.3 | Foundational–Hardening | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | MS-2.5, MS-3.3, MG-2.2, MP-2.3 | Hardening–Advanced | Build |
| LLM09 | Misinformation | Medium | GV-1.7, MS-2.6, MS-4.1, MG-2.4 | Foundational–Hardening | Both |
| LLM10 | Unbounded Consumption | Medium | MS-2.5, MG-2.2, MG-3.2, GV-1.7 | Foundational–Hardening | Both |

---

## Audience tags

- **CISO / governance** — full file, primary AI RMF governance reference
- **Compliance officer** — GV subcategories, implementation tiers
- **Risk manager** — MAP and MEASURE subcategories
- **Security engineer** — MEASURE and MANAGE subcategories
- **Developer** — MS-2.5, MG-2.2 entries per vulnerability
- **Auditor** — GV-1.6, GV-1.7, MS-2.6 entries
- **OT engineer** — LLM01, LLM04, LLM10 with ISA 62443 crosswalk

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour, bypassing safety controls and executing unauthorised
actions. The NIST AI RMF addresses this primarily through governance
of input handling policies, risk measurement of adversarial inputs,
and managed response to injection incidents.

**Real-world references:**
- EchoLeak (2025) — Microsoft 365 Copilot turned into silent
  exfiltration engine via indirect prompt injection
- Samsung source code leak (2023) — proprietary code surfaced
  through manipulated model queries

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Policies for trustworthy AI characteristics | GV-1.7 | GOVERN | Organisational policies explicitly address adversarial input risks including prompt injection |
| Risk categorisation | MP-2.3 | MAP | Prompt injection categorised as a high-priority risk in the AI system risk register |
| Testing and evaluation — adversarial | MS-2.5 | MEASURE | Adversarial testing programme validates model resilience to prompt injection at each release |
| Risk response — incident | MG-2.2 | MANAGE | Defined incident response procedures for detected prompt injection attacks |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish and document organisational policy requiring
  input validation and prompt structure enforcement for all LLM
  deployments — include in AI system governance charter
- MP-2.3: Categorise prompt injection as Critical in your AI risk
  register — assign ownership, treatment timelines, and review cadence
- Treat all external content processed by the model as untrusted —
  policy enforced, not just best effort

**Hardening**
- MS-2.5: Include prompt injection scenarios in your adversarial
  evaluation programme — test direct, indirect, and jailbreak vectors
  before each production release
- MG-2.2: Define and test incident response runbooks for prompt
  injection detection — who is notified, what is isolated, how is
  impact assessed
- Implement runtime monitoring for prompt injection indicators —
  feed alerts into your AI incident management workflow

**Advanced**
- MS-2.5: Extend adversarial testing to cover your specific RAG
  sources, tool descriptors, and email/document processing pipelines
- MG-2.2: Establish automated response — quarantine affected
  sessions, notify owners, trigger forensic capture on injection
  detection signals
- GV-1.7: Include prompt injection risk treatment in board-level
  AI risk reporting

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| NIST AI RMF Playbook | Reference | https://airc.nist.gov/Docs/2 |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage
- Other frameworks: MITRE ATLAS AML.T0051 · NIST CSF 2.0 PR.AC-5 · ISO 42001 6.1.2

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, proprietary code, or confidential
information through outputs — from training data memorisation,
over-permissive RAG retrieval, or improperly sanitised responses.
The AI RMF addresses this through data governance policies, privacy
risk measurement, and managed data protection controls.

**Real-world references:**
- Samsung source code leak (2023)
- Multiple healthcare LLM deployments surfacing PHI through
  over-permissive RAG retrieval (2024)

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Organisational policies for data privacy in AI systems — classification, handling, and disclosure controls |
| Risk categorisation | MP-2.3 | MAP | Sensitive information disclosure categorised and risk-rated in AI system risk register |
| Testing — data leakage | MS-2.6 | MEASURE | Evaluation programme includes data leakage and privacy disclosure testing |
| Risk response — data | MG-2.4 | MANAGE | Defined procedures for responding to sensitive data disclosure incidents |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish data classification policy covering all data
  used in LLM training, fine-tuning, and RAG — define handling
  requirements per classification level
- MP-2.3: Include sensitive information disclosure in your AI risk
  register — map to specific data assets and RAG sources at risk
- Implement output scanning for PII and sensitive patterns before
  responses reach users — enforce as a policy requirement, not optional

**Hardening**
- MS-2.6: Include data leakage scenarios in your AI evaluation
  programme — test training data memorisation, RAG over-retrieval,
  and output redaction effectiveness
- MG-2.4: Define incident response for data disclosure — notification
  timelines, regulatory reporting obligations, user notification
- Audit RAG access controls per sprint — verify that retrieval scope
  matches the authorised user's data access rights

**Advanced**
- MS-2.6: Conduct model inversion and membership inference red team
  exercises to validate that sensitive training data cannot be
  reconstructed from model outputs
- GV-1.6: Extend data governance policies to cover derived data —
  embeddings, indexes, summaries — not just source data
- MG-2.4: Implement machine unlearning readiness — versioned
  data-to-model linkage enabling targeted retraining on erasure request

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Private AI | Commercial | https://private-ai.com |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.2 · ISO 27701 · EU AI Act Art. 10 · PCIDSS Req 3

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets,
libraries, and plugins — any of which can be compromised to introduce
backdoors or malicious functionality. The AI RMF addresses this through
supply chain risk governance, dependency mapping, and third-party
risk management.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Supply chain data governance — policies for third-party model and data provenance |
| Interdependencies | MP-5.1 | MAP | Mapping of all AI system dependencies including third-party models, datasets, and libraries |
| Testing and evaluation | MS-2.5 | MEASURE | Evaluation programme includes supply chain component integrity testing |
| Residual risk — third party | MG-3.2 | MANAGE | Residual risk from third-party components documented, monitored, and treated |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish AI supply chain policy — approved sources for
  model weights, datasets, and libraries, with sign-off requirements
  before production use
- MP-5.1: Maintain a complete ML SBOM (Software Bill of Materials)
  for every production AI system — model, adapters, datasets, libraries
- Pin all dependency versions — never pull latest in production
  without review and sign-off

**Hardening**
- MS-2.5: Include supply chain integrity testing in your evaluation
  programme — verify signatures, scan for backdoors, validate
  provenance before each deployment
- MG-3.2: Document and treat residual risk from all third-party
  components — include in AI risk register with review cadence
- Implement automated SBOM generation and drift detection — alert
  on any unplanned component change

**Advanced**
- MP-5.1: Extend dependency mapping to cover runtime dynamic
  components — MCP servers, plugins, and tools fetched at inference
- MS-2.5: Conduct backdoor detection using neural cleanse or
  equivalent on all new model versions before production
- GV-1.6: Establish responsible disclosure relationships with model
  and tool providers — ensure supply chain vulnerability reporting
  path is defined and tested

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · MITRE ATLAS AML.T0056 · CycloneDX ML SBOM

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Attackers corrupt training data or fine-tuning pipelines to embed
backdoors or bias model behaviour in ways baked into the weights and
invisible to standard testing. The AI RMF addresses this as a core
data quality and adversarial evaluation requirement.

**Real-world references:**
- Nightshade (2023) — poison pixels successfully corrupted image
  generation model behaviour
- Adversarial examples achieving 35% influence on model outputs
  despite defensive mechanisms

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | Data and model poisoning categorised as Critical in AI risk register |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing specifically covering poisoning detection in training pipelines |
| Data quality | MS-3.3 | MEASURE | Data quality measurement and validation applied to all training and fine-tuning data |
| Risk response | MG-2.2 | MANAGE | Defined response procedures including model rollback for detected poisoning events |

#### Mitigations by tier

**Foundational**
- MS-3.3: Implement data quality measurement on all training data —
  anomaly detection, source validation, and lineage tracking before
  any training run
- MP-2.3: Include data poisoning in your AI risk register with
  specific treatment controls assigned to training pipeline owners
- Implement source allowlisting for training data — only approved,
  validated sources enter training pipelines

**Hardening**
- MS-2.5: Include poisoning detection in your adversarial evaluation
  programme — test for backdoor triggers and biased outputs on each
  model version before promotion
- MG-2.2: Establish model rollback capability — versioned model
  registry with ability to revert to a known-clean checkpoint on
  poisoning detection
- Apply differential privacy during training to limit the influence
  of any single training example

**Advanced**
- MS-2.5: Conduct post-training backdoor detection using neural
  cleanse or equivalent as a standard pre-deployment gate
- MS-3.3: Implement continuous training data monitoring — alert on
  statistical drift in data distribution that may indicate poisoning
- GV-1.6: Establish dataset governance policy — all training data
  must have documented provenance, approval, and quality attestation

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 · ISO 42001 6.1.2 · NIST CSF 2.0 PR.DS-8

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM-generated output passed to downstream components without
validation enables XSS, command injection, SSRF, or SQL injection
via AI-generated content. The AI RMF addresses this through output
evaluation requirements and managed response to output-related incidents.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Testing — output safety | MS-2.5 | MEASURE | Output handling security included in AI evaluation and testing programme |
| Testing — data leakage | MS-2.6 | MEASURE | Output leakage and injection scenarios covered in evaluation |
| Risk response | MG-2.2 | MANAGE | Incident response for output handling failures defined and tested |
| Policies for trustworthy AI | GV-1.7 | GOVERN | Organisational policy requires secure output handling for all LLM integrations |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy requiring all LLM outputs to be treated
  as untrusted input by downstream systems — encoding, validation,
  and sanitisation mandatory before rendering or execution
- MS-2.5: Include output injection scenarios in your AI evaluation
  programme — XSS, SQL injection, command injection via LLM output
- Never pass raw LLM output directly to database queries, shell
  commands, or eval functions — policy enforced at code review

**Hardening**
- MS-2.6: Test output sanitisation effectiveness as part of
  every release evaluation — not just at initial deployment
- MG-2.2: Define incident response for output injection events —
  what is isolated, how is impact assessed, what is user notification
- Implement output schema validation — define and enforce the
  structure of acceptable model responses per integration point

**Advanced**
- MS-2.5: Conduct DAST (Dynamic Application Security Testing) on
  all interfaces that consume LLM output — include in CI/CD pipeline
- Deploy dedicated output security layer between LLM and all
  downstream consumers, independent of the model
- GV-1.7: Include output security requirements in AI procurement
  standards — vendors must demonstrate output handling controls

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: OWASP ASVS V5 · NIST CSF 2.0 PR.DS-5 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs granted excessive autonomy over tools, APIs, and systems execute
unintended or harmful actions when manipulated. The AI RMF addresses
this through governance of AI decision authority, human oversight
requirements, and managed response to autonomous action incidents.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Organisational policy defines and enforces limits on AI system autonomy and decision authority |
| Risk categorisation | MP-2.3 | MAP | Excessive agency risks mapped to specific tool and API integrations in the risk register |
| Testing — adversarial | MS-2.5 | MEASURE | Autonomy boundary testing included in adversarial evaluation programme |
| Risk response | MG-2.2 | MANAGE | Defined response for unauthorised autonomous actions including rollback and notification |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish AI autonomy policy — define the maximum
  decision authority permitted for each LLM deployment, requiring
  human approval for irreversible or high-impact actions
- MP-2.3: Map all tool and API integrations to risk levels — include
  in AI risk register with least-privilege controls assigned
- Implement and enforce a tool permission manifest for every LLM
  deployment — reviewed and signed off before each release

**Hardening**
- MS-2.5: Test autonomy boundaries as part of each release
  evaluation — verify that the model cannot exceed its defined
  permission scope even under adversarial input
- MG-2.2: Establish automated response to detected unauthorised
  autonomous actions — session isolation, owner notification,
  action rollback where feasible
- Log all tool invocations with full parameter capture — feed into
  AI risk monitoring programme

**Advanced**
- GV-1.7: Include AI autonomy limits in board-level AI governance
  reporting — autonomous action scope changes require executive
  sign-off
- MS-2.5: Conduct red team exercises specifically targeting
  excessive agency through indirect prompt injection
- Formally specify permitted action graphs — only pre-approved
  action sequences can execute in production

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006 · MITRE ATLAS AML.T0015 · ISA/IEC 62443 SR 2.1 (OT)

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic, or
security controls are extracted by adversaries — enabling targeted
attacks against specific defences. The AI RMF addresses this through
confidentiality policies, configuration security testing, and
managed disclosure response.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | System prompts classified as sensitive configuration — subject to data governance policy |
| Testing — data leakage | MS-2.6 | MEASURE | Prompt extraction scenarios included in evaluation programme |
| Risk response — data | MG-2.4 | MANAGE | Defined response for detected system prompt leakage |
| Risk categorisation | MP-2.3 | MAP | System prompt leakage risk mapped and rated in AI risk register |

#### Mitigations by tier

**Foundational**
- GV-1.6: Classify system prompts as sensitive configuration
  artefacts — version controlled, access controlled, and reviewed
  on every change
- Never embed credentials, API keys, or sensitive data in system
  prompts — use environment variables and secret managers, enforced
  by policy
- MP-2.3: Include system prompt leakage in AI risk register with
  specific extraction scenario testing assigned

**Hardening**
- MS-2.6: Include prompt extraction scenarios in your evaluation
  programme — test against your specific deployment before go-live
  and after each system prompt change
- MG-2.4: Define response to detected prompt leakage — prompt
  rotation, impact assessment, downstream attack monitoring
- Implement output monitoring to detect response patterns indicative
  of system prompt disclosure

**Advanced**
- MS-2.6: Conduct adversarial prompt extraction red team exercises
  covering all known techniques against your specific deployment
- Deploy output classifiers trained to detect and block responses
  containing system prompt content
- GV-1.6: Treat system prompt design as a security design review
  artefact — include in your SDLC security gates

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · MITRE ATLAS AML.T0041 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in embedding stores enable adversarial retrieval
manipulation, inference of sensitive information from embeddings,
and semantic search poisoning. The AI RMF addresses this through
data quality measurement and adversarial evaluation of retrieval
systems.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Testing — adversarial | MS-2.5 | MEASURE | Vector store and embedding adversarial testing included in evaluation programme |
| Data quality | MS-3.3 | MEASURE | Data quality controls applied to embedding generation and vector store ingestion |
| Risk response | MG-2.2 | MANAGE | Response procedures for detected vector store compromise or manipulation |
| Risk categorisation | MP-2.3 | MAP | Embedding and vector store risks mapped in AI system risk register |

#### Mitigations by tier

**Foundational**
- MS-3.3: Apply data quality validation to all content before
  embedding generation — garbage-in to vector stores is a security
  risk, not just a quality issue
- Implement access controls on vector store read and write operations —
  enforce through policy and technical controls
- Classify all embedding stores as sensitive data assets in your
  AI risk register

**Hardening**
- MS-2.5: Include embedding manipulation scenarios in your
  adversarial evaluation programme — test retrieval poisoning
  and adversarial query scenarios
- Encrypt embedding vectors at rest and in transit — embeddings
  can leak source content information through inversion attacks
- Implement anomaly detection on vector store ingestion and
  query patterns

**Advanced**
- MS-2.5: Conduct embedding inversion red team exercises to
  validate that your embeddings do not reconstruct source content
- Apply differential privacy in embedding generation for sensitive
  corpora — measure privacy budget consumption
- MG-2.2: Establish vector store integrity monitoring with
  automated alerts on anomalous content injection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: AIUC-1 A · MITRE ATLAS AML.T0063 · NIST CSF 2.0 PR.DS-7

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but factually incorrect content that users
or downstream systems act upon. The AI RMF addresses this through
accuracy measurement requirements, feedback mechanisms, and
governance of AI-generated content quality.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Organisational policy on AI-generated content accuracy and human oversight requirements |
| Testing — output quality | MS-2.6 | MEASURE | Accuracy and hallucination testing included in AI evaluation programme |
| Feedback mechanisms | MS-4.1 | MEASURE | Feedback channels for detecting and tracking misinformation in production |
| Risk response — data | MG-2.4 | MANAGE | Procedures for responding to detected misinformation incidents |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy on AI content accuracy — define domains
  where AI output requires human verification before action,
  especially medical, legal, financial, and safety-critical contexts
- MS-2.6: Include hallucination and accuracy testing in your AI
  evaluation programme — benchmark against your specific use case
  domains before deployment
- Display source citations alongside model responses — policy
  requirement for all public-facing LLM deployments

**Hardening**
- MS-4.1: Implement feedback mechanisms for production misinformation
  detection — user reporting, automated fact-checking, output quality
  metrics fed back into risk monitoring
- MG-2.4: Define incident response for misinformation events —
  severity thresholds, correction procedures, user notification
- Deploy RAG grounded on verified, up-to-date sources for domains
  where accuracy is critical

**Advanced**
- MS-2.6: Build automated fact-checking pipelines for high-stakes
  output domains — measure and track hallucination rates per domain
- MS-4.1: Implement continuous accuracy monitoring in production
  with drift detection — alert when hallucination rates exceed
  defined thresholds
- GV-1.7: Include AI content accuracy in board-level AI risk
  reporting for regulated industries

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13 · AIUC-1 F · ENISA AI Threat Landscape

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption —
CPU, memory, tokens, API costs — causing denial of service or
runaway cost. The AI RMF addresses this through operational
resilience governance, resource limit measurement, and managed
response to availability incidents.

#### NIST AI RMF mapping

| Subcategory | ID | Function | Description |
|---|---|---|---|
| Testing — adversarial | MS-2.5 | MEASURE | Resource exhaustion and denial-of-service scenarios included in adversarial testing |
| Risk response | MG-2.2 | MANAGE | Defined response to detected unbounded consumption events including rate limiting activation |
| Residual risk — availability | MG-3.2 | MANAGE | Residual availability risk from resource exhaustion documented and treated |
| Policies for trustworthy AI | GV-1.7 | GOVERN | Organisational policy defines resource limits and availability requirements for all LLM deployments |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish resource governance policy — define token
  limits, rate limits, and cost budgets for every LLM deployment
  as a mandatory deployment requirement
- Implement rate limiting per user, session, and API key at the
  application layer — enforced before requests reach the model
- MS-2.5: Include resource exhaustion scenarios in adversarial
  testing — sponge example attacks and token amplification

**Hardening**
- MG-2.2: Define automated response to consumption anomalies —
  rate limit tightening, session suspension, owner notification,
  cost circuit breakers
- MG-3.2: Document residual availability risk in your AI risk
  register — define acceptable recovery time objectives (RTO) and
  recovery point objectives (RPO) for LLM services
- Implement per-tenant cost budgets with automatic suspension
  on breach — not just alerting

**Advanced**
- MS-2.5: Conduct adversarial cost-maximisation testing against
  your specific deployment — identify the inputs that generate
  maximum token consumption for your model and guard those paths
- GV-1.7: Include availability SLAs and cost governance in AI
  operational policy — reviewed quarterly against actual consumption
- Implement adaptive rate limiting with real-time system load
  awareness — thresholds adjust dynamically under attack conditions

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.1 (OT) · NIST SP 800-82 (OT) · CWE-400

---

## Implementation priority aligned to AI RMF

| Phase | GV — Govern | MP — Map | MS — Measure | MG — Manage |
|---|---|---|---|---|
| 1 — Now | GV-1.7 autonomy and input policy | MP-2.3 risk register all 10 entries | MS-2.5 adversarial testing LLM01/04/06 | MG-2.2 incident response LLM01/04 |
| 2 — This sprint | GV-1.6 data classification policy | MP-5.1 SBOM and dependency mapping | MS-2.6 output and leakage testing | MG-2.4 data incident response |
| 3 — This quarter | All GV policies reviewed and approved | MP-2.3 full risk register complete | MS-3.3 data quality controls live | MG-3.2 residual risk documentation |
| 4 — Ongoing | Board-level AI risk reporting | Dependency map refreshed quarterly | MS-4.1 production feedback loops | All MG procedures exercised |

---

## AI RMF profiles

The NIST AI RMF supports the creation of AI risk profiles —
current state vs target state assessments. For LLM deployments,
a starter profile mapping all 10 OWASP entries to AI RMF subcategories
is available at:
`data/llm-top10/nist-aiRMF-profile.json`

This can be used directly in AI RMF-aligned governance programmes
and compliance assessments.

---

## References

- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [NIST AI RMF Playbook](https://airc.nist.gov/Docs/2)
- [NIST Trustworthy and Responsible AI Resource Center](https://airc.nist.gov)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [NIST SP 800-218A — Secure Software Development for AI](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)
- [Executive Order 14110 on Safe, Secure, and Trustworthy AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
