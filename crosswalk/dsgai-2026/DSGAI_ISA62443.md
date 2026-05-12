<!--
  GenAI Security Crosswalk
  Source list : OWASP GenAI Data Security Risks and Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : ISA/IEC 62443 — Industrial Automation and Control Systems Security
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × ISA/IEC 62443

Mapping the [OWASP GenAI Data Security Risks and Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) —
the international standard for Industrial Automation and Control
Systems (IACS) security.

---

## Why DSGAI in OT environments

The DSGAI 2026 taxonomy was developed for enterprise GenAI deployments,
but every data security risk it describes has an amplified form in
operational technology environments:

**DSGAI01 Sensitive Data Leakage** in OT means process parameters,
safety system configurations, network topology, and control logic
exposed — the operational intelligence that enables targeted
physical attacks.

**DSGAI04 Data and Model Poisoning** in OT means a poisoned predictive
maintenance model that systematically misses failure precursors, or
a poisoned process optimisation model that recommends setpoints outside
safe operating envelopes — failures baked into the model and invisible
until triggered.

**DSGAI12 Unsafe NL Data Gateways** in OT means a natural language
interface to historian, CMMS, or process control systems that can
be exploited to extract sensitive process data or inject commands
into OT workflows.

**DSGAI17 Data Availability and Resilience Failures** in OT means
silent RAG degradation causing incorrect process guidance before
detection — a consequence category that does not exist in IT environments.

This file provides OT-specific guidance for all 21 DSGAI entries,
applying ISA/IEC 62443 zone model, Fundamental Requirements (FRs),
and Security Requirements (SRs) to GenAI data security risks in
industrial environments.

Use alongside `LLM_ISA62443.md` and `Agentic_ISA62443.md` for
complete OT coverage of all three OWASP source lists.

---

## OT architecture context for GenAI data security

GenAI systems handling OT data must be placed within the ISA/IEC
62443 zone and conduit model:
```
Enterprise Zone (Level 4–5)
    ? [Firewall + proxy — no direct OT protocol access]
DMZ / Demilitarized Zone (Level 3.5)
    ? GenAI systems should be deployed HERE when they need OT data
    ? [Data diode or unidirectional gateway where feasible]
    ? [Firewall — OT protocol aware, allowlisted flows only]
Control Zone (Level 3) — SCADA, historian, HMI, DCS
    ? [Firewall — minimal, monitored]
Field Zone (Level 0–2) — PLCs, RTUs, field devices, safety systems
```

**Hard rules for GenAI data in OT:**

1. No GenAI system may be placed in Zone 2 or below
2. Historian data flows to GenAI must be read-only and logged
3. GenAI outputs destined for operator display must pass through
   DMZ validation before reaching control zone interfaces
4. No direct GenAI connection to OT field protocols (Modbus, DNP3,
   OPC-UA) without a validated, allowlisted protocol gateway
5. Training data derived from OT historian requires same
   classification as live OT data — not treated as archive data
6. RAG corpora containing OT procedures, P&IDs, or equipment
   specifications are sensitive — RBAC required, encryption mandatory

---

## Security level guidance for DSGAI in OT

| DSGAI data risk factor | SL adjustment | Rationale |
|---|---|---|
| GenAI trained on OT process data | +1 SL | Training data contains operational intelligence |
| RAG corpus includes P&IDs or safety procedures | +1 SL | Sensitive OT documentation in retrieval scope |
| GenAI outputs influence process decisions | +1 SL | Misinformation has direct process consequence |
| GenAI connected to historian with write access | +2 SL | Data integrity risk extends to process control |
| GenAI in active fraud detection or anomaly pipeline | +1 SL | Poisoning affects safety-relevant decisions |
| NL gateway to CMMS or work order system | +1 SL | Data gateway commands affect physical maintenance |

---

## Quick-reference summary

| ID | Name | OT Severity | Primary 62443 FRs / SRs | Minimum SL |
|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | **Critical** | FR 4 DC-1/DC-4, FR 1 IAC-2, FR 6 TRE-1 | SL 2 |
| DSGAI02 | Agent Identity & Credential Exposure | **Critical** | FR 1 IAC-2/IAC-6, FR 4 DC-4, FR 6 TRE-1 | SL 2–3 |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | FR 5 RDF-1, FR 1 IAC-2, FR 6 TRE-6 | SL 2 |
| DSGAI04 | Data, Model & Artifact Poisoning | **Critical** | FR 3 SI-3/SI-7, FR 6 TRE-1, FR 7 RA-6 | SL 2–3 |
| DSGAI05 | Data Integrity & Validation Failures | High | FR 3 SI-3/SI-7, FR 2 UC-6, FR 6 TRE-6 | SL 2 |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | FR 3 SI-2, FR 5 RDF-3, FR 6 TRE-6 | SL 2 |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | FR 4 DC-1, FR 1 IAC-2, 62443-2-4 | SL 2 |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | 62443-2-1, 62443-2-4, FR 6 TRE-6 | SL 2 |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | FR 4 DC-1/DC-4, FR 3 SI-3, FR 6 TRE-6 | SL 2 |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | FR 4 DC-1, FR 3 SI-3, 62443-2-1 | SL 1–2 |
| DSGAI11 | Cross-Context Conversation Bleed | High | FR 1 IAC-2, FR 4 DC-4, FR 5 RDF-1 | SL 2 |
| DSGAI12 | Unsafe NL Data Gateways | **Critical** | FR 2 UC-2/UC-6, FR 3 SI-3, FR 6 TRE-1 | SL 2–3 |
| DSGAI13 | Vector Store Platform Security | High | FR 1 IAC-2, FR 4 DC-1, FR 3 SI-7 | SL 2 |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | FR 4 DC-1/DC-4, FR 1 IAC-2, FR 6 TRE-6 | SL 2 |
| DSGAI15 | Over-Broad Context Windows | High | FR 1 IAC-2, FR 4 DC-4, FR 5 RDF-1 | SL 2 |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | FR 3 SI-2, FR 1 IAC-2, FR 6 TRE-6 | SL 2 |
| DSGAI17 | Data Availability & Resilience Failures | **Critical** | FR 7 RA-6/RA-7, FR 6 TRE-6, FR 5 RDF-1 | SL 2–3 |
| DSGAI18 | Inference & Data Reconstruction | High | FR 4 DC-4, FR 3 SI-3, FR 6 TRE-6 | SL 2–3 |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | FR 3 SI-2, FR 4 DC-1, 62443-2-4 | SL 2 |
| DSGAI20 | Model Exfiltration & IP Replication | High | FR 4 DC-4, FR 1 IAC-2, FR 6 TRE-6 | SL 2 |
| DSGAI21 | Disinformation via Data Poisoning | **Critical** | FR 3 SI-3/SI-7, FR 6 TRE-1, FR 7 RA-6 | SL 2–3 |

