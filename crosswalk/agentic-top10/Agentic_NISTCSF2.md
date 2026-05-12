<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : NIST Cybersecurity Framework 2.0 (CSF 2.0)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × NIST CSF 2.0

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework).

The new GOVERN function in CSF 2.0 is especially relevant for agentic
AI — autonomous systems require explicit governance policies around
acceptable autonomy scope, human oversight requirements, and supply
chain management that the old CSF 1.1 had no category for. Every
agentic deployment should map its autonomy policy to GV.OC-01 and
GV.RM-01 before any technical controls are designed.

---

## Quick-reference summary

| ID | Name | Severity | Primary CSF 2.0 Categories | Tier |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | GV.OC-01, PR.PS-04, DE.CM-01, RS.MI-01 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | PR.AA-05, GV.OC-01, DE.CM-01, RS.AN-03 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | PR.AA-01, PR.AA-05, PR.DS-01, DE.CM-01 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | GV.SC-01, GV.SC-06, ID.AM-08, PR.PS-02 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | PR.PS-04, PR.IR-01, DE.CM-01, RS.MI-01 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | PR.DS-01, DE.CM-09, ID.AM-08, RS.AN-03 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | PR.AA-01, PR.DS-02, DE.CM-01, GV.SC-01 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | PR.IR-01, DE.CM-01, RS.MI-01, RC.RP-01 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | GV.OC-01, PR.AT-01, DE.CM-09, RS.CO-03 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | DE.CM-09, DE.AE-02, RS.AN-03, PR.AA-05 | Hardening–Advanced |

---

## Audience tags

- **CISO / governance** — full file, CSF 2.0 integration for agentic AI programme
- **Risk manager** — GOVERN and IDENTIFY entries per vulnerability
- **Security operations** — DETECT and RESPOND entries
- **Federal agency / FISMA** — CSF 2.0 as NIST reference framework
- **OT engineer** — ASI01, ASI02, ASI08 with ISA 62443 crosswalk

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through instruction injection.
CSF 2.0 GOVERN provides the policy anchor — without GV.OC-01 defining
acceptable agent behaviour, every other control lacks a reference point.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Policy defines permissible agent autonomy — agents cannot change stated goals without human confirmation |
| Platform Security | PR.PS-04 | PROTECT | Secure software development — input validation and goal-state verification as platform security controls |
| Continuous Monitoring | DE.CM-01 | DETECT | Networks and assets monitored — injection indicators detected across all agent input channels |
| Incident Mitigation | RS.MI-01 | RESPOND | Incidents contained — agent suspended, actions reversed, kill switch activated |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Establish and document policy on permissible
  agent autonomy — what goal changes require human
  confirmation, what actions agents cannot take autonomously
- GV.RM-06: Include agent goal hijack in risk register —
  document per-deployment blast radius, owner, treatment

**IDENTIFY**
- ID.RA-01: Map all injection paths per deployment in
  risk assessment — user prompt, RAG, tool returns,
  email, documents, web content

**PROTECT**
- PR.PS-04: Implement goal-state verification and input
  validation as platform security requirements — structural
  controls enforced at the orchestration layer
- Treat all external content as untrusted regardless of
  source channel

**DETECT**
- DE.CM-01: Monitor all agent input channels for injection
  indicators — real-time detection, not periodic review

**RESPOND**
- RS.MI-01: Define containment procedure for goal hijack —
  kill switch activation, action reversal checklist,
  downstream impact assessment

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B001/B005 · NIST AI RMF GV-1.7 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools via prompt manipulation or unsafe
delegation. CSF 2.0 identity and access control (PR.AA) governs
the tool permission surface.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions managed — per-tool permission manifests, least privilege per tool, irreversibility classification |
| Organisational Context | GV.OC-01 | GOVERN | Policy defines permissible tool invocations — which tools require human confirmation |
| Continuous Monitoring | DE.CM-01 | DETECT | All tool invocations logged and monitored — anomalous parameters, unusual sequences, high frequency detected |
| Incident Analysis | RS.AN-03 | RESPOND | Root cause analysis — which tool was misused, what downstream impact occurred, what parameters were used |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Define tool use policy — approved tools per
  agent role, operations requiring human confirmation,
  prohibited tool operations documented

**PROTECT**
- PR.AA-05: Implement per-tool permission manifests —
  each tool scoped to minimum required operations,
  enforced at the orchestration layer
- Human confirmation gates for all irreversible tool
  invocations — independent of the agent interface

