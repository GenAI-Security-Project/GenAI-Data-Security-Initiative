<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : PCI DSS v4.0
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × PCI DSS v4.0

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/) —
the Payment Card Industry Data Security Standard, version 4.0,
mandatory from March 2025.

---

## Why PCI DSS for agentic AI security

PCI DSS applies to any organisation that stores, processes, or
transmits cardholder data (CHD). Agentic AI deployments introduce
new PCI scope risks that did not exist with static LLM deployments:

**Agents with tool access to payment systems** — an agent granted
tool access to payment APIs, CRM systems with CHD, or customer
service platforms with transaction history is in PCI scope. The
agent's memory, context window, and observability pipeline may
all contain CHD.

**Autonomous actions on payment data** — agents that can initiate
refunds, modify account data, or create payment records require
PCI Requirement 7 (least-privilege access) and Requirement 10
(audit logging) controls on agent identity and action scope.

**Supply chain for agentic components** — Requirement 12.8 vendor
management extends to agent framework providers, tool registry
operators, and model providers when their components process or
have access to CHD.

**PCI DSS v4.0 customised approach** — for novel agentic controls
that do not map to traditional PCI requirements, v4.0's customised
approach provides the mechanism to document AI-specific controls
as satisfying the intent of requirements through alternative means.

---

## PCI DSS v4.0 structure

| Requirement | Title | Agentic relevance |
|---|---|---|
| 1 | Network security controls | Agent infrastructure network segmentation |
| 2 | Secure configurations | Agent framework and model component hardening |
| 3 | Protect stored account data | CHD in agent memory, context, and tool responses |
| 4 | Protect cardholder data in transit | Agent API calls and tool invocations carrying CHD |
| 5 | Protect against malicious software | Agent component integrity, supply chain |
| 6 | Develop and maintain secure systems | Secure development for agentic integrations |
| 7 | Restrict access to cardholder data | Agent least-privilege for CHD access |
| 8 | Identify users and authenticate access | Agent identity, authentication, credential management |
| 9 | Restrict physical access | Physical controls for agentic infrastructure |
| 10 | Log and monitor all access | Agent audit logging, action monitoring |
| 11 | Test security systems | Agentic security testing — goal hijack, tool misuse |
| 12 | Support information security policies | Agentic risk management, vendor programme |

---

## Quick-reference summary

| ID | Name | Severity | Primary PCI DSS v4.0 Requirements | Tier |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | Req 6.2, Req 11.3, Req 10.2, Req 12.3 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | Req 7.2, Req 7.3, Req 10.2, Req 6.2 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | Req 8.2, Req 8.3, Req 7.2, Req 10.2 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | Req 12.8, Req 6.3, Req 5.2, Req 2.2 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | Req 6.2, Req 6.4, Req 11.3, Req 10.2 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | Req 3.4, Req 3.5, Req 6.5, Req 11.3 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | Req 4.2, Req 8.2, Req 10.2, Req 6.2 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | Req 10.7, Req 12.3, Req 1.3, Req 2.2 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | Req 12.6, Req 6.2, Req 10.2, Req 12.3 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | Req 7.2, Req 10.2, Req 11.3, Req 12.3 | Hardening–Advanced |

---

## Audience tags

- **PCI DSS QSA / ISA** — criteria applicability for agentic AI system scope assessment
- **CISO at payments organisation** — risk programme entries for agentic AI in PCI scope
- **Engineer building agents on payment platforms** — Req 7/8/10 implementation entries
- **Compliance officer** — v4.0 customised approach entries for novel agentic controls

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives to access, exfiltrate, or
modify CHD through goal hijack. If the agent has any tool access to
payment systems, a successful goal hijack is a potential CHD
compromise event with PCI breach notification consequences.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 6.2 | Bespoke agent code reviewed for injection resistance — all agent integration code includes prompt injection as a vulnerability category | Secure code review records, findings, remediation |
| Req 11.3 | Penetration testing covers goal hijack — agentic AI systems tested for prompt injection before production and annually | Pen test report with goal hijack test cases |
| Req 10.2 | Agent actions logged — all goal-relevant agent actions logged with user identity, session ID, and action detail | Audit log configuration, sample log entries |
| Req 12.3 | Targeted risk analysis documents goal hijack — likelihood, impact on CHD, treatment controls specified | Risk analysis for agentic AI in PCI scope |