---

## Audience tags

- **OT security engineer** — full file, primary reference for GenAI data security in OT
- **ICS security architect** — zone model, data flow controls, SL ratings
- **Control system engineer** — DSGAI04, DSGAI12, DSGAI17, DSGAI21 entries
- **Safety engineer** — DSGAI04, DSGAI17, DSGAI21 entries — SIS intersection
- **CISO (critical infrastructure)** — SL mapping and governance entries
- **OT procurement** — 62443-2-4 supplier requirements for GenAI vendors

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**OT Severity:** Critical

Sensitive OT data — process parameters, historian tag names, equipment
specifications, safety system configurations, network topology —
leaks through GenAI outputs, RAG retrieval, or observability pipelines.
In OT environments this is operational intelligence that enables
targeted physical attacks.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | All OT data flowing through GenAI systems encrypted — historian exports, embedding stores, prompt caches |
| Use of physical diagnostic and test interfaces | SR 4.4 | FR 4 — DC | GenAI outputs containing sensitive OT identifiers (tag names, IPs, device types) masked before leaving DMZ |
| Human user authentication | SR 1.2 | FR 1 — IAC | Access to GenAI systems in OT scope authenticated — each user with unique, traceable identity |
| Timely response to events | SR 6.1 | FR 6 — TRE | Sensitive OT data disclosure treated as security event — agent suspended, disclosure scope assessed |

#### Zone and conduit controls

- GenAI systems placed in DMZ (Level 3.5) — never in
  control zone — data flows from historian to GenAI
  read-only through logged conduit
- OT-specific output masking: tag IDs, device names,
  IP addresses, safety system identifiers masked before
  GenAI outputs cross the DMZ boundary into any
  less-trusted zone or external interface
- All historian queries logged with user identity —
  sensitive OT data access auditable at conduit

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 4.1: Encrypt all OT data in GenAI scope —
  historian exports, embedding stores, RAG corpora
  containing equipment documentation, prompt caches
- SR 1.2: Authenticate all access to GenAI systems
  handling OT data — unique identities, traceable
  access for compliance and forensics
- Apply OT-specific output masking — tag IDs,
  device names, network addresses masked by default

**Hardening (SL 2–3)**
- SR 4.4: Implement OT-specific data masking at
  DMZ boundary — no cleartext OT topology or
  equipment configuration data in GenAI outputs
- SR 6.1: Include OT data leakage in incident
  response — disclosure scope assessment covering
  what operational intelligence was exposed

**Advanced (SL 3–4)**
- Conduct OT data disclosure red team — attempt
  to extract operational intelligence enabling
  targeted attack through GenAI inference queries
  against your specific historian and SCADA topology

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.4 · ISO 27001 A.8.11 · NIST CSF 2.0 PR.DS-01

---

### DSGAI02 — Agent Identity & Credential Exposure

**OT Severity:** Critical

AI agent credentials providing access to historian, CMMS, or
process control interfaces are exposed through memory stores, logs,
or tool payloads — enabling lateral movement into OT systems.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Human user authentication | SR 1.2 | FR 1 — IAC | All agent credentials unique and traceable — no shared service accounts for OT-accessing agents |
| Authenticator management | SR 1.6 | FR 1 — IAC | Agent credential lifecycle managed — issuance, rotation, revocation documented per agent |
| Data confidentiality | SR 4.1 | FR 4 — DC | Agent credentials never transmitted or stored in cleartext within OT network |
| Timely response to events | SR 6.1 | FR 6 — TRE | Agent credential exposure treated as security event — immediate rotation, lateral movement assessment |

#### Zone and conduit controls

- Agent credentials scoped to minimum OT data access —
  historian read limited to specific tag groups required
  for the agent's defined function
- Credentials issued at session start, revoked at
  session end — no persistent standing credentials
  in OT-adjacent agent memory
- Zone 2 access prohibition — no agent credential
  may grant access to Zone 2 device interfaces,
  PLC programming ports, or safety system configuration

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 1.2: Unique service identity per OT-accessing
  agent — all agent actions in OT traceable to
  specific agent identity in audit log
- SR 4.1: All agent credentials encrypted in OT
  environment — no cleartext tokens in agent memory,
  configuration, or observability logs
- Short-lived JIT credentials — expire at session end

**Hardening (SL 2–3)**
- SR 1.6: Agent credential lifecycle documented —
  issuance, rotation, revocation all logged in OT
  identity management system
- Credential anomaly detection — agent credential
  use outside expected OT system scope triggers
  immediate alert

**Advanced (SL 3–4)**
- PKI-backed agent identities for Zone 3 access —
  signed requests, certificate-bound credentials,
  revocation infrastructure
- OT-specific lateral movement red team — attempt
  to move from compromised agent credential to
  other OT systems, document access scope achievable

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: OWASP NHI Top 10 · NIST SP 800-82 Rev 3 Section 6 · NIST CSF 2.0 PR.AA-01

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**OT Severity:** High