**DETECT**
- DE.CM-01: Log and monitor all tool invocations —
  tool identity, parameters, user session, timestamp,
  anomalous patterns alerted

**RESPOND**
- RS.AN-03: Investigate tool misuse incidents — what
  parameters were generated, what downstream state
  was changed, what can be reversed

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006/B007 · EU AI Act Art. 14 · ISA/IEC 62443 SR 2.2 (OT)

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials exploited for lateral movement.
CSF 2.0 identity management (PR.AA) and data security (PR.DS) are
the primary PROTECT categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-01 | PROTECT | Identities and credentials managed — NHI inventory, lifecycle management, unique identity per agent |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions managed — agent credential scope enforced, least privilege per agent role |
| Data Security | PR.DS-01 | PROTECT | Sensitive data protected at rest — agent credentials encrypted, not stored in cleartext |
| Continuous Monitoring | DE.CM-01 | DETECT | Credential usage monitored — anomalous access patterns detected |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Include agent credential exposure in risk
  register — document NHI inventory status, scope
  controls, rotation programme maturity

**IDENTIFY**
- ID.AM-08: Inventory all agent NHIs as part of asset
  management — every agent identity, its permissions,
  TTL, and associated systems

**PROTECT**
- PR.AA-01: Manage all agent identities — unique NHI
  per deployment, documented lifecycle, no shared
  credentials across agent instances
- PR.AA-05: Enforce least privilege on all agent
  credentials — minimum scope, quarterly review,
  short-lived JIT issuance
- PR.DS-01: Store all agent credentials encrypted —
  secret manager, no cleartext in config or logs

**DETECT**
- DE.CM-01: Monitor agent credential usage — anomalous
  access scope, unusual timing, cross-system lateral
  movement detected

**RESPOND**
- RS.MI-01: Contain credential exposure — immediate
  rotation, lateral movement assessment, downstream
  system notification

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 A/B007 · ISO 27001 A.8.2

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Compromised tools, MCP servers, or model components alter agent
behaviour. CSF 2.0 GOVERN supply chain risk management (GV.SC)
is the primary category — supply chain is now a first-class concern.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Cybersecurity supply chain risk management programme — all agent component vendors in scope |
| Supply Chain Risk Management | GV.SC-06 | GOVERN | Cybersecurity requirements in supplier contracts — integrity guarantees, vulnerability disclosure SLA |
| Asset Management | ID.AM-08 | IDENTIFY | Agent components inventoried — ML SBOM for all tools, MCP servers, model weights, libraries |
| Platform Security | PR.PS-02 | PROTECT | Software managed to reduce risk — component integrity verification, change management |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Establish supply chain programme for all
  agent components — tool providers, MCP server vendors,
  model weight sources assessed and managed
- GV.SC-06: Include security requirements in contracts
  with all agent component providers — integrity, disclosure,
  notification obligations

**IDENTIFY**
- ID.AM-08: Maintain ML SBOM for all agent deployments —
  components inventoried with versions, sources, hashes
- ID.RA-08: Receive threat intelligence on agent supply
  chain threats — MCP compromise campaigns, model backdoors

**PROTECT**
- PR.PS-02: Verify integrity of all components before
  deployment — cryptographic signatures, hash verification
- Change management for all component updates — no
  runtime loading from unapproved sources

**DETECT**
- DE.CM-09: Monitor for unauthorised component changes —
  runtime hash verification, deviation triggers alert

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · ISO 27001 A.5.19/A.5.21 · ISA/IEC 62443 62443-2-4 (OT)

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate and execute code become RCE gateways. CSF 2.0
platform security (PR.PS) and infrastructure resilience (PR.IR)
address sandbox and execution control requirements.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Platform Security | PR.PS-04 | PROTECT | Secure software development — static analysis, sandbox, allowlist as code execution platform security controls |
| Infrastructure Resilience | PR.IR-01 | PROTECT | Networks and environments protected — sandbox isolated from production infrastructure |
| Continuous Monitoring | DE.CM-01 | DETECT | Code execution monitored — sandbox escape attempts, anomalous system calls detected |
| Incident Mitigation | RS.MI-01 | RESPOND | Code execution incidents contained — sandbox isolated, forensic capture initiated |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Policy defines agent code execution scope —
  which agents may execute code, what sandbox requirements
  apply, what formal approval is required

