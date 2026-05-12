<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : OWASP Application Security Verification Standard (ASVS) 4.0.3
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × OWASP ASVS 4.0.3

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [OWASP Application Security Verification Standard (ASVS) 4.0.3](https://owasp.org/www-project-application-security-verification-standard/) —
the framework for testing and verifying web application and API
security, organised into 14 chapters with three verification levels.

---

## ASVS and agentic AI

Agentic systems are web applications and APIs with additional attack
surfaces. Every standard ASVS control applies — plus several chapters
become dramatically more important than they are for conventional
applications:

**V5 — Validation, Sanitisation and Encoding** is the most critical
chapter for agentic AI. Prompt injection is an injection vulnerability
(CWE-74) — the same category ASVS V5 addresses for SQL, OS commands,
and LDAP. The same input validation principles apply.

**V4 — Access Control** governs tool permissions. An agent that can
invoke a tool with arbitrary parameters under a shared high-privilege
account is a V4.1.3 (least privilege) violation.

**V11 — Business Logic** is critical for agentic AI — goal hijack,
excessive agency, and cascading failures are all business logic abuse
scenarios that V11 directly addresses.

**V13 — API and Web Service** covers all LLM API endpoints and
agent orchestration APIs — rate limiting, authentication, output
validation, and replay protection.

**Verification levels:**
- L1 — Opportunistic: passively verifiable, minimal security requirement
- L2 — Standard: most applications with sensitive data
- L3 — Advanced: high-value targets, high assurance required

---

## Quick-reference summary

| ID | Name | Severity | Primary ASVS Chapters / Requirements | Level | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | V5.1, V5.2, V11.1, V1.1 | L1–L3 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | V4.1, V11.1, V13.1, V7.2 | L1–L3 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | V2.1, V4.1, V6.1, V7.2 | L1–L3 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | V10.2, V14.2, V1.1 | L2–L3 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | V5.2, V5.3, V11.1, V13.1 | L1–L3 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | V5.1, V4.1, V6.1, V12.1 | L2–L3 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | V9.1, V3.3, V4.1, V7.2 | L1–L3 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | V11.1, V13.1, V7.4, V1.1 | L1–L3 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | V11.1, V5.2, V7.4, V13.1 | L1–L2 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | V7.2, V11.1, V4.1, V13.1 | L2–L3 | Hardening–Advanced |

---

## Audience tags

- **Developer** — full file, specific ASVS requirements to implement
- **Security architect** — V1 architecture, V11 business logic entries
- **Penetration tester** — verification requirements per level for test planning
- **Security engineer** — V4 access control, V5 validation, V13 API security
- **Auditor** — ASVS level mapping for assurance assessment
- **OT engineer** — ASI01, ASI02, ASI08 with ISA 62443 crosswalk

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through direct or indirect
instruction injection. ASVS Chapter V5 (Validation, Sanitisation and
Encoding) is the primary chapter — prompt injection is an injection
vulnerability class fully covered by V5.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify all user input validated against allowlist | V5.1.1 | L1 | All inputs to agents validated — indirect injection through processed content equally in scope |
| Verify output encoding prevents injection | V5.2.1 | L1 | Agent responses encoded before passing to downstream renderers — outputs treated as untrusted |
| Verify application protects against OS command injection | V5.2.5 | L1 | Agent-generated instructions not executed in system context without validation |
| Threat modelling of all data flows | V1.1.2 | L2 | All agent input sources threat-modelled — every indirect injection path documented |
| Verify business logic limits prevent function abuse | V11.1.2 | L2 | Business logic controls prevent injection from redirecting agent goal |

#### Mitigations by tier

**Foundational (L1)**
- V5.1.1: Input validation on all agent input channels —
  user prompt, RAG content, tool returns, email, uploaded
  documents all validated as untrusted content
- V5.2.1: Output encoding before passing to downstream
  systems — agent outputs treated as untrusted input
- Kill switch implementation — V11 business logic
  control enabling immediate halt of agent activity

**Hardening (L2)**
- V1.1.2: Threat model all agent data flows — every
  indirect injection surface identified and documented,
  mitigations verified in security testing
- V11.1.2: Business logic controls prevent goal redirection —
  goal-state verification implemented, deviation
  triggers suspension rather than continuation

**Advanced (L3)**
- V5.1.1: Validate all content sources for each specific
  deployment — historian data (OT), email content,
  web results each treated as injection vectors
- V11.1.2: Adversarial goal hijack testing as L3
  verification — multi-turn and indirect scenarios
  verified against your specific agentic deployment

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · AIUC-1 B001/B005 · CWE-74

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools via prompt manipulation or unsafe
delegation. ASVS Chapter V4 (Access Control) governs tool permissions —
least privilege (V4.1.3) applies to every agent tool integration.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify access control enforces least privilege | V4.1.3 | L1 | Agent tool access scoped to minimum required operations — read-only by default, write access formally approved |
| Verify all sensitive functions have access control | V4.1.1 | L1 | All destructive tool operations require explicit authorisation — not inheritable from agent session |
| Verify all business logic decisions logged | V7.2.2 | L2 | All tool invocations logged — tool identity, parameters, agent session, timestamp |
| Verify business logic abuse scenarios identified | V11.1.2 | L2 | Tool chain exploitation scenarios identified in threat model — mitigations implemented and verified |
| Verify API rate limiting | V13.1.1 | L1 | Tool API endpoints rate-limited — anomalous invocation frequency detected |

#### Mitigations by tier

**Foundational (L1)**
- V4.1.3: Least privilege on all agent tool integrations —
  per-tool permission manifests enforced at orchestration
  layer, not just policy
- V4.1.1: Access controls on all destructive tool
  operations — irreversible tools require human
  confirmation, enforced independently of agent framework
- V13.1.1: Rate limiting on all tool API endpoints —
  anomalous frequency detected and alerted

**Hardening (L2)**
- V7.2.2: Log all tool invocations — tool identity,
  parameters, agent identity, timestamp — immutable
  audit trail for forensic investigation
- V11.1.2: Identify and document tool chain exploitation
  scenarios — combinations of legitimate tool calls
  producing harmful outcomes verified in testing

**Advanced (L3)**
- V4.1.3: Include agent tool permissions in privileged
  access reviews — quarterly, unused permissions removed
- V11.1.2: Adversarial tool chain testing at L3 —
  attempt harm through legitimate tool sequences in
  your specific deployment

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: ISO 27001 A.8.2 · AIUC-1 B006/B007 · CWE-284

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials exploited for lateral movement.
ASVS Chapter V2 (Authentication) and V4 (Access Control) govern
agent credential management.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify credentials not in source code | V2.1.1 | L1 | Agent credentials not hardcoded — secret manager required |
| Verify access control enforces least privilege | V4.1.3 | L1 | Agent credential scope minimum required — no over-privileged NHIs |
| Verify sensitive data encrypted at rest | V6.1.1 | L2 | Agent credentials encrypted at rest — no cleartext in config or agent memory |
| Verify access control decisions logged | V7.2.1 | L2 | All credential usage logged — issuance, access, expiry detectable |
| Verify secrets not in source code | V14.2.3 | L2 | Agent credentials not committed to source control |

#### Mitigations by tier

**Foundational (L1)**
- V2.1.1: No hardcoded agent credentials — secret
  manager required for all agent credential storage
- V4.1.3: Least privilege on all agent credentials —
  minimum scope per agent role, short TTL, JIT issuance
- Unique credential per agent deployment — no shared
  NHIs across agent instances

**Hardening (L2)**
- V6.1.1: Encrypt all agent credentials at rest —
  same cryptographic standards as production data
- V7.2.1: Log all credential operations — issuance,
  use, expiry, anomalous patterns detectable
- V14.2.3: Agent credentials never in source code —
  enforce as CI/CD gate

**Advanced (L3)**
- PKI-backed agent identities as L3 credential control —
  certificate-based authentication for all agent-to-system
  connections
- V4.1.3: Quarterly privileged access review includes
  all agent NHIs — documented as L3 assurance evidence

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 (all entries) · ISO 27001 A.8.2/A.5.16 · CWE-522

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Compromised tools, MCP servers, or model components alter agent
behaviour. ASVS Chapter V10 (Malicious Code) and V14 (Configuration)
govern agent components as software supply chain elements.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify third-party components current and free of vulnerabilities | V10.2.1 | L2 | All agent component libraries scanned for CVEs — ML SBOM maintained and monitored |
| Verify only minimal approved external libraries | V10.2.2 | L2 | Approved component list — unsigned or unverified agent components rejected |
| Verify build pipelines include security checks | V14.2.2 | L2 | CI/CD pipeline for agent components includes integrity verification and CVE scanning |
| Verify threat model covers all data flows | V1.1.2 | L2 | Supply chain threat model documents all agent component sources and trust levels |

#### Mitigations by tier

**Foundational (L1)**
- Maintain ML SBOM for all agentic deployments —
  every component inventoried with version, source, hash
- Pin all component versions — no automatic updates
  without review

**Hardening (L2)**
- V10.2.1: CVE scanning in CI/CD for all agent components —
  ML libraries, MCP server dependencies, inference
  runtime all scanned before deployment
- V10.2.2: Approved component list enforced — only
  sourced from approved vendors, cryptographic signatures
  verified before loading any component
- V14.2.2: Build pipeline includes agent component
  integrity checks — unsigned components blocked

**Advanced (L3)**
- Operate isolated evaluation environment — behavioural
  testing of each component before production promotion
- V10.2.1: Runtime integrity monitoring — hash
  verification of loaded components, deviation triggers
  suspension

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: ISO 27001 A.5.19/A.5.21 · NIST CSF 2.0 GV.SC-01 · CWE-494

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate and execute code become RCE gateways. ASVS V5
(Validation) and V5.2 (Output Handling) are the primary chapters —
agent-generated code is untrusted output that must never be executed
without validation.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify output encoding of untrusted data in HTML context | V5.2.1 | L1 | Agent code output encoded before rendering in any context |
| Verify application does not use eval or dynamic code | V5.2.4 | L1 | No eval or exec of agent-generated code — absolute prohibition enforced in code review |
| Verify output encoding in OS command context | V5.2.5 | L1 | Agent-generated commands validated before any shell execution |
| Verify output encoding in SQL context | V5.3.5 | L1 | No raw agent output in SQL context — parameterised execution only |
| Verify business logic limits | V11.1.2 | L2 | Code execution capability in agents subject to business logic controls — sandbox, allowlist, static analysis |

#### Mitigations by tier

**Foundational (L1)**
- V5.2.4: Never use eval, exec, or equivalent on
  agent-generated code — absolute L1 requirement,
  enforced through automated code review
- V5.2.5: No raw agent output in shell context —
  validated against allowlist before any execution
- V5.3.5: No raw agent output in SQL context —
  parameterised execution only, no string interpolation

**Hardening (L2)**
- V11.1.2: Business logic controls for code execution —
  sandbox, network isolation, and allowlist as L2
  verification requirements for agentic code execution
- Static analysis of agent-generated code before
  execution — V5 input validation principle applied
  to code as output

**Advanced (L3)**
- Hardware-level sandboxing as L3 assurance control —
  kernel-level isolation preventing escape to host
- V5.2.4: Adversarial code injection testing at L3 —
  attempt RCE through crafted inputs against specific
  deployment, verify sandbox containment

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISO 27001 A.8.28

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent memory poisoning causes systematic incorrect behaviour.
ASVS V5.1 (input validation) and V4.1 (access control) govern
memory write paths as input boundaries requiring validation and
access control.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify all user input validated against allowlist | V5.1.1 | L1 | All content entering agent memory validated — injection patterns rejected at write boundary |
| Verify access control enforces least privilege | V4.1.3 | L1 | Memory write access restricted to minimum required sources — only agent and authorised administrators can write |
| Verify sensitive data encrypted at rest | V6.1.1 | L2 | Agent memory stores encrypted at rest — embeddings, long-term memory |
| Verify file upload malware scanning | V12.1.1 | L2 | Content entering agent memory scanned — adversarial content, injection patterns detected before write |

#### Mitigations by tier

**Foundational (L1)**
- V5.1.1: Validate all content before writing to agent
  memory — injection patterns rejected at write boundary,
  untrusted sources cannot bypass validation
- V4.1.3: Least privilege on memory write access —
  only agent and designated administrators can write,
  no unauthenticated memory writes

**Hardening (L2)**
- V6.1.1: Encrypt all agent memory stores at rest —
  embeddings, long-term memory, operational knowledge
- V12.1.1: Scan content before memory write — adversarial
  patterns, credential content detected before ingestion
- TTL enforcement on memory entries — V12 file resource
  management principle applied to memory store content

**Advanced (L3)**
- Cryptographic integrity verification on memory store —
  tamper detection as L3 assurance control
- V5.1.1: Adversarial memory poisoning testing at L3 —
  injection paths via each content source tested,
  detection capability verified

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3/A.8.24 · NIST AI RMF MS-2.5 · CWE-349

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

A2A channels lacking authentication enable agent-in-the-middle attacks.
ASVS Chapter V9 (Communication) and V3 (Session Management) govern
A2A communication as API communication requiring encryption and
session integrity.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify TLS used for all client connectivity | V9.1.1 | L1 | All A2A communication encrypted — mutual TLS, no cleartext inter-agent messages |
| Verify anti-replay tokens in state-changing operations | V3.3.1 | L1 | Replay protection on all A2A messages — nonces, timestamps, sequence numbers |
| Verify access control enforces identity | V4.1.3 | L1 | A2A channels enforce sender identity — unauthenticated messages rejected |
| Verify all security controls logged | V7.2.1 | L2 | All A2A messages logged — sender identity, content hash, schema validation results |

#### Mitigations by tier

**Foundational (L1)**
- V9.1.1: Enforce mutual TLS on all A2A channels —
  both parties authenticate, messages encrypted, L1
  requirement for all production A2A communication
- V3.3.1: Replay protection on all A2A messages —
  nonces, timestamps, sequence numbers enforced
- V4.1.3: A2A channels enforce sender identity —
  unauthenticated messages rejected at the channel layer

**Hardening (L2)**
- V7.2.1: Log all A2A messages — sender identity,
  content hash, timestamp — immutable audit trail
- Schema validation on all A2A message payloads —
  reject malformed or unexpected structures

**Advanced (L3)**
- PKI-backed agent identities for A2A — short-lived
  certificates, hardware-backed keys as L3 assurance
- V9.1.1: A2A channel security in penetration testing
  at L3 — spoofing, replay, schema violations tested

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 NHI-4/NHI-7 · ISO 27001 A.8.20/A.8.24 · CWE-287

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Single-point faults propagate through multi-agent workflows. ASVS
Chapter V11 (Business Logic) and V13 (API and Web Service) govern
cascade prevention as business logic abuse and API resilience.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify business logic assumptions documented | V11.1.1 | L2 | Cascade blast radius documented as business logic assumption — maximum affected systems formally accepted |
| Verify business logic limits prevent abuse | V11.1.2 | L2 | Circuit breakers as business logic controls — cascade propagation limited by design |
| Verify API rate limiting | V13.1.1 | L1 | Rate limiting on all agent API endpoints — cascade amplification through API exhaustion limited |
| Verify error handling does not expose sensitive data | V7.4.1 | L1 | Cascade errors handled gracefully — no sensitive system information in error responses |

#### Mitigations by tier

**Foundational (L1)**
- V13.1.1: Rate limiting on all agent API endpoints —
  cascade amplification through API saturation limited
- V7.4.1: Cascade errors handled gracefully — explicit
  unavailability notice to operators, no silent failure
- Kill switch implementation — V11 business logic
  control enabling immediate halt of agent cluster

**Hardening (L2)**
- V11.1.1: Document cascade blast radius as business
  logic assumption — maximum affected systems formally
  defined and accepted before multi-agent deployment
- V11.1.2: Circuit breakers as business logic controls —
  cascade propagation limited at each agent-to-agent
  boundary

**Advanced (L3)**
- V11.1.2: Chaos engineering as L3 business logic
  verification — intentional failure injection verifies
  circuit breaker effectiveness
- V13.1.1: Adversarial load testing at L3 — verify
  rate limiting holds under cascade amplification

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISO 27001 A.5.30 · ISA/IEC 62443 SR 7.6/7.7 (OT) · CWE-400

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents build false trust enabling manipulation of human approvers.
ASVS V11 (Business Logic) addresses trust exploitation as a business
logic abuse scenario where the AI system manipulates the human
decision-making process.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify business logic assumptions documented | V11.1.1 | L2 | AI advisory limitations documented as business logic assumptions — verification requirements per domain |
| Verify outputs encoded before rendering | V5.2.1 | L1 | Agent advisory outputs clearly labelled — users cannot mistake AI output for authoritative content |
| Verify all security controls logged | V7.4.1 | L1 | Agent-influenced operator decisions logged — aggregate patterns detectable |
| Verify API rejects large unexpected payloads | V13.1.3 | L1 | Approval flows independent of agent interface — no state-changing approvals via agent chat |

#### Mitigations by tier

**Foundational (L1)**
- V5.2.1: Label all agent advisory output — clear visual
  distinction from authoritative content in all rendering
  contexts, enforced at rendering layer not in response
- V7.4.1: Log all agent-influenced decisions — aggregate
  over-trust patterns detectable through log analysis
- V13.1.3: Approval flows independent of agent interface —
  sensitive state changes cannot be approved via agent
  chat, separate confirmation system required

**Hardening (L2)**
- V11.1.1: Document AI advisory limitations as business
  logic assumptions — which domains require verification,
  what constitutes an authoritative source vs AI advisory
- Safety alarm independence — agents cannot acknowledge
  or suppress safety alarms, enforced as V11 business
  logic control (OT)

**Advanced (L3)**
- V11.1.2: Trust exploitation in penetration testing
  at L3 — test operator susceptibility to manipulated
  recommendations in your specific deployment
- Operator competency verification as L3 assurance —
  operators demonstrate ability to identify AI advisory
  vs authoritative content

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · ISO 27001 A.6.3 · AIUC-1 C/F

---

### ASI10 — Rogue Agents

**Severity:** Critical

Compromised agents pursue hidden goals while appearing compliant.
ASVS V7 (Error Handling and Logging) is the primary chapter —
comprehensive logging is the foundational rogue agent control.
Without complete audit trails, rogue behaviour cannot be detected.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify access control decisions logged | V7.2.1 | L2 | All agent actions logged — no production deployment without complete observability |
| Verify all business logic decisions logged | V7.2.2 | L2 | All agent tool invocations and recommendations logged — systematic bias detectable through aggregate analysis |
| Verify business logic limits prevent abuse | V11.1.2 | L2 | Scope constraints as business logic controls — rogue agent cannot exceed permission envelope |
| Verify API rate limiting | V13.1.1 | L1 | Rate limiting prevents rogue agent from amplifying impact through API exhaustion |

#### Mitigations by tier

**Foundational (L1)**
- V13.1.1: Rate limiting on all agent API endpoints —
  rogue agent cannot amplify impact through excessive
  tool invocations
- Scope constraints enforced at orchestration layer —
  V11 business logic control, rogue agent cannot exceed
  its permission envelope

**Hardening (L2)**
- V7.2.1: Complete audit logging of all agent actions —
  no production deployment without full observability,
  L2 verification requirement
- V7.2.2: All tool invocations and recommendations
  logged — systematic bias detectable through aggregate
  analysis across sessions
- V11.1.2: Behavioural baseline as business logic
  control — deviation from baseline triggers tiered
  response as documented business logic behaviour

**Advanced (L3)**
- V7.2.2: Rogue agent red team at L3 — simulate
  persistent hidden goal pursuit, verify detection
  capability via aggregate log analysis, document
  maximum dwell time before detection
- V11.1.2: Multi-agent consensus for high-stakes
  decisions — rogue single agent cannot influence
  critical outcomes without cross-validation

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: ISO 27001 A.8.16/A.8.15 · AIUC-1 B001/B002/C/E · CWE-284

---

## ASVS verification checklist for agentic AI

### L1 — Baseline (all agentic deployments)

- [ ] V5.1.1: Input validation on all agent input channels
- [ ] V5.2.1: Advisory labels on all agent outputs — rendering layer enforcement
- [ ] V5.2.4: No eval or exec of agent-generated code
- [ ] V5.2.5: No raw agent output in shell context
- [ ] V5.3.5: No raw agent output in SQL context
- [ ] V4.1.1/V4.1.3: Least privilege on all agent tool and credential access
- [ ] V2.1.1: No hardcoded agent credentials
- [ ] V9.1.1: All A2A communication encrypted (mutual TLS)
- [ ] V3.3.1: Replay protection on all A2A messages
- [ ] V13.1.1: Rate limiting on all agent API endpoints
- [ ] V7.4.1: Cascade errors handled gracefully

### L2 — Standard (deployments with sensitive data or autonomous action)

- [ ] V1.1.2: All agent data flows threat-modelled
- [ ] V6.1.1: All agent credentials and memory stores encrypted at rest
- [ ] V7.2.1: All agent access control decisions logged
- [ ] V7.2.2: All agent tool invocations and recommendations logged
- [ ] V10.2.1: Agent component CVEs in vulnerability management
- [ ] V10.2.2: Approved component list enforced
- [ ] V11.1.1: Cascade blast radius and AI advisory limitations documented
- [ ] V11.1.2: Circuit breakers and scope constraints as business logic controls
- [ ] V14.2.2: Build pipeline includes agent component integrity checks
- [ ] V14.2.3: Agent credentials not in source code

### L3 — Advanced (high-assurance, high-consequence deployments)

- [ ] Adversarial goal hijack testing covering all indirect injection surfaces
- [ ] Adversarial tool chain exploitation testing
- [ ] Sandbox escape testing for code execution agents
- [ ] A2A security penetration testing — spoofing, replay, schema
- [ ] Cascade resilience under adversarial load
- [ ] Rogue agent detection red team — aggregate log analysis verification
- [ ] Supply chain integrity testing — compromised component detection

---

## Implementation priority by ASVS level

| Phase | ASI entries | ASVS level | Priority requirements |
|---|---|---|---|
| 1 — L1 baseline | ASI01, ASI02, ASI05, ASI08 | L1 | V5.1.1, V4.1.3, V5.2.4, V13.1.1 |
| 2 — L1 complete | ASI03, ASI07, ASI09 | L1 | V2.1.1, V9.1.1, V3.3.1, V5.2.1 |
| 3 — L2 standard | ASI04, ASI06, ASI10 | L2 | V10.2.1, V7.2.1/V7.2.2, V6.1.1 |
| 4 — L2 complete | ASI08, ASI09 | L2 | V11.1.1, V11.1.2 |
| 5 — L3 advanced | All | L3 | Adversarial testing, red team, chaos engineering |

---

## References

- [OWASP ASVS 4.0.3](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP ASVS GitHub](https://github.com/OWASP/ASVS)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with L1/L2/L3 verification requirements | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