OT staff use unapproved GenAI tools and paste process data, historian
exports, or equipment documentation into external AI services —
creating ungoverned flows of sensitive OT operational intelligence
to external services.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Information flow restriction | SR 5.1 | FR 5 — RDF | Network controls block OT data flows to unapproved AI endpoints — DLP at OT DMZ boundary |
| Use control | SR 1.2 | FR 1 — IAC | Approved AI tools only on OT workstations — unapproved services blocked at network layer |
| Timely response to events | SR 6.6 | FR 6 — TRE | Shadow AI discovery triggers incident response — data impact assessment, vendor notification |

#### Zone and conduit controls

- Block unapproved AI service endpoints at Zone 3/4
  boundary — no OT data reaches external AI services
  outside approved conduit
- DLP on OT workstation egress — historian exports,
  P&ID files, equipment documentation detected before
  reaching external AI services
- OT acceptable use policy: no sensitive OT data in
  unapproved AI tools — enforced at network layer,
  not only policy

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 5.1: Network controls blocking OT data flows to
  unapproved AI endpoints — enforced at DMZ conduit
- OT-specific acceptable use policy — explicitly covers
  what OT data must not be used with external AI tools

**Hardening (SL 2–3)**
- SR 6.6: Shadow AI discovery in OT — automated
  detection of OT data flows to unapproved AI services
  triggers incident response

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: NIST SP 800-82 Rev 3 Section 8 · ISO 27001 A.5.10 · NIST CSF 2.0 GV.OC-01

---

### DSGAI04 — Data, Model & Artifact Poisoning

**OT Severity:** Critical

Training data or model weights corrupted with backdoors — in OT,
a poisoned GenAI model providing process recommendations or anomaly
detection can systematically miss failure precursors, misclassify
safety-relevant conditions, or recommend setpoints outside safe
operating envelopes. The effect is baked into the model and may
not manifest until triggered by a specific process condition.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — SI | Training data integrity controls — source allowlisting, anomaly detection, provenance tracking |
| Software and information integrity monitoring | SR 3.7 | FR 3 — SI | Continuous monitoring of OT GenAI model outputs — systematic anomalies indicating poisoning detected |
| Timely response to events | SR 6.1 | FR 6 — TRE | Poisoning events treated as Critical security incidents — model suspended, process control fallback activated |
| Denial of service protection | SR 7.6 | FR 7 — RA | Poisoned model availability impact contained — fallback procedure prevents physical process disruption |

#### Zone and conduit controls

- OT historian data used for training treated as
  Zone 3 operational data — same classification and
  access controls as live process data
- Model integrity verification before any OT advisory
  system promotion — hash-based check against approved
  baseline mandatory deployment gate
- Process control fallback documented — if GenAI
  advisory system is suspended due to poisoning
  detection, operator control mode defined and tested

#### OT-specific threat scenario

A poisoned anomaly detection model deployed in a Zone 3 predictive
maintenance pipeline systematically classifies a specific vibration
signature as normal when it actually indicates bearing failure. The
backdoor is triggered by normal process conditions and invisible to
output distribution analysis on the training range. The model
continues to generate plausible-looking normal health scores while
the failure progresses. This is qualitatively different from IT
poisoning because the physical consequence — equipment failure,
unplanned shutdown, or safety event — accumulates over weeks before
detection.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.3: Training data integrity controls for all
  OT GenAI — historian data source allowlisting,
  anomaly detection on data distributions, provenance
  tracking from historian to training dataset
- Model rollback capability — approved clean version
  always available, rollback procedure tested as
  part of OT incident response exercise

**Hardening (SL 2–3)**
- SR 3.7: Production monitoring of OT GenAI model
  outputs — systematic anomalies in recommendations
  or health scores detected as poisoning indicators
- SR 6.1: OT poisoning incident response — model
  suspension, process control fallback, engineering
  review of all affected recommendations

**Advanced (SL 3–4)**
- Post-training backdoor detection as mandatory
  OT deployment gate — test with OT-specific trigger
  conditions before any Zone 3 advisory system deployment
- Include poisoning scenarios in Process Hazard
  Analysis — assess physical consequences of each
  possible poisoned recommendation for each process area

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.3 · ISO 27001 A.8.27 · MITRE ATLAS AML.T0020

---

### DSGAI05 — Data Integrity & Validation Failures

**OT Severity:** High

Adversarially crafted payloads corrupt GenAI data pipelines or exploit
ingestion vulnerabilities. In OT, CVE-2024-3584 class path traversal
in vector database snapshot imports achieves arbitrary file write on
hosts within Zone 3 — a direct path to Zone 3 host compromise.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — SI | Multi-stage validation at all GenAI ingestion boundaries — path traversal prevention mandatory in Zone 3 |
| Software and information integrity monitoring | SR 3.7 | FR 3 — SI | Runtime monitoring of ingestion pipelines — anomalous payloads detected and rejected |
| Use control | SR 2.6 | FR 2 — UC | Only approved, validated data sources permitted in Zone 3 GenAI ingestion — unapproved sources blocked |
| Timely response to events | SR 6.6 | FR 6 — TRE | Ingestion integrity failure treated as security event — pipeline suspended, forensic capture |

#### Zone and conduit controls

- Sandbox all snapshot import operations — no direct
  write to Zone 3 filesystem paths, isolated execution
  environment for all archive import operations
- Patch CVE-2024-3584 and equivalents immediately —
  arbitrary file write on Zone 3 host is Critical
  in any OT environment

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.3: Multi-stage validation at all OT GenAI
  ingestion boundaries — schema, semantic, path
  traversal prevention before any data enters pipeline
- Patch CVE-2024-3584 class — urgent priority in
  all Zone 3 environments

