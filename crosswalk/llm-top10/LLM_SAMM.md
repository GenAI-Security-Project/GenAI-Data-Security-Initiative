<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : OWASP SAMM v2.0 — Software Assurance Maturity Model
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × OWASP SAMM v2.0

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [OWASP Software Assurance Maturity Model (SAMM) v2.0](https://owaspsamm.org/) —
the framework for measuring and improving software security programme
maturity across the software development lifecycle.

---

## Why SAMM for LLM security

SAMM is the practitioner's framework for software security — it
answers not just "what controls are needed?" but "how mature is
our programme, and what should we improve next?" For LLM applications,
SAMM provides three things that other frameworks do not:

**Maturity measurement:** SAMM's three maturity levels (1–3) per
practice allow teams to assess their current LLM security posture
and define a target maturity. Level 1 is the minimum acceptable
baseline; Level 3 is optimised and proactive.

**Development lifecycle integration:** SAMM organises practices
across the SDLC — Design, Implementation, Verification, Operations.
LLM security risks map directly to SAMM practices at every lifecycle
phase — from threat modelling in Design through penetration testing
in Verification through incident detection in Operations.

**Continuous improvement roadmap:** SAMM's maturity model gives
security teams a roadmap for improving LLM security programme
maturity over time, not just a point-in-time control checklist.

---

## SAMM v2.0 structure

SAMM organises security into 5 Business Functions, each containing
3 Security Practices, each with 2 Streams:

| Business Function | Security Practices |
|---|---|
| Governance (G) | Strategy & Metrics · Policy & Compliance · Education & Guidance |
| Design (D) | Threat Assessment · Security Requirements · Security Architecture |
| Implementation (I) | Secure Build · Secure Deployment · Defect Management |
| Verification (V) | Architecture Assessment · Requirements-Driven Testing · Security Testing |
| Operations (O) | Incident Management · Environment Management · Operational Management |

**Maturity levels:**
- Level 1 — Initial/Ad-hoc: Basic security practices, reactive
- Level 2 — Managed: Defined processes, consistent execution
- Level 3 — Optimised: Proactive, metrics-driven, continuously improving

---

## Quick-reference summary

| ID | Name | Severity | Primary SAMM Practices | Maturity Target | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | D-TA, I-SB, V-ST, O-IM | L2 minimum / L3 for high-risk | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | D-SR, I-SB, V-RT, O-OM | L2 minimum | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | G-PC, I-SB, V-AA | L2 minimum | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | D-TA, I-SB, V-ST, O-IM | L2 minimum / L3 for high-risk | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | D-SR, I-SB, V-RT, V-ST | L1 minimum / L2 target | Foundational–Hardening |
| LLM06 | Excessive Agency | High | D-TA, D-SA, G-SM, O-OM | L2 minimum | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | D-SR, I-SB, V-ST | L1 minimum / L2 target | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | D-TA, I-SB, V-ST | L2 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | G-EG, D-SR, V-RT, O-OM | L1 minimum / L2 target | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | D-SR, I-SD, O-IM, O-EM | L1 minimum / L2 target | Foundational–Hardening |

**SAMM practice codes:**
G-SM = Governance / Strategy & Metrics ·
G-PC = Governance / Policy & Compliance ·
G-EG = Governance / Education & Guidance ·
D-TA = Design / Threat Assessment ·
D-SR = Design / Security Requirements ·
D-SA = Design / Security Architecture ·
I-SB = Implementation / Secure Build ·
I-SD = Implementation / Secure Deployment ·
V-AA = Verification / Architecture Assessment ·
V-RT = Verification / Requirements-Driven Testing ·
V-ST = Verification / Security Testing ·
O-IM = Operations / Incident Management ·
O-EM = Operations / Environment Management ·
O-OM = Operations / Operational Management

---

## Audience tags

- **Security programme lead** — full file, SAMM maturity roadmap for LLM security
- **AppSec engineer** — Implementation and Verification practice entries
- **Security architect** — Design practice entries
- **CISO** — Governance practice entries, maturity scorecard
- **Developer** — I-SB (Secure Build) entries per vulnerability
- **Auditor** — maturity level mapping for programme assessment

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour. Prompt injection maps across the full SAMM lifecycle —
from threat modelling (Design) through secure coding (Implementation)
through adversarial testing (Verification) through incident response
(Operations).

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Threat Assessment (D-TA) | Threat Modelling | L2 | LLM data flows threat-modelled — all injection paths (direct, indirect, multi-turn) identified and documented |
| Secure Build (I-SB) | Security of Build Pipeline | L1 | Input validation and context separation as secure build requirements — reviewed in CI/CD before merge |
| Security Testing (V-ST) | Adversarial Testing | L2 | Adversarial testing programme covering prompt injection — direct, indirect, RAG-specific, jailbreak scenarios |
| Incident Management (O-IM) | Incident Detection | L2 | Runtime injection detection as operational monitoring — alerts integrated into incident management |

#### Maturity roadmap

**Level 1 — Initial**
- D-TA: Add prompt injection to threat model as an
  explicit threat category for all LLM-integrated
  applications — document injection paths even informally
- I-SB: Implement input validation in code — all LLM
  integrations treat external content as untrusted,
  reviewed in code review before merge
- Document injection as a security requirement for
  all new LLM features before development begins

**Level 2 — Managed**
- D-TA: Formal threat modelling for all LLM applications —
  all indirect injection surfaces documented, mitigations
  mapped to each path, residual risk accepted
- V-ST: Defined adversarial testing programme — injection
  scenarios in test plan, results tracked across releases,
  regressions prevented
- O-IM: Runtime injection monitoring as operational
  control — alerts generated, incident response defined

**Level 3 — Optimised**
- V-ST: Automated adversarial testing in CI/CD —
  injection test suite runs on every PR to LLM-integrated
  code, blocking merge on new vulnerabilities
- O-IM: Injection incident metrics drive programme
  improvement — attack patterns, detection rates,
  response times measured and improved quarterly
- D-TA: Threat model updated when new injection
  techniques emerge — proactive rather than reactive

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| Promptfoo | Open-source | https://github.com/promptfoo/promptfoo |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · NIST CSF 2.0 PR.PS-04 · OWASP ASVS V5.1

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, or confidential information through
outputs. SAMM Design (Security Requirements) and Verification
(Requirements-Driven Testing) govern data protection as a requirements
and testing concern throughout the SDLC.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Security Requirements (D-SR) | Software Requirements | L1 | Data classification and handling requirements defined for all LLM-integrated applications before development |
| Secure Build (I-SB) | Security of Code | L1 | Output redaction and DLP implemented in code — LLM output scanned before delivery, reviewed in build |
| Requirements-Driven Testing (V-RT) | Control Verification | L2 | Data protection requirements verified in testing — PII patterns confirmed not to appear in LLM outputs |
| Operational Management (O-OM) | Data Protection | L2 | Production DLP monitoring on LLM output channels — operational data protection as ongoing practice |

#### Maturity roadmap

**Level 1 — Initial**
- D-SR: Define data classification requirements for
  LLM applications — which data enters the model,
  what handling requirements apply, what must not
  appear in outputs
- I-SB: Implement output redaction in code — PII
  and sensitive patterns scanned before delivery,
  reviewed in code review as security requirement

**Level 2 — Managed**
- V-RT: Verify data protection requirements in testing —
  test cases confirm PII cannot be extracted from
  model outputs, results tracked across releases
- O-OM: Production DLP monitoring on all LLM output
  channels — operational data protection, not just
  development-time controls

**Level 3 — Optimised**
- V-RT: Automated data leakage testing in CI/CD —
  PII detection tests run on LLM outputs in pipeline
- O-OM: Data disclosure incident metrics drive
  programme improvement — disclosure patterns,
  detection rates, response times measured and
  improved quarterly
- Apply differential privacy for sensitive training
  corpora — L3 proactive privacy engineering practice

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.11/A.8.12 · NIST AI RMF GV-1.6 · EU AI Act Art. 10

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets, and
plugins. SAMM Governance (Policy & Compliance) and Implementation
(Secure Build) govern supply chain security as a policy and build
pipeline concern.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Policy & Compliance (G-PC) | Supplier Security | L2 | Supply chain security policy covers LLM component vendors — security requirements in procurement |
| Secure Build (I-SB) | Security of Build Pipeline | L2 | ML SBOM maintained, CVE scanning in CI/CD — LLM components verified before each deployment |
| Architecture Assessment (V-AA) | Architecture Validation | L2 | LLM supply chain architecture reviewed — trust boundaries and component integrity verified |

#### Maturity roadmap

**Level 1 — Initial**
- I-SB: Maintain ML SBOM and pin component versions —
  every LLM component inventoried with version and
  source, no automatic updates without review
- G-PC: Define basic supplier security requirements
  for LLM component vendors — provenance, disclosure
  obligations before any component enters production

**Level 2 — Managed**
- I-SB: CVE scanning in CI/CD for all LLM components —
  ML library vulnerabilities block deployment when
  critical, patching process defined
- G-PC: Supplier security policy covers AI supply
  chain — contracts include security obligations,
  periodic assessments for strategic vendors
- V-AA: Architecture review includes LLM supply chain —
  trust boundaries, component integrity, runtime loading
  patterns assessed

**Level 3 — Optimised**
- I-SB: Automated supply chain integrity verification —
  cryptographic signature validation in CI/CD pipeline,
  unsigned components blocked automatically
- G-PC: Metrics-driven supplier security programme —
  vendor security posture tracked, incidents measured,
  programme improved based on data

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Grype | Open-source | https://github.com/anchore/grype |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST CSF 2.0 GV.SC-01 · ISO 27001 A.5.19/A.5.21 · NIST SP 800-218A

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Adversaries corrupt training data or model weights. SAMM Design
(Threat Assessment) is the starting point — poisoning must be in
the threat model before any other control can be effectively
designed. Verification (Security Testing) provides the adversarial
testing practice that detects it.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Threat Assessment (D-TA) | Threat Modelling | L2 | Poisoning attack vectors documented in threat model — training data sources, supply chain, fine-tuning pipeline each assessed |
| Secure Build (I-SB) | Security of Build Pipeline | L2 | Training data integrity controls in build pipeline — source allowlisting, anomaly detection, provenance tracking |
| Security Testing (V-ST) | Adversarial Testing | L2 | Poisoning detection in adversarial testing — backdoor trigger testing before each model promotion |
| Incident Management (O-IM) | Incident Response | L2 | Poisoning incident response defined — model rollback, affected deployment scope, disclosure procedure |

#### Maturity roadmap

**Level 1 — Initial**
- D-TA: Add poisoning to LLM threat model — document
  which training data sources are potentially adversary-
  influenced, what the consequence is if poisoning succeeds
- I-SB: Implement basic training data integrity —
  source allowlisting, hash verification of training
  datasets before use
- Model rollback capability — clean checkpoint always
  available, procedure documented

**Level 2 — Managed**
- V-ST: Defined poisoning detection testing — backdoor
  trigger scenarios in adversarial test plan, results
  tracked across model versions
- I-SB: Automated training data validation in pipeline —
  anomaly detection on data distributions flags potential
  poisoning before training runs
- O-IM: Poisoning incident response plan — rollback
  procedure tested, affected deployment scope assessment,
  notification checklist

**Level 3 — Optimised**
- V-ST: Post-training backdoor detection as mandatory
  CI/CD gate — neural cleanse or equivalent blocks
  promotion of poisoned models automatically
- O-IM: Poisoning incident metrics drive programme
  improvement — detection rates, response times,
  affected scope measured quarterly
- D-TA: Threat model updated as new poisoning
  techniques emerge — proactive intelligence integration

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0020 · ISO 27001 A.8.27

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
injection attacks. SAMM Design (Security Requirements) and
Implementation (Secure Build) address output handling as a development
requirement — output security must be specified before code is written.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Security Requirements (D-SR) | Software Requirements | L1 | Output encoding and schema validation as explicit security requirements before development |
| Secure Build (I-SB) | Security of Code | L1 | Output validation implemented in code — LLM output treated as untrusted, reviewed in code review |
| Requirements-Driven Testing (V-RT) | Control Verification | L1 | Output security requirements verified in testing — XSS, SQL injection via LLM output tested |
| Security Testing (V-ST) | Penetration Testing | L2 | DAST on all interfaces consuming LLM output as penetration testing activity |

#### Maturity roadmap

**Level 1 — Initial**
- D-SR: Define output security as an explicit
  requirement — LLM output is untrusted input to
  downstream systems, encoded and validated before
  use, documented as security requirement before
  any LLM integration is developed
- I-SB: Implement output encoding in code — no eval,
  no raw LLM output in SQL, shell, or HTML rendering
  context — enforced through code review

**Level 2 — Managed**
- V-RT: Verify output security requirements in
  testing — XSS, SQL injection, command injection
  via LLM output tested systematically before each
  release, results tracked
- V-ST: DAST on all interfaces consuming LLM output
  as defined penetration testing activity — results
  remediated before release

**Level 3 — Optimised**
- V-RT: Automated output injection testing in CI/CD —
  injection scenarios run against LLM output handling
  code on every PR
- V-ST: Output security in red team programme —
  novel injection techniques tested against your
  specific downstream consumers

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: OWASP ASVS V5 · CIS Controls CIS 16 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with excessive autonomy execute unintended or harmful actions.
SAMM Governance (Strategy & Metrics) and Design (Security Architecture)
address excessive agency as a programme governance and architecture
concern — autonomy scope must be a governance decision, not just
a configuration choice.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Strategy & Metrics (G-SM) | Create and Promote | L2 | AI autonomy policy as security programme strategy — acceptable autonomous action scope defined and communicated |
| Security Architecture (D-SA) | Architecture Design | L2 | Least privilege architecture for LLM tool access — action scope enforced by design, not just policy |
| Threat Assessment (D-TA) | Threat Modelling | L2 | Excessive agency threat modelled — what happens if each tool is invoked autonomously with adversarial parameters |
| Operational Management (O-OM) | Operational Monitoring | L2 | All LLM tool invocations logged and monitored — anomalous scope detected as operational control |

#### Maturity roadmap

**Level 1 — Initial**
- G-SM: Define acceptable LLM autonomous action scope —
  basic policy identifying which actions require human
  confirmation, communicated to development teams
- D-SA: Least privilege tool access by design —
  minimum permissions per tool, read-only by default,
  enforced at architecture level not just policy

**Level 2 — Managed**
- D-TA: Formal threat model for LLM autonomous actions —
  each tool's worst-case autonomous invocation documented,
  mitigations designed and implemented
- O-OM: Log and monitor all tool invocations —
  anomalous scope, unusual parameters, high frequency
  detected as operational management control
- Human confirmation gates for irreversible actions —
  architecture-enforced, not model-instruction-dependent

**Level 3 — Optimised**
- G-SM: Metrics-driven autonomy governance — autonomous
  action incidents, confirmation rates, scope violations
  measured and reported in security programme metrics
- D-TA: Threat model updated as agent capabilities
  expand — proactive assessment before each new
  tool or autonomous capability is enabled

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: EU AI Act Art. 14 · AIUC-1 B006 · ISO 42001 A.6.1.2

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing security controls are extracted by adversaries.
SAMM Design (Security Requirements) and Implementation (Secure Build)
address system prompt security as a requirements and code security
concern.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Security Requirements (D-SR) | Software Requirements | L1 | System prompt security as explicit requirement — confidentiality, encryption, access control specified before development |
| Secure Build (I-SB) | Security of Code | L1 | System prompt protection implemented in code — no cleartext storage, version control access restrictions |
| Security Testing (V-ST) | Penetration Testing | L2 | Prompt extraction testing as penetration testing activity — resistance to known extraction techniques verified |

#### Maturity roadmap

**Level 1 — Initial**
- D-SR: Define system prompt security requirements —
  classification, encryption requirements, access
  control documented before any LLM application
  is developed
- I-SB: Implement system prompt protection in code —
  no hardcoded prompts in source, secret manager
  required, enforced in code review

**Level 2 — Managed**
- V-ST: Prompt extraction testing in security testing
  programme — known extraction techniques tested
  before each deployment, results tracked

**Level 3 — Optimised**
- V-ST: Automated prompt confidentiality testing —
  extraction attempts in CI/CD pipeline
- I-SB: System prompt tokenisation as advanced
  build practice — sensitive identifiers replaced
  with opaque tokens in build pipeline

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · ISO 27001 A.5.12 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Vector stores are susceptible to adversarial retrieval and inference
attacks. SAMM Design (Threat Assessment) and Verification (Security
Testing) address embedding security as a design-time threat and
verification-time testing concern.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Threat Assessment (D-TA) | Threat Modelling | L2 | Vector store attack surface threat-modelled — RBAC bypass, embedding inversion, bulk extraction documented |
| Secure Build (I-SB) | Security of Code | L1 | RBAC and encryption implemented for all vector stores — security requirements enforced in code |
| Security Testing (V-ST) | Penetration Testing | L2 | Vector store attacks in penetration testing — RBAC bypass, CVE-2024-3584 class, embedding inversion tested |

#### Maturity roadmap

**Level 1 — Initial**
- I-SB: RBAC and encryption as build requirements
  for all vector stores — no unauthenticated access
  in any environment, enforced in code review

**Level 2 — Managed**
- D-TA: Vector store threat model — RBAC bypass,
  path traversal, embedding inversion, bulk extraction
  all documented as threats with mitigations designed
- V-ST: Vector store attacks in defined penetration
  testing programme — results tracked, CVEs patched
  as urgent findings

**Level 3 — Optimised**
- V-ST: Embedding inversion testing in red team
  programme — validate sensitive source content
  cannot be reconstructed under realistic conditions

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · ISO 27001 A.8.3/A.8.24 · CWE-284

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but incorrect content. SAMM Governance
(Education & Guidance) and Design (Security Requirements) address
misinformation as both a training concern and a requirements concern
— accuracy requirements must be specified and users must be trained.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Education & Guidance (G-EG) | Training & Awareness | L1 | All users of LLM decision-support tools trained on output limitations — SAMM awareness practice applied to AI limitations |
| Security Requirements (D-SR) | Software Requirements | L1 | Accuracy thresholds as security requirements — domains requiring verification documented before development |
| Requirements-Driven Testing (V-RT) | Control Verification | L2 | Accuracy requirements verified in testing — hallucination rates measured against thresholds per domain |
| Operational Management (O-OM) | Monitoring | L2 | Production accuracy monitoring as operational management — drift detection, degradation alerted |

#### Maturity roadmap

**Level 1 — Initial**
- G-EG: Train all LLM decision-support users on
  output limitations — mandatory before access
  granted, documented as SAMM awareness practice
- D-SR: Define accuracy thresholds as security
  requirements — which domains require verification
  before action, what constitutes acceptable accuracy

**Level 2 — Managed**
- V-RT: Verify accuracy requirements in testing —
  hallucination rates measured against thresholds
  per domain before each release, results tracked
- O-OM: Production accuracy monitoring — drift
  detected, degradation alerted as operational control

**Level 3 — Optimised**
- O-OM: Accuracy incident metrics drive programme —
  hallucination rates per domain, correction response
  times measured and improved quarterly
- V-RT: Automated accuracy regression testing —
  domain-specific test suites run in CI/CD

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 F · ENISA GOV

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption.
SAMM Design (Security Requirements), Implementation (Secure Deployment),
and Operations (Incident Management, Environment Management) address
resource exhaustion as a requirements, deployment, and operational concern.

#### SAMM practice mapping

| Practice | Stream | Maturity | How it applies |
|---|---|---|---|
| Security Requirements (D-SR) | Software Requirements | L1 | Rate limiting and resource caps as security requirements — specified before LLM infrastructure deployment |
| Secure Deployment (I-SD) | Deployment Process | L1 | Rate limiting and resource controls deployed with every LLM deployment — not optional post-deployment hardening |
| Incident Management (O-IM) | Incident Detection | L1 | Consumption anomaly detection as incident management control — automated response, escalation procedure |
| Environment Management (O-EM) | Configuration Management | L2 | Resource limits as environment configuration — documented, version-controlled, reviewed on change |

#### Maturity roadmap

**Level 1 — Initial**
- D-SR: Define rate limiting and resource caps as
  security requirements — hard token limits, per-user
  budgets, cost caps documented before deployment
- I-SD: Rate limiting and resource controls deployed
  in every LLM deployment — enforced at API gateway,
  not optional post-deployment configuration
- O-IM: Basic consumption anomaly detection —
  alert on unusual resource usage, defined escalation

**Level 2 — Managed**
- O-EM: Resource limits as managed environment
  configuration — documented, version-controlled,
  reviewed on change, same rigour as security configuration
- O-IM: Defined incident response for consumption
  events — automated rate tightening, cost circuit
  breakers, owner notification workflow

**Level 3 — Optimised**
- O-IM: Consumption incident metrics drive programme —
  attack patterns, impact, response times measured
  and reported in security programme metrics
- V-ST: Adversarial load testing in security testing
  programme — sponge example attacks tested before
  each production deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: NIST CSF 2.0 PR.IR-01 · CIS Controls CIS 4 · CWE-400

---

## SAMM scorecard for LLM security

Use this scorecard to assess current LLM security programme maturity
and define a target state:

| SAMM Practice | Current Level | Target Level | LLM entries covered |
|---|---|---|---|
| Threat Assessment (D-TA) | __ | __ | LLM01, LLM04, LLM06, LLM08 |
| Security Requirements (D-SR) | __ | __ | LLM02, LLM05, LLM07, LLM09, LLM10 |
| Security Architecture (D-SA) | __ | __ | LLM06 |
| Secure Build (I-SB) | __ | __ | LLM01, LLM02, LLM03, LLM04, LLM05, LLM07, LLM08 |
| Secure Deployment (I-SD) | __ | __ | LLM10 |
| Architecture Assessment (V-AA) | __ | __ | LLM03 |
| Requirements-Driven Testing (V-RT) | __ | __ | LLM02, LLM05, LLM09 |
| Security Testing (V-ST) | __ | __ | LLM01, LLM04, LLM07, LLM08, LLM10 |
| Incident Management (O-IM) | __ | __ | LLM01, LLM04, LLM10 |
| Environment Management (O-EM) | __ | __ | LLM10 |
| Operational Management (O-OM) | __ | __ | LLM02, LLM06, LLM09 |
| Strategy & Metrics (G-SM) | __ | __ | LLM06 |
| Policy & Compliance (G-PC) | __ | __ | LLM03 |
| Education & Guidance (G-EG) | __ | __ | LLM09 |

**Minimum viable maturity for any LLM production deployment:**

| Practice | Minimum level | Key activity |
|---|---|---|
| D-TA | L1 | Injection and poisoning in threat model |
| D-SR | L1 | Output security, data classification, rate limiting as requirements |
| I-SB | L1 | Input validation, output encoding, component inventory in build |
| I-SD | L1 | Rate limiting deployed with every LLM deployment |
| O-IM | L1 | Injection and consumption incident response defined |
| G-EG | L1 | All LLM users trained on output limitations |

---

## Implementation priority

| Phase | LLM entries | SAMM practices | Rationale |
|---|---|---|---|
| 1 — Design | LLM01, LLM04, LLM06 | D-TA, D-SR, D-SA | Threat model and requirements before code — highest leverage point |
| 2 — Build | LLM01, LLM02, LLM05 | I-SB | Input validation, output encoding, DLP in code — closes most common breach paths |
| 3 — Deploy and monitor | LLM10, LLM09 | I-SD, O-OM, O-IM | Rate limiting deployed, monitoring live, incident response defined |
| 4 — Test | LLM03, LLM04, LLM07 | V-ST, V-AA, V-RT | Supply chain assessment, adversarial testing, requirements verification |
| 5 — Optimise | All | L3 across all practices | Automation, metrics, proactive programme improvement |

---

## References

- [OWASP SAMM v2.0](https://owaspsamm.org/)
- [OWASP SAMM GitHub](https://github.com/owaspsamm/core)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with SAMM maturity scorecard | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
