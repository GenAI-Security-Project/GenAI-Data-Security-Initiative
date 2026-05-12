<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : DORA – Digital Operational Resilience Act (EU Regulation 2022/2554)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 – DORA

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [Digital Operational Resilience Act (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
(EU Regulation 2022/2554, effective 17 January 2025).

DORA establishes a binding regulatory framework for digital operational
resilience across the EU financial sector. It mandates comprehensive ICT
risk management, incident reporting, resilience testing, and third-party
risk oversight. For financial entities deploying LLM-based AI systems,
DORA requires that AI-specific risks — including adversarial attacks, model
failures, data poisoning, and vendor dependency — are integrated into the
ICT risk management framework, incident management processes, resilience
testing programmes, and third-party oversight arrangements. This mapping
enables financial institutions to trace each OWASP LLM Top 10 risk to
specific DORA articles and implement controls that satisfy regulatory
obligations.

---

## DORA article groups

| Group | Articles | Purpose |
|---|---|---|
| ICT Risk Management | Art. 5–7 | Governance framework, risk management strategy, policies and procedures for ICT including AI systems |
| Identification | Art. 8 | Identification and classification of ICT assets including AI models, datasets, and inference infrastructure |
| Protection and Prevention | Art. 9 | Security controls for ICT systems including AI-specific protections against adversarial attacks |
| Detection | Art. 10 | Anomaly detection, monitoring, and alerting for ICT systems including AI behaviour monitoring |
| Response and Recovery | Art. 11 | Incident response, business continuity, and recovery procedures for AI service disruptions |
| Backup Policies | Art. 12 | Backup and restoration of ICT systems including model checkpoints and training data |
| Learning and Evolving | Art. 13 | Post-incident analysis, lessons learned, and continuous improvement for AI incidents |
| ICT Incident Management | Art. 17–23 | Incident classification, reporting to regulators, and communication for AI-related incidents |
| Resilience Testing | Art. 24–27 | Penetration testing, red-teaming, and resilience testing including AI adversarial testing |
| Third-Party Risk | Art. 28–44 | Oversight of third-party ICT service providers including AI model providers and data vendors |
| Information Sharing | Art. 45 | Threat intelligence sharing arrangements including AI-specific threat intelligence |

---

## Quick-reference summary

| ID | Name | Severity | DORA Articles | Scope |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | Art. 9, Art. 24–27, Art. 10 | Both |
| LLM02 | Sensitive Information Disclosure | High | Art. 9, Art. 17–23, Art. 5–7 | Both |
| LLM03 | Training Data Poisoning | Critical | Art. 28–44, Art. 9, Art. 8 | Both |
| LLM04 | Model DoS | High | Art. 9, Art. 10, Art. 12 | Both |
| LLM05 | Supply Chain Vulnerabilities | High | Art. 28–44, Art. 8, Art. 5–7 | Both |
| LLM06 | Excessive Agency | High | Art. 5–7, Art. 9, Art. 24–27 | Build |
| LLM07 | System Prompt Leakage | High | Art. 9, Art. 17–23, Art. 13 | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | Art. 9, Art. 24–27 | Build |
| LLM09 | Misinformation | Medium | Art. 10, Art. 5–7, Art. 13 | Both |
| LLM10 | Unbounded Consumption | Medium | Art. 9, Art. 10, Art. 12 | Both |

---

## Audience tags

`developer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `risk-manager`

- **Developer / ML engineer** – Art. 9 and Art. 24–27 entries; protection controls and resilience testing
- **Security engineer** – Art. 9, Art. 10, Art. 17–23 entries; detection, protection, and incident management
- **Risk manager** – Art. 5–7 and Art. 28–44 entries; governance, strategy, and third-party risk
- **Compliance officer** – full file; DORA regulatory traceability and evidence mapping
- **CISO** – Art. 5–7 entries; ICT risk governance and AI strategy

---

## Detailed mappings

---

### LLM01 – Prompt Injection

**Severity:** Critical

Malicious instructions embedded in user inputs or external content manipulate
LLM behaviour, bypassing safety controls and executing unauthorised actions.
DORA requires financial entities to implement protection and prevention
measures against adversarial AI inputs (Art. 9), conduct resilience testing
including AI red-teaming for prompt injection (Art. 24–27), and deploy
detection capabilities to identify injection attempts in real time (Art. 10).

**Real-world references:**
- EchoLeak (2025) – indirect prompt injection turned Microsoft 365 Copilot
  into a silent exfiltration engine via email content
- Samsung source code leak (2023) – proprietary data surfaced through
  manipulated model queries

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — adversarial input controls | Art. 9 | Protection | Implement ICT security controls to detect and block adversarial inputs including direct and indirect prompt injection; treat as a mandatory protection measure |
| Digital Operational Resilience Testing — AI red-teaming | Art. 24–27 | Testing | Include prompt injection scenarios in threat-led penetration testing (TLPT); cover direct, indirect, and multimodal injection vectors targeting financial AI services |
| Detection — injection monitoring | Art. 10 | Detection | Deploy detection mechanisms for prompt injection attempts; monitor inference requests for adversarial patterns and alert security operations |
| Information Sharing — injection threat intelligence | Art. 45 | Sharing | Share prompt injection threat intelligence with sector peers through DORA information sharing arrangements |

#### Mitigations

**Foundational**
- Art. 9: Implement input validation on all LLM-facing endpoints;
  enforce structural separation between system instructions and user
  content; reject inputs matching known injection signatures
- Establish a policy that all LLM inputs from untrusted sources are
  treated as potentially adversarial; document in ICT risk management
  framework per Art. 5–7
- Art. 10: Deploy detection mechanisms for adversarial prompt patterns;
  establish alerting thresholds and escalation procedures

**Hardening**
- Art. 24–27: Include prompt injection in threat-led penetration testing
  scope; cover direct injection, indirect injection via RAG sources,
  jailbreak patterns, and multimodal vectors
- Art. 9: Apply privilege separation; if the model cannot invoke
  destructive actions by design, injection impact is bounded
- Art. 10: Integrate injection detection signals into security monitoring;
  automate session isolation on high-confidence injection indicators

**Advanced**
- Art. 24–27: Extend adversarial testing to cover your specific RAG
  document corpus, tool descriptors, and any document processing
  pipelines handling financial data
- Art. 45: Participate in sector information sharing arrangements to
  exchange prompt injection indicators and attack patterns
- Art. 13: Document injection incidents and lessons learned; update
  protection controls based on post-incident analysis

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| PyRIT | Open-source | https://github.com/Azure/PyRIT |
| DORA RTS/ITS | Reference | https://www.eba.europa.eu/regulation-and-policy/digital-operational-resilience-act-dora |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: MITRE ATLAS AML.T0051 – FedRAMP SI-10 – SP 800-218A PW.2.1-PS

---

### LLM02 – Sensitive Information Disclosure

**Severity:** High

LLMs inadvertently reveal sensitive data — PII, financial records, credentials,
or proprietary content — through model responses. DORA requires financial
entities to implement protection controls preventing data disclosure (Art. 9),
report ICT incidents involving data breaches to regulators (Art. 17–23),
and maintain governance frameworks covering AI data handling (Art. 5–7).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — data disclosure controls | Art. 9 | Protection | Implement ICT security controls to prevent LLM-based disclosure of sensitive financial data, PII, and credentials; include output monitoring and data loss prevention |
| ICT Incident Management — data breach reporting | Art. 17–23 | Incidents | Classify LLM data disclosure events as ICT-related incidents; report to competent authorities per DORA incident classification and reporting requirements |
| ICT Risk Management — AI data governance | Art. 5–7 | Governance | Include AI data handling in ICT risk management framework; define policies for data processed by LLM systems including classification, retention, and access controls |
| Detection — data leakage detection | Art. 10 | Detection | Deploy detection mechanisms for sensitive data in model outputs; monitor for PII, financial data, and credential patterns in inference responses |

#### Mitigations

**Foundational**
- Art. 9: Implement output monitoring to detect sensitive data in model
  responses; deploy data loss prevention controls on all LLM endpoints
  processing financial data
- Art. 5–7: Include AI data handling policies in the ICT risk management
  framework; classify data processed by LLM systems per organisational
  data classification scheme
- Art. 17–23: Define incident classification criteria for LLM data
  disclosure events; establish reporting procedures to competent authorities

**Hardening**
- Art. 9: Conduct data memorisation testing on models before deployment;
  verify that training data — especially financial records and PII —
  cannot be extracted through targeted queries
- Art. 10: Deploy automated detection for sensitive data patterns in
  model outputs; alert and block on detection of financial data, PII,
  or credentials
- Art. 5–7: Define data retention policies for inference logs; ensure
  compliance with financial data handling requirements

**Advanced**
- Apply differential privacy to training pipelines handling financial
  data; measure and track privacy budget
- Art. 17–23: Conduct tabletop exercises for LLM data disclosure
  incidents; test regulatory reporting procedures
- Art. 13: Establish post-incident learning processes for data
  disclosure events; update controls based on root cause analysis

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Nightfall DLP | Commercial | https://www.nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Privilege Escalation
- DSGAI 2026: DSGAI08 Data Leakage & Exposure, DSGAI16 Erosion of Privacy
- Other frameworks: GDPR Art. 33–34 – FedRAMP SC-28 – SP 800-218A PS.1.1-PS

---

### LLM03 – Training Data Poisoning

**Severity:** Critical

Attackers corrupt training data or fine-tuning pipelines to embed backdoors
or bias model behaviour. DORA requires financial entities to manage
third-party ICT service provider risk covering AI model and data providers
(Art. 28–44), implement protection controls for training pipeline integrity
(Art. 9), and maintain asset identification covering AI training data (Art. 8).

**Real-world references:**
- Nightshade (2023) – poison pixels successfully corrupted image generation
  model behaviour at scale
- BadNets (academic) – backdoor triggers embedded through poisoned training
  labels, activating only on specific inputs

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Third-Party Risk — AI data and model provider oversight | Art. 28–44 | Third-Party | Include AI model providers and training data vendors in third-party ICT risk oversight; assess data provenance, integrity, and poisoning risk |
| Protection and Prevention — training pipeline integrity | Art. 9 | Protection | Implement security controls protecting training data pipelines from unauthorised modification, poisoned data injection, and backdoor embedding |
| Identification — AI training data assets | Art. 8 | Identification | Identify and classify all AI training datasets, fine-tuning data, and model weights as ICT assets in the asset inventory |
| Learning and Evolving — poisoning post-mortem | Art. 13 | Learning | Conduct post-incident analysis for data poisoning events; identify root cause, trace poisoned records, and update protection controls |

#### Mitigations

**Foundational**
- Art. 28–44: Include AI model providers and training data vendors in
  third-party risk assessments; evaluate data provenance, integrity
  controls, and poisoning detection capabilities
- Art. 9: Implement access controls on all training data repositories;
  enforce least privilege; log all training data modifications
- Art. 8: Register all AI training datasets, model weights, and
  fine-tuning data in the ICT asset inventory

**Hardening**
- Art. 9: Apply anomaly detection to training data before each training
  run; flag statistical outliers and content inconsistent with the
  source domain
- Art. 28–44: Require contractual commitments from AI data providers
  covering data integrity, provenance documentation, and incident
  notification for supply chain compromises
- Art. 8: Maintain versioned training data snapshots with integrity
  verification; enable rollback to pre-poisoning states

**Advanced**
- Apply differential privacy during training to bound the influence of
  any single training example
- Art. 28–44: Conduct on-site assessments of critical AI model providers;
  verify their training data integrity controls
- Art. 13: Establish training data forensics playbook; procedures for
  isolating poisoned records and determining impact on model weights

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI05 Data Integrity & Validation Failures
- Other frameworks: MITRE ATLAS AML.T0032 – FedRAMP SR-2 – SP 800-218A PS.1.1-PS

---

### LLM04 – Model DoS

**Severity:** High

Adversarial inputs trigger disproportionate compute, memory, or token
consumption causing denial of service or runaway inference cost. DORA
requires financial entities to implement protection controls for service
availability (Art. 9), deploy detection for consumption anomalies (Art. 10),
and maintain backup and recovery policies for AI services (Art. 12).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — availability controls | Art. 9 | Protection | Implement rate limiting, token quotas, and cost circuit breakers on AI inference services to prevent resource exhaustion and denial of service |
| Detection — consumption anomaly detection | Art. 10 | Detection | Monitor AI inference services for resource consumption anomalies; alert on token spikes, latency degradation, and cost overruns |
| Backup Policies — AI service continuity | Art. 12 | Backup | Maintain backup model deployments, checkpoint restoration capability, and fallback inference paths for AI services supporting critical financial functions |
| Response and Recovery — DoS incident response | Art. 11 | Recovery | Define response and recovery procedures for AI denial of service events; include automated throttling, failover, and service restoration |

#### Mitigations

**Foundational**
- Art. 9: Implement rate limiting and token quotas at the API gateway;
  define per-user, per-session, and per-service consumption limits
- Art. 10: Monitor AI inference resource consumption in real time;
  establish baseline usage patterns and alert on deviations
- Art. 12: Maintain backup model deployments for critical financial
  AI services; document restoration procedures

**Hardening**
- Art. 9: Deploy cost circuit breakers that automatically suspend
  service on threshold breach; per-tenant budgets with automatic
  suspension
- Art. 11: Define and test automated response to consumption incidents;
  include failover to backup deployments and throttle activation
- Art. 10: Include sponge example attacks and token amplification in
  detection scenarios; test detection capabilities regularly

**Advanced**
- Conduct adversarial cost-maximisation testing to identify maximum-cost
  input patterns; apply additional controls at those paths
- Art. 12: Include AI services in business continuity testing; verify
  backup deployment can handle production load
- Art. 11: Document AI service RTO and RPO per DORA requirements;
  test recovery procedures quarterly

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Locust | Open-source | https://locust.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 – FedRAMP SC-7 – SP 800-218A PW.2.1-PS

---

### LLM05 – Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets, libraries,
and plugins — any of which can be compromised. DORA requires financial
entities to manage third-party ICT service provider risk including AI
vendors (Art. 28–44), identify and classify all AI supply chain components
(Art. 8), and maintain governance covering AI supply chain risk (Art. 5–7).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Third-Party Risk — AI vendor oversight | Art. 28–44 | Third-Party | Include AI model providers, dataset vendors, and ML library maintainers in third-party ICT risk management; conduct due diligence, contractual oversight, and ongoing monitoring |
| Identification — AI supply chain assets | Art. 8 | Identification | Identify and classify all AI supply chain components — models, datasets, adapters, libraries, plugins — in the ICT asset inventory with provenance records |
| ICT Risk Management — AI supply chain governance | Art. 5–7 | Governance | Include AI supply chain risk in the ICT risk management framework; define policies for AI component sourcing, vetting, and lifecycle management |
| Resilience Testing — supply chain resilience | Art. 24–27 | Testing | Include AI supply chain disruption scenarios in resilience testing; test fallback procedures for third-party AI service failures |

#### Mitigations

**Foundational**
- Art. 28–44: Include all AI service providers in third-party risk
  assessments per DORA requirements; establish contractual provisions
  covering security, incident notification, and audit rights
- Art. 8: Maintain a complete ML SBOM for every production AI system;
  register all AI components in the ICT asset inventory
- Art. 5–7: Define an approved sources policy for AI components;
  model weights, datasets, and libraries must come from vetted sources

**Hardening**
- Art. 28–44: Require contractual commitments from AI providers covering
  security practices, vulnerability notification, and right to audit;
  identify critical AI providers per DORA criteria
- Art. 8: Implement automated supply chain integrity verification in
  CI/CD; verify cryptographic signatures on all model artefacts
- Art. 24–27: Include AI vendor failure scenarios in resilience testing;
  test failover to alternative providers

**Advanced**
- Art. 28–44: Conduct on-site assessments of critical AI providers;
  assess their security posture, training data practices, and incident
  management capabilities
- Art. 5–7: Include AI supply chain risk in board-level risk reporting;
  monitor concentration risk across AI providers
- Extend ML SBOM to cover runtime dynamic components; track at
  inference time

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |
| Sigstore | Open-source | https://www.sigstore.dev |

#### Cross-references
- Agentic Top 10: ASI04 Supply Chain Compromise, ASI10 AI Agent Dependency Failures
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI19 Third-Party Data Risk
- Other frameworks: MITRE ATLAS AML.T0056 – FedRAMP SR-2 – EBA Outsourcing Guidelines

---

### LLM06 – Excessive Agency

**Severity:** High

LLMs granted excessive autonomy over tools, APIs, and systems execute
unintended or harmful actions when manipulated. DORA requires financial
entities to maintain ICT risk governance covering AI autonomy risk
(Art. 5–7), implement protection controls for agent action boundaries
(Art. 9), and conduct resilience testing of autonomy controls (Art. 24–27).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — AI autonomy governance | Art. 5–7 | Governance | Include AI autonomy and excessive agency in the ICT risk management framework; define acceptable autonomy thresholds and escalation procedures for financial AI systems |
| Protection and Prevention — agent action boundaries | Art. 9 | Protection | Implement security controls enforcing least privilege on AI agent tool access, API permissions, and autonomous action scope within financial systems |
| Resilience Testing — autonomy boundary testing | Art. 24–27 | Testing | Include excessive agency scenarios in resilience testing; test that AI agents cannot exceed defined permission boundaries under adversarial conditions |
| Detection — unauthorised action detection | Art. 10 | Detection | Monitor AI agent actions for unauthorised tool invocations, scope violations, and anomalous behaviour patterns; alert on detection |

#### Mitigations

**Foundational**
- Art. 5–7: Define AI autonomy policies in the ICT risk management
  framework; specify maximum permitted tool access and autonomous
  action types for each financial AI deployment
- Art. 9: Implement least privilege for all AI agent tool access;
  maintain a tool permission manifest per deployment; require human
  approval for irreversible financial actions
- Art. 10: Log all AI agent tool invocations with full parameter
  capture; monitor for scope violations

**Hardening**
- Art. 24–27: Test autonomy boundaries as part of resilience testing;
  conduct red team exercises targeting excessive agency through
  indirect injection targeting tool invocation
- Art. 9: Enforce that AI agents cannot initiate financial transactions,
  modify customer data, or access regulated systems without explicit
  human authorisation
- Art. 5–7: Include AI autonomy risk in board-level risk reporting;
  review thresholds quarterly

**Advanced**
- Art. 24–27: Conduct formal adversarial exercises specifically testing
  indirect injection through every data source feeding financial AI
  agents; permission manifest must hold under worst-case injection
- Formally specify permitted action graphs for financial AI systems;
  only pre-approved action sequences can execute in production
- Art. 5–7: Include AI autonomy limits in regulatory reporting;
  document controls and residual risk

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI07 Lateral Tool Chaining
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: FedRAMP AC-6 – SP 800-218A PW.1.1-PS – MITRE ATLAS AML.T0015

---

### LLM07 – System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic, or security
controls are extracted by adversaries. DORA requires financial entities to
implement protection controls for system prompt confidentiality (Art. 9),
classify prompt extraction as an ICT incident for reporting (Art. 17–23),
and apply lessons learned from extraction events (Art. 13).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — prompt confidentiality | Art. 9 | Protection | Classify system prompts as sensitive ICT configuration; implement protection controls including encryption, access control, and output monitoring to prevent extraction |
| ICT Incident Management — prompt extraction reporting | Art. 17–23 | Incidents | Classify successful system prompt extraction as an ICT-related incident; assess impact and report per DORA incident classification criteria |
| Learning and Evolving — extraction post-mortem | Art. 13 | Learning | Conduct post-incident analysis for prompt extraction events; identify root cause, assess business impact, and update protection controls |
| Detection — extraction attempt detection | Art. 10 | Detection | Deploy detection mechanisms for system prompt extraction attempts; monitor inference requests for extraction technique patterns |

#### Mitigations

**Foundational**
- Art. 9: Classify system prompts as sensitive configuration; encrypt
  at rest, enforce access controls, and apply version control and
  audit logging to all prompt stores
- Art. 9: Enforce that no credentials, API keys, or sensitive business
  logic is embedded in system prompts; use secrets management solutions
- Art. 17–23: Define incident classification criteria for prompt
  extraction events; establish reporting procedures

**Hardening**
- Art. 10: Deploy output monitoring to detect response patterns
  indicative of system prompt disclosure; alert and escalate
- Art. 9: Conduct structured red team exercises covering known prompt
  extraction techniques before each deployment
- Art. 17–23: Include prompt extraction in incident response playbooks;
  define severity classification based on prompt content sensitivity

**Advanced**
- Art. 13: Document prompt extraction incidents and update controls
  based on post-incident analysis; share lessons across the organisation
- Deploy output classifiers trained to detect and block responses
  containing system prompt content
- Art. 9: Implement secrets detection in CI/CD pipelines; flag prompt
  configuration files containing potential credentials before deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| HashiCorp Vault | Commercial | https://www.vaultproject.io |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI08 Data Leakage & Exposure
- Other frameworks: CWE-200 – FedRAMP SC-28 – SP 800-218A PS.1.1-PS

---

### LLM08 – Vector and Embedding Weaknesses

**Severity:** Medium

Vulnerabilities in vector databases and embedding pipelines enable data
poisoning, unauthorised access, or extraction of sensitive information from
vector representations. DORA requires financial entities to implement
protection controls for embedding infrastructure (Art. 9) and include
embedding security in resilience testing (Art. 24–27).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — embedding store protection | Art. 9 | Protection | Implement security controls for vector databases and embedding stores — encryption at rest, access controls, and integrity monitoring for financial data embeddings |
| Resilience Testing — embedding security testing | Art. 24–27 | Testing | Include vector database and embedding pipeline security in resilience testing; test for injection, access control bypass, and data extraction from embeddings |
| Identification — embedding infrastructure assets | Art. 8 | Identification | Register vector databases, embedding models, and retrieval infrastructure in the ICT asset inventory with classification per data sensitivity |
| Detection — embedding tampering detection | Art. 10 | Detection | Monitor embedding stores for unauthorised modifications, anomalous writes, and bulk access patterns indicative of extraction or poisoning |

#### Mitigations

**Foundational**
- Art. 9: Encrypt all vector databases at rest; implement access
  controls restricting read/write access to authorised services;
  classify embedding stores by the sensitivity of source data
- Art. 8: Register embedding infrastructure in the ICT asset inventory;
  maintain dependency mapping to source data systems
- Art. 10: Monitor embedding store access patterns; alert on anomalous
  bulk reads or unexpected write operations

**Hardening**
- Art. 9: Implement tenant isolation in multi-tenant vector databases;
  enforce access control at namespace or collection level
- Art. 24–27: Include embedding inversion testing in resilience testing;
  assess whether sensitive financial data can be reconstructed from
  stored embeddings
- Art. 9: Deploy anomaly detection on embedding writes; flag vectors
  inconsistent with the source domain

**Advanced**
- Deploy embedding watermarking to detect tampering and verify provenance
- Art. 24–27: Conduct advanced resilience testing covering embedding
  poisoning, retrieval manipulation, and cross-tenant data leakage
- Art. 13: Document embedding security incidents; update protection
  controls based on lessons learned

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| Milvus | Open-source | https://milvus.io |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- Agentic Top 10: ASI06 Memory Poisoning & Context Confusion
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning
- Other frameworks: MITRE ATLAS AML.T0018 – FedRAMP SC-28 – SP 800-218A PS.1.1-PS

---

### LLM09 – Misinformation

**Severity:** Medium

LLMs generate factually incorrect, misleading, or fabricated content that
users or downstream systems treat as authoritative. In financial services,
misinformation can lead to incorrect risk assessments, compliance violations,
or customer harm. DORA requires detection of AI output quality degradation
(Art. 10), governance covering AI reliability (Art. 5–7), and continuous
improvement from misinformation incidents (Art. 13).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Detection — output quality monitoring | Art. 10 | Detection | Deploy detection mechanisms for AI output quality degradation — hallucinations, factual errors, and misleading content in financial AI outputs |
| ICT Risk Management — AI reliability governance | Art. 5–7 | Governance | Include AI output reliability in the ICT risk management framework; define acceptable accuracy thresholds for financial AI use cases |
| Learning and Evolving — misinformation post-mortem | Art. 13 | Learning | Conduct post-incident analysis for misinformation events; identify root cause, assess customer and regulatory impact, and update controls |
| Protection and Prevention — grounding controls | Art. 9 | Protection | Implement factual grounding controls for financial AI outputs — RAG with authoritative sources, confidence scoring, and human review for high-stakes outputs |

#### Mitigations

**Foundational**
- Art. 10: Monitor financial AI outputs for hallucination indicators;
  establish baseline accuracy metrics and alert on degradation
- Art. 5–7: Define acceptable accuracy thresholds for each financial
  AI use case; document in the ICT risk management framework
- Art. 9: Implement retrieval-augmented generation with authoritative
  financial data sources; verify grounding data currency and accuracy

**Hardening**
- Art. 10: Deploy automated hallucination detection; cross-check
  financial AI outputs against authoritative sources before delivery
- Art. 5–7: Include AI output quality metrics in management reporting;
  escalate accuracy degradation through risk governance channels
- Art. 13: Establish post-incident review process for misinformation
  events; update grounding sources and detection thresholds

**Advanced**
- Deploy factual grounding verification for all customer-facing
  financial AI outputs; require human review for regulatory and
  compliance-related content
- Art. 10: Include AI output quality monitoring in continuous DORA
  resilience assessment; track accuracy trends over time
- Art. 5–7: Include misinformation risk in board-level risk reporting
  for financial AI deployments

#### Tools

| Tool | Type | Link |
|---|---|---|
| Ragas | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |
| TruLens | Open-source | https://github.com/truera/trulens |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- DSGAI 2026: DSGAI17 Bias in Data
- Other frameworks: NIST AI RMF MAP 2.3 – FedRAMP SI-4 – SP 800-218A PW.7.2-PS

---

### LLM10 – Unbounded Consumption

**Severity:** Medium

Unrestricted resource usage — compute, memory, tokens, API costs — causes
denial of service or runaway cost. DORA requires financial entities to
implement protection controls for service availability (Art. 9), deploy
detection for consumption anomalies (Art. 10), and maintain backup and
recovery policies for AI service continuity (Art. 12).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — consumption controls | Art. 9 | Protection | Implement rate limiting, token quotas, and cost circuit breakers on financial AI inference services; define per-user and per-service consumption limits |
| Detection — consumption anomaly detection | Art. 10 | Detection | Monitor AI service consumption metrics in real time; alert on token spikes, latency degradation, and cost overruns affecting financial service availability |
| Backup Policies — AI service continuity | Art. 12 | Backup | Maintain backup model deployments and fallback inference paths for AI services supporting critical financial functions; test restoration procedures |
| Response and Recovery — consumption incident response | Art. 11 | Recovery | Define response and recovery procedures for AI consumption incidents; include automatic throttling, failover activation, and service restoration |

#### Mitigations

**Foundational**
- Art. 9: Define per-user token limits, rate limits, and cost budgets
  as mandatory protection controls; enforce at the API gateway
- Art. 10: Monitor consumption metrics and establish baseline usage;
  alert on deviations from expected patterns
- Art. 12: Maintain backup model deployments for critical financial
  AI services; document restoration procedures

**Hardening**
- Art. 9: Deploy cost circuit breakers with automatic suspension;
  per-tenant budgets with escalation on breach
- Art. 11: Define and test automated response to consumption incidents;
  exercise procedures quarterly per DORA resilience testing requirements
- Art. 10: Include adversarial consumption patterns in detection
  scenarios; test detection capabilities regularly

**Advanced**
- Conduct adversarial cost-maximisation testing for financial AI
  services; identify maximum-cost input patterns and apply controls
- Art. 12: Include AI services in DORA business continuity testing;
  verify backup deployments under production load
- Art. 11: Document AI service RTO and RPO per DORA requirements;
  include in regulatory reporting

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| AWS Budgets / Azure Cost Management | Commercial | https://aws.amazon.com/aws-cost-management/aws-budgets/ |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 – FedRAMP SC-7 – SP 800-218A PW.2.1-PS

---

## Implementation priority

| Phase | Governance (Art. 5–7) | Protection & Detection (Art. 9–10) | Testing & Third-Party (Art. 24–44) |
|---|---|---|---|
| 1 – Now | Include AI risk in ICT risk management framework (LLM06/09); define AI data policies (LLM02) | Art. 9 input validation for LLM01; output monitoring for LLM02/07; rate limiting for LLM04/10 | Art. 28–44 third-party AI provider assessment for LLM03/05 |
| 2 – This sprint | AI autonomy policies for LLM06; AI supply chain governance for LLM05 | Art. 10 detection for LLM01/04/09/10; Art. 9 embedding protection for LLM08 | Art. 24–27 prompt injection testing for LLM01; supply chain resilience for LLM05 |
| 3 – This quarter | Board-level AI risk reporting; AI incident classification criteria (LLM02/07) | Art. 9 comprehensive protection for all entries; Art. 10 AI behaviour monitoring | Art. 24–27 full AI resilience testing programme; Art. 28–44 critical provider assessments |
| 4 – Ongoing | Governance framework refresh; regulatory reporting updates | Continuous monitoring; detection tuning; protection control updates | Annual resilience testing; third-party reassessment; threat intelligence sharing (Art. 45) |

---

## References

- [DORA – EU Regulation 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [EBA DORA Regulatory Technical Standards](https://www.eba.europa.eu/regulation-and-policy/digital-operational-resilience-act-dora)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [ECB Guide on Outsourcing and ICT Risk](https://www.bankingsupervision.europa.eu/)
- [MITRE ATLAS](https://atlas.mitre.org)
- [ENISA Threat Landscape for AI](https://www.enisa.europa.eu/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – LLM01–LLM10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