**Hardening (SL 2–3)**
- SR 3.7: Monitor OT ingestion pipelines for anomalous
  payloads — unusual encoding, schema violations alerted
  as potential integrity attack

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: NIST SP 800-82 Rev 3 Section 7.2 · CWE-20 · ISO 27001 A.8.26/A.8.28

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**OT Severity:** High

AI tools and MCP servers receive context payloads containing OT data
with no minimisation. In OT environments, tools receiving context
may include historian query results, equipment health data, alarm
records, and process parameters — all sensitive operational intelligence.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.2 | FR 3 — SI | All OT tool integrations assessed — security requirements in vendor contracts per 62443-2-4 |
| Information flow restriction | SR 5.3 | FR 5 — RDF | OT-sensitive context minimised before tool API calls — tools receive minimum required, not full OT context |
| Timely response to events | SR 6.6 | FR 6 — TRE | Tool data exchange anomalies detected — unusual data volumes in tool calls alerted |

#### Zone and conduit controls

- Apply 62443-2-4 supplier requirements to all tool
  and MCP providers that may receive OT data —
  same requirements as OT software vendors
- DLP on tool API calls from Zone 3 context —
  OT-sensitive identifiers detected before leaving
  the controlled environment

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.2: Apply 62443-2-4 to all OT tool vendors —
  provenance, integrity, incident notification
- SR 5.3: OT context minimisation — tools receive
  only minimum data required, not full process context

**Hardening (SL 2–3)**
- DLP on tool payloads from OT context — sensitive
  OT data patterns detected before leaving Zone 3
  boundary through tool integration channels

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: NIST SP 800-82 Rev 3 Section 8.4 · ISO 27001 A.5.19/A.5.20

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**OT Severity:** High

GenAI creates ungoverned derived data assets — in OT, embeddings
and caches derived from historian data, P&IDs, and equipment
specifications are sensitive operational intelligence that must be
governed with the same rigour as source documents.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | OT-derived GenAI assets (embeddings, caches) classified and protected — not treated as general IT data |
| Human user authentication | SR 1.2 | FR 1 — IAC | Access controls on all GenAI-derived OT data assets — same authentication requirements as source data |
| 62443-2-4 | Supplier security requirements | — | GenAI vendors handling OT-derived assets subject to 62443-2-4 programme |

#### Zone and conduit controls

- OT data classification propagates to all derived
  assets — embedding of historian data classified
  at same level as live historian access
- Secure disposal of derived OT assets — deletion
  of source triggers deletion of all embeddings,
  caches, and summaries derived from it

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 4.1: All OT-derived GenAI assets classified
  and protected — embeddings, summaries, caches
  from OT data inherit source classification
- Extend OT asset inventory to GenAI-derived assets —
  ungoverned stores represent untracked attack surface

**Hardening (SL 2–3)**
- 62443-2-4: Apply supplier requirements to all
  GenAI vendors handling OT-derived assets

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: NIST SP 800-82 Rev 3 Section 6 · ISO 27001 A.5.9/A.8.10

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**OT Severity:** High

GenAI systems trigger regulatory obligations in OT environments —
NERC CIP, NIS2, CFATS, and sector-specific requirements apply to
GenAI systems handling OT data. Non-compliance creates additional
legal exposure beyond the security risk.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| 62443-2-1 | Security management system | — | OT security management system updated to cover GenAI deployments — policy, roles, assessment |
| 62443-2-4 | Supplier security requirements | — | GenAI vendors assessed under OT supplier security programme — same requirements as OT software vendors |
| Timely response to events | SR 6.6 | FR 6 — TRE | Non-compliance incidents trigger defined response — regulatory notification procedures documented |

#### OT regulatory crosswalk for GenAI

| Regulation | GenAI data security intersection | Primary DSGAI entries |
|---|---|---|
| NERC CIP (electric) | CIP-007/010/011 — GenAI systems handling BES Cyber System data | DSGAI01, DSGAI04, DSGAI07 |
| NIS2 (EU) | Essential entity AI security obligations | DSGAI01, DSGAI04, DSGAI17 |
| IEC 61511 (functional safety) | GenAI in safety instrumented system advisory capacity | DSGAI04, DSGAI17, DSGAI21 |
| CFATS (US chemical) | Chemical facility security tier intersection | DSGAI01, DSGAI12 |
| AWIA 2018 (water) | Water system cybersecurity risk assessment | DSGAI04, DSGAI17 |

#### Mitigations by tier

**Foundational (SL 1–2)**
- 62443-2-1: Update OT security management system to
  cover GenAI — scope definition, policy, roles,
  risk assessment for each GenAI deployment in OT scope
- Conduct regulatory scoping for all OT GenAI —
  which sector regulations apply, what obligations
  are triggered, who is accountable

**Hardening (SL 2–3)**
- 62443-2-4: Apply supplier requirements to all GenAI
  vendors with OT data access — same programme as
  OT software vendors
- SR 6.6: Regulatory incident response procedures —
  breach notification timelines, regulatory contacts,
  reporting obligations documented and tested

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: NERC CIP series · EU AI Act Art. 10/17 · NIST SP 800-82 Rev 3 Section 8

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**OT Severity:** High

Multimodal GenAI in OT processes images of P&IDs, equipment nameplates,
control room displays, and inspection photographs — OCR extraction
of this content creates sensitive OT data that may not be treated
with appropriate controls.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | Extracted OT content from multimodal inputs classified and protected — OCR output of P&ID is as sensitive as the P&ID |
| Software and information integrity | SR 3.3 | FR 3 — SI | Multimodal extraction pipelines validated — no uncontrolled OT data entering unclassified processing |
| Timely response to events | SR 6.6 | FR 6 — TRE | Multimodal OT data leakage treated as security event |

#### Zone and conduit controls

- OT-specific multimodal input classification:
  P&ID images, equipment photographs, control room
  displays all classified at Zone 3 data level
