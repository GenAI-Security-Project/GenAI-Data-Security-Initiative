<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01–DSGAI21)
  Framework   : FedRAMP AI Overlay (NIST SP 800-53 Rev 5 AI-specific extensions)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 – FedRAMP AI Overlay

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/dsgai-2026/)
to the [FedRAMP AI Overlay](https://www.fedramp.gov/) extending
[NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
with AI-specific control enhancements.

FedRAMP (Federal Risk and Authorization Management Program) is the US
government's standardised approach to security authorisation for cloud
services. The AI overlay extends FedRAMP baseline controls with
AI-specific requirements. The DSGAI 2026 mapping focuses on the data
security dimensions of GenAI systems within the federal authorisation
boundary — training data protection, data governance, privacy
preservation, and regulatory compliance. It addresses how organisations
can leverage FedRAMP AI overlay controls to secure the data that flows
into, through, and out of AI pipelines: from provenance and lineage of
training corpora, through access control and integrity of model artefacts,
to data retention, consent management, and cross-jurisdictional compliance.

---

## FedRAMP AI control families

| Family | ID | Purpose |
|---|---|---|
| Access Control | AC | Data access enforcement, AI service account management, least privilege for data operations |
| Audit and Accountability | AU | Data access logging, AI decision audit trails, inference logging |
| Configuration Management | CM | Data pipeline configuration, model versioning, data flow controls |
| Identification and Authentication | IA | Identity for AI data processors, NHI management |
| Incident Response | IR | Data breach incident handling, AI-specific data incident reporting |
| Program Management | PM | Data governance strategy, AI risk management, privacy programme |
| Risk Assessment | RA | Data-specific risk assessment, privacy impact assessment |
| System and Services Acquisition | SA | Third-party data service controls, AI data SDLC |
| System and Communications Protection | SC | Data encryption, boundary protection, data flow enforcement |
| System and Information Integrity | SI | Data validation, data quality monitoring, input integrity |
| Supply Chain Risk Management | SR | Data supply chain plan, data provenance controls |

---

## Quick-reference summary

| ID | Name | Severity | FedRAMP AI Controls | Scope |
|---|---|---|---|---|
| DSGAI01 | Data Access Logging | High | AU-2, AU-12, AC-3 | Both |
| DSGAI02 | Data Visibility & Transparency | High | PM-9, AU-2, CM-3 | Both |
| DSGAI03 | Shadow AI & Unvetted Tools | High | CM-7, SA-9, AC-3 | Both |
| DSGAI04 | Data Model & Artifact Poisoning | Critical | SR-2, SR-3, SI-3, SC-28 | Both |
| DSGAI05 | Data Provenance & Quality | High | SR-3, SI-10, CM-3 | Both |
| DSGAI06 | Data Lineage Fragmentation | Medium | CM-3, AU-2, PM-9 | Build |
| DSGAI07 | Excessive Data Aggregation | High | AC-6, SC-7, PM-9 | Both |
| DSGAI08 | Data Leakage & Exposure | Critical | SC-28, AC-3, AU-2, SI-4 | Both |
| DSGAI09 | Intellectual Property Theft | High | SC-28, AC-3, AU-12 | Both |
| DSGAI10 | Synthetic Data Generation Risk | Medium | SI-4, CA-7, RA-5 | Build |
| DSGAI11 | Data Retention & Deletion | High | CM-3, SC-28, PM-9 | Both |
| DSGAI12 | Data Ownership & Monetisation | Medium | PM-9, AC-3, AU-2 | Both |
| DSGAI13 | Data Misuse & Manipulation | High | AC-3, AU-2, SI-4 | Both |
| DSGAI14 | Consent Management Failures | High | PM-9, AC-3, AU-2 | Both |
| DSGAI15 | Data Minimisation Violations | Medium | AC-6, CM-7, PM-9 | Build |
| DSGAI16 | Erosion of Privacy | High | SC-28, AC-3, PM-9, SI-4 | Both |
| DSGAI17 | Bias in Data | High | SI-4, CA-7, RA-5 | Both |
| DSGAI18 | Governance Gaps | High | PM-9, CM-3, RA-3 | Both |
| DSGAI19 | Third-Party Data Risk | High | SA-9, SR-2, SR-3 | Both |
| DSGAI20 | Data Localization Violations | High | SC-7, PM-9, CM-3 | Both |
| DSGAI21 | Non-Compliance with Data Laws | Critical | PM-9, RA-3, AU-2, AC-3 | Both |

---

## Audience tags

`data-engineer` `privacy-officer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `dpo`

- **Data engineer / ML engineer** – SI, CM, and SC controls per entry; data pipeline security
- **Privacy officer / DPO** – PM and AC entries; data minimisation, consent, and retention
- **Security engineer** – SC, AU, and AC controls; encryption, audit, and access enforcement
- **FedRAMP assessor** – full file; control traceability and evidence mapping for AI data security
- **Compliance officer** – full file; FedRAMP AI overlay alignment and regulatory traceability
- **CISO** – PM and RA entries; data governance strategy and risk prioritisation

---

## Detailed mappings

---

### DSGAI01 – Data Access Logging

**Severity:** High

Insufficient logging of data access events in AI systems prevents detection
of unauthorised access, complicates incident investigation, and fails
regulatory audit requirements. FedRAMP AI overlay addresses this through
comprehensive event logging for AI data access (AU-2), audit generation
covering model inference (AU-12), and access enforcement requiring
authenticated, logged access to AI data stores (AC-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Event Logging — AI data access logging | AU-2 | AU | Log all access to AI training data, model weights, inference inputs and outputs, and configuration; include user/service identity, timestamp, and access type |
| Audit Generation — inference audit trail | AU-12 | AU | Generate audit records for all model inference requests with sufficient detail for compliance and incident investigation |
| Access Enforcement — authenticated data access | AC-3 | AC | Enforce authenticated, authorised access to all AI data stores; deny unauthenticated access; log all access decisions |

#### Mitigations

**Foundational**
- AU-2: Implement comprehensive logging for all AI data access events;
  cover training data, model weights, inference inputs/outputs, and
  prompt configurations
- AC-3: Enforce authenticated access to all AI data stores; deny
  unauthenticated access by default
- AU-12: Generate inference audit records per FedRAMP requirements

**Hardening**
- AU-2: Feed AI data access logs into FedRAMP continuous monitoring;
  establish alerting for anomalous access patterns
- AU-12: Implement tamper-evident logging for inference audit trails;
  ensure log integrity for regulatory compliance
- AC-3: Review data access patterns quarterly; identify and remediate
  over-permissioned access

**Advanced**
- AU-2: Implement real-time analytics on data access logs; detect
  anomalous access patterns indicative of data exfiltration
- AU-12: Include AI data access logging in FedRAMP annual assessment;
  demonstrate logging completeness and integrity
- AC-3: Deploy dynamic access control based on data sensitivity and
  user risk context

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| AWS CloudTrail / Azure Monitor | Commercial | https://aws.amazon.com/cloudtrail/ |
| Elasticsearch | Open-source | https://www.elastic.co |
| Splunk | Commercial | https://www.splunk.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: SP 800-218A PS.1.1-PS – NIST CSF 2.0 DE.AE-3 – ISO 27001 A.12.4

---

### DSGAI02 – Data Visibility & Transparency

**Severity:** High

Lack of visibility into what data AI systems process, how it flows through
pipelines, and what decisions are made based on it. FedRAMP AI overlay
addresses this through risk management strategy requiring data visibility
(PM-9), event logging for data flow tracking (AU-2), and configuration
change control for data pipelines (CM-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Risk Management Strategy — data visibility requirements | PM-9 | PM | Include data visibility and transparency requirements in AI risk management strategy; define what data flows must be documented and monitored |
| Event Logging — data flow tracking | AU-2 | AU | Log data movement through AI pipelines — ingestion, transformation, training, inference; enable end-to-end data flow traceability |
| Configuration Change Control — data pipeline documentation | CM-3 | CM | Document and control changes to AI data pipeline configurations; maintain current data flow diagrams and processing documentation |

#### Mitigations

**Foundational**
- PM-9: Define data visibility requirements for all AI systems within
  the FedRAMP boundary; specify what data flows must be documented
- AU-2: Log data movement through AI pipelines with sufficient detail
  for traceability; cover ingestion, transformation, and inference
- CM-3: Maintain current data flow documentation; update on every
  pipeline change

**Hardening**
- PM-9: Include data visibility metrics in management reporting;
  track coverage across AI systems
- AU-2: Implement automated data flow tracing; visualise end-to-end
  data movement through AI pipelines
- CM-3: Implement automated documentation generation for data pipelines;
  ensure documentation stays current

**Advanced**
- PM-9: Include data visibility in FedRAMP SSP; demonstrate
  comprehensive understanding of AI data flows
- AU-2: Deploy real-time data flow monitoring dashboards; enable
  immediate visibility into AI data processing
- CM-3: Implement drift detection for data pipeline configurations;
  alert on undocumented changes

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| OpenLineage | Open-source | https://openlineage.io |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: SP 800-218A PW.1.1-PS – NIST AI RMF MAP 2.3 – ISO 42001 A.7.2

---

### DSGAI03 – Shadow AI & Unvetted Tools

**Severity:** High

Unauthorised or unvetted AI tools and services used within the organisation
bypass security controls and data governance. FedRAMP AI overlay addresses
this through least functionality restricting approved AI tools (CM-7),
external service controls for third-party AI (SA-9), and access enforcement
preventing unauthorised AI tool usage (AC-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Functionality — approved AI tools only | CM-7 | CM | Restrict AI tool usage to approved, vetted tools within the FedRAMP boundary; disable or block access to unauthorised AI services |
| External Information System Services — third-party AI controls | SA-9 | SA | Require FedRAMP authorisation or equivalent for all third-party AI services; block data transfer to unauthorised AI tools |
| Access Enforcement — AI tool access control | AC-3 | AC | Enforce access control preventing data transfer to unauthorised AI tools; monitor and block shadow AI usage |

#### Mitigations

**Foundational**
- CM-7: Define and enforce an approved AI tools list; block access to
  unauthorised AI services from the FedRAMP environment
- SA-9: Require FedRAMP authorisation for all third-party AI services
  processing federal data
- AC-3: Implement network-level controls preventing data transfer to
  unauthorised AI tools

**Hardening**
- CM-7: Implement automated discovery of AI tool usage; detect and
  alert on shadow AI activity
- SA-9: Conduct security assessment of all AI tools before approval;
  include in FedRAMP continuous monitoring
- AC-3: Deploy DLP controls blocking sensitive data transfer to
  unapproved AI services

**Advanced**
- CM-7: Include shadow AI detection in FedRAMP continuous monitoring;
  track and report on unauthorised AI tool usage
- SA-9: Implement automated compliance verification for third-party
  AI services; alert on authorisation expiry
- AC-3: Deploy advanced behavioural analytics to detect indirect
  shadow AI usage patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Nightfall DLP | Commercial | https://www.nightfall.ai |
| Netskope | Commercial | https://www.netskope.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security/business/cloud-apps-defender |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: SP 800-218A PW.4.1-PS – CIS Controls 2 – NIST CSF 2.0 ID.AM-2

---

### DSGAI04 – Data Model & Artifact Poisoning

**Severity:** Critical

Attackers corrupt training data, model weights, or pipeline artefacts to
embed backdoors or bias AI system behaviour. FedRAMP AI overlay addresses
this through supply chain planning for AI data sources (SR-2), supply
chain controls for artefact provenance (SR-3), malicious code protection
for training pipelines (SI-3), and encryption of data and model artefacts
at rest (SC-28).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Supply Chain Risk Management Plan — AI data and artefact sources | SR-2 | SR | Include AI training data, model weights, and pipeline artefacts in supply chain risk management with provenance documentation |
| Supply Chain Controls — artefact provenance verification | SR-3 | SR | Verify integrity and provenance of all AI artefacts using cryptographic signatures and checksums before use in any pipeline |
| Malicious Code Protection — training pipeline integrity | SI-3 | SI | Extend malicious code protection to training data and model artefacts; detect poisoned data, anomalous patterns, and backdoor indicators |
| Protection of Information at Rest — artefact encryption | SC-28 | SC | Encrypt all training data, model weights, and pipeline artefacts at rest; enforce key management per FedRAMP requirements |

#### Mitigations

**Foundational**
- SR-2: Include all AI data sources and artefacts in supply chain plan;
  document provenance and risk assessment for each
- SR-3: Verify cryptographic integrity of all artefacts before use;
  maintain signed checksums for training data and model weights
- SC-28: Encrypt all AI artefacts at rest using FIPS 140-validated
  modules

**Hardening**
- SI-3: Apply anomaly detection to training data; flag statistical
  outliers and content inconsistent with source domain
- SR-3: Implement automated integrity verification in CI/CD; block
  deployment of unverified artefacts
- SR-2: Reassess supply chain risk on schedule aligned with FedRAMP
  continuous monitoring

**Advanced**
- SI-3: Conduct backdoor detection on all new model versions; use
  neural cleanse or equivalent before production
- SR-3: Implement continuous supply chain integrity monitoring; alert
  on artefact modification or provenance changes
- SC-28: Include artefact security in FedRAMP annual assessment

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Sigstore | Open-source | https://www.sigstore.dev |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning
- Agentic Top 10: ASI06 Memory Poisoning & Context Confusion
- Other frameworks: MITRE ATLAS AML.T0032 – SP 800-218A PS.1.1-PS – NIST CSF 2.0 PR.DS-8

---

### DSGAI05 – Data Provenance & Quality

**Severity:** High

Insufficient data provenance tracking and quality controls lead to use of
unreliable, outdated, or inappropriately sourced data in AI systems.
FedRAMP AI overlay addresses this through supply chain controls for data
provenance (SR-3), input validation for data quality (SI-10), and
configuration change control for data pipeline changes (CM-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Supply Chain Controls — data provenance tracking | SR-3 | SR | Implement provenance tracking for all AI training data; document source, collection method, processing history, and licensing for each dataset |
| Information Input Validation — data quality controls | SI-10 | SI | Validate quality, completeness, and accuracy of data entering AI pipelines; reject data failing quality thresholds |
| Configuration Change Control — data source changes | CM-3 | CM | Require formal change control for all data source additions, modifications, and removals; maintain audit trail |

#### Mitigations

**Foundational**
- SR-3: Implement provenance tracking for all training data; document
  source, collection method, and licensing
- SI-10: Define and enforce data quality thresholds; reject data failing
  validation checks
- CM-3: Require change control for data source modifications

**Hardening**
- SR-3: Implement automated provenance verification; validate data
  source integrity at each pipeline stage
- SI-10: Deploy continuous data quality monitoring; alert on quality
  degradation
- CM-3: Include data source changes in FedRAMP change management

**Advanced**
- SR-3: Include data provenance in FedRAMP annual assessment;
  demonstrate comprehensive provenance tracking
- SI-10: Implement advanced data quality analytics; detect subtle
  quality issues affecting model performance
- CM-3: Deploy automated data lineage tracking; maintain real-time
  data flow documentation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| OpenLineage | Open-source | https://openlineage.io |
| Apache Atlas | Open-source | https://atlas.apache.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning
- Agentic Top 10: ASI06 Memory Poisoning & Context Confusion
- Other frameworks: SP 800-218A PS.3.1-PS – NIST CSF 2.0 PR.DS-8 – ISO 42001 A.7.4

---

### DSGAI06 – Data Lineage Fragmentation

**Severity:** Medium

Fragmented or incomplete data lineage across AI pipelines prevents
understanding of how data is transformed, combined, and used in model
development. FedRAMP AI overlay addresses this through configuration change
control for pipeline documentation (CM-3), event logging for data
transformation tracking (AU-2), and risk management requiring lineage
visibility (PM-9).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Configuration Change Control — pipeline lineage documentation | CM-3 | CM | Maintain comprehensive data lineage documentation for all AI pipelines; update on every transformation, combination, or processing change |
| Event Logging — data transformation logging | AU-2 | AU | Log all data transformation events in AI pipelines; enable end-to-end lineage reconstruction from source to model |
| Risk Management Strategy — lineage requirements | PM-9 | PM | Include data lineage completeness in AI risk management strategy; define minimum lineage requirements per data sensitivity level |

#### Mitigations

**Foundational**
- CM-3: Maintain data lineage documentation for all AI pipelines;
  update on every change
- AU-2: Log data transformation events with input/output references;
  enable lineage reconstruction
- PM-9: Define lineage requirements per data sensitivity level

**Hardening**
- CM-3: Implement automated lineage capture; reduce manual documentation
  burden and ensure completeness
- AU-2: Deploy end-to-end lineage tracing; visualise data flow from
  source through transformation to model
- PM-9: Include lineage completeness in management reporting

**Advanced**
- CM-3: Include data lineage in FedRAMP SSP; demonstrate comprehensive
  lineage tracking
- AU-2: Implement lineage-based impact analysis; assess how data source
  changes affect downstream models
- PM-9: Deploy lineage-based compliance verification; automate
  regulatory traceability checks

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenLineage | Open-source | https://openlineage.io |
| Apache Atlas | Open-source | https://atlas.apache.org |
| dbt | Open-source | https://www.getdbt.com |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning
- Agentic Top 10: ASI07 Lateral Tool Chaining
- Other frameworks: SP 800-218A PS.3.1-PS – NIST AI RMF MAP 2.3 – ISO 42001 A.7.4

---

### DSGAI07 – Excessive Data Aggregation

**Severity:** High

AI systems aggregate data from multiple sources creating combined datasets
with higher sensitivity than individual sources, enabling re-identification
or inference of sensitive attributes. FedRAMP AI overlay addresses this
through least privilege restricting data aggregation scope (AC-6), boundary
protection controlling data flow (SC-7), and risk management covering
aggregation risk (PM-9).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Privilege — data aggregation restrictions | AC-6 | AC | Restrict data aggregation scope to minimum necessary; enforce controls preventing combination of datasets that create higher-sensitivity aggregates |
| Boundary Protection — data flow control | SC-7 | SC | Enforce boundary protection on data flows between systems; prevent uncontrolled data aggregation across security boundaries |
| Risk Management Strategy — aggregation risk | PM-9 | PM | Include data aggregation risk in AI risk management strategy; assess combined sensitivity of aggregated datasets |

#### Mitigations

**Foundational**
- AC-6: Restrict data aggregation to minimum necessary per use case;
  require justification for cross-source data combination
- SC-7: Enforce boundary controls on data flows; prevent data from
  crossing sensitivity boundaries without authorisation
- PM-9: Assess aggregation risk for each AI data pipeline

**Hardening**
- AC-6: Implement automated aggregation controls; alert when combined
  datasets exceed defined sensitivity thresholds
- SC-7: Deploy data flow enforcement; block unauthorised data
  combination across boundaries
- PM-9: Include aggregation risk in management risk reporting

**Advanced**
- Apply privacy-enhancing technologies — differential privacy,
  k-anonymity — to aggregated datasets
- SC-7: Include data aggregation controls in FedRAMP annual assessment
- PM-9: Deploy automated aggregation risk assessment; continuously
  evaluate combined dataset sensitivity

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Privilege Escalation
- Other frameworks: SP 800-218A PW.1.1-PS – NIST Privacy Framework – ISO 27701

---

### DSGAI08 – Data Leakage & Exposure

**Severity:** Critical

Sensitive data is exposed through model outputs, training data extraction,
side channels, or misconfigured data stores. FedRAMP AI overlay addresses
this through encryption at rest (SC-28), access enforcement (AC-3),
comprehensive logging (AU-2), and system monitoring for leakage indicators
(SI-4).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — AI data encryption | SC-28 | SC | Encrypt all AI data at rest — training data, model weights, inference logs, embedding stores — using FIPS 140-validated modules |
| Access Enforcement — AI data access | AC-3 | AC | Enforce role-based access control on all AI data stores; restrict access based on clearance, need-to-know, and data sensitivity |
| Event Logging — leakage detection logging | AU-2 | AU | Log AI data access and model outputs with sufficient detail to detect data leakage; include output content metadata |
| System Monitoring — leakage indicator detection | SI-4 | SI | Monitor model outputs and data access patterns for leakage indicators — PII, credentials, classification markings in outputs; alert on detection |

#### Mitigations

**Foundational**
- SC-28: Encrypt all AI data at rest; enforce key management per
  FedRAMP requirements
- AC-3: Implement role-based access on all AI data stores; deny by
  default
- AU-2: Log all data access and model outputs

**Hardening**
- SI-4: Deploy output monitoring for sensitive data patterns; alert
  and block on detection
- SC-28: Conduct data extraction testing; verify training data cannot
  be extracted through targeted queries
- AU-2: Feed data access logs into continuous monitoring

**Advanced**
- Apply differential privacy to training; bound memorisation risk
- SI-4: Include data leakage testing in FedRAMP annual assessment
- Deploy output classifiers detecting and redacting sensitive content

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Nightfall DLP | Commercial | https://www.nightfall.ai |
| AWS Macie / Azure Purview | Commercial | https://aws.amazon.com/macie/ |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM07 System Prompt Leakage
- Agentic Top 10: ASI03 Privilege Escalation
- Other frameworks: SP 800-218A PS.1.1-PS – CWE-200 – NIST CSF 2.0 PR.DS-5

---

### DSGAI09 – Intellectual Property Theft

**Severity:** High

AI model weights, training data, proprietary algorithms, or fine-tuning
datasets are stolen or extracted. FedRAMP AI overlay addresses this through
encryption at rest (SC-28), access enforcement (AC-3), and audit generation
for IP access tracking (AU-12).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — IP encryption | SC-28 | SC | Encrypt all intellectual property — model weights, proprietary training data, algorithms — at rest with FIPS 140-validated modules |
| Access Enforcement — IP access control | AC-3 | AC | Enforce strict access control on AI intellectual property; restrict to minimum necessary personnel with audit trail |
| Audit Generation — IP access tracking | AU-12 | AU | Generate audit records for all access to AI intellectual property; enable detection of unauthorised access and exfiltration |

#### Mitigations

**Foundational**
- SC-28: Encrypt all AI IP at rest; implement key management per
  FedRAMP requirements
- AC-3: Restrict access to AI IP to minimum necessary personnel;
  enforce multi-factor authentication for model weight access
- AU-12: Log all access to AI IP with full identity and action detail

**Hardening**
- SC-28: Implement DLP controls for AI IP; monitor and block
  exfiltration attempts
- AC-3: Implement time-bounded access for model weight downloads;
  require approval workflow
- AU-12: Feed IP access logs into continuous monitoring; alert on
  anomalous access patterns

**Advanced**
- Deploy model watermarking to detect stolen model weights
- SC-28: Include IP protection in FedRAMP annual assessment
- AC-3: Implement hardware-backed key management for model weight
  encryption keys

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Commercial | https://www.vaultproject.io |
| Nightfall DLP | Commercial | https://www.nightfall.ai |
| AWS KMS / Azure Key Vault | Commercial | https://aws.amazon.com/kms/ |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: SP 800-218A PS.1.1-PS – MITRE ATLAS AML.T0024 – NIST CSF 2.0 PR.DS-5

---

### DSGAI10 – Synthetic Data Generation Risk

**Severity:** Medium

Synthetic data generated by AI systems may inadvertently encode sensitive
patterns, enable re-identification, or produce biased outputs. FedRAMP AI
overlay addresses this through system monitoring for synthetic data quality
(SI-4), continuous monitoring for drift (CA-7), and vulnerability scanning
covering synthetic data risks (RA-5).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| System Monitoring — synthetic data quality | SI-4 | SI | Monitor synthetic data outputs for quality, privacy preservation, and absence of sensitive pattern leakage |
| Continuous Monitoring — synthetic data drift | CA-7 | CA | Include synthetic data quality metrics in continuous monitoring; track for privacy degradation and bias drift |
| Vulnerability Scanning — synthetic data risks | RA-5 | RA | Include synthetic data re-identification and pattern leakage in vulnerability assessment |

#### Mitigations

**Foundational**
- SI-4: Monitor synthetic data for sensitive pattern leakage; validate
  privacy preservation before use
- CA-7: Track synthetic data quality metrics over time
- RA-5: Assess re-identification risk for synthetic datasets

**Hardening**
- SI-4: Deploy automated privacy validation for synthetic data;
  verify differential privacy guarantees
- CA-7: Include synthetic data monitoring in continuous monitoring
- RA-5: Conduct re-identification testing on synthetic datasets

**Advanced**
- Deploy formal privacy guarantees for synthetic data generation
- Include synthetic data risk in FedRAMP assessment
- Implement continuous privacy monitoring for synthetic data pipelines

#### Tools

| Tool | Type | Link |
|---|---|---|
| Gretel AI | Commercial | https://gretel.ai |
| SDV | Open-source | https://sdv.dev |
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: SP 800-218A PW.7.2-PS – NIST Privacy Framework – ISO 27701

---

### DSGAI11 – Data Retention & Deletion

**Severity:** High

Failure to implement appropriate data retention and deletion policies for
AI training data, inference logs, and model artefacts. FedRAMP AI overlay
addresses this through configuration change control for retention policies
(CM-3), encryption of retained data (SC-28), and risk management covering
retention governance (PM-9).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Configuration Change Control — retention policy management | CM-3 | CM | Define and enforce data retention policies for all AI data; implement automated deletion schedules; log policy changes |
| Protection of Information at Rest — retained data encryption | SC-28 | SC | Encrypt all retained AI data; implement crypto-shredding capability for secure deletion |
| Risk Management Strategy — retention governance | PM-9 | PM | Include data retention risk in AI risk management; define retention periods per data type and regulatory requirement |

#### Mitigations

**Foundational**
- CM-3: Define retention policies for all AI data types; implement
  automated deletion schedules
- SC-28: Encrypt retained data with per-dataset keys enabling
  crypto-shredding
- PM-9: Define retention periods per FedRAMP and applicable regulations

**Hardening**
- CM-3: Implement automated retention enforcement; verify deletion
  completeness
- SC-28: Implement crypto-shredding for model weight disposal
- PM-9: Include retention compliance in management reporting

**Advanced**
- CM-3: Include retention compliance in FedRAMP annual assessment
- Deploy automated retention compliance verification across all AI
  data stores
- PM-9: Implement retention impact analysis for AI model retraining

#### Tools

| Tool | Type | Link |
|---|---|---|
| AWS S3 Lifecycle / Azure Lifecycle Management | Commercial | https://aws.amazon.com/s3/ |
| HashiCorp Vault | Commercial | https://www.vaultproject.io |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Apache Atlas | Open-source | https://atlas.apache.org |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI06 Memory Poisoning & Context Confusion
- Other frameworks: SP 800-218A PS.3.1-PS – NIST CSF 2.0 PR.DS-3 – GDPR Art. 17

---

### DSGAI12 – Data Ownership & Monetisation

**Severity:** Medium

Unclear data ownership and monetisation policies for AI training data,
model outputs, and derived insights. FedRAMP AI overlay addresses this
through risk management strategy covering ownership governance (PM-9),
access enforcement based on ownership (AC-3), and logging of data usage
(AU-2).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Risk Management Strategy — ownership governance | PM-9 | PM | Define data ownership policies for AI data; clarify rights and responsibilities for training data, outputs, and derived insights |
| Access Enforcement — ownership-based access | AC-3 | AC | Enforce access controls aligned with data ownership; restrict usage based on ownership rights and licence terms |
| Event Logging — usage tracking | AU-2 | AU | Log data usage for ownership compliance; track how data is used across AI systems for licence and rights management |

#### Mitigations

**Foundational**
- PM-9: Define ownership policies for all AI data categories
- AC-3: Align access controls with ownership rights
- AU-2: Log data usage for ownership compliance tracking

**Hardening**
- PM-9: Include ownership governance in management reporting
- AC-3: Implement automated licence compliance enforcement
- AU-2: Deploy usage analytics for ownership tracking

**Advanced**
- PM-9: Include ownership in FedRAMP SSP
- Deploy automated rights management for AI data
- AU-2: Implement comprehensive usage auditing

#### Tools

| Tool | Type | Link |
|---|---|---|
| Collibra | Commercial | https://www.collibra.com |
| Apache Atlas | Open-source | https://atlas.apache.org |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Alation | Commercial | https://www.alation.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: SP 800-218A PW.1.1-PS – ISO 42001 A.7.2 – NIST Privacy Framework

---

### DSGAI13 – Data Misuse & Manipulation

**Severity:** High

AI data used for purposes beyond original consent or manipulated to produce
biased or harmful outcomes. FedRAMP AI overlay addresses this through access
enforcement restricting data usage (AC-3), logging of all data operations
(AU-2), and system monitoring for misuse indicators (SI-4).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Access Enforcement — purpose-limited data access | AC-3 | AC | Enforce purpose-limitation on AI data access; restrict usage to approved purposes documented in data processing agreements |
| Event Logging — data operation logging | AU-2 | AU | Log all data operations with purpose context; enable detection of purpose drift and unauthorised usage |
| System Monitoring — misuse detection | SI-4 | SI | Monitor AI data usage patterns for misuse indicators; alert on data access inconsistent with approved purposes |

#### Mitigations

**Foundational**
- AC-3: Enforce purpose-limitation controls on data access; restrict
  to approved uses
- AU-2: Log all data operations with usage context
- SI-4: Monitor for data usage inconsistent with approved purposes

**Hardening**
- AC-3: Implement automated purpose enforcement; block operations
  outside approved scope
- AU-2: Deploy usage pattern analytics; detect purpose drift
- SI-4: Include misuse detection in continuous monitoring

**Advanced**
- AC-3: Include purpose-limitation compliance in FedRAMP assessment
- Deploy automated purpose compliance verification
- SI-4: Implement advanced misuse detection analytics

#### Tools

| Tool | Type | Link |
|---|---|---|
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Collibra | Commercial | https://www.collibra.com |
| Splunk | Commercial | https://www.splunk.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: SP 800-218A PW.1.1-PS – NIST Privacy Framework – GDPR Art. 5

---

### DSGAI14 – Consent Management Failures

**Severity:** High

Failure to obtain, track, and honour data subject consent for AI processing
activities. FedRAMP AI overlay addresses this through risk management
covering consent governance (PM-9), access enforcement aligned with consent
(AC-3), and logging for consent compliance (AU-2).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Risk Management Strategy — consent governance | PM-9 | PM | Include consent management in AI risk management strategy; define consent requirements per data type and processing activity |
| Access Enforcement — consent-based access | AC-3 | AC | Enforce access controls aligned with consent status; block AI processing on data where consent has been withdrawn |
| Event Logging — consent compliance logging | AU-2 | AU | Log consent status and changes; enable audit of consent compliance for all AI data processing activities |

#### Mitigations

**Foundational**
- PM-9: Define consent requirements for all AI data processing
- AC-3: Align data access with consent status; block processing on
  withdrawn consent
- AU-2: Log consent decisions and status changes

**Hardening**
- PM-9: Include consent compliance in management reporting
- AC-3: Implement automated consent enforcement across AI pipelines
- AU-2: Deploy consent audit capabilities; verify compliance

**Advanced**
- PM-9: Include consent management in FedRAMP SSP
- Deploy automated consent lifecycle management
- AC-3: Implement real-time consent verification at data access

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| Collibra | Commercial | https://www.collibra.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| TrustArc | Commercial | https://trustarc.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: SP 800-218A PW.1.1-PS – GDPR Art. 7 – NIST Privacy Framework

---

### DSGAI15 – Data Minimisation Violations

**Severity:** Medium

AI systems collect, process, or retain more data than necessary for their
stated purpose. FedRAMP AI overlay addresses this through least privilege
restricting data collection (AC-6), least functionality limiting data
processing scope (CM-7), and risk management covering minimisation (PM-9).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Privilege — data collection restrictions | AC-6 | AC | Restrict AI data collection to minimum necessary for stated purpose; enforce at pipeline ingestion points |
| Least Functionality — data processing restrictions | CM-7 | CM | Restrict AI data processing to minimum necessary scope; disable collection of non-essential data fields |
| Risk Management Strategy — minimisation governance | PM-9 | PM | Include data minimisation in AI risk management; define minimum necessary data per AI use case |

#### Mitigations

**Foundational**
- AC-6: Restrict data collection to minimum necessary; enforce at
  ingestion points
- CM-7: Disable collection of non-essential data fields
- PM-9: Define minimum necessary data per AI use case

**Hardening**
- AC-6: Implement automated minimisation enforcement; alert on
  collection exceeding defined scope
- CM-7: Deploy data field filtering at pipeline ingestion
- PM-9: Include minimisation compliance in management reporting

**Advanced**
- Deploy privacy-enhancing technologies to reduce data requirements
- Include minimisation in FedRAMP annual assessment
- Implement continuous minimisation compliance monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| OneTrust | Commercial | https://www.onetrust.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: SP 800-218A PW.1.1-PS – GDPR Art. 5(1)(c) – NIST Privacy Framework

---

### DSGAI16 – Erosion of Privacy

**Severity:** High

AI systems progressively erode privacy through inference, aggregation, and
memorisation — even when individual data points are not explicitly sensitive.
FedRAMP AI overlay addresses this through encryption at rest (SC-28),
access enforcement (AC-3), risk management covering privacy risk (PM-9),
and system monitoring for privacy erosion indicators (SI-4).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — privacy-preserving storage | SC-28 | SC | Encrypt AI data at rest; implement privacy-preserving storage techniques to prevent inference and re-identification |
| Access Enforcement — privacy-aligned access | AC-3 | AC | Enforce access controls that account for inference and aggregation risk; restrict access based on combined sensitivity |
| Risk Management Strategy — privacy risk assessment | PM-9 | PM | Include AI privacy erosion in risk management; assess inference, aggregation, and memorisation risks for AI systems |
| System Monitoring — privacy erosion detection | SI-4 | SI | Monitor for privacy erosion indicators; detect inference capabilities, re-identification risk, and memorisation patterns |

#### Mitigations

**Foundational**
- SC-28: Encrypt AI data at rest; implement privacy-preserving controls
- AC-3: Enforce access controls accounting for aggregation risk
- PM-9: Assess privacy erosion risk for each AI system

**Hardening**
- SI-4: Deploy privacy erosion monitoring; detect inference and
  re-identification capabilities
- SC-28: Conduct memorisation testing; verify training data privacy
- PM-9: Include privacy erosion in management risk reporting

**Advanced**
- Apply differential privacy to training; bound memorisation
- Deploy privacy-preserving computation techniques
- Include privacy erosion assessment in FedRAMP annual assessment

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| Opacus | Open-source | https://opacus.ai |
| OneTrust | Commercial | https://www.onetrust.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Privilege Escalation
- Other frameworks: SP 800-218A PW.1.1-PS – NIST Privacy Framework – GDPR Art. 25

---

### DSGAI17 – Bias in Data

**Severity:** High

Biased training data leads to discriminatory or unfair AI outcomes. FedRAMP
AI overlay addresses this through system monitoring for bias indicators
(SI-4), continuous monitoring for output fairness (CA-7), and vulnerability
scanning covering bias detection (RA-5).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| System Monitoring — bias detection | SI-4 | SI | Monitor AI outputs for bias indicators; track fairness metrics across demographic groups and use cases |
| Continuous Monitoring — fairness monitoring | CA-7 | CA | Include bias and fairness metrics in continuous monitoring; track output equity over time |
| Vulnerability Scanning — bias assessment | RA-5 | RA | Include bias detection and fairness assessment in vulnerability scanning; test for disparate impact |

#### Mitigations

**Foundational**
- SI-4: Monitor AI outputs for bias indicators; establish baseline
  fairness metrics
- CA-7: Include fairness metrics in continuous monitoring
- RA-5: Conduct bias assessment before deployment

**Hardening**
- SI-4: Deploy automated bias detection; alert on fairness degradation
- CA-7: Track fairness trends over time; escalate degradation
- RA-5: Include bias testing in regular vulnerability assessments

**Advanced**
- Deploy formal fairness constraints in training pipelines
- Include bias assessment in FedRAMP annual assessment
- Implement continuous fairness monitoring with automated remediation

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM AI Fairness 360 | Open-source | https://aif360.mybluemix.net |
| Fairlearn | Open-source | https://fairlearn.org |
| What-If Tool | Open-source | https://pair-code.github.io/what-if-tool/ |
| Fiddler AI | Commercial | https://www.fiddler.ai |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: SP 800-218A PW.7.2-PS – NIST AI RMF MAP 2.3 – ISO 42001 A.6.2.6

---

### DSGAI18 – Governance Gaps

**Severity:** High

Insufficient governance frameworks for AI data management — unclear roles,
missing policies, and inadequate oversight. FedRAMP AI overlay addresses
this through risk management strategy covering governance (PM-9),
configuration change control for policy management (CM-3), and risk
assessment for governance completeness (RA-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Risk Management Strategy — AI governance framework | PM-9 | PM | Establish comprehensive AI data governance framework within risk management strategy; define roles, policies, and oversight mechanisms |
| Configuration Change Control — governance policy management | CM-3 | CM | Maintain AI governance policies under change control; require approval for policy modifications; audit all changes |
| Risk Assessment — governance completeness | RA-3 | RA | Assess AI governance completeness; identify gaps in roles, policies, oversight, and accountability |

#### Mitigations

**Foundational**
- PM-9: Establish AI data governance framework; define roles and
  policies
- CM-3: Maintain governance policies under change control
- RA-3: Assess governance completeness; identify gaps

**Hardening**
- PM-9: Include governance in management reporting; track maturity
- CM-3: Implement automated policy compliance checking
- RA-3: Conduct regular governance gap analysis

**Advanced**
- PM-9: Include governance in FedRAMP SSP; demonstrate maturity
- Deploy automated governance monitoring
- RA-3: Include governance in FedRAMP annual assessment

#### Tools

| Tool | Type | Link |
|---|---|---|
| Collibra | Commercial | https://www.collibra.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Alation | Commercial | https://www.alation.com |
| ServiceNow GRC | Commercial | https://www.servicenow.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: SP 800-218A PW.1.1-PS – NIST AI RMF GOV – ISO 42001 5.1

---

### DSGAI19 – Third-Party Data Risk

**Severity:** High

Risks from third-party data sources, processors, and AI service providers
handling organisational data. FedRAMP AI overlay addresses this through
external service controls (SA-9), supply chain planning for data providers
(SR-2), and supply chain controls for data provenance (SR-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| External Information System Services — third-party data controls | SA-9 | SA | Require FedRAMP authorisation for third-party data service providers; establish SLAs covering data security, privacy, and incident notification |
| Supply Chain Risk Management Plan — data provider risk | SR-2 | SR | Include third-party data providers in supply chain risk management; assess data handling practices and security posture |
| Supply Chain Controls — data provenance from third parties | SR-3 | SR | Verify provenance and integrity of data from third-party sources; implement validation before ingestion into AI pipelines |

#### Mitigations

**Foundational**
- SA-9: Require FedRAMP authorisation for third-party data providers
- SR-2: Include data providers in supply chain risk plan
- SR-3: Verify third-party data provenance and integrity

**Hardening**
- SA-9: Include data provider security in continuous monitoring
- SR-2: Conduct regular third-party risk reassessment
- SR-3: Implement automated data validation from third-party sources

**Advanced**
- SA-9: Conduct on-site assessments of critical data providers
- SR-2: Include third-party data risk in board-level reporting
- SR-3: Deploy continuous third-party data integrity monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| CycloneDX | Open-source | https://cyclonedx.org |
| OneTrust Vendorpedia | Commercial | https://www.onetrust.com |
| ServiceNow VRM | Commercial | https://www.servicenow.com |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: SP 800-218A PW.4.1-PS – NIST CSF 2.0 ID.SC-2 – EBA Outsourcing Guidelines

---

### DSGAI20 – Data Localization Violations

**Severity:** High

AI data processed or stored outside jurisdictional requirements — data
residency laws, cross-border transfer restrictions. FedRAMP AI overlay
addresses this through boundary protection enforcing data flow (SC-7),
risk management covering localisation (PM-9), and configuration change
control for data location (CM-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Boundary Protection — data flow enforcement | SC-7 | SC | Enforce data flow controls preventing AI data from crossing jurisdictional boundaries; restrict to approved data centres and regions |
| Risk Management Strategy — localisation governance | PM-9 | PM | Include data localisation in AI risk management; define data residency requirements per jurisdiction and data type |
| Configuration Change Control — data location management | CM-3 | CM | Maintain documentation of AI data storage locations; require change control for data location modifications |

#### Mitigations

**Foundational**
- SC-7: Enforce data flow controls at network boundary; prevent AI
  data from leaving approved jurisdictions
- PM-9: Define data residency requirements per applicable laws
- CM-3: Document all AI data storage locations; update on change

**Hardening**
- SC-7: Implement automated data flow enforcement; alert on
  unauthorised cross-border transfers
- PM-9: Include localisation compliance in management reporting
- CM-3: Deploy automated data location tracking

**Advanced**
- SC-7: Include data localisation in FedRAMP annual assessment
- Deploy automated cross-border transfer detection and blocking
- PM-9: Implement continuous localisation compliance monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| AWS Region Controls / Azure Policy | Commercial | https://aws.amazon.com/compliance/data-residency/ |
| Netskope | Commercial | https://www.netskope.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| OneTrust | Commercial | https://www.onetrust.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: SP 800-218A PW.1.1-PS – GDPR Art. 44–49 – FedRAMP High Baseline

---

### DSGAI21 – Non-Compliance with Data Laws

**Severity:** Critical

AI systems fail to comply with applicable data protection regulations —
GDPR, CCPA, HIPAA, sector-specific requirements. FedRAMP AI overlay
addresses this through risk management covering regulatory compliance
(PM-9), risk assessment identifying compliance gaps (RA-3), comprehensive
logging for regulatory evidence (AU-2), and access enforcement aligned
with legal requirements (AC-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Risk Management Strategy — regulatory compliance | PM-9 | PM | Include regulatory compliance in AI risk management; map applicable data laws to AI processing activities and define compliance requirements |
| Risk Assessment — compliance gap analysis | RA-3 | RA | Conduct regulatory compliance gap analysis for AI systems; identify areas of non-compliance and define remediation plans |
| Event Logging — regulatory evidence | AU-2 | AU | Maintain comprehensive logs for regulatory compliance evidence; ensure audit trails meet requirements of applicable data laws |
| Access Enforcement — legally mandated controls | AC-3 | AC | Implement access controls mandated by applicable data laws; enforce data subject rights, purpose limitation, and processing restrictions |

#### Mitigations

**Foundational**
- PM-9: Map applicable data laws to AI processing activities; define
  compliance requirements for each
- RA-3: Conduct compliance gap analysis; identify non-compliance areas
- AU-2: Implement logging sufficient for regulatory evidence
- AC-3: Implement legally mandated access controls

**Hardening**
- PM-9: Include regulatory compliance in management reporting; track
  compliance status across AI systems
- RA-3: Conduct regular compliance reassessment aligned with
  regulatory changes
- AU-2: Implement automated compliance evidence collection

**Advanced**
- PM-9: Include AI regulatory compliance in FedRAMP SSP
- Deploy automated compliance monitoring across all AI systems
- RA-3: Include regulatory compliance in FedRAMP annual assessment

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| TrustArc | Commercial | https://trustarc.com |
| ServiceNow GRC | Commercial | https://www.servicenow.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: SP 800-218A PW.1.1-PS – GDPR – CCPA – HIPAA – FedRAMP High Baseline

---

## Implementation priority

| Phase | AC / AU | SC / SI / CM | PM / RA / SA / SR |
|---|---|---|---|
| 1 – Now | AU-2 data access logging for DSGAI01/08; AC-3 access enforcement for DSGAI08/09/21 | SC-28 encryption for DSGAI04/08/09; SI-3 poisoning protection for DSGAI04 | PM-9 governance for DSGAI02/18/21; SR-2 supply chain for DSGAI04/19 |
| 2 – This sprint | AU-12 inference audit for DSGAI01; AC-6 least privilege for DSGAI07/15; AU-2 lineage logging for DSGAI06 | SI-10 data quality for DSGAI05; CM-3 change control for DSGAI05/06/11; CM-7 shadow AI blocking for DSGAI03 | SA-9 third-party controls for DSGAI03/19; SR-3 provenance for DSGAI04/05; RA-3 compliance gap for DSGAI21 |
| 3 – This quarter | AC-3 consent and purpose controls for DSGAI13/14; AU-2 comprehensive logging for all entries | SC-7 boundary and localisation for DSGAI07/20; SI-4 monitoring for DSGAI08/13/16/17 | CA-7 continuous monitoring for DSGAI10/17; RA-5 bias and synthetic data assessment for DSGAI10/17; PM-9 privacy and minimisation for DSGAI15/16 |
| 4 – Ongoing | Access control reviews; audit log analysis; consent lifecycle management | Continuous monitoring; encryption key rotation; configuration drift detection | Annual FedRAMP assessment; governance maturity tracking; third-party reassessment |

---

## References

- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [FedRAMP](https://www.fedramp.gov/)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/dsgai-2026/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – DSGAI01–DSGAI21 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
