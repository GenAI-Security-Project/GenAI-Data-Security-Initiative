<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : SOC 2 Type II — AICPA Trust Services Criteria
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × SOC 2

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [SOC 2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) —
the AICPA's System and Organization Controls 2 report framework,
based on the Trust Services Criteria (TSC).

---

## Why SOC 2 for agentic AI security

SOC 2 is the most widely required security assurance framework for
SaaS and cloud service providers in North America and increasingly
globally. For organisations offering agentic AI products or services,
SOC 2 is critical for three reasons specific to autonomy:

**Autonomous action scope:** Agentic systems take real-world actions —
deleting records, sending messages, placing orders, executing code.
SOC 2 CC5 (Control Activities) and CC6 (Logical Access) criteria
apply directly to the permission models that govern what actions
agents may take. Auditors assessing agentic systems will scrutinise
whether action scope is controlled and whether human confirmation
is required for irreversible operations.

**Processing integrity for autonomous outputs:** SOC 2 Processing
Integrity (PI) criteria — complete, accurate, and authorised
processing — extend to agent-generated actions and outputs. An agent
that executes an action based on a goal-hijacked prompt has failed
PI1 (authorised processing) regardless of whether the action was
technically correct.

**Supply chain and third-party risk:** Agentic systems are built
on stacks of third-party components — frameworks, model providers,
tool registries, plugin vendors. SOC 2 CC9 (Risk Mitigation) vendor
management criteria apply to the full agentic supply chain.

---

## SOC 2 Trust Services Criteria

| Category | Code | Scope |
|---|---|---|
| Security | CC (Common Criteria) | CC1–CC9: Control environment, risk assessment, access, monitoring |
| Availability | A | System availability and performance commitments |
| Processing Integrity | PI | Complete, accurate, valid, and authorised processing |
| Confidentiality | C | Protection of confidential information |
| Privacy | P | Personal information lifecycle management |

**Agentic AI SOC 2 audit focus:**
Auditors assessing agentic deployments will focus on: whether goal
hijack and tool misuse risks are identified in the risk programme
(CC3, CC9); whether agent permissions and actions are logged and
monitored (CC6, CC7); whether supply chain components are managed
through change management (CC8, CC9); and whether cascading failure
scenarios are covered by availability and incident response controls
(A1, CC7).

---

## SOC 2 criteria reference

| Criteria | Title | Agentic relevance |
|---|---|---|
| CC1 | Control environment | Agentic governance, policies, accountability |
| CC2 | Communication and information | Agentic risk communication, incident disclosure |
| CC3 | Risk assessment | Agentic risk identification — goal hijack, tool misuse, cascade failures |
| CC4 | Monitoring activities | Continuous monitoring of agentic controls |
| CC5 | Control activities | Agent action scope policies, procedures, controls |
| CC6 | Logical and physical access | Agent authentication, authorisation, credential management |
| CC7 | System operations | Agent monitoring, change detection, incident response |
| CC8 | Change management | Agent framework updates, model changes, tool changes |
| CC9 | Risk mitigation | Agent supply chain vendor risk, contractual controls |
| A1 | Availability | Multi-agent system availability and cascade failure resilience |
| PI1 | Processing integrity | Authorised, complete, and accurate agent action execution |
| C1–C2 | Confidentiality | Agent credential and confidential data protection |
| P1–P8 | Privacy | Personal information handled by agents |

---

## Quick-reference summary

| ID | Name | Severity | Primary SOC 2 Criteria | Tier |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | CC3, CC7, CC5, PI1 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | CC5, CC6, CC7, PI1 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | CC6, CC7, C1, P1 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | CC9, CC8, CC3, CC5 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | CC5, CC7, CC6, PI1 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | CC3, CC7, PI1, CC5 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | CC6, CC7, CC5, CC9 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | A1, CC7, CC3, CC5 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | CC5, CC3, PI1, P7 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | CC7, CC6, CC3, A1 | Hardening–Advanced |

---

## Audience tags