**PROTECT**
- PR.PS-04: Implement static analysis, sandbox, and allowlist
  as platform security requirements for all code execution
  capability in agent deployments
- PR.IR-01: Isolate code execution sandbox from production
  infrastructure — no network access to production systems
  from within sandbox

**DETECT**
- DE.CM-01: Monitor code execution environments —
  anomalous system calls, network attempts, file access
  outside scratch directory detected and alerted

**RESPOND**
- RS.MI-01: Contain code execution incidents — sandbox
  isolation, kill switch activation, scope assessment

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent memory poisoning causes systematic incorrect behaviour
across all future interactions. CSF 2.0 data security (PR.DS) and
detection (DE.CM) govern memory store integrity.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Agent memory stores protected at rest — access controls, encryption, integrity verification |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for anomalous data — memory content integrity checks, unusual write patterns detected |
| Asset Management | ID.AM-08 | IDENTIFY | Agent memory stores inventoried as data assets — content classification, access controls, TTL documented |
| Incident Analysis | RS.AN-03 | RESPOND | Memory poisoning incidents analysed — affected sessions identified, operational decisions influenced reviewed |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Include memory poisoning in risk register —
  per deployment documentation of memory trust levels
  and detection capability

**IDENTIFY**
- ID.AM-08: Inventory all agent memory stores —
  classify content, document access controls, TTL, and
  write access controls

**PROTECT**
- PR.DS-01: Protect agent memory stores — access controls,
  encryption at rest, write access restricted to authorised
  sources, TTL enforced

**DETECT**
- DE.CM-09: Monitor memory stores for anomalous content
  and access patterns — statistical integrity checks,
  unusual write volumes alerted

**RESPOND**
- RS.AN-03: Investigate poisoning incidents — which memory
  entries were affected, which decisions were influenced,
  what operational impact occurred

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002 · NIST AI RMF MS-2.5 · ISA/IEC 62443 SR 3.7 (OT)

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

A2A channels lacking authentication enable agent-in-the-middle attacks.
CSF 2.0 identity management (PR.AA) and data-in-transit protection
(PR.DS-02) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-01 | PROTECT | Agent identities managed — each agent has a unique, verifiable identity for A2A authentication |
| Data Security | PR.DS-02 | PROTECT | Data in transit protected — all A2A communication encrypted, integrity verified |
| Continuous Monitoring | DE.CM-01 | DETECT | A2A channels monitored — replay attacks, spoofed senders, anomalous message patterns detected |
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Inter-agent communication infrastructure treated as internal supply chain — authentication requirements documented |

#### Mitigations by CSF function

**PROTECT**
- PR.AA-01: Issue unique identity per agent — A2A
  authentication bound to specific agent identity,
  not shared service account
- PR.DS-02: Enforce mutual TLS on all A2A channels —
  encryption and authentication in a single control,
  short-lived certificates, replay protection

**DETECT**
- DE.CM-01: Monitor all A2A communication — unusual
  sender identities, replayed messages, schema violations
  detected and alerted

**RESPOND**
- RS.MI-01: Contain A2A compromise — channel isolation,
  affected agent suspension, message log forensics

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 NHI-4/NHI-7 · AIUC-1 B007/B008 · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Single-point faults propagate through multi-agent workflows. CSF 2.0
infrastructure resilience (PR.IR) and recovery planning (RC.RP) are
the primary categories. In OT environments this is Critical severity.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Infrastructure Resilience | PR.IR-01 | PROTECT | Networks and environments protected for resilience — circuit breakers, blast radius limits, fail-safe defaults |
| Continuous Monitoring | DE.CM-01 | DETECT | Cascade indicators detected — correlated failure patterns across agent cluster monitored |
| Incident Mitigation | RS.MI-01 | RESPOND | Incidents contained — kill switch activated, process control fallback initiated |
| Incident Recovery | RC.RP-01 | RECOVER | Recovery plan includes agent cluster failures — BCP covers AI system availability, RTO/RPO defined |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-01: Include cascade risk in risk management strategy —
  define acceptable blast radius per deployment, document
  recovery time objectives for agent clusters

**PROTECT**
- PR.IR-01: Implement circuit breakers and blast radius
  limits as resilience measures — agent clusters segmented,
  inter-cluster propagation controlled

**DETECT**
- DE.CM-01: Monitor for cascade indicators — correlated
  anomalous agent actions detected before physical impact

**RESPOND**
- RS.MI-01: Cascade containment — kill switch activation,
  process control fallback, operator notification

