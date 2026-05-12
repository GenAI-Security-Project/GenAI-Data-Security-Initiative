<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : ISA/IEC 62443 — Industrial Automation and Control Systems Security
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × ISA/IEC 62443

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
— the international standard series for Industrial Automation and
Control Systems (IACS) security, widely mandated across energy, water,
manufacturing, oil and gas, transportation, and critical infrastructure.

---

## Why this mapping exists

LLMs are entering OT environments faster than most security teams
recognise. The use cases are already in production:

- Predictive maintenance copilots querying historian databases
- Natural-language interfaces to SCADA and DCS systems
- AI-assisted anomaly detection in process control networks
- Digital twin orchestration with LLM planning layers
- Operator decision-support systems in control rooms
- Automated incident report generation from sensor data

The blast radius when an LLM system operating in or adjacent to an OT
network is compromised is categorically different from IT. Prompt
injection reaching an NL-to-SCADA interface is not a data breach —
it is a process disruption event with potential physical consequences.

ISA/IEC 62443 is the framework OT security engineers actually use.
This mapping translates OWASP LLM Top 10 risks into the language,
zones, conduits, security levels, and foundational requirements that
OT practitioners work with every day.

---

## ISA/IEC 62443 structure

| Series | Title | Relevance |
|---|---|---|
| 62443-1-1 | Terminology, concepts, and models | Zones, conduits, security levels, IACS definition |
| 62443-2-1 | IACS security management system | Security programme requirements — relevant to LLM governance |
| 62443-3-2 | Security risk assessment | Risk assessment methodology — zone/conduit model |
| 62443-3-3 | System security requirements and SLs | System-level Security Requirements (SRs) — primary control reference |
| 62443-4-1 | Secure product development requirements | Development lifecycle — relevant to LLM integration development |
| 62443-4-2 | Technical security requirements | Component-level requirements — relevant to LLM components |

**Security Levels (SL):**

| SL | Protection against |
|---|---|
| SL 1 | Casual or unintentional violation |
| SL 2 | Intentional violation using simple means with low motivation |
| SL 3 | Intentional violation using sophisticated means with moderate motivation |
| SL 4 | Intentional violation using sophisticated means with high motivation — state-sponsored |

**Foundational Requirements (FRs) from 62443-3-3:**

| FR | Name |
|---|---|
| FR 1 | Identification and Authentication Control (IAC) |
| FR 2 | Use Control (UC) |
| FR 3 | System Integrity (SI) |
| FR 4 | Data Confidentiality (DC) |
| FR 5 | Restricted Data Flow (RDF) |
| FR 6 | Timely Response to Events (TRE) |
| FR 7 | Resource Availability (RA) |

---

## Quick-reference summary

| ID | Name | OT Severity | Primary 62443 FRs / SRs | Minimum SL | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | **Critical** in OT | FR 3 SI-3, FR 2 UC-2, FR 1 IAC-6 | SL 2–3 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | FR 4 DC-4, FR 5 RDF-1, FR 1 IAC-2 | SL 2 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | FR 3 SI-2, FR 2 UC-6, 62443-2-4 | SL 2 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | **Critical** in OT | FR 3 SI-3, FR 3 SI-7, FR 6 TRE-1 | SL 2–3 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | FR 3 SI-3, FR 2 UC-3, FR 3 SI-1 | SL 2 | Foundational–Hardening |
| LLM06 | Excessive Agency | **Critical** in OT | FR 2 UC-2, FR 2 UC-6, FR 1 IAC-2 | SL 2–3 | Foundational–Advanced |
| LLM07 | System Prompt Leakage | Medium | FR 4 DC-4, FR 3 SI-1, FR 5 RDF-1 | SL 2 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | FR 3 SI-7, FR 4 DC-3, FR 3 SI-3 | SL 2 | Hardening–Advanced |
| LLM09 | Misinformation | High in OT | FR 3 SI-1, FR 6 TRE-2, FR 2 UC-3 | SL 2 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | **Critical** in OT | FR 7 RA-6, FR 7 RA-7, FR 6 TRE-6 | SL 2 | Foundational–Advanced |

**OT severity note:** Several vulnerabilities rated Medium or High in
IT contexts are elevated to High or Critical in OT environments due
to physical consequence potential. These are marked above and explained
in each entry.

---

## Audience tags

- **OT security engineer** — full file, primary reference
- **ICS security architect** — zone/conduit model sections
- **CISO (critical infrastructure)** — SL mapping and governance sections
- **Control system engineer** — LLM01, LLM06, LLM10 entries
- **Procurement / vendor assessment** — 62443-2-4, supply chain entries
- **Compliance (NERC CIP, NIS2, CFATS)** — full file with regulatory crosswalk notes

---

## Zone and conduit model — where LLMs sit

