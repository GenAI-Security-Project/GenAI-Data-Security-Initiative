<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01–DSGAI21)
  Framework   : DORA – Digital Operational Resilience Act (EU Regulation 2022/2554)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 – DORA

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/dsgai-2026/)
to the [Digital Operational Resilience Act (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
(EU Regulation 2022/2554, effective 17 January 2025).

DORA establishes a binding regulatory framework for digital operational
resilience across the EU financial sector. For financial entities managing
AI data security, DORA requires that data-related risks — including data
poisoning, leakage, privacy erosion, third-party data dependency, and
governance failures — are integrated into ICT risk management, incident
reporting, resilience testing, and third-party oversight. The DSGAI 2026
mapping focuses on the data security dimensions critical to the EU financial
sector: from training data provenance and integrity, through access control
and privacy preservation, to data retention, consent management, and
cross-jurisdictional compliance. Financial institutions deploying generative
AI must ensure that AI data security risks are treated as first-class
concerns within the DORA ICT risk management framework, incident management
processes, resilience testing programmes, and third-party oversight
arrangements. This mapping enables financial institutions to trace each
OWASP DSGAI risk to specific DORA articles and implement controls satisfying
both data security and operational resilience regulatory obligations.

---

## DORA article groups

| Group | Articles | Purpose |
|---|---|---|
| ICT Risk Management | Art. 5–7 | Governance framework, risk management strategy, and data governance policies for AI data security |
| Identification | Art. 8 | Identification and classification of ICT assets including AI data stores, pipelines, and embeddings |
| Protection and Prevention | Art. 9 | Security controls for data protection, access control, integrity, and privacy preservation |
| Detection | Art. 10 | Anomaly detection, monitoring, and alerting for data security events in AI systems |
| Response and Recovery | Art. 11 | Incident response and recovery procedures for AI data security incidents |
| Backup Policies | Art. 12 | Backup and restoration of AI data, models, configurations, and lineage metadata |
| Learning and Evolving | Art. 13 | Post-incident analysis, lessons learned, and continuous improvement for AI data security |
| ICT Incident Management | Art. 17–23 | Incident classification, reporting to regulators, and communication for AI data breaches |
| Resilience Testing | Art. 24–27 | Testing data security controls, data extraction resistance, and privacy protections |
| Third-Party Risk | Art. 28–44 | Oversight of third-party data providers, AI vendors, and data processors |
| Information Sharing | Art. 45 | Threat intelligence sharing for AI data security threats across the financial sector |

---

## Quick-reference summary

| ID | Name | Severity | DORA Articles | Scope |
|---|---|---|---|---|
| DSGAI01 | Data Access Logging | High | Art. 8, Art. 9, Art. 10, Art. 17–23 | Both |
| DSGAI02 | Data Visibility | High | Art. 5–7, Art. 8 | Both |
| DSGAI03 | Shadow AI | High | Art. 28–44, Art. 8, Art. 5–7 | Both |
| DSGAI04 | Data/Artifact Poisoning | Critical | Art. 9, Art. 24–27, Art. 12 | Both |
| DSGAI05 | Data Provenance | High | Art. 8, Art. 9, Art. 28–44 | Both |
| DSGAI06 | Data Lineage | Medium | Art. 8, Art. 12, Art. 5–7 | Build |
| DSGAI07 | Excessive Aggregation | High | Art. 5–7, Art. 9 | Both |
| DSGAI08 | Data Leakage | Critical | Art. 9, Art. 17–23, Art. 10 | Both |
| DSGAI09 | IP Theft | High | Art. 9, Art. 28–44 | Both |
| DSGAI10 | Synthetic Data Risk | Medium | Art. 9, Art. 24–27, Art. 13 | Build |
| DSGAI11 | Retention/Deletion | High | Art. 5–7, Art. 12 | Both |
| DSGAI12 | Data Ownership | Medium | Art. 5–7, Art. 28–44 | Both |
| DSGAI13 | Data Misuse | High | Art. 5–7, Art. 9, Art. 17–23 | Both |
| DSGAI14 | Consent Management | High | Art. 5–7, Art. 9 | Both |
| DSGAI15 | Data Minimisation | Medium | Art. 5–7, Art. 9 | Build |
| DSGAI16 | Privacy Erosion | High | Art. 5–7, Art. 9, Art. 10 | Both |
| DSGAI17 | Bias in Data | High | Art. 5–7, Art. 24–27, Art. 13 | Both |
| DSGAI18 | Governance Gaps | High | Art. 5–7, Art. 13 | Both |
| DSGAI19 | Third-Party Data Risk | High | Art. 28–44, Art. 8, Art. 45 | Both |
| DSGAI20 | Data Localization | High | Art. 5–7, Art. 28–44 | Both |
| DSGAI21 | Non-Compliance | Critical | Art. 5–7, Art. 17–23, Art. 13 | Both |

---

## Audience tags

`data-engineer` `privacy-officer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `dpo`

- **Data engineer / ML engineer** – Art. 9 and Art. 8 entries; data protection controls and asset identification
- **Privacy officer / DPO** – Art. 5–7 entries; governance, consent, minimisation, and privacy
- **Security engineer** – Art. 9, Art. 10, Art. 17–23 entries; protection, detection, and incident management
- **Risk manager** – Art. 5–7 and Art. 28–44 entries; governance and third-party data risk
- **Compliance officer** – full file; DORA regulatory traceability for AI data security
- **CISO** – Art. 5–7 entries; data governance strategy and risk oversight

---

## Detailed mappings

---

### DSGAI01 – Data Access Logging

**Severity:** High

Insufficient logging of data access events in AI systems prevents detection
of unauthorised access, complicates forensic investigation, and undermines
regulatory audit readiness. DORA requires financial entities to identify
and classify AI data assets (Art. 8), implement protection controls for
data access (Art. 9), deploy detection mechanisms for data access anomalies
(Art. 10), and report material data access incidents to regulators
(Art. 17–23). Without comprehensive logging, financial institutions cannot
demonstrate compliance with DORA operational resilience requirements.

**Real-world references:**
- Capital One breach (2019) – misconfigured access controls and inadequate
  logging allowed mass data exfiltration to go undetected
- SolarWinds (2020) – insufficient access logging delayed identification
  of supply chain compromise across financial institutions

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Identification — data asset classification | Art. 8 | Identification | Register all AI data stores in ICT asset inventory; ensure logging coverage for all identified data assets including training data, model weights, and inference stores |
| Protection and Prevention — data access controls | Art. 9 | Protection | Implement security controls for AI data access — authentication, authorisation, and encryption; enforce least privilege on all data access paths |
| Detection — data access monitoring | Art. 10 | Detection | Deploy detection mechanisms for anomalous AI data access; monitor for unauthorised access patterns, bulk extractions, and access outside normal parameters |
| ICT Incident Management — access incident reporting | Art. 17–23 | Incidents | Classify material AI data access violations as ICT-related incidents; report to competent authorities per DORA incident classification and reporting requirements |

#### Mitigations

**Foundational**
- Art. 8: Register all AI data stores in the ICT asset inventory;
  document data sensitivity classification and logging requirements
- Art. 9: Implement authentication and authorisation on all AI data
  access paths; enforce least privilege; encrypt data at rest and in transit
- Art. 10: Deploy detection for anomalous AI data access; monitor all
  training data, model weight, and inference data access events

**Hardening**
- Art. 10: Deploy automated access anomaly detection; alert on unusual
  patterns indicative of data exfiltration or credential misuse
- Art. 17–23: Define incident classification criteria for AI data access
  violations; establish reporting procedures to competent authorities
- Art. 9: Implement time-bounded access tokens; log all access with
  full context including user, action, resource, and timestamp

**Advanced**
- Art. 10: Integrate AI data access monitoring into continuous DORA
  resilience assessment; deploy real-time analytics on access patterns
- Art. 17–23: Conduct tabletop exercises for AI data access breach
  scenarios; test regulatory reporting procedures
- Art. 8: Map data store dependencies; ensure complete logging coverage
  across all AI pipeline stages

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Elasticsearch | Open-source | https://www.elastic.co |
| Splunk | Commercial | https://www.splunk.com |
| AWS CloudTrail / Azure Monitor | Commercial | https://aws.amazon.com/cloudtrail/ |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: FedRAMP AU-2 – SP 800-218A PS.1.1-PS – ISO 27001 A.12.4

---

### DSGAI02 – Data Visibility

**Severity:** High

Lack of visibility into what data AI systems process and how it flows
through training, fine-tuning, and inference pipelines. DORA requires
governance covering data visibility (Art. 5–7) and asset identification
including data stores and pipelines (Art. 8). Without visibility, financial
entities cannot assess data-related risks, enforce data policies, or
demonstrate regulatory compliance.

**Real-world references:**
- Multiple financial institutions reported inability to trace data flows
  through AI systems during regulatory examinations (2024–2025)
- EU supervisory authorities cited data flow opacity as a top concern
  in AI adoption assessments

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — data visibility governance | Art. 5–7 | Governance | Include data visibility and transparency requirements in ICT risk management; define what AI data flows must be documented and monitored |
| Identification — data asset mapping | Art. 8 | Identification | Map all AI data assets — training data, inference data, embeddings, model artefacts — in the ICT asset inventory with data flow documentation |
| Detection — data flow monitoring | Art. 10 | Detection | Monitor AI data flows for undocumented data movement; alert on data transfers outside documented pipelines |

#### Mitigations

**Foundational**
- Art. 5–7: Define data visibility requirements for all financial AI
  systems; specify documentation and monitoring scope for each data
  category
- Art. 8: Map all AI data assets in the ICT inventory; document data
  flows from source through processing to output
- Establish data classification scheme covering AI-specific data types

**Hardening**
- Art. 5–7: Include data visibility completeness in management risk
  reporting; track coverage metrics
- Art. 8: Implement automated data flow discovery; maintain current
  data flow documentation with change detection
- Art. 10: Deploy automated data flow anomaly detection; alert on
  undocumented data movement

**Advanced**
- Art. 5–7: Include data visibility in board-level risk reporting
- Deploy real-time data flow visualisation for all AI pipelines
- Art. 8: Implement continuous data asset discovery and reconciliation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| OpenLineage | Open-source | https://openlineage.io |
| Collibra | Commercial | https://www.collibra.com |
| Alation | Commercial | https://www.alation.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: FedRAMP PM-9 – SP 800-218A PW.1.1-PS – ISO 42001 A.7.2

---

### DSGAI03 – Shadow AI

**Severity:** High

Unauthorised or unvetted AI tools and services bypass data security
controls, creating unmonitored data flows and regulatory exposure. DORA
requires third-party ICT risk management covering AI tools (Art. 28–44),
identification of all ICT assets including shadow AI services (Art. 8),
and governance policies for approved AI tools (Art. 5–7). Shadow AI in
the financial sector creates uncontrolled data processing that evades
both DORA and GDPR oversight.

**Real-world references:**
- Samsung semiconductor division employees leaked proprietary data through
  unauthorised ChatGPT usage (2023)
- Multiple banks reported shadow AI tool proliferation across trading
  desks and operations teams (2024–2025)

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Third-Party Risk — AI tool vendor oversight | Art. 28–44 | Third-Party | Include AI tools and services in third-party ICT risk management; conduct due diligence before approval; monitor ongoing compliance with financial sector requirements |
| Identification — shadow AI discovery | Art. 8 | Identification | Identify and register all AI tools — authorised and unauthorised — in the ICT asset inventory; maintain discovery mechanisms for unapproved AI services |
| ICT Risk Management — AI tool governance | Art. 5–7 | Governance | Define approved AI tools policy in ICT risk management framework; require vetting and approval before use in financial data processing |

#### Mitigations

**Foundational**
- Art. 28–44: Include AI tools in third-party risk assessment; conduct
  due diligence before approval; verify data handling practices
- Art. 8: Implement shadow AI discovery; register all AI tools in
  ICT asset inventory
- Art. 5–7: Define approved AI tools policy; communicate to all staff

**Hardening**
- Art. 28–44: Require contractual provisions for data handling,
  security, and incident notification from AI tool providers
- Art. 8: Deploy automated shadow AI detection through network
  monitoring and endpoint controls
- Art. 5–7: Include shadow AI monitoring metrics in management reporting

**Advanced**
- Art. 28–44: Conduct on-site assessment of critical AI tool providers;
  verify compliance with financial sector requirements
- Art. 8: Implement continuous shadow AI discovery with automated
  alerting and remediation workflows
- Art. 5–7: Include shadow AI risk in board-level risk reporting

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
- Other frameworks: FedRAMP CM-7 – SP 800-218A PW.4.1-PS – EBA Outsourcing Guidelines

---

### DSGAI04 – Data/Artifact Poisoning

**Severity:** Critical

Attackers corrupt training data, model weights, or pipeline artefacts to
embed backdoors, bias outputs, or degrade model reliability. DORA requires
financial entities to implement protection controls for training pipeline
integrity (Art. 9), conduct resilience testing including data poisoning
scenarios (Art. 24–27), and maintain backup and restoration capabilities
for AI data and models (Art. 12). In the financial sector, poisoned models
could produce fraudulent risk assessments, manipulated trading signals,
or biased credit decisions.

**Real-world references:**
- Nightshade (2023) – poison pixels successfully corrupted image generation
  model behaviour at scale
- BadNets (academic) – backdoor triggers embedded through poisoned training
  labels, activating only on specific inputs

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — training pipeline integrity | Art. 9 | Protection | Implement security controls protecting training data and model artefacts from poisoning, tampering, and unauthorised modification |
| Resilience Testing — poisoning detection testing | Art. 24–27 | Testing | Include data poisoning scenarios in resilience testing; test detection capabilities and recovery procedures for poisoned data and model artefacts |
| Backup Policies — model and data restoration | Art. 12 | Backup | Maintain versioned backups of training data and model weights with integrity verification; enable rollback to pre-poisoning states |
| Learning and Evolving — poisoning post-mortem | Art. 13 | Learning | Conduct post-incident analysis for data poisoning events; trace poisoned content and update protection controls |

#### Mitigations

**Foundational**
- Art. 9: Implement access controls on all training data repositories;
  enforce least privilege; log all training data modifications; verify
  artefact integrity before use
- Art. 12: Maintain versioned training data snapshots and model weight
  checkpoints with integrity hashes; document restoration procedures
- Art. 24–27: Include data poisoning detection in baseline resilience
  testing scope

**Hardening**
- Art. 9: Deploy anomaly detection on training data before each training
  run; flag statistical outliers and content inconsistent with the
  source domain
- Art. 24–27: Conduct red team exercises targeting training pipeline
  integrity; test backdoor insertion and detection capabilities
- Art. 12: Implement automated integrity verification on backup
  restoration; test rollback procedures quarterly

**Advanced**
- Apply differential privacy during training to bound the influence of
  any single training example
- Art. 24–27: Include training data poisoning in threat-led penetration
  testing (TLPT) scope; test sophisticated poisoning vectors
- Art. 9: Conduct backdoor detection on model weights before production
  deployment; establish poisoning forensics playbook

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
- Other frameworks: MITRE ATLAS AML.T0032 – FedRAMP SR-2 – SP 800-218A PS.1.1-PS

---

### DSGAI05 – Data Provenance

**Severity:** High

Insufficient provenance tracking for AI data undermines trust in model
outputs and prevents regulatory audit of data sources. DORA requires
asset identification covering data sources (Art. 8), protection controls
for data quality and integrity (Art. 9), and third-party oversight for
external data sources (Art. 28–44). In the financial sector, unverified
data provenance can lead to models trained on inappropriate, inaccurate,
or legally restricted data.

**Real-world references:**
- EU AI Act Article 10 requirements for training data documentation
  prompted financial institutions to audit AI data provenance (2025)
- Several financial AI vendors found to have used scraped data without
  proper licensing or provenance documentation

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Identification — data source documentation | Art. 8 | Identification | Document provenance, collection method, and quality characteristics for all AI training data in the ICT asset inventory |
| Protection and Prevention — data quality controls | Art. 9 | Protection | Implement data quality validation before AI pipeline ingestion; reject data failing quality or provenance thresholds |
| Third-Party Risk — external data source oversight | Art. 28–44 | Third-Party | Include external data sources in third-party risk management; assess data quality, provenance practices, and licensing compliance |

#### Mitigations

**Foundational**
- Art. 8: Document provenance for all training data sources; record
  collection method, date, licensing, and quality characteristics
- Art. 9: Implement data quality validation at pipeline ingestion
  points; define minimum quality thresholds per data type
- Art. 28–44: Assess external data source quality and provenance
  as part of third-party risk assessment

**Hardening**
- Art. 8: Implement automated provenance tracking across all AI
  data pipelines; maintain provenance chain from source to model
- Art. 9: Deploy continuous data quality monitoring; alert on quality
  degradation or provenance gaps
- Art. 28–44: Require quality attestations and provenance documentation
  from data providers

**Advanced**
- Art. 8: Include provenance completeness in regulatory reporting;
  maintain audit-ready provenance records
- Art. 9: Implement advanced data quality analytics with automated
  remediation workflows
- Art. 28–44: Conduct on-site assessment of critical data sources;
  verify provenance practices

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
- Other frameworks: FedRAMP SR-3 – SP 800-218A PS.3.1-PS – ISO 42001 A.7.4

---

### DSGAI06 – Data Lineage

**Severity:** Medium

Incomplete data lineage across AI pipelines prevents tracing how data is
transformed, combined, and consumed by models. DORA requires asset
identification covering data transformations (Art. 8), backup policies
including lineage metadata (Art. 12), and governance for lineage
requirements (Art. 5–7). Lineage gaps in financial AI systems prevent
impact analysis when data quality issues or poisoning events are detected.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Identification — data transformation mapping | Art. 8 | Identification | Map all data transformations in AI pipelines; document inputs, outputs, and processing logic for each stage |
| Backup Policies — lineage metadata preservation | Art. 12 | Backup | Include lineage metadata in backup policies; ensure lineage records can be restored alongside data and models |
| ICT Risk Management — lineage governance | Art. 5–7 | Governance | Include data lineage requirements in ICT risk management; define minimum lineage completeness per data sensitivity |

#### Mitigations

**Foundational**
- Art. 8: Map data transformations across all AI pipelines; document
  lineage for training, fine-tuning, and inference data
- Art. 12: Include lineage metadata in backup scope; ensure lineage
  can be restored alongside data
- Art. 5–7: Define lineage requirements per data sensitivity level

**Hardening**
- Art. 8: Implement automated lineage capture using pipeline
  instrumentation; maintain current lineage documentation
- Art. 12: Test lineage metadata restoration; verify lineage
  completeness after backup recovery
- Art. 5–7: Include lineage completeness in management reporting

**Advanced**
- Art. 8: Implement lineage-based impact analysis; trace downstream
  effects of data quality issues
- Art. 12: Include lineage in DORA business continuity testing
- Art. 5–7: Include lineage coverage in board-level risk reporting

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
- Other frameworks: FedRAMP CM-3 – SP 800-218A PS.3.1-PS – ISO 42001 A.7.4

---

### DSGAI07 – Excessive Aggregation

**Severity:** High

AI data aggregation creates combined datasets with higher sensitivity than
individual sources, enabling re-identification and inference attacks. DORA
requires governance covering aggregation risk (Art. 5–7) and protection
controls for aggregation boundaries (Art. 9). In the financial sector,
aggregation of customer transaction data, behavioural patterns, and
external data can create datasets that significantly exceed the sensitivity
of the originals.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — aggregation risk governance | Art. 5–7 | Governance | Include data aggregation risk in ICT risk management; assess combined sensitivity of aggregated financial datasets used in AI systems |
| Protection and Prevention — aggregation controls | Art. 9 | Protection | Implement controls preventing uncontrolled data aggregation; enforce restrictions on combining datasets that create higher-sensitivity aggregates |
| Detection — aggregation anomaly detection | Art. 10 | Detection | Monitor for excessive data aggregation patterns; alert on dataset combinations exceeding defined sensitivity thresholds |

#### Mitigations

**Foundational**
- Art. 5–7: Define aggregation risk policies; assess combined sensitivity
  of datasets before merging for AI use
- Art. 9: Implement aggregation controls; restrict dataset combination
  per sensitivity policies; require approval for high-sensitivity merges
- Classify aggregated datasets at the combined sensitivity level

**Hardening**
- Art. 5–7: Include aggregation risk in management reporting; track
  aggregation events and sensitivity levels
- Art. 9: Deploy automated aggregation enforcement; block unauthorised
  dataset combinations; implement approval workflows
- Art. 10: Deploy aggregation anomaly detection; alert on unexpected
  dataset combinations

**Advanced**
- Apply privacy-enhancing technologies — differential privacy,
  k-anonymity — to aggregated datasets before AI consumption
- Art. 5–7: Include aggregation risk in board-level risk reporting
- Deploy continuous aggregation risk assessment with automated
  sensitivity scoring

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
- Other frameworks: FedRAMP AC-6 – SP 800-218A PW.1.1-PS – GDPR Art. 25

---

### DSGAI08 – Data Leakage

**Severity:** Critical

Sensitive data exposed through model outputs, training data extraction,
misconfigured data stores, or uncontrolled inference pipelines. DORA
requires protection controls preventing data disclosure (Art. 9), incident
reporting for data breaches (Art. 17–23), and detection for leakage
indicators (Art. 10). Data leakage from financial AI systems may expose
PII, credit data, trading strategies, or regulatory-protected information.

**Real-world references:**
- EchoLeak (2025) – indirect prompt injection turned Microsoft 365 Copilot
  into a silent exfiltration engine via email content
- Samsung source code leak (2023) – proprietary data surfaced through
  employee interactions with AI tools

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — data leakage controls | Art. 9 | Protection | Implement security controls preventing AI data leakage — output monitoring, DLP, access controls, and encryption for all financial AI data |
| ICT Incident Management — data breach reporting | Art. 17–23 | Incidents | Classify AI data leakage events as ICT-related incidents; report to competent authorities per DORA incident classification criteria |
| Detection — leakage indicator monitoring | Art. 10 | Detection | Deploy detection for data leakage indicators in model outputs — PII, financial data, credentials; alert and block on detection |
| Learning and Evolving — leakage post-mortem | Art. 13 | Learning | Conduct post-incident analysis for data leakage events; identify root cause and update controls |

#### Mitigations

**Foundational**
- Art. 9: Implement output monitoring and DLP for financial AI systems;
  encrypt all AI data at rest and in transit; enforce access controls
- Art. 17–23: Define incident classification for AI data leakage;
  establish reporting procedures to competent authorities
- Art. 10: Deploy leakage detection in model outputs; monitor for
  PII, financial data, and credential patterns

**Hardening**
- Art. 9: Conduct data extraction testing before deployment; verify
  training data cannot be recovered through targeted queries
- Art. 17–23: Include AI data leakage in incident response playbooks;
  test notification procedures
- Art. 10: Deploy automated sensitive data detection and blocking
  in real time; integrate with security operations

**Advanced**
- Apply differential privacy to training pipelines; bound memorisation
  risk for sensitive financial data
- Art. 17–23: Conduct tabletop exercises for AI data breach scenarios
  involving financial regulators
- Art. 13: Establish data leakage forensics playbook; procedures for
  scope determination and regulatory notification

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
- Other frameworks: FedRAMP SC-28 – GDPR Art. 33–34 – SP 800-218A PS.1.1-PS

---

### DSGAI09 – IP Theft

**Severity:** High

AI model weights, training data, proprietary algorithms, or financial
modelling IP stolen or extracted through model inversion, side-channel
attacks, or insider threats. DORA requires protection controls for IP
assets (Art. 9) and third-party oversight to prevent IP leakage through
vendor relationships (Art. 28–44). In the financial sector, IP theft
can expose proprietary trading strategies, risk models, and competitive
advantages.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — IP protection controls | Art. 9 | Protection | Implement security controls protecting AI intellectual property — encryption, access controls, and DLP for model weights, training data, and proprietary algorithms |
| Third-Party Risk — IP protection in vendor relationships | Art. 28–44 | Third-Party | Address IP protection in third-party agreements; ensure vendors cannot access, replicate, or misuse proprietary AI assets |
| Detection — IP exfiltration detection | Art. 10 | Detection | Deploy detection for IP exfiltration attempts; monitor model weight access and download patterns |

#### Mitigations

**Foundational**
- Art. 9: Encrypt AI IP at rest and in transit; implement access
  controls; deploy DLP covering model weights and proprietary data
- Art. 28–44: Address IP ownership and protection in all AI vendor
  agreements; require confidentiality commitments
- Monitor IP access patterns; log all model weight and algorithm access

**Hardening**
- Art. 9: Implement time-bounded access for model weight access;
  enforce multi-factor authentication for IP asset download
- Art. 28–44: Require contractual commitments against model
  replication; include IP protection audit rights
- Deploy exfiltration detection analytics targeting model weight
  and training data access

**Advanced**
- Deploy model watermarking for theft detection and attribution
- Art. 9: Implement hardware-backed key management for model
  encryption; use trusted execution environments for inference
- Art. 28–44: Conduct IP protection assessments of critical AI
  vendors; verify isolation controls

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Commercial | https://www.vaultproject.io |
| Nightfall DLP | Commercial | https://www.nightfall.ai |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| AWS KMS / Azure Key Vault | Commercial | https://aws.amazon.com/kms/ |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: FedRAMP SC-28 – MITRE ATLAS AML.T0024 – SP 800-218A PS.1.1-PS

---

### DSGAI10 – Synthetic Data Risk

**Severity:** Medium

Synthetic data may encode sensitive patterns from source data, enable
re-identification, or produce statistically unfaithful representations
that degrade model quality. DORA requires protection controls for
synthetic data privacy (Art. 9), resilience testing covering synthetic
data risks (Art. 24–27), and continuous improvement for synthetic data
processes (Art. 13). Financial institutions increasingly use synthetic
data for model training and testing, making privacy validation critical.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — synthetic data privacy | Art. 9 | Protection | Implement privacy controls for synthetic data generation; validate privacy preservation and absence of sensitive pattern leakage from source financial data |
| Resilience Testing — synthetic data testing | Art. 24–27 | Testing | Include synthetic data re-identification and privacy testing in resilience testing programme; test for linkage attacks and attribute inference |
| Learning and Evolving — synthetic data improvement | Art. 13 | Learning | Apply lessons learned from synthetic data privacy failures; update generation processes and validation controls |

#### Mitigations

**Foundational**
- Art. 9: Validate synthetic data privacy before use; implement
  quality controls; verify absence of direct identifiers
- Art. 24–27: Include re-identification testing for synthetic data
  in baseline resilience testing
- Art. 13: Document synthetic data quality and privacy metrics

**Hardening**
- Art. 9: Deploy automated privacy validation for synthetic data
  generation; test for quasi-identifier combinations
- Art. 24–27: Conduct advanced re-identification testing using
  linkage attacks and background knowledge scenarios
- Art. 13: Establish feedback loops from privacy testing to
  generation parameter tuning

**Advanced**
- Deploy formal privacy guarantees — differential privacy — for
  synthetic data generation pipelines
- Art. 24–27: Include synthetic data risk in TLPT scope; test for
  sophisticated re-identification vectors
- Art. 13: Implement continuous privacy monitoring for synthetic
  data pipelines; track privacy metrics over time

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
- Other frameworks: FedRAMP SI-4 – SP 800-218A PW.7.2-PS – NIST Privacy Framework

---

### DSGAI11 – Retention/Deletion

**Severity:** High

Failure to implement appropriate retention and deletion for AI data
including training data, model weights, inference logs, and embeddings.
DORA requires governance covering retention policies (Art. 5–7) and
backup policies including deletion procedures (Art. 12). Financial
institutions face overlapping retention requirements from DORA, GDPR,
MiFID II, and national regulations, making AI data lifecycle management
particularly challenging.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — retention governance | Art. 5–7 | Governance | Include data retention policies in ICT risk management; define retention periods per data type, AI processing stage, and regulatory requirement |
| Backup Policies — retention and deletion procedures | Art. 12 | Backup | Implement backup policies aligned with retention requirements; include secure deletion procedures for expired AI data, embeddings, and model artefacts |
| Protection and Prevention — retention enforcement | Art. 9 | Protection | Enforce retention policies through automated deletion and crypto-shredding; prevent retention beyond defined periods |

#### Mitigations

**Foundational**
- Art. 5–7: Define retention policies for all AI data types —
  training data, model weights, inference logs, embeddings, and
  intermediate pipeline outputs
- Art. 12: Implement backup policies aligned with retention
  requirements; include deletion procedures for expired data
- Classify AI data per applicable retention requirements

**Hardening**
- Art. 5–7: Include retention compliance metrics in management
  reporting; track retention policy adherence
- Art. 12: Implement crypto-shredding for secure deletion of
  encrypted AI data; verify deletion completeness
- Art. 9: Deploy automated retention enforcement with verification;
  alert on retention violations

**Advanced**
- Art. 5–7: Include retention in board-level risk reporting;
  address conflicting retention requirements
- Deploy automated retention compliance verification across
  all AI data stores
- Art. 12: Include retention in DORA business continuity testing;
  verify deletion procedures work across backup media

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
- Other frameworks: FedRAMP CM-3 – GDPR Art. 17 – SP 800-218A PS.3.1-PS

---

### DSGAI12 – Data Ownership

**Severity:** Medium

Unclear data ownership and rights for AI training data, model outputs,
and derived insights creates legal, regulatory, and operational risk.
DORA requires governance covering ownership (Art. 5–7) and third-party
risk management for data rights (Art. 28–44). Financial institutions
must clarify ownership of AI-generated insights, model outputs, and
derived data to avoid disputes and ensure regulatory compliance.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — ownership governance | Art. 5–7 | Governance | Define data ownership policies for AI data; clarify rights and responsibilities for training data, model outputs, and derived financial insights |
| Third-Party Risk — data rights management | Art. 28–44 | Third-Party | Address data ownership and usage rights in third-party agreements; clarify ownership of AI outputs and derived data produced using vendor models |
| Identification — ownership mapping | Art. 8 | Identification | Map ownership for all AI data assets; document rights, restrictions, and licensing for training data and outputs |

#### Mitigations

**Foundational**
- Art. 5–7: Define ownership policies for all AI data categories —
  training data, model weights, outputs, and derived insights
- Art. 28–44: Address ownership in all third-party agreements;
  clarify who owns AI-generated outputs and derived data
- Document ownership for all AI data assets in the ICT inventory

**Hardening**
- Art. 5–7: Include ownership clarity in management reporting;
  track unresolved ownership issues
- Art. 28–44: Implement usage rights tracking for third-party data;
  monitor compliance with licensing restrictions
- Deploy automated rights management workflows for AI data

**Advanced**
- Art. 5–7: Include ownership in board-level reporting; address
  emerging ownership questions for AI-generated content
- Deploy automated rights management and licensing compliance
  for AI training data
- Art. 28–44: Conduct periodic ownership and rights audits for
  third-party AI data

#### Tools

| Tool | Type | Link |
|---|---|---|
| Collibra | Commercial | https://www.collibra.com |
| Apache Atlas | Open-source | https://atlas.apache.org |
| OneTrust | Commercial | https://www.onetrust.com |
| Alation | Commercial | https://www.alation.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: FedRAMP PM-9 – SP 800-218A PW.1.1-PS – ISO 42001 A.7.2

---

### DSGAI13 – Data Misuse

**Severity:** High

AI data used beyond original consent, purpose, or authorisation, or
manipulated for harmful outcomes. DORA requires governance covering
data usage policies (Art. 5–7), protection controls for purpose-limited
data access (Art. 9), and incident reporting for misuse events impacting
customers (Art. 17–23). Financial institutions must ensure AI data usage
respects both DORA requirements and data subject rights.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — data usage governance | Art. 5–7 | Governance | Include data usage policies in ICT risk management; define approved purposes for each AI data category; restrict repurposing |
| Protection and Prevention — purpose-limited data controls | Art. 9 | Protection | Implement controls enforcing purpose-limitation on AI data usage; restrict processing to approved purposes per data classification |
| ICT Incident Management — misuse incident reporting | Art. 17–23 | Incidents | Classify AI data misuse as ICT-related incidents where customer or regulatory impact occurs; report per DORA criteria |

#### Mitigations

**Foundational**
- Art. 5–7: Define approved purposes for each AI data category;
  document purpose restrictions in ICT risk framework
- Art. 9: Enforce purpose-limitation on AI data access; implement
  access controls aligned with approved purposes
- Art. 17–23: Define incident criteria for data misuse events

**Hardening**
- Art. 5–7: Include purpose compliance in management reporting;
  track data usage against approved purposes
- Art. 9: Implement automated purpose enforcement; deploy usage
  monitoring and alerting
- Art. 17–23: Include data misuse in incident response playbooks;
  define severity classification

**Advanced**
- Art. 5–7: Include data misuse risk in board-level reporting
- Art. 9: Deploy advanced purpose compliance verification using
  behavioural analytics and data flow analysis
- Art. 17–23: Conduct tabletop exercises for data misuse scenarios
  involving regulatory reporting

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
- Other frameworks: FedRAMP AC-3 – GDPR Art. 5 – SP 800-218A PW.1.1-PS

---

### DSGAI14 – Consent Management

**Severity:** High

Failure to manage data subject consent for AI processing — collecting,
training on, or inferring from data without appropriate consent, or
failing to honour consent withdrawal. DORA requires governance covering
consent requirements (Art. 5–7) and protection controls aligned with
consent status (Art. 9). Financial institutions must align AI data
processing with both GDPR consent requirements and DORA ICT risk
governance.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — consent governance | Art. 5–7 | Governance | Include consent management in ICT risk management; define consent requirements per data type and AI processing activity for financial services |
| Protection and Prevention — consent-aligned controls | Art. 9 | Protection | Implement access controls aligned with consent status; block AI processing on data where consent has been withdrawn or is insufficient |
| Detection — consent violation monitoring | Art. 10 | Detection | Monitor for AI processing inconsistent with consent status; alert on violations |

#### Mitigations

**Foundational**
- Art. 5–7: Define consent requirements for all AI data processing
  activities; map consent basis per data category
- Art. 9: Align access controls with consent status; implement
  mechanisms to propagate consent changes to all AI systems
- Document consent basis for all AI training data

**Hardening**
- Art. 5–7: Include consent compliance metrics in management
  reporting; track consent coverage and withdrawal handling
- Art. 9: Implement automated consent enforcement; block processing
  on consent withdrawal in real time
- Deploy consent status propagation across all AI data pipelines

**Advanced**
- Art. 5–7: Include consent management in board-level reporting
- Art. 9: Deploy real-time consent verification at data access
  points; implement consent-aware data pipelines
- Implement model retraining triggers on consent withdrawal to
  remove affected data influence

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| TrustArc | Commercial | https://trustarc.com |
| Collibra | Commercial | https://www.collibra.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI02 Misconfigured Access Controls
- Other frameworks: FedRAMP PM-9 – GDPR Art. 7 – NIST Privacy Framework

---

### DSGAI15 – Data Minimisation

**Severity:** Medium

AI systems collect, process, or retain more data than necessary for
their stated purpose. DORA requires governance covering minimisation
policies (Art. 5–7) and protection controls restricting data collection
and processing (Art. 9). Financial institutions must balance AI model
performance requirements against the data minimisation principle,
particularly for customer financial data.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — minimisation governance | Art. 5–7 | Governance | Include data minimisation in ICT risk management; define minimum necessary data per AI use case and processing activity |
| Protection and Prevention — collection restrictions | Art. 9 | Protection | Implement controls restricting AI data collection to minimum necessary; enforce at pipeline ingestion points and model training configuration |
| Identification — data necessity mapping | Art. 8 | Identification | Document data necessity justification for each AI data asset; map minimum required data per use case |

#### Mitigations

**Foundational**
- Art. 5–7: Define minimisation requirements per AI use case;
  document justification for each data element collected
- Art. 9: Restrict collection to minimum necessary data; implement
  filtering at pipeline ingestion points
- Conduct data necessity assessments for all AI systems

**Hardening**
- Art. 5–7: Include minimisation metrics in management reporting;
  track data collection volumes against justified minimums
- Art. 9: Deploy automated minimisation enforcement; block collection
  of unjustified data elements
- Implement data stripping and anonymisation at collection time

**Advanced**
- Deploy privacy-enhancing technologies — federated learning,
  secure aggregation — to reduce data requirements
- Art. 5–7: Include minimisation in board-level risk reporting
- Conduct periodic minimisation reviews as AI use cases evolve

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
- Other frameworks: FedRAMP AC-6 – GDPR Art. 5(1)(c) – NIST Privacy Framework

---

### DSGAI16 – Privacy Erosion

**Severity:** High

AI progressively erodes privacy through inference, aggregation,
memorisation, and cross-referencing of data that individually may not
be sensitive. DORA requires governance covering privacy risk (Art. 5–7),
protection controls against privacy erosion (Art. 9), and detection
for privacy degradation indicators (Art. 10). In financial services,
AI-driven inference can reveal sensitive financial circumstances,
health conditions, or life events from seemingly innocuous transaction
data.

**Real-world references:**
- Target pregnancy prediction (2012) — retail analytics inferred
  customer pregnancy from purchase patterns before the customer
  disclosed it
- Cambridge Analytica (2018) — aggregated social media data enabled
  detailed psychographic profiling beyond original data scope

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — privacy risk governance | Art. 5–7 | Governance | Include AI privacy erosion in ICT risk management; assess inference, aggregation, and memorisation risks for financial AI systems |
| Protection and Prevention — privacy-preserving controls | Art. 9 | Protection | Implement privacy-preserving controls for AI systems; prevent inference, re-identification, and memorisation-based privacy erosion |
| Detection — privacy degradation monitoring | Art. 10 | Detection | Monitor for privacy degradation indicators; detect inference attacks, re-identification attempts, and memorisation in model outputs |

#### Mitigations

**Foundational**
- Art. 5–7: Assess privacy erosion risk for each financial AI system;
  document inference, aggregation, and memorisation risk profiles
- Art. 9: Implement privacy-preserving controls; restrict AI inference
  capabilities on sensitive financial data
- Art. 10: Monitor for privacy degradation indicators in AI outputs

**Hardening**
- Art. 9: Deploy memorisation testing on trained models; verify
  training data privacy before production deployment
- Art. 5–7: Include privacy erosion risk in management reporting;
  track privacy metrics over time
- Art. 10: Deploy inference attack detection; alert on attempts
  to extract private information through model queries

**Advanced**
- Apply differential privacy to training pipelines handling
  financial customer data; track privacy budget
- Art. 5–7: Include privacy erosion in board-level risk reporting
- Art. 10: Deploy continuous privacy monitoring with automated
  response to detected privacy degradation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Opacus | Open-source | https://opacus.ai |
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| OneTrust | Commercial | https://www.onetrust.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Privilege Escalation
- Other frameworks: FedRAMP SC-28 – GDPR Art. 25 – SP 800-218A PW.1.1-PS

---

### DSGAI17 – Bias in Data

**Severity:** High

Biased training data leads to discriminatory AI outcomes in financial
services — unfair credit decisions, biased fraud detection, or
discriminatory pricing. DORA requires governance covering fairness
(Art. 5–7), resilience testing for bias detection (Art. 24–27), and
continuous improvement for fairness processes (Art. 13). Financial
regulators increasingly scrutinise AI-driven decision fairness,
making bias detection a regulatory compliance requirement.

**Real-world references:**
- Apple Card gender discrimination allegations (2019) — AI credit
  scoring produced disparate outcomes by gender
- UK FCA review of AI in financial services (2024) — highlighted
  data bias as a top consumer protection concern

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — fairness governance | Art. 5–7 | Governance | Include AI bias and fairness in ICT risk management; define fairness requirements for financial AI systems and acceptable disparity thresholds |
| Resilience Testing — bias testing | Art. 24–27 | Testing | Include bias detection and fairness testing in resilience testing programme; test for disparate impact in financial AI outputs across demographic groups |
| Learning and Evolving — fairness improvement | Art. 13 | Learning | Apply lessons learned from bias incidents; update training data, model parameters, and controls based on fairness assessments |

#### Mitigations

**Foundational**
- Art. 5–7: Define fairness requirements for all financial AI use
  cases; specify acceptable disparity thresholds per regulation
- Art. 24–27: Include bias testing in baseline resilience testing;
  measure fairness metrics across protected characteristics
- Art. 13: Document bias assessment results; track fairness trends

**Hardening**
- Art. 5–7: Include fairness metrics in management reporting;
  escalate bias findings through risk governance channels
- Art. 24–27: Conduct disparate impact testing using representative
  financial datasets; test across all protected characteristics
- Art. 13: Establish feedback loops from bias testing to training
  data curation and model parameter tuning

**Advanced**
- Deploy formal fairness constraints in model training pipelines
- Art. 5–7: Include bias risk in board-level risk reporting;
  address regulatory fairness expectations
- Art. 24–27: Include bias testing in TLPT scope; test for
  sophisticated bias vectors including proxy discrimination

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
- Other frameworks: FedRAMP SI-4 – NIST AI RMF MAP 2.3 – ISO 42001 A.6.2.6

---

### DSGAI18 – Governance Gaps

**Severity:** High

Insufficient governance for AI data management — missing policies,
unclear accountability, inadequate oversight, or fragmented governance
structures. DORA requires comprehensive ICT risk governance (Art. 5–7)
and continuous improvement processes (Art. 13). Financial institutions
with governance gaps cannot demonstrate DORA compliance, respond
effectively to AI data incidents, or maintain consistent controls
across AI deployments.

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — AI governance framework | Art. 5–7 | Governance | Establish comprehensive AI data governance within ICT risk management; define roles, policies, accountability, and oversight mechanisms |
| Learning and Evolving — governance improvement | Art. 13 | Learning | Apply lessons learned to improve AI data governance; update policies and controls based on incident analysis and regulatory changes |
| Identification — governance scope mapping | Art. 8 | Identification | Map all AI systems subject to governance; ensure complete coverage of AI data assets in governance framework |

#### Mitigations

**Foundational**
- Art. 5–7: Establish AI data governance framework; define roles,
  responsibilities, and escalation procedures; appoint data owners
  for all AI systems
- Art. 13: Implement lessons learned process for governance
  effectiveness; review and update policies annually
- Map all AI systems subject to governance requirements

**Hardening**
- Art. 5–7: Include governance maturity metrics in management
  reporting; track policy coverage and compliance rates
- Art. 13: Conduct regular governance gap analysis; compare
  against regulatory expectations and industry standards
- Implement automated governance coverage tracking across all
  AI deployments

**Advanced**
- Art. 5–7: Include governance maturity in board-level reporting;
  benchmark against financial sector peers
- Deploy automated governance monitoring and compliance dashboards
- Art. 13: Establish continuous governance improvement programme;
  integrate regulatory change monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| Collibra | Commercial | https://www.collibra.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| ServiceNow GRC | Commercial | https://www.servicenow.com |
| Alation | Commercial | https://www.alation.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- Other frameworks: FedRAMP PM-9 – NIST AI RMF GOV – ISO 42001 5.1

---

### DSGAI19 – Third-Party Data Risk

**Severity:** High

Risks from third-party data sources, AI model providers, and data
processors — including data quality issues, supply chain compromise,
vendor lock-in, and concentration risk. DORA requires comprehensive
third-party risk management (Art. 28–44), asset identification for
third-party data (Art. 8), and information sharing for threat
intelligence (Art. 45). DORA places particular emphasis on third-party
ICT risk management for the financial sector, including designation
of critical third-party providers by European Supervisory Authorities.

**Real-world references:**
- Multiple financial institutions experienced data quality degradation
  when third-party data vendors changed collection methodologies without
  notification (2024)
- ESA designation of critical cloud providers (2025) highlighted
  concentration risk in AI infrastructure

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Third-Party Risk — data provider and processor oversight | Art. 28–44 | Third-Party | Include all third-party data providers and processors in DORA third-party risk management; conduct due diligence, establish contracts, and monitor ongoing compliance |
| Identification — third-party data inventory | Art. 8 | Identification | Register all third-party data sources in ICT asset inventory; document provenance, contracts, and dependency relationships |
| Information Sharing — third-party threat intelligence | Art. 45 | Sharing | Participate in information sharing arrangements for third-party AI data risks; share threat intelligence on data provider compromises |

#### Mitigations

**Foundational**
- Art. 28–44: Include all data providers in third-party risk
  assessment; establish contractual controls covering security,
  data quality, and incident notification
- Art. 8: Register all third-party data sources in ICT asset
  inventory; document dependency relationships
- Art. 45: Establish information sharing channels for third-party
  data security threats

**Hardening**
- Art. 28–44: Identify critical data providers per DORA criteria;
  require enhanced oversight and contractual commitments;
  assess concentration risk
- Art. 8: Implement automated third-party data tracking; monitor
  for undocumented data source usage
- Art. 45: Actively participate in sector information sharing for
  AI data threats

**Advanced**
- Art. 28–44: Conduct on-site assessments of critical data providers;
  verify their security posture and data handling practices
- Art. 8: Deploy continuous third-party data monitoring with
  automated alerting on quality or security changes
- Art. 45: Contribute to and consume threat intelligence on
  third-party AI data supply chain risks

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust Vendorpedia | Commercial | https://www.onetrust.com |
| ServiceNow VRM | Commercial | https://www.servicenow.com |
| CycloneDX | Open-source | https://cyclonedx.org |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: FedRAMP SA-9 – EBA Outsourcing Guidelines – SP 800-218A PW.4.1-PS

---

### DSGAI20 – Data Localization

**Severity:** High

AI data processed or stored outside jurisdictional requirements — EU
data residency rules, national data sovereignty laws, or regulatory
restrictions on cross-border data transfer. DORA requires governance
for localisation (Art. 5–7) and third-party risk management for
cross-border data handling (Art. 28–44). Financial institutions face
strict data residency requirements, and AI workloads processed by
cloud-based providers may inadvertently cross jurisdictional boundaries.

**Real-world references:**
- Schrems II (2020) invalidated EU-US Privacy Shield, forcing
  financial institutions to reassess cross-border AI data transfers
- EU Data Act (2024) introduced additional data localisation
  requirements impacting AI deployments

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — localisation governance | Art. 5–7 | Governance | Include data localisation in ICT risk management; define residency requirements per jurisdiction and data type for AI systems |
| Third-Party Risk — cross-border data oversight | Art. 28–44 | Third-Party | Address data localisation in third-party agreements; verify provider data processing locations meet residency requirements; monitor for unauthorised cross-border transfers |
| Identification — data location mapping | Art. 8 | Identification | Map physical and logical locations of all AI data; document processing jurisdictions for training, inference, and storage |

#### Mitigations

**Foundational**
- Art. 5–7: Define localisation requirements per applicable laws
  and regulations; map requirements to AI data categories
- Art. 28–44: Verify provider data processing locations; include
  localisation commitments in contracts
- Document data processing locations for all AI workloads

**Hardening**
- Art. 5–7: Include localisation compliance in management reporting;
  track data residency status across all AI systems
- Art. 28–44: Require contractual localisation commitments; implement
  monitoring for provider compliance
- Deploy automated cross-border transfer detection and blocking

**Advanced**
- Art. 5–7: Include localisation in board-level risk reporting;
  address evolving jurisdictional requirements
- Art. 28–44: Conduct provider location verification audits;
  verify physical infrastructure locations
- Implement continuous localisation compliance monitoring with
  automated enforcement at network boundaries

#### Tools

| Tool | Type | Link |
|---|---|---|
| AWS Region Controls / Azure Policy | Commercial | https://aws.amazon.com/compliance/data-residency/ |
| Netskope | Commercial | https://www.netskope.com |
| OneTrust | Commercial | https://www.onetrust.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI04 Supply Chain Compromise
- Other frameworks: FedRAMP SC-7 – GDPR Art. 44–49 – DORA Art. 28–44

---

### DSGAI21 – Non-Compliance

**Severity:** Critical

AI systems fail to comply with applicable data protection and financial
regulations — GDPR, DORA, MiFID II, PSD2, national data protection
laws, or sector-specific requirements. DORA requires governance covering
regulatory compliance (Art. 5–7), incident reporting for material
compliance failures (Art. 17–23), and continuous improvement for
compliance processes (Art. 13). Non-compliance in the financial sector
can result in significant fines, licence revocation, and reputational
damage.

**Real-world references:**
- Meta GDPR fine of EUR 1.2 billion (2023) for unlawful cross-border
  data transfers — directly applicable to AI training data
- Italian DPA temporarily banned ChatGPT (2023) over GDPR compliance
  concerns, affecting financial institutions using the service

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — regulatory compliance governance | Art. 5–7 | Governance | Include regulatory compliance in ICT risk management; map applicable data laws to AI processing activities; define compliance requirements and accountability |
| ICT Incident Management — compliance incident reporting | Art. 17–23 | Incidents | Classify material regulatory non-compliance events as ICT incidents; report to competent authorities per DORA criteria; coordinate with DPO for GDPR notifications |
| Learning and Evolving — compliance improvement | Art. 13 | Learning | Apply lessons learned from compliance failures; update controls and processes based on regulatory changes, enforcement actions, and incident analysis |
| Identification — regulated data mapping | Art. 8 | Identification | Map all AI data subject to regulatory requirements; ensure complete coverage in compliance programme |

#### Mitigations

**Foundational**
- Art. 5–7: Map all applicable data laws to AI processing activities;
  define compliance requirements per data type and jurisdiction
- Art. 17–23: Define incident classification criteria for compliance
  failures; establish reporting procedures including GDPR breach
  notification coordination
- Art. 13: Document compliance assessment results; track regulatory
  changes affecting AI data processing

**Hardening**
- Art. 5–7: Include compliance status in management reporting; track
  compliance metrics across all AI systems and jurisdictions
- Art. 17–23: Include compliance failures in incident response
  playbooks; test notification procedures with regulatory bodies
- Art. 13: Conduct regular compliance reassessment; update controls
  for new regulations and enforcement guidance

**Advanced**
- Art. 5–7: Include compliance in board-level risk reporting;
  maintain regulatory change monitoring programme
- Deploy automated compliance monitoring across all AI systems;
  implement continuous compliance verification
- Art. 13: Establish continuous compliance improvement programme;
  benchmark against regulatory expectations and enforcement trends

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
- Other frameworks: FedRAMP PM-9 – GDPR – CCPA – DORA Art. 5–7

---

## Implementation priority

| Phase | Governance (Art. 5–7) | Protection & Detection (Art. 9–10) | Incidents, Testing & Third-Party (Art. 11–44) |
|---|---|---|---|
| 1 – Now | Data governance framework for DSGAI18/21; data access policies for DSGAI01; consent governance for DSGAI14 | Art. 9 data leakage controls for DSGAI08; poisoning protection for DSGAI04; access controls for DSGAI01/09 | Art. 28–44 data provider assessment for DSGAI04/19; Art. 17–23 incident criteria for DSGAI08/21 |
| 2 – This sprint | Retention policies for DSGAI11; minimisation governance for DSGAI15; ownership policies for DSGAI12; localisation policies for DSGAI20 | Art. 9 data quality validation for DSGAI05; shadow AI blocking for DSGAI03; Art. 10 access monitoring for DSGAI01; leakage detection for DSGAI08 | Art. 28–44 shadow AI vendor assessment for DSGAI03; third-party data oversight for DSGAI19; Art. 12 backup for DSGAI04/11 |
| 3 – This quarter | Visibility governance for DSGAI02; lineage for DSGAI06; aggregation for DSGAI07; fairness for DSGAI17; privacy for DSGAI16 | Art. 10 bias monitoring for DSGAI17; aggregation detection for DSGAI07; Art. 9 privacy controls for DSGAI16; Art. 10 privacy monitoring for DSGAI16 | Art. 24–27 privacy and bias testing for DSGAI10/16/17; Art. 28–44 critical provider assessments; Art. 13 post-mortem processes |
| 4 – Ongoing | Governance maturity tracking; board-level reporting; regulatory change monitoring for DSGAI21 | Continuous monitoring; detection tuning; privacy control updates | Annual resilience testing; third-party reassessment; Art. 45 information sharing for DSGAI19 |

---

## References

- [DORA – EU Regulation 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [EBA DORA Regulatory Technical Standards](https://www.eba.europa.eu/regulation-and-policy/digital-operational-resilience-act-dora)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/dsgai-2026/)
- [GDPR – EU Regulation 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [ENISA Threat Landscape for AI](https://www.enisa.europa.eu/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – DSGAI01–DSGAI21 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