#### Mitigations

**Foundational**
- Req 6.2: Include prompt injection in secure code
  review requirements for all agent integrations
- Req 12.3: Conduct targeted risk analysis for
  goal hijack impact on CHD — document likelihood,
  impact, and treatment controls

**Hardening**
- Req 11.3: Include goal hijack test cases in
  penetration testing — direct, indirect, and
  multi-turn injection against all agent input channels
- Req 10.2: Log all agent actions in PCI scope —
  user identity, session ID, action taken, data accessed

**Advanced**
- Req 6.2: Implement goal-state verification as
  a documented secure development control — technical
  control corroborating secure code review evidence

#### Crosswalk
- LLM Top 10: LLM01 Prompt Injection

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents invoke tools accessing payment systems with destructive
parameters or beyond authorised scope. Requirement 7 (least-privilege)
applies to all tool permissions; Requirement 10 requires logging
of all tool invocations on CHD systems.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 7.2 | Agent tool permissions follow least-privilege — agent can only access CHD systems required for defined function | Access control matrix for agent tools, privilege review records |
| Req 7.3 | Agent tool permissions reviewed periodically — unused tool permissions removed; review schedule documented | Periodic access review records |
| Req 10.2 | All tool invocations on CHD systems logged — tool name, parameters, data accessed, user/session identity | Tool invocation audit log |
| Req 6.2 | Tool parameter validation in agent code — LLM-generated tool parameters validated before execution | Code review records covering parameter validation |

#### Mitigations

**Foundational**
- Req 7.2: Apply least-privilege to all agent tool
  permissions — document required tools per agent role,
  grant only those tools
- Req 10.2: Log all tool invocations on CHD systems —
  required for PCI audit regardless of agent involvement

**Hardening**
- Req 7.3: Schedule periodic agent tool permission
  review — at minimum annually per PCI requirements
- Req 6.2: Include tool parameter validation in
  secure code review — reject out-of-range or
  unexpected parameters before tool dispatch

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials providing access to CHD.
PCI DSS Requirement 8 (authentication) and Requirement 7
(least-privilege) apply directly to agent identity management.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 8.2 | Agent accounts are system/application accounts — unique agent identity per deployment, no shared credentials | Account inventory, unique account evidence |
| Req 8.3 | Agent credential management — unique credentials, strong authentication where interactive, credential rotation schedule | Credential management policy, rotation records |
| Req 7.2 | Agent access to CHD follows need-to-know — access to cardholder data restricted to what agent function requires | Access control matrix, need-to-know justification |
| Req 10.2 | Agent credential usage logged — all authentication events for agent accounts in CHD scope logged | Authentication audit log |

#### Mitigations

**Foundational**
- Req 8.2: Assign unique identity to each agent
  deployment in PCI scope — no shared accounts,
  no human credentials used by agents
- Req 7.2: Restrict agent access to minimum CHD
  scope required — need-to-know justification
  documented for each access grant

**Hardening**
- Req 8.3: Implement credential rotation for agent
  accounts — rotation schedule documented and enforced
- Req 10.2: Log all agent authentication events —
  required PCI audit trail for accounts accessing CHD

---

### ASI04 — Agentic Supply Chain

**Severity:** High

Third-party agentic components (frameworks, model providers, tool
vendors) are in PCI supply chain scope when they process or access
CHD. Requirement 12.8 mandates vendor management for all third-party
service providers with access to CHD.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 12.8 | Agentic component vendors with CHD access managed as TPSPs — written agreements, annual confirmation of PCI compliance | TPSP list, written agreements, compliance confirmations |
| Req 6.3 | Agentic component CVEs in vulnerability management — ML libraries, agent frameworks, inference runtime dependencies scanned | Vulnerability scan results, patch records |
| Req 5.2 | Malicious software protection for agent components — integrity verification for model weights and plugin descriptors | Integrity check configuration, verification records |
| Req 2.2 | Secure baseline configuration for agentic infrastructure — hardening standards applied to agent deployment platforms | Hardening baseline documentation |