- Short retention for multimodal OT uploads —
  automated deletion after processing purpose complete

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 4.1: OT-specific content classification for
  multimodal extraction — OCR of P&ID image requires
  same controls as the original P&ID document
- Apply same data masking to extracted OT identifiers
  in multimodal outputs as to direct historian queries

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.4 · ISO 27001 A.8.11

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**OT Severity:** Medium

Synthetic OT data — process simulations, synthetic historian data —
may retain re-identification risk that exposes real process parameters
or equipment characteristics through statistical inference.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | Synthetic OT datasets not automatically excluded from protection — assessed before classification change |
| Software and information integrity | SR 3.3 | FR 3 — SI | Synthetic data generation pipeline validated — source OT data integrity maintained |
| 62443-2-1 | Security management | — | OT synthetic data governance policy — when synthetic data removes OT classification obligation |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 4.1: Treat synthetic OT data as sensitive until
  formal re-identification risk assessment — process
  simulation data may reveal real equipment characteristics
- Document acceptable anonymisation standards for
  OT data in 62443-2-1 security management programme

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.5.34 · NIST SP 800-82 Rev 3 Section 6

---

### DSGAI11 — Cross-Context Conversation Bleed

**OT Severity:** High

Multi-user GenAI deployments in OT environments leak one operator's
process context into another operator's session — exposing operational
decisions, alarm interpretations, or equipment configurations across
shifts or roles.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Human user authentication | SR 1.2 | FR 1 — IAC | Per-operator session isolation — each operator's context inaccessible to all other sessions |
| Data confidentiality | SR 4.1 | FR 4 — DC | Per-operator session data encrypted — KV cache isolation prevents cross-session OT data exposure |
| Information flow restriction | SR 5.1 | FR 5 — RDF | Cross-session data flows restricted — Zone 3 GenAI enforces strict operator session boundaries |

#### Zone and conduit controls

- Per-operator RAG namespaces in Zone 3 GenAI —
  no shared context between operators regardless of
  shared physical infrastructure
- Multi-tenant isolation testing before each
  Zone 3 deployment — cross-session OT data access
  specifically tested

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 1.2: Per-operator session isolation — each
  operator's OT context, retrieved procedures, and
  process history inaccessible to all other sessions
- SR 4.1: Encrypt per-operator session data —
  session isolation technical control documented

**Hardening (SL 2–3)**
- Multi-tenant isolation testing before Zone 3
  deployment — verify operator A cannot retrieve
  operator B's process context through any query

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: NIST SP 800-82 Rev 3 · ISO 27001 A.8.3

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**OT Severity:** Critical

LLM-to-database interfaces in OT environments — NL to historian,
NL to CMMS, NL to alarm management — create direct paths from
natural language to process data and potentially to work order
systems. This is one of the highest-risk DSGAI entries in OT contexts
because the blast radius extends from data exposure to physical
work scheduling.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Least privilege | SR 2.2 | FR 2 — UC | NL gateway executes under requesting operator's permissions — never shared high-privilege OT service account |
| Use control enforcement | SR 2.1 | FR 2 — UC | NL gateway query allowlisting — only pre-approved query patterns permitted to OT data systems |
| Software and information integrity | SR 3.3 | FR 3 — SI | NL gateway input validation — injection addressed as a known vulnerability class in Zone 3 |
| Timely response to events | SR 6.1 | FR 6 — TRE | NL gateway misuse treated as Critical security event — query log forensics, data exposure scope |

#### Zone and conduit controls

- Read-only by default for all OT NL gateways —
  no write, delete, or command operations through
  LLM-generated queries without formal approval
- Query allowlisting enforced at Zone 3 conduit —
  only pre-approved patterns reach historian or CMMS,
  destructive queries blocked before execution
- CMMS write access through NL gateway requires
  human confirmation — separate approval outside
  the NL interface

#### OT-specific threat scenario

An LLM-to-historian interface deployed in Zone 3 for maintenance
analysis is exploited through a crafted natural language query that
generates SQL selecting all process parameters, setpoint histories,
and safety function activation records — operational intelligence
enabling a targeted physical attack. The query executes under a
shared high-privilege historian service account that the LLM gateway
was granted. This is DSGAI12 + AML.T0057 (Data from Information
Repositories) realised in Zone 3.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 2.2: Per-operator execution — NL gateway queries
  execute under requesting operator's historian
  permissions, never shared high-privilege account
- SR 3.3: Query allowlisting and parameterised
  execution as secure development requirements —
  injection addressed before any OT NL gateway deployment
- Read-only default — no write or command access
  through NL gateway without documented justification

**Hardening (SL 2–3)**
- SR 2.1: Allowlist enforced at conduit — bulk
  extraction patterns rejected before reaching historian
- SR 6.1: Log all NL-generated queries with operator
  identity — forensic audit trail for all OT data access
- Include NL gateway injection in OT penetration testing

**Advanced (SL 3–4)**
- Adversarial NL-to-SQL testing against OT historian —
  attempt destructive or bulk extraction queries,
  verify allowlist holds
- Conduct Process Hazard Analysis for NL gateway —
  assess physical consequences if NL gateway enables
  work order creation or setpoint access

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: NIST SP 800-82 Rev 3 Section 7.2 · CWE-89 · MITRE ATLAS AML.T0057

---

### DSGAI13 — Vector Store Platform Security

**OT Severity:** High

Vector databases in Zone 3 storing embeddings of equipment documentation,
maintenance procedures, and process parameters are high-value OT
data repositories with weaker default security posture than traditional
OT data historians.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Human user authentication | SR 1.2 | FR 1 — IAC | RBAC on all Zone 3 vector stores — no unauthenticated access in any OT environment |
| Data confidentiality | SR 4.1 | FR 4 — DC | Zone 3 vector store content encrypted — equipment documentation and procedure embeddings as sensitive OT data |
| Software and information integrity monitoring | SR 3.7 | FR 3 — SI | Vector store integrity monitoring — anomalous access patterns indicating bulk extraction detected |

