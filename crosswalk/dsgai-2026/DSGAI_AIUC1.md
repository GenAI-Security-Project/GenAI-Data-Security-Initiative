<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01-DSGAI21)
  Framework   : AIUC-1 — The standard for AI agent security, safety and reliability
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × AIUC-1

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to [AIUC-1](https://www.aiuc-1.com/) — the world's
first AI agent security, safety and reliability certification framework,
developed with 100+ Fortune 500 CISOs.

AIUC-1 is an OWASP GenAI Security Project partner. Its six domains
(Data & Privacy, Security, Safety, Reliability, Accountability, Society)
map directly to the data security concerns across the DSGAI taxonomy —
Domain A (Data & Privacy) alone covers a majority of the 21 DSGAI entries.

---

## AIUC-1 domains at a glance

| Domain | ID | Focus |
|---|---|---|
| Data & Privacy | A | PII protection, data leakage, IP, access controls, training data |
| Security | B | Adversarial robustness, injection, output filtering, permissions |
| Safety | C | Harm prevention, unsafe outputs, guardrails, human oversight |
| Reliability | D | Availability, consistency, failure recovery, rate limiting |
| Accountability | E | Audit trails, logging, explainability, incident response |
| Society | F | Bias, misinformation, societal harm, transparency |

---

## Quick-reference summary

| ID | Name | Severity | Primary AIUC-1 Domains/Controls | Tier |
|---|---|---|---|---|
| DSGAI01 | Prompt Injection via Data Channels | Critical | B001, B002, B005, B006 | Foundational–Advanced |
| DSGAI02 | Training Data Poisoning | Critical | A (all), B001, B002, E | Hardening–Advanced |
| DSGAI03 | Sensitive Data in Training Sets | High | A (all), B006, E | Foundational–Hardening |
| DSGAI04 | Insecure Data Pipelines | High | A, B001, B003, E | Foundational–Hardening |
| DSGAI05 | Guardrail Circumvention | High | B001, B002, B005, C | Hardening–Advanced |
| DSGAI06 | Unintended Data Disclosure | High | A, B006, B009, E | Foundational–Hardening |
| DSGAI07 | Excessive Data Access | High | A, B006, B007, E | Foundational–Hardening |
| DSGAI08 | Data Leakage in Retrieval | High | A, B005, B006 | Hardening–Advanced |
| DSGAI09 | RAG Corpus Manipulation | Critical | A, B001, B002, E | Hardening–Advanced |
| DSGAI10 | Context Window Poisoning | High | B001, B002, B005 | Hardening–Advanced |
| DSGAI11 | Session Persistence Attacks | High | A, B006, E | Hardening–Advanced |
| DSGAI12 | Model Inversion and Extraction | High | A, B006, D, E | Hardening–Advanced |
| DSGAI13 | Data Leakage through Tool Integration | High | A, B003, B007, E | Foundational–Hardening |
| DSGAI14 | Model Weight Theft | High | A, B006, E | Hardening–Advanced |
| DSGAI15 | Inference Data Exposure | High | A, B006, E | Foundational–Hardening |
| DSGAI16 | Third-Party Data Dependencies | High | B001, B003, B008 | Foundational–Hardening |
| DSGAI17 | Model Supply Chain Risks | High | B001, B003, B008, A | Foundational–Hardening |
| DSGAI18 | Data Retention and Deletion Failures | Medium | A, E | Foundational–Hardening |
| DSGAI19 | Cascading Data Failures | High | D, B006, E | Hardening–Advanced |
| DSGAI20 | Regulatory Non-Compliance | High | A, C, E, F | Foundational–Hardening |
| DSGAI21 | Data Provenance and Lineage Failures | Medium | A, E | Foundational–Hardening |

---

## Audience tags

- **Data engineer / ML engineer** — Domain A, B001, B002 — data pipeline security
- **Security engineer** — B001–B009, E — full security domain
- **Auditor** — A, E, B003, B007 — compliance and evidence
- **CISO / governance** — A, C, E, F — programme and oversight
- **Privacy officer** — Domain A, DSGAI03, DSGAI15, DSGAI18, DSGAI20
- **AI red teamer** — B001, B002, B005 — adversarial data pipeline testing

---

## Detailed mappings

---

### DSGAI01 — Prompt Injection via Data Channels

Malicious instructions embedded in training data, retrieved documents,
or tool outputs manipulate model behaviour at inference time.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Adversarial testing of all data injection vectors | Foundational |
| Detect adversarial input | B002 | Runtime detection of injection in data channels | Hardening |
| Implement real-time input filtering | B005 | Filter all external data before context assembly | Foundational |
| Prevent unauthorized AI actions | B006 | Prevent execution of injected instructions | Foundational |

**Mitigations:**
- B005: content filtering at all data ingestion boundaries
- B006: trust-level tagging — retrieved data cannot override system instructions
- B001: adversarial injection testing in CI/CD for all data channels
- B002: runtime anomaly detection on model decisions correlated with external data

---

### DSGAI02 — Training Data Poisoning

OT process data or public datasets used in training are corrupted —
causing models to learn backdoored, biased, or degraded behaviours.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain (all) | A | Training data integrity, provenance, and access control | Foundational |
| Third-party adversarial robustness testing | B001 | Backdoor and poisoning detection in training pipeline | Foundational |
| Detect adversarial input | B002 | Detect anomalous training data patterns | Hardening |
| Audit trails and logging | E | Chain of custody for training data | Foundational |

**Mitigations:**
- Domain A: hash verification for all training data; restrict write access
- B001: adversarial probing of trained models for backdoor triggers
- B002: statistical anomaly detection on training data distributions
- Domain E: immutable chain of custody from data source to training job

---

### DSGAI03 — Sensitive Data in Training Sets

PII, credentials, trade secrets, or regulated data included in training
sets lead to model memorisation and potential disclosure at inference.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain (all) | A | Data classification and minimisation for training datasets | Foundational |
| Prevent unauthorized AI actions | B006 | Output restrictions preventing memorised sensitive data disclosure | Foundational |
| Audit trails and logging | E | Evidence of PII scanning and removal procedures | Foundational |

**Mitigations:**
- Domain A: automated PII scanning of all training datasets before use
- Domain A data minimisation: remove or anonymise detected sensitive records
- B006: output filtering blocking memorised sensitive data patterns
- Domain E: audit evidence of data cleaning procedures

---

### DSGAI04 — Insecure Data Pipelines

Data ingestion, preprocessing, and serving pipelines lack authentication,
integrity controls, or logging — enabling tampering or exfiltration.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Access controls and integrity for pipeline data | Foundational |
| Third-party adversarial robustness testing | B001 | Pipeline security testing | Foundational |
| Third-party security assessment | B003 | Assessment of third-party pipeline components | Hardening |
| Audit trails and logging | E | Per-stage pipeline audit logging | Foundational |

**Mitigations:**
- Domain A: authentication and encryption for all pipeline connections
- B001: pipeline security testing in CI/CD
- B003: assess all third-party pipeline components
- Domain E: per-stage audit logging with forensic retention

---

### DSGAI05 — Guardrail Circumvention

Safety guardrails protecting GenAI system outputs are bypassed through
adversarial prompting, model manipulation, or architectural weaknesses.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Dedicated guardrail bypass red team testing | Hardening |
| Detect adversarial input | B002 | Runtime detection of bypass attempts | Hardening |
| Implement real-time input filtering | B005 | Secondary filtering layer outside model inference | Foundational |
| Safety domain (harm prevention) | C | Guardrail architecture and effectiveness requirements | Foundational |

**Mitigations:**
- Domain C: defence-in-depth guardrail design — multiple independent layers
- B001: dedicated adversarial testing programme targeting guardrail bypass
- B005: secondary rule-based guardrail outside LLM inference path
- B002: runtime detection of guardrail bypass attempts

---

### DSGAI06 — Unintended Data Disclosure

GenAI systems surface sensitive information in responses through
memorisation, over-retrieval, or insufficient output filtering.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Output data classification and filtering | Foundational |
| Prevent unauthorized AI actions | B006 | Output scope restrictions for sensitive data categories | Foundational |
| Validate AI-generated content | B009 | Output validation before delivery | Foundational |
| Audit trails and logging | E | Output logging for disclosure incident investigation | Foundational |

**Mitigations:**
- Domain A + B006: DLP scanning and output filtering for all sensitive data patterns
- B009: output validation before delivery to user
- Domain E: audit logging of all outputs with forensic retention
- Per-user output filtering based on entitlement

---

### DSGAI07 — Excessive Data Access

GenAI systems are granted data access beyond their declared function —
creating unnecessary exposure and blast radius on compromise.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Data minimisation and access control | Foundational |
| Prevent unauthorized AI actions | B006 | Scope restrictions for data access | Foundational |
| Third-party permission controls | B007 | Least-privilege for third-party data access | Hardening |
| Audit trails and logging | E | Data access audit logging | Foundational |

**Mitigations:**
- Domain A: least-privilege data access per GenAI system component
- B006: query-scoped data access — minimum data returned per request
- B007: third-party tool data access restricted to declared scope
- Domain E: data access audit logging with drift detection

---

### DSGAI08 — Data Leakage in Retrieval

RAG pipelines return documents exceeding user entitlement — exposing
data from other tenants, higher-sensitivity tiers, or access-controlled corpora.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Per-user entitlement controls on corpus access | Foundational |
| Implement real-time input filtering | B005 | Filter retrieved content to minimum required | Foundational |
| Prevent unauthorized AI actions | B006 | Enforce retrieval scope restrictions | Foundational |

**Mitigations:**
- Domain A: access-controlled retrieval with per-query entitlement filtering
- B005: post-retrieval content filtering before context inclusion
- B006: enforce that retrieved documents match user entitlement
- Automated cross-tenant leakage test suite (see B001)

---

### DSGAI09 — RAG Corpus Manipulation

Attackers tamper with RAG corpora — through data pipeline compromise
or malicious document injection — causing retrieval to return manipulated
content that steers model outputs.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Corpus integrity, write authentication, provenance | Foundational |
| Third-party adversarial robustness testing | B001 | Corpus poisoning simulation | Hardening |
| Detect adversarial input | B002 | Corpus integrity monitoring and distribution drift detection | Hardening |
| Audit trails and logging | E | Immutable corpus write audit log | Foundational |

**Mitigations:**
- Domain A: write authentication for corpus stores; hash verification at ingest
- B001: document injection simulation in CI/CD
- B002: corpus distribution drift detection in production
- Domain E: immutable audit log for all corpus write operations

---

### DSGAI10 — Context Window Poisoning

Malicious content injected into the active context window through tool
output or retrieved documents manipulates in-context reasoning.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Context injection testing across all sources | Foundational |
| Detect adversarial input | B002 | Runtime detection of context manipulation | Hardening |
| Implement real-time input filtering | B005 | Content filtering at context assembly | Foundational |

**Mitigations:**
- B005: sanitise all external content before context window assembly
- B001: adversarial context injection testing across all content sources
- B002: anomaly detection on model decisions correlated with context anomalies
- Trust-level tagging: external content cannot override system instructions

---

### DSGAI11 — Session Persistence Attacks

Attackers exploit session memory to persist malicious instructions or
extracted information across session boundaries.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Session data access controls and encryption | Foundational |
| Prevent unauthorized AI actions | B006 | Session isolation enforcement | Foundational |
| Audit trails and logging | E | Session access audit logging | Foundational |

**Mitigations:**
- Domain A: session isolation, encryption, and access controls
- B006: no cross-session data access without explicit authorisation
- Domain E: audit logging of all session read/write operations
- Session TTL and automatic purge policy

---

### DSGAI12 — Model Inversion and Extraction

Adversaries query models systematically to reconstruct training data
or replicate model weights through systematic prompting.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Model weight and inference data protection | Foundational |
| Prevent unauthorized AI actions | B006 | API rate limiting and scope restrictions | Foundational |
| Reliability domain | D | Rate limiting and query budget enforcement | Foundational |
| Audit trails and logging | E | Query pattern logging for extraction detection | Foundational |

**Mitigations:**
- Domain D + B006: API rate limiting and per-user query budget
- Domain A: restrict confidence score and logit exposure in API responses
- Domain E: query pattern logging with extraction detection alerting
- Periodic model extraction simulation exercise (B001)

---

### DSGAI13 — Data Leakage through Tool Integration

GenAI system tool integrations leak data to unauthorised parties through
misconfigured permissions or over-broad API responses.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Tool integration data scope controls | Foundational |
| Third-party security assessment | B003 | Formal assessment of all tool integrations | Hardening |
| Third-party permission controls | B007 | Least-privilege for all tool data access | Hardening |
| Audit trails and logging | E | Tool response audit logging | Foundational |

**Mitigations:**
- Domain A + B007: minimum data principle for all tool responses
- B003: security assessment for all third-party tool integrations
- Domain E: log all tool API responses with full payload
- Automated data leakage tests per tool (B001)

---

### DSGAI14 — Model Weight Theft

Proprietary model weights are stolen through infrastructure compromise,
insider threat, or API extraction.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Model weight classification as IP asset with access controls | Foundational |
| Prevent unauthorized AI actions | B006 | Access restrictions on model weight storage | Foundational |
| Audit trails and logging | E | Model weight access audit logging | Foundational |

**Mitigations:**
- Domain A: classify model weights as sensitive IP; apply encryption and access controls
- B006: strict access scope on model storage systems
- Domain E: alert on unexpected model weight access patterns
- Third-party cloud provider contractual protections (B003)

---

### DSGAI15 — Inference Data Exposure

Input data submitted at inference time is logged or retained in ways
that expose it to unauthorised parties.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Inference data minimisation and retention policy | Foundational |
| Prevent unauthorized AI actions | B006 | Access restrictions on inference log data | Foundational |
| Audit trails and logging | E | Inference data access audit logging | Foundational |

**Mitigations:**
- Domain A: data minimisation — log only what is operationally necessary
- Domain A: apply encryption to all inference logs at rest
- B006: restrict inference log access to authorised roles
- Define and enforce inference log retention periods

---

### DSGAI16 — Third-Party Data Dependencies

GenAI systems depend on external data sources whose security cannot
be guaranteed, introducing supply chain risks.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Extend testing to third-party data inputs | Foundational |
| Third-party security assessment | B003 | Formal assessment of data source providers | Hardening |
| Third-party NHI controls | B008 | Controls for third-party credentials and API keys | Hardening |

**Mitigations:**
- B003: security assessment for all critical external data source providers
- B001: integrity testing for all third-party data at ingestion
- B008: NHI controls for all third-party data API credentials
- Data source SBOM with version pinning

---

### DSGAI17 — Model Supply Chain Risks

Pre-trained models, adapters, or ML frameworks are compromised —
introducing backdoored models or vulnerable code into production.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Backdoor detection in third-party models | Foundational |
| Third-party security assessment | B003 | Formal assessment of model providers | Hardening |
| Third-party NHI controls | B008 | Credentials for model provider APIs | Hardening |
| Data & Privacy domain | A | Model provenance tracking | Foundational |

**Mitigations:**
- B001: adversarial probing of all third-party models for backdoor triggers
- B003: formal vendor assessment for model providers
- Domain A: model provenance tracking; hash verification at deployment
- Model SBOM with version pinning

---

### DSGAI18 — Data Retention and Deletion Failures

GenAI systems retain personal data or training artefacts beyond required
retention periods or fail to honour deletion requests.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Data retention policy, deletion procedures, right-to-erasure | Foundational |
| Audit trails and logging | E | Retention compliance evidence | Foundational |

**Mitigations:**
- Domain A: documented retention periods for all GenAI data
- Domain A: deletion capability verification for each data store
- Domain E: audit evidence of retention policy compliance
- Automated retention enforcement and deletion scheduling

---

### DSGAI19 — Cascading Data Failures

Failures in data pipelines propagate through multiple GenAI components,
causing compounding degradation in downstream dependent systems.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Reliability domain (all) | D | Availability controls, circuit breakers, fault isolation | Foundational |
| Prevent unauthorized AI actions | B006 | Scope restrictions preventing cascade amplification | Foundational |
| Audit trails and logging | E | Cascade indicator logging for forensics | Foundational |

**Mitigations:**
- Domain D: circuit breaker pattern between pipeline stages
- Domain D: fail-safe state definition for all pipeline failures
- Domain E: cascade indicator logging for incident investigation
- Chaos engineering exercise for pipeline failure scenarios (B001)

---

### DSGAI20 — Regulatory Non-Compliance in Data Use

GenAI systems process personal data in ways that violate applicable law —
GDPR, CCPA, HIPAA, EU AI Act — through inadequate consent, cross-border
transfers, or prohibited processing.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Legal basis for data processing; consent management | Foundational |
| Safety domain | C | Safety controls addressing regulatory harm scenarios | Foundational |
| Accountability domain | E | Compliance evidence and audit trails | Foundational |
| Society domain | F | Transparency disclosures required by law | Foundational |

**Mitigations:**
- Domain A: map all applicable regulations; document legal basis for all processing
- Domain E: records of processing activities (GDPR Art. 30)
- Domain F: AI content disclosures (EU AI Act Art. 52)
- Domain C + A: DPIA for high-risk processing activities

---

### DSGAI21 — Data Provenance and Lineage Failures

GenAI systems cannot demonstrate where training data, retrieved
documents, or inference inputs originated — preventing audit and
traceability.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Provenance metadata requirements for all GenAI data | Foundational |
| Audit trails and logging | E | End-to-end lineage records | Foundational |

**Mitigations:**
- Domain A: provenance metadata attached to all ingested data
- Domain E: end-to-end lineage tracking from source to inference
- Automated provenance coverage tests in CI/CD
- Immutable lineage ledger for regulated deployments

---

## AIUC-1 certification readiness — DSGAI domain coverage

| AIUC-1 Domain | Primary DSGAI entries | Status |
|---|---|---|
| A — Data & Privacy | DSGAI02, DSGAI03, DSGAI06, DSGAI07, DSGAI08, DSGAI09, DSGAI14, DSGAI15, DSGAI18, DSGAI21 | |
| B — Security | DSGAI01, DSGAI04, DSGAI05, DSGAI10, DSGAI12, DSGAI16, DSGAI17 | |
| C — Safety | DSGAI05, DSGAI20 | |
| D — Reliability | DSGAI12, DSGAI19 | |
| E — Accountability | DSGAI02, DSGAI06, DSGAI09, DSGAI13, DSGAI18, DSGAI20, DSGAI21 | |
| F — Society | DSGAI20 | |

**Note:** Domain A covers over 50% of DSGAI entries — the data security
focus of AIUC-1 makes it exceptionally well-matched for the DSGAI taxonomy.

---

## References

- [AIUC-1 Standard](https://www.aiuc-1.com/)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [LLM_AIUC1.md](../llm-top10/LLM_AIUC1.md) — AIUC-1 for LLM deployments
- [Agentic_AIUC1.md](../agentic-top10/Agentic_AIUC1.md) — AIUC-1 for agentic deployments
- [DSGAI_ISO42001.md](DSGAI_ISO42001.md) — ISO 42001 AIMS controls complement AIUC-1 certification

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping DSGAI01–DSGAI21 to AIUC-1 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
