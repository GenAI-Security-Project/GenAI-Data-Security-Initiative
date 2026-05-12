<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01–DSGAI21)
  Framework   : CIS Controls v8.1
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × CIS Controls v8.1

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [CIS Controls v8.1](https://www.cisecurity.org/controls)
— the Center for Internet Security's prioritised set of cyber defence safeguards,
organised into 18 control groups with Implementation Groups (IG1/IG2/IG3) scaling
from small organisations to enterprise security programmes.

CIS Controls are the most action-oriented security framework available — every
safeguard names a specific tool, activity, or configuration to implement. For
DSGAI risks, the most critical controls are data protection (CIS 3), access control
(CIS 6), audit log management (CIS 8), application software security (CIS 16),
and service provider management (CIS 15) — covering the full GenAI data lifecycle
from training through inference.

---

## CIS Controls structure

| Group | Controls | Scope |
|---|---|---|
| Basic hygiene (IG1) | CIS 1–6 | Asset inventory, data protection, secure config, account management, access control |
| Foundational (IG2) | CIS 7–11 | Vulnerability management, audit logs, malware, network monitoring |
| Organisational (IG3) | CIS 12–18 | Network monitoring, security awareness, app security, incident response, pen testing |

**Implementation Groups:**
- IG1 — Essential cyber hygiene, all organisations
- IG2 — IG1 + additional controls for organisations handling sensitive data
- IG3 — IG2 + advanced controls for enterprise and regulated industries

---

## Quick-reference summary

| ID | Name | Severity | Primary CIS Controls | IG | Tier | Scope |
|---|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | CIS 3, CIS 8, CIS 16 | IG1–IG3 | Foundational–Advanced | Both |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | CIS 5, CIS 6, CIS 12 | IG1–IG3 | Foundational–Advanced | Both |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | CIS 2, CIS 4, CIS 13 | IG1–IG3 | Foundational–Hardening | Both |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | CIS 7, CIS 16, CIS 18 | IG2–IG3 | Hardening–Advanced | Both |
| DSGAI05 | Data Integrity & Validation Failures | High | CIS 16, CIS 8 | IG2–IG3 | Foundational–Hardening | Build |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | CIS 4, CIS 6, CIS 15 | IG1–IG3 | Foundational–Hardening | Both |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | CIS 3, CIS 1, CIS 8 | IG1–IG3 | Foundational–Advanced | Both |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | CIS 3, CIS 8, CIS 17 | IG1–IG3 | Foundational–Advanced | Both |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | CIS 3, CIS 13, CIS 16 | IG2–IG3 | Hardening–Advanced | Both |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | CIS 3, CIS 18 | IG2–IG3 | Hardening–Advanced | Build |
| DSGAI11 | Cross-Context Conversation Bleed | High | CIS 3, CIS 6, CIS 16 | IG1–IG3 | Foundational–Hardening | Build |
| DSGAI12 | Unsafe NL Data Gateways | Critical | CIS 16, CIS 6, CIS 18 | IG2–IG3 | Foundational–Advanced | Build |
| DSGAI13 | Vector Store Platform Security | High | CIS 3, CIS 6, CIS 16 | IG2–IG3 | Foundational–Hardening | Both |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | CIS 8, CIS 3, CIS 6 | IG1–IG3 | Foundational–Hardening | Build |
| DSGAI15 | Over-Broad Context Windows | High | CIS 3, CIS 6, CIS 16 | IG1–IG3 | Foundational–Hardening | Build |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | CIS 2, CIS 4, CIS 10 | IG1–IG3 | Foundational–Hardening | Both |
| DSGAI17 | Data Availability & Resilience Failures | High | CIS 11, CIS 13 | IG1–IG3 | Foundational–Advanced | Both |
| DSGAI18 | Inference & Data Reconstruction | High | CIS 3, CIS 18 | IG2–IG3 | Hardening–Advanced | Both |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | CIS 3, CIS 6, CIS 14 | IG1–IG2 | Foundational–Hardening | Both |
| DSGAI20 | Model Exfiltration & IP Replication | High | CIS 6, CIS 8, CIS 18 | IG2–IG3 | Hardening–Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | CIS 7, CIS 16, CIS 18 | IG2–IG3 | Hardening–Advanced | Both |

---

## Audience tags

- **Security programme lead** — full file, use as GenAI security roadmap anchored to CIS Controls
- **IT security / sysadmin** — CIS 1–6 hygiene controls, most actionable for small teams
- **AppSec engineer** — CIS 16 application security, CIS 18 penetration testing
- **SOC analyst** — CIS 8 audit logging, CIS 13 network monitoring
- **CISO** — implementation group guidance for communicating security posture to leadership
- **Compliance** — DSGAI08 for regulatory mapping, IG guidance for tiered compliance evidence

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

PII, financial data, credentials, and proprietary content exposed through model
outputs, RAG over-retrieval, training data memorisation, or inadequate output filtering.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.1 — Establish and maintain data management process | CIS 3 | Document all GenAI data stores — training data, vector stores, model outputs — and apply data handling procedures | IG1 | Foundational | Both |
| 3.13 — Deploy DLP solutions | CIS 3 | DLP tooling deployed on model output channels — detects and blocks PII, credentials, and sensitive patterns | IG2 | Hardening | Both |
| 8.2 — Collect audit logs | CIS 8 | All model inference requests and responses logged with user identity for disclosure incident investigation | IG1 | Foundational | Both |
| 16.12 — Implement code-level security checks | CIS 16 | Output sanitisation and redaction implemented and tested as part of application security review | IG2 | Hardening | Build |

#### Mitigations by tier

**Foundational (IG1)**
- Inventory all GenAI data stores and classify all data by sensitivity
- Implement output redaction for PII and credentials on all model response channels
- Enforce deny-by-default access control on RAG data sources

**Hardening (IG2)**
- Deploy DLP on model output pipelines
- Audit RAG retrieval scope regularly — over-permissive indexes drive most incidents

**Advanced (IG3)**
- Conduct model inversion red team exercises (CIS 18.1)
- Implement machine unlearning for post-deployment data removal

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.12 — ASVS V8 — CWE-200

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

Agent credentials, API keys, and tokens embedded in prompts, logs, or memory
expose agent identity to compromise — potentially cascading to all services
the agent can access.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 5.4 — Restrict administrator privileges | CIS 5 | Agent service accounts restricted to minimum required permissions — no shared high-privilege accounts | IG1 | Foundational | Both |
| 6.5 — Require MFA for admin access | CIS 6 | Management interfaces for AI service accounts protected with MFA | IG1 | Foundational | Both |
| 5.3 — Disable dormant accounts | CIS 5 | Inactive agent credentials disabled — credential lifecycle managed with automated expiry | IG1 | Foundational | Both |
| 12.7 — Deploy host-based intrusion detection | CIS 12 | Credential theft detection on systems hosting agent workloads | IG2 | Hardening | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Store all agent credentials in secrets managers — never in prompts, code, or logs
- Apply least privilege to all agent service accounts
- Rotate agent credentials on a defined schedule

**Hardening (IG2)**
- Implement JIT credential issuance — scoped per task, auto-expired
- Monitor credential usage for anomalous access patterns

**Advanced (IG3)**
- Deploy workload identity (SPIFFE/SPIRE) for multi-agent environments
- Implement per-session ephemeral credentials with automatic revocation

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://github.com/hashicorp/vault |
| SPIRE | Open-source | https://github.com/spiffe/spire |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.5.17 — ASVS V2 — CWE-312

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unauthorised AI tools to process sensitive business data —
bypassing governance controls and creating uncontrolled data copies.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 2.1 — Maintain authorised software inventory | CIS 2 | Inventory of all AI tools in use maintained — shadow AI tools identified and reviewed | IG1 | Foundational | Both |
| 4.1 — Establish secure configuration | CIS 4 | Secure configuration baselines for AI tool usage — approved tools configured with organisational settings | IG1 | Foundational | Both |
| 13.4 — Perform traffic filtering | CIS 13 | Egress filtering blocking data transmission to unapproved AI service domains | IG2 | Hardening | Both |
| 14.6 — Train workforce on AI security | CIS 14 | Security awareness training covers shadow AI risks and acceptable AI tool usage policy | IG1 | Foundational | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Publish and enforce an approved AI tools register
- Include shadow AI in acceptable use policy
- Conduct security awareness training on shadow AI risks

**Hardening (IG2)**
- Implement egress filtering blocking unapproved AI service domains
- Deploy CASB to detect shadow AI tool usage

**Advanced (IG3)**
- Monitor network traffic for shadow AI usage patterns (CIS 13.8)
- Automated discovery of new AI tools before they become entrenched

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDLP | Open-source | https://github.com/ezarko/opendlp |
| Zscaler Internet Access | Commercial | https://www.zscaler.com |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- Other frameworks: ISO 27001 A.5.23 — ASVS V14 — ENISA L3-GRC

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Adversarial data injected into training datasets, fine-tuning corpora, or RAG
stores alters model behaviour — introducing backdoors, biases, or targeted
misinformation persisting into production.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 7.1 — Establish vulnerability management | CIS 7 | GenAI components — models, datasets, plugins — included in vulnerability management programme | IG1 | Foundational | Both |
| 16.11 — Use up-to-date software components | CIS 16 | Training data sources and model components reviewed for known poisoning incidents before use | IG2 | Hardening | Both |
| 18.1 — Establish penetration testing programme | CIS 18 | Red team exercises include data poisoning attack scenarios against training and RAG pipelines | IG3 | Advanced | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Implement data validation on all training and fine-tuning ingestion pipelines
- Restrict write access to training data stores

**Hardening (IG2)**
- Generate and version a Dataset Bill of Materials (DBoM) per training run
- Apply statistical outlier detection before training

**Advanced (IG3)**
- Certified data provenance with cryptographic attestation
- Red team training and RAG pipelines specifically for poisoning vectors

#### Tools

| Tool | Type | Link |
|---|---|---|
| Cleanlab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 — ASVS V10 — CWE-345

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

Absence of validation on data entering or leaving GenAI systems enables injection
attacks, silent data corruption, and security bypasses in downstream systems.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 16.1 — Establish secure coding practices | CIS 16 | Secure coding standards cover input validation and output encoding for all GenAI pipeline components | IG2 | Foundational | Build |
| 8.5 — Collect detailed audit logs | CIS 8 | Validation failures logged with sufficient context for incident investigation | IG2 | Foundational | Build |

#### Mitigations by tier

**Foundational (IG1–IG2)**
- Treat all data entering GenAI pipelines as untrusted — validate against defined schema
- Implement output validation on all model response channels
- Log validation failures server-side with context

**Hardening (IG2–IG3)**
- Apply allowlist-based validation on NL gateway inputs
- Include data integrity checks in CI/CD pipeline gates

**Advanced (IG3)**
- Deploy continuous data quality monitoring across pipeline stages
- Conduct application security review of all validation logic

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Other frameworks: ISO 27001 A.8.28 — ASVS V5 — CWE-20

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

Data exchanged between LLMs and external tools or plugins bypasses standard security
controls — enabling data exposure, injection via tool outputs, or exfiltration.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 4.2 — Maintain secure configuration of cloud assets | CIS 4 | Cloud-based plugins and tools configured securely — no default credentials or unnecessary permissions | IG1 | Foundational | Both |
| 6.4 — Require password manager | CIS 6 | Tool API keys managed in secrets managers — not hardcoded in agent configuration | IG1 | Foundational | Both |
| 15.1 — Establish service provider management policy | CIS 15 | Security requirements for all plugin and tool providers documented and reviewed before integration | IG2 | Hardening | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Apply least privilege to all plugin and tool data access
- Validate all tool outputs before returning to the model
- Log all tool invocations with input, output, and caller identity

**Hardening (IG2)**
- Per-session tool scope — agents receive only needed tools per task
- Schema validation on all plugin input and output channels

**Advanced (IG3)**
- Behaviour anomaly detection on tool invocation patterns (CIS 13.8)
- Formal security review of all plugin providers (CIS 15.2)

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Tool Misuse, ASI07 Insecure Inter-Agent Communication
- Other frameworks: ISO 27001 A.5.19 — ASVS V4 — AIUC-1 B006

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

Absence of data classification and lifecycle management causes over-retention,
unclear data ownership, and inability to fulfil deletion obligations under
privacy regulations.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.2 — Establish data inventory | CIS 3 | Comprehensive inventory of all GenAI data stores — training data, vector stores, fine-tuning sets — maintained and current | IG1 | Foundational | Both |
| 3.3 — Configure data access control lists | CIS 3 | Access control lists on GenAI data stores based on data classification | IG1 | Foundational | Both |
| 3.11 — Encrypt sensitive data at rest | CIS 3 | Training corpora and vector stores containing sensitive data encrypted at rest | IG1 | Foundational | Both |
| 8.3 — Ensure adequate audit log storage | CIS 8 | Data governance events — classification changes, retention actions, deletion — logged and retained | IG1 | Foundational | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Classify all training and RAG data before ingestion
- Assign data owners for all AI datasets
- Define and enforce data retention schedules

**Hardening (IG2)**
- Implement automated data classification on ingestion pipelines
- Enforce automated deletion of data past retention period

**Advanced (IG3)**
- Implement machine unlearning to support deletion obligations (CIS 3.10)
- Regular data lineage audits (CIS 18.2)

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| Amundsen | Open-source | https://github.com/amundsen-io/amundsen |

#### Cross-references
- Other frameworks: ISO 27001 A.5.12 — GDPR Art. 5 — ENISA L3-GRC

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems process data in ways violating GDPR, EU AI Act, HIPAA, PCI DSS,
or other regulatory obligations through consent failures or cross-border transfers.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.1 — Data management process | CIS 3 | Data management process documents regulatory requirements applicable to all GenAI data processing activities | IG1 | Foundational | Both |
| 8.2 — Collect audit logs | CIS 8 | Compliance-relevant events logged with sufficient fidelity to demonstrate regulatory compliance | IG1 | Foundational | Both |
| 17.1 — Incident response management | CIS 17 | Incident response plan covers regulatory notification obligations for AI-related data breaches | IG1 | Foundational | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Map all personal data flows through GenAI systems — document lawful basis
- Implement data subject rights (access, deletion, portability) for AI-processed data
- Conduct DPIA for all high-risk AI deployments

**Hardening (IG2)**
- Automated compliance monitoring — detect processing beyond declared purpose
- Maintain records of processing activities covering GenAI data uses

**Advanced (IG3)**
- Privacy-by-design implementation — federated learning, differential privacy
- Annual regulatory compliance audit against AI-specific requirements

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| OneTrust | Commercial | https://www.onetrust.com |

#### Cross-references
- Other frameworks: ISO 27001 A.5.31 — EU AI Act Art. 9-15 — GDPR Art. 35

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Sensitive data in images, audio, or documents processed by multimodal AI is
disclosed through model outputs — bypassing text-only DLP controls.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.13 — Deploy DLP solutions | CIS 3 | DLP extended to cover non-text modalities — images, audio, documents — entering and leaving GenAI systems | IG2 | Hardening | Both |
| 13.1 — Centralise security event alerting | CIS 13 | Multimodal data exfiltration events surfaced in central SIEM | IG2 | Hardening | Both |
| 16.12 — Implement code-level security checks | CIS 16 | Multimodal input handling code reviewed for data leakage paths | IG2 | Hardening | Both |

#### Mitigations by tier

**Foundational (IG1–IG2)**
- Extend DLP to all non-text modalities
- Implement content scanning for images, audio, and documents before ingestion

**Hardening (IG2–IG3)**
- Deploy multimodal-aware PII detection
- Apply data minimisation — pass only required fields, not full documents

**Advanced (IG3)**
- Multimodal-specific red team exercises (CIS 18.1)
- Output filtering for responses derived from multimodal inputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Azure AI Content Safety | Commercial | https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.11 — ASVS V5 — ENISA L2-DP

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data generation and anonymisation techniques fail to prevent
re-identification — enabling reconstruction of original PII through linkage attacks.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.7 — Establish data classification scheme | CIS 3 | Synthetic data classified appropriately — residual re-identification risk assessed and documented | IG1 | Hardening | Build |
| 18.3 — Remediate penetration test findings | CIS 18 | Re-identification testing results treated as penetration test findings — tracked to remediation | IG3 | Advanced | Build |

#### Mitigations by tier

**Foundational (IG1)**
- Do not treat synthetic data as inherently safe
- Apply k-anonymity (k≥5) to all synthetic datasets before training use

**Hardening (IG2)**
- Test anonymised datasets with linkage attacks before production use
- Document re-identification risk assessment per dataset

**Advanced (IG3)**
- Implement differential privacy (ε ≤ 1.0) for high-sensitivity datasets
- Quarterly re-identification testing as external datasets evolve

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| ARX Anonymisation Tool | Open-source | https://github.com/arx-deidentifier/arx |
| SDV (Synthetic Data Vault) | Open-source | https://github.com/sdv-dev/SDV |

#### Cross-references
- Other frameworks: ISO 27001 A.8.11 — GDPR Recital 26 — ENISA L2-DP

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Conversation history or user data from one session bleeds into another user's
session through inadequate context isolation or cache management.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.3 — Configure data access control lists | CIS 3 | Context storage namespaced per user — cross-user access to conversation context blocked | IG1 | Foundational | Build |
| 6.2 — Establish allowlist of authorised software | CIS 6 | Session management libraries for LLM applications reviewed and approved | IG1 | Foundational | Build |
| 16.6 — Establish security requirements | CIS 16 | Session isolation requirements defined in application security specifications | IG2 | Foundational | Build |

#### Mitigations by tier

**Foundational (IG1)**
- Implement strict session isolation — each user's context completely isolated
- Clear conversation context on session termination
- Never cache responses in shared layers without per-user namespacing

**Hardening (IG2)**
- Audit session management logic specifically for AI context persistence
- Session isolation tests in CI/CD

**Advanced (IG3)**
- Adversarial testing targeting cross-session data leakage (CIS 18.1)
- Context isolation verification as automated test on every deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Burp Suite Community | Open-source | https://portswigger.net/burp/communitydownload |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.3 — ASVS V3 — CWE-200

---

### DSGAI12 — Unsafe NL Data Gateways

**Severity:** Critical

Natural language interfaces used as gateways to databases or APIs allow prompt
injection or poorly validated NL-to-query translation to bypass access controls.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 16.2 — Establish secure configuration for software | CIS 16 | NL data gateway applications configured to parameterise all generated queries — no raw model output executed | IG2 | Foundational | Build |
| 6.3 — Require password manager for service accounts | CIS 6 | NL gateway service credentials managed — least privilege applied to data source access | IG1 | Foundational | Build |
| 18.1 — Establish penetration testing programme | CIS 18 | Red team exercises include NL injection attack scenarios against all NL data gateways | IG3 | Advanced | Build |

#### Mitigations by tier

**Foundational (IG1–IG2)**
- Parameterise all LLM-generated queries — never execute raw model output
- Apply same access control as the underlying data source
- Log all NL gateway queries with translated query and user identity

**Hardening (IG2–IG3)**
- Query schema allowlisting — limit tables and operations NL gateway can generate
- Rate limiting and result size limits on all NL gateway endpoints

**Advanced (IG3)**
- Red team specifically for NL-to-SQL injection vectors (CIS 18.1)
- Query intent verification — flag enumeration patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| SQLFluff | Open-source | https://github.com/sqlfluff/sqlfluff |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM01 Prompt Injection
- Other frameworks: ASVS V5.3 — CWE-89 — OWASP Top 10 A3

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector stores lack standard security controls — allowing unauthorised access,
adversarial vector injection, and extraction of sensitive source content.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.11 — Encrypt sensitive data at rest | CIS 3 | Embedding vectors encrypted at rest — prevents inversion attacks and raw data extraction | IG1 | Foundational | Both |
| 6.1 — Establish access control inventory | CIS 6 | Access permissions to vector store namespaces inventoried and reviewed | IG1 | Foundational | Both |
| 16.7 — Use standard-security components | CIS 16 | Vector store platforms assessed for security configuration before production deployment | IG2 | Hardening | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Implement RBAC on all vector store namespaces
- Validate all content before embedding generation
- Monitor ingestion for anomalous content

**Hardening (IG2)**
- Encrypt vectors at rest and in transit
- Trust-tiered retrieval weighted by source provenance

**Advanced (IG3)**
- Embedding inversion red team exercises (CIS 18.1)
- Differential privacy in embedding generation for sensitive corpora

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Other frameworks: ISO 27001 A.8.3 — ASVS V6 — CWE-327

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Logging and telemetry systems capture and retain sensitive data from model
interactions — creating high-value targets containing conversation content and PII.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 8.2 — Collect audit logs | CIS 8 | Audit logs capture security-relevant events without capturing sensitive conversation content | IG1 | Foundational | Build |
| 8.10 — Retain audit logs | CIS 8 | Log retention policy defined — sensitive content logs retained for minimum required period then deleted | IG1 | Foundational | Build |
| 3.13 — Deploy DLP on log pipelines | CIS 3 | DLP applied to telemetry pipelines — PII and credentials redacted before log storage | IG2 | Hardening | Build |
| 6.3 — Access control on log infrastructure | CIS 6 | Log and monitoring stores protected with the same access rigour as production systems | IG1 | Foundational | Build |

#### Mitigations by tier

**Foundational (IG1)**
- Redact PII, credentials, and sensitive content from logs at collection time
- Apply access control to logging infrastructure as strictly as production data

**Hardening (IG2)**
- Define log retention policy — logs held only for minimum required period
- Encrypt logs at rest and in transit

**Advanced (IG3)**
- Log integrity monitoring — detect tampering with audit logs
- Anomaly detection on log access patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Fluent Bit | Open-source | https://github.com/fluent/fluent-bit |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.15 — ASVS V7 — ENISA L1-LOG

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Excessively large context windows aggregate data from multiple trust domains into
a single namespace — enabling cross-source leakage and context poisoning.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.3 — Configure data access control lists | CIS 3 | Context window population controlled by explicit allow rules based on data classification | IG1 | Foundational | Build |
| 3.1 — Data minimisation | CIS 3 | Context windows populated with minimum data necessary — not maximum available | IG1 | Foundational | Build |
| 16.6 — Security requirements | CIS 16 | Context window size and composition limits defined as security requirements in application design | IG2 | Hardening | Build |

#### Mitigations by tier

**Foundational (IG1)**
- Enforce data minimisation on context window population
- Maintain trust-domain separation within context
- Set explicit context window size limits

**Hardening (IG2)**
- Context window auditing — log what data enters each inference call
- Context redaction before passing sensitive data classes to model

**Advanced (IG3)**
- Context window policy enforcement as independent control (CIS 16.7)
- Red team context population logic for cross-source leakage

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM07 System Prompt Leakage
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3 — ASVS V4 — ENISA L2-DP

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Browser-integrated and endpoint AI assistants access data beyond their declared
scope — reading clipboard, files, or browsing history without per-action authorisation.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 2.6 — Allowlist authorised software | CIS 2 | Browser AI extensions and endpoint assistants on approved software list — unapproved tools blocked | IG1 | Foundational | Both |
| 4.1 — Secure configuration baseline | CIS 4 | Endpoint AI tools configured to minimum required permissions — over-permissive defaults locked down | IG1 | Foundational | Both |
| 10.1 — Deploy anti-malware | CIS 10 | Endpoint AI tools vetted for malicious behaviour — included in endpoint security monitoring | IG1 | Foundational | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Restrict endpoint AI assistant OS permissions to minimum declared functionality
- Review and restrict browser extension permissions before deployment
- Include endpoint AI tools in application security review

**Hardening (IG2)**
- Monitor endpoint AI tool network activity
- Application allowlisting to control which AI assistants run on managed endpoints

**Advanced (IG3)**
- Security assessment of all endpoint AI tools before enterprise deployment
- Endpoint DLP covering AI assistant exfiltration vectors

#### Tools

| Tool | Type | Link |
|---|---|---|
| osquery | Open-source | https://github.com/osquery/osquery |
| OpenDLP | Open-source | https://github.com/ezarko/opendlp |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI10 Rogue Agents
- Other frameworks: ISO 27001 A.8.1 — ASVS V4 — ENISA L1-EP

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

GenAI systems fail to maintain availability of training data, RAG corpora, and
inference due to inadequate backup, recovery, and resilience controls.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 11.1 — Establish recovery capability | CIS 11 | Backup and recovery procedures defined and tested for all GenAI data stores | IG1 | Foundational | Both |
| 11.4 — Test data recovery | CIS 11 | Recovery procedures for training data and vector stores tested at least quarterly | IG2 | Foundational | Both |
| 13.8 — Deploy DNS filtering | CIS 13 | GenAI inference endpoints protected by DNS-layer defences reducing DDoS exposure | IG2 | Hardening | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Implement backup and recovery for all GenAI data stores
- Define RTO and RPO for GenAI services — test recovery regularly
- Rate limiting and quota management on inference endpoints

**Hardening (IG2)**
- Multi-region replication for production vector stores
- Circuit breakers on model inference pipelines

**Advanced (IG3)**
- Chaos engineering targeting GenAI data store availability (CIS 18.1)
- Automated failover for critical inference endpoints

#### Tools

| Tool | Type | Link |
|---|---|---|
| Velero | Open-source | https://github.com/vmware-tanzu/velero |
| Chaos Monkey | Open-source | https://github.com/Netflix/chaosmonkey |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISO 27001 A.5.30 — ASVS V11 — ENISA L1-RES

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Attackers query GenAI systems with crafted inputs to reconstruct training data
or infer membership of individuals in training sets through model outputs.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.11 — Encrypt sensitive data at rest | CIS 3 | Training data and model weights encrypted — reduces utility of model extraction attacks | IG1 | Hardening | Both |
| 18.1 — Penetration testing | CIS 18 | Membership inference and model inversion attacks included in red team scope | IG3 | Advanced | Both |

#### Mitigations by tier

**Foundational (IG1–IG2)**
- Apply differential privacy during training to limit memorisation
- Monitor query patterns for membership inference attack signatures

**Hardening (IG2–IG3)**
- Membership inference red team before production deployment
- Suppress confidence score outputs where not functionally required

**Advanced (IG3)**
- Machine unlearning to remove memorised sensitive records
- Query-level anomaly detection for systematic inference patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.11 — ASVS V8 — CWE-200

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human reviewers and RLHF annotators exposed to sensitive or harmful model-generated
content without adequate controls — creating privacy and welfare risks.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 3.3 — Access control lists | CIS 3 | Annotation platform restricts labeller access to minimum dataset scope required for the task | IG1 | Foundational | Both |
| 6.5 — Require MFA | CIS 6 | Annotation platform access protected with MFA — especially for external labeller contractors | IG1 | Foundational | Both |
| 14.3 — Train workforce to identify attacks | CIS 14 | Labellers trained on data handling requirements and harmful content reporting procedures | IG1 | Foundational | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Apply data minimisation to annotation tasks — redact sensitive fields not needed
- Restrict labeller access to minimum required dataset scope
- Audit labeller access to sensitive content

**Hardening (IG2)**
- Harmful content warning systems for labellers
- Data handling agreements with third-party annotation providers (CIS 15.1)

**Advanced (IG3)**
- Automated pre-filtering to reduce human exposure to most harmful content
- Privacy impact assessments on annotation workflows (CIS 3.1)

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Label Studio | Open-source | https://github.com/HumanSignal/label-studio |

#### Cross-references
- Other frameworks: ISO 27001 A.5.20 — GDPR Art. 28 — ENISA L3-GRC

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Attackers use model extraction techniques — crafted queries to reconstruct model
behaviour — to steal proprietary model capabilities without access to model weights.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 6.2 — Allowlist authorised access | CIS 6 | Model API access authenticated and rate-limited — systematic extraction queries detected and blocked | IG1 | Hardening | Both |
| 8.6 — Collect DNS query audit logs | CIS 8 | Unusual query patterns logged — extraction attack signatures surfaced in audit logs | IG2 | Hardening | Both |
| 18.1 — Penetration testing | CIS 18 | Model extraction attacks included in red team scope — test detection controls before production | IG3 | Advanced | Both |

#### Mitigations by tier

**Foundational (IG1–IG2)**
- Rate limiting and query monitoring on all model inference APIs
- Log unusual query patterns indicating systematic extraction

**Hardening (IG2–IG3)**
- Suppress confidence scores and logits where not functionally required
- Query diversity detection — flag systematic query patterns

**Advanced (IG3)**
- Model watermarking — embed detectable fingerprints in outputs
- Extraction attack detection via query pattern analysis

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| ART (Adversarial Robustness Toolbox) | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |

#### Cross-references
- Other frameworks: ISO 27001 A.5.12 — ASVS V4 — ENISA L2-ADV

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

Adversarial data injected into training or RAG corpora causes models to
systematically generate false outputs targeting specific topics or entities.

#### CIS Controls mapping

| Safeguard | CIS | Description | IG | Tier | Scope |
|---|---|---|---|---|---|
| 7.1 — Vulnerability management | CIS 7 | RAG corpus content sources monitored for disinformation injection incidents | IG1 | Hardening | Both |
| 16.11 — Use up-to-date components | CIS 16 | Training data sources and RAG documents reviewed for known disinformation content | IG2 | Hardening | Both |
| 18.1 — Penetration testing | CIS 18 | Red team exercises include disinformation injection attacks against RAG pipelines | IG3 | Advanced | Both |

#### Mitigations by tier

**Foundational (IG1)**
- Provenance tracking for all RAG corpus content — source and last-verified date recorded
- Validate training data for factual consistency

**Hardening (IG2)**
- Monitor production outputs for systematic factual drift from baselines
- Source diversity requirements for high-stakes RAG corpora

**Advanced (IG3)**
- Automated fact-checking pipelines for high-risk output domains
- Red team RAG corpus injection detection controls

#### Tools

| Tool | Type | Link |
|---|---|---|
| Cleanlab | Open-source | https://github.com/cleanlab/cleanlab |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 — ASVS V5 — EU AI Act Art. 13

---

## Implementation priority

| Phase | DSGAI entries | Key CIS Controls | Rationale |
|---|---|---|---|
| 1 — Do now | DSGAI01, DSGAI02, DSGAI12 | CIS 3, CIS 5, CIS 6, CIS 16 | Critical severity — data protection, credential security, NL gateway safety |
| 2 — This sprint | DSGAI03, DSGAI04, DSGAI11 | CIS 2, CIS 7, CIS 16 | Shadow AI, poisoning, and context isolation |
| 3 — This quarter | DSGAI05–07, DSGAI13–15 | CIS 3, CIS 8 | Data governance, vector store security, telemetry controls |
| 4 — Ongoing | DSGAI08–10, DSGAI16–21 | CIS 15, CIS 17, CIS 18 | Compliance, resilience, and advanced threat mitigation |

---

## References

- [CIS Controls v8.1](https://www.cisecurity.org/controls)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [OWASP AIVSS](https://aivss.owasp.org)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-27 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