- **SaaS/cloud service provider** — full file, SOC 2 evidence mapping for agentic products
- **Security officer preparing for SOC 2 audit** — criteria-to-control mapping for agentic scope
- **SOC 2 auditor** — criteria applicability for agentic AI system assessment
- **CISO** — risk programme coverage gaps, criteria most likely to be findings
- **Engineer building agentic products** — CC5/CC6/CC7 control implementation entries

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through direct or indirect
instruction injection. This implicates SOC 2 Processing Integrity
(PI1 — authorised processing) because an agent executing a hijacked
goal is processing on behalf of an unauthorised principal, and
CC3/CC7 because the risk must be identified, treated, and monitored.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC3.2 | Goal hijack risk identified in risk assessment — prompt injection, indirect injection, multi-turn manipulation documented | Risk register with goal hijack entries, treatment status |
| CC7.2 | Runtime monitoring for goal-deviation indicators — AI-specific anomaly detection covering instruction-override patterns | Monitoring configuration, alert logs, incident records |
| CC5.2 | Control activities define acceptable agent actions — agent cannot deviate from authorised goal scope | Agent permission policy, goal-state verification design documentation |
| PI1.1 | Agent processing is authorised — actions taken by agent correspond to user's authorised intent, not attacker's injected instruction | Action audit log, authorisation records per agent session |

#### Mitigations

**Foundational**
- CC3: Document goal hijack in risk register — direct,
  indirect, and multi-turn injection scenarios with
  treatment controls and residual risk
- CC5: Define authorised action scope per agent role —
  policy document stating what agents may and may not do

**Hardening**
- CC7: Deploy runtime goal-state monitoring — detect
  deviation between session-start intent and in-progress
  agent actions before irreversible steps execute
- PI1: Implement authorised-action verification —
  log each agent action with the authorisation basis
  (session intent, user permission level) as PI evidence

**Advanced**
- CC7: Red team goal hijack scenarios — documented
  adversarial testing with results retained as CC7
  evidence of effective monitoring
- CC5: Implement goal-state verification middleware —
  technical control corroborating the CC5 policy

#### Crosswalk
- LLM Top 10: LLM01 Prompt Injection
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents invoke tools with destructive parameters or beyond authorised
scope. SOC 2 CC5 (Control Activities) requires policies defining
what tool invocations are permitted; CC6 (Logical Access) requires
that permissions enforce those policies; PI1 requires that all tool
invocations are authorised.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC5.2 | Control activities define tool permission scope — which tools are permitted, which parameters are valid, which actions require confirmation | Tool permission policy, permitted action allowlist |
| CC6.1 | Logical access controls enforce tool permissions — agent cannot invoke tools outside authorised scope | Tool invocation logs, access rejection records |
| CC7.2 | Monitoring for anomalous tool invocations — destructive parameters, out-of-scope tools, unexpected sequences detected | Tool call audit log, anomaly alert records |
| PI1.2 | Tool invocations are complete and accurate — parameter validation ensures tool calls match intended business operation | Validation configuration, rejected call logs |

#### Mitigations

**Foundational**
- CC5: Document tool permission policy — permitted
  tools, valid parameter ranges, and irreversible
  action confirmation requirements
- CC6: Enforce tool permissions technically — agent
  framework cannot dispatch out-of-scope tool calls

**Hardening**
- CC7: Log all tool invocations with parameters —
  alert on destructive parameter patterns, out-of-scope
  destinations, or unexpectedly high-frequency calls
- PI1: Implement parameter validation before execution —
  tool call parameters validated against defined ranges
  before dispatch; rejections logged

**Advanced**
- CC8: Treat tool registry changes as system changes —
  new tools or modified tool descriptors go through
  change management including security review

#### Crosswalk
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials that attackers exploit for
lateral movement. SOC 2 CC6 (Logical Access) covers the full
credential lifecycle; Confidentiality (C1–C2) covers credentials
as confidential assets; Privacy (P) applies wherever agent
credentials provide access to personal data.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC6.1 | Agent credentials managed as logical access assets — provisioning, scope, rotation, revocation per access management policy | Credential lifecycle records, provisioning logs |
| CC6.3 | Credentials revoked at session end — no persistent credential caching in agent memory after session terminates | Session termination logs, credential TTL configuration |
| CC7.3 | Credential usage monitored — anomalous scope expansion or after-session access detected | Credential audit log, anomaly alert records |
| C1.1 | Agent credentials treated as confidential information — stored in secrets manager, access-controlled | Secrets management configuration, access control evidence |

#### Mitigations

**Foundational**
- CC6: Provision agent credentials with documented
  scope and TTL — provisioning records retained as
  CC6 evidence; access management policy covers agents
- CC6: Revoke credentials at session end — technical
  enforcement of TTL, not relying on agent behaviour

**Hardening**
- CC7: Monitor all agent credential operations —
  access log covering all credential use, anomaly
  detection for unexpected scope or post-session access
