<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01-DSGAI21)
  Framework   : OWASP SAMM v2.0 — Software Assurance Maturity Model
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × OWASP SAMM v2.0

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [OWASP Software Assurance Maturity Model (SAMM) v2.0](https://owaspsamm.org/) —
the framework for measuring and improving software security programme
maturity across the software development lifecycle.

---

## Why SAMM for GenAI data security

The DSGAI taxonomy documents 21 data-oriented risks that emerge when
organisations build, deploy, and operate GenAI systems. SAMM is the
right lens for these risks because it answers a question that pure
control frameworks cannot: **how mature does our security programme
need to be before we can safely operate these data flows?**

Three SAMM properties are especially valuable for DSGAI:

**Data governance is a SAMM Design problem.** DSGAI's risks — from
training data poisoning (DSGAI02) to RAG corpus manipulation
(DSGAI09) to model weight theft (DSGAI14) — originate in design
decisions made before a single line of production code is written.
SAMM Design practices (D-TA, D-SR, D-SA) provide the structured
approach to catching these risks early.

**Implementation practices determine data pipeline security.** DSGAI
data risks live in pipelines: ingestion, preprocessing, embedding,
training, retrieval. SAMM's Implementation function (I-SB, I-SD)
provides the maturity model for securing these pipelines.

**Operations maturity determines detection and response.** DSGAI
risks often manifest as subtle degradation — poisoned embeddings,
drifting model behaviour — rather than hard failures. SAMM Operations
practices (O-IM, O-OM, O-EM) provide the monitoring and incident
response maturity to detect and respond.

---

## SAMM v2.0 structure

| Business Function | Security Practices |
|---|---|
| Governance (G) | Strategy & Metrics (G-SM) · Policy & Compliance (G-PC) · Education & Guidance (G-EG) |
| Design (D) | Threat Assessment (D-TA) · Security Requirements (D-SR) · Security Architecture (D-SA) |
| Implementation (I) | Secure Build (I-SB) · Secure Deployment (I-SD) · Defect Management (I-DM) |
| Verification (V) | Architecture Assessment (V-AA) · Requirements-Driven Testing (V-RT) · Security Testing (V-ST) |
| Operations (O) | Incident Management (O-IM) · Environment Management (O-EM) · Operational Management (O-OM) |

**Maturity levels:**
- Level 1 — Initial/Ad-hoc: Basic security practices, reactive
- Level 2 — Managed: Defined processes, consistent execution
- Level 3 — Optimised: Proactive, metrics-driven, continuously improving

---

## Quick-reference summary

| ID | Name | Severity | Primary SAMM Practices | Maturity Target | Tier |
|---|---|---|---|---|---|
| DSGAI01 | Prompt Injection via Data Channels | Critical | D-TA, I-SB, V-ST, O-IM | L2 min / L3 high-risk | Foundational–Advanced |
| DSGAI02 | Training Data Poisoning | Critical | D-TA, I-SB, V-ST, O-IM | L2 min / L3 high-risk | Hardening–Advanced |
| DSGAI03 | Sensitive Data in Training Sets | High | D-SR, G-PC, I-SB, V-RT | L2 min | Foundational–Hardening |
| DSGAI04 | Insecure Data Pipelines | High | D-SA, I-SB, I-SD, V-AA | L2 min | Foundational–Hardening |
| DSGAI05 | Guardrail Circumvention | High | D-SA, V-ST, O-IM | L2 min | Hardening–Advanced |
| DSGAI06 | Unintended Data Disclosure | High | D-SR, I-SB, V-ST, O-OM | L2 min | Foundational–Hardening |
| DSGAI07 | Excessive Data Access | High | D-SA, G-SM, V-AA, O-OM | L2 min | Foundational–Hardening |
| DSGAI08 | Data Leakage in Retrieval | High | D-TA, I-SB, V-ST | L2 min | Hardening–Advanced |
| DSGAI09 | RAG Corpus Manipulation | Critical | D-TA, I-SB, V-ST, O-IM | L2 min / L3 high-risk | Hardening–Advanced |
| DSGAI10 | Context Window Poisoning | High | D-TA, I-SB, V-ST | L2 min | Hardening–Advanced |
| DSGAI11 | Session Persistence Attacks | High | D-SA, I-SB, O-EM, V-ST | L2 min | Hardening–Advanced |
| DSGAI12 | Model Inversion and Extraction | High | D-TA, V-ST, O-OM | L2 min | Hardening–Advanced |
| DSGAI13 | Data Leakage through Tool Integration | High | D-SR, I-SB, V-ST, G-PC | L2 min | Foundational–Hardening |
| DSGAI14 | Model Weight Theft | High | D-SA, G-PC, V-AA, O-OM | L2 min | Hardening–Advanced |
| DSGAI15 | Inference Data Exposure | High | D-SR, I-SB, O-EM | L2 min | Foundational–Hardening |
| DSGAI16 | Third-Party Data Dependencies | High | G-PC, I-SB, V-AA | L2 min | Foundational–Hardening |
| DSGAI17 | Model Supply Chain Risks | High | G-PC, I-SB, V-AA, D-TA | L2 min | Foundational–Hardening |
| DSGAI18 | Data Retention and Deletion Failures | Medium | G-PC, D-SR, O-OM | L1 min | Foundational–Hardening |
| DSGAI19 | Cascading Data Failures | High | D-SA, O-IM, O-EM, V-AA | L2 min | Hardening–Advanced |
| DSGAI20 | Regulatory Non-Compliance in Data Use | High | G-PC, G-SM, D-SR, O-OM | L2 min | Foundational–Hardening |
| DSGAI21 | Data Provenance and Lineage Failures | Medium | G-PC, D-SR, O-OM, V-RT | L1 min | Foundational–Hardening |

---

## Target audience

| Role | Files to prioritise |
|---|---|
| Security programme lead | Full file — maturity scorecard for DSGAI programme roadmap |
| Data engineer / ML engineer | Design and Implementation sections per relevant entry |
| AppSec / security engineer | Verification sections; V-ST test cases for data pipelines |
| Compliance / GRC | Governance columns, regulatory alignment notes |
| AI red team | V-ST columns — adversarial data pipeline testing |

---

## Detailed mappings

---

### DSGAI01 — Prompt Injection via Data Channels

Malicious instructions embedded in training data, retrieved documents,
tool outputs, or user-supplied content manipulate model behaviour
or agent execution at inference time.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Data injection surface model | L2 required | Model all channels where untrusted content reaches the model |
| Implementation / Secure Build (I-SB) | A — Build Process | Input sanitisation in data pipelines | L2 required | Enforce sanitisation at every point where external data enters inference pipeline |
| Verification / Security Testing (V-ST) | B — Deep Testing | Data injection test suite | L2 required | Adversarial injection tests across all data input channels |
| Operations / Incident Management (O-IM) | A — Incident Detection | Injection anomaly alerting | L2 required | Alert on unexpected model behaviour correlated with external data retrieval |
| Governance / Education & Guidance (G-EG) | B — Training | Developer training on data injection | L1 minimum | Data engineers understand injection risk surface |

**Maturity target:** L2 minimum; L3 for systems where injection could cause physical harm or regulatory breach.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Audit all external data ingestion points
- Apply content filtering before any external data enters context window
- Log all retrieved content for forensic review

**Tier 2 — Short-term:**
- Build injection test cases into CI/CD pipeline
- Implement trust-level tagging: user input, retrieved content, system prompt — never elevate
- Red team exercise: attempt injection via each data channel

**Tier 3 — Strategic:**
- D-TA L3: threat model updated after every new data source integration
- Continuous monitoring for injection-correlated anomalies in production

#### Cross-references

- LLM Top 10: LLM01 (Prompt Injection)
- Agentic: ASI01 (Prompt Injection in Agentic Systems)
- See also: [DSGAI_AITG.md](../shared/TOOLS.md), [DSGAI_MITREATLAS.md](DSGAI_MITREATLAS.md)

---

### DSGAI02 — Training Data Poisoning

Adversaries corrupt training datasets — through data supply chain
compromise, insider manipulation, or public data contamination —
causing models to learn biased, backdoored, or degraded behaviours.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Training data supply chain threat model | L2 required | Enumerate all sources, custodians, and transformation stages of training data |
| Implementation / Secure Build (I-SB) | A — Build Process | Training data integrity pipeline | L2 required | Hash verification, provenance tracking, and anomaly detection in training data |
| Verification / Security Testing (V-ST) | B — Deep Testing | Backdoor and poisoning detection | L2 required | Statistical analysis and adversarial probing for poisoned behaviours |
| Operations / Incident Management (O-IM) | A — Incident Detection | Model behaviour drift alerting | L2 required | Alert on model output drift that may indicate active poisoning |
| Governance / Policy & Compliance (G-PC) | A — Policy | Training data governance policy | L2 required | Formal policy for data source approval, verification, and chain of custody |

**Maturity target:** L2 minimum; L3 for foundation models or systems where poisoning has safety implications.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Inventory all training data sources; flag unverified or public sources
- Implement hash verification for all training datasets
- Restrict training data write access to authorised personnel only

**Tier 2 — Short-term:**
- Implement data provenance tracking from source to training job
- Add statistical anomaly detection on training data distributions
- V-ST: adversarial probing of fine-tuned models for backdoor triggers

**Tier 3 — Strategic:**
- G-PC L3: formal training data supply chain audit programme
- I-SB L3: automated poisoning detection in ML CI/CD pipeline
- Periodic model re-evaluation against clean held-out dataset

#### Cross-references

- LLM Top 10: LLM04 (Data and Model Poisoning)
- See also: [DSGAI_MITREATLAS.md](DSGAI_MITREATLAS.md), [DSGAI_ISO27001.md](DSGAI_ISO27001.md)

---

### DSGAI03 — Sensitive Data in Training Sets

Personal data, PII, credentials, trade secrets, or regulated
information (PCI, PHI) inadvertently included in training datasets
— leading to model memorisation and potential disclosure at inference.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Requirements (D-SR) | A — Requirements | Training data classification requirements | L2 required | Require data classification check before any dataset enters training pipeline |
| Governance / Policy & Compliance (G-PC) | A — Policy | Data minimisation policy | L2 required | Policy mandating PII/sensitive data removal before training |
| Implementation / Secure Build (I-SB) | A — Build Process | PII detection in data pipeline | L2 required | Automated PII scanning of all training datasets before use |
| Verification / Requirements-Driven Testing (V-RT) | A — Testing | Training data PII scanning tests | L2 required | Automated tests verifying PII detection coverage |
| Operations / Operational Management (O-OM) | A — Monitoring | Memorisation probing | L1 minimum | Periodic probing of deployed models for sensitive data memorisation |

**Maturity target:** L2 minimum; GDPR and CCPA create legal obligations that make G-PC L2 non-negotiable.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Run PII detection scan on all existing training datasets
- Remove or anonymise detected sensitive records
- Establish training data ingestion gate: datasets must pass PII scan before use

**Tier 2 — Short-term:**
- Integrate automated PII scanning into ML CI/CD pipeline
- Implement differential privacy for high-sensitivity training scenarios
- Add memorisation evaluation to model testing suite

**Tier 3 — Strategic:**
- G-PC L3: data governance committee reviews training dataset composition
- Privacy-preserving training techniques (federated learning, synthetic data) for regulated data
- Annual model audit for sensitive data exposure

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- See also: [DSGAI_PCIDSS.md](DSGAI_PCIDSS.md), [DSGAI_EUAIAct.md](DSGAI_EUAIAct.md)

---

### DSGAI04 — Insecure Data Pipelines

Data ingestion, preprocessing, feature extraction, and serving
pipelines lack authentication, integrity controls, or logging —
enabling injection, tampering, or exfiltration of data in transit.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Data pipeline security architecture | L2 required | Design authentication and integrity controls for every pipeline stage |
| Implementation / Secure Build (I-SB) | A — Build Process | Pipeline hardening | L2 required | mTLS, input validation, and access controls enforced across pipeline |
| Implementation / Secure Deployment (I-SD) | A — Deployment | Secure pipeline deployment | L2 required | Infrastructure-as-code with security controls applied at provisioning |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Pipeline architecture review | L2 required | Review every pipeline component for authentication and integrity gaps |
| Operations / Environment Management (O-EM) | A — Patching | Pipeline component patching | L1 minimum | Regular security updates for all pipeline components |

**Maturity target:** L2 minimum; pipeline security architecture review is a pre-production gate.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Audit authentication on all pipeline stage-to-stage connections
- Enable TLS for all pipeline communications
- Add integrity verification at pipeline output (hash of transformed data)

**Tier 2 — Short-term:**
- Implement per-stage audit logging: who accessed what data, when
- Add anomaly detection on data volumes and transformation outputs
- Architecture review: identify and eliminate unauthenticated pipeline endpoints

**Tier 3 — Strategic:**
- I-SB L3: automated security scanning of infrastructure-as-code templates
- O-EM L3: continuous pipeline health monitoring with automated remediation
- Chaos engineering: simulate pipeline component failure and verify containment

#### Cross-references

- LLM Top 10: LLM03 (Supply Chain), LLM08 (Vector and Embedding Weaknesses)
- See also: [DSGAI_ISO27001.md](DSGAI_ISO27001.md), [DSGAI_NISTCSF2.md](DSGAI_NISTCSF2.md)

---

### DSGAI05 — Guardrail Circumvention

Content filters, output validators, and safety classifiers protecting
GenAI system outputs are bypassed through adversarial prompting,
model fine-tuning, or architectural weaknesses, enabling prohibited
content or actions to pass.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Defence-in-depth guardrail design | L2 required | Guardrails at multiple layers: input, generation, output |
| Verification / Security Testing (V-ST) | B — Deep Testing | Guardrail bypass red team | L2 required | Dedicated adversarial testing programme targeting all guardrail bypass vectors |
| Operations / Incident Management (O-IM) | A — Incident Detection | Guardrail bypass alerting | L2 required | Alert on disabled or bypassed guardrails in production |
| Governance / Strategy & Metrics (G-SM) | A — Policy | Guardrail governance | L2 required | Guardrail effectiveness metrics reviewed by security leadership |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Guardrail architecture review | L1 minimum | Pre-deployment review of all guardrail bypass scenarios |

**Maturity target:** L2 minimum; V-ST guardrail bypass testing required before every model update.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Audit all existing guardrails: identify single points of failure
- Confirm guardrails cannot be disabled via input manipulation
- Add immutable logging: guardrail decisions logged and tamper-proof

**Tier 2 — Short-term:**
- Add secondary, rule-based guardrail outside LLM inference path
- V-ST: automated bypass attempt battery in CI/CD for every model change
- Define minimum guardrail effectiveness metric; fail deployment if below threshold

**Tier 3 — Strategic:**
- D-SA L3: independent safety architecture review board for high-risk systems
- Continuous adversarial probing of production guardrails
- G-SM L3: quarterly guardrail effectiveness reporting to leadership

#### Cross-references

- Agentic: ASI08 (Inversion of Safety Controls)
- LLM Top 10: LLM01 (Prompt Injection as bypass vector)
- See also: [DSGAI_ENISA.md](DSGAI_ENISA.md), [DSGAI_EUAIAct.md](DSGAI_EUAIAct.md) Art. 15

---

### DSGAI06 — Unintended Data Disclosure

GenAI systems surface sensitive information — PII, trade secrets,
internal data — in responses through memorisation, over-retrieval,
or insufficient output filtering.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Requirements (D-SR) | A — Requirements | Output data classification requirements | L2 required | Define what categories of data may appear in model outputs |
| Implementation / Secure Build (I-SB) | A — Build Process | Output content inspection | L2 required | Apply DLP scanning to all model outputs before delivery |
| Verification / Security Testing (V-ST) | A — Automated | Disclosure test cases | L2 required | Automated testing for memorisation and over-retrieval of sensitive content |
| Operations / Operational Management (O-OM) | A — Monitoring | Output monitoring | L2 required | Continuous monitoring of production outputs for sensitive content patterns |
| Governance / Policy & Compliance (G-PC) | A — Policy | Data disclosure policy | L1 minimum | Documented policy on what data may be surfaced in model responses |

**Maturity target:** L2 minimum; output DLP is a pre-production gate.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Add DLP scanning to output pipeline
- Define blocklist of sensitive content patterns (PII formats, internal identifiers)
- Audit existing outputs for historical disclosure incidents

**Tier 2 — Short-term:**
- Implement per-user output filtering based on entitlement
- V-ST: test suite probing for memorised sensitive content
- Add output redaction for any PII detected at runtime

**Tier 3 — Strategic:**
- O-OM L3: real-time output anomaly detection with automated redaction
- G-PC L3: formal data disclosure impact assessment for all new data sources
- Annual model audit for sensitive content memorisation

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- Agentic: ASI06 (Data Exfiltration via Agentic Channels)
- See also: [DSGAI_SOC2.md](DSGAI_SOC2.md), [DSGAI_PCIDSS.md](DSGAI_PCIDSS.md)

---

### DSGAI07 — Excessive Data Access

GenAI systems — retrieval pipelines, agentic tools, API integrations
— are granted data access beyond what their declared function requires,
creating unnecessary exposure and blast radius on compromise.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Data least-privilege architecture | L2 required | Define minimum data scope for each system component |
| Governance / Strategy & Metrics (G-SM) | B — Roadmap | Data access governance programme | L2 required | Formalise data access review as part of security programme |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Data access audit | L2 required | Periodic review of declared vs actual data access per component |
| Operations / Operational Management (O-OM) | B — Review | Access drift detection | L2 required | Alert when component requests data outside declared scope |
| Governance / Policy & Compliance (G-PC) | A — Policy | Data access policy | L1 minimum | Documented policy requiring data access justification |

**Maturity target:** L2 minimum.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Enumerate all data sources accessible to each GenAI component
- Remove access to any data source not exercised in past 30 days
- Apply least-privilege to RAG retrieval: query-scoped access only

**Tier 2 — Short-term:**
- Implement data access declaration in deployment manifests
- V-AA: architecture review includes data access scope sign-off
- Automate drift detection: alert when runtime access exceeds manifest

**Tier 3 — Strategic:**
- G-SM L3: data access review board with quarterly reporting
- D-SA L3: zero-trust data access architecture for all GenAI components
- Annual penetration test targeting data access boundary violations

#### Cross-references

- LLM Top 10: LLM06 (Excessive Agency)
- Agentic: ASI02 (Excessive Permissions and Scope)
- See also: [DSGAI_ISO27001.md](DSGAI_ISO27001.md), [DSGAI_CISControls.md](DSGAI_CISControls.md)

---

### DSGAI08 — Data Leakage in Retrieval

Retrieval-augmented generation (RAG) pipelines return documents
exceeding the user's entitlement — exposing information from other
tenants, higher-sensitivity tiers, or access-controlled corpora.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Retrieval entitlement threat model | L2 required | Model all paths where over-retrieval can expose unauthorised content |
| Implementation / Secure Build (I-SB) | A — Build Process | Retrieval access control enforcement | L2 required | Enforce per-query entitlement filtering in retrieval pipeline |
| Verification / Security Testing (V-ST) | B — Deep Testing | Cross-tenant retrieval leakage tests | L2 required | Test whether queries can retrieve documents from other tenants or restricted tiers |
| Operations / Operational Management (O-OM) | A — Monitoring | Retrieval audit logging | L1 minimum | Log all retrieved documents with user identity for forensic review |
| Governance / Policy & Compliance (G-PC) | A — Policy | RAG entitlement policy | L1 minimum | Policy mapping corpus access to user roles and data classification |

**Maturity target:** L2 minimum; retrieval entitlement check is a pre-production gate for multi-tenant RAG.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Implement per-query entitlement filter in retrieval pipeline
- Add metadata-based access control to all corpus documents
- Log all retrieval operations with user context

**Tier 2 — Short-term:**
- V-ST: automated cross-tenant leakage test battery in CI/CD
- Red team: attempt retrieval of documents outside declared entitlement
- Add retrieval anomaly detection: flag unusual document access patterns

**Tier 3 — Strategic:**
- I-SB L3: automated entitlement coverage analysis for all corpus changes
- D-TA L3: threat model updated for every new corpus or retrieval path
- See [shared/RECIPES.md](../shared/RECIPES.md) Pattern 1 — Access-Controlled RAG

#### Cross-references

- LLM Top 10: LLM08 (Vector and Embedding Weaknesses)
- Agentic: ASI06 (Data Exfiltration via Agentic Channels)
- See also: [DSGAI_ASVS.md](DSGAI_ASVS.md), [DSGAI_ISO27001.md](DSGAI_ISO27001.md)

---

### DSGAI09 — RAG Corpus Manipulation

Attackers tamper with documents in RAG corpora — through data
pipeline compromise, malicious document upload, or embedding store
poisoning — causing retrieval to return manipulated content that
steers model outputs.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Corpus integrity threat model | L2 required | Enumerate all write paths to the corpus and attack scenarios for each |
| Implementation / Secure Build (I-SB) | A — Build Process | Corpus write integrity controls | L2 required | Authenticate and verify all corpus writes; hash embeddings at ingest |
| Verification / Security Testing (V-ST) | B — Deep Testing | Corpus poisoning simulation | L2 required | Attempt to inject manipulated documents; verify detection |
| Operations / Incident Management (O-IM) | A — Incident Detection | Corpus integrity monitoring | L2 required | Alert on unexpected corpus changes or embedding distribution shifts |
| Governance / Policy & Compliance (G-PC) | A — Policy | Corpus change management policy | L1 minimum | All corpus changes go through a review and approval process |

**Maturity target:** L2 minimum; L3 for corpora used in safety-critical or regulated decision support.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Apply write authentication to embedding store: only authorised pipeline may write
- Add document hash verification at corpus ingest
- Log all corpus write operations with submitter identity

**Tier 2 — Short-term:**
- Implement corpus integrity checks: detect unexpected document changes
- V-ST: document injection test battery
- G-PC: corpus change approval process with security review for sensitive corpora

**Tier 3 — Strategic:**
- O-IM L3: automated detection of embedding distribution drift (possible poisoning signal)
- Periodic corpus audit: re-verify document authenticity against source
- D-TA L3: threat model updated after every new corpus data source

#### Cross-references

- LLM Top 10: LLM04 (Data and Model Poisoning), LLM08 (Vector and Embedding Weaknesses)
- See also: [DSGAI_MITREATLAS.md](DSGAI_MITREATLAS.md), [DSGAI_NISTCSF2.md](DSGAI_NISTCSF2.md)

---

### DSGAI10 — Context Window Poisoning

Malicious content injected into the active context window — through
tool output, retrieved documents, or session history — manipulates
in-context reasoning without persisting to long-term memory.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Context window injection model | L2 required | Map all sources that contribute to context window; assess trust level per source |
| Implementation / Secure Build (I-SB) | A — Build Process | Context assembly validation | L2 required | Validate and sanitise all content before context window assembly |
| Verification / Security Testing (V-ST) | B — Deep Testing | Context poisoning test suite | L2 required | Adversarial tests injecting malicious content via each context source |
| Operations / Incident Management (O-IM) | A — Incident Detection | In-context manipulation alerting | L1 minimum | Alert on reasoning deviations correlated with external content in context |

**Maturity target:** L2 minimum.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Apply trust-level tagging to all context window sources
- Sanitise all external content before context inclusion
- Log full context window for forensic review on anomalous outputs

**Tier 2 — Short-term:**
- V-ST: inject adversarial content via each context source; verify containment
- Implement context source prioritisation: system instructions cannot be overridden by retrieved content
- Add reasoning consistency check on final output

**Tier 3 — Strategic:**
- D-TA L3: threat model updated for every new context source integration
- Research and deploy formal context integrity verification techniques

#### Cross-references

- LLM Top 10: LLM01 (Prompt Injection), LLM08 (Vector and Embedding Weaknesses)
- Agentic: ASI03 (Memory Manipulation and Persistence)
- See also: [DSGAI_ENISA.md](DSGAI_ENISA.md), [DSGAI_CWE_CVE.md](DSGAI_CWE_CVE.md)

---

### DSGAI11 — Session Persistence Attacks

Attackers exploit session memory and conversation history to persist
malicious instructions or extracted information across session
boundaries, enabling cross-session attacks and long-term manipulation.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Session isolation architecture | L2 required | Design session boundary enforcement; no cross-session data leakage |
| Implementation / Secure Build (I-SB) | A — Build Process | Session data integrity | L2 required | Encrypt, sign, and access-control all persistent session data |
| Operations / Environment Management (O-EM) | A — Patching | Session store hardening | L2 required | Apply access controls and encryption to all session persistence stores |
| Verification / Security Testing (V-ST) | B — Deep Testing | Cross-session leakage tests | L2 required | Test whether session data is accessible or injectable across user boundaries |

**Maturity target:** L2 minimum.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Enforce session isolation at storage layer: no cross-user session access
- Encrypt all persistent session data at rest
- Log all session read/write operations

**Tier 2 — Short-term:**
- V-ST: cross-session data access test battery
- Implement session TTL and automatic purge policy
- Add integrity signatures to session records

**Tier 3 — Strategic:**
- Formal session security architecture review for multi-tenant deployments
- O-EM L3: automated session integrity monitoring

#### Cross-references

- Agentic: ASI03 (Memory Manipulation and Persistence)
- See also: [DSGAI_ASVS.md](DSGAI_ASVS.md), [DSGAI_SOC2.md](DSGAI_SOC2.md)

---

### DSGAI12 — Model Inversion and Extraction

Adversaries query deployed models to reconstruct training data,
replicate model weights, or extract sensitive information encoded
in model parameters through systematic prompting or gradient attacks.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Model extraction threat model | L2 required | Model extraction attack surface: API rate limits, confidence scores, output verbosity |
| Verification / Security Testing (V-ST) | B — Deep Testing | Extraction and inversion simulation | L2 required | Attempt model extraction via systematic querying; verify detection and rate limiting |
| Operations / Operational Management (O-OM) | A — Monitoring | Query pattern anomaly detection | L2 required | Alert on systematic query patterns consistent with extraction attempts |
| Design / Security Requirements (D-SR) | A — Requirements | API output restriction requirements | L1 minimum | Minimise logit exposure, confidence scores, and internal state leakage |

**Maturity target:** L2 minimum.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Implement API rate limiting per user/IP
- Remove or restrict confidence score and logit output from API responses
- Log all high-volume query sessions

**Tier 2 — Short-term:**
- Add query pattern detection: alert on systematic extraction-pattern queries
- Implement per-user query budget with soft/hard limits
- V-ST: model extraction simulation exercise

**Tier 3 — Strategic:**
- Differential privacy techniques for sensitive models
- O-OM L3: continuous extraction attempt detection using ML-based query analysis
- Legal and contractual protections: API terms of service with extraction prohibition

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- DSGAI14 (Model Weight Theft)
- See also: [DSGAI_MITREATLAS.md](DSGAI_MITREATLAS.md) AML.T0027

---

### DSGAI13 — Data Leakage through Tool Integration

GenAI system tool integrations — APIs, databases, file systems,
communication services — leak data to unauthorised parties through
misconfigured permissions, over-broad responses, or insecure tool
implementations.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Requirements (D-SR) | A — Requirements | Tool integration data security requirements | L2 required | Minimum data returned per tool; response scope limitations |
| Implementation / Secure Build (I-SB) | A — Build Process | Tool response filtering | L2 required | Filter tool responses to minimum data required before passing to model |
| Verification / Security Testing (V-ST) | A — Automated | Tool data leakage tests | L2 required | Automated tests verifying tool responses are scoped to minimum |
| Governance / Policy & Compliance (G-PC) | A — Policy | Tool approval policy | L2 required | All tools reviewed for data scope before integration |
| Operations / Operational Management (O-OM) | A — Monitoring | Tool response monitoring | L1 minimum | Log all tool responses; alert on anomalous data volumes |

**Maturity target:** L2 minimum.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Audit all tool integrations for data scope
- Remove any tools returning data beyond declared function
- Add logging to all tool response streams

**Tier 2 — Short-term:**
- Implement minimum data principle in tool wrappers: filter before passing to model
- V-ST: automated test suite for data leakage per tool
- G-PC: tool review board with security sign-off

**Tier 3 — Strategic:**
- I-SB L3: automated data leakage scanning in tool integration CI/CD
- O-OM L3: real-time tool response anomaly detection
- Tool governance programme with periodic re-review of approved tools

#### Cross-references

- Agentic: ASI05 (Tool and Plugin Abuse)
- LLM Top 10: LLM07 (System Prompt Leakage via Tools)
- See also: [DSGAI_ASVS.md](DSGAI_ASVS.md), [DSGAI_CWE_CVE.md](DSGAI_CWE_CVE.md)

---

### DSGAI14 — Model Weight Theft

Adversaries gain access to proprietary model weights through
infrastructure compromise, insider threat, or API extraction —
stealing intellectual property and enabling fine-tuned attack models
that bypass original safety controls.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Model asset protection architecture | L2 required | Treat model weights as crown-jewel assets with appropriate access controls |
| Governance / Policy & Compliance (G-PC) | A — Policy | Model asset classification policy | L2 required | Classify model weights; require formal access control and custodian assignment |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Model storage security review | L2 required | Periodic review of model storage access controls |
| Operations / Operational Management (O-OM) | A — Monitoring | Model asset access monitoring | L2 required | Alert on unexpected access to model weight storage |
| Governance / Strategy & Metrics (G-SM) | B — Roadmap | IP protection programme | L1 minimum | Document model IP protection controls in security programme roadmap |

**Maturity target:** L2 minimum for any organisation with proprietary fine-tuned models.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Apply access controls and encryption to all model weight storage
- Audit who has current access to model weights; remove unnecessary access
- Enable access logging on all model storage systems

**Tier 2 — Short-term:**
- Classify model weights as high-sensitivity assets in asset inventory
- V-AA: architecture review of model storage access controls
- Red team exercise: attempt model weight exfiltration via infrastructure

**Tier 3 — Strategic:**
- Hardware security modules (HSM) for model weight protection in high-value deployments
- O-OM L3: automated anomaly detection on model weight access patterns
- Legal protections: trade secret designations and contractual controls with cloud providers

#### Cross-references

- DSGAI12 (Model Inversion and Extraction)
- LLM Top 10: LLM03 (Supply Chain)
- See also: [DSGAI_ISO27001.md](DSGAI_ISO27001.md), [DSGAI_MITREATLAS.md](DSGAI_MITREATLAS.md) AML.T0044

---

### DSGAI15 — Inference Data Exposure

Input data submitted to GenAI systems at inference time — queries,
documents, user data — is logged, retained, or used in ways that
expose it to unauthorised parties, including third-party model
providers, logging infrastructure, or analytics systems.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Requirements (D-SR) | A — Requirements | Inference data handling requirements | L2 required | Define what inference data may be logged, retained, and shared |
| Implementation / Secure Build (I-SB) | A — Build Process | Inference data minimisation | L2 required | Log only what is operationally necessary; scrub sensitive data from logs |
| Operations / Environment Management (O-EM) | A — Patching | Inference data store hardening | L2 required | Access controls, encryption, and retention policies for all inference logs |
| Governance / Policy & Compliance (G-PC) | A — Policy | Inference data retention policy | L1 minimum | Documented policy on inference data retention periods and deletion |

**Maturity target:** L2 minimum; GDPR creates legal obligations for inference data handling.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Audit all inference logging configurations
- Remove any inference data logging not required for operations
- Apply encryption to all inference logs at rest

**Tier 2 — Short-term:**
- Implement inference data scrubbing: PII removed from logs before storage
- Review third-party model provider data retention terms
- Define and enforce inference log retention periods and deletion

**Tier 3 — Strategic:**
- G-PC L3: privacy impact assessment for all inference data flows
- O-EM L3: automated inference data lifecycle management
- Data residency controls for regulated sectors

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- DSGAI03 (Sensitive Data in Training Sets)
- See also: [DSGAI_EUAIAct.md](DSGAI_EUAIAct.md), [DSGAI_SOC2.md](DSGAI_SOC2.md)

---

### DSGAI16 — Third-Party Data Dependencies

GenAI systems depend on external data sources — APIs, data brokers,
open datasets, web scraping — whose quality, security, or availability
cannot be guaranteed, introducing poisoning, quality degradation, or
supply chain risks.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Policy & Compliance (G-PC) | A — Policy | Third-party data source policy | L2 required | Approved vendor list for all external data sources |
| Implementation / Secure Build (I-SB) | B — Dependencies | Data source SBOM | L2 required | Inventory of all external data sources with security contact and last-verified date |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Data dependency architecture review | L2 required | Architecture review validates all external data dependencies against policy |
| Operations / Operational Management (O-OM) | B — Review | Data source monitoring | L1 minimum | Track security advisories and availability for all integrated data sources |

**Maturity target:** L2 minimum.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Inventory all third-party data sources in use
- Flag sources without security contact or recent review
- Pin data source versions where possible; reject unversioned public data in production

**Tier 2 — Short-term:**
- Implement data source review process: all new sources require security assessment
- Add integrity verification for all third-party data at ingestion
- Monitor for security advisories on all data source providers

**Tier 3 — Strategic:**
- G-PC L3: formal vendor security assessment programme for data dependencies
- I-SB L3: automated data dependency scanning in CI/CD
- Periodic supply chain red team exercise targeting data source compromise

#### Cross-references

- LLM Top 10: LLM03 (Supply Chain Vulnerabilities)
- Agentic: ASI07 (Supply Chain Compromise in Agent Ecosystems)
- DSGAI17 (Model Supply Chain Risks)
- See also: [DSGAI_CWE_CVE.md](DSGAI_CWE_CVE.md), [DSGAI_ISO27001.md](DSGAI_ISO27001.md)

---

### DSGAI17 — Model Supply Chain Risks

Pre-trained models, fine-tuning datasets, model hubs, and ML
frameworks are compromised — introducing backdoored models, malicious
adapters, or vulnerable ML library code into production GenAI systems.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Policy & Compliance (G-PC) | A — Policy | Model provenance policy | L2 required | Only approved model sources; provenance verification required |
| Implementation / Secure Build (I-SB) | B — Dependencies | Model SBOM | L2 required | SBOM covering base models, adapters, and ML framework dependencies |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Model supply chain architecture review | L2 required | Architecture review validates model sourcing against policy |
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Model supply chain threat model | L2 required | Model compromise scenarios for base models, adapters, and frameworks |
| Operations / Operational Management (O-OM) | B — Review | Model security advisory monitoring | L1 minimum | Track CVEs and security advisories for all model components |

**Maturity target:** L2 minimum; no production deployment of unverified base models.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Verify provenance of all models currently in production
- Flag any models from unverified sources for review
- Pin all model versions; reject floating references in production

**Tier 2 — Short-term:**
- Implement model hash verification at deployment
- G-PC: model review board for all new base model or adapter integrations
- V-ST: adversarial probing of fine-tuned models for backdoor triggers

**Tier 3 — Strategic:**
- I-SB L3: automated model supply chain scanning in CI/CD
- Periodic re-evaluation of production models against clean evaluation set
- Formal model provenance attestation for regulated deployments

#### Cross-references

- LLM Top 10: LLM03 (Supply Chain Vulnerabilities), LLM04 (Data and Model Poisoning)
- Agentic: ASI07 (Supply Chain Compromise)
- See also: [DSGAI_MITREATLAS.md](DSGAI_MITREATLAS.md) AML.T0010

---

### DSGAI18 — Data Retention and Deletion Failures

GenAI systems retain personal data, training artefacts, or inference
logs beyond required retention periods — or fail to honour deletion
requests — creating regulatory violations and unnecessary exposure.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Policy & Compliance (G-PC) | A — Policy | Data retention and deletion policy | L2 required | Documented retention periods and deletion procedures for all GenAI data |
| Design / Security Requirements (D-SR) | A — Requirements | Deletion requirements | L1 minimum | Right-to-erasure and retention limits built into system requirements |
| Operations / Operational Management (O-OM) | A — Monitoring | Retention compliance monitoring | L1 minimum | Automated verification that data is deleted per retention schedule |
| Governance / Strategy & Metrics (G-SM) | B — Roadmap | Privacy programme integration | L1 minimum | GenAI data lifecycle integrated into existing privacy programme |

**Maturity target:** L1 minimum before production; GDPR Art. 17 creates right to erasure obligations.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Document all data stores containing GenAI system data
- Define retention periods for each data store; implement deletion schedule
- Verify deletion capability: confirm data can actually be deleted from each store

**Tier 2 — Short-term:**
- Implement automated retention policy enforcement
- Test deletion procedures: verify data is unrecoverable after deletion
- Add right-to-erasure workflow for user data in inference logs

**Tier 3 — Strategic:**
- G-PC L3: formal data lifecycle governance for all GenAI data
- Privacy-by-design: new features require retention review before deployment
- Annual audit of retention compliance across all GenAI data stores

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- DSGAI15 (Inference Data Exposure)
- See also: [DSGAI_EUAIAct.md](DSGAI_EUAIAct.md), [DSGAI_SOC2.md](DSGAI_SOC2.md)

---

### DSGAI19 — Cascading Data Failures

Failures in data pipelines — corrupt embeddings, failed ingestion,
incorrect transformations — propagate through multiple GenAI system
components, causing compounding degradation or failures in dependent
downstream components.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Pipeline fault isolation | L2 required | Design circuit breakers and isolation boundaries between data pipeline stages |
| Operations / Incident Management (O-IM) | A — Incident Detection | Cascade detection alerting | L2 required | Detect correlated failures across pipeline stages; alert before full cascade |
| Operations / Environment Management (O-EM) | A — Patching | Pipeline health monitoring | L2 required | Continuous health checks across all pipeline components |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Cascade failure architecture review | L1 minimum | Verify blast radius containment design before deployment |
| Operations / Incident Management (O-IM) | B — Response | Pipeline incident playbook | L1 minimum | Documented runbook for data pipeline cascade scenarios |

**Maturity target:** L2 minimum; O-IM playbook required before production for complex multi-stage pipelines.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Add health checks to all pipeline stages
- Implement circuit breaker pattern between pipeline stages
- Document blast radius: if stage X fails, which downstream components are affected?

**Tier 2 — Short-term:**
- Red team: simulate cascading failure from one corrupted pipeline stage
- Deploy O-IM playbook for data pipeline cascade incidents
- Add per-stage data validation checkpoints

**Tier 3 — Strategic:**
- D-SA L3: formal chaos engineering programme for data pipelines
- O-EM L3: automated cascade detection with predictive alerting
- Architecture pattern: idempotent pipeline stages with rollback capability

#### Cross-references

- Agentic: ASI10 (Cascading Agent Failures)
- See also: [DSGAI_NISTCSF2.md](DSGAI_NISTCSF2.md), [DSGAI_ISO27001.md](DSGAI_ISO27001.md)

---

### DSGAI20 — Regulatory Non-Compliance in Data Use

GenAI systems process personal data, biometric data, or regulated
information in ways that violate applicable law — GDPR, CCPA, HIPAA,
PCI DSS, EU AI Act — through inadequate consent management, cross-border
transfers, prohibited processing, or insufficient documentation.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Policy & Compliance (G-PC) | A — Policy | Regulatory compliance programme | L2 required | Mapped regulatory obligations for all applicable jurisdictions |
| Governance / Strategy & Metrics (G-SM) | A — Policy | Compliance metrics and reporting | L2 required | Compliance KPIs tracked and reported to leadership |
| Design / Security Requirements (D-SR) | A — Requirements | Regulatory requirements in design | L2 required | Regulatory obligations surfaced as design requirements for all data flows |
| Operations / Operational Management (O-OM) | A — Monitoring | Compliance monitoring | L2 required | Continuous monitoring for regulatory control effectiveness |
| Governance / Education & Guidance (G-EG) | B — Training | Compliance training | L1 minimum | All staff handling regulated data understand applicable obligations |

**Maturity target:** L2 minimum; G-PC at L2 is non-negotiable for any organisation processing personal data.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Map all applicable regulations for each GenAI data flow
- Identify any processing without legal basis
- Document data processing activities (GDPR Art. 30 records of processing)

**Tier 2 — Short-term:**
- Implement consent management for any user-facing data collection
- Complete DPIA for high-risk processing activities (EU AI Act + GDPR)
- G-PC: legal review of cross-border data transfer mechanisms

**Tier 3 — Strategic:**
- G-PC L3: formal compliance monitoring programme with external audit
- G-SM L3: compliance dashboard with real-time regulatory status
- Annual regulatory impact assessment for all new GenAI features

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- See also: [DSGAI_EUAIAct.md](DSGAI_EUAIAct.md), [DSGAI_SOC2.md](DSGAI_SOC2.md), [DSGAI_PCIDSS.md](DSGAI_PCIDSS.md)

---

### DSGAI21 — Data Provenance and Lineage Failures

GenAI systems cannot demonstrate where training data, retrieved
documents, or inference inputs originated — making it impossible to
audit decisions, respond to data quality incidents, or comply with
traceability requirements in regulated sectors.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Policy & Compliance (G-PC) | A — Policy | Data provenance policy | L1 minimum | Policy requiring provenance metadata for all GenAI data |
| Design / Security Requirements (D-SR) | A — Requirements | Provenance tracking requirements | L1 minimum | Provenance metadata built into data pipeline requirements |
| Operations / Operational Management (O-OM) | A — Monitoring | Lineage monitoring | L1 minimum | Alert on loss of provenance metadata in data flows |
| Verification / Requirements-Driven Testing (V-RT) | A — Testing | Provenance coverage tests | L1 minimum | Tests verifying provenance metadata is preserved through pipeline |
| Governance / Strategy & Metrics (G-SM) | B — Roadmap | Data governance roadmap | L1 minimum | Provenance programme included in data governance roadmap |

**Maturity target:** L1 minimum for all deployments; L2 for regulated sectors (financial services, healthcare).

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Attach source metadata to all ingested data
- Log origin, timestamp, and version for all training datasets
- Add provenance fields to corpus document schema

**Tier 2 — Short-term:**
- Implement end-to-end lineage tracking in data pipelines
- V-RT: automated provenance coverage test suite
- G-PC: provenance requirements documented and signed off

**Tier 3 — Strategic:**
- Immutable lineage ledger for regulatory traceability
- G-PC L3: formal data governance programme with lineage as a core requirement
- Integration with CROSSREF.md for cross-source-list risk traceability

#### Cross-references

- LLM Top 10: LLM04 (Data and Model Poisoning)
- DSGAI02 (Training Data Poisoning), DSGAI09 (RAG Corpus Manipulation)
- See also: [DSGAI_ISO42001.md](DSGAI_ISO42001.md), [DSGAI_NISTAIRMF.md](DSGAI_NISTAIRMF.md)

---

## SAMM maturity scorecard — GenAI data security minimum viable levels

| Practice | Minimum Viable Level | Current Level | Gap | Priority |
|---|:---:|:---:|:---:|:---:|
| G-SM Strategy & Metrics | L2 | | | |
| G-PC Policy & Compliance | L2 | | | |
| G-EG Education & Guidance | L1 | | | |
| D-TA Threat Assessment | L2 | | | |
| D-SR Security Requirements | L2 | | | |
| D-SA Security Architecture | L2 | | | |
| I-SB Secure Build | L2 | | | |
| I-SD Secure Deployment | L1 | | | |
| I-DM Defect Management | L1 | | | |
| V-AA Architecture Assessment | L2 | | | |
| V-RT Requirements-Driven Testing | L1 | | | |
| V-ST Security Testing | L2 | | | |
| O-IM Incident Management | L2 | | | |
| O-EM Environment Management | L2 | | | |
| O-OM Operational Management | L2 | | | |

**Scoring:** Any practice below Minimum Viable Level with active DSGAI-listed
data flows in production is a compliance and security risk.

**GDPR note:** G-PC at L2 is a legal baseline for any organisation processing
personal data in GenAI systems operating in jurisdictions covered by GDPR or CCPA.

---

## Implementation priority table

| Priority | Practices | DSGAI entries addressed |
|---|---|---|
| P1 — Pre-production gate | D-TA L2, I-SB L2, G-PC L2 | DSGAI01, DSGAI02, DSGAI03, DSGAI09 |
| P2 — First 30 days | D-SA L2, V-ST L2, O-IM L2 | DSGAI04, DSGAI05, DSGAI06, DSGAI08 |
| P3 — 60-day milestone | V-AA L2, O-OM L2, D-SR L2 | DSGAI07, DSGAI13, DSGAI15, DSGAI20 |
| P4 — Programme maturity | All practices L3, formal audits | DSGAI12, DSGAI14, DSGAI19 |

---

## References

- [OWASP SAMM v2.0](https://owaspsamm.org/)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [OWASP LLM Top 10 2025 × SAMM](../llm-top10/LLM_SAMM.md)
- [Agentic Top 10 2026 × SAMM](../agentic-top10/Agentic_SAMM.md)
- [shared/RECIPES.md](../shared/RECIPES.md) — Pattern 1: Access-Controlled RAG Retrieval
- [DSGAI_ISO42001.md](DSGAI_ISO42001.md) — AIMS controls complement SAMM data governance practices

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping DSGAI01–DSGAI21 to SAMM v2.0 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
