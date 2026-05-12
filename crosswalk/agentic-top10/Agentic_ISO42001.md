<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : ISO/IEC 42001:2023 — Artificial Intelligence Management System
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × ISO/IEC 42001:2023

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) —
the international standard for Artificial Intelligence Management Systems (AIMS).

---

## Why ISO 42001 is critical for agentic AI governance

Agentic AI systems expose ISO 42001 obligations more acutely than
any other AI deployment pattern because the standard's two most
demanding requirements — impact assessment (A.5.2) and responsible
AI system management (A.6.1.2) — are directly triggered by autonomy.

**A.5.2 Impact assessment** requires organisations to assess the
impact of AI systems on persons. An agent that executes multi-step
actions autonomously — submitting work orders, sending communications,
modifying records, or influencing process control — has a direct,
concrete impact on persons that a static advisory LLM does not.
Every agentic deployment at an organisation with ISO 42001 scope
requires a formal impact assessment under A.5.2.

**A.6.1.2 Responsible AI system management** requires that AI systems
be managed responsibly throughout their lifecycle. Autonomous operation,
persistent memory, tool access, and multi-agent orchestration each
introduce lifecycle management obligations that did not exist for
earlier advisory AI deployments.

**A.6.2.3 AI system security** requires security controls appropriate
to the AI system's risk profile. Agentic systems warrant significantly
stronger security controls than equivalent static LLMs — this mapping
documents the specific controls that A.6.2.3 requires for each
Agentic Top 10 risk.

---

## Quick-reference summary

| ID | Name | Severity | Primary ISO 42001 Controls | Tier |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | A.6.2.3, A.6.2.6, A.5.2, Cl.6.1 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | A.6.1.2, A.6.2.3, A.5.2, A.10.1 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | A.6.2.3, A.7.3, Cl.7, A.10.1 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | A.10.1, A.10.2, A.6.2.3, A.7.2 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | A.6.2.3, A.6.2.6, A.5.2, Cl.6.1 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | A.7.2, A.7.3, A.6.2.3, A.6.2.8 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | A.6.2.3, A.6.2.6, A.10.1, Cl.8 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | A.6.2.3, A.6.2.8, Cl.6.1, Cl.9 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | A.5.2, A.8.1, A.9.1, Cl.5 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | A.6.2.3, A.6.2.8, A.6.1.2, Cl.9 | Hardening–Advanced |

---

## Audience tags

- **CISO / governance** — full file, ISO 42001 AIMS integration for agentic AI programme
- **AI governance lead** — A.5.2 impact assessment, A.6.1.2 responsible management
- **Auditor / certifier** — clause and control mapping for ISO 42001 certification
- **Security engineer** — A.6.2.3, A.6.2.6, A.6.2.8 technical control entries
- **Legal / DPO** — A.5.2 impact assessment, A.8.1 transparency obligations
- **OT engineer** — ASI01, ASI02, ASI08 with ISA 62443 crosswalk

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through instruction injection.
Under ISO 42001, goal hijack is both a security risk (A.6.2.3) and
an impact risk (A.5.2) — an agent whose goal has been redirected
autonomously executing a harmful multi-step attack chain has a direct,
concrete impact on persons that must be assessed and managed.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Goal-state verification and input validation as AIMS security design requirements — structural controls enforced at orchestration layer |
| Testing of AI systems | A.6.2.6 | Goal hijack scenarios in AIMS testing — direct, indirect, multi-turn injection tested before each production release |
| Impact assessment | A.5.2 | Impact assessment covers goal hijack risk — what autonomous actions are possible if goal is redirected, who is affected |
| Risk assessment | Cl.6.1 | Goal hijack in AI risk register — blast radius per deployment, owner, treatment, review cadence |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.5.2: Include goal hijack in AI impact assessment —
  what autonomous actions are possible if goal is
  redirected, which stakeholders are affected, documented
  in AIMS before any agentic deployment
- Cl.6.1: Document goal hijack in AI risk register —
  deployment-specific blast radius, risk owner,
  treatment controls, review cadence