#### Zone and conduit controls

- Vector stores in Zone 3 accessible only from
  authorised Zone 3 services — network isolation
  at conduit level
- Patch all vector database CVEs immediately in
  Zone 3 — CVE-2024-3584 class is Critical in OT

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 1.2: RBAC on all Zone 3 vector stores —
  no unauthenticated access in any OT environment
- SR 4.1: Encrypt Zone 3 vector store content —
  same protection as source OT documentation
- Patch CVE-2024-3584 — urgent in Zone 3

**Hardening (SL 2–3)**
- SR 3.7: Monitor Zone 3 vector store access —
  bulk extraction and unusual query patterns alerted
  through OT SIEM integration

#### Cross-references
- LLM Top 10: LLM08 Vector & Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 · ISO 27001 A.8.3/A.8.24

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**OT Severity:** High

Observability pipelines capturing Zone 3 GenAI interactions contain
sensitive OT data — historian queries, process parameters, alarm
interpretations — at scale, with often weaker access controls than
the production systems they observe.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | OT GenAI telemetry stores classified and protected — process data in logs requires same protection as live data |
| Use of physical diagnostic and test interfaces | SR 4.4 | FR 4 — DC | OT-specific data masking before telemetry capture — tag IDs, equipment identifiers masked before logging |
| Human user authentication | SR 1.2 | FR 1 — IAC | Access controls on OT GenAI telemetry stores — need-to-know enforced |

#### Zone and conduit controls

- Apply OT data masking before telemetry capture —
  tag IDs, device names, alarm details masked before
  entering observability pipeline
- Short TTL for Zone 3 GenAI debug traces — sensitive
  OT interaction data retained only for required window

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 4.4: OT-specific masking before telemetry —
  process data identifiers masked before logging
- SR 4.1: Protect OT GenAI telemetry stores —
  same access controls as production OT data

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.4 · ISO 27001 A.8.15

---

### DSGAI15 — Over-Broad Context Windows

**OT Severity:** High

Excessive context injection aggregates OT data from multiple trust
domains — historian records, maintenance procedures, alarm histories,
P&ID details — into a single LLM context window, amplifying the impact
of any injection that reaches this context in Zone 3.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Least privilege | SR 2.2 | FR 2 — UC | OT context assembly restricted to minimum data required for the specific query — not broad process datasets |
| Data confidentiality | SR 4.1 | FR 4 — DC | OT context window classification tracking — highest classification drives response handling |
| Information flow restriction | SR 5.1 | FR 5 — RDF | Context assembly limits in Zone 3 — cross-trust-domain aggregation restricted |

#### Zone and conduit controls

- Minimum-necessary OT context injection —
  only historian tags directly relevant to the
  query included, not broad process datasets
- Classification ceiling enforcement — if context
  window includes Zone 3 operational data at any
  classification, response handling reflects that level

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 2.2: Minimum-necessary OT context injection —
  relevant tags only, not broad Zone 3 datasets
- SR 4.1: Classification ceiling tracking in context —
  highest classification of any injected content
  drives response handling requirements

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: NIST SP 800-82 Rev 3 · ISO 27001 A.8.3

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**OT Severity:** High

Browser AI assistants on Zone 3 engineering workstations or historian
client machines access sensitive OT data across open applications —
P&ID viewers, SCADA HMI sessions, historian client interfaces,
CMMS browser tabs.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.2 | FR 3 — SI | Browser AI extensions assessed as third-party software — 62443-2-4 requirements before Zone 3 deployment |
| Human user authentication | SR 1.2 | FR 1 — IAC | Approved extensions only on Zone 3 workstations — unapproved AI extensions blocked at device management |
| Timely response to events | SR 6.6 | FR 6 — TRE | Browser AI anomalies on Zone 3 workstations treated as security events |

#### Zone and conduit controls

- No unapproved AI extensions on Zone 3 workstations —
  device management enforcement, not just policy
- Approved browser AI extensions assessed under
  62443-2-4 supplier programme before Zone 3 deployment

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.2: Apply 62443-2-4 to all browser AI extension
  providers before Zone 3 deployment
- SR 1.2: Block unapproved AI extensions on Zone 3
  workstations — device management enforcement

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: NIST SP 800-82 Rev 3 Section 8 · ISO 27001 A.8.1/A.8.7

---

### DSGAI17 — Data Availability & Resilience Failures

**OT Severity:** Critical

Silent GenAI pipeline failures in OT advisory systems — predictive
maintenance, anomaly detection, process optimisation — produce incorrect
guidance indistinguishable from correct output. In OT environments
this can propagate from the AI advisory layer into physical process
control before human detection. This is the unique OT amplifier of
DSGAI17 — in IT environments silent failures cause incorrect information;
in OT environments they cause incorrect physical actions.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Denial of service protection | SR 7.6 | FR 7 — RA | Circuit breakers preventing OT GenAI service degradation from affecting process control |
| Control system backup | SR 7.7 | FR 7 — RA | OT GenAI failures cannot affect backup and recovery of process control — independence verified |
| Timely response to events | SR 6.6 | FR 6 — TRE | OT GenAI pipeline failures treated as security events — process control fallback activated |
| Information flow restriction | SR 5.1 | FR 5 — RDF | OT GenAI availability events do not propagate to process control — architectural separation |

#### Zone and conduit controls

- OT GenAI advisory system and process control
  systems architecturally separated — GenAI failure
  cannot affect Zone 2 or below
- Explicit unavailability notification — when OT
  GenAI advisory is degraded, operators receive clear
  notification; stale data is never presented as current
- Process control fallback tested — operator manual
  mode procedure works without GenAI advisory, tested
  in periodic drills

#### OT-specific threat scenario