ISA/IEC 62443 organises IACS into security zones connected by conduits.
LLMs in OT environments typically introduce new zones or bridge existing
ones in ways the original zone model did not anticipate:
```
Zone 4: Enterprise / IT network
    |
    | [Conduit — DMZ / data diode / unidirectional gateway]
    |
Zone 3: Operations / SCADA / historian
    |     ? LLMs most commonly deployed here or at this boundary
    | [Conduit — strictly controlled]
    |
Zone 2: Control network / DCS
    |
    | [Conduit — minimal, monitored]
    |
Zone 1: Field devices / PLCs / RTUs
```

**LLM deployment patterns and their zone risk:**

| Deployment pattern | Zone location | Primary risks |
|---|---|---|
| Predictive maintenance copilot | Zone 3 or Zone 3/4 boundary | LLM01, LLM02, LLM06 |
| NL-to-SCADA / NL-to-historian gateway | Zone 3 | LLM01, LLM05, LLM06, LLM10 |
| Operator decision-support system | Zone 3 | LLM09, LLM01 |
| Digital twin orchestration | Zone 3/4 boundary | LLM04, LLM06, LLM10 |
| Anomaly detection / alert triage | Zone 3 | LLM04, LLM09 |
| Incident report generation | Zone 3/4 boundary | LLM02, LLM07 |

**Key principle:** LLMs must never be deployed in Zone 2 or Zone 1.
Any LLM integration must be behind at least one conduit from control
systems. If an LLM needs to send commands to Zone 2 or below, those
commands must pass through a validated, approved command gateway with
human-in-the-loop confirmation — not directly from the LLM output.

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**OT Severity:** Critical (elevated from High — NL-to-SCADA makes
this a process disruption vector, not just a data risk)

Malicious instructions in input or processed content manipulate LLM
behaviour. In OT environments, the impact is not limited to data
exfiltration — an LLM with any connection to control system interfaces
can be manipulated to generate incorrect commands, suppress alarms,
or trigger unintended process actions.

**OT-specific threat scenario:**
An operator pastes an incident report into an LLM-powered maintenance
assistant. The report contains indirect prompt injection from a
compromised external system. The LLM generates a work order that
recommends shutting down a safety-critical valve during peak operating
conditions — plausible enough that the operator approves it without
verification.

**Real-world reference:**
- Multiple documented cases of LLM assistants connected to enterprise
  historian databases being manipulated through crafted query content
  to generate misleading process recommendations (2024)

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | All inputs to LLMs connected to OT systems validated for integrity — crafted inputs rejected |
| Least privilege | SR 2.2 | FR 2 — Use Control | LLMs granted minimum necessary access to OT data — cannot read or write to control systems without explicit scoping |
| Use control enforcement | SR 2.1 | FR 2 — Use Control | Enforcement of permitted use of LLM within OT context — out-of-scope requests rejected at the gateway layer |
| Authenticator feedback | SR 1.6 | FR 1 — IAC | LLM interactions logged with user identity — injection attempts attributable to specific sessions |
| Remote session termination | SR 1.9 | FR 1 — IAC | Ability to terminate LLM sessions immediately on detection of suspicious behaviour |

#### Zone and conduit controls

**Zone placement:**
- LLMs must reside in Zone 3 (operations zone) or Zone 4 (enterprise)
- No LLM process may have direct write access to Zone 2 or below
- Conduit between LLM and Zone 3 historian/SCADA must enforce
  read-only by default with explicit write allowlisting

**Conduit requirements for NL-to-control interfaces:**
- Input validation at the conduit — reject inputs containing
  injection indicators before reaching the LLM
- Command validation at the conduit — validate LLM-generated
  commands against a predefined safe command set before execution
- Human-in-the-loop gate — any command to Zone 2 or below
  requires human confirmation regardless of LLM confidence

#### Mitigations by tier

**Foundational (SL 1–2)**
- Implement input validation at the conduit boundary — do not
  pass raw external content directly to LLMs connected to OT
- Classify all content entering LLM context from OT data sources
  as untrusted — historian data, sensor readings, operator logs
- Deploy SR 2.2 least-privilege controls — LLM access scoped
  to specific historian tags or SCADA read-only endpoints,
  never full write access

**Hardening (SL 2–3)**
- Implement prompt injection detection at the Zone 3 boundary —
  filter inputs before they reach LLM processing
- Require human approval for any LLM recommendation that results
  in a control action — SR 2.1 use control enforcement
- Maintain full audit log of all LLM inputs, outputs, and any
  control actions attributable to LLM recommendations

**Advanced (SL 3–4)**
- Implement architectural separation between LLM advisory function
  and any control action execution path — LLM can never directly
  trigger a control action, only make a recommendation that passes
  through a validated command gateway with human approval