- A.6.2.3: Implement goal-state verification and input
  validation as AIMS security design requirements —
  document as A.6.2.3 control evidence before deployment

**Hardening**
- A.6.2.6: Include goal hijack scenarios in AIMS testing
  programme — all indirect injection surfaces tested,
  results as AIMS documented information
- A.6.2.8: Implement runtime injection monitoring as
  AIMS operational control — alerts integrated into
  AIMS incident management
- Kill switch documented as A.6.2.3 security design
  control — tested as A.6.2.6 testing activity

**Advanced**
- A.5.2: Update impact assessment when agent autonomy
  scope expands — AIMS requirement before each new
  agentic capability is enabled in production
- Cl.9: Include goal hijack incidents in AIMS
  performance evaluation — trend data, control
  effectiveness in management review

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways, DSGAI15 Over-Broad Context Windows
- Other frameworks: EU AI Act Art. 14 · AIUC-1 B001/B005 · NIST CSF 2.0 GV.OC-01

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools via prompt manipulation or unsafe
delegation. Under ISO 42001, A.6.1.2 (responsible AI system management)
requires that tool access be managed responsibly throughout the agent
lifecycle — tool permissions are a lifecycle management obligation,
not a one-time configuration.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Responsible AI system management | A.6.1.2 | Tool access managed responsibly throughout agent lifecycle — permission review, irreversibility classification, human oversight requirements |
| AI system security | A.6.2.3 | Per-tool permission manifests and parameter validation as AIMS security controls |
| Impact assessment | A.5.2 | Tool misuse impact assessed — what harm is possible if each tool is misused autonomously |
| Third-party AI system acquisition | A.10.1 | Tool and MCP server providers assessed as third-party AI components — security obligations in contracts |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.5.2: Include tool misuse in AI impact assessment —
  for each tool: what is the worst-case harm if misused
  autonomously, which stakeholders are affected,
  documented in AIMS before deployment
- A.6.1.2: Manage tool access as responsible AI system
  lifecycle obligation — permission review at each
  deployment, change, and quarterly thereafter
- Human confirmation gates for irreversible tools —
  documented as A.6.1.2 responsible management control

**Hardening**
- A.6.2.3: Implement per-tool permission manifests and
  parameter validation as AIMS security design requirements
- A.6.2.6: Include tool misuse scenarios in AIMS testing —
  destructive parameters, tool chain exploitation, MCP
  descriptor poisoning tested before each deployment
- A.10.1: Apply security requirements to all tool and
  MCP server providers — AIMS third-party obligations

**Advanced**
- A.5.2: Formal impact assessment before adding any
  new tool to an agentic deployment — AIMS requirement
  before each new tool capability
- Cl.9: Monitor tool invocation patterns in AIMS
  performance evaluation — anomalous patterns, misuse
  incidents in management review

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: EU AI Act Art. 14 · AIUC-1 B006/B007 · ISA/IEC 62443 SR 2.2 (OT)

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials that attackers exploit for lateral
movement. ISO 42001 Clause 7 (Support) and A.7.3 (Data provenance)
govern credential handling as an AIMS resource and data management
obligation — NHI is an AI system resource under ISO 42001.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Credential security as AIMS design requirement — short-lived JIT credentials, no cleartext storage, least privilege |
| Data provenance and characteristics | A.7.3 | Agent credentials tracked as AI system data — issuance, scope, expiry, rotation documented |
| Support | Cl.7 | Resources for AI systems include NHIs — agent identities inventoried and managed as AIMS resources |
| Third-party AI system acquisition | A.10.1 | Third-party services accessed via agent credentials assessed — security obligations in access arrangements |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.7: Inventory all agent NHIs as AI system resources —
  permissions, TTL, rotation schedule documented in AIMS
- A.6.2.3: Implement short-lived JIT credentials as AIMS
  security design requirement — no long-lived agent tokens
- A.7.3: Track agent credential provenance — issuance,
  scope, expiry, rotation as AIMS documented information

**Hardening**
- A.6.2.3: Encrypt all agent credentials at rest —
  secret manager, no cleartext in config or agent memory,
  documented as AIMS security control