A RAG-powered anomaly detection pipeline in Zone 3 experiences
silent vector store staleness — the index has not been refreshed
for 72 hours due to a failed refresh job. The system continues
returning responses derived from stale embeddings, classifying a
new failure mode as normal because similar patterns were normal 72
hours ago. The anomaly progresses to equipment failure before the
stale index is detected. This is qualitatively different from IT
availability failures because the consequence is physical.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 7.6: Circuit breakers at OT GenAI service
  boundary — graceful degradation to manual mode
  rather than silent misinformation
- Freshness monitoring — alert when index age exceeds
  defined threshold before stale data reaches operators
- Process control fallback tested — manual mode
  operates correctly when GenAI advisory is unavailable

**Hardening (SL 2–3)**
- SR 6.6: OT GenAI pipeline health in OT SIEM —
  freshness, availability metrics reviewed as security
  monitoring, not just operational monitoring
- SR 7.7: Verify OT GenAI failures cannot affect
  backup process control — architectural independence
  confirmed through testing

**Advanced (SL 3–4)**
- Adversarial availability testing — attempt to
  saturate OT GenAI endpoints, verify circuit breakers
  and process control fallback hold under load
- Include OT GenAI availability scenarios in Process
  Hazard Analysis — what physical consequences are
  possible if advisory system provides incorrect data

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.6 · IEC 61511 (functional safety) · AIUC-1 D

---

### DSGAI18 — Inference & Data Reconstruction

**OT Severity:** High

Membership inference and model inversion attacks against OT GenAI
systems reconstruct sensitive process parameters, equipment characteristics,
or safety system configurations embedded in training data.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | Inference attack resistance as OT data protection measure — differential privacy for OT training data |
| Timely response to events | SR 6.6 | FR 6 — TRE | Inference attack campaigns detected — systematic query patterns indicative of AML.T0024.000 alerted |
| Software and information integrity | SR 3.3 | FR 3 — SI | Confidence score suppression as OT integrity control — limits information available for model inversion |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 4.1: Apply differential privacy in OT GenAI
  training — limits reconstruction of sensitive process
  parameters from model outputs
- Confidence score suppression — reduces information
  enabling inference attacks against OT-trained models

**Hardening (SL 2–3)**
- SR 6.6: Monitor for inference attack patterns —
  systematic output space probing against OT GenAI
  models detected and rate-limited

**Advanced (SL 3–4)**
- Membership inference red team against OT-trained
  models before deployment — verify process parameters
  and equipment characteristics cannot be reconstructed

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.4 · MITRE ATLAS AML.T0024.000

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**OT Severity:** Medium

Human annotators accessing OT data for labelling — equipment health
labelling, alarm classification, maintenance record annotation —
are a supply chain access path to sensitive operational data.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.2 | FR 3 — SI | Labelling vendors with OT data access assessed under 62443-2-4 — same requirements as OT software vendors |
| Data confidentiality | SR 4.1 | FR 4 — DC | OT data minimisation in labelling tasks — annotators see minimum content needed, not full process records |
| 62443-2-4 | Supplier security requirements | — | All labelling vendors with OT data access assessed before engagement |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.2: Apply 62443-2-4 to labelling vendors with
  OT data access — same programme as OT software vendors
- SR 4.1: OT data minimisation in labelling — annotators
  see anonymised or minimised data rather than full
  process records

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: NIST SP 800-82 Rev 3 Section 8.4 · ISO 27001 A.5.34

---

### DSGAI20 — Model Exfiltration & IP Replication

**OT Severity:** High

OT GenAI models trained on proprietary process data — equipment
failure signatures, process optimisation parameters, safety threshold
models — represent both IP and operational intelligence. Model
replication enables adversaries to probe the model for process
insights without direct OT system access.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Data confidentiality | SR 4.1 | FR 4 — DC | OT GenAI model APIs rate-limited — systematic extraction requires high query volumes, rate limiting raises cost |
| Human user authentication | SR 1.2 | FR 1 — IAC | Authentication on all OT GenAI model inference APIs — unauthenticated systematic querying blocked |
| Timely response to events | SR 6.6 | FR 6 — TRE | Model extraction patterns detected — unusual query diversity alerted as potential AML.T0016 |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 1.2: Authentication on all OT GenAI model APIs —
  no unauthenticated systematic querying possible
- SR 4.1: Rate limiting as OT data protection control —
  systematic model extraction requires high query
  volumes, rate limiting raises cost significantly

**Hardening (SL 2–3)**
- SR 6.6: Monitor for extraction patterns —
  unusual query diversity and volume alerted
  as potential AML.T0016 in OT SIEM

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST SP 800-82 Rev 3 · MITRE ATLAS AML.T0016 · ISO 27001 A.5.12

---

### DSGAI21 — Disinformation via Data Poisoning

**OT Severity:** Critical

False content injected into RAG corpora causes OT GenAI advisory
systems to surface incorrect process guidance, safety procedures, or
maintenance recommendations. In OT environments, a poisoned RAG
corpus in a Zone 3 advisory system can propagate incorrect guidance
to operators making safety-critical decisions — the physical consequence
of acting on RAG-sourced misinformation is qualitatively different
from IT environments.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — SI | OT RAG corpus integrity controls — source allowlisting, hash verification, ingestion gates |
| Software and information integrity monitoring | SR 3.7 | FR 3 — SI | Continuous OT RAG corpus monitoring — unauthorised modifications detected before reaching operators |
| Timely response to events | SR 6.1 | FR 6 — TRE | OT RAG poisoning treated as Critical security event — source quarantine, index rebuild, process control assessment |
| Denial of service protection | SR 7.6 | FR 7 — RA | Poisoned advisory output blast radius contained — process control fallback if advisory system compromised |

#### Zone and conduit controls

- OT RAG corpus treated as Zone 3 operational data —
  same source trust requirements as live process data
- Engineering-approved sources only — no external
  web content in OT advisory RAG corpus without
  engineering review and approval