- C1: Classify agent credentials as confidential —
  secrets manager storage, no plaintext credentials
  in environment variables, logs, or agent memory

**Advanced**
- CC6: Implement per-task ephemeral credentials —
  each task receives a fresh, scoped credential;
  credential reuse impossible after task completion
- CC7: Red team credential extraction — test whether
  credentials appear in agent outputs, logs, or
  tool payloads; retain results as CC7 test evidence

#### Crosswalk
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure

---

### ASI04 — Agentic Supply Chain

**Severity:** High

Agentic stacks depend on third-party frameworks, tools, model
weights, and plugins. SOC 2 CC9 (Risk Mitigation) covers vendor
risk management; CC8 covers change management for component updates.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC9.2 | Third-party agentic components assessed — agent frameworks, tool vendors, model providers subject to vendor risk management | Vendor assessments, contractual security obligations |
| CC8.1 | Component changes managed through change management — model updates, framework upgrades, tool changes require security review | Change management records, security review sign-offs |
| CC3.3 | Agentic supply chain risk included in risk assessment — compromised component scenarios documented with treatment | Risk register with supply chain entries |
| CC5.3 | Integrity checks required before component deployment — cryptographic verification of model weights and tool descriptors | Integrity verification configuration, deployment logs |

#### Mitigations

**Foundational**
- CC9: Maintain agentic component inventory and vendor
  register — every framework, tool vendor, and model
  provider listed with security assessment status
- CC8: Include agentic component updates in change
  management — security review required before any
  model, framework, or tool version change

**Hardening**
- CC9: Require contractual security obligations from
  all agentic component vendors — vulnerability
  disclosure SLA, security incident notification
- CC5: Implement integrity verification for deployed
  components — cryptographic hashes, signed artefacts

**Advanced**
- CC9: Annual vendor re-assessment for agentic
  components — vendors with material security posture
  changes flagged for immediate review

#### Crosswalk
- LLM Top 10: LLM03 Supply Chain Vulnerabilities

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents generate and execute code beyond authorised scope. SOC 2
CC5 requires controls on what code may be executed; CC6 controls
the execution environment access; CC7 monitors for out-of-scope
execution events; PI1 requires that code execution is authorised.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC5.2 | Control activities define permitted code execution scope — sandbox requirements, approved languages, forbidden operations | Code execution policy, sandbox configuration |
| CC6.1 | Execution sandboxes access-controlled — no host filesystem or network access without authorisation | Sandbox configuration, access control evidence |
| CC7.2 | Code execution events monitored — syscall patterns, network calls, and filesystem access from sandboxes logged | Execution audit log, alert configuration |
| PI1.1 | Code execution is authorised — agent cannot execute code that was not explicitly requested by authorised user | Code execution authorisation records |

#### Mitigations

**Foundational**
- CC5: Define code execution policy — permitted
  languages, sandbox requirements, prohibited
  operations (host filesystem, network egress)
- CC6: Enforce execution sandbox — containerised
  execution with no host access; network egress
  restricted to approved endpoints

**Hardening**
- CC7: Log all execution events — syscalls, network
  calls, filesystem operations logged with agent
  identity and session context
- PI1: Require explicit user authorisation for
  code execution — agent cannot execute generated
  code without user confirmation token

**Advanced**
- CC7: Red team sandbox escape — test container
  escape techniques; retain results as CC7 evidence

#### Crosswalk
- LLM Top 10: LLM05 Insecure Output Handling

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Attackers corrupt agent memory stores, context windows, or
conversation history. SOC 2 CC3 identifies this as an operational
risk; PI1 requires that agent processing based on poisoned context
is not treated as authorised; CC7 covers anomaly detection on
memory stores.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC3.3 | Memory poisoning risk documented in risk assessment — scenarios for RAG, persistent memory, and context window corruption | Risk register with memory poisoning entries |
| CC7.2 | Agent memory stores monitored for unexpected modifications — baseline established, deviations trigger alerts | Memory access log, anomaly alert configuration |
| PI1.1 | Processing based on compromised memory is not authorised — memory integrity controls support PI1 evidence | Integrity verification configuration |
| CC5.2 | Controls on memory store write access — only authorised processes may write to agent memory stores | Memory access policy, write access controls |

#### Mitigations

**Foundational**
- CC5: Restrict write access to agent memory stores —
  only the owning agent process may write; external
  writes require explicit authorisation
- CC3: Document memory poisoning scenarios in risk
  register — RAG corpus, persistent memory, context
  window; treatment controls documented