- A.6.2.8: Monitor credential usage as AIMS operational
  control — anomalous access patterns alerted
- A.10.1: Apply security requirements to all services
  accessed via agent credentials — AIMS third-party
  obligation

**Advanced**
- Cl.9: Include credential exposure incidents in AIMS
  performance evaluation — NHI programme maturity
  metrics in management review
- Formal agent offboarding procedure as A.6.1.2
  responsible lifecycle management — credential
  revocation on decommission documented in AIMS

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 A/B007 · NIST CSF 2.0 PR.AA-01/05

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Compromised tools, MCP servers, or model components alter agent
behaviour. ISO 42001 A.10 (Third-party and customer relationships)
is the primary section — all agent components are third-party AI
system components under ISO 42001.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Third-party AI system acquisition | A.10.1 | All agent tool and MCP server providers assessed — security obligations, integrity guarantees, disclosure SLA in contracts |
| Customer relationships | A.10.2 | Obligations to downstream consumers of agentic systems — what supply chain security is guaranteed |
| AI system security | A.6.2.3 | Component integrity verification as AIMS security design requirement — cryptographic signatures before loading |
| Data quality | A.7.2 | Training data from third-party sources assessed — same data quality criteria as internal data |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.10.1: Establish AIMS third-party requirements for
  all agent component vendors — integrity guarantees,
  vulnerability disclosure, incident notification
  documented before any component enters production
- A.6.2.3: Component integrity verification as AIMS
  security design requirement — cryptographic signatures
  verified before loading any tool, MCP server, or model

**Hardening**
- A.6.2.6: Test all components in AIMS testing programme —
  signature verification, descriptor review for hidden
  instructions, behavioural testing in isolated environment
- A.10.1: Include agent supply chain incidents in AIMS
  third-party review — compromised component response
  procedure documented as AIMS operational control

**Advanced**
- A.10.2: Document supply chain security obligations
  provided to downstream consumers — what component
  integrity they can rely on when consuming your
  agentic system APIs
- Cl.9: Include supply chain incidents in AIMS
  performance evaluation — trend data, vendor
  performance in management review

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · NIST CSF 2.0 GV.SC-01 · ISO 27001 A.5.19/A.5.21

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate and execute code become RCE gateways. Under
ISO 42001, code execution capability requires formal risk assessment
(Cl.6.1) and impact assessment (A.5.2) before any agent with this
capability is deployed — the impact on persons from RCE in an
agentic deployment is severe and must be formally accepted.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Sandbox, static analysis, and allowlist as AIMS security design requirements for code execution capability |
| Testing of AI systems | A.6.2.6 | Sandbox escape and code injection scenarios in AIMS testing — adversarial testing before each deployment |
| Impact assessment | A.5.2 | Impact of code execution capability formally assessed — RCE impact on persons and systems documented |
| Risk assessment | Cl.6.1 | Code execution risk in AI risk register — blast radius, sandbox status, permitted operations documented |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.6.1: Document code execution risk in AI risk register —
  sandbox status, permitted operations, blast radius,
  formal risk acceptance before any agentic code execution
  deployment
- A.5.2: Formal impact assessment for code execution
  capability — what harm is possible, which persons are
  affected, documented in AIMS before deployment
- A.6.2.3: Sandbox, static analysis, and allowlist as
  AIMS security design requirements — no deployment
  without these controls documented

**Hardening**
- A.6.2.6: Include sandbox escape scenarios in AIMS
  testing — adversarial code injection tested before
  each deployment, results as AIMS test evidence
- A.6.2.3: Network isolation of code execution environment
  as AIMS security design requirement — documented before
  any code execution deployment

**Advanced**
- Hardware-level sandboxing as advanced A.6.2.3 security
  design control — documented in AIMS for highest-risk
  code execution deployments