- Cryptographic provenance for critical OT documents
  in RAG — P&IDs, safety procedures, equipment
  specifications hash-verified before indexing

#### OT-specific threat scenario

An adversary with access to the documentation management system
used by an OT advisory RAG pipeline injects a modified version of
a maintenance procedure for a safety-critical valve — the modification
changes the recommended test interval from 6 months to 18 months
and omits a critical pre-maintenance isolation step. The modified
document is indexed by the RAG system. Over the following months,
operators following AI-recommended maintenance procedures based on
the poisoned document create conditions for a safety incident.
The poisoning required no access to the OT network — only to the
documentation system that feeds the RAG corpus.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.3: OT RAG corpus integrity controls —
  hash-based verification of all indexed content,
  source allowlisting to engineering-approved sources
- Engineering-approved sources only for OT advisory
  RAG — no unreviewed external content in any corpus
  that influences Zone 3 advisory outputs

**Hardening (SL 2–3)**
- SR 3.7: Continuous OT RAG corpus monitoring —
  integrity hashing on all indexed documents, changes
  trigger immediate alert and engineering review
- SR 6.1: OT RAG poisoning incident response —
  source quarantine, full index rebuild, review of
  all recommendations issued since poison ingestion

**Advanced (SL 3–4)**
- Include RAG poisoning in Process Hazard Analysis —
  assess physical consequences of each possible
  incorrect recommendation per process area
- Adversarial OT RAG integrity testing before each
  deployment — attempt content injection via each
  documentation source, verify detection holds

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 Section 5.3 · IEC 61511 · MITRE ATLAS AML.T0045

---

## OT GenAI data security deployment checklist

### Before any OT GenAI data deployment

- [ ] Zone assignment documented — GenAI system in DMZ or enterprise tier
- [ ] OT data classification applied to all data assets in GenAI scope
- [ ] Data flows from historian to GenAI read-only through logged conduit
- [ ] No direct GenAI connection to OT field protocols without validated gateway
- [ ] 62443-2-4 requirements applied to all GenAI vendors with OT data access
- [ ] Process control fallback defined and tested for each GenAI advisory function

### Data protection

- [ ] All OT data in GenAI scope encrypted at rest (SR 4.1)
- [ ] OT-specific output masking implemented — tag IDs, device names masked (SR 4.4)
- [ ] RAG corpus access-controlled — RBAC required, encryption mandatory
- [ ] Telemetry stores classified at same level as captured OT data (SR 4.1)
- [ ] Derived assets (embeddings, caches) classified as Zone 3 data (SR 4.1)

### Ingestion and supply chain

- [ ] CVE-2024-3584 class patched in all Zone 3 vector databases
- [ ] Multi-stage ingestion validation implemented (SR 3.3)
- [ ] OT RAG corpus limited to engineering-approved sources (SR 3.3)
- [ ] All RAG corpus documents hash-verified before indexing (SR 3.7)
- [ ] 62443-2-4 applied to training data providers and labelling vendors

### Access and identity

- [ ] Per-operator session isolation implemented (SR 1.2)
- [ ] NL gateways execute under operator permissions, not shared account (SR 2.2)
- [ ] RBAC enabled on all Zone 3 vector stores (SR 1.2)
- [ ] Agent credentials scoped to minimum OT data access (SR 1.6)
- [ ] Zone 2 access prohibition verified — no agent or GenAI credential grants Zone 2 access

### Availability and resilience

- [ ] Freshness monitoring on all OT GenAI pipelines (SR 6.6)
- [ ] Circuit breakers implemented at GenAI-process interface (SR 7.6)
- [ ] Explicit unavailability notification to operators on GenAI degradation
- [ ] Process control fallback verified — manual mode operates without GenAI
- [ ] OT GenAI availability in BCP — RTO/RPO defined and tested (SR 7.7)

### Monitoring and response

- [ ] OT GenAI outputs monitored — poisoning and accuracy degradation detected (SR 3.7)
- [ ] NL gateway queries logged with operator identity (SR 6.1)
- [ ] Inference attack patterns monitored — unusual query diversity alerted (SR 6.6)
- [ ] RAG corpus integrity monitoring live — modification alerts in OT SIEM (SR 3.7)
- [ ] OT GenAI incident response procedures defined for each DSGAI entry
- [ ] Poisoning and disinformation scenarios in Process Hazard Analysis

---

## Implementation priority for OT environments

| Phase | DSGAI entries | 62443 requirements | Rationale |
|---|---|---|---|
| 1 — Before deployment | DSGAI01, DSGAI07 | SR 4.1, SR 1.2 | Data classification and access controls are the foundation |
| 2 — Data protection | DSGAI12, DSGAI13 | SR 2.2, SR 3.3 | NL gateway and vector store controls close highest-risk data paths |
| 3 — Integrity | DSGAI04, DSGAI21 | SR 3.3, SR 3.7 | Training and RAG integrity controls close poisoning paths |
| 4 — Resilience | DSGAI17 | SR 7.6, SR 7.7 | Availability controls ensure advisory failures do not propagate to process control |
| 5 — Supply chain | DSGAI06, DSGAI19 | SR 3.2, 62443-2-4 | Supplier requirements for all GenAI vendors with OT data access |
| 6 — Ongoing | DSGAI02–DSGAI16, DSGAI18–DSGAI20 | SR 6.1/6.6, SR 4.4 | Monitoring, telemetry controls, and advanced attack coverage |

---

## References

- [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [NIST SP 800-82 Rev 3 — Guide to OT Security](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [LLM Top 10 × ISA/IEC 62443](../llm-top10/LLM_ISA62443.md)
- [Agentic Top 10 × ISA/IEC 62443](../agentic-top10/Agentic_ISA62443.md)
- [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)
- [IEC 61511 — Functional Safety](https://www.iec.ch/homepage)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full OT entries with zone model, SL ratings, and OT deployment checklist | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