**Hardening**
- CC7: Establish memory integrity baseline and monitor
  for deviations — drift detection alerts for unexpected
  changes to persistent agent state
- PI1: Implement memory integrity verification —
  hash-based baseline for critical memory stores;
  changes logged with source identity

**Advanced**
- CC7: Test memory poisoning attack paths — adversarial
  content injection into memory stores; retain results
  as CC7 test evidence

#### Crosswalk
- LLM Top 10: LLM04 Data and Model Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning

---

### ASI07 — Insecure Inter-Agent Comms

**Severity:** High

Agents communicate without mutual authentication or message
integrity. SOC 2 CC6 covers authentication of inter-system
communication; CC5 defines the controls on what agents may
request of each other; CC7 covers monitoring of inter-agent
traffic.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC6.1 | Inter-agent authentication required — all agent-to-agent messages authenticated before acting | mTLS configuration, certificate management records |
| CC5.2 | Inter-agent communication policy — which agents may communicate with which, under what conditions, with what data | Inter-agent communication policy document |
| CC7.2 | Inter-agent traffic monitored — unexpected communication patterns, unauthorised agent requests detected | Inter-agent traffic logs, anomaly alert records |
| CC9.2 | Third-party agents treated as vendor risk — agents from external providers assessed before integration | Vendor assessment records for third-party agents |

#### Mitigations

**Foundational**
- CC5: Define inter-agent communication policy —
  approved agent pairs, permitted message types,
  data classification limits
- CC6: Require authentication for all inter-agent
  messages — certificates or tokens, not IP trust

**Hardening**
- CC7: Log all inter-agent communication — message
  source, destination, content summary, and action
  taken; alert on policy violations
- CC6: Implement message integrity verification —
  receiving agent validates message integrity before
  acting on it

**Advanced**
- CC7: Test inter-agent spoofing scenarios — verify
  agents reject unauthenticated messages; retain
  results as CC7 test evidence

#### Crosswalk
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Agent failures propagate through multi-agent systems causing
large-scale service disruption. SOC 2 Availability (A1) is the
primary criteria — service availability commitments must be met
even when individual agents fail. CC7 (System Operations) covers
failure detection and incident response.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| A1.1 | Availability commitments defined for multi-agent system — RTO/RPO documented; cascade failure scenarios in availability risk | Availability SLA, BCP documentation |
| A1.2 | Capacity and performance monitoring — early warning of cascade failure precursors (latency, error rate, queue depth) | Monitoring dashboards, alert configuration |
| CC7.3 | Cascade failure incidents detected and responded to — incident response procedures for multi-agent failures | IR plan covering cascade scenarios, incident records |
| CC3.3 | Cascade failure risk in risk assessment — blast radius analysis, dependency mapping documented | Risk register with cascade failure entries |

#### Mitigations

**Foundational**
- A1: Document availability commitments for multi-agent
  deployments — RTO/RPO per agent tier, cascade
  failure scenarios in BCP
- CC7: Implement early warning monitoring for cascade
  precursors — latency, error rate, and queue depth
  thresholds with alerting

**Hardening**
- A1: Implement circuit breakers — agent-to-agent
  calls circuit-break on failure threshold to prevent
  cascade propagation
- CC7: Include cascade failure in IR plan — activation
  procedure, isolation steps, recovery sequence documented

**Advanced**
- A1: Test cascade failure recovery — simulation
  of multi-agent failure scenarios; retain results
  as A1 availability evidence

#### Crosswalk
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents exploit human trust through deceptive outputs. SOC 2 CC5
(Control Activities) covers policies prohibiting deceptive design;
PI1 (Processing Integrity) requires that outputs are accurate and
complete; Privacy criteria (P7 — quality and accuracy) apply where
inaccurate AI outputs affect individuals.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC5.3 | AI disclosure policy — users informed when interacting with AI agents; deceptive design patterns prohibited | AI disclosure policy, UI evidence |
| CC3.3 | Trust exploitation risk in risk assessment — social engineering, impersonation, false urgency scenarios documented | Risk register with trust exploitation entries |
| PI1.3 | Agent outputs are accurate and complete — outputs not designed to mislead; factual accuracy controls for high-stakes outputs | Output quality controls, factual accuracy testing |
| P7.1 | Accuracy of personal data in AI outputs — privacy criteria require that AI-generated information about individuals is accurate | Accuracy review procedures |

#### Mitigations

**Foundational**
- CC5: Publish AI disclosure policy — users notified
  when interacting with agents; impersonation and
  false urgency prohibited