- Cl.9: Include code execution incidents in AIMS
  performance evaluation — incident rates, sandbox
  effectiveness in management review

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent memory poisoning causes systematic incorrect behaviour.
ISO 42001 A.7 (Data for AI systems) governs agent memory stores as
AI data assets — the same data governance obligations that apply to
training data apply to agent memory that influences behaviour.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Data quality | A.7.2 | Agent memory content quality requirements — access controls, integrity verification, TTL as data quality controls |
| Data provenance and characteristics | A.7.3 | Memory provenance tracked — source, write access controls, TTL, modification history in AIMS |
| AI system security | A.6.2.3 | Memory store access controls and integrity monitoring as AIMS security design requirements |
| Monitoring of AI systems | A.6.2.8 | Memory integrity monitored in operation — anomalous write patterns, content integrity checks as AIMS monitoring |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.7.2: Establish data quality requirements for agent
  memory — access controls, write restrictions, content
  validation, TTL documented as AIMS data quality controls
- A.7.3: Track memory provenance in AIMS — source of
  each memory entry, write access controls, TTL,
  modification history as AIMS documented information
- A.6.2.3: Memory store access controls as AIMS security
  design requirement — only agent and designated
  administrators can write, documented before deployment

**Hardening**
- A.6.2.8: Implement memory integrity monitoring as AIMS
  operational control — statistical anomaly detection,
  alerts integrated into AIMS incident management
- Memory TTL enforcement as A.7.2 data quality control —
  entries expire and require re-validation, documented
  in AIMS

**Advanced**
- Cryptographic integrity verification of memory store
  as advanced A.6.2.3 security control — tamper
  detection documented in AIMS
- Cl.9: Include memory poisoning incidents in AIMS
  performance evaluation — affected decisions, operational
  impact in management review

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002 · NIST AI RMF MS-2.5 · ISA/IEC 62443 SR 3.7 (OT)

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

A2A communication channels lacking authentication enable agent-in-the-
middle attacks. ISO 42001 A.6.2.3 (security) and Clause 8 (operation)
govern A2A communication security as an operational design control.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | A2A authentication, encryption, and schema validation as AIMS security design requirements |
| Testing of AI systems | A.6.2.6 | A2A security scenarios in AIMS testing — spoofing, replay, schema violations before deployment |
| Third-party AI system acquisition | A.10.1 | A2A communication infrastructure providers assessed — security obligations in arrangements |
| Operation | Cl.8 | A2A communication documented as AIMS operational control — authentication requirements, encryption standards |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.6.2.3: Document A2A authentication and encryption
  as AIMS security design requirements — mutual TLS,
  unique agent identities, replay protection specified
  before deployment
- Cl.8: A2A communication controls documented as AIMS
  operational procedures — authentication method, key
  management, anomaly response

**Hardening**
- A.6.2.6: Include A2A security scenarios in AIMS testing —
  unauthenticated injection, replay attacks, schema
  violations tested before deployment
- A.6.2.8: Monitor A2A channels as AIMS operational
  control — anomalous patterns, unusual senders alerted

**Advanced**
- Cl.9: Include A2A security incidents in AIMS
  performance evaluation — channel compromise events,
  authentication failures in management review
- PKI-backed agent identities for A2A as advanced
  A.6.2.3 security control — documented in AIMS

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 NHI-4/NHI-7 · AIUC-1 B007/B008 · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Single-point faults propagate through multi-agent workflows. ISO 42001
Clause 6.1 (risk assessment) requires cascade blast radius to be
formally documented and accepted before multi-agent deployment.
In OT environments this is Critical severity.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Circuit breakers and blast radius limits as AIMS security design requirements |
| Monitoring of AI systems | A.6.2.8 | Cascade indicators monitored in operation — correlated failure patterns detected as AIMS monitoring |
| Risk assessment | Cl.6.1 | Cascade blast radius in AI risk register — maximum affected systems formally documented and accepted |
| Performance evaluation | Cl.9 | Cascade incidents in AIMS performance evaluation — circuit breaker effectiveness, recovery times in management review |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.6.1: Document cascade blast radius in AI risk register —
  maximum systems affected by any single failure,
  formally accepted before multi-agent deployment
- A.6.2.3: Circuit breakers and fail-safe defaults as
  AIMS security design requirements — documented before
  any multi-agent production deployment
- Kill switch documented as AIMS operational control
  under Clause 8 — tested as A.6.2.6 testing activity

