<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : SOC 2 Type II — AICPA Trust Services Criteria
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 x SOC 2

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [SOC 2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
— the AICPA's System and Organization Controls 2 report framework,
based on the Trust Services Criteria (TSC).

---

## Why SOC 2 for LLM security

SOC 2 is the most widely required security assurance framework for
SaaS and cloud service providers in North America and increasingly
globally. If your organisation offers LLM-powered services to
enterprise customers, builds AI products on cloud infrastructure,
or processes customer data through LLM pipelines, you almost
certainly face SOC 2 audit requirements from your customers.

SOC 2 differs from prescriptive frameworks like ISO 27001 or CIS
Controls — it does not mandate specific controls. Instead, it
requires that you demonstrate effective controls against five
Trust Services Criteria categories. The auditor assesses whether
your controls address the criteria, not whether you implemented
a specific safeguard.

This mapping answers the question: **which SOC 2 criteria does
each LLM Top 10 risk implicate, and what controls satisfy those
criteria for LLM-specific risks?**

---

## SOC 2 Trust Services Criteria

| Category | Code | Scope |
|---|---|---|
| Security | CC (Common Criteria) | CC1-CC9: Logical and physical access, change management, risk management, monitoring |
| Availability | A | System availability and performance commitments |
| Processing Integrity | PI | Complete, accurate, and authorised processing |
| Confidentiality | C | Protection of confidential information |
| Privacy | P | Personal information lifecycle management |

**Most LLM risks implicate Security (CC) criteria.** The Common
Criteria are the most directly relevant — CC6 (logical access),
CC7 (system operations and monitoring), CC8 (change management),
and CC9 (risk mitigation) map across all ten LLM Top 10 entries.
Confidentiality (C) and Privacy (P) apply wherever personal or
confidential data flows through LLM pipelines.

**SOC 2 audit focus for LLM applications:**
Auditors assessing LLM applications will focus on: whether prompt
injection risks are identified and treated in your risk management
programme (CC3, CC9), whether training data handling meets
confidentiality and privacy criteria (C1, P3-P5), whether model
and supply chain components are managed through change management
(CC8), and whether monitoring covers LLM-specific anomalies (CC7).

---

## SOC 2 criteria reference

| Criteria | Title | LLM relevance |
|---|---|---|
| CC1 | Control environment | Risk governance, policies, accountability |
| CC2 | Communication and information | Risk communication, disclosure |
| CC3 | Risk assessment | AI risk identification and treatment |
| CC4 | Monitoring activities | Continuous monitoring of controls |
| CC5 | Control activities | Policies, procedures, and controls |
| CC6 | Logical and physical access | Authentication, authorisation, access controls |
| CC7 | System operations | Change detection, incident response, monitoring |
| CC8 | Change management | Model updates, component changes, deployment |
| CC9 | Risk mitigation | Vendor risk, supply chain, contractual controls |
| C1 | Confidentiality policies | Confidential information handling policy |
| C2 | Confidential information protection | Encryption, access controls on confidential data |
| P1-P8 | Privacy criteria | Personal information collection, use, retention, disposal |

---

## Quick-reference summary

| ID | Name | Severity | Primary SOC 2 Criteria | Tier |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | CC3, CC7, CC5, CC6 | Foundational-Advanced |
| LLM02 | Sensitive Information Disclosure | High | C1, C2, CC6, P3, P5 | Foundational-Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | CC9, CC8, CC3, CC5 | Foundational-Hardening |
| LLM04 | Data and Model Poisoning | Critical | CC3, CC7, CC8, CC9 | Hardening-Advanced |
| LLM05 | Insecure Output Handling | High | CC5, CC7, PI1, CC3 | Foundational-Hardening |
| LLM06 | Excessive Agency | High | CC6, CC5, CC3, CC7 | Foundational-Hardening |
| LLM07 | System Prompt Leakage | High | C2, CC6, CC5, CC7 | Foundational-Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | C2, CC6, CC7, P5 | Hardening-Advanced |
| LLM09 | Misinformation | Medium | PI1, CC3, CC7, CC5 | Foundational-Hardening |
| LLM10 | Unbounded Consumption | Medium | A1, CC7, CC3, CC5 | Foundational-Hardening |

---

## Audience tags

- **CISO / compliance lead** — full file, SOC 2 criteria mapping for LLM programme
- **SOC 2 audit preparation team** — criteria-to-control mapping for auditor evidence
- **SaaS / cloud AI product team** — customer trust and vendor compliance context
- **Security engineer** — CC6/CC7 technical control implementation
- **DPO** — LLM02, LLM08 Privacy criteria entries
- **Sales / legal** — vendor trust and supply chain criteria (CC9, CC8)

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour. SOC 2 addresses this through CC3 (risk assessment —
prompt injection must be identified as a risk), CC7 (system operations
— monitoring must detect injection attempts), CC5 (control activities —
input validation procedures), and CC6 (logical access — LLM access
controls limit the damage from successful injection).

**Auditor expectation:** For LLM applications in scope of a SOC 2
audit, auditors will expect to see prompt injection identified in
the risk assessment (CC3.2), monitoring controls detecting anomalous
LLM behaviour (CC7.2), and documented input validation procedures
(CC5.2). Absence of injection-specific controls in an LLM application
is a SOC 2 gap finding.

#### SOC 2 criteria mapping

| Criteria | How it applies to prompt injection |
|---|---|
| CC3.2 — Risk assessment identifies threats and vulnerabilities | Prompt injection documented as a threat in LLM application risk assessment — vectors, likelihood, impact assessed |
| CC7.2 — Anomaly and threat detection | Runtime monitoring for prompt injection indicators on all LLM input channels — alerts integrated into SOC monitoring |
| CC5.2 — Select and develop control activities | Input validation procedures documented for all LLM integrations — implemented, tested, and reviewed |
| CC6.1 — Logical access restrictions | LLM access controls limit the blast radius of successful injection — least privilege enforced on all tool access |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document prompt injection as a risk in your LLM risk
  register (CC3.2 evidence) — vectors, likelihood, impact,
  treatment decision, owner, and review cadence
- Establish and document input validation procedures for
  all LLM integrations (CC5.2 evidence) — include in
  security policies and developer standards
- Deploy runtime monitoring for injection indicators
  (CC7.2 evidence) — integrate into SIEM, demonstrate
  alert and response capability to auditors

**Audit evidence preparation**
- Risk register entries showing prompt injection identified
  and treated (CC3.2)
- Input validation procedure documentation (CC5.2)
- Monitoring configuration and sample alerts (CC7.2)
- Security testing results showing injection resistance
  (CC5.2, CC7.4)

**Hardening**
- Establish structured adversarial testing programme
  covering injection scenarios — results documented as
  CC7.4 security testing evidence
- Implement architectural separation between system prompt
  and user input — documented as CC5.2 control activity
- Quarterly red team exercises — results shared with
  auditors as evidence of continuous improvement (CC4.1)

**Advanced**
- Implement injection detection with automated response —
  demonstrates CC7.3 evaluation of security events
- Include injection detection rate in security metrics
  reported to management (CC2.2 communication)
- Threat intelligence programme informing injection
  detection logic (CC9.2 threat intelligence)

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · NIST AI RMF MS-2.5 · NIST CSF 2.0 PR.PS-04

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, proprietary code, or confidential
information through outputs. This directly implicates SOC 2
Confidentiality (C) and Privacy (P) criteria — the most commercially
significant for SaaS providers whose customers include these criteria
in vendor security assessments.

**Auditor expectation:** Auditors will expect to see confidential
information identified and protected (C1, C2), personal information
handled per privacy commitments (P3-P5), and monitoring for data
leakage through LLM outputs (CC7.2). For SaaS providers with
customer data in LLM scope, C and P criteria are likely to be
included in the audit scope explicitly.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C1.1 — Confidentiality policy | Policy identifying confidential information in LLM scope and how it is handled — training data, RAG corpus, outputs |
| C2.1 — Confidential information protection | Technical controls protecting confidential data in LLM pipelines — encryption, access controls, output scanning |
| P3.1 — Personal information collection | Personal information in LLM scope identified — training data, RAG sources, outputs — collection documented |
| P5.1 — Personal information use | Personal information used only for purposes disclosed — LLM processing of customer PII limited to agreed use cases |
| CC6.1 — Logical access | Access controls on RAG data sources — users retrieve only data they are authorised to access |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document confidentiality policy covering LLM scope
  (C1.1 evidence) — identify what confidential information
  enters LLM pipelines, how it is classified, handled, protected
- Implement and document technical protection controls
  (C2.1 evidence) — encryption at rest and in transit,
  access-controlled retrieval, output redaction
- Document personal information handling procedures
  for LLM scope (P3.1, P5.1 evidence) — what PII enters
  LLM pipelines, lawful basis, retention, deletion

**Audit evidence preparation**
- Confidentiality and privacy policies covering LLM (C1.1, P3.1)
- Encryption configuration and access control documentation (C2.1)
- Data inventory showing PII in LLM scope (P3.1)
- DLP configuration and monitoring evidence (CC7.2)
- RAG access control configuration and testing results (CC6.1)

**Hardening**
- Deploy DLP monitoring on all LLM output channels —
  demonstrates C2.1 ongoing protection and CC7.2 monitoring
- Implement output redaction — document as C2.1 technical
  control for auditors
- Audit RAG access controls per quarter — demonstrates
  CC4.1 monitoring of access control effectiveness

**Advanced**
- Apply differential privacy in training — documented as
  C2.1 advanced technical control
- Conduct model inversion red team — demonstrates
  CC7.4 security testing of confidentiality controls
- Privacy impact assessment for LLM deployments —
  P1.1 privacy management evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity and Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference and Data Reconstruction
- Other frameworks: EU AI Act Art. 10 · GDPR Art. 25 · ISO 27001 A.8.11/A.8.12

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets,
libraries, and plugins. SOC 2 CC9 (risk mitigation — vendor and
third-party risk) is the primary criterion. CC8 (change management)
applies to model updates as system changes. Auditors increasingly
ask about AI-specific supply chain controls given the rapid growth
of model supply chain incidents.

**Auditor expectation:** Auditors will expect to see LLM component
vendors assessed under your vendor risk management programme (CC9.1,
CC9.2), model and component updates managed through change management
(CC8.1), and supply chain risks identified in the risk assessment
(CC3.2).

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC9.1 — Vendor risk management | LLM component vendors assessed before use — security questionnaires, SOC 2 reports reviewed, ongoing monitoring |
| CC9.2 — Vendor agreements | Contractual security obligations for LLM vendors — data handling, vulnerability disclosure, incident notification |
| CC8.1 — Change management | LLM model updates and component changes managed through change management — approval, testing, rollback |
| CC3.2 — Risk assessment | Supply chain attack vectors identified in LLM risk assessment — training data sources, model providers, plugin vendors |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Include LLM component vendors in vendor risk management
  programme (CC9.1 evidence) — security assessments,
  review of SOC 2 reports, ongoing monitoring
- Establish vendor agreements covering LLM-specific
  obligations (CC9.2 evidence) — data handling, vulnerability
  disclosure, incident notification, training data use restrictions
- Include model and component updates in change management
  process (CC8.1 evidence) — approval, testing, rollback
  capability documented

**Audit evidence preparation**
- Vendor risk assessment records for LLM component vendors (CC9.1)
- Vendor agreements with LLM security obligations (CC9.2)
- Change management records for model updates (CC8.1)
- ML SBOM as evidence of supply chain visibility (CC3.2, CC9.1)
- Risk register showing supply chain risks assessed (CC3.2)

**Hardening**
- Generate ML SBOM automatically — demonstrates CC9.1
  vendor monitoring capability to auditors
- Conduct vendor security assessments before any new
  LLM component enters production — CC9.1 evidence
- Version pinning and integrity verification in CI/CD —
  CC8.1 change management control evidence

**Advanced**
- Operate isolated model evaluation environment —
  demonstrates CC8.1 testing before production change
- Establish responsible disclosure with LLM vendors —
  CC9.2 contractual obligation evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model and Artifact Poisoning
- Other frameworks: ISO 27001 A.5.19/A.5.21 · NIST AI RMF MP-5.1 · NIST SP 800-218A

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Adversaries corrupt training data or model weights. SOC 2 CC3 (risk
assessment), CC7 (anomaly detection), CC8 (change management), and
CC9 (vendor risk) all apply. For SaaS providers offering AI products,
a poisoned model affecting customer data is a CC7 security event
requiring incident response and CC3 risk treatment.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC3.2 — Risk assessment | Data and model poisoning identified as threats in LLM risk assessment — training pipeline, supply chain, and model update vectors |
| CC7.2 — Threat detection | Anomaly detection on model outputs and training data distributions — poisoning indicators detected before operational impact |
| CC8.1 — Change management | Model promotions managed through change management — integrity verification before production deployment |
| CC9.1 — Vendor risk | Training data providers assessed — data provenance, quality, and integrity guarantees required from vendors |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document data and model poisoning in LLM risk assessment
  (CC3.2 evidence) — training data sources, fine-tuning
  pipeline, and supply chain attack vectors assessed
- Implement model integrity verification before production
  (CC8.1 evidence) — hash-based integrity check documented
  in change management procedures
- Include training data providers in vendor risk management
  (CC9.1 evidence) — data provenance and quality requirements
  in vendor agreements

**Audit evidence preparation**
- Risk register entries for data and model poisoning (CC3.2)
- Change management records showing integrity verification (CC8.1)
- Vendor assessment records for training data providers (CC9.1)
- Model output monitoring configuration and alerts (CC7.2)
- Incident response procedure for poisoning events (CC7.3)

**Hardening**
- Include poisoning detection in security testing programme —
  CC7.4 security testing evidence
- Implement training data anomaly detection — CC7.2
  monitoring evidence
- Model rollback capability — CC8.1 rollback procedure
  in change management records

**Advanced**
- Post-training backdoor detection as deployment gate —
  CC8.1 testing before production change evidence
- Continuous model output monitoring — CC7.2 ongoing
  anomaly detection evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory and Context Poisoning
- DSGAI 2026: DSGAI04 Data Model and Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032 · ISO 27001 A.8.27

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
injection attacks. SOC 2 Processing Integrity (PI1) applies —
LLM outputs are system processing outputs that must be complete,
accurate, and processed only in authorised ways. CC5 (control
activities) covers the input validation procedures that downstream
systems must implement.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| PI1.1 — Processing integrity policies | Policy requiring LLM output validation before use in downstream processing — complete and authorised processing |
| CC5.2 — Select and develop control activities | Input validation procedures for all systems consuming LLM output — encoding, schema validation, sanitisation |
| CC7.2 — Anomaly detection | Monitoring for injection patterns in LLM output channels — detect anomalous processing before downstream harm |
| CC3.2 — Risk assessment | Output injection risks identified in LLM risk assessment — XSS, SQL injection, command injection via AI-generated content |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document output validation procedures (CC5.2 evidence) —
  encoding, schema validation, and sanitisation requirements
  for all interfaces consuming LLM output
- Include output injection risks in LLM risk assessment
  (CC3.2 evidence) — downstream consumers assessed
- Document processing integrity policy for LLM outputs
  (PI1.1 evidence) — what constitutes authorised and
  valid LLM output processing

**Audit evidence preparation**
- Output validation procedure documentation (CC5.2, PI1.1)
- Risk assessment entries for output injection (CC3.2)
- Security testing results for output injection (CC7.4)
- Monitoring configuration for output channels (CC7.2)

**Hardening**
- Conduct DAST on all interfaces consuming LLM output —
  CC7.4 security testing evidence
- Implement output schema validation — CC5.2 documented
  control activity evidence
- Include output injection in security testing programme —
  CC7.4 results retained as audit evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity and Validation Failures
- Other frameworks: OWASP ASVS V5 · CIS Controls CIS 16 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with excessive autonomy execute unintended or harmful actions.
SOC 2 CC6 (logical access — least privilege) is the primary criterion.
CC5 (control activities — human oversight procedures) and CC3 (risk
assessment — autonomous action risks identified) also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC6.1 — Logical access restrictions | LLM tool access managed under least privilege — minimum scope, documented justification, regular review |
| CC6.3 — Access removal | LLM tool permissions removed promptly when no longer required — access review process covers LLM tool scope |
| CC5.2 — Control activities | Human oversight procedures for LLM autonomous actions — confirmation requirements documented and enforced |
| CC3.2 — Risk assessment | Excessive agency risks identified — what autonomous actions can the LLM take, what is the blast radius |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Manage LLM tool access under CC6.1 least privilege —
  document minimum scope justification, regular review
  schedule, access control configuration as audit evidence
- Document human oversight procedures (CC5.2 evidence) —
  which actions require human confirmation, who approves,
  how overrides are logged
- Include excessive agency in LLM risk assessment
  (CC3.2 evidence) — autonomous action vectors and
  blast radius documented

**Audit evidence preparation**
- LLM tool access control configuration showing least privilege (CC6.1)
- Access review records for LLM tool permissions (CC6.1, CC6.3)
- Human oversight procedure documentation (CC5.2)
- Risk assessment entries for excessive agency (CC3.2)
- Audit logs of LLM tool invocations (CC7.2)

**Hardening**
- Implement formal quarterly access reviews for LLM tool
  permissions — CC6.3 access removal evidence
- Deploy action guardrails as independent layer —
  CC5.2 documented control activity
- Log all LLM tool invocations — CC7.2 monitoring evidence

**Advanced**
- Red team testing of excessive agency via injection —
  CC7.4 security testing evidence
- Formally specify permitted action graphs — CC5.2
  detailed control activity documentation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin and Agent Data Exchange
- Other frameworks: EU AI Act Art. 14 · AIUC-1 B006 · ISO 27001 A.8.2

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions are extracted.
SOC 2 Confidentiality (C2) applies — system prompts may contain
confidential business logic and security controls that qualify
as confidential information. CC6 (logical access — restricting
access to system prompts) and CC5 (procedures for prompt security)
also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | System prompts classified as confidential — encryption at rest, access-controlled, not in cleartext config |
| CC6.1 — Logical access | Access controls on system prompt storage — only authorised personnel can read or modify, all access logged |
| CC5.2 — Control activities | System prompt security procedures — version control, rotation, extraction resistance testing documented |
| CC7.2 — Monitoring | Access to system prompt storage monitored — anomalous access attempts detected and alerted |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Classify and document system prompts as confidential
  information (C2.1 evidence) — encryption at rest,
  access-controlled, policy documented
- Implement access controls on system prompt storage
  (CC6.1 evidence) — access control configuration,
  authorised accessor list, access logs
- Document system prompt security procedures (CC5.2 evidence) —
  version control, rotation schedule, extraction testing

**Audit evidence preparation**
- System prompt classification and protection documentation (C2.1)
- Access control configuration and accessor records (CC6.1)
- Version control and rotation records (CC5.2)
- Extraction testing results (CC7.4)
- Access monitoring configuration and alerts (CC7.2)

**Hardening**
- Conduct prompt extraction testing — CC7.4 security
  testing evidence demonstrating extraction resistance
- Implement system prompt rotation — CC5.2 procedure
  evidence showing ongoing maintenance of controls
- Log all access to system prompts — CC7.2 monitoring
  and CC6.1 access traceability evidence

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · CWE-200 · ISO 27001 A.5.12

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in vector stores enable adversarial retrieval and
embedding inversion. SOC 2 Confidentiality (C2) applies if
embeddings contain confidential information. Privacy (P5) applies
if embeddings encode personal data — the ENISA pseudonymisation
guidance position that embeddings of personal data are personal
data is increasingly reflected in SOC 2 audit expectations.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | Embeddings of confidential information protected — encrypted at rest, access-controlled, inversion-resistant |
| CC6.1 — Logical access | RBAC on all vector store collections — no unauthenticated access in any environment |
| CC7.2 — Anomaly detection | Anomaly detection on vector store query patterns — bulk extraction and unusual retrieval volumes detected |
| P5.1 — Personal information use | Embeddings of personal data used only for authorised purposes — privacy commitments apply to derived forms |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document embeddings as confidential/personal information
  where applicable (C2.1, P5.1 evidence) — classification,
  protection requirements, authorised use cases
- Implement RBAC on vector stores (CC6.1 evidence) —
  access control configuration, access logs
- Deploy query monitoring (CC7.2 evidence) — alert
  configuration, sample alerts for auditors

**Audit evidence preparation**
- Embedding classification and protection documentation (C2.1)
- Vector store access control configuration (CC6.1)
- Query monitoring configuration and alerts (CC7.2)
- Encryption configuration for vector stores at rest (C2.1)
- Privacy documentation for embeddings of personal data (P5.1)

**Hardening**
- Conduct embedding inversion testing — CC7.4 security
  testing evidence showing protection effectiveness
- Apply differential privacy in embedding generation —
  C2.1 advanced technical control evidence
- Patch all known vector database CVEs — CC8.1
  change management evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- Agentic Top 10: ASI06 Memory and Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference and Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · ISO 27001 A.8.3/A.8.24 · GDPR Recital 26

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but incorrect content. SOC 2 Processing
Integrity (PI1) applies — LLM outputs are processing results that
must be complete and accurate for the purposes for which they are
used. CC3 (risk assessment — misinformation harm identified) and
CC7 (monitoring — accuracy degradation detected) also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| PI1.1 — Processing integrity policy | Policy on LLM output accuracy — acceptable accuracy thresholds, verification requirements for high-stakes use cases |
| PI1.2 — System inputs are complete and accurate | LLM inputs (RAG sources, training data) quality controls — authoritative, current, verified sources |
| CC3.2 — Risk assessment | Misinformation risk identified in LLM risk assessment — harm potential of incorrect outputs per use case |
| CC7.2 — Anomaly detection | Production monitoring for accuracy degradation and hallucination patterns — drift detection |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document processing integrity policy for LLM outputs
  (PI1.1 evidence) — accuracy thresholds, verification
  requirements for high-stakes use cases
- Document RAG source quality controls (PI1.2 evidence) —
  authoritative sources, version control, freshness controls
- Include misinformation in LLM risk assessment
  (CC3.2 evidence) — harm potential per use case

**Audit evidence preparation**
- Processing integrity policy for LLM (PI1.1)
- RAG source governance documentation (PI1.2)
- Risk assessment entries for misinformation (CC3.2)
- Production accuracy monitoring configuration (CC7.2)
- User communication on LLM output limitations (CC2.1)

**Hardening**
- Implement production accuracy monitoring — CC7.2
  ongoing monitoring evidence
- Deploy confidence scoring — PI1.1 processing integrity
  control evidence
- Conduct domain-specific accuracy testing — CC7.4
  security testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation and Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 F · NIST CSF 2.0 GV.OC-01

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption.
SOC 2 Availability (A1) is the primary criterion — availability
commitments require that the system operates as documented and
resource exhaustion attacks are protected against. CC7 (monitoring
— consumption anomalies detected) and CC3 (risk assessment —
DoS risks identified) also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| A1.1 — Availability policies | LLM service availability commitments documented — SLAs, RTO/RPO, resource limits that protect availability |
| A1.2 — Environmental protections | Rate limiting and resource controls protect LLM service availability — implemented and monitored |
| CC7.2 — Anomaly detection | Real-time monitoring of LLM resource consumption — cost anomalies and unusual volume patterns alerted |
| CC3.2 — Risk assessment | Resource exhaustion risks identified in LLM risk assessment — DoS and sponge attack vectors assessed |

#### Mitigations for SOC 2 evidence

**Control implementation**
- Document LLM service availability commitments (A1.1
  evidence) — SLAs, RTO/RPO, resource protection measures
- Implement and document rate limiting and resource controls
  (A1.2 evidence) — configuration documentation showing
  limits enforced
- Include resource exhaustion in LLM risk assessment
  (CC3.2 evidence) — DoS and cost amplification vectors

**Audit evidence preparation**
- LLM service availability policy and commitments (A1.1)
- Rate limiting and resource control configuration (A1.2)
- Risk assessment entries for resource exhaustion (CC3.2)
- Consumption monitoring configuration and alerts (CC7.2)
- Incident response procedure for availability events (CC7.3)

**Hardening**
- Define and test BCP for LLM service failures — A1.2
  environmental protection and CC9.1 resilience evidence
- Implement per-tenant cost budgets — A1.2 availability
  protection evidence
- Conduct adversarial load testing — CC7.4 testing evidence

**Advanced**
- Deploy sponge example detection — A1.2 advanced
  protection evidence
- Conduct availability incident drills — CC7.3 incident
  response preparedness evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability and Resilience Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · CIS Controls CIS 12 · NIST CSF 2.0 PR.IR-01

---

## SOC 2 audit preparation checklist for LLM applications

### Risk management (CC3)

- [ ] Prompt injection documented in LLM risk register (CC3.2)
- [ ] Data and model poisoning documented in LLM risk register (CC3.2)
- [ ] Supply chain risks documented in LLM risk register (CC3.2)
- [ ] Excessive agency risks documented with blast radius (CC3.2)
- [ ] Resource exhaustion risks documented (CC3.2)

### Control activities (CC5)

- [ ] Input validation procedures for LLM integrations (CC5.2)
- [ ] Output validation procedures for all LLM consumers (CC5.2)
- [ ] Human oversight procedures for LLM autonomous actions (CC5.2)
- [ ] System prompt security procedures (CC5.2)
- [ ] LLM component change management procedures (CC8.1)

### Logical access (CC6)

- [ ] LLM tool access managed as privileged access — least privilege (CC6.1)
- [ ] Quarterly access reviews for LLM tool permissions (CC6.1, CC6.3)
- [ ] Access controls on RAG data sources verified (CC6.1)
- [ ] RBAC on all vector stores enabled (CC6.1)
- [ ] System prompt access controls in place (CC6.1)

### Monitoring (CC7)

- [ ] Runtime monitoring for injection indicators (CC7.2)
- [ ] DLP monitoring on LLM output channels (CC7.2)
- [ ] Model output anomaly detection active (CC7.2)
- [ ] Production accuracy and hallucination monitoring (CC7.2)
- [ ] Resource consumption monitoring with alerts (CC7.2)
- [ ] Security testing programme covering LLM Top 10 (CC7.4)

### Vendor risk (CC9)

- [ ] LLM component vendors in vendor risk management programme (CC9.1)
- [ ] Vendor agreements with LLM-specific obligations (CC9.2)
- [ ] Training data providers assessed (CC9.1)
- [ ] ML SBOM maintained for supply chain visibility (CC9.1)

### Confidentiality and privacy (C, P)

- [ ] Confidential information in LLM scope identified and classified (C1.1)
- [ ] Technical protection controls for confidential LLM data (C2.1)
- [ ] Personal information in LLM scope documented (P3.1)
- [ ] Personal information use limitations enforced (P5.1)
- [ ] Embeddings of personal data classified and protected (C2.1, P5.1)

### Availability (A)

- [ ] LLM service availability commitments documented (A1.1)
- [ ] Rate limiting and resource controls protecting availability (A1.2)
- [ ] BCP coverage for LLM service failures (A1.2)

---

## Implementation priority

| Phase | LLM entries | SOC 2 criteria | Rationale |
|---|---|---|---|
| 1 — Audit readiness | LLM01, LLM02, LLM03 | CC3, CC9, C1/C2 | Risk register, vendor risk, and data classification are the first auditor asks |
| 2 — This sprint | LLM06, LLM07, LLM10 | CC6, CC5, A1 | Access control, configuration security, and availability commitments |
| 3 — This quarter | LLM04, LLM05 | CC8, CC7, PI1 | Change management and monitoring programme for integrity and output security |
| 4 — Ongoing | LLM08, LLM09 | C2, P5, CC7 | Embedding security and accuracy monitoring hardening |

---

## References

- AICPA SOC 2 Trust Services Criteria: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
- AICPA Trust Services Criteria 2017 (updated 2022): https://us.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria.pdf
- OWASP LLM Top 10 2025: https://genai.owasp.org/llm-top-10/
- ENISA AI Cybersecurity recommendations: https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-25 | 2026-Q1 | Initial mapping — LLM01-LLM10 full entries with SOC 2 audit preparation checklist | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