- Deploy adversarial testing of LLM integrations against OT
  scenarios — indirect injection through historian, alarm, and
  work order data
- Conduct tabletop exercises simulating LLM-mediated process
  disruption scenarios — include in OT incident response planning

#### Tools

| Tool | Type | Link |
|---|---|---|
| Claroty | Commercial | https://claroty.com |
| Dragos | Commercial | https://www.dragos.com |
| Garak (for adversarial testing) | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: NIST SP 800-82 Rev 3 Section 5 · MITRE ATT&CK ICS T0855 · NERC CIP-007

---

### LLM02 — Sensitive Information Disclosure

**OT Severity:** High

LLMs with access to OT data — process parameters, equipment
specifications, network topology, safety system configurations —
can disclose operational intelligence that enables targeted physical
attacks, sabotage, or competitive espionage.

**OT-specific threat scenario:**
A predictive maintenance LLM with read access to the historian
surfaces detailed equipment specifications, failure modes, and
maintenance schedules in response to crafted queries — giving an
adversary the reconnaissance data needed to plan a targeted
physical or cyber attack on specific assets.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Data confidentiality in transit | SR 4.1 | FR 4 — Data Confidentiality | All OT data accessed by LLMs encrypted in transit — no cleartext historian queries over OT network |
| Data confidentiality at rest | SR 4.2 | FR 4 — Data Confidentiality | OT data used in LLM context or stored by LLM components encrypted at rest |
| Information flow restriction | SR 5.1 | FR 5 — Restricted Data Flow | LLM outputs containing OT data restricted to authorised users — no unrestricted external output |
| Identification and authentication | SR 1.2 | FR 1 — IAC | All LLM access to OT data systems requires authenticated, authorised identity |

#### Zone and conduit controls

- Data flowing from Zone 3 historian to LLM must pass through
  a data classification filter — strip or redact sensitive
  process parameters, equipment IDs, and network topology data
  before injection into LLM context
- LLM outputs containing OT data must be reviewed before
  external transmission — no direct API output to untrusted
  external systems from an LLM with OT data access
- Conduit from Zone 3 to Zone 4 must enforce data diode
  principles where feasible — data flows out of OT, not in

#### Mitigations by tier

**Foundational (SL 1–2)**
- Classify all OT data by sensitivity before granting LLM access —
  safety system configurations, network topology, and equipment
  specifications require higher clearance than production metrics
- Implement SR 5.1 information flow restriction — LLM cannot
  output OT data to any destination not explicitly authorised
- Audit all LLM access to OT data sources — log every query,
  every data element accessed, every output generated

**Hardening (SL 2–3)**
- Implement output redaction for sensitive OT identifiers —
  equipment tags, IP addresses, safety function identifiers
  masked before leaving Zone 3 boundary
- Restrict LLM read access to minimum required historian tags —
  no broad SELECT * access to historian databases
- SR 4.1/4.2: Enforce encryption on all OT-LLM data paths

**Advanced (SL 3–4)**
- Implement need-to-know access controls on historian data
  fed to LLM — operator-class data access, not engineer-class
- Deploy data loss prevention on all LLM output channels in
  OT context — OT-specific patterns (tag IDs, device names,
  network addresses) detected and blocked
- Conduct OT data disclosure red team exercises — attempt
  to extract operational intelligence through crafted LLM
  queries against your specific historian configuration

#### Tools

| Tool | Type | Link |
|---|---|---|
| Nozomi Networks | Commercial | https://www.nozominetworks.com |
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage
- Other frameworks: NIST SP 800-82 Rev 3 Section 6 · IEC 62351 (power systems) · NERC CIP-011

---

### LLM03 — Supply Chain Vulnerabilities

**OT Severity:** High

LLM components, model weights, and plugins introduced into OT
environments inherit OT supply chain criticality. A backdoored
LLM component in a Zone 3 maintenance assistant is a persistent
threat actor inside the industrial network perimeter.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Software and information integrity | SR 3.2 | FR 3 — System Integrity | Integrity verification of all LLM components before deployment in OT environment |
| Use control | SR 2.6 | FR 2 — Use Control | Restrictions on software installation — only approved, verified LLM components permitted in OT zones |
| 62443-2-4 | Supplier security requirements | — | Security requirements applied to all LLM vendors with access to OT environments |

#### Zone and conduit controls

- Apply OT change management processes to all LLM component
  updates — no automatic model weight updates in OT environments
- Treat LLM model versions as IACS software components — subject
  to the same approval, testing, and rollback procedures as
  SCADA software updates
- Conduit controls must block unapproved LLM component downloads —
  LLM components for OT deployment approved and staged from
  a controlled repository, never pulled from public internet
  from within the OT network

#### Mitigations by tier

**Foundational (SL 1–2)**
- Apply 62443-2-4 supplier security requirements to all LLM
  vendors with components deployed in OT environments —
  provenance, integrity guarantees, and vulnerability disclosure
  obligations contractually required
