<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic AI Applications 2026 (ASI01-ASI10)
  Framework   : NIST SP 800-82 Rev 3 — Guide to Operational Technology (OT) Security
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × NIST SP 800-82 Rev 3

Mapping the [OWASP Top 10 for Agentic AI Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [NIST SP 800-82 Revision 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) —
Guide to Operational Technology (OT) Security, published May 2023.

**Use this file alongside [Agentic_ISA62443.md](Agentic_ISA62443.md).**
ISA 62443 provides the zone model and security level requirements;
SP 800-82 provides the implementation guidance, network architecture
recommendations, and U.S. regulatory context.

---

## Why SP 800-82 Rev 3 for agentic AI in OT

Autonomous AI agents in OT environments represent a qualitatively
different risk profile from static LLM deployments. An agent can
take sequences of actions — reading sensor data, issuing commands,
invoking SCADA APIs — without human review at each step. SP 800-82
Rev 3 is the right framework for this scenario because:

**Autonomous action amplifies OT risk.** SP 800-82 Section 5 documents
OT-specific threat categories — manipulation of control, denial of
safety, equipment damage — that become dramatically more accessible
when an autonomous agent can chain tool calls across OT boundaries.

**SP 800-82 Rev 3 explicitly addresses remote and cloud access.**
Rev 3's expansion of remote access, cloud integration, and third-party
connectivity sections makes it directly applicable to agentic systems
that operate across IT/OT boundaries.

**Federal and sector regulatory alignment.** SP 800-82 is referenced
by CISA, underpins NERC CIP technical guidance, and is mandatory
for many FISMA-covered federal OT deployments. Agentic AI crossing
OT boundaries must comply.

---

## SP 800-82 Rev 3 structure

| Section | Title | Agentic relevance |
|---|---|---|
| Section 4 | OT Overview and Key Differences from IT | Baseline architecture context for agent placement |
| Section 5 | OT Threats and Vulnerabilities | Agent-amplified threat categories |
| Section 6 | Risk Management | Risk assessment for autonomous agent integration |
| Section 7 | Recommended Security Architecture | Network segmentation for agent communications |
| Section 8 | OT Security Program | Governance, programme, and supply chain controls |
| Appendix G | Network Architecture Examples | Reference architectures for agent placement |

---

## Quick-reference summary

| ID | Name | OT Severity | SP 800-82 Sections | SP 800-53 Controls | Tier |
|---|---|---|---|---|---|
| ASI01 | Prompt Injection in Agentic Systems | **Critical** | 5.3, 6.2, 7.2 | SI-10, SI-3, AC-3 | Foundational–Advanced |
| ASI02 | Excessive Permissions and Scope | **Critical** | 5.3, 6.2, 7.1 | AC-6, AC-3, AU-12 | Foundational–Advanced |
| ASI03 | Memory Manipulation and Persistence | High | 5.3, 6.2 | SI-7, SC-28, AC-3 | Hardening–Advanced |
| ASI04 | Multi-Agent Trust Exploitation | **Critical** | 5.3, 6.2, 7.2 | IA-3, AC-3, AU-12 | Hardening–Advanced |
| ASI05 | Tool and Plugin Abuse | High | 5.5, 6.3, 8.4 | SA-12, CM-7, SR-3 | Foundational–Hardening |
| ASI06 | Data Exfiltration via Agentic Channels | **Critical** | 5.4, 6.2, 7.3 | SC-28, AC-3, AU-9 | Hardening–Advanced |
| ASI07 | Supply Chain Compromise in Agent Ecosystems | High | 5.5, 6.3, 8.4 | SA-12, SR-3, SR-6 | Foundational–Hardening |
| ASI08 | Inversion of Safety Controls | **Critical** | 5.3, 6.2, 7.1 | SI-3, AC-6, AU-12 | Advanced |
| ASI09 | Inadequate Human Oversight and Control | **Critical** | 5.3, 6.2, 8.2 | AC-6, AU-12, AT-3 | Foundational–Advanced |
| ASI10 | Cascading Agent Failures | **Critical** | 5.6, 6.2, 7.2 | SC-5, SI-17, AU-12 | Hardening–Advanced |

---

## Audience tags

- **OT security engineer** — full file, primary implementation reference
- **Federal agency security officer** — SP 800-53 control mapping, FISMA alignment
- **ICS/SCADA security architect** — Section 7 network architecture references
- **CISO (critical infrastructure)** — Section 6 risk management, Section 8 programme
- **AI/OT integration team** — agent placement guidance, tool permission controls
- **CMMC / FedRAMP assessor** — SP 800-53 control identifiers per ASI entry

---

## SP 800-82 Rev 3 network architecture: agent placement

SP 800-82 Rev 3 recommends a defence-in-depth architecture. Autonomous
agents must be placed explicitly within this architecture — they must
never be assumed to fit within an existing zone without deliberate design.

**Recommended agent placement per SP 800-82 Rev 3 Appendix G:**

```
Enterprise Zone (Level 4-5)
    ↓ [Firewall + proxy — HTTPS only, no direct OT protocol access]
DMZ / Demilitarized Zone (Level 3.5)
    → Agents with read-only OT data access SHOULD be deployed here
    → Agents with command capability MUST be isolated in a dedicated agent zone
    ↓ [Application-layer firewall — protocol-specific allow-listing]
OT Network Zone (Level 3 — Site Operations)
    → No agent should reside here; data flows up, commands verified before execution
    ↓ [Unidirectional gateway recommended for most data flows]
Control Zone (Level 2 — Supervisory)
Field Device Zone (Level 1 — Basic Control)
    → Agents MUST NOT have direct access to Level 1-2 devices
```

**Key constraint from SP 800-82 Section 7.1:**
Any autonomous system with command capability crossing zone boundaries
requires authenticated, logged, and human-confirmable action paths.

---

## Detailed mappings

---

### ASI01 — Prompt Injection in Agentic Systems

Adversarial instructions in OT sensor data, historian outputs, or
engineering documentation processed by agents hijack agent actions —
potentially issuing commands or altering configurations.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.3 | Vulnerabilities common to IT/OT | Injection via historian and SCADA data feeds |
| §6.2 | Risk assessment | Assess injection risk at every agent data ingestion point |
| §7.2 | Security controls for ICS | Input validation mandatory at OT data boundary |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SI-10 | Information Input Validation | Validate all OT data before agent processing |
| SI-3 | Malicious Code Protection | Content filtering on all agent inputs |
| AC-3 | Access Enforcement | Restrict which OT data sources can reach agent input |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Define trusted OT data sources; reject unverified data before agent processing
- Implement input validation on all historian, SCADA, and document feeds
- Log all OT data fed to agent with source and timestamp

**Tier 2 — Short-term:**
- Add instruction sanitisation layer at OT data ingestion boundary
- Red team: attempt injection via SCADA historian data
- Verify no injected instruction can reach Level 2/1 control plane

**Tier 3 — Strategic:**
- Continuous monitoring of agent decisions correlated with OT data anomalies
- SP 800-53 SI-10 automated validation in OT data pipeline CI/CD

---

### ASI02 — Excessive Permissions and Scope

Agents granted access to OT systems beyond their declared function —
SCADA write access, PLC configuration permissions, safety system reads
— create catastrophic blast radius when compromised.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.3 | Common ICS vulnerabilities | Excessive privilege is specifically listed as OT vulnerability class |
| §6.2 | Risk assessment | Assess agent permission scope as part of OT risk register |
| §7.1 | Secure architecture | Least privilege must be enforced at zone boundary for all automated systems |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| AC-6 | Least Privilege | Minimum OT access per agent role; enforce at zone boundary |
| AC-3 | Access Enforcement | Enforce agent identity and access policy at OT network boundary |
| AU-12 | Audit Record Generation | Log every agent action in OT zone with full context |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Document minimum OT permissions required for each agent function
- Remove any OT access not exercised in past 30 days
- Treat agent OT access as privileged account: apply same controls as human OT admin

**Tier 2 — Short-term:**
- Implement per-task JIT OT permission issuance (see RECIPES.md)
- Architecture review: confirm no agent has direct write access to Level 1-2 devices
- Quarterly OT permission audit for all agent identities

**Tier 3 — Strategic:**
- SP 800-53 AC-6 enforcement via OT network access control system
- Formal agent identity programme with OT-specific NHI controls

---

### ASI03 — Memory Manipulation and Persistence

Corrupted agent memory causes agents to act on false OT state — misreporting
equipment status, misremembering maintenance history, or carrying persistent
attacker instructions across sessions into OT decision-making.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.3 | ICS vulnerabilities | Memory corruption and state manipulation |
| §6.2 | Risk assessment | Assess agent memory stores as OT data integrity risk |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SI-7 | Software, Firmware, and Information Integrity | Integrity verification for agent memory stores |
| SC-28 | Protection of Information at Rest | Encrypt and access-control all persistent agent memory |
| AC-3 | Access Enforcement | Restrict write access to agent memory stores |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Apply access controls to all agent memory stores
- Add integrity metadata (HMAC) to all OT-state memory writes
- Log all memory read/write operations

**Tier 2 — Short-term:**
- Implement memory validation pipeline for all OT state information
- Periodic memory audit: compare agent's stored OT state with ground truth
- Red team: attempt memory poisoning via OT data feeds

**Tier 3 — Strategic:**
- Formal provenance tracking for all OT state stored in agent memory
- Cross-session memory integrity checks before any OT decision

---

### ASI04 — Multi-Agent Trust Exploitation

Compromised agents in multi-agent OT orchestration networks are trusted
by peer agents — enabling instruction injection, lateral movement across
OT zones, and coordinated action against industrial infrastructure.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.3 | ICS vulnerabilities | Lateral movement between control systems |
| §6.2 | Risk assessment | Assess inter-agent trust as OT risk |
| §7.2 | Security controls | Authenticate all automated system-to-system communications |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| IA-3 | Device Identification and Authentication | Authenticate all agent-to-agent communications |
| AC-3 | Access Enforcement | Enforce per-agent trust boundaries |
| AU-12 | Audit Record Generation | Log all inter-agent instructions |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Implement mutual authentication between all agents in OT orchestration network
- No agent may issue commands exceeding its own permission set to peer agents
- Log all inter-agent instructions with full payload

**Tier 2 — Short-term:**
- Agent identity registry: all OT agents have verifiable identities
- Red team: simulate compromised sub-agent attempting lateral movement to OT zone
- Architecture review: trust graph for all agent-to-agent communications

**Tier 3 — Strategic:**
- Cryptographic attestation of agent identity and OT permission set
- Automated verification that no agent in network exceeds declared OT scope

---

### ASI05 — Tool and Plugin Abuse

Malicious or misconfigured tools accessible to OT agents — SCADA
connectors, historian APIs, engineering workstation integrations —
enable unintended data access or command issuance via the tool interface.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.5 | Supply chain risks | Third-party tool components in OT |
| §6.3 | Supply chain risk management | Tool integration approval process |
| §8.4 | Third-party management | Vendor assessment for OT tool providers |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SA-12 | Supply Chain Protection | Assess all OT tool vendors |
| CM-7 | Least Functionality | Allow-list only approved tools; deny all others |
| SR-3 | Supply Chain Controls and Plans | Document tool supply chain controls |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Enumerate all tools accessible to OT agents
- Remove any unreviewed tools from OT agent configuration
- Validate all tool descriptors against declared function

**Tier 2 — Short-term:**
- Implement tool approval board for all OT-connected tool integrations
- Add tool call logging with full payload for all OT tool invocations
- Red team: provide malicious tool descriptor to OT agent

**Tier 3 — Strategic:**
- SA-12 formal vendor assessment for all OT tool providers
- Automated tool supply chain scanning in OT CI/CD pipeline

---

### ASI06 — Data Exfiltration via Agentic Channels

Agents with OT data access and outbound communication capabilities
exfiltrate process data, equipment configurations, safety parameters,
or intellectual property via tool calls, API requests, or generated outputs.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.4 | Data confidentiality risks in OT | OT data exfiltration via compromised automation |
| §6.2 | Risk assessment | Assess outbound data paths from agent |
| §7.3 | Network monitoring | Monitor all outbound data from OT zone |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SC-28 | Protection of Information at Rest | Classify and protect all OT data accessible to agents |
| AC-3 | Access Enforcement | Enforce read scope per agent; minimum OT data access |
| AU-9 | Protection of Audit Information | Secure audit logs of agent data access |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Apply content inspection to all agent outputs leaving OT boundary
- Define maximum data volume per tool call from OT zone
- Log all outbound data with full payloads

**Tier 2 — Short-term:**
- DLP scanning on all agent output leaving OT boundary
- Red team: SSRF-style exfiltration via OT tool calls
- Implement per-session OT data access budgets

**Tier 3 — Strategic:**
- O-IM: automated exfiltration detection using OT data flow baselines
- Data residency controls: OT data must not leave defined geographic or network boundary

---

### ASI07 — Supply Chain Compromise in Agent Ecosystems

Third-party components in the agentic OT stack — orchestration frameworks,
MCP servers, ML libraries — are compromised, introducing malicious behaviour
into the OT agent deployment.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.5 | Supply chain risks | Expanded to include agentic AI components |
| §6.3 | Supply chain risk management | SBOM and vendor assessment for agentic stack |
| §8.4 | Third-party management | Formal vendor programme for OT agent components |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SA-12 | Supply Chain Protection | Vendor assessment for all agentic stack components |
| SR-3 | Supply Chain Controls and Plans | SBOM for agentic OT deployment |
| SR-6 | Supplier Assessments and Reviews | Periodic review of all agentic component suppliers |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Generate SBOM for agentic OT deployment; flag unverified components
- Pin all dependency versions; reject floating versions in OT production
- Verify provenance of all ML components used in OT agent stack

**Tier 2 — Short-term:**
- Implement automated vulnerability scanning for agentic SBOM
- SA-12: formal vendor assessment for critical agentic stack components
- Periodic red team exercise targeting agentic supply chain attack vectors

**Tier 3 — Strategic:**
- SR-6: annual supplier review for all agentic component vendors
- Formal component integrity programme aligned with CISA software security guidance

---

### ASI08 — Inversion of Safety Controls

Safety guardrails protecting OT agent behaviour are bypassed — enabling
agents to issue commands that violate safety parameters, bypass interlocks,
or disable protective functions in industrial systems.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.3 | ICS vulnerabilities | Safety system bypass is the highest severity OT threat |
| §6.2 | Risk assessment | Safety control inversion must be in OT risk register |
| §7.1 | Secure architecture | Mandatory: safety function must be independent of AI decision layer |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SI-3 | Malicious Code Protection | Protect safety control logic from AI-driven modification |
| AC-6 | Least Privilege | AI system must not have write access to safety function parameters |
| AU-12 | Audit Record Generation | Immutable logging of all safety-adjacent agent actions |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate (absolute requirement):**
- Safety functions must be hardware-enforced and independent of AI layer
- AI agents must not have write access to any safety interlock parameters
- Confirm: AI system failure or compromise cannot affect safety system state

**Tier 2 — Short-term:**
- Independent adversarial testing of all safety guardrail bypass scenarios
- Architecture review: safety control path analysis for all agent-reachable systems
- Immutable safety action log that cannot be disabled or modified by AI layer

**Tier 3 — Strategic:**
- Formal safety case documentation for all agentic OT deployments
- Continuous adversarial safety testing in staging environment
- Periodic safety architecture review by independent safety engineer

---

### ASI09 — Inadequate Human Oversight and Control

Agents take OT actions — equipment commands, configuration changes,
setpoint adjustments — without human review, removing the oversight
layer that would detect errors, adversarial manipulation, or safety
boundary violations before they cause physical consequences.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.3 | ICS vulnerabilities | Inadequate human oversight cited as OT vulnerability category |
| §6.2 | Risk assessment | Quantify consequences of unsupervised agent OT actions |
| §8.2 | OT security programme | Governance policy for autonomous OT systems |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| AC-6 | Least Privilege | Autonomous OT actions constrained to minimum necessary scope |
| AU-12 | Audit Record Generation | Every autonomous OT action logged with rationale |
| AT-3 | Role-Based Training | OT operators trained to monitor, intervene, and override agents |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Add human confirmation gate for all irreversible OT actions
- Implement emergency stop: immediately halt all agent OT activity
- Log every autonomous OT action with decision rationale

**Tier 2 — Short-term:**
- Define autonomy tiers for OT actions: auto / confirm / human-required
- AT-3: operator training programme for agentic OT oversight
- Implement autonomous action budget: configurable hard limit per session

**Tier 3 — Strategic:**
- Real-time OT oversight dashboard for operations team
- AU-12 L3: forensic-quality audit log for all autonomous OT actions
- Formal autonomy policy reviewed and signed by CISO and safety officer

---

### ASI10 — Cascading Agent Failures

Failures in multi-agent OT orchestration propagate — corrupted state
from one agent cascades into downstream agents, amplifying errors
across the OT system and potentially triggering correlated failures
in multiple industrial components.

#### SP 800-82 Rev 3 mapping

| Section | Requirement | How it applies |
|---|---|---|
| §5.6 | Availability risks | Cascading failure across OT components |
| §6.2 | Risk assessment | Cascade failure scenarios in OT risk register |
| §7.2 | Security controls | Circuit breakers between OT automation layers |

#### SP 800-53 controls

| Control | Title | Application |
|---|---|---|
| SC-5 | Denial-of-Service Protection | Rate limiting and circuit breakers prevent cascade amplification |
| SI-17 | Fail-Safe Procedures | Define fail-safe state for every autonomous OT action |
| AU-12 | Audit Record Generation | Log cascade indicators for post-incident forensics |

#### Three-tier mitigations

**Tier 1 — Pre-deployment gate:**
- Define fail-safe state for every agent-controllable OT parameter
- Implement circuit breaker pattern between OT orchestration layers
- Document cascade blast radius: if agent X fails, what OT components are affected?

**Tier 2 — Short-term:**
- Chaos engineering exercise: simulate cascading failure in staging
- Deploy O-IM playbook for cascade incidents in OT environment
- Add per-agent OT action checkpointing for rollback capability

**Tier 3 — Strategic:**
- Formal OT chaos engineering programme aligned with SP 800-82 §8
- Automated cascade detection with predictive alerting before full failure
- Architecture pattern: stateless agents with OT state sourced from authoritative systems

---

## OT pre-deployment checklist — agentic AI

Complete this checklist before deploying any autonomous AI agent in an OT environment.

| Item | Requirement | SP 800-82 Ref | Status |
|---|---|---|---|
| Zone placement | Agent deployed in correct SP 800-82 zone | §7, App G | ☐ |
| Permission scope | Minimum OT permissions documented and enforced | §7.1 | ☐ |
| Command capability | All command paths require human confirmation | §7.1 | ☐ |
| Safety independence | Safety function independent of AI layer | §5.3 | ☐ |
| Audit logging | All agent OT actions logged to immutable log | §7.3 | ☐ |
| Emergency stop | Kill switch tested and accessible to operators | §8.2 | ☐ |
| Supply chain | SBOM generated for agentic stack | §8.4 | ☐ |
| Operator training | OT operators trained on agent oversight | §8.2 | ☐ |
| Incident playbook | Cascade failure playbook documented | §6.2 | ☐ |
| Risk assessment | Agentic AI scenarios in OT risk register | §6.2 | ☐ |

---

## U.S. regulatory crosswalk

| Regulation | Applicability | Relevant agentic AI requirements |
|---|---|---|
| NERC CIP-007 | Electric utility OT | System security management for any automated system with BES access |
| NERC CIP-013 | Electric utility supply chain | SBOM and vendor assessment for agentic stack components |
| AWIA 2018 | Water utilities | Risk assessment must include autonomous system threat scenarios |
| CMMC Level 2 | DoD contractors | SP 800-53 AC-6, AU-12, SI-7, SI-10 required for autonomous OT systems |
| FISMA | Federal agencies | All SP 800-53 controls apply; agentic AI in OT requires ISSO review |
| TSA Directives | Pipeline operators | Autonomous system access to pipeline control systems requires security review |

---

## References

- [NIST SP 800-82 Rev 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) — May 2023
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Security and Privacy Controls
- [Agentic_ISA62443.md](Agentic_ISA62443.md) — complementary zone model and SL ratings
- [LLM_NISTSP80082.md](../llm-top10/LLM_NISTSP80082.md) — LLM entry mapping
- [OWASP Top 10 for Agentic AI Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [shared/RECIPES.md](../shared/RECIPES.md) — OT kill switch and JIT credential patterns

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping ASI01–ASI10 to SP 800-82 Rev 3 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