**RECOVER**
- RC.RP-01: Recovery plan covers agent cluster failures —
  restart procedures, state validation, root cause
  investigation before reactivation

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6/7.7 (OT) · NIST SP 800-82 Rev 3

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents build false trust enabling manipulation of human approvers.
CSF 2.0 awareness training (PR.AT) and organisational context
(GV.OC-01) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Policy requires AI disclosure and advisory labelling — agent transparency as a governance requirement |
| Awareness and Training | PR.AT-01 | PROTECT | Users trained on AI limitations — operators understand agent advisory status and verification requirements |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for aggregate over-trust patterns — systematic operator acceptance without verification detected |
| Communication | RS.CO-03 | RESPOND | Information shared following incidents — trust exploitation incidents reported to affected users |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Policy requires AI disclosure in all
  agent-user interactions — EU AI Act Art. 50 compliance
  as a governance requirement, not just legal obligation

**PROTECT**
- PR.AT-01: Train all users of agent decision-support
  tools on AI limitations — verification requirements,
  how to identify AI output vs authoritative content
- Independent approval flows for sensitive actions —
  chat interface cannot be the consent mechanism

**DETECT**
- DE.CM-09: Monitor for aggregate over-trust patterns —
  systematic operator acceptance of agent recommendations
  without independent verification detected

**RESPOND**
- RS.CO-03: Report trust exploitation incidents —
  notify affected users, initiate retraining

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 C/F · ISA/IEC 62443 SR 2.3 (OT)

---

### ASI10 — Rogue Agents

**Severity:** Critical

Compromised agents pursue hidden goals while appearing compliant.
CSF 2.0 detection (DE.CM, DE.AE) is the most critical function —
without behavioural monitoring, rogue agents operate indefinitely.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for anomalous data and software use — behavioural baseline deviation detected |
| Adverse Event Analysis | DE.AE-02 | DETECT | Detected events analysed to understand attack targets — rogue agent patterns correlated across sessions |
| Incident Analysis | RS.AN-03 | RESPOND | Root cause analysis — what caused rogue behaviour, which sessions were affected, what was the blast radius |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions managed — rogue agent cannot exceed its permission envelope regardless of internal goal state |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Policy requires comprehensive audit logging
  of all agent actions — no production deployment
  without full observability

**IDENTIFY**
- ID.RA-01: Include rogue agent risk in risk assessment —
  detection capability, blast radius, response procedures
  documented per deployment

**PROTECT**
- PR.AA-05: Scope constraints enforced at infrastructure
  layer — rogue agent cannot exceed its permission
  envelope regardless of internal state

**DETECT**
- DE.CM-09: Continuous behavioural monitoring —
  establish baseline during commissioning, alert on
  deviation using tiered response
- DE.AE-02: Analyse patterns across sessions — systematic
  recommendation bias detected through aggregate analysis

**RESPOND**
- RS.AN-03: Rogue agent containment and investigation —
  kill switch activation, recommendation audit,
  process state validation, forensic capture
- RS.MI-01: Contain rogue agent — credentials revoked,
  actions reviewed, process state validated

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · EU AI Act Art. 14/15 · ISA/IEC 62443 SR 3.7 (OT)

---

## CSF 2.0 profile for agentic AI

| CSF Function | Priority entries | Key categories | Target state |
|---|---|---|---|
| GOVERN | ASI01, ASI02, ASI04 | GV.OC-01, GV.SC-01/06, GV.RM-01/06 | Autonomy policy published, supply chain programme live, risk register complete |
| IDENTIFY | ASI03, ASI04, ASI08 | ID.AM-08, ID.RA-01, ID.RA-08 | All agent NHIs inventoried, component SBOM maintained, cascade blast radius documented |
| PROTECT | ASI03, ASI05, ASI07 | PR.AA-01/05, PR.DS-01/02, PR.PS-04, PR.IR-01 | NHI governance live, A2A mTLS implemented, sandbox deployed |
| DETECT | ASI10, ASI06, ASI08 | DE.CM-01/09, DE.AE-02 | Behavioural baselines established, memory monitoring live, cascade detection operational |
| RESPOND | ASI01, ASI08, ASI10 | RS.AN-03, RS.MI-01 | Kill switch tested, incident response exercised for all ASI scenarios |
| RECOVER | ASI08 | RC.RP-01 | BCP covers agent cluster failures, RTO/RPO defined and tested |

---

## References

- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with CSF 2.0 profile | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