- Maintain ML SBOM for every LLM component in OT deployment —
  model, adapters, libraries, and inference runtime
- Pin all LLM component versions — no dynamic updates in
  production OT environments

**Hardening (SL 2–3)**
- SR 3.2: Verify cryptographic signatures of all LLM components
  before deployment in OT environment — unsigned components
  rejected at the OT network boundary
- Apply OT change management to LLM model updates — test in
  a representative non-production environment before OT deployment
- Scan all LLM components for embedded backdoors before
  each OT deployment — ModelScan or equivalent

**Advanced (SL 3–4)**
- Implement isolated model evaluation environment — LLM
  components evaluated for backdoor behaviour in an air-gapped
  test environment before promotion to OT production
- 62443-2-4: Require vendor security attestation for each
  LLM component update — signed statement of security testing
  coverage and known vulnerability status
- Establish responsible disclosure relationship with LLM
  vendors — OT-specific vulnerability notification path
  with defined SLA

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| CycloneDX | Open-source | https://cyclonedx.org |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 · NIST SP 800-218A · NERC CIP-013

---

### LLM04 — Data and Model Poisoning

**OT Severity:** Critical (elevated — poisoned process recommendations
can cause physical harm)

Adversaries corrupt training data or model weights to embed backdoors
that cause the LLM to generate incorrect process recommendations,
suppress safety alarms, or provide false operational guidance —
effects that may not manifest until a specific trigger condition
is reached during operations.

**OT-specific threat scenario:**
A threat actor compromises the training pipeline for an LLM used for
alarm rationalisation. A backdoor is embedded that, when a specific
combination of process conditions appears, causes the model to classify
a genuine safety alarm as a nuisance alarm — suppressing operator
response to an actual process upset.

**Real-world reference:**
- Research demonstrating that LLMs used for industrial decision support
  can be poisoned to produce systematically incorrect recommendations
  for specific equipment types or process conditions (2024–2025)

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | LLM model integrity verified before each OT deployment — poisoning detection as integrity control |
| Software and information integrity (monitoring) | SR 3.7 | FR 3 — System Integrity | Continuous monitoring of LLM outputs for anomalous recommendations — statistical deviation detection |
| Timely response to events | SR 6.1 | FR 6 — TRE | Detection and response to poisoning indicators — LLM output anomalies treated as security events |

#### Zone and conduit controls

- All data sourced from OT historian or SCADA for LLM training
  must pass through a data integrity gate — cryptographic
  lineage from source to training dataset
- LLM training pipelines for OT-deployed models must be
  air-gapped or strictly isolated — no internet-connected
  training infrastructure for models deployed in Zone 3
- Implement output monitoring in Zone 3 — LLM recommendations
  cross-checked against a physics-based or rule-based reference
  model for plausibility before display to operator

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.3: Implement model integrity verification before each
  OT deployment — hash-based integrity check, deviation from
  approved baseline triggers rejection
- Validate LLM outputs against independent rule-based checks
  for all safety-relevant recommendations — LLM is advisory,
  never authoritative, on safety-critical decisions
- Establish model rollback capability — approved baseline
  version always available for immediate revert

**Hardening (SL 2–3)**
- SR 3.7: Implement continuous output monitoring — statistical
  anomaly detection on LLM recommendation distributions,
  alert on deviation from established baseline
- Apply adversarial testing covering OT-specific poisoning
  scenarios — alarm suppression, incorrect setpoint
  recommendation, false equipment health assessment
- Conduct post-training backdoor detection before each
  OT deployment — treat as mandatory security gate

**Advanced (SL 3–4)**
- SR 6.1: Integrate LLM output anomaly detection into
  OT SIEM — poisoning indicators treated as security events
  with defined response procedures
- Implement independent safety validation layer — LLM
  recommendations for safety-relevant actions cross-validated
  against SIS (Safety Instrumented System) logic before display
- Establish OT-specific threat intelligence on AI model
  poisoning campaigns targeting industrial sectors

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| Claroty (OT monitoring) | Commercial | https://claroty.com |
| Dragos | Commercial | https://www.dragos.com |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 · MITRE ATT&CK ICS T0831 · NERC CIP-010

---

### LLM05 — Insecure Output Handling

**OT Severity:** High

LLM-generated output passed to downstream OT systems without
validation can enable injection into SCADA interfaces, HMI rendering,
historian write-back, or work order systems — turning LLM output
into an OT attack vector.

