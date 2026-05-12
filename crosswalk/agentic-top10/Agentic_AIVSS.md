<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : OWASP AIVSS — AI Vulnerability Scoring System
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × OWASP AIVSS

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [OWASP AI Vulnerability Scoring System (AIVSS)](https://aivss.owasp.org) —
the scoring framework designed to quantify the severity of vulnerabilities
in AI and ML systems in a way that standard CVSS cannot adequately capture.

---

## Why AIVSS for agentic AI

CVSS was designed for discrete software vulnerabilities with defined
exploit paths and clear remediation. Agentic AI risks have properties
that CVSS cannot express:

- **Autonomy amplifier** — the same injection that produces a single
  bad response in a static LLM enables a complete multi-step attack
  chain in an agent. AIVSS captures the autonomy dimension.
- **Persistence dimension** — memory poisoning and rogue agent risks
  persist across sessions. CVSS temporal metrics do not capture this.
- **Blast radius vs single system** — a cascading failure affects
  multiple downstream systems simultaneously. CVSS scope captures
  this partially but not the agentic cascade dynamic.
- **Human oversight counterfactual** — the presence or absence of a
  human in the loop fundamentally changes the severity of many agentic
  risks. AIVSS incorporates human oversight as a scoring dimension.

---

## AIVSS scoring dimensions

AIVSS extends CVSS with AI-specific dimensions. The relevant
dimensions for agentic risk scoring are:

| Dimension | Abbreviation | Values | Agentic relevance |
|---|---|---|---|
| Attack Vector | AV | Network / Adjacent / Local / Physical | How the agent is reached |
| Attack Complexity | AC | Low / High | Difficulty of executing the attack |
| Privileges Required | PR | None / Low / High | Access needed to exploit |
| User Interaction | UI | None / Required | Human in the loop requirement |
| Scope | S | Unchanged / Changed | Does exploit cross system boundaries |
| Confidentiality Impact | C | None / Low / High | Data exposure |
| Integrity Impact | I | None / Low / High | Data or action integrity |
| Availability Impact | A | None / Low / High | System availability |
| **Autonomy Level** | **AL** | **None / Supervised / Autonomous** | Agent operates without human per-action confirmation |
| **Persistence** | **PE** | **None / Session / Long-term** | How long the effect persists |
| **Blast Radius** | **BR** | **Single / Multi / Critical-Infrastructure** | Downstream systems affected |

---

## Scoring methodology for this file

Each ASI entry is scored under two scenarios to show how autonomy
changes severity:

- **Scenario A — Supervised deployment:** Human reviews and confirms
  all agent actions before execution. Human oversight mitigates but
  does not eliminate the risk.
- **Scenario B — Autonomous deployment:** Agent executes actions
  without per-action human confirmation. Represents highest-risk
  operational configuration.

The AIVSS score difference between A and B is the **autonomy premium**
— the additional severity introduced by removing human oversight.

---

## Quick-reference summary

| ID | Name | AIVSS Score (Supervised) | AIVSS Score (Autonomous) | Autonomy Premium | Severity Band |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | 7.8 | 9.8 | +2.0 | High / Critical |
| ASI02 | Tool Misuse & Exploitation | 7.5 | 9.6 | +2.1 | High / Critical |
| ASI03 | Identity & Privilege Abuse | 8.1 | 9.3 | +1.2 | High / Critical |
| ASI04 | Agentic Supply Chain | 6.8 | 8.4 | +1.6 | Medium / High |
| ASI05 | Unexpected Code Execution | 8.4 | 9.9 | +1.5 | High / Critical |
| ASI06 | Memory & Context Poisoning | 6.5 | 8.7 | +2.2 | Medium / High |
| ASI07 | Insecure Inter-Agent Comms | 6.9 | 8.2 | +1.3 | Medium / High |
| ASI08 | Cascading Agent Failures | 7.1 | 9.1 | +2.0 | High / Critical |
| ASI09 | Human-Agent Trust Exploitation | 5.4 | 7.3 | +1.9 | Medium / High |
| ASI10 | Rogue Agents | 7.6 | 9.7 | +2.1 | High / Critical |

**Key finding:** The autonomy premium across all 10 entries averages
+1.79 severity points. Removing human oversight converts 7 of 10
entries from High to Critical. This is the quantitative case for
mandatory human oversight in high-stakes agentic deployments.

---

## Audience tags

- **Risk manager** — full file, use AIVSS scores to prioritise remediation
- **CISO** — autonomy premium table for board-level AI risk reporting
- **Security architect** — per-entry scoring rationale for design decisions
- **QSA / assessor** — severity evidence for EU AI Act and PCI DSS assessments
- **Penetration tester** — scoring rationale to calibrate test severity ratings

---

## Detailed scoring

---

### ASI01 — Agent Goal Hijack

**Supervised score: 7.8 (High)**
**Autonomous score: 9.8 (Critical)**
**Autonomy premium: +2.0**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Injection via network-accessible input channels |
| Attack Complexity | Low (L) | Well-documented techniques, tools available |
| Privileges Required | None (N) | User-level access to LLM interface sufficient |
| User Interaction | Required (R) | Human reviews recommendations before action |
| Scope | Changed (C) | Hijacked goal can affect systems beyond the LLM |
| Confidentiality | High (H) | Hijacked agent may extract sensitive data |
| Integrity | High (H) | Hijacked agent may corrupt data or trigger harmful actions |
| Availability | Low (L) | Disruption of agent service |
| Autonomy Level | Supervised (S) | Human confirmation of all consequential actions |
| Persistence | Session (S) | Goal hijack typically within-session |
| Blast Radius | Multi (M) | Agent has access to multiple downstream systems |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L/AL:S/PE:S/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | Agent executes without human review |
| Autonomy Level | Autonomous (A) | No per-action human confirmation |
| Persistence | Long-term (L) | Autonomous execution before detection |
| Blast Radius | Critical-Infrastructure (CI) | In OT environments, physical consequence possible |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L/AL:A/PE:L/BR:CI

#### Autonomy premium rationale

Goal hijack in a supervised deployment requires the attacker to craft
output that convincingly misleads a human reviewer. In autonomous
deployment, the attack chain executes completely before any human
sees the output — the entire kill chain completes within a single
agent session. The +2.0 premium reflects this fundamental change
in the attacker's required sophistication.

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Goal-state verification | -0.5 | Structural detection before action |
| Input validation on all channels | -0.3 | Reduces AC from L to H for indirect injection |
| Human confirmation gates | -2.0 | Moves from Autonomous to Supervised scoring |
| Least privilege tool access | -0.4 | Reduces blast radius |

---

### ASI02 — Tool Misuse & Exploitation

**Supervised score: 7.5 (High)**
**Autonomous score: 9.6 (Critical)**
**Autonomy premium: +2.1**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Via network-accessible LLM interface |
| Attack Complexity | Low (L) | Tool misuse via injection is well-understood |
| Privileges Required | None (N) | User-level access sufficient |
| User Interaction | Required (R) | Human approves tool invocations |
| Scope | Changed (C) | Tools interact with systems beyond the LLM |
| Confidentiality | High (H) | Tool access may expose sensitive data |
| Integrity | High (H) | Destructive tool calls corrupt data or trigger actions |
| Availability | Low (L) |  Tool unavailability impacts service |
| Autonomy Level | Supervised (S) | Human reviews irreversible tool calls |
| Persistence | Session (S) | Tool misuse within-session |
| Blast Radius | Multi (M) | Tools span multiple backend systems |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L/AL:S/PE:S/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | No human review of tool calls |
| Autonomy Level | Autonomous (A) | All tool calls execute without confirmation |
| Persistence | Long-term (L) | Tool misuse persists until discovered |
| Blast Radius | Critical-Infrastructure (CI) | OT tools: physical process consequences |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/AL:A/PE:L/BR:CI

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Per-tool permission manifests | -0.5 | Reduces exploitable tool surface |
| Parameter validation at conduit | -0.4 | Raises AC by requiring parameter crafting |
| Irreversibility gates | -2.0 | Eliminates autonomous execution of high-impact tools |
| Tool call anomaly detection | -0.3 | Reduces persistence by shortening dwell time |

---

### ASI03 — Identity & Privilege Abuse

**Supervised score: 8.1 (High)**
**Autonomous score: 9.3 (Critical)**
**Autonomy premium: +1.2**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Credential theft via network paths |
| Attack Complexity | Low (L) | Credentials in memory/logs are accessible |
| Privileges Required | Low (L) | Requires access to agent interface |
| User Interaction | Required (R) | Human oversight reduces unchecked access |
| Scope | Changed (C) | Stolen credentials enable lateral movement |
| Confidentiality | High (H) | All data accessible to stolen credential |
| Integrity | High (H) | Write access under stolen credential |
| Availability | Low (L) | Credential abuse may not cause outage |
| Autonomy Level | Supervised (S) | Human reviews access patterns |
| Persistence | Long-term (L) | Stolen credentials valid until rotated |
| Blast Radius | Multi (M) | All systems accessible to credential |

**AIVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:L/AL:S/PE:L/BR:M

#### Autonomous deployment (Scenario B)

The autonomy premium for ASI03 is lower (+1.2) than other entries
because credential theft impact is largely independent of whether
the agent is supervised — the stolen credential can be used directly
by the attacker outside the agent framework regardless.

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | No human credential usage review |
| Autonomy Level | Autonomous (A) | Credential use not reviewed per-action |

**AIVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L/AL:A/PE:L/BR:M

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Short-lived JIT credentials | -0.8 | Reduces PE from Long-term to Session |
| Unique identity per agent | -0.3 | Limits credential blast radius |
| Credential anomaly detection | -0.4 | Reduces dwell time |
| NHI-5 least privilege | -0.5 | Reduces BR from Multi to Single for narrow-scope agents |

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Supervised score: 6.8 (Medium)**
**Autonomous score: 8.4 (High)**
**Autonomy premium: +1.6**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Supply chain compromise via upstream repositories |
| Attack Complexity | High (H) | Requires supply chain access, timing, and evasion |
| Privileges Required | None (N) | Legitimate package consumption |
| User Interaction | Required (R) | Human reviews behavioural changes in testing |
| Scope | Changed (C) | Compromised component affects all consumers |
| Confidentiality | High (H) | Backdoor may exfiltrate data silently |
| Integrity | High (H) | Backdoor may alter agent decisions |
| Availability | Low (L) | Supply chain attacks typically avoid detection via outages |
| Autonomy Level | Supervised (S) | Human reviews anomalous behaviour |
| Persistence | Long-term (L) | Embedded backdoor persists across updates |
| Blast Radius | Multi (M) | All agents using the compromised component |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:L/AL:S/PE:L/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | No human catches behavioural anomaly |
| Autonomy Level | Autonomous (A) | Backdoored actions execute without review |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:L/AL:A/PE:L/BR:M

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Cryptographic signature verification | -0.8 | Raises AC significantly |
| Isolated evaluation environment | -0.6 | Detects behavioural anomaly before production |
| ML SBOM with CVE monitoring | -0.4 | Reduces dwell time of known-vulnerable components |

---

### ASI05 — Unexpected Code Execution

**Supervised score: 8.4 (High)**
**Autonomous score: 9.9 (Critical)**
**Autonomy premium: +1.5**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Via LLM API input |
| Attack Complexity | Low (L) | Code injection via prompt is well-understood |
| Privileges Required | None (N) | User-level access |
| User Interaction | Required (R) | Human reviews generated code before execution |
| Scope | Changed (C) | RCE scope extends beyond the LLM |
| Confidentiality | High (H) | Code can read any accessible data |
| Integrity | High (H) | Code can modify any accessible state |
| Availability | High (H) | Code can destroy data or exhaust resources |
| Autonomy Level | Supervised (S) | Code reviewed before execution |
| Persistence | Long-term (L) | Backdoor code can persist |
| Blast Radius | Multi (M) | Zone 3 network access in OT |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H/AL:S/PE:L/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | Code executes without review |
| Autonomy Level | Autonomous (A) | Execution without confirmation |
| Blast Radius | Critical-Infrastructure (CI) | OT: code runs inside Zone 3 network |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/AL:A/PE:L/BR:CI

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Hardware-level sandboxing | -0.7 | Raises AC for sandbox escape |
| Static analysis before execution | -0.5 | Raises AC |
| No-code-execution policy (preferred) | -9.9 | Eliminates risk entirely — strongest control |

---

### ASI06 — Memory & Context Poisoning

**Supervised score: 6.5 (Medium)**
**Autonomous score: 8.7 (High)**
**Autonomy premium: +2.2**

The autonomy premium for ASI06 is the highest (+2.2) because supervised
deployments catch memory poisoning through human review of anomalous
recommendations. In autonomous deployments, poisoned memory silently
influences every decision without any human noticing the pattern.

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Via conversation, RAG, or tool return |
| Attack Complexity | High (H) | Requires crafting content that survives validation and influences memory |
| Privileges Required | None (N) | User-level access sufficient |
| User Interaction | Required (R) | Human notices anomalous recommendations |
| Scope | Changed (C) | Poisoned memory influences downstream decisions |
| Confidentiality | Low (L) | Memory poisoning is primarily an integrity attack |
| Integrity | High (H) | Systematic incorrect recommendations |
| Availability | Low (L) | Memory poisoning typically maintains service appearance |
| Autonomy Level | Supervised (S) | Human catches anomalous patterns |
| Persistence | Long-term (L) | Poisoned memory persists across sessions |
| Blast Radius | Multi (M) | All decisions using poisoned memory |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:L/I:H/A:L/AL:S/PE:L/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | No human reviews recommendation patterns |
| Autonomy Level | Autonomous (A) | Poisoned decisions execute without human check |
| Confidentiality | High (H) | Autonomous agent acts on poisoned memory including data access |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:L/AL:A/PE:L/BR:M

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Memory TTL enforcement | -0.5 | Reduces PE from Long-term to Session |
| Memory integrity monitoring | -0.6 | Enables earlier detection |
| Validated sources only for memory writes | -0.7 | Raises AC |

---

### ASI07 — Insecure Inter-Agent Communication

**Supervised score: 6.9 (Medium)**
**Autonomous score: 8.2 (High)**
**Autonomy premium: +1.3**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Adjacent (A) | Requires access to A2A network segment |
| Attack Complexity | High (H) | Requires network position on A2A channel |
| Privileges Required | Low (L) | Network access to A2A segment |
| User Interaction | Required (R) | Human reviews anomalous agent coordination |
| Scope | Changed (C) | Spoofed messages affect downstream agents |
| Confidentiality | High (H) | A2A messages may contain sensitive context |
| Integrity | High (H) | Spoofed messages corrupt agent coordination |
| Availability | Low (L) | A2A attacks typically maintain service appearance |
| Autonomy Level | Supervised (S) | Human reviews cross-agent coordination outcomes |
| Persistence | Session (S) | Within the scope of compromised session |
| Blast Radius | Multi (M) | All agents in the cluster |

**AIVSS Vector:** AV:A/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:L/AL:S/PE:S/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | Agents coordinate without human visibility |
| Autonomy Level | Autonomous (A) | A2A coordination executes without review |

**AIVSS Vector:** AV:A/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:L/AL:A/PE:S/BR:M

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Mutual TLS on A2A channels | -0.7 | Raises AC significantly |
| Replay protection | -0.3 | Raises AC for replay attacks |
| A2A network isolation | -0.5 | Changes AV from Adjacent to Local |

---

### ASI08 — Cascading Agent Failures

**Supervised score: 7.1 (High)**
**Autonomous score: 9.1 (Critical)**
**Autonomy premium: +2.0**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Trigger via crafted input or component failure |
| Attack Complexity | High (H) | Requires specific failure conditions across multiple agents |
| Privileges Required | None (N) | User-level access may trigger cascade |
| User Interaction | Required (R) | Human can interrupt cascade manually |
| Scope | Changed (C) | Cascade affects multiple systems |
| Confidentiality | Low (L) | Cascade is primarily availability/integrity attack |
| Integrity | High (H) | Cascading incorrect actions across systems |
| Availability | High (H) | Process disruption is primary impact |
| Autonomy Level | Supervised (S) | Human can interrupt |
| Persistence | Session (S) | Cascade resolved within session |
| Blast Radius | Multi (M) | All systems in agent cluster |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:L/I:H/A:H/AL:S/PE:S/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | No human intervention possible in time |
| Autonomy Level | Autonomous (A) | Cascade completes before human review |
| Blast Radius | Critical-Infrastructure (CI) | OT: physical process consequences before detection |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:H/A:H/AL:A/PE:S/BR:CI

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Circuit breakers | -0.8 | Reduces BR and limits propagation |
| Cascade depth limits | -0.4 | Reduces BR |
| Operator kill switch | -0.8 | Restores effective human oversight even in autonomous deployments |

---

### ASI09 — Human-Agent Trust Exploitation

**Supervised score: 5.4 (Medium)**
**Autonomous score: 7.3 (High)**
**Autonomy premium: +1.9**

ASI09 is the only entry where supervised deployment is not
inherently safer — the attack specifically targets the human supervisor.
The supervised score is lower because the attack requires a human
to make a decision, providing at least some friction. The autonomous
score rises because automated workflows can be manipulated into
approving actions with no human available to question the outcome.

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Via agent interface |
| Attack Complexity | High (H) | Requires sustained social engineering across sessions |
| Privileges Required | None (N) | User-level access |
| User Interaction | Required (R) | Attack targets human decision-making |
| Scope | Changed (C) | Manipulated human approves actions outside intended scope |
| Confidentiality | Low (L) | Trust exploitation is primarily integrity/action attack |
| Integrity | High (H) | Incorrect approvals corrupt operational decisions |
| Availability | None (N) | Availability unaffected |
| Autonomy Level | Supervised (S) | Human is target |
| Persistence | Long-term (L) | Trust accumulates across many sessions |
| Blast Radius | Single (S) | Targets specific human decision-maker |

**AIVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:L/I:H/A:N/AL:S/PE:L/BR:S

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| Attack Complexity | Low (L) | No human friction; automated workflows more susceptible |
| User Interaction | None (N) | No human in the decision loop |
| Autonomy Level | Autonomous (A) | Automated decisions execute without review |
| Blast Radius | Multi (M) | Automated workflows affect multiple systems |

**AIVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N/AL:A/PE:L/BR:M

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| AI disclosure (Art. 50) | -0.4 | Raises user awareness |
| Independent approval flows | -0.8 | Eliminates automated approval path |
| Aggregate trust monitoring | -0.4 | Detects systematic manipulation patterns |

---

### ASI10 — Rogue Agents

**Supervised score: 7.6 (High)**
**Autonomous score: 9.7 (Critical)**
**Autonomy premium: +2.1**

#### Supervised deployment (Scenario A)

| Dimension | Value | Rationale |
|---|---|---|
| Attack Vector | Network (N) | Via supply chain, injection, or memory poisoning |
| Attack Complexity | High (H) | Requires sustained covert operation without detection |
| Privileges Required | Low (L) | Agent's existing access scope |
| User Interaction | Required (R) | Human reviews agent recommendations |
| Scope | Changed (C) | Rogue agent affects all systems it has access to |
| Confidentiality | High (H) | Rogue agent may exfiltrate data covertly |
| Integrity | High (H) | Systematic biased recommendations |
| Availability | Low (L) | Rogue agents typically maintain service to avoid detection |
| Autonomy Level | Supervised (S) | Human catches patterns through review |
| Persistence | Long-term (L) | Designed to persist undetected |
| Blast Radius | Multi (M) | All systems accessible to agent |

**AIVSS Vector:** AV:N/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:L/AL:S/PE:L/BR:M

#### Autonomous deployment (Scenario B)

| Dimension | Value change | Rationale |
|---|---|---|
| User Interaction | None (N) | No human reviews agent decisions |
| Autonomy Level | Autonomous (A) | Rogue actions execute without review |
| Blast Radius | Critical-Infrastructure (CI) | In OT: physical sabotage scenario |

**AIVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:L/AL:A/PE:L/BR:CI

#### Severity-reducing controls

| Control | Score reduction | Notes |
|---|---|---|
| Behavioural baseline monitoring | -0.8 | Raises AC by requiring evasion of baseline |
| Aggregate recommendation analysis | -0.5 | Detects systematic bias |
| Short-lived credentials | -0.4 | Limits dwell time benefit for attacker |
| Least privilege tool scope | -0.5 | Reduces BR |

---

## AIVSS scores in risk register context

Use AIVSS scores to drive prioritisation in your AI risk register:

| AIVSS range | Severity band | Risk register treatment |
|---|---|---|
| 9.0–10.0 | Critical | Immediate remediation before production; executive notification |
| 7.0–8.9 | High | Remediation within 30 days; CISO visibility |
| 4.0–6.9 | Medium | Remediation within 90 days; security engineering ownership |
| 0.1–3.9 | Low | Remediation in next sprint cycle; accept with documented rationale |

**For autonomous deployments:** Use the Autonomous scenario score.
**For supervised deployments:** Use the Supervised scenario score.
**For mixed deployments:** Use the worst-case score for risk register entry.

---

## References

- [OWASP AIVSS](https://aivss.owasp.org)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [CVSS v3.1 Specification](https://www.first.org/cvss/specification-document)
- [AIUC-1 Standard](https://www.aiuc-1.com)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial scoring — ASI01–ASI10 dual-scenario AIVSS with autonomy premium analysis | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