#### Mitigations

**Foundational**
- Req 12.8: List all agentic component vendors with
  potential CHD access — obtain written agreements
  and annual PCI compliance confirmation
- Req 6.3: Include agentic component libraries in
  vulnerability management — scan on schedule,
  patch within PCI-required timelines

**Hardening**
- Req 5.2: Verify integrity of model weights and
  plugin descriptors — cryptographic verification
  before deployment
- Req 2.2: Apply PCI hardening standards to agentic
  infrastructure — remove unnecessary services,
  apply secure baseline configurations

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents generate and execute code that accesses CHD systems or
network segments. Requirement 6.4 (public-facing application
protection) and Requirement 6.2 (secure development) apply;
Requirement 10.2 requires logging of code execution events.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 6.2 | Code generation and execution controls in secure development — agent cannot execute generated code without validation | Secure development policy covering code generation |
| Req 6.4 | Agent execution environments protected — WAF or equivalent for agent endpoints with code execution capability | WAF configuration, protection evidence |
| Req 11.3 | Code execution paths in penetration testing — test whether crafted inputs cause execution of out-of-scope code | Pen test report with code execution test cases |
| Req 10.2 | Code execution events logged — all agent-initiated execution with session identity and code summary | Code execution audit log |

#### Mitigations

**Foundational**
- Req 6.2: Require explicit authorisation for all
  code execution — agent cannot execute generated
  code without user confirmation
- Req 10.2: Log all code execution events — required
  for PCI audit trail in cardholder data environment

**Hardening**
- Req 6.4: Protect agent execution endpoints —
  WAF rules covering common code injection patterns
- Req 11.3: Include code execution test cases in
  annual penetration test scope

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

CHD in agent memory or context is corrupted or exfiltrated through
poisoning attacks. Requirement 3 (protect stored account data)
applies to CHD in agent memory; Requirement 3.4 requires truncation
or hashing of PAN data wherever it is stored.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 3.4 | PAN in agent memory protected — primary account numbers truncated or masked if stored in agent context or memory stores | Memory store review, PAN protection evidence |
| Req 3.5 | Agent memory encryption — CHD in persistent memory stores encrypted using strong cryptography | Encryption configuration, key management records |
| Req 6.5 | Model and memory changes managed — updates to agent memory stores treated as system changes requiring security review | Change management records |
| Req 11.3 | Memory poisoning in penetration test scope — test whether adversarial content in memory affects agent behaviour | Pen test report |

#### Mitigations

**Foundational**
- Req 3.4: Prevent storage of full PAN in agent
  memory or context — truncate or mask PAN before
  storage in any agent data store
- Req 3.5: Encrypt all CHD in agent persistent
  memory stores — strong cryptography, documented
  key management

**Hardening**
- Req 6.5: Include agent memory store updates
  in change management — security review required
  before any change to stores potentially containing CHD

---

### ASI07 — Insecure Inter-Agent Comms

**Severity:** High

CHD transmitted between agents without encryption or mutual
authentication. Requirement 4.2 requires strong cryptography
for CHD in transit; Requirement 8.2 requires authenticated
inter-agent communication.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 4.2 | CHD encrypted in transit between agents — all inter-agent communication carrying CHD uses TLS 1.2+ | TLS configuration, protocol verification |
| Req 8.2 | Inter-agent authentication — agents authenticate to each other before exchanging CHD | Certificate configuration, authentication evidence |
| Req 10.2 | Inter-agent CHD exchanges logged — source, destination, data classification, timestamp | Inter-agent communication audit log |
| Req 6.2 | Secure development requirements for inter-agent APIs — authentication and encryption requirements in design specifications | Design documentation, code review records |

#### Mitigations

**Foundational**
- Req 4.2: Enforce TLS 1.2+ on all inter-agent
  communication in PCI scope — no plaintext CHD
  transmission between agents