**OT-specific threat scenario:**
An LLM-generated maintenance work order is rendered in an HMI without
output sanitisation. The LLM output contains a crafted string that
exploits a known parsing vulnerability in the HMI software, enabling
code execution on the HMI workstation in Zone 3.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | All LLM output validated before rendering or passing to OT systems |
| Use control | SR 2.3 | FR 2 — Use Control | LLM output restricted to authorised actions — no raw output directly to control interfaces |
| Software and information integrity | SR 3.1 | FR 3 — System Integrity | Communication integrity enforcement on all LLM-to-OT data paths |

#### Zone and conduit controls

- Conduit from LLM output to Zone 3 systems must implement
  output schema validation — only outputs conforming to a
  predefined safe structure pass the conduit
- LLM-generated commands to any OT system must be validated
  against an approved command set at the conduit — no raw
  LLM output reaches Zone 2 or below
- HMI and SCADA rendering layers must sanitise all LLM-sourced
  content — treat as untrusted input regardless of source

#### Mitigations by tier

**Foundational (SL 1–2)**
- Treat all LLM output as untrusted input to OT systems —
  encode, validate, and sanitise before rendering or passing
  to any Zone 3 component
- SR 2.3: Implement output allowlisting — only predefined
  output formats accepted by OT interfaces, all other
  formats rejected at the boundary
- Never pass raw LLM output directly to historian write-back,
  work order systems, or HMI rendering — always through
  a validated formatting layer

**Hardening (SL 2–3)**
- SR 3.3: Implement output schema validation as a conduit
  control — LLM output parsed and validated before crossing
  any zone boundary
- Apply OT-specific output sanitisation — strip or reject
  any LLM output containing HTML, script tags, or control
  characters before presentation to OT systems
- Test all OT interfaces that consume LLM output for injection
  vulnerabilities — include in OT penetration testing scope

**Advanced (SL 3–4)**
- Implement a dedicated LLM output validation gateway between
  Zone 4/3 LLM and Zone 3 OT systems — independent validation
  layer not controlled by the LLM
- Conduct adversarial output testing specifically targeting
  your OT HMI and SCADA parsing — test LLM output injection
  against real OT system interfaces
- SR 3.1: Enforce communication integrity on all LLM-to-OT
  paths — message authentication codes on all LLM output
  destined for OT systems

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: NIST SP 800-82 Rev 3 · MITRE ATT&CK ICS T0855 · CWE-79

---

### LLM06 — Excessive Agency

**OT Severity:** Critical (elevated — autonomous action in OT has
physical consequence potential that IT autonomous action does not)

LLMs with excessive autonomy over OT interfaces — historian write-back,
work order execution, setpoint adjustment, alarm management — can
execute unintended or manipulated control actions when their goal is
hijacked or their inputs are crafted.

**This is the most critical LLM vulnerability for OT environments.**
The principle of least agency — grant the minimum autonomy required
for safe, bounded tasks — must be applied with zero tolerance in OT.

**OT-specific threat scenario:**
An LLM-powered digital twin orchestration system is manipulated through
indirect prompt injection in equipment telemetry data. The LLM
autonomously adjusts setpoints on a process control system, believing
it is optimising performance — but the adjustment triggers a process
upset requiring emergency shutdown.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Least privilege | SR 2.2 | FR 2 — Use Control | LLMs granted minimum necessary permissions to OT systems — read-only by default, no autonomous write |
| Use control enforcement | SR 2.1 | FR 2 — Use Control | All LLM actions in OT context subject to explicit use controls — no autonomous action without human confirmation |
| User authentication | SR 1.2 | FR 1 — IAC | LLM actions in OT context authenticated as a distinct identity — traceable in OT audit log |
| Session lock | SR 1.9 | FR 1 — IAC | LLM sessions with OT access can be locked and terminated immediately by operators |

#### Zone and conduit controls

**Hard rule — no exceptions:**
LLMs must never autonomously execute control actions at Zone 2 or
below. Any LLM integration that needs to influence process control
must do so through:

1. A recommendation displayed to a human operator
2. Human confirmation captured through a separate, non-LLM interface
3. A validated command gateway that enforces the approved command
   set and logs the human confirmation

**Zone 3 LLM autonomous write permissions:**
- Historian write-back: Requires human confirmation for each write
- Work order creation: Requires human approval before execution
- Alarm acknowledgement: LLM cannot acknowledge alarms autonomously
- Setpoint adjustment: Never autonomous — human confirmation mandatory

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 2.2: Implement and enforce least-privilege access for
  all LLMs in OT environments — read-only to historian and
  SCADA by default, no exceptions without documented justification
- Require explicit human confirmation for every control action
  recommended by an LLM — confirmation through a separate,
  independent interface, not through the LLM chat interface
- Log all LLM recommendations and human confirmations with
  full timestamp and operator identity — OT audit trail

**Hardening (SL 2–3)**
- SR 2.1: Implement formal use control enforcement — define
  the complete set of permitted LLM actions in OT context
  and enforce it at the conduit layer, not in the model