**Hardening**
- A.6.2.8: Cascade detection monitoring as AIMS operational
  control — correlated failure patterns alerted before
  physical impact in OT environments
- Agent cluster segmentation as A.6.2.3 design control —
  failure propagation bounded by architecture

**Advanced**
- A.5.2: Impact assessment covers cascade scenarios —
  what physical or operational harm is possible from
  cascade in each deployment, documented in AIMS
- Cl.9: Include cascade incidents in AIMS performance
  evaluation — blast radius, circuit breaker
  effectiveness, recovery times in management review

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6/7.7 (OT) · NIST SP 800-82 Rev 3

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents build false trust enabling manipulation of human approvers.
ISO 42001 A.8.1 (Information for interested parties) and A.9.1
(Use of AI systems) directly govern the transparency and use guidance
obligations that are the primary defence against trust exploitation.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Impact assessment | A.5.2 | Trust exploitation impact assessed — which persons are affected by AI decisions influenced by manipulated trust |
| Information for interested parties | A.8.1 | AI system transparency obligations — users informed of AI nature, advisory status, limitations, EU AI Act Art. 50 alignment |
| Use of AI systems | A.9.1 | Guidance on appropriate use — domains requiring human verification, how to distinguish AI advisory from authoritative content |
| Policy | Cl.5 | Leadership commitment to AI transparency — AI disclosure and advisory labelling requirements in AI policy |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.5: Establish AI transparency as policy commitment —
  AI disclosure, advisory labelling, and human oversight
  requirements documented at executive level in AIMS
- A.8.1: Implement AI transparency as AIMS obligation —
  all agent-user interactions disclose AI nature,
  advisory status communicated — EU AI Act Art. 50
  compliance as AIMS control evidence
- A.9.1: Document appropriate use guidance for all
  agentic deployments — domains requiring verification,
  how to identify AI output vs authoritative content

**Hardening**
- A.5.2: Include trust exploitation in AI impact assessment —
  which persons are affected by decisions influenced
  by manipulated agent trust, documented in AIMS
- A.6.2.8: Monitor for aggregate over-trust patterns
  as AIMS operational control — systematic operator
  acceptance without verification detected

**Advanced**
- Cl.9: Include trust exploitation incidents in AIMS
  performance evaluation — pattern analysis, operator
  competency assessment results in management review
- A.9.1: Operator training on AI limitations as AIMS
  support requirement — competence evidence documented
  per Clause 7

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 C/F · ISA/IEC 62443 SR 2.3 (OT)

---

### ASI10 — Rogue Agents

**Severity:** Critical

Compromised agents pursue hidden goals while appearing compliant.
Under ISO 42001, A.6.1.2 (responsible AI system management) requires
that agents be managed responsibly throughout their operational lifecycle
— a rogue agent operating without detection is an A.6.1.2 failure.
A.6.2.8 (monitoring) is the primary detection control.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Scope constraints enforced at infrastructure layer — rogue agent cannot exceed permission envelope |
| Monitoring of AI systems | A.6.2.8 | Behavioural monitoring as AIMS operational control — baseline deviation detection is the primary rogue agent control |
| Responsible AI system management | A.6.1.2 | Comprehensive audit logging and rogue agent containment as responsible lifecycle management obligation |
| Performance evaluation | Cl.9 | Rogue agent detection rates and containment times in AIMS management review |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.6.1.2: Document comprehensive audit logging as
  responsible AI system management obligation — no
  agentic production deployment without full observability
- A.6.2.3: Scope constraints as AIMS security design
  requirement — rogue agent cannot exceed permission
  envelope, enforced at infrastructure layer
- Cl.6.1: Document rogue agent risk in AI risk register —
  detection capability status, blast radius, containment
  procedure per deployment

**Hardening**
- A.6.2.8: Establish behavioural baseline and continuous
  monitoring as AIMS operational control — baseline
  documented during commissioning, deviation triggers
  tiered response
- A.6.1.2: Rogue agent containment procedure as
  responsible lifecycle management — kill switch,
  recommendation audit, state validation documented

