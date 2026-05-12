<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01–DSGAI21)
  Framework   : NIST SP 800-218A Secure Software Development Practices for Generative AI and Dual-Use Foundation Models
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 – NIST SP 800-218A

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/dsgai-2026/)
to [NIST SP 800-218A: Secure Software Development Practices for Generative AI and Dual-Use Foundation Models](https://doi.org/10.6028/NIST.SP.800-218A.ipd)
(Initial Public Draft, March 2024).

NIST SP 800-218A extends the Secure Software Development Framework (SSDF)
with AI-specific practices covering the full lifecycle of generative AI and
foundation model development. The DSGAI 2026 mapping focuses on the data
security dimensions of GenAI systems — training data protection, data
governance, privacy preservation, and regulatory compliance. It addresses
how organisations can leverage SP 800-218A to secure the data that flows
into, through, and out of AI pipelines: from provenance and lineage of
training corpora, through access control and integrity of model artefacts,
to data retention, consent management, and cross-jurisdictional compliance.
Organisations following SSDF for their conventional software estate can
extend that programme to their AI data security posture using this mapping.
US federal agencies are directed to align with SP 800-218A under OMB
memoranda referencing the SSDF.

---

## SP 800-218A practice groups

| Group | ID | Purpose |
|---|---|---|
| Produce Well-Secured Software | PW | Security requirements, design, reuse, secure coding, review, and testing across the AI development lifecycle |
| Protect the Software | PS | Protecting model weights, training data, pipeline code, and build artefacts from unauthorised access and tampering |
| Respond to Vulnerabilities | RV | Identifying, assessing, remediating, and analysing AI-specific vulnerabilities including emergent behaviours |

---

## Quick-reference summary

| ID | Name | Severity | SP 800-218A Practices | Scope |
|---|---|---|---|---|
| DSGAI01 | Data Access Logging | High | PS.1.1-PS, RV.1.1-PS | Both |
| DSGAI02 | Data Visibility & Transparency | High | PW.1.1-PS, PW.2.1-PS | Both |
| DSGAI03 | Shadow AI & Unvetted Tools | High | PW.4.1-PS, PS.1.1-PS, RV.1.1-PS | Both |
| DSGAI04 | Data Model & Artifact Poisoning | Critical | PS.1.1-PS, PS.3.1-PS, PW.4.1-PS, RV.3.1-PS | Both |
| DSGAI05 | Data Provenance & Quality | High | PS.2.1-PS, PS.3.1-PS, PW.4.1-PS | Both |
| DSGAI06 | Data Lineage Fragmentation | Medium | PS.3.1-PS, PW.2.1-PS | Build |
| DSGAI07 | Excessive Data Aggregation | High | PW.1.1-PS, PW.2.1-PS | Both |
| DSGAI08 | Data Leakage & Exposure | Critical | PS.1.1-PS, PW.5.1-PS, PW.7.2-PS | Both |
| DSGAI09 | Intellectual Property Theft | High | PS.1.1-PS, PS.3.1-PS | Both |
| DSGAI10 | Synthetic Data Generation Risk | Medium | PW.7.2-PS, PW.8.2-PS, RV.3.1-PS | Build |
| DSGAI11 | Data Retention & Deletion | High | PW.1.1-PS, PS.3.1-PS, RV.2.1-PS | Both |
| DSGAI12 | Data Ownership & Monetisation | Medium | PW.1.1-PS, PS.1.1-PS | Both |
| DSGAI13 | Data Misuse & Manipulation | High | PW.1.1-PS, PW.7.2-PS, RV.1.1-PS | Both |
| DSGAI14 | Consent Management Failures | High | PW.1.1-PS, PW.2.1-PS | Both |
| DSGAI15 | Data Minimisation Violations | Medium | PW.1.1-PS, PW.2.1-PS | Build |
| DSGAI16 | Erosion of Privacy | High | PW.1.1-PS, PW.2.1-PS, PS.1.1-PS | Both |
| DSGAI17 | Bias in Data | High | PW.7.2-PS, PW.8.2-PS, RV.3.1-PS | Both |
| DSGAI18 | Governance Gaps | High | PW.1.1-PS, PW.2.1-PS, RV.3.1-PS | Both |
| DSGAI19 | Third-Party Data Risk | High | PW.4.1-PS, PS.2.1-PS, RV.1.1-PS | Both |
| DSGAI20 | Data Localization Violations | High | PW.1.1-PS, PS.1.1-PS, PS.3.1-PS | Both |
| DSGAI21 | Non-Compliance with Data Laws | Critical | PW.1.1-PS, PW.2.1-PS, RV.3.1-PS | Both |

---

## Audience tags

`data-engineer` `privacy-officer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `dpo`

- **Data engineer / ML engineer** – PW and PS practices per entry; data pipeline security and governance
- **Privacy officer / DPO** – PW.1 and PW.2 entries; data minimisation, consent, and retention requirements
- **Security engineer** – PS and RV practices; access logging, integrity verification, and incident response
- **Compliance officer** – full file; SSDF alignment, regulatory traceability, and data law compliance
- **CISO** – PW.1 and PW.2 entries; data governance strategy and risk prioritisation

---

## Detailed mappings

---

### DSGAI01 – Data Access Logging

**Severity:** High

Insufficient logging of data access across AI pipelines prevents detection of
unauthorised data retrieval, training data exfiltration, and abuse of model
query interfaces. SP 800-218A addresses this through access protection and
audit controls on training data and pipeline artefacts (PS.1), and
vulnerability identification procedures that depend on comprehensive audit
trails (RV.1).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Protect all code from unauthorised access — data access audit controls | PS.1.1-PS | PS | Implement comprehensive audit logging for all access to training data, model weights, embedding stores, and pipeline configuration; enforce tamper-evident log storage |
| Identify and confirm vulnerabilities — audit-driven detection | RV.1.1-PS | RV | Establish procedures to detect data access anomalies using audit logs; define triage workflows for suspicious access patterns across AI data stores |

#### Mitigations

**Foundational**
- PS.1.1-PS: Enable audit logging on all training data repositories, model
  registries, and embedding stores — log identity, timestamp, data object,
  and operation type for every access event
- Define a data access logging policy that covers all AI pipeline stages
  from data ingestion through inference; enforce at architecture review
- RV.1.1-PS: Establish baseline access patterns for AI data stores;
  configure alerts for deviations including bulk downloads, out-of-hours
  access, and access from unexpected identities

**Hardening**
- PS.1.1-PS: Implement tamper-evident log storage — write-once storage or
  cryptographic chaining to prevent log deletion or modification by
  compromised accounts
- RV.1.1-PS: Integrate AI data access logs into your SIEM; create
  correlation rules for multi-stage exfiltration patterns across training
  data, embeddings, and model query interfaces
- Implement per-dataset and per-model access quotas; alert on consumption
  anomalies that may indicate exfiltration attempts

**Advanced**
- PS.1.1-PS: Deploy data-level access logging that captures field-level
  access within structured training datasets — not just file-level access
- RV.1.1-PS: Build automated anomaly detection models over access logs
  to identify subtle exfiltration patterns invisible to rule-based alerts
- Conduct quarterly access log reviews with data stewards to verify
  access patterns align with authorised use cases

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Elastic SIEM | Open-source | https://www.elastic.co/security |
| AWS CloudTrail | Commercial | https://aws.amazon.com/cloudtrail/ |
| Azure Monitor | Commercial | https://azure.microsoft.com/en-us/products/monitor |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM07 System Prompt Leakage
- Agentic Top 10: ASI02 Tool Misuse, ASI06 Memory & Context Poisoning
- Other frameworks: NIST CSF 2.0 DE.CM – ISO 42001 6.1.2 – SSDF PS.1

---

### DSGAI02 – Data Visibility & Transparency

**Severity:** High

Lack of visibility into what data is used across AI systems prevents
informed governance decisions and regulatory compliance. SP 800-218A
addresses this through security requirements that mandate data inventory
and classification (PW.1), and design practices requiring data flow
documentation (PW.2).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — data inventory and classification | PW.1.1-PS | PW | Define security requirements mandating a complete data inventory covering all datasets used in training, fine-tuning, RAG, and evaluation; classify by sensitivity |
| Design software — data flow transparency | PW.2.1-PS | PW | Design AI pipelines with documented data flow diagrams showing data origins, transformations, storage locations, and access points; maintain as living artefacts |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish a comprehensive data inventory for all AI systems
  covering training datasets, fine-tuning corpora, RAG sources, evaluation
  benchmarks, and prompt templates — classify each by sensitivity level
- PW.2.1-PS: Create and maintain data flow diagrams for every AI pipeline;
  document data origins, transformations, intermediate storage, and all
  consumers of each dataset
- Define data visibility requirements as mandatory security design
  requirements reviewed at architecture gates

**Hardening**
- PW.1.1-PS: Implement automated data discovery and classification tools
  to detect undocumented datasets entering AI pipelines; alert on
  unclassified data usage
- PW.2.1-PS: Integrate data lineage tracking into ML pipeline orchestration
  tools; automatically capture data transformations and dependencies
- Publish data transparency reports for internal stakeholders documenting
  what data each AI system consumes and how it is processed

**Advanced**
- PW.1.1-PS: Implement continuous data inventory reconciliation — compare
  declared data usage against actual pipeline execution logs to detect
  undeclared data sources
- PW.2.1-PS: Deploy runtime data flow monitoring that validates actual
  data movement matches documented architecture; alert on deviations
- Extend transparency to external stakeholders where required by
  regulation — publish model cards documenting data usage

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| Amundsen | Open-source | https://www.amundsen.io |
| Google Data Catalog | Commercial | https://cloud.google.com/data-catalog |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- Other frameworks: EU AI Act Art. 13 – ISO 42001 A.7 – NIST AI RMF Map 1.1

---

### DSGAI03 – Shadow AI & Unvetted Tools

**Severity:** High

Employees deploy unsanctioned AI tools that process organisational data
outside governed pipelines, creating uncontrolled data flows and compliance
blind spots. SP 800-218A addresses this through third-party component vetting
(PW.4), access controls that detect unauthorised tool usage (PS.1), and
vulnerability identification for shadow AI exposure (RV.1).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Reuse existing well-secured software — AI tool vetting | PW.4.1-PS | PW | Vet all AI tools, services, and plugins before organisational adoption; verify data handling, security posture, and compliance capabilities |
| Protect all code from unauthorised access — shadow AI detection | PS.1.1-PS | PS | Implement controls to detect and prevent unauthorised AI tool usage that processes organisational data outside governed pipelines |
| Identify and confirm vulnerabilities — shadow AI exposure monitoring | RV.1.1-PS | RV | Establish procedures to identify data exposure from shadow AI tool usage; define triage and remediation workflows for unsanctioned data processing |

#### Mitigations

**Foundational**
- PW.4.1-PS: Establish an approved AI tools registry — all AI tools and
  services must pass security and data handling review before organisational
  use; publish the approved list and enforce through policy
- PS.1.1-PS: Implement network-level controls to detect data flows to
  known AI service endpoints from corporate networks — DLP policies that
  flag uploads to unsanctioned AI services
- Define an acceptable AI use policy that specifies data classification
  restrictions for AI tool usage; enforce through training and monitoring

**Hardening**
- RV.1.1-PS: Deploy CASB or equivalent controls to monitor and alert on
  organisational data sent to unsanctioned AI services; establish triage
  procedures for detected shadow AI usage
- PW.4.1-PS: Require AI tool vendors to provide data processing agreements,
  security certifications, and data residency commitments before approval
- PS.1.1-PS: Implement endpoint DLP controls that detect copy-paste of
  sensitive data into browser-based AI tools

**Advanced**
- PW.4.1-PS: Conduct periodic shadow AI audits — scan network logs, SaaS
  usage data, and expense reports for evidence of unsanctioned AI tool
  procurement or usage
- RV.1.1-PS: Build automated shadow AI detection pipelines that
  continuously monitor for new AI service endpoints and alert on first use
- PS.1.1-PS: Integrate shadow AI controls into ZTNA policies; block
  data transfer to unapproved AI services at the identity layer

#### Tools

| Tool | Type | Link |
|---|---|---|
| Netskope | Commercial | https://www.netskope.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-cloud-apps |
| Zscaler | Commercial | https://www.zscaler.com |
| OpenDLP | Open-source | https://github.com/ezarko/opendlp |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities, LLM06 Excessive Agency
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities, ASI10 AI Agent Dependency Failures
- Other frameworks: NIST CSF 2.0 ID.AM – ISO 27001 A.8.1 – CIS Control 2

---

### DSGAI04 – Data Model & Artifact Poisoning

**Severity:** Critical

Attackers corrupt training data, model weights, or pipeline artefacts to
embed backdoors, bias outputs, or compromise downstream systems. This is
the data security perspective of training data poisoning — focused on
protecting the integrity of data assets throughout the AI supply chain.
SP 800-218A addresses this through access protection (PS.1), versioned
artefact management (PS.3), supply chain vetting (PW.4), and root cause
analysis (RV.3).

**Real-world references:**
- Nightshade (2023) – poison pixels corrupted image generation model
  behaviour at scale through training data manipulation
- Hugging Face model repository incidents (2024) – malicious model
  artefacts uploaded to public repositories with embedded payloads

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Protect all code from unauthorised access — data and artefact integrity | PS.1.1-PS | PS | Protect training data, model weights, adapters, and pipeline artefacts from unauthorised modification; enforce write access controls and integrity monitoring |
| Archive and protect software releases — versioned artefact management | PS.3.1-PS | PS | Maintain versioned, integrity-verified snapshots of all training data, model checkpoints, and pipeline artefacts; enable rollback to known-good state |
| Reuse existing well-secured software — dataset and artefact vetting | PW.4.1-PS | PW | Vet all third-party datasets, pre-trained models, and pipeline components for provenance, integrity, and potential poisoning before use |
| Analyse root causes — poisoning forensics | RV.3.1-PS | RV | When poisoning is detected, conduct forensic analysis to identify corrupted records, trace to source, and determine blast radius across dependent models |

#### Mitigations

**Foundational**
- PS.1.1-PS: Implement strict write access controls on all training data
  repositories, model registries, and pipeline artefact stores — enforce
  least privilege with MFA for write operations; log all modifications
- PW.4.1-PS: Establish a data and artefact approval process — all new
  datasets and pre-trained models must pass provenance, integrity, and
  statistical quality review before entering any pipeline
- PS.3.1-PS: Implement immutable versioning for all training data snapshots
  and model checkpoints — every training run must reference a specific,
  integrity-verified version

**Hardening**
- PW.4.1-PS: Apply anomaly detection to training data before each run —
  flag statistical outliers, unexpected distributions, and content
  inconsistent with the declared source domain
- PS.3.1-PS: Maintain a secure artefact registry with signed checksums;
  implement automated integrity verification on every pipeline stage
  transition
- RV.3.1-PS: Establish a poisoning forensics playbook — procedures for
  isolating corrupted data, tracing to origin, and determining influence
  on model weights and downstream consumers

**Advanced**
- PW.4.1-PS: Conduct backdoor detection (neural cleanse or equivalent)
  on all new model versions trained on external data before production
  promotion
- Apply differential privacy during training to bound the influence of
  any single training example — measure and track privacy budget
- RV.3.1-PS: Implement continuous data integrity monitoring — alert on
  distribution drift in training data that may indicate ongoing poisoning

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities, ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 – NIST CSF 2.0 PR.DS-8 – ISO 42001 6.1.2

---

### DSGAI05 – Data Provenance & Quality

**Severity:** High

AI systems trained on data of unknown origin or poor quality produce
unreliable outputs and introduce unquantified risk. SP 800-218A addresses
this through integrity verification of data supply chains (PS.2), versioned
data management with provenance records (PS.3), and third-party dataset
vetting (PW.4).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Verify software integrity — data provenance verification | PS.2.1-PS | PS | Verify provenance and integrity of all datasets used in training, fine-tuning, and evaluation; maintain cryptographic attestation of data origin and chain of custody |
| Archive and protect software releases — data versioning with provenance | PS.3.1-PS | PS | Maintain versioned dataset snapshots with provenance metadata recording origin, collection method, processing steps, and quality metrics |
| Reuse existing well-secured software — dataset quality vetting | PW.4.1-PS | PW | Vet all datasets for quality, completeness, representativeness, and fitness for purpose before use in any training or evaluation pipeline |

#### Mitigations

**Foundational**
- PS.2.1-PS: Establish provenance requirements for all training data —
  every dataset must have documented origin, collection methodology,
  licensing terms, and chain of custody before entering any pipeline
- PW.4.1-PS: Define data quality gates for AI pipelines — completeness,
  consistency, accuracy, and representativeness thresholds that datasets
  must meet before use
- PS.3.1-PS: Implement dataset versioning with provenance metadata;
  every training run must reference a specific dataset version with
  complete provenance record

**Hardening**
- PS.2.1-PS: Implement cryptographic data provenance — hash chains or
  digital signatures on dataset snapshots that provide tamper-evident
  chain of custody from source to training pipeline
- PW.4.1-PS: Deploy automated data quality monitoring — statistical
  profiling, schema validation, and distribution analysis on every
  dataset version before pipeline ingestion
- PS.3.1-PS: Maintain a data catalogue with searchable provenance
  records enabling traceability from any model output to its training
  data lineage

**Advanced**
- PS.2.1-PS: Implement W3C PROV or equivalent provenance standard for
  all AI data assets — enable machine-readable provenance queries across
  the full data supply chain
- PW.4.1-PS: Build automated data quality scoring that continuously
  monitors dataset health metrics and alerts on degradation trends
- Extend provenance tracking to cover synthetic data generation —
  record the source model, parameters, and seed data for all generated
  training content

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| DVC (Data Version Control) | Open-source | https://dvc.org |
| Apache Atlas | Open-source | https://atlas.apache.org |
| Pachyderm | Open-source | https://www.pachyderm.com |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- Other frameworks: NIST AI RMF Map 2.3 – ISO 42001 A.7.3 – EU AI Act Art. 10

---

### DSGAI06 – Data Lineage Fragmentation

**Severity:** Medium

When data transformations across AI pipelines are not tracked end-to-end,
organisations lose the ability to audit what data contributed to a model
output, complicating compliance, debugging, and incident response. SP 800-218A
addresses this through versioned artefact management with lineage metadata
(PS.3) and design requirements for traceable data pipelines (PW.2).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Archive and protect software releases — lineage-aware artefact management | PS.3.1-PS | PS | Maintain end-to-end data lineage records linking every model version to its training data, transformations, and intermediate artefacts |
| Design software — traceable data pipeline architecture | PW.2.1-PS | PW | Design AI data pipelines with built-in lineage tracking; require lineage metadata capture at every transformation step as an explicit design requirement |

#### Mitigations

**Foundational**
- PS.3.1-PS: Implement data lineage tracking that records the full
  transformation chain from raw data sources through preprocessing,
  augmentation, and training to model artefact — link every model
  version to its complete data ancestry
- PW.2.1-PS: Include end-to-end data lineage as an explicit design
  requirement for all AI pipelines; review at architecture gates
- Define lineage metadata standards specifying what must be captured at
  each pipeline stage — source, transformation, timestamp, operator, and
  output hash

**Hardening**
- PS.3.1-PS: Deploy automated lineage capture integrated with ML pipeline
  orchestration tools (MLflow, Kubeflow, etc.) — eliminate manual lineage
  documentation that becomes stale
- PW.2.1-PS: Design data pipelines as directed acyclic graphs with
  immutable intermediate artefacts; lineage is inherent in the pipeline
  structure
- Implement lineage validation gates — block model promotion if lineage
  records are incomplete or inconsistent

**Advanced**
- PS.3.1-PS: Build queryable lineage graphs that enable forward and
  backward tracing — from any data source to all affected models and
  from any model to all contributing data sources
- PW.2.1-PS: Integrate lineage with incident response — enable rapid
  identification of all models affected when a data source is found to
  be compromised or biased
- Implement lineage-based impact analysis for data retention and deletion
  requests — trace which models must be retrained when data is removed

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenLineage | Open-source | https://openlineage.io |
| Marquez | Open-source | https://marquezproject.ai |
| MLflow | Open-source | https://mlflow.org |
| DataHub | Open-source | https://datahubproject.io |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST AI RMF Measure 2.6 – ISO 42001 A.7.3 – EU AI Act Art. 12

---

### DSGAI07 – Excessive Data Aggregation

**Severity:** High

AI systems that aggregate data across multiple sources create combined
datasets whose sensitivity exceeds the classification of any individual
source, enabling re-identification, inference attacks, and privacy violations.
SP 800-218A addresses this through security requirements that govern data
combination policies (PW.1) and design practices requiring aggregation risk
analysis (PW.2).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — data aggregation controls | PW.1.1-PS | PW | Define security requirements governing how datasets may be combined for AI training and inference; require aggregation impact assessments before merging datasets |
| Design software — aggregation-aware data architecture | PW.2.1-PS | PW | Design AI data pipelines with aggregation controls that prevent combination of datasets whose joint sensitivity exceeds authorised classification levels |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish a data aggregation policy for AI systems — require
  a privacy and sensitivity impact assessment before any dataset merge
  operation that combines data from different sources or classifications
- PW.2.1-PS: Design data pipelines with explicit aggregation boundaries;
  document which dataset combinations are authorised and which are
  prohibited
- Classify combined datasets at the highest sensitivity of any
  contributing source plus aggregation uplift where re-identification
  risk increases

**Hardening**
- PW.1.1-PS: Implement technical controls that enforce aggregation
  policies — automated checks that verify dataset combination compliance
  before pipeline execution
- PW.2.1-PS: Conduct re-identification risk assessments on aggregated
  datasets before use in training; apply k-anonymity, l-diversity, or
  differential privacy as appropriate
- Deploy data masking or tokenisation on identifying fields before
  aggregation into training datasets

**Advanced**
- PW.1.1-PS: Build automated aggregation risk scoring that evaluates
  re-identification probability as datasets are combined; block
  high-risk aggregations without explicit approval
- PW.2.1-PS: Implement privacy-preserving data aggregation techniques
  — federated learning, secure multi-party computation, or
  differential privacy mechanisms for cross-source training
- Conduct periodic re-identification audits on production training
  datasets to verify aggregation controls remain effective

#### Tools

| Tool | Type | Link |
|---|---|---|
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| OpenDP | Open-source | https://opendp.org |
| Google Differential Privacy | Open-source | https://github.com/google/differential-privacy |
| Presidio | Open-source | https://github.com/microsoft/presidio |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM08 Vector and Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: GDPR Art. 5(1)(c) – NIST Privacy Framework CT.DM-P – ISO 27701 A.7.4

---

### DSGAI08 – Data Leakage & Exposure

**Severity:** Critical

Sensitive data leaks through model outputs, training data memorisation,
embedding inversion, or insecure pipeline configurations — exposing PII,
trade secrets, or classified information. SP 800-218A addresses this
through access protection (PS.1), secure coding for data handling (PW.5),
and output review for unintended disclosure (PW.7).

**Real-world references:**
- Samsung source code leak (2023) — proprietary code exposed through
  employee prompts to ChatGPT
- Training data extraction attacks (Carlini et al., 2023) — verbatim
  training data extracted from production LLMs

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Protect all code from unauthorised access — data exfiltration prevention | PS.1.1-PS | PS | Implement controls preventing sensitive data exfiltration through model interfaces, API endpoints, and pipeline outputs; enforce data classification boundaries |
| Secure coding — data handling in AI pipelines | PW.5.1-PS | PW | Enforce secure coding practices for all data handling in AI pipelines; implement output filtering, PII detection, and data masking before model responses reach consumers |
| Review for security vulnerabilities — data leakage review | PW.7.2-PS | PW | Include data leakage and memorisation scenarios in pre-release security reviews; verify that outputs cannot reveal training data or sensitive context |

#### Mitigations

**Foundational**
- PS.1.1-PS: Classify all data entering AI pipelines by sensitivity;
  implement DLP controls on model output channels that detect and block
  responses containing PII, credentials, or data above the authorised
  classification level
- PW.5.1-PS: Enforce secure data handling standards across all AI
  pipeline code — no plaintext storage of sensitive training data, no
  logging of PII in inference traces, encryption at rest and in transit
- PW.7.2-PS: Include training data memorisation and extraction scenarios
  in pre-release security reviews; test whether models can reproduce
  sensitive training content

**Hardening**
- PS.1.1-PS: Deploy output-side DLP that scans model responses in
  real-time for PII, credentials, and sensitive patterns; block or
  redact before delivery to the consumer
- PW.7.2-PS: Conduct memorisation audits — use extraction attacks
  against your own models to quantify memorisation risk before
  production deployment
- PW.5.1-PS: Implement data masking in training data preprocessing —
  replace or tokenise PII before data enters training pipelines

**Advanced**
- Apply differential privacy during training to bound memorisation risk;
  measure and report the privacy guarantee (epsilon) for each model
- PS.1.1-PS: Deploy canary data detection — embed known canary records
  in training data and monitor model outputs for canary reproduction
  as an ongoing memorisation indicator
- PW.7.2-PS: Implement automated data leakage testing in CI/CD — gate
  model promotion on passing extraction resistance benchmarks

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Nightfall | Commercial | https://www.nightfall.ai |
| OpenDP | Open-source | https://opendp.org |

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage, LLM01 Prompt Injection
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- Other frameworks: MITRE ATLAS AML.T0024 – GDPR Art. 32 – NIST CSF 2.0 PR.DS-5

---

### DSGAI09 – Intellectual Property Theft

**Severity:** High

AI models and their training data represent significant intellectual
property that can be stolen through model extraction attacks, training
data reconstruction, or unauthorised access to model registries. SP 800-218A
addresses this through access protection of model assets (PS.1) and
versioned, access-controlled artefact management (PS.3).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Protect all code from unauthorised access — IP protection | PS.1.1-PS | PS | Protect model weights, architecture specifications, training data, and proprietary algorithms from unauthorised access; implement defence against model extraction attacks |
| Archive and protect software releases — IP asset management | PS.3.1-PS | PS | Maintain access-controlled, versioned registries for all IP-sensitive AI artefacts; enforce need-to-know access and log all access events |

#### Mitigations

**Foundational**
- PS.1.1-PS: Classify model weights, architecture specifications, and
  proprietary training data as trade secrets or restricted IP; apply
  access controls commensurate with classification — need-to-know basis,
  MFA, and full audit logging
- PS.3.1-PS: Maintain all IP-sensitive AI artefacts in access-controlled
  registries with versioning and audit trails; restrict export and
  download capabilities
- Define an AI IP protection policy covering model weights, training
  data, and proprietary algorithms; include in employee and contractor
  agreements

**Hardening**
- PS.1.1-PS: Deploy rate limiting and query monitoring on model
  inference APIs to detect and throttle model extraction attacks —
  alert on query patterns consistent with model stealing
- PS.3.1-PS: Implement watermarking of model weights to enable
  detection of stolen models in third-party deployments
- Encrypt model weights at rest and in transit; implement secure
  enclaves for model serving where classification warrants it

**Advanced**
- PS.1.1-PS: Conduct model extraction red team exercises — test
  whether your deployed models can be functionally replicated through
  API access and quantify extraction resistance
- Deploy fingerprinting techniques that enable identification of
  model copies even after fine-tuning or distillation by adversaries
- PS.3.1-PS: Implement data room controls for highly sensitive model
  artefacts — time-limited, audited access sessions with no export
  capability

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Sigstore | Open-source | https://www.sigstore.dev |
| AWS Nitro Enclaves | Commercial | https://aws.amazon.com/ec2/nitro/nitro-enclaves/ |
| Azure Confidential Computing | Commercial | https://azure.microsoft.com/en-us/solutions/confidential-compute/ |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- Other frameworks: MITRE ATLAS AML.T0024 – TRIPS Agreement Art. 39 – EU Trade Secrets Directive

---

### DSGAI10 – Synthetic Data Generation Risk

**Severity:** Medium

Synthetic data generated for AI training may inherit biases from source
data, fail to provide meaningful privacy guarantees, or introduce artefacts
that degrade model performance. SP 800-218A addresses this through output
quality review (PW.7), adversarial testing of synthetic data fidelity
(PW.8), and root cause analysis when synthetic data causes model failures
(RV.3).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Review for security vulnerabilities — synthetic data quality review | PW.7.2-PS | PW | Review synthetic data for bias inheritance, privacy leakage, and statistical fidelity before use in training pipelines; verify privacy guarantees are meaningful |
| Test for security vulnerabilities — synthetic data adversarial testing | PW.8.2-PS | PW | Conduct adversarial testing of synthetic data for membership inference, attribute inference, and reconstruction attacks to validate privacy claims |
| Analyse root causes — synthetic data failure analysis | RV.3.1-PS | RV | When model failures trace to synthetic training data, conduct root cause analysis of the generation process, source data, and privacy mechanism |

#### Mitigations

**Foundational**
- PW.7.2-PS: Establish quality gates for synthetic data — statistical
  fidelity metrics, bias assessments, and privacy guarantee validation
  must pass before synthetic data enters any training pipeline
- Define a synthetic data governance policy specifying acceptable
  generation methods, required privacy guarantees (e.g. differential
  privacy epsilon thresholds), and mandatory quality assessments
- PW.8.2-PS: Conduct membership inference testing on synthetic datasets
  to validate that individual source records cannot be identified

**Hardening**
- PW.8.2-PS: Test synthetic data for attribute inference and
  reconstruction attacks — verify that sensitive attributes of source
  individuals cannot be inferred from the synthetic output
- PW.7.2-PS: Compare statistical distributions of synthetic data against
  source data to detect bias amplification — reject synthetic datasets
  that amplify protected attribute correlations
- Maintain provenance records linking synthetic datasets to their source
  data, generation model, and privacy parameters

**Advanced**
- RV.3.1-PS: Build automated quality monitoring for synthetic data
  pipelines — continuous assessment of fidelity, utility, and privacy
  metrics with alerting on degradation
- Apply formal privacy guarantees (differential privacy with published
  epsilon) to synthetic data generation; audit that generation
  processes maintain stated guarantees
- PW.8.2-PS: Conduct periodic red team exercises targeting synthetic
  data privacy claims — attempt to reconstruct source data from
  synthetic outputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| SDV (Synthetic Data Vault) | Open-source | https://sdv.dev |
| Gretel.ai | Commercial | https://gretel.ai |
| OpenDP | Open-source | https://opendp.org |
| Anonymeter | Open-source | https://github.com/statice/anonymeter |

#### Cross-references
- LLM Top 10: LLM09 Misinformation, LLM03 Training Data Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST AI RMF Measure 2.11 – Article 29 WP Opinion on Anonymisation – ISO 27559

---

### DSGAI11 – Data Retention & Deletion

**Severity:** High

AI systems complicate data retention and deletion because training data is
encoded into model weights, cached in embedding stores, and replicated across
pipeline stages. Traditional deletion does not guarantee data removal from
trained models. SP 800-218A addresses this through retention requirements
(PW.1), versioned artefact management enabling selective rollback (PS.3), and
remediation procedures for deletion requests (RV.2).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — data retention and deletion policies | PW.1.1-PS | PW | Define security requirements governing data retention periods, deletion procedures, and right-to-erasure compliance for all data in AI pipelines |
| Archive and protect software releases — retention-aware artefact management | PS.3.1-PS | PS | Maintain versioned data and model artefacts with retention metadata; enable selective data removal and model retraining on deletion requests |
| Assess, prioritise, and remediate — deletion request remediation | RV.2.1-PS | RV | Define procedures to assess and remediate data deletion requests including impact analysis on trained models and retraining requirements |

#### Mitigations

**Foundational**
- PW.1.1-PS: Define data retention policies for every AI data asset class
  — training data, fine-tuning data, inference logs, embeddings, and model
  checkpoints; align with regulatory requirements (GDPR Art. 17, CCPA)
- PS.3.1-PS: Implement retention metadata on all data and model artefacts;
  enable automated identification of artefacts containing data subject to
  deletion requests
- Document which models were trained on which data versions — enable
  impact analysis when deletion requests are received

**Hardening**
- RV.2.1-PS: Establish a deletion request processing workflow that
  includes: data identification, model impact assessment, data removal
  from all pipeline stages, and model retraining scheduling
- PS.3.1-PS: Implement automated retention enforcement — artefacts
  exceeding retention periods are flagged for review and deletion;
  dependent models are identified for retraining
- Deploy machine unlearning techniques where full retraining is
  infeasible — validate that unlearning effectively removes the
  influence of deleted data

**Advanced**
- PW.1.1-PS: Implement data lifecycle management that tracks every
  data record from ingestion through model training to model retirement;
  enable complete audit trail for regulatory response
- RV.2.1-PS: Build automated deletion impact analysis — on receiving
  a deletion request, automatically identify all affected datasets,
  embeddings, models, and downstream consumers
- Research and deploy certified machine unlearning with verifiable
  guarantees that deleted data cannot be extracted from retrained models

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| Immuta | Commercial | https://www.immuta.com |
| OneTrust | Commercial | https://www.onetrust.com |
| DVC (Data Version Control) | Open-source | https://dvc.org |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM08 Vector and Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: GDPR Art. 17 – CCPA Sec. 1798.105 – NIST Privacy Framework CT.DP-P

---

### DSGAI12 – Data Ownership & Monetisation

**Severity:** Medium

Ambiguity around data ownership in AI pipelines — particularly when
training data includes user-contributed content, licensed datasets, or
outputs from other AI models — creates legal, ethical, and commercial
risk. SP 800-218A addresses this through security requirements that govern
data rights (PW.1) and access controls that enforce ownership boundaries
(PS.1).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — data ownership and rights management | PW.1.1-PS | PW | Define security requirements that establish clear data ownership, licensing terms, and permitted use for all datasets in AI pipelines |
| Protect all code from unauthorised access — ownership-based access controls | PS.1.1-PS | PS | Implement access controls that enforce data ownership boundaries; prevent use of datasets outside their licensed scope or ownership agreement |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish a data ownership registry for all AI datasets —
  document the owner, licensing terms, permitted use cases, and
  restrictions for every dataset entering an AI pipeline
- PS.1.1-PS: Implement access controls that enforce ownership-based
  restrictions — prevent teams from using datasets outside their
  licensed scope; log all access for audit
- Include data ownership and licensing review as a mandatory step in
  the data ingestion approval process

**Hardening**
- PW.1.1-PS: Implement automated licence compliance checking — validate
  that dataset usage in training, fine-tuning, and evaluation complies
  with licence terms before pipeline execution
- PS.1.1-PS: Deploy technical controls that prevent unauthorised
  redistribution or monetisation of datasets — DRM, access expiry,
  and usage metering for licensed content
- Maintain records of all datasets used to train each model version
  to enable licence compliance auditing

**Advanced**
- PW.1.1-PS: Implement data contribution tracking for AI outputs —
  attribute model capabilities to contributing datasets to support
  fair revenue sharing and licence compliance
- PS.1.1-PS: Deploy blockchain or cryptographic audit trails for
  high-value data licensing transactions — tamper-evident records of
  data usage and monetisation
- Conduct periodic data rights audits — verify all datasets in
  production pipelines have current, valid licensing and ownership
  documentation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Collibra | Commercial | https://www.collibra.com |
| Alation | Commercial | https://www.alation.com |
| Apache Atlas | Open-source | https://atlas.apache.org |
| CycloneDX | Open-source | https://cyclonedx.org |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities, LLM03 Training Data Poisoning
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- Other frameworks: EU AI Act Art. 10 – Copyright Directive Art. 4 – WIPO AI & IP Policy

---

### DSGAI13 – Data Misuse & Manipulation

**Severity:** High

Data processed by AI systems is used for purposes beyond its intended scope
or is manipulated to influence model behaviour — including repurposing
user data for training without consent, manipulating input data to skew
outputs, or weaponising data access for competitive advantage. SP 800-218A
addresses this through purpose limitation requirements (PW.1), output review
for misuse indicators (PW.7), and monitoring for data misuse in production
(RV.1).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — purpose limitation controls | PW.1.1-PS | PW | Define security requirements enforcing data purpose limitation — each dataset must have documented permitted uses and technical controls preventing unauthorised repurposing |
| Review for security vulnerabilities — misuse and manipulation detection | PW.7.2-PS | PW | Include data misuse and manipulation scenarios in pre-release reviews; verify that purpose limitation controls are enforced and cannot be bypassed |
| Identify and confirm vulnerabilities — production misuse monitoring | RV.1.1-PS | RV | Establish procedures to detect data misuse and manipulation in production including monitoring for purpose-scope violations and data manipulation patterns |

#### Mitigations

**Foundational**
- PW.1.1-PS: Document permitted use cases for every dataset in AI
  pipelines; implement technical controls that enforce purpose limitation
  — prevent datasets from being used in pipelines they were not
  approved for
- PW.7.2-PS: Include data misuse scenarios in pre-release security
  reviews — verify that purpose limitation controls are in place and
  effective for every data source
- Define a data misuse policy that specifies consequences for
  unauthorised data repurposing; enforce through access controls and
  monitoring

**Hardening**
- RV.1.1-PS: Deploy monitoring for data purpose-scope violations —
  detect when datasets are accessed by pipelines or users outside their
  approved scope; alert and escalate
- PW.1.1-PS: Implement technical purpose binding on datasets — metadata
  tags that are validated by pipeline orchestration tools before data
  access is permitted
- PW.7.2-PS: Conduct periodic reviews of actual data usage against
  approved purpose — identify and remediate scope creep

**Advanced**
- RV.1.1-PS: Build automated purpose compliance monitoring that
  continuously validates data usage against declared purposes across
  all AI pipelines
- PW.1.1-PS: Implement cryptographic purpose binding — data can only
  be decrypted by authorised pipelines using purpose-specific keys
- Conduct adversarial data manipulation testing — verify that input
  data manipulation cannot skew model outputs in ways that benefit
  the manipulator

#### Tools

| Tool | Type | Link |
|---|---|---|
| Immuta | Commercial | https://www.immuta.com |
| Privacera | Commercial | https://privacera.com |
| Apache Ranger | Open-source | https://ranger.apache.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency, LLM03 Training Data Poisoning
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- Other frameworks: GDPR Art. 5(1)(b) – NIST Privacy Framework CT.PO-P – ISO 27701 A.7.2.2

---

### DSGAI14 – Consent Management Failures

**Severity:** High

AI systems that process personal data without proper consent, or that fail
to honour consent withdrawal, violate data protection regulations and erode
user trust. SP 800-218A addresses this through security requirements that
mandate consent-aware data processing (PW.1) and design practices requiring
consent enforcement mechanisms (PW.2).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — consent management requirements | PW.1.1-PS | PW | Define security requirements mandating consent verification before personal data enters AI training, fine-tuning, or inference pipelines |
| Design software — consent enforcement architecture | PW.2.1-PS | PW | Design AI systems with consent enforcement mechanisms that validate consent status before data processing and honour consent withdrawal across all pipeline stages |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish consent management requirements for all AI
  systems that process personal data — document the legal basis for
  processing, consent scope, and withdrawal procedures for each data
  subject category
- PW.2.1-PS: Design consent enforcement into AI pipeline architecture
  — consent status must be checked before data enters training,
  fine-tuning, or inference; withdrawal must propagate to all pipeline
  stages
- Maintain a consent registry that maps data subjects to their consent
  status and scope across all AI systems

**Hardening**
- PW.1.1-PS: Implement automated consent verification at pipeline
  ingestion points — reject data from subjects who have not consented
  or have withdrawn consent
- PW.2.1-PS: Design consent withdrawal propagation — when consent is
  withdrawn, automatically identify and flag all affected datasets,
  embeddings, and models for remediation
- Conduct periodic consent compliance audits — verify that all
  personal data in AI pipelines has valid, current consent

**Advanced**
- PW.2.1-PS: Implement granular consent management supporting
  per-purpose consent — data subjects can consent to inference but
  not training, or to specific model types
- PW.1.1-PS: Deploy consent-aware machine unlearning — when consent
  is withdrawn, automatically initiate data removal and model
  retraining workflows
- Build real-time consent dashboards enabling data subjects to view
  and manage their consent across all AI systems

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| Transcend | Commercial | https://transcend.io |
| CookieYes | Open-source | https://www.cookieyes.com |
| Osano | Commercial | https://www.osano.com |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM06 Excessive Agency
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- Other frameworks: GDPR Art. 6–7 – CCPA Sec. 1798.120 – NIST Privacy Framework CT.PO-P

---

### DSGAI15 – Data Minimisation Violations

**Severity:** Medium

AI systems that collect, store, or process more data than necessary for
their stated purpose increase attack surface, privacy risk, and regulatory
exposure. SP 800-218A addresses this through security requirements enforcing
data minimisation (PW.1) and design practices that embed minimisation
principles into pipeline architecture (PW.2).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — data minimisation requirements | PW.1.1-PS | PW | Define security requirements enforcing data minimisation — AI systems must collect and process only the data necessary for their documented purpose |
| Design software — minimisation-by-design | PW.2.1-PS | PW | Design AI data pipelines with data minimisation controls built in; implement field-level filtering, aggregation, and anonymisation at ingestion |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish data minimisation requirements for all AI systems
  — document the minimum data needed for each pipeline stage; prohibit
  collection or retention of data not justified by a documented purpose
- PW.2.1-PS: Design data ingestion pipelines to collect only required
  fields — implement field-level filtering at ingestion; strip
  unnecessary attributes before data enters training or inference
  pipelines
- Conduct data necessity reviews as part of the AI system design
  process — challenge every data field for necessity

**Hardening**
- PW.1.1-PS: Implement automated data minimisation enforcement —
  pipeline validation that rejects datasets containing fields not
  listed in the approved data schema for that pipeline
- PW.2.1-PS: Apply privacy-enhancing technologies at ingestion —
  anonymisation, pseudonymisation, or aggregation of personal data
  before it enters training pipelines
- Conduct periodic data minimisation audits — verify that production
  AI pipelines are not processing data beyond their documented scope

**Advanced**
- PW.2.1-PS: Implement dynamic data minimisation — adapt the data
  collected based on the specific task, providing only the minimum
  context needed for each inference request
- PW.1.1-PS: Build data necessity scoring that quantifies the
  contribution of each data field to model performance — remove
  low-contribution fields that add privacy risk without meaningful
  utility
- Deploy feature importance analysis to guide minimisation decisions;
  remove features that contribute negligible predictive value

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| ARX Data Anonymization | Open-source | https://arx.deidentifier.org |
| Amnesia | Open-source | https://amnesia.openaire.eu |
| Google Differential Privacy | Open-source | https://github.com/google/differential-privacy |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses, LLM06 Excessive Agency
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: GDPR Art. 5(1)(c) – NIST Privacy Framework CT.DM-P – ISO 27701 A.7.4.1

---

### DSGAI16 – Erosion of Privacy

**Severity:** High

AI systems progressively erode individual privacy through inference of
sensitive attributes, behavioural profiling, cross-context tracking, and
training data memorisation — even when individual data points appear
non-sensitive. SP 800-218A addresses this through privacy-aware security
requirements (PW.1), privacy-preserving design (PW.2), and access controls
that prevent privacy-eroding data combinations (PS.1).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — privacy preservation requirements | PW.1.1-PS | PW | Define security requirements that mandate privacy impact assessments, privacy-preserving techniques, and limits on inference of sensitive attributes for all AI systems |
| Design software — privacy-preserving AI architecture | PW.2.1-PS | PW | Design AI systems with privacy preservation as a core architectural principle; embed differential privacy, federated learning, or secure computation where appropriate |
| Protect all code from unauthorised access — privacy boundary enforcement | PS.1.1-PS | PS | Implement access controls that prevent cross-context data combination enabling re-identification or sensitive attribute inference |

#### Mitigations

**Foundational**
- PW.1.1-PS: Require privacy impact assessments (PIAs) for all AI systems
  before deployment — assess risks of attribute inference, profiling, and
  memorisation; document mitigations
- PW.2.1-PS: Design AI systems to limit inference of sensitive attributes
  — apply output filtering, response rounding, and attribute suppression
  to prevent privacy-eroding inferences
- PS.1.1-PS: Implement data compartmentalisation — prevent combination
  of data from different contexts that could enable re-identification
  or profiling

**Hardening**
- PW.1.1-PS: Implement ongoing privacy risk monitoring — measure and
  track privacy degradation metrics across model versions and deployment
  contexts
- PW.2.1-PS: Deploy differential privacy in training and inference where
  personal data is processed; publish and track privacy budgets (epsilon)
  per data subject population
- PS.1.1-PS: Apply technical controls preventing cross-context data
  linkage — separate storage, separate access credentials, and
  purpose-bound encryption keys

**Advanced**
- PW.2.1-PS: Implement federated learning or secure multi-party
  computation for scenarios where centralised data processing poses
  unacceptable privacy risk
- PW.1.1-PS: Conduct privacy red team exercises — test whether AI
  systems can be used to infer protected attributes, reconstruct
  individual records, or build behavioural profiles
- Deploy formal privacy guarantees with published, auditable privacy
  parameters for all AI systems processing personal data

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://opendp.org |
| PySyft | Open-source | https://github.com/OpenMined/PySyft |
| TensorFlow Privacy | Open-source | https://github.com/tensorflow/privacy |
| Flower (Federated Learning) | Open-source | https://flower.ai |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses, LLM01 Prompt Injection
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- Other frameworks: GDPR Art. 25 – NIST Privacy Framework – EU AI Act Art. 10 – ISO 27701

---

### DSGAI17 – Bias in Data

**Severity:** High

Biased training data produces discriminatory model outputs affecting
protected groups — manifesting as unfair lending decisions, biased hiring
recommendations, discriminatory content moderation, or inequitable service
delivery. SP 800-218A addresses this through output review for bias and
fairness (PW.7), adversarial testing for discriminatory behaviour (PW.8),
and root cause analysis tracing bias to data sources (RV.3).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Review for security vulnerabilities — bias and fairness review | PW.7.2-PS | PW | Include bias, fairness, and discrimination testing in pre-release model behaviour reviews; assess model outputs across protected attributes and demographic groups |
| Test for security vulnerabilities — adversarial fairness testing | PW.8.2-PS | PW | Conduct adversarial testing for discriminatory outputs; test model behaviour across demographic groups, intersectional categories, and edge cases |
| Analyse root causes — bias source tracing | RV.3.1-PS | RV | When discriminatory behaviour is identified, conduct root cause analysis tracing bias to specific training data sources, labelling processes, or preprocessing steps |

#### Mitigations

**Foundational**
- PW.7.2-PS: Establish fairness metrics and thresholds for all AI systems
  — demographic parity, equalised odds, or calibration metrics appropriate
  to the deployment context; evaluate before each release
- PW.8.2-PS: Include bias testing in pre-release adversarial testing —
  test model outputs across protected attributes and intersectional
  categories; gate promotion on fairness threshold compliance
- Document the demographic composition and representativeness of
  training data for every model version; assess for known gaps

**Hardening**
- RV.3.1-PS: Establish bias root cause analysis procedures — when
  discriminatory behaviour is detected, trace to specific data sources,
  labelling processes, or preprocessing decisions and remediate
- PW.7.2-PS: Deploy continuous fairness monitoring in production —
  track fairness metrics across demographic groups in live traffic;
  alert on degradation
- Implement bias mitigation techniques in training — resampling,
  reweighting, or adversarial debiasing appropriate to the identified
  bias pattern

**Advanced**
- PW.8.2-PS: Conduct intersectional fairness testing covering
  combinations of protected attributes — bias may be invisible at the
  single-attribute level but significant at intersections
- RV.3.1-PS: Build automated bias regression testing — continuous
  evaluation of fairness metrics across model versions to detect bias
  introduction or amplification in the development lifecycle
- Deploy model cards with mandatory fairness reporting for all
  production AI systems — publish evaluation results and known
  limitations

#### Tools

| Tool | Type | Link |
|---|---|---|
| Fairlearn | Open-source | https://fairlearn.org |
| AI Fairness 360 | Open-source | https://aif360.mybluemix.net |
| What-If Tool | Open-source | https://pair-code.github.io/what-if-tool |
| Aequitas | Open-source | https://github.com/dssg/aequitas |

#### Cross-references
- LLM Top 10: LLM09 Misinformation, LLM03 Training Data Poisoning
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- Other frameworks: NIST AI RMF Measure 2.11 – EU AI Act Art. 10 – ISO 42001 A.7.4 – EEOC AI Guidance

---

### DSGAI18 – Governance Gaps

**Severity:** High

Absence of comprehensive data governance frameworks for AI systems leads to
inconsistent data handling, unclear accountability, and inability to enforce
policies across the AI lifecycle. SP 800-218A addresses this through
security requirements that mandate governance structures (PW.1), design
practices requiring governance integration (PW.2), and root cause analysis
that identifies governance failures (RV.3).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — AI data governance requirements | PW.1.1-PS | PW | Define security requirements mandating AI-specific data governance including data stewardship, accountability structures, and policy enforcement mechanisms |
| Design software — governance-integrated AI architecture | PW.2.1-PS | PW | Design AI systems with governance controls integrated into pipeline architecture; embed policy enforcement, approval workflows, and audit capabilities |
| Analyse root causes — governance failure analysis | RV.3.1-PS | RV | When data governance failures contribute to AI incidents, conduct root cause analysis to identify governance gaps and strengthen frameworks |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish an AI data governance framework defining roles
  (data stewards, data owners, AI system owners), responsibilities,
  and accountability for all data in AI pipelines
- PW.2.1-PS: Integrate governance controls into AI pipeline design —
  approval workflows for data ingestion, model training, and deployment;
  policy-as-code enforcement at pipeline gates
- Define data governance policies covering classification, access,
  retention, quality, and compliance for all AI data assets

**Hardening**
- PW.1.1-PS: Implement policy-as-code governance — encode data governance
  policies in machine-executable form; enforce automatically at pipeline
  execution time
- PW.2.1-PS: Deploy governance dashboards providing real-time visibility
  into policy compliance across all AI systems — track violations,
  exceptions, and remediation status
- RV.3.1-PS: Include governance gap analysis in all AI incident post-mortems
  — identify whether governance failures contributed to the incident and
  strengthen accordingly

**Advanced**
- PW.1.1-PS: Implement continuous governance compliance monitoring —
  automated assessment of all AI pipelines against governance policies
  with alerting on non-compliance
- PW.2.1-PS: Build governance maturity scoring for AI systems — assess
  each system against governance maturity criteria and prioritise
  improvement based on risk
- RV.3.1-PS: Conduct periodic governance effectiveness reviews — assess
  whether governance frameworks are achieving their objectives and
  adapt based on incident trends

#### Tools

| Tool | Type | Link |
|---|---|---|
| Collibra | Commercial | https://www.collibra.com |
| Atlan | Commercial | https://atlan.com |
| Apache Atlas | Open-source | https://atlas.apache.org |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities, ASI09 Human-Agent Trust Exploitation
- Other frameworks: NIST AI RMF Govern – ISO 42001 5.1 – EU AI Act Art. 9 – OECD AI Principles

---

### DSGAI19 – Third-Party Data Risk

**Severity:** High

AI systems relying on third-party data sources, APIs, and pre-trained
components inherit the security and quality risks of those external
dependencies. Compromised or low-quality third-party data can poison
models, violate compliance obligations, or introduce supply chain
vulnerabilities. SP 800-218A addresses this through third-party component
vetting (PW.4), integrity verification (PS.2), and monitoring for
third-party vulnerability disclosures (RV.1).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Reuse existing well-secured software — third-party data vetting | PW.4.1-PS | PW | Vet all third-party data sources, APIs, and pre-trained components for security, quality, compliance, and provenance before use in AI pipelines |
| Verify software integrity — third-party data integrity | PS.2.1-PS | PS | Verify integrity of all third-party data deliveries using checksums, signatures, or schema validation; detect tampering or corruption before pipeline ingestion |
| Identify and confirm vulnerabilities — third-party monitoring | RV.1.1-PS | RV | Monitor for security advisories and quality issues from third-party data providers; establish triage procedures for third-party data incidents |

#### Mitigations

**Foundational**
- PW.4.1-PS: Establish a third-party data approval process — all external
  data sources must pass security review, quality assessment, compliance
  verification, and provenance documentation before entering any pipeline
- PS.2.1-PS: Verify integrity of every third-party data delivery —
  validate checksums, schemas, and statistical profiles against expected
  baselines; reject deliveries that fail validation
- Maintain a third-party data inventory documenting all external data
  dependencies, their providers, and the AI systems that consume them

**Hardening**
- RV.1.1-PS: Subscribe to third-party provider security advisories
  and data quality notifications; define triage SLAs for third-party
  data incidents
- PW.4.1-PS: Conduct periodic re-assessment of third-party data
  providers — verify that security, quality, and compliance posture
  remains acceptable; include in vendor risk management programme
- PS.2.1-PS: Implement automated third-party data quality monitoring
  — continuous profiling of incoming data feeds with alerting on
  quality degradation or unexpected changes

**Advanced**
- PW.4.1-PS: Implement data sandboxing for new third-party data sources
  — isolate and evaluate in a non-production environment before
  integration into production pipelines
- RV.1.1-PS: Build automated third-party risk scoring that continuously
  evaluates provider risk based on incident history, compliance status,
  and data quality trends
- PS.2.1-PS: Deploy supply chain integrity verification (SLSA or
  equivalent) for critical third-party data dependencies

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| CycloneDX | Open-source | https://cyclonedx.org |
| Sigstore | Open-source | https://www.sigstore.dev |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities, LLM03 Training Data Poisoning
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities, ASI10 AI Agent Dependency Failures
- Other frameworks: SSDF PW.4 – NIST CSF 2.0 ID.SC – ISO 27036 – MITRE ATLAS AML.T0056

---

### DSGAI20 – Data Localization Violations

**Severity:** High

AI systems that process, store, or transfer data across jurisdictional
boundaries without complying with data localization requirements violate
sovereignty laws and regulatory mandates. Cloud-based AI training, global
model serving, and cross-border data pipelines create complex localization
challenges. SP 800-218A addresses this through localization requirements
(PW.1), access controls enforcing jurisdictional boundaries (PS.1), and
versioned artefact management with jurisdiction metadata (PS.3).

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — data localization requirements | PW.1.1-PS | PW | Define security requirements mandating compliance with data localization laws for all AI pipeline data; document jurisdictional restrictions for each dataset |
| Protect all code from unauthorised access — jurisdictional access controls | PS.1.1-PS | PS | Implement access controls that enforce data localization boundaries; prevent data transfer or processing outside authorised jurisdictions |
| Archive and protect software releases — jurisdiction-aware artefact management | PS.3.1-PS | PS | Maintain jurisdiction metadata on all data and model artefacts; enable verification that training and serving comply with localization requirements |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish data localization requirements for every AI dataset
  — document the jurisdictional restrictions, applicable regulations
  (GDPR, China PIPL, India DPDP, etc.), and compliant processing locations
  for each data category
- PS.1.1-PS: Implement technical controls preventing cross-border data
  transfer outside authorised jurisdictions — geofencing, region-locked
  storage, and transfer controls on AI pipeline data
- Map all AI data flows against localization requirements — identify
  where data is stored, processed, and transferred for every pipeline

**Hardening**
- PS.3.1-PS: Maintain jurisdiction metadata on all data and model
  artefacts; verify localization compliance at every pipeline stage
  transition before execution
- PS.1.1-PS: Deploy network-level controls preventing data egress to
  non-compliant regions — enforce at infrastructure layer, not relying
  solely on application controls
- PW.1.1-PS: Implement automated localization compliance checking —
  validate that pipeline configurations route data to compliant
  processing locations before execution

**Advanced**
- PW.1.1-PS: Build localization-aware AI pipeline orchestration —
  automatically route data processing to compliant regions based on
  jurisdiction metadata attached to each dataset
- PS.1.1-PS: Deploy confidential computing for scenarios where data
  must be processed in non-ideal jurisdictions — provide technical
  guarantees that host infrastructure cannot access data in use
- Implement data residency dashboards with real-time visibility into
  where all AI data is stored, processed, and transferred — enable
  continuous localization compliance monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| Azure Policy | Commercial | https://azure.microsoft.com/en-us/products/azure-policy |
| AWS Config | Commercial | https://aws.amazon.com/config/ |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Privacera | Commercial | https://privacera.com |

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage, LLM05 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- Other frameworks: GDPR Ch. V – China PIPL Art. 38 – India DPDP Sec. 16 – NIST Privacy Framework

---

### DSGAI21 – Non-Compliance with Data Laws

**Severity:** Critical

AI systems that fail to comply with applicable data protection, privacy,
and AI-specific regulations expose organisations to enforcement actions,
fines, and reputational damage. The rapidly evolving regulatory landscape
spanning GDPR, CCPA, EU AI Act, and sector-specific rules creates complex
compliance obligations for AI systems. SP 800-218A addresses this through
compliance-aware security requirements (PW.1), design practices that embed
regulatory compliance (PW.2), and root cause analysis for compliance
failures (RV.3).

**Real-world references:**
- Italian Garante ChatGPT ban (2023) — temporary ban for GDPR
  non-compliance regarding training data processing
- EU AI Act (2024) — comprehensive AI regulation with obligations for
  training data governance, transparency, and human oversight

#### SP 800-218A mapping

| Practice | ID | Group | Description |
|---|---|---|---|
| Define security requirements — regulatory compliance requirements | PW.1.1-PS | PW | Define security requirements that mandate compliance with all applicable data protection, privacy, and AI-specific regulations for each AI system deployment |
| Design software — compliance-by-design | PW.2.1-PS | PW | Design AI systems with regulatory compliance built into architecture; embed compliance controls, audit capabilities, and regulatory reporting into pipeline design |
| Analyse root causes — compliance failure analysis | RV.3.1-PS | RV | When regulatory non-compliance is identified, conduct root cause analysis to determine the gap, affected data subjects, and required remediation |

#### Mitigations

**Foundational**
- PW.1.1-PS: Establish a regulatory compliance registry for all AI systems
  — document applicable regulations (GDPR, CCPA, EU AI Act, sector
  rules), compliance obligations, and responsible officers for each
  system
- PW.2.1-PS: Design compliance controls into AI pipeline architecture —
  consent verification, purpose limitation, data minimisation, and
  transparency mechanisms built in from the start, not bolted on
- Conduct regulatory compliance assessments before deploying any AI
  system that processes personal data or falls under AI-specific
  regulation

**Hardening**
- PW.1.1-PS: Implement automated regulatory compliance monitoring —
  continuous assessment of AI systems against applicable regulations
  with alerting on compliance gaps
- PW.2.1-PS: Deploy compliance-as-code — encode regulatory requirements
  in machine-executable policies enforced at pipeline execution time;
  block non-compliant data processing automatically
- RV.3.1-PS: Include compliance gap analysis in all AI incident
  post-mortems — determine whether regulatory violations occurred and
  initiate mandatory notification procedures

**Advanced**
- PW.2.1-PS: Build regulatory change monitoring — track evolving
  regulations across all relevant jurisdictions; automatically assess
  impact on existing AI systems and flag required updates
- PW.1.1-PS: Implement comprehensive compliance documentation
  generation — automated production of Data Protection Impact
  Assessments, model cards, and regulatory filings from pipeline
  metadata
- RV.3.1-PS: Establish a regulatory response team with defined
  procedures for managing regulatory inquiries, enforcement actions,
  and mandatory breach notifications related to AI systems

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| TrustArc | Commercial | https://trustarc.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Transcend | Commercial | https://transcend.io |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency, LLM07 System Prompt Leakage
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- Other frameworks: GDPR – CCPA – EU AI Act – NIST AI RMF Govern 1.1 – ISO 42001 4.1

---

## Implementation priority

| Phase | PW – Produce | PS – Protect | RV – Respond |
|---|---|---|---|
| 1 – Now | PW.1.1-PS governance and compliance requirements for DSGAI18/21; PW.2.1-PS data visibility for DSGAI02 | PS.1.1-PS access controls and logging for DSGAI01/08; data exfiltration prevention | RV.1.1-PS monitoring for DSGAI03 shadow AI and DSGAI13 data misuse |
| 2 – This sprint | PW.4.1-PS third-party data vetting for DSGAI04/05/19; PW.5.1-PS secure data handling for DSGAI08 | PS.2.1-PS integrity verification for DSGAI05/19; PS.3.1-PS versioned artefact management for DSGAI04/09 | RV.2.1-PS deletion request procedures for DSGAI11; triage SLAs for third-party incidents |
| 3 – This quarter | PW.7.2-PS bias and fairness reviews for DSGAI17; PW.2.1-PS consent and minimisation design for DSGAI14/15 | PS.1.1-PS localization controls for DSGAI20; PS.3.1-PS lineage tracking for DSGAI06 | RV.3.1-PS root cause playbooks for DSGAI04/17/21; compliance failure analysis |
| 4 – Ongoing | PW.8.2-PS adversarial testing for DSGAI10/17; privacy red team programme; regulatory change monitoring | Supply chain integrity monitoring; data provenance verification; cross-border compliance monitoring | Production compliance monitoring; governance effectiveness reviews; incident response exercises |

---

## References

- [NIST SP 800-218A (Initial Public Draft, March 2024)](https://doi.org/10.6028/NIST.SP.800-218A.ipd)
- [NIST SSDF (SP 800-218)](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/dsgai-2026/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [MITRE ATLAS](https://atlas.mitre.org)
- [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – DSGAI01–DSGAI21 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