- Conduct regular reviews of LLM permission scope — any
  permission not actively used is removed
- Deploy OT-specific guardrails — LLM cannot generate
  recommendations outside a pre-defined safe parameter range
  for any process variable

**Advanced (SL 3–4)**
- Implement formal separation between LLM advisory and control
  execution — architectural guarantee that LLM output cannot
  become a control action without passing through a validated,
  human-controlled approval chain
- Conduct red team exercises testing LLM excessive agency
  through indirect injection in OT data sources — historian
  data, alarm logs, maintenance records
- Include LLM excessive agency scenarios in Process Hazard
  Analysis (PHA) and Safety Integrity Level (SIL) assessments

#### Tools

| Tool | Type | Link |
|---|---|---|
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| Claroty | Commercial | https://claroty.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: NIST SP 800-82 Rev 3 · IEC 61511 (safety systems) · MITRE ATT&CK ICS T0855

---

### LLM07 — System Prompt Leakage

**OT Severity:** Medium (elevated to High if prompt contains OT
network topology or safety system configuration)

System prompts for LLMs deployed in OT environments often contain
operationally sensitive information — network topology, equipment
identifiers, safety thresholds, and operational parameters. Extraction
of this information provides reconnaissance capability for targeted OT attacks.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Data confidentiality in transit | SR 4.1 | FR 4 — Data Confidentiality | System prompt content treated as sensitive OT configuration data — encrypted in transit |
| Software and information integrity | SR 3.1 | FR 3 — System Integrity | System prompt integrity protected — unauthorised modification detected |
| Information flow restriction | SR 5.1 | FR 5 — Restricted Data Flow | System prompt content cannot flow to unauthorised external destinations |

#### Mitigations by tier

**Foundational (SL 1–2)**
- Classify OT LLM system prompts as sensitive operational
  configuration — subject to same access controls as SCADA
  configuration files
- Remove all OT-specific identifiers from system prompts
  where possible — use generic references, resolve to
  specific assets at runtime through a controlled lookup
- SR 4.1: Encrypt system prompts at rest and in transit —
  do not store in cleartext in application configuration files

**Hardening (SL 2–3)**
- Implement prompt extraction testing against OT LLM
  deployments before go-live — test recovery of OT network
  topology and equipment data from the system prompt
- SR 5.1: Enforce information flow restriction — system prompt
  content cannot be output to any destination outside the
  authorised OT operator scope
- Rotate system prompt versions on schedule — limits shelf
  life of any extracted OT configuration data

**Advanced (SL 3–4)**
- Implement system prompt tokenisation for all OT-specific
  identifiers — equipment tags, IP addresses, and safety
  parameters replaced with opaque tokens resolved at runtime
- Include system prompt leakage in OT red team exercises —
  assess what OT reconnaissance value extracted prompts provide
- Apply SR 3.1 integrity protection to system prompts —
  hash verification on load, alert on modification

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: NIST SP 800-82 Rev 3 · NERC CIP-011 (BES Cyber System Information)

---

### LLM08 — Vector and Embedding Weaknesses

**OT Severity:** Medium (elevated if embedding stores contain OT
operational data or safety system documentation)

Vector stores used by OT LLMs — containing equipment documentation,
maintenance procedures, process parameters — are susceptible to
adversarial retrieval manipulation and embedding inversion attacks
that could surface incorrect technical guidance to operators.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Software and information integrity (monitoring) | SR 3.7 | FR 3 — System Integrity | Vector store content integrity monitored — alert on anomalous retrieval patterns |
| Data confidentiality | SR 4.3 | FR 4 — Data Confidentiality | Embeddings of sensitive OT documentation encrypted — inversion attack protection |
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | Vector store ingestion validated — only authorised OT documentation enters the corpus |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.3: Implement access controls on OT vector stores —
  RBAC enforced at collection level, operator-class access
  to operational content, restricted access to safety docs
- Classify all OT documentation before ingestion into vector
  stores — safety procedures require higher access tier
- SR 4.3: Encrypt all OT vector store content at rest

**Hardening (SL 2–3)**
- SR 3.7: Implement vector store query monitoring — alert
  on anomalous query patterns or unusual retrieval volumes
- Implement trust-tiered retrieval — safety-critical and
  vendor-sensitive documentation weighted by source trust,
  not only semantic similarity
- Apply content integrity verification on vector store
  ingestion — only hash-verified authorised documents admitted

**Advanced (SL 3–4)**
- Conduct embedding inversion testing against OT vector
  stores — validate that safety procedure details and
  equipment specifications cannot be reconstructed
- Implement adversarial retrieval testing — attempt to
  manipulate retrieval to surface incorrect maintenance
  procedures through crafted queries