- CC3: Document trust exploitation risk — social
  engineering and impersonation scenarios in risk
  register with treatment controls

**Hardening**
- PI1: Implement output accuracy controls for
  high-stakes use cases — citation requirements,
  fact-checking for claims about individuals or entities
- P7: Review AI-generated outputs about individuals
  for accuracy — feedback mechanism for users to
  report inaccurate AI claims

#### Crosswalk
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning

---

### ASI10 — Rogue Agents

**Severity:** Critical

Agents operate outside authorised scope — executing unsanctioned
tasks or communicating with unapproved systems. SOC 2 CC7 (System
Operations) is the primary detection criteria; CC6 covers the
access controls that define authorised scope; Availability (A1)
is implicated when rogue agents consume resources that degrade
service for legitimate operations.

#### SOC 2 criteria mapping

| Criteria | How it applies | Evidence |
|---|---|---|
| CC7.2 | Continuous monitoring for rogue agent behaviour — actions outside authorised scope detected and alerted | Agent action audit log, anomaly alert records |
| CC6.1 | Access controls define authorised agent scope — technical enforcement of what agents may and may not do | Permission policy, access control configuration |
| CC3.3 | Rogue agent risk in risk assessment — autonomous agent operating outside scope is a documented risk | Risk register with rogue agent scenarios |
| A1.1 | Rogue agent impact on availability — resource consumption by rogue agents does not degrade service for authorised operations | Resource monitoring, quota enforcement records |

#### Mitigations

**Foundational**
- CC6: Define and enforce authorised agent scope —
  technical controls prevent actions outside defined
  role regardless of model instruction
- CC3: Document rogue agent risk — autonomous operation
  outside scope scenarios with treatment controls

**Hardening**
- CC7: Establish per-agent behavioural baseline —
  monitor for deviations from expected action patterns;
  alert on out-of-scope communications or unexpected
  resource consumption
- CC7: Include rogue agent containment in IR plan —
  automated isolation triggers and rollback procedures

**Advanced**
- CC7: Test rogue agent detection — simulate
  out-of-scope agent behaviour; verify detection
  triggers; retain results as CC7 test evidence

#### Crosswalk
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI03 Shadow AI & Unsanctioned Data Flows

---

## SOC 2 audit checklist for agentic AI

The following items are most likely to generate findings in a SOC 2
audit that includes agentic AI system scope:

| Criteria | Likely auditor question | What to prepare |
|---|---|---|
| CC3 | Is goal hijack in the risk register? | Risk register entries with treatment controls and residual risk |
| CC5 | Is there an agent permission policy? | Documented permitted tools, actions, and confirmation requirements |
| CC6 | Are agent credentials managed per access management policy? | Provisioning records, TTL configuration, revocation logs |
| CC7 | Are agent actions logged and monitored? | Audit log configuration, anomaly detection setup, alert records |
| CC8 | Do model and component updates go through change management? | Change records for model updates, framework upgrades, tool changes |
| CC9 | Are agentic component vendors assessed? | Vendor assessment records, contractual security obligations |
| A1 | Is multi-agent availability covered in BCP? | BCP documentation, cascade failure scenarios, recovery test results |
| PI1 | Are agent actions authorised and logged? | Authorisation records per session, action audit trail |

---

## Implementation priority

| Priority | ASI IDs | SOC 2 focus | Rationale |
|---|---|---|---|
| P1 — Critical | ASI01, ASI02, ASI03 | CC3, CC5, CC6, CC7 | Critical severity — most likely to be audit findings |
| P2 — High | ASI04, ASI05, ASI10 | CC8, CC9, CC6/CC7 | Supply chain, code execution, rogue agent scope |
| P3 — High | ASI06, ASI07, ASI08 | CC3/CC7, CC6, A1 | Memory, inter-agent, cascade — availability and integrity |
| P4 — Medium | ASI09 | CC5, PI1, P7 | Trust exploitation — policy and output quality controls |

---

## References

- [SOC 2 Trust Services Criteria](https://www.aicpa-cima.com/resources/landing/2017-trust-services-criteria)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [LLM_SOC2.md](../llm-top10/LLM_SOC2.md) — SOC 2 × LLM Top 10
- [DSGAI_SOC2.md](../dsgai-2026/DSGAI_SOC2.md) — SOC 2 × DSGAI 2026

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-27 | Initial release — full ASI01–ASI10 mapping to SOC 2 Trust Services Criteria |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the OWASP GenAI Data Security Initiative.
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
