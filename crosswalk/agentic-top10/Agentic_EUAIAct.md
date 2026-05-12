<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : EU Artificial Intelligence Act (EU AI Act) — Regulation EU 2024/1689
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × EU AI Act

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [EU Artificial Intelligence Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
(Regulation EU 2024/1689).

Agentic AI systems introduce the highest-risk EU AI Act compliance
surface because autonomy, tool use, and multi-agent orchestration
directly engage the Act's most demanding obligations:

- **Article 14** (human oversight) is existentially relevant to
  agentic AI — agents that execute actions autonomously without
  human confirmation are the precise scenario Article 14 was
  written to govern
- **Article 15** (robustness and cybersecurity) applies to every
  ASI entry — agentic systems must be resilient against adversarial
  manipulation, goal hijack, and cascading failures
- **Article 9** (risk management) must cover the full agentic
  risk surface — tool access, A2A communication, memory stores,
  supply chain, and cascade paths

**Compliance deadline reminder:** August 2, 2026 — high-risk AI
system obligations apply. This is 4 months away. Agentic AI systems
deployed in high-risk categories (Annex III) must have conformity
assessment completed, quality management system operational, and
human oversight implemented and tested.

---

## Quick-reference summary

| ID | Name | Severity | Primary EU AI Act Articles | Applies to | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | Art. 9, Art. 14, Art. 15 | High-risk · GPAI systemic | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | Art. 9, Art. 14, Art. 15 | High-risk · GPAI | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | Art. 9, Art. 17, Art. 25 | High-risk · GPAI | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | Art. 10, Art. 15, Art. 17 | High-risk · GPAI | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | Art. 9, Art. 15, Art. 17 | High-risk · GPAI | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | Art. 9, Art. 14, Art. 15 | High-risk · GPAI | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | Art. 13, Art. 14, Art. 50 | All tiers | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | Art. 9, Art. 14, Art. 15, Art. 17 | High-risk · GPAI systemic | Hardening–Advanced |

---

## Audience tags

- **CISO / governance** — full file, EU AI Act compliance for agentic deployments
- **Legal / compliance officer** — articles mapping, fines exposure per entry
- **DPO** — ASI03, ASI06 GDPR intersection entries
- **Security engineer** — Art. 15 robustness entries
- **AI/ML engineer** — Art. 10 data governance, Art. 15 technical requirements
- **Auditor** — Art. 17 quality management, conformity assessment evidence
- **OT engineer** — ASI01, ASI02, ASI08 critical infrastructure provisions

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical
**Applies to:** High-risk · GPAI models with systemic risk

An attacker redirects agent objectives through direct or indirect
instruction injection. Article 14 is the most directly applicable
article — an agent whose goals have been hijacked and executes a
multi-step attack chain autonomously is a textbook Article 14 human
oversight failure. Article 15 mandates technical resilience against
adversarial input manipulation.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Goal hijack scenarios identified and mitigated in risk management system | Agent goal hijack included in Art. 9 risk assessment for every agentic deployment |
| Art. 14 — Human oversight | Meaningful human oversight over high-risk AI system outputs | Agents whose goals can be hijacked and execute autonomously are an Art. 14 failure — human confirmation required before goal-changing actions |
| Art. 15 — Accuracy, robustness, cybersecurity | Technical resilience against adversarial input manipulation | Input filtering, goal-state verification, and injection detection are Art. 15 technical requirements |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 14: Implement ability for operators to pause and override
  agents — mandatory for high-risk systems, cannot be waived
  by deployers under Art. 29
- Document all external content sources that feed agent context
  as foreseeable risk vectors in Art. 9 risk management

**Hardening — high-risk AI systems (from Aug 2026)**
- Art. 14: Implement and document goal-state verification —
  any agent action that diverges from stated goal requires
  human confirmation — auditable evidence for conformity
  assessment
- Art. 15: Implement and document technical injection
  detection controls — as Art. 15 robustness evidence
- Art. 17: Include goal hijack incident response in quality
  management system — suspension procedure, action reversal
  checklist documented

**Advanced — systemic risk GPAI models**
- Art. 55(1)(b): Conduct adversarial testing covering goal
  hijack scenarios — document results available to AI Office
- Art. 55: Report serious goal hijack incidents to AI Office
  without undue delay

#### Fines exposure
Art. 14 human oversight violations: up to **€15M or 3%**.
Art. 15 robustness violations: up to **€15M or 3%**.
Art. 55 systemic risk violations: up to **€35M or 7%**.

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B001/B005/B006 · NIST AI RMF GV-1.7 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical
**Applies to:** High-risk · GPAI models

Agents misuse legitimate tools, calling them with destructive
parameters or chaining them in unexpected sequences. Article 14
directly governs this — agents executing tool invocations with
irreversible OT or business consequences without human confirmation
are an Art. 14 human oversight failure. Article 15 mandates
cybersecurity measures preventing tool misuse.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Tool misuse risks identified and mitigated | All agent tool integrations assessed in Art. 9 risk management — reversibility classification documented |
| Art. 14 — Human oversight | Human oversight over high-risk AI actions | Irreversible tool invocations require human confirmation — Art. 14 binding requirement |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures preventing tool misuse | Per-tool permission manifests and parameter validation are Art. 15 technical requirements |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 14: For any high-risk agentic deployment, irreversible
  tool invocations — delete, send, publish, execute, pay —
  require human confirmation, cannot be bypassed

**Hardening — high-risk AI systems**
- Art. 14: Document human oversight mechanisms for all
  tool invocations — what requires approval, who approves,
  how overrides are logged — required for conformity assessment
- Art. 15: Implement and document per-tool permission
  manifests and parameter validation as Art. 15 cybersecurity
  evidence
- Art. 17: Include tool misuse incident response in quality
  management system — which tools can be disabled remotely,
  downstream impact assessment procedure

**Advanced — GPAI systemic risk**
- Art. 55(1)(b): Conduct adversarial testing covering tool
  chain exploitation — document for AI Office
- Art. 55: Incident reporting for serious tool misuse events

#### Fines exposure
Art. 14 violations: up to **€15M or 3%**.
Art. 15 violations: up to **€15M or 3%**.

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006 · ISA/IEC 62443 SR 2.1/2.2 (OT) · NIST AI RMF MP-5.1

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical
**Applies to:** High-risk · GPAI models · GDPR intersection

Agents inherit and cache credentials that, when compromised, expose
all systems the agent has access to. Article 15 mandates cybersecurity
measures for high-risk AI — NHI governance, short-lived credentials,
and access scope controls are Art. 15 technical requirements, not
optional best practices.

**GDPR intersection:** Where agent credentials provide access to
systems containing personal data, GDPR Art. 32 (security of
processing) applies in addition to EU AI Act obligations.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Credential exposure risk identified and mitigated | Agent credential lifecycle in Art. 9 risk management — NHI inventory, scope controls, rotation documented |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures protecting against credential theft | Short-lived credentials, JIT access, PKI-backed identities are Art. 15 requirements |
| Art. 17 — Quality management | Documented procedures for credential incident response | Agent credential incident response in quality management system — rotation, containment, lateral movement assessment |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 9: Document agent credential exposure as a foreseeable
  risk — assign treatment controls and review cadence
- GDPR Art. 32: Implement appropriate technical measures for
  agent access to personal data — short-lived credentials
  and access logging as security of processing requirements

**Hardening — high-risk AI systems**
- Art. 15: Implement and document NHI governance as Art. 15
  cybersecurity measure — credential lifecycle management,
  JIT access, anomaly detection evidence for conformity
  assessment
- Art. 17: Establish credential incident response in quality
  management — rotation procedure, containment checklist,
  lateral movement scope assessment

**Advanced — GPAI models**
- Art. 53(1)(a): Include agent identity architecture in GPAI
  technical documentation — how agents acquire, use, and
  expire credentials
- Implement PKI-backed agent identities as advanced Art. 15
  cybersecurity measure

#### Fines exposure
Art. 15 violations: up to **€15M or 3%**.
GDPR Art. 32 violations: up to **€20M or 4%**.

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 A/B007 · ISO 27001 A.8.2

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High
**Applies to:** High-risk · GPAI models

Malicious or compromised tools, MCP servers, or model components
loaded at runtime alter agent behaviour. Article 25 value chain
responsibility obligations mean providers cannot simply disclaim
supply chain risk — they must document what deployers inherit and
deployers must verify.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Supply chain risks identified and mitigated | All agent components in Art. 9 risk management — dynamic runtime components explicitly in scope |
| Art. 17 — Quality management | Quality management includes supply chain controls | Documented supply chain security procedures — component verification, change management |
| Art. 25 — Value chain responsibilities | Providers document obligations; deployers verify | Agent tool and MCP server supply chain obligations distributed along value chain |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 25: Understand your position in the AI value chain
  for all agent component integrations — provider vs deployer
  obligations explicitly identified

**Hardening — high-risk AI systems**
- Art. 9: Include all agent supply chain components in risk
  management — dynamic runtime components explicitly assessed
- Art. 17: Establish documented supply chain procedures —
  component verification, change management, rollback
  capability documented in quality management system
- Art. 25: Document supply chain obligations in contractual
  arrangements with tool and MCP server vendors

**Advanced — GPAI models**
- Art. 53(1)(a): Include agent component supply chain in
  GPAI technical documentation — available to AI Office
- Implement continuous component integrity monitoring —
  document as Art. 15 cybersecurity measure

#### Fines exposure
Art. 25 value chain violations: up to **€15M or 3%**.

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · AIUC-1 B001/B003/B008 · ISA/IEC 62443 62443-2-4 (OT)

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical
**Applies to:** High-risk · GPAI models

Agents that generate and execute code become RCE gateways. Article 15
mandates technical robustness and cybersecurity — sandboxing,
allowlisting, and static analysis of agent-generated code are Art. 15
technical requirements, not optional hardening.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Code execution risks identified and mitigated | Agent code execution capability documented in Art. 9 risk management — sandbox status, permitted operations |
| Art. 15 — Accuracy, robustness, cybersecurity | Technical robustness against adversarial code execution | Sandboxing, input filtering, static analysis are Art. 15 requirements for agents with code execution |
| Art. 17 — Quality management | Post-market monitoring covering code execution incidents | Code execution anomaly response in quality management system |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 9: Document agent code execution capability as a
  foreseeable risk — sandbox status and permitted operations
  documented before any deployment

**Hardening — high-risk AI systems**
- Art. 15: Implement and document sandboxing, input
  filtering, and static analysis as Art. 15 cybersecurity
  evidence — required for conformity assessment
- Art. 17: Include code execution incident response in
  quality management system — sandbox isolation, kill switch,
  forensic capture procedure

**Advanced — GPAI systemic risk**
- Art. 55(1)(b): Include code execution attack scenarios
  in adversarial testing programme — sandbox escape attempts
  documented for AI Office
- Hardware-level sandboxing documented as Art. 15 advanced
  cybersecurity measure

#### Fines exposure
Art. 15 violations: up to **€15M or 3%**.

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI06 — Memory & Context Poisoning

**Severity:** High
**Applies to:** High-risk · GPAI models · GDPR intersection

Persistent memory poisoning causes systematic incorrect behaviour
across all future interactions. Article 10 data governance obligations
apply to agent memory stores that contain personal data — the same
governance requirements that apply to training data apply to runtime
memory that influences model behaviour.

**GDPR intersection:** Where agent memory stores contain personal
data, GDPR Art. 25 (data protection by design) and Art. 32 (security
of processing) apply — memory access controls and TTL enforcement
are privacy-by-design requirements.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 10 — Data and data governance | Data governance applies to all data influencing AI behaviour — including agent memory | Agent memory governance — classification, access controls, integrity validation, retention — is an Art. 10 requirement |
| Art. 15 — Accuracy, robustness, cybersecurity | Technical resilience against adversarial memory manipulation | Memory integrity monitoring and access controls are Art. 15 requirements |
| Art. 17 — Quality management | Post-market monitoring for memory integrity | Memory anomaly detection in post-market monitoring programme |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 10: Apply data governance to agent memory stores —
  classification, access controls, and retention limits
  documented before deployment
- GDPR Art. 25: Implement data protection by design for
  memory stores containing personal data — access controls
  and TTL as privacy-by-design requirements

**Hardening — high-risk AI systems**
- Art. 10: Document memory governance as Art. 10 compliance
  evidence — classification propagation, access logs,
  retention enforcement — required for conformity assessment
- Art. 15: Implement memory integrity monitoring and
  anomaly detection as Art. 15 cybersecurity measures
- Art. 17: Include memory poisoning incident response
  in quality management system

**Advanced — GPAI models**
- Art. 53(1)(a): Document agent memory architecture in
  GPAI technical documentation — memory types, trust levels,
  access controls, retention policies
- Cryptographic memory integrity verification as advanced
  Art. 15 cybersecurity measure

#### Fines exposure
Art. 10/15 violations: up to **€15M or 3%**.
GDPR Art. 25/32 violations: up to **€20M or 4%**.

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002 · ISO 27001 A.8.15 · NIST AI RMF GV-1.6

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High
**Applies to:** High-risk · GPAI models

A2A communication channels lacking authentication or encryption
enable agent-in-the-middle attacks. Article 15 cybersecurity
obligations apply to all components of a high-risk AI system —
inter-agent communication channels are system components, not
peripheral infrastructure.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | A2A communication risks identified and mitigated | Inter-agent channels in Art. 9 risk assessment — authentication, encryption, schema validation status |
| Art. 15 — Accuracy, robustness, cybersecurity | Cybersecurity measures protecting all system components | Authenticated, encrypted A2A communication is an Art. 15 requirement for high-risk agentic systems |
| Art. 17 — Quality management | Documentation of A2A security controls | A2A authentication and encryption documented in quality management system |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 9: Map all A2A communication channels in risk
  management system — authentication and encryption
  status documented before deployment

**Hardening — high-risk AI systems**
- Art. 15: Implement and document A2A authentication and
  encryption as Art. 15 cybersecurity evidence — required
  for conformity assessment
- Art. 17: Include A2A security in quality management —
  authentication method, encryption standard, and replay
  protection documented

**Advanced — GPAI models**
- Art. 53(1)(a): Document A2A communication architecture
  in GPAI technical documentation
- Mutual TLS on all A2A channels documented as advanced
  Art. 15 cybersecurity measure

#### Fines exposure
Art. 15 violations: up to **€15M or 3%**.

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 B007/B008 · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High
**Applies to:** High-risk · GPAI models

Single-point faults propagate through multi-agent workflows. In
critical infrastructure environments, cascading agent failures can
cross from the AI layer into physical process control. Article 15
robustness obligations require resilience against cascading failure —
circuit breakers and fail-safe defaults are technical requirements,
not optional features.

**OT critical note:** For agents in critical infrastructure (Annex III
high-risk category), Art. 15 robustness failures carrying physical
process consequences face heightened compliance scrutiny.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Cascade risks identified and mitigated — blast radius defined | Cascade scenarios in Art. 9 risk management — maximum affected systems, circuit breaker thresholds |
| Art. 14 — Human oversight | Human oversight over high-risk AI — ability to pause and stop | Circuit breakers and kill switches are Art. 14 human oversight mechanisms |
| Art. 15 — Accuracy, robustness, cybersecurity | Technical resilience against cascading failures | Circuit breakers, fail-safe defaults, and cascade containment architecture are Art. 15 requirements |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 14: Implement operator-accessible kill switch for
  all agent clusters — mandatory for high-risk systems
- Art. 9: Define cascade blast radius before each multi-agent
  deployment — document and accept in risk management system

**Hardening — high-risk AI systems**
- Art. 15: Implement and document circuit breakers, fail-safe
  defaults, and cascade containment as Art. 15 robustness
  evidence — required for conformity assessment
- Art. 14: Document human oversight mechanisms for cascade
  events — who is notified, what fallback activates, how
  operators resume control
- Art. 17: Include cascade incident response in quality
  management system

**Advanced — critical infrastructure deployments**
- Art. 15: Conduct chaos engineering testing — document
  cascade resilience evidence for conformity assessment
- Art. 14: Automated process control fallback on cascade
  detection documented as Art. 14 human oversight measure

#### Fines exposure
Art. 14 violations: up to **€15M or 3%**.
Art. 15 violations: up to **€15M or 3%**.

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6 (OT) · NIST SP 800-82 (OT)

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium
**Applies to:** All tiers — Art. 50 transparency applies universally

Users anthropomorphise agents, enabling hijacked agents to manipulate
humans into approving harmful actions. Article 14 (human oversight)
and Article 50 (AI disclosure) are the primary articles — the
transparency obligation that Art. 50 establishes is the baseline
defence against trust exploitation.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 13 — Transparency | Users informed of capabilities, limitations, and AI nature | Agents must clearly communicate their AI nature and advisory limitations |
| Art. 14 — Human oversight | Effective human oversight over high-risk AI | Humans must be able to override agent recommendations — trust exploitation undermines Art. 14 effectiveness |
| Art. 50 — Transparency for certain AI systems | Chatbots and AI-generated content must disclose AI nature | All agent-user interactions require AI disclosure — universal obligation |

#### Compliance obligations by tier

**Foundational — all deployments (already required)**
- Art. 50: All agent deployments must disclose AI nature in
  user-facing interactions — universal obligation in force
  from August 2025
- Art. 13: Document and communicate agent capabilities and
  advisory limitations to deployers and users

**Hardening — high-risk AI systems**
- Art. 14: Implement and document human oversight measures
  that are robust against trust exploitation — approval
  flows must be independent of the agent interface
- Art. 17: Include trust exploitation incident response in
  quality management — aggregate pattern detection and
  operator retraining procedures

**Advanced — all deployments**
- Art. 50: AI-generated content that could be mistaken for
  authoritative human guidance must be clearly marked —
  applies to all agent recommendations
- Behavioural analysis detecting manipulation patterns
  documented as Art. 14 human oversight enhancement

#### Fines exposure
Art. 50 transparency violations: up to **€7.5M or 1.5%**.
Art. 14 violations: up to **€15M or 3%**.

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: AIUC-1 C/F · NIST AI RMF GV-1.7 · EU AI Act Art. 52

---

### ASI10 — Rogue Agents

**Severity:** Critical
**Applies to:** High-risk · GPAI models with systemic risk

Malicious or compromised agents appear compliant but pursue hidden
goals. Article 14 human oversight is compromised by a rogue agent —
the human confirms actions that appear legitimate but serve the
attacker's intent. Article 15 technical resilience requirements
mandate behavioural monitoring and kill switch capability.

#### EU AI Act mapping

| Article | Obligation | How it applies |
|---|---|---|
| Art. 9 — Risk management | Rogue agent scenarios identified and mitigated | Rogue agent risk in Art. 9 risk management — detection capability, blast radius, response documented |
| Art. 14 — Human oversight | Human oversight mechanisms effective against rogue behaviour | Kill switch and behavioural monitoring are Art. 14 human oversight requirements for agentic systems |
| Art. 15 — Accuracy, robustness, cybersecurity | Technical resilience against rogue agent behaviour | Behavioural baselines, anomaly detection, and automated suspension are Art. 15 requirements |
| Art. 17 — Quality management | Post-market monitoring covering rogue agent detection | Behavioural monitoring in post-market monitoring programme |

#### Compliance obligations by tier

**Foundational — all deployments**
- Art. 9: Document rogue agent risk in risk management —
  detection capability status, blast radius, and defined
  response procedures before deployment
- Art. 14: Implement operator-accessible kill switch —
  mandatory for high-risk systems, cannot be waived

**Hardening — high-risk AI systems**
- Art. 15: Implement behavioural baselines and anomaly
  detection as Art. 15 technical measures — evidence
  required for conformity assessment
- Art. 14: Document how kill switch and behavioural monitoring
  constitute effective human oversight — required in
  conformity assessment
- Art. 17: Include rogue agent containment in quality
  management — kill switch procedure, audit checklist,
  operational impact assessment

**Advanced — systemic risk GPAI models**
- Art. 55(1)(b): Include rogue agent scenarios in adversarial
  testing programme — persistent hidden goal detection
  tested, results available to AI Office
- Art. 55: Incident reporting for serious rogue agent events

#### Fines exposure
Art. 14 violations: up to **€15M or 3%**.
Art. 15 violations: up to **€15M or 3%**.
Art. 55 systemic risk violations: up to **€35M or 7%**.

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · NIST AI RMF MS-2.5 · ISA/IEC 62443 SR 3.7 (OT)

---

## Agentic AI × EU AI Act compliance checklist

### August 2025 — GPAI obligations (already past)

- [ ] Determine if any agentic systems qualify as GPAI models (Art. 51)
- [ ] If GPAI: technical documentation published (Art. 53) — covers ASI03/04/06
- [ ] If GPAI: information security policy implemented (Art. 53)
- [ ] If systemic risk GPAI: registered with AI Office
- [ ] If systemic risk GPAI: adversarial testing programme live (Art. 55) — covers ASI01/ASI10
- [ ] All agent-user interfaces: Art. 50 AI disclosure implemented

### August 2026 — High-risk obligations (4 months away)

- [ ] Classify all agentic systems against Annex III high-risk categories
- [ ] Art. 9 risk management covers all ASI entries per deployment
- [ ] Art. 14 human oversight: kill switch implemented and tested for all agents
- [ ] Art. 14 human oversight: irreversible tool invocations require human confirmation
- [ ] Art. 15 cybersecurity: agent tool permission manifests documented
- [ ] Art. 15 cybersecurity: A2A authentication and encryption implemented
- [ ] Art. 15 cybersecurity: behavioural baselines and anomaly detection live
- [ ] Art. 17 quality management: incident response procedures for each ASI entry
- [ ] Conformity assessment completed
- [ ] EU Declaration of Conformity signed

---

## Implementation priority aligned to EU AI Act

| Phase | ASI entries | Articles | Deadline |
|---|---|---|---|
| 1 — Immediate | ASI09 — Art. 50 disclosure | Art. 50 | Now — already required |
| 2 — Urgent | ASI03/04/06 — GPAI documentation | Art. 53 | Aug 2025 — past |
| 3 — Critical | ASI01/02/08/10 — human oversight | Art. 14 | Aug 2026 |
| 4 — Critical | ASI03/05/07 — cybersecurity | Art. 15 | Aug 2026 |
| 5 — Ongoing | ASI10 — systemic risk adversarial testing | Art. 55(1)(b) | Continuous |

---

## References

- [EU AI Act full text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [AIUC-1 — OWASP Agentic Top 10 coverage](https://www.aiuc-1.com/research/aiuc-1-certification-covers-all-owasp-agentic-top-10-threats)
- [ENISA AI Act guidance](https://www.enisa.europa.eu)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with compliance checklist and fines exposure | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