- SR 3.7: Integrate vector store anomaly alerts into
  OT SIEM — unusual retrieval patterns treated as
  potential reconnaissance activity

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: NIST SP 800-82 Rev 3 · NIST AI RMF MS-2.5

---

### LLM09 — Misinformation

**OT Severity:** High (elevated — incorrect process guidance in OT
can cause equipment damage, environmental incidents, or personnel harm)

LLMs generate plausible but incorrect operational guidance —
incorrect maintenance procedures, incorrect setpoint recommendations,
incorrect alarm interpretations. In OT environments, operators
acting on LLM-generated misinformation can cause process upsets,
equipment damage, or safety incidents.

**OT-specific threat scenario:**
An LLM-powered troubleshooting assistant hallucinates a
maintenance procedure for an unfamiliar equipment variant —
the procedure is plausible but incorrect, leading an operator
to perform actions that damage the equipment and cause an
unplanned process shutdown.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Software and information integrity | SR 3.1 | FR 3 — System Integrity | LLM outputs for safety-relevant guidance cross-validated against authoritative sources |
| Timely response to events | SR 6.2 | FR 6 — TRE | Procedures for detecting and responding to LLM misinformation incidents |
| Use control | SR 2.3 | FR 2 — Use Control | LLM advisory outputs clearly distinguished from authoritative procedural documentation |

#### Mitigations by tier

**Foundational (SL 1–2)**
- Clearly distinguish LLM advisory output from authoritative
  OT documentation — operators must know when guidance is
  LLM-generated vs engineering-approved
- SR 2.3: Restrict LLM use in OT to specific advisory
  functions — never as the sole source for safety-critical
  procedures or setpoint recommendations
- Implement citation display — LLM recommendations must
  reference the source documentation they are based on,
  operators verify against the source before acting

**Hardening (SL 2–3)**
- SR 3.1: Implement cross-validation for LLM recommendations
  on safety-relevant procedures — independent rule-based
  check or engineering review before operator action
- Deploy RAG grounded on authoritative, version-controlled
  OT documentation — not on uncontrolled web content
- SR 6.2: Establish incident response for LLM misinformation
  events — process for identifying affected operations,
  correcting actions taken, and preventing recurrence

**Advanced (SL 3–4)**
- Implement OT-specific hallucination detection — test LLM
  accuracy on equipment-specific procedures for all equipment
  types in your plant before deployment
- Deploy confidence threshold controls — low-confidence
  LLM recommendations flagged prominently or escalated to
  engineering review before operator action
- Include LLM misinformation scenarios in operator training —
  ensure operators understand LLM limitations and verification
  requirements in OT context

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 · IEC 61511 (SIL) · AIUC-1 C/F

---

### LLM10 — Unbounded Consumption

**OT Severity:** Critical (elevated — resource exhaustion in OT
environments can directly affect process availability and safety systems)

Resource exhaustion caused by adversarial or accidental LLM query
overload can degrade OT network performance, overwhelm historian
databases, or consume processing capacity needed by safety-critical
systems. In Zone 3, availability is not a convenience requirement —
it is a safety requirement.

**OT-specific threat scenario:**
A threat actor bombards an LLM-powered maintenance assistant with
computationally expensive queries, saturating the network segment
shared with Zone 3 historian and HMI systems. Network latency increases
to the point where SCADA polling is affected, causing alarm delays
during a simultaneous process upset.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | How it applies in OT |
|---|---|---|---|
| Denial of service protection | SR 7.6 | FR 7 — Resource Availability | LLM components protected against resource exhaustion attacks affecting OT availability |
| Control system backup | SR 7.7 | FR 7 — Resource Availability | LLM resource exhaustion cannot affect backup and recovery of OT control systems |
| Timely response to events | SR 6.6 | FR 6 — TRE | Network monitoring detects and responds to LLM-related resource exhaustion before OT impact |

#### Zone and conduit controls

**Critical design requirement:**
LLM infrastructure must be on a network segment that cannot affect
Zone 3 critical infrastructure availability under load. Specifically:

- LLM compute resources must not be shared with Zone 3 SCADA,
  historian, or HMI systems
- Network bandwidth available to LLM components must be capped —
  LLM traffic cannot consume bandwidth needed by OT polling protocols
- Rate limiting at the conduit — queries from Zone 4/3 boundary
  to LLM limited to prevent saturation of shared network paths
- Circuit breaker at Zone 3 boundary — if LLM response latency
  exceeds threshold, queries are dropped, not queued

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 7.6: Implement rate limiting on all LLM interfaces in
  OT environments — hard caps on queries per time window
  per user and per session
- Network segment isolation — LLM compute on dedicated
  network segment, bandwidth-limited conduit to OT network
- Token limits on all LLM queries in OT context — prevent
  runaway computation from single queries

**Hardening (SL 2–3)**
- SR 6.6: Integrate LLM resource monitoring with OT network
  monitoring — alert when LLM-related traffic approaches
  thresholds that could affect OT communications