- Req 8.2: Implement mutual authentication for
  inter-agent communication — certificates or tokens,
  not IP-based trust

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Multi-agent failures cause unavailability of payment services.
PCI DSS Requirement 10.7 requires detection of critical control
failures; Requirement 12.3 requires targeted risk analysis for
system availability risks.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 10.7 | Critical agent control failures detected promptly — monitoring for cascade precursors with alert thresholds | Monitoring configuration, alert records, detection evidence |
| Req 12.3 | Cascade failure risk analysis — targeted risk analysis documents cascade failure likelihood, impact, treatment | Risk analysis documentation |
| Req 1.3 | Network controls prevent cascade propagation — agent network segments isolated to contain blast radius | Network diagram, segmentation evidence |
| Req 2.2 | Baseline availability configuration for agent infrastructure — capacity and resilience requirements in hardening baseline | Hardening baseline documentation |

#### Mitigations

**Foundational**
- Req 10.7: Configure monitoring for cascade failure
  early warning indicators — latency, error rate, and
  queue depth alerts before full service impact
- Req 12.3: Conduct targeted risk analysis for
  cascade failure in PCI scope — document treatment
  controls including circuit breakers

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents deceive payment service users into taking harmful actions.
Requirement 12.6 (security awareness) requires training on AI
deception risks; Requirement 6.2 covers secure development
requirements for honest agent interaction design.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 12.6 | Security awareness covers AI deception — staff trained to recognise AI impersonation and social engineering | Training curriculum, completion records |
| Req 6.2 | Honest design requirements for agent interactions — AI disclosure requirements in secure development policy | Secure development policy, design review records |
| Req 10.2 | Agent-human interaction events logged — session records for agent interactions involving CHD decisions | Interaction audit log |
| Req 12.3 | Trust exploitation risk analysis — targeted risk analysis documents scenarios and treatment | Risk analysis documentation |

---

### ASI10 — Rogue Agents

**Severity:** Critical

Agents operate outside authorised scope — accessing CHD systems
not in their defined role. Requirement 7 (least-privilege) and
Requirement 10 (monitoring) are primary; Requirement 11.3
(penetration testing) requires testing for rogue agent behaviour.

#### PCI DSS v4.0 mapping

| Requirement | How it applies | Evidence |
|---|---|---|
| Req 7.2 | Agent access to CHD follows documented scope — technical controls prevent access outside defined role | Access control matrix, technical enforcement evidence |
| Req 10.2 | Rogue agent behaviour logged — actions outside defined scope generate audit log entries and alerts | Action audit log, out-of-scope alert records |
| Req 11.3 | Rogue agent scenarios in penetration test scope — test whether agents can operate outside authorised scope | Pen test report with rogue agent test cases |
| Req 12.3 | Rogue agent risk analysis — targeted risk analysis documents scenarios, CHD impact, treatment | Risk analysis documentation |

#### Mitigations

**Foundational**
- Req 7.2: Enforce agent scope technically —
  access controls prevent CHD access outside
  defined agent role
- Req 10.2: Alert on out-of-scope agent actions —
  required PCI monitoring for CHD systems

**Hardening**
- Req 11.3: Include rogue agent test cases in
  annual penetration test — verify scope enforcement
  cannot be bypassed

---

## PCI DSS v4.0 agentic AI evidence checklist

| Requirement | Evidence required for agentic AI in scope |
|---|---|
| Req 6.2 | Secure code review records covering goal hijack, tool misuse, code execution for all agent integration code |
| Req 7.2 | Access control matrix for all agent tool and CHD system access with need-to-know justification |
| Req 8.2 | Unique agent account inventory, credential management policy, rotation records |
| Req 10.2 | Audit log configuration covering all agent actions on CHD systems; sample log extracts |
| Req 11.3 | Penetration test report with agentic test cases: goal hijack, tool misuse, rogue agent, code execution |
| Req 12.3 | Targeted risk analysis for each agentic AI risk in PCI scope |
| Req 12.8 | TPSP list including agentic component vendors; written agreements; annual compliance confirmations |

---

## References

- [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [LLM_PCIDSS.md](../llm-top10/LLM_PCIDSS.md) — PCI DSS × LLM Top 10
- [DSGAI_PCIDSS.md](../dsgai-2026/DSGAI_PCIDSS.md) — PCI DSS × DSGAI 2026

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-27 | Initial release — full ASI01–ASI10 mapping to PCI DSS v4.0 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the OWASP GenAI Data Security Initiative.
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