**Advanced**
- Cl.9: Include rogue agent detection and containment
  in AIMS performance evaluation — detection rates,
  dwell time, blast radius, corrective actions in
  management review
- Aggregate recommendation analysis as A.6.2.8
  monitoring control — systematic bias detected
  through periodic pattern review

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · EU AI Act Art. 14/15 · ISA/IEC 62443 SR 3.7 (OT)

---

## ISO 42001 AIMS implementation checklist for agentic deployments

### Before any agentic deployment

- [ ] AI risk assessment completed covering all ASI01–ASI10 risks (Cl.6.1)
- [ ] AI impact assessment completed — autonomous action impact on persons (A.5.2)
- [ ] Tool access formally documented — permission manifests, irreversibility classification (A.6.1.2)
- [ ] Agent NHIs inventoried as AI system resources (Cl.7)
- [ ] Third-party requirements applied to all tool and MCP providers (A.10.1)
- [ ] Transparency obligations assessed — AI disclosure, advisory labelling (A.8.1)
- [ ] Use guidance documented — verification requirements, trust boundaries (A.9.1)

### Design and development

- [ ] Goal-state verification documented as AIMS security design control (A.6.2.3)
- [ ] Tool permission manifests documented as AIMS security design control (A.6.2.3)
- [ ] Short-lived JIT credentials as AIMS security design requirement (A.6.2.3)
- [ ] Kill switch design documented as AIMS security design control (A.6.2.3)
- [ ] Cascade containment architecture documented (A.6.2.3)
- [ ] Code execution sandbox design documented if applicable (A.6.2.3)

### Testing

- [ ] Goal hijack scenarios in AIMS testing programme (A.6.2.6)
- [ ] Tool misuse scenarios in AIMS testing programme (A.6.2.6)
- [ ] Supply chain component integrity tested (A.6.2.6)
- [ ] Kill switch tested from operator console (A.6.2.6)
- [ ] A2A security scenarios tested (A.6.2.6)
- [ ] Behavioural baseline established during commissioning (A.6.2.8)

### Operation

- [ ] Behavioural monitoring live for all agents (A.6.2.8)
- [ ] Memory integrity monitoring live for all memory stores (A.6.2.8)
- [ ] Credential anomaly monitoring live (A.6.2.8)
- [ ] A2A channel monitoring live (A.6.2.8)
- [ ] Cascade detection monitoring live (A.6.2.8)

### Performance evaluation and review

- [ ] All ASI risks covered in AIMS performance monitoring (Cl.9)
- [ ] Agentic incidents included in AIMS management review (Cl.9)
- [ ] Third-party agent component performance reviewed (Cl.9)
- [ ] Impact assessments updated when agentic scope expands (A.5.2)

---

## ISO 42001 and EU AI Act alignment for agentic AI

ISO 42001 and the EU AI Act are increasingly aligned — the EU AI Act
references management system approaches as evidence of compliance:

| EU AI Act Article | ISO 42001 alignment | ASI entries |
|---|---|---|
| Art. 9 — Risk management | Cl.6.1 AI risk assessment | All ASI entries |
| Art. 9 — Risk management | A.5.2 Impact assessment | ASI01, ASI02, ASI05, ASI09 |
| Art. 14 — Human oversight | A.6.1.2 Responsible management | ASI01, ASI02, ASI08, ASI10 |
| Art. 15 — Robustness and cybersecurity | A.6.2.3 AI system security | All ASI entries |
| Art. 15 — Accuracy and robustness | A.6.2.6 Testing | All ASI entries |
| Art. 17 — Quality management | Cl.9 Performance evaluation | All ASI entries |
| Art. 13 — Transparency | A.8.1 Information for interested parties | ASI09 |
| Art. 25 — Value chain | A.10.1 Third-party relationships | ASI03, ASI04, ASI07 |

Organisations using ISO 42001 as a management system for agentic AI
can use AIMS documented information as evidence of EU AI Act compliance
— the mapping above shows which AIMS controls satisfy which articles.

---

## References

- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [LLM Top 10 × ISO 42001](../llm-top10/LLM_ISO42001.md)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with AIMS checklist and EU AI Act alignment table | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