- Implement circuit breakers — LLM service degradation
  does not cascade to OT system availability
- SR 7.7: Verify that LLM compute resource exhaustion
  cannot affect historian, HMI, or SCADA backup systems

**Advanced (SL 3–4)**
- Conduct OT-specific load testing — simulate LLM resource
  exhaustion attacks and verify zero impact on Zone 3
  system availability and response times
- SR 7.6: Implement sponge example detection in OT LLM
  context — identify inputs designed to maximise computation
  and reject before they reach inference
- Include LLM denial-of-service scenarios in OT incident
  response and business continuity planning — defined
  procedures for LLM service degradation during process
  operations

#### Tools

| Tool | Type | Link |
|---|---|---|
| Claroty | Commercial | https://claroty.com |
| Nozomi Networks | Commercial | https://www.nozominetworks.com |
| LiteLLM (rate limiting) | Open-source | https://github.com/BerriAI/litellm |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: NIST SP 800-82 Rev 3 · NERC CIP-007 · IEC 62351

---

## OT deployment checklist for LLM integrations

Use this checklist before deploying any LLM system in or adjacent
to an OT environment:

### Architecture

- [ ] LLM identified in zone model — zone assignment documented
- [ ] Conduit requirements defined between LLM zone and OT zones
- [ ] LLM has no direct write access to Zone 2 or below
- [ ] Network segmentation verified — LLM traffic cannot affect OT availability
- [ ] Human-in-the-loop confirmation gate implemented for all control recommendations

### Security level

- [ ] Target SL defined for LLM integration based on zone security level
- [ ] Security requirements (SRs) mapped to target SL for all FRs
- [ ] Security requirements verified through testing before OT deployment

### Access controls

- [ ] LLM access to OT data classified and least-privilege enforced (SR 2.2)
- [ ] LLM identity registered in OT identity management — audit trail enabled
- [ ] Session termination capability implemented (SR 1.9)
- [ ] Use control policies documented and enforced (SR 2.1)

### Supply chain

- [ ] 62443-2-4 supplier security requirements applied to all LLM vendors
- [ ] ML SBOM completed for all LLM components
- [ ] Integrity verification (SR 3.2) implemented for all components
- [ ] OT change management applied to LLM component updates

### Operations

- [ ] LLM output monitoring integrated with OT SIEM (FR 6)
- [ ] Resource consumption limits implemented (FR 7)
- [ ] Incident response procedures defined for LLM-specific scenarios
- [ ] Operator training on LLM limitations and verification requirements completed

---

## Regulatory crosswalk

Organisations operating under these regulations will find this
mapping directly relevant:

| Regulation | Relevance | Key intersection |
|---|---|---|
| NERC CIP (North America electric) | CIP-007 (ports/services), CIP-010 (config), CIP-013 (supply chain) | LLM01, LLM03, LLM04, LLM10 |
| NIS2 Directive (EU) | Essential entities cybersecurity obligations | LLM01, LLM06, LLM10 |
| CFATS (US chemical) | Chemical facility security — Tier 1–4 | LLM01, LLM06, LLM09 |
| IEC 62351 (power systems) | Communication security for power systems | LLM02, LLM07 |
| IEC 61511 (safety systems) | Safety Instrumented Systems — SIL requirements | LLM06, LLM09, LLM10 |
| EU AI Act Annex III | High-risk AI in critical infrastructure | All entries — see LLM_EUAIAct.md |

---

## Implementation priority for OT environments

| Phase | LLM entries | 62443 requirements | Rationale |
|---|---|---|---|
| 1 — Before any OT deployment | LLM06, LLM10 | SR 2.1/2.2, SR 7.6 | Excessive agency and resource exhaustion are the two risks that can cause immediate physical impact |
| 2 — Deployment gates | LLM01, LLM05 | SR 3.3, SR 2.3 | Prompt injection and output handling must be validated before go-live |
| 3 — First 30 days | LLM03, LLM04 | SR 3.2, SR 3.3/3.7 | Supply chain and poisoning require pipeline-level controls before production training |
| 4 — Ongoing | LLM02, LLM07, LLM08, LLM09 | SR 4.1/4.2, SR 3.1/3.7 | Data confidentiality, prompt leakage, vector security, misinformation monitoring |

---

## References

- [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [ISA/IEC 62443-3-3 System Security Requirements](https://www.isa.org/products/isa-iec-62443-3-3-system-security-requirements)
- [NIST SP 800-82 Rev 3 — Guide to OT Security](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [CISA ICS-CERT Advisories](https://www.cisa.gov/ics)
- [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)
- [IEC 62351 — Security for Power Systems Communications](https://www.iec.ch/homepage)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full OT entries with zone model and deployment checklist | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
