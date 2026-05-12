<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : NIST SP 800-82 Rev 3 — Guide to Operational Technology (OT) Security
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × NIST SP 800-82 Rev 3

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [NIST SP 800-82 Revision 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)
— Guide to Operational Technology (OT) Security, published May 2023
by the National Institute of Standards and Technology.

---

## Why SP 800-82 Rev 3 for LLM security

NIST SP 800-82 Rev 3 is the definitive U.S. government guidance for
securing industrial control systems, SCADA, distributed control
systems (DCS), and other OT environments. It is referenced by CISA,
mandatory for many federal agencies under FISMA, and widely adopted
across energy, water, transportation, manufacturing, and chemical
sectors globally.

Rev 3 (2023) significantly expanded coverage of cloud, remote access,
and emerging technology risks — making it the most applicable version
for LLM integration in OT environments. It aligns directly with
ISA/IEC 62443 (see `LLM_ISA62443.md`) while providing US-government-
specific implementation guidance, threat intelligence references, and
sector-specific considerations.

**Use this file alongside `LLM_ISA62443.md`.** The two frameworks are
complementary: ISA 62443 provides the zone model and security level
requirements; SP 800-82 provides the implementation guidance,
network architecture recommendations, and U.S. regulatory context.

---

## SP 800-82 Rev 3 structure

| Section | Title | LLM relevance |
|---|---|---|
| Section 4 | OT Overview and Key Differences from IT | Architecture context for LLM deployment |
| Section 5 | OT Threats and Vulnerabilities | Threat mapping for LLM-specific OT risks |
| Section 6 | Risk Management | Risk assessment framework for LLM integration |
| Section 7 | Recommended Security Architecture | Network segmentation, DMZ design for LLM |
| Section 8 | OT Security Program | Governance, policy, and programme requirements |
| Appendix G | Network Architecture Examples | Reference architectures for LLM placement |

**SP 800-82 Rev 3 references NIST SP 800-53 Rev 5 controls.** Where
relevant, specific SP 800-53 control identifiers are cited in this
mapping — these are the same controls used in FedRAMP, FISMA, and
CMMC compliance programmes.

---

## Quick-reference summary

| ID | Name | OT Severity | SP 800-82 Sections | SP 800-53 Controls | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | **Critical** | 5.3, 6.2, 7.2 | SI-10, SI-3, AC-3 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | 5.4, 6.2, 7.3 | SC-28, AC-3, AU-9 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | 5.5, 6.3, 8.4 | SA-12, SR-3, SR-6 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | **Critical** | 5.3, 6.2, 7.2 | SI-7, SI-10, AU-12 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | 5.3, 7.2 | SI-10, SI-3, CM-7 | Foundational–Hardening |
| LLM06 | Excessive Agency | **Critical** | 5.3, 6.2, 7.1 | AC-6, AC-3, AU-12 | Foundational–Advanced |
| LLM07 | System Prompt Leakage | Medium | 5.4, 7.3 | SC-28, AC-3, AU-9 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | 5.3, 6.2 | SI-7, SC-28, AC-3 | Hardening–Advanced |
| LLM09 | Misinformation | High in OT | 5.3, 6.2, 8.2 | SI-3, AC-3, AT-3 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | **Critical** | 5.6, 6.2, 7.2 | SC-5, SI-17, AU-12 | Foundational–Advanced |

---

## Audience tags

- **OT security engineer** — full file, primary implementation reference
- **Federal agency security officer** — SP 800-53 control mapping, FISMA alignment
- **ICS security architect** — Section 7 network architecture references
- **CISO (critical infrastructure)** — Section 6 risk management, Section 8 programme
- **CMMC / FedRAMP assessor** — SP 800-53 control identifiers per vulnerability
- **Procurement / CISA alignment** — supply chain entries, Section 8.4

---

## SP 800-82 Rev 3 network architecture context

SP 800-82 Rev 3 recommends a defense-in-depth architecture with
multiple layers of segmentation between enterprise and control
networks. LLMs must be placed within this architecture explicitly —
not assumed to fit in an existing tier.

**Recommended LLM placement per SP 800-82 Rev 3 Appendix G:**
```
Enterprise Zone (Level 4–5)
    ? [Firewall + proxy — HTTPS only, no direct OT protocol access]
DMZ / Demilitarized Zone (Level 3.5)
    ? LLMs should be deployed HERE when they need OT data access
    ? [Data diode or unidirectional gateway where feasible]
    ? [Firewall — OT protocol aware, allowlisted flows only]
Control Zone (Level 3) — SCADA, historian, HMI
    ? [Firewall — minimal, monitored]
Field Zone (Level 0–2) — PLCs, RTUs, field devices
```

**Key SP 800-82 Rev 3 architecture principles for LLM deployment:**
- LLMs are DMZ or enterprise-tier components — never control zone
- Data flows from historian to LLM must be read-only and logged
- LLM outputs destined for operator display must pass through
  the DMZ firewall with output validation
- No direct LLM connection to OT protocols (Modbus, DNP3, OPC-UA)
  without a validated, allowlisted protocol gateway

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**OT Severity:** Critical

Malicious instructions in input or processed content manipulate LLM
behaviour. In OT environments, prompt injection reaching an LLM with
any connection to historian data, work order systems, or operator
interfaces can result in incorrect process guidance, suppressed alarms,
or manipulated maintenance schedules.

**SP 800-82 Rev 3 threat reference:**
Section 5.3 — "Attacks on OT via IT/OT convergence paths" —
explicitly identifies the IT/OT boundary as a primary attack vector.
LLMs deployed at this boundary without input validation are a new
instantiation of this documented threat pattern.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.3 — Threats | Malicious code and logic attacks via IT/OT convergence | Prompt injection as a new logic attack vector through LLM at the IT/OT boundary |
| Section 6.2 — Risk assessment | Identify threats, vulnerabilities, and impacts for all OT systems | Prompt injection documented in OT risk assessment for each LLM integration |
| Section 7.2 — Network segmentation | Defense-in-depth network architecture with validated data flows | Input validation layer at the DMZ/control zone boundary — prompt injection filtered before reaching LLM |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SI-10 | Information Input Validation | Validate all inputs to LLMs connected to OT systems — reject inputs containing injection indicators |
| SI-3 | Malicious Code Protection | Treat prompt injection as a malicious code analog — detection and response controls required |
| AC-3 | Access Enforcement | LLM access to OT systems enforced by policy — injection cannot escalate LLM access beyond defined scope |

#### Mitigations by tier

**Foundational**
- SI-10: Implement input validation at the DMZ boundary for
  all content entering LLM context from OT sources — historian
  data, alarm logs, work orders, and operator inputs
- Establish a documented threat profile for prompt injection
  in your OT risk assessment (Section 6.2) — specific to
  each LLM integration point
- Treat all external content processed by LLMs as untrusted —
  vendor communications, web content, and third-party data
  feeds are not trusted inputs regardless of source

**Hardening**
- SI-3: Deploy prompt injection detection at the IT/OT
  boundary — active monitoring, not just filtering
- Section 7.2: Validate network segmentation — confirm that
  LLM compromise cannot provide direct access to control zone
  systems without crossing a monitored firewall
- Maintain adversarial test suite covering OT-specific
  injection vectors — indirect injection through historian
  data and maintenance record content

**Advanced**
- Implement architectural separation between LLM advisory
  function and any control action path — Section 7.2
  defense-in-depth principle applied to LLM outputs
- Conduct OT-specific red team exercises targeting prompt
  injection via historian data, alarm content, and
  maintenance system records
- Document LLM prompt injection in the site OT security
  programme (Section 8) — included in incident response
  procedures and operator training

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Claroty | Commercial | https://claroty.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISA/IEC 62443 SR 3.3 · MITRE ATT&CK ICS T0855 · NERC CIP-007

---

### LLM02 — Sensitive Information Disclosure

**OT Severity:** High

LLMs with OT data access can disclose process parameters, equipment
specifications, network topology, and safety system configurations —
providing adversaries with the operational intelligence needed to
plan targeted physical attacks.

**SP 800-82 Rev 3 threat reference:**
Section 5.4 — "Information disclosure and espionage" — identifies
OT network topology, device configurations, and process parameters
as high-value intelligence targets. LLMs with historian access
represent a new path for automated operational intelligence gathering.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.4 — Threats | Information disclosure and OT espionage | LLMs with historian access as a new vector for automated OT intelligence gathering |
| Section 6.2 — Risk assessment | Assess confidentiality of OT data | OT data classification applied to all data accessible by LLMs |
| Section 7.3 — Data protection | Protecting OT data at rest and in transit | Encryption and access controls on all OT data paths feeding LLM context |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SC-28 | Protection of Information at Rest | OT data used in LLM context encrypted at rest — historian exports, embedding stores, prompt caches |
| AC-3 | Access Enforcement | LLM access to OT data enforced by classification — sensitive process and network data requires elevated access tier |
| AU-9 | Protection of Audit Information | LLM access logs to OT data protected — audit trail of all OT data accessed by LLM |

#### Mitigations by tier

**Foundational**
- AC-3: Classify all OT data before granting LLM access —
  apply the same classification framework used for OT network
  documentation to historian data, process parameters, and
  equipment specifications
- SC-28: Encrypt all OT data at rest in LLM context —
  historian exports, prompt caches, embedding stores, and
  observability logs containing OT data
- Restrict LLM read access to minimum required historian tags —
  do not grant broad SELECT access to full historian namespace

**Hardening**
- AU-9: Protect and retain all LLM access logs to OT data —
  every historian query, every data element accessed, every
  output generated — immutable audit trail
- Implement output redaction for OT-specific sensitive
  identifiers — equipment tags, IP addresses, safety
  function identifiers masked before leaving DMZ
- Section 7.3: Apply data diode principles to historian-to-LLM
  data flows where feasible — data flows from OT to LLM,
  not in the reverse direction

**Advanced**
- Conduct OT data disclosure red team exercise — attempt to
  extract operational intelligence through crafted LLM
  queries against your specific historian and SCADA configuration
- Apply data loss prevention to all LLM output channels —
  OT-specific patterns (tag IDs, device names, network addresses)
  detected and blocked before external transmission
- Section 6.2: Include OT data disclosure via LLM in the
  site risk assessment — quantify the operational intelligence
  value of data accessible to each LLM integration

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nozomi Networks | Commercial | https://www.nozominetworks.com |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage
- Other frameworks: ISA/IEC 62443 SR 4.1/4.2 · NERC CIP-011 · IEC 62351

---

### LLM03 — Supply Chain Vulnerabilities

**OT Severity:** High

LLM components introduced into OT environments inherit the criticality
of the OT supply chain. SP 800-82 Rev 3 has significantly expanded
supply chain guidance in its 2023 revision — directly applicable to
LLM component procurement and deployment in critical infrastructure.

**SP 800-82 Rev 3 reference:**
Section 8.4 — "OT Supply Chain Risk Management" — provides specific
guidance on managing third-party software and hardware risks in OT
environments. LLM model weights, inference runtimes, and plugins are
in scope as OT software components.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.5 — Supply chain threats | Third-party software compromise as OT attack vector | LLM model weights and plugins as supply chain risk components |
| Section 6.3 — Risk response | Supply chain risk treatment | ML SBOM and component integrity verification as supply chain controls |
| Section 8.4 — Supply chain programme | OT supply chain risk management programme | LLM vendors subject to same supply chain security requirements as OT software vendors |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SA-12 | Supply Chain Protection | Security requirements applied to all LLM component vendors — provenance, integrity, vulnerability disclosure |
| SR-3 | Supply Chain Controls and Plans | Documented supply chain security plan covering LLM components in OT deployment |
| SR-6 | Supplier Assessments and Reviews | Periodic security assessment of LLM vendors with OT-deployed components |

#### Mitigations by tier

**Foundational**
- SA-12: Apply OT supply chain security requirements to all
  LLM component vendors — provenance documentation, integrity
  guarantees, and vulnerability disclosure obligations
- Maintain ML SBOM for all LLM components in OT deployment —
  model, adapters, inference runtime, and libraries — same
  rigour as OT software asset inventory
- Pin all LLM component versions — no automatic updates
  in OT environments, ever

**Hardening**
- SR-3: Develop a supply chain security plan for LLM
  components in OT — covers procurement, testing, deployment,
  update, and decommission lifecycle
- Apply OT change management to all LLM component updates —
  test in representative non-production environment before
  any OT deployment
- Verify cryptographic signatures of all LLM components
  before OT deployment — unsigned components rejected

**Advanced**
- SR-6: Conduct periodic security assessments of LLM vendors
  with OT-deployed components — include in the site OT
  supply chain risk management programme (Section 8.4)
- Operate isolated LLM component evaluation environment —
  test behavioural characteristics before Zone 3 promotion
- Establish responsible disclosure relationship with LLM
  vendors — OT-specific vulnerability notification path
  with defined response SLA

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| CycloneDX | Open-source | https://cyclonedx.org |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: ISA/IEC 62443 62443-2-4 · NERC CIP-013 · NIST SP 800-218A

---

### LLM04 — Data and Model Poisoning

**OT Severity:** Critical

Adversaries corrupt training data or model weights to embed backdoors
causing incorrect process guidance — effects baked into the model
and invisible until a trigger condition is reached during operations.
In OT, a poisoned LLM providing process recommendations is a
persistent insider threat with authenticated access to operational
decision-making.

**SP 800-82 Rev 3 threat reference:**
Section 5.3 — "Attacks targeting the integrity of OT data and
systems" — this threat class maps directly to model poisoning:
the integrity of the LLM's outputs cannot be assured if the
model's training data or weights have been compromised.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.3 — Integrity threats | Attacks targeting OT data and system integrity | Model poisoning as an integrity attack on the LLM advisory system |
| Section 6.2 — Risk assessment | Assess integrity risks for all OT-connected systems | Model poisoning scenarios included in OT risk assessment for each LLM |
| Section 7.2 — Defense-in-depth | Layered controls to maintain system integrity | Independent validation of LLM outputs against rule-based reference systems |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SI-7 | Software, Firmware, and Information Integrity | Model integrity verification before each OT deployment — hash-based integrity check |
| SI-10 | Information Input Validation | Training data validation — adversarial content detected and rejected before training |
| AU-12 | Audit Record Generation | Full audit trail of LLM outputs — poisoning indicators detectable through output analysis |

#### Mitigations by tier

**Foundational**
- SI-7: Implement model integrity verification before each OT
  deployment — hash-based check against approved baseline,
  deviation triggers rejection
- Validate all training data sourced from OT historian or
  other OT systems — SI-10 input validation applied to
  training pipeline, not just inference
- Establish model rollback capability — approved clean version
  always available for immediate revert on poisoning detection

**Hardening**
- AU-12: Implement comprehensive LLM output audit trail —
  all recommendations logged, enabling retrospective analysis
  for poisoning indicators
- Section 7.2: Cross-validate LLM process recommendations
  against independent rule-based reference — discrepancies
  flagged before display to operator
- Apply adversarial testing covering OT-specific poisoning
  scenarios before each OT deployment — alarm suppression,
  incorrect setpoint recommendation, false health assessment

**Advanced**
- Conduct post-training backdoor detection as a mandatory
  OT deployment gate — neural cleanse or equivalent,
  results documented in site security records
- SI-7: Integrate model integrity monitoring into OT SIEM —
  runtime hash verification, deviation triggers alert and
  agent suspension
- Include model poisoning scenarios in Process Hazard Analysis —
  assess what physical consequences a successfully poisoned
  LLM could produce for each process area it advises

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| Dragos | Commercial | https://www.dragos.com |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Poisoning
- Other frameworks: ISA/IEC 62443 SR 3.3/3.7 · MITRE ATT&CK ICS T0831 · NERC CIP-010

---

### LLM05 — Insecure Output Handling

**OT Severity:** High

LLM-generated output passed to OT systems without validation can
enable injection into HMI rendering, historian write-back, or work
order systems. SP 800-82 Rev 3 Section 7.2 defense-in-depth
principles require that all data crossing zone boundaries be validated —
LLM output is no exception.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.3 — Threats | Code injection and execution via data paths | LLM output injection as a new instantiation of this threat at the IT/OT boundary |
| Section 7.2 — Network segmentation | Validated data flows across zone boundaries | LLM output validated at DMZ boundary before entering control zone display or data systems |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SI-10 | Information Input Validation | LLM outputs validated before passing to OT systems — schema validation, allowlist enforcement |
| SI-3 | Malicious Code Protection | LLM output scanning for malicious content before OT system ingestion |
| CM-7 | Least Functionality | OT interfaces that consume LLM output configured to accept only defined, safe input formats |

#### Mitigations by tier

**Foundational**
- SI-10: Treat all LLM output as untrusted input to OT
  systems — encode, validate, and sanitise before rendering
  in HMI or passing to historian or work order systems
- CM-7: Configure OT interfaces consuming LLM output to
  accept only allowlisted formats — reject any LLM output
  that does not conform to expected structure
- Never pass raw LLM output directly to historian write-back,
  alarm management systems, or control interfaces

**Hardening**
- SI-3: Deploy output scanning at the DMZ boundary — scan
  LLM outputs for malicious content before crossing into
  control zone display infrastructure
- Section 7.2: Validate that DMZ firewall enforces output
  format constraints — malformed or unexpected LLM output
  blocked at the boundary
- Test all OT interfaces consuming LLM output for injection
  vulnerabilities — include in OT penetration testing scope

**Advanced**
- Implement dedicated LLM output validation gateway at the
  DMZ boundary — independent validation layer not controlled
  by the LLM or its hosting infrastructure
- Section 7.2: Conduct architecture review confirming that
  LLM output injection cannot propagate to control zone
  through any path not covered by DMZ validation
- Include LLM output injection scenarios in OT security
  exercises and tabletop exercises

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISA/IEC 62443 SR 3.3 · NIST SP 800-53 SI-10 · MITRE ATT&CK ICS T0855

---

### LLM06 — Excessive Agency

**OT Severity:** Critical

LLMs with excessive autonomy over OT interfaces can execute unintended
process actions. SP 800-82 Rev 3 Section 7.1 explicitly requires
minimal necessary functionality and access — the least functionality
principle is the SP 800-82 equivalent of least agency.

**SP 800-82 Rev 3 reference:**
Section 7.1 — "Separation of OT from corporate networks" —
establishes that data flows between IT and OT must be restricted to
only what is operationally necessary. LLM write access to OT systems
must meet this same standard of necessity.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.3 — Threats | Unauthorised command execution via IT/OT interfaces | LLM autonomous actions as a new path for unauthorised command execution |
| Section 6.2 — Risk assessment | Assess impact of unauthorised access and control | LLM excessive agency assessed as an unauthorised access risk for each OT interface |
| Section 7.1 — Architecture | Minimal necessary connectivity at IT/OT boundary | LLM access to OT systems restricted to minimum required — read-only by default |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| AC-6 | Least Privilege | LLM granted minimum necessary OT access — read-only to historian, no write access without documented justification |
| AC-3 | Access Enforcement | LLM access to OT systems enforced by policy — scope cannot be exceeded regardless of model instruction |
| AU-12 | Audit Record Generation | All LLM actions in OT context logged — full accountability for every OT data access and any recommended action |

#### Mitigations by tier

**Foundational**
- AC-6: Apply least privilege to all LLM OT access — read-only
  to historian by default, no autonomous write access without
  documented business justification and human confirmation gate
- Require human confirmation for every control action arising
  from an LLM recommendation — confirmation through a
  separate interface, not through the LLM itself
- AU-12: Log all LLM interactions with OT systems — every
  historian query, every recommendation, every operator
  confirmation or rejection

**Hardening**
- AC-3: Implement and enforce access controls at the OT
  interface layer — LLM access scope cannot be exceeded
  regardless of what the model requests
- Section 7.1: Review all LLM OT data flows against the
  minimum necessary standard — remove any access that cannot
  be justified by a specific operational requirement
- Conduct regular access reviews — any LLM permission not
  actively used in the past 30 days is removed

**Advanced**
- Section 7.1: Implement architectural separation between
  LLM advisory output and control action execution — physical
  or logical separation guaranteeing LLM output cannot
  directly trigger a control action without human approval
- Include LLM excessive agency in OT risk assessment
  (Section 6.2) — assess what physical consequences are
  possible if each LLM integration executes autonomously
- Red team exercises testing LLM excessive agency scenarios —
  indirect injection through OT data sources leading to
  autonomous process actions

#### Tools

| Tool | Type | Link |
|---|---|---|
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| Claroty | Commercial | https://claroty.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISA/IEC 62443 SR 2.1/2.2 · IEC 61511 · NERC CIP-005

---

### LLM07 — System Prompt Leakage

**OT Severity:** Medium (elevated to High if prompt contains network
topology or safety configuration)

System prompts for OT-deployed LLMs often contain sensitive
operational information. SP 800-82 Rev 3 Section 5.4 identifies
OT configuration data as high-value reconnaissance intelligence —
system prompts containing this information are in scope.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.4 — Information disclosure | OT configuration and topology data as espionage target | System prompts containing OT specifics treated as sensitive configuration data |
| Section 7.3 — Data protection | Protecting sensitive OT data | System prompt encryption and access controls as data protection measures |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SC-28 | Protection of Information at Rest | System prompts encrypted at rest — not stored in cleartext configuration files |
| AC-3 | Access Enforcement | System prompt access restricted to authorised personnel — version controlled, access logged |
| AU-9 | Protection of Audit Information | System prompt access logs protected — unauthorised access attempts detectable |

#### Mitigations by tier

**Foundational**
- SC-28: Encrypt all OT LLM system prompts at rest — not
  stored in cleartext application configuration or source code
- Remove all OT-specific identifiers from system prompts
  where possible — use generic references resolved to
  specific assets at runtime through a controlled lookup
- Apply access controls to system prompt storage — same
  classification as OT configuration files

**Hardening**
- Conduct prompt extraction testing before each OT LLM
  deployment — assess what OT reconnaissance value an
  adversary could derive from extracted prompt content
- Section 7.3: Implement information flow restriction —
  system prompt content cannot be output to any destination
  outside the authorised OT operator scope
- Rotate system prompt versions on schedule — limits shelf
  life of any extracted OT configuration intelligence

**Advanced**
- Implement system prompt tokenisation for all OT-specific
  identifiers — equipment tags, IP addresses, safety
  parameters replaced with opaque tokens
- Include system prompt leakage in OT red team exercises —
  quantify the reconnaissance value of extracted prompts
  for your specific OT environment
- Section 5.4: Document system prompt leakage in the OT
  threat model — specific to each LLM deployment with
  sensitive OT context in the prompt

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: ISA/IEC 62443 SR 4.1 · NERC CIP-011 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**OT Severity:** Medium (elevated if embedding stores contain
equipment specifications or safety procedure documentation)

Vector stores used by OT LLMs — containing maintenance procedures,
equipment documentation, and process parameters — are susceptible to
adversarial retrieval manipulation that could surface incorrect
technical guidance to operators.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.3 — Integrity threats | Attacks targeting the integrity of OT decision-support data | Vector store poisoning as an integrity attack on LLM knowledge sources |
| Section 6.2 — Risk assessment | Assess integrity risks for all OT-connected systems | Vector store integrity included in OT LLM risk assessment |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SI-7 | Software, Firmware, and Information Integrity | Vector store integrity monitoring — alert on anomalous content or unexpected modifications |
| SC-28 | Protection of Information at Rest | OT vector store content encrypted at rest |
| AC-3 | Access Enforcement | Access controls on OT vector stores — RBAC enforced at collection level |

#### Mitigations by tier

**Foundational**
- AC-3: Implement access controls on all OT vector stores —
  RBAC enforced at collection level, no unauthenticated access
- SC-28: Encrypt all OT vector store content at rest —
  equipment specifications and safety procedures require
  same protection as equivalent OT documentation
- Classify OT vector store content before ingestion —
  safety procedures require higher access tier than
  general operational documentation

**Hardening**
- SI-7: Implement vector store integrity monitoring —
  alert on anomalous query patterns or unexpected content
  modifications in OT knowledge stores
- Implement trust-tiered retrieval — safety-critical and
  vendor-sensitive documentation weighted by source trust,
  not only semantic similarity
- Apply content integrity verification on vector store
  ingestion — only hash-verified authorised documents admitted
  to OT knowledge base

**Advanced**
- Conduct embedding inversion testing against OT vector
  stores — validate that safety procedure details and
  equipment specifications cannot be reconstructed from
  embeddings
- Section 6.2: Include vector store adversarial retrieval
  in OT risk assessment — assess what incorrect guidance
  an adversary could surface through crafted queries
- Integrate vector store anomaly alerts into OT SIEM —
  unusual retrieval patterns treated as potential
  reconnaissance activity

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISA/IEC 62443 SR 3.7 · NIST AI RMF MS-2.5

---

### LLM09 — Misinformation

**OT Severity:** High

LLMs generate plausible but incorrect process guidance — wrong
maintenance procedures, incorrect alarm interpretations, false
equipment health assessments. Operators acting on LLM misinformation
in OT environments can cause equipment damage, process upsets,
environmental incidents, or personnel harm.

**SP 800-82 Rev 3 reference:**
Section 8.2 — "OT Security Awareness and Training" — identifies
operator training as a critical control. Operators must understand
LLM limitations — this is an SP 800-82 training requirement, not
optional guidance.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.3 — Integrity threats | Attacks degrading the reliability of OT decision-support | LLM misinformation as an integrity attack on operator decision-making |
| Section 6.2 — Risk assessment | Assess reliability of OT advisory systems | LLM accuracy limitations assessed in OT risk assessment per use case |
| Section 8.2 — Training | OT security awareness and training | Operator training on LLM limitations and verification requirements |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SI-3 | Malicious Code Protection | Analogy: LLM misinformation detection controls as an integrity assurance layer on advisory outputs |
| AC-3 | Access Enforcement | LLM advisory outputs restricted to defined advisory roles — never authoritative source for safety-critical procedures |
| AT-3 | Role-Based Training | Operator training on LLM advisory limitations — mandatory for all operators using LLM decision-support tools |

#### Mitigations by tier

**Foundational**
- AT-3: Implement role-based training for all operators
  using LLM decision-support tools — training must cover
  LLM hallucination risk, verification requirements, and
  when to override LLM recommendations
- AC-3: Restrict LLM advisory role — LLM outputs clearly
  distinguished from engineering-approved procedures in all
  HMI and operator console displays
- Require source citation for all LLM recommendations —
  operators verify against the cited source before acting
  on any safety-relevant recommendation

**Hardening**
- Section 6.2: Assess LLM accuracy limitations in OT risk
  assessment — specific to each process area and equipment
  type the LLM advises on
- Cross-validate LLM recommendations for safety-relevant
  procedures against independent rule-based reference —
  discrepancies flagged to operator and engineering
- Deploy RAG grounded on authoritative, version-controlled
  OT documentation — not on uncontrolled web content

**Advanced**
- Conduct OT-specific hallucination testing — validate LLM
  accuracy on equipment-specific procedures for all equipment
  types in your plant before deployment
- Section 8.2: Include LLM misinformation scenarios in
  operator competency assessments — verify operators can
  identify when to seek independent verification
- Include LLM misinformation in Process Hazard Analysis —
  assess physical consequences of plausible but incorrect
  guidance for each LLM advisory use case

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning
- Other frameworks: ISA/IEC 62443 SR 3.1 · IEC 61511 (human factors) · AIUC-1 C/F

---

### LLM10 — Unbounded Consumption

**OT Severity:** Critical

Resource exhaustion caused by adversarial LLM queries can saturate
the network segment shared with control zone systems, affecting
historian polling, HMI responsiveness, and SCADA communications.
SP 800-82 Rev 3 Section 5.6 identifies denial of service as a
critical OT threat class — LLM-induced resource exhaustion is a
new instantiation of this documented threat.

**SP 800-82 Rev 3 threat reference:**
Section 5.6 — "Denial of service attacks against OT systems" —
explicitly identifies network resource exhaustion as an OT availability
threat. LLM resource consumption must be architected and controlled
to prevent this threat from manifesting through the IT/OT boundary.

#### SP 800-82 Rev 3 mapping

| Section | Guidance | OT application |
|---|---|---|
| Section 5.6 — DoS threats | Denial of service attacks targeting OT availability | LLM-induced resource exhaustion as a DoS vector affecting shared OT network infrastructure |
| Section 6.2 — Risk assessment | Assess availability risks for OT systems | LLM resource consumption impact assessed on shared OT network and compute infrastructure |
| Section 7.2 — Network segmentation | Network architecture preventing DoS propagation | LLM infrastructure isolated from OT control network — bandwidth caps at DMZ boundary |

**SP 800-53 Rev 5 controls:**

| Control | Title | Application |
|---|---|---|
| SC-5 | Denial of Service Protection | LLM infrastructure protected against resource exhaustion attacks affecting OT availability |
| SI-17 | Fail-Safe Procedures | LLM service degradation has defined fail-safe behaviour — process control continues without LLM |
| AU-12 | Audit Record Generation | LLM resource consumption logged — patterns indicating exhaustion attacks detectable |

#### Mitigations by tier

**Foundational**
- SC-5: Implement rate limiting on all LLM interfaces —
  hard caps on queries per time window preventing saturation
  of shared OT network resources
- Section 7.2: Network segmentation — LLM compute on dedicated
  segment, bandwidth-capped conduit to OT network, LLM traffic
  cannot saturate OT control communications
- SI-17: Define fail-safe behaviour for LLM service degradation —
  process control must continue normally when LLM is unavailable,
  operators not dependent on LLM for safety-critical functions

**Hardening**
- AU-12: Integrate LLM resource consumption monitoring with
  OT network monitoring — alert when LLM traffic approaches
  thresholds that could affect OT communications
- Section 7.2: Validate network segmentation under load —
  simulate LLM saturation and confirm zero impact on
  historian polling, HMI response, and SCADA communications
- Implement circuit breakers — LLM service degradation
  isolated from OT system availability

**Advanced**
- Conduct OT-specific load testing — simulate adversarial
  LLM resource exhaustion and verify zero impact on
  Zone 3 system availability and response times
- SC-5: Implement sponge example detection — inputs designed
  to maximise LLM computation identified and rejected before
  they affect OT network performance
- Section 6.2: Include LLM denial-of-service in OT risk
  assessment — quantify the impact of LLM infrastructure
  saturation on each OT system sharing network resources

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Nozomi Networks | Commercial | https://www.nozominetworks.com |
| Kong Gateway | Open-source | https://github.com/Kong/kong |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 · NERC CIP-007 · IEC 62351

---

## SP 800-82 Rev 3 and ISA 62443 crosswalk

Use this table to align SP 800-82 guidance with ISA/IEC 62443
requirements for organisations using both frameworks:

| SP 800-82 Rev 3 Section | ISA/IEC 62443 equivalent | LLM Top 10 entries |
|---|---|---|
| Section 5.3 — Integrity threats | FR 3 — System Integrity (SI) | LLM01, LLM04, LLM05 |
| Section 5.4 — Information disclosure | FR 4 — Data Confidentiality (DC) | LLM02, LLM07 |
| Section 5.5 — Supply chain | 62443-2-4, FR 3 SI-2 | LLM03 |
| Section 5.6 — Denial of service | FR 7 — Resource Availability (RA) | LLM10 |
| Section 6.2 — Risk assessment | 62443-3-2 Security risk assessment | All entries |
| Section 7.1 — Architecture | 62443-1-1 Zone/conduit model | LLM06 |
| Section 7.2 — Network segmentation | FR 5 — Restricted Data Flow (RDF) | LLM01, LLM05, LLM10 |
| Section 7.3 — Data protection | FR 4 — Data Confidentiality (DC) | LLM02, LLM07, LLM08 |
| Section 8.2 — Training | 62443-2-1 Security programme | LLM09 |
| Section 8.4 — Supply chain programme | 62443-2-4 Supplier requirements | LLM03 |

---

## SP 800-82 Rev 3 OT LLM deployment checklist

### Risk assessment (Section 6)

- [ ] Prompt injection documented in OT risk assessment per LLM integration
- [ ] Data disclosure risk assessed — OT data accessible by LLM classified
- [ ] Supply chain risks assessed — LLM vendor security posture documented
- [ ] Model poisoning impact assessed — physical consequences per process area
- [ ] Excessive agency impact assessed — what autonomous action could cause
- [ ] DoS impact assessed — LLM resource exhaustion impact on OT communications

### Network architecture (Section 7)

- [ ] LLM placed in DMZ or enterprise tier — not in control zone
- [ ] Data flows from historian to LLM read-only and logged
- [ ] LLM output validated at DMZ boundary before reaching control zone displays
- [ ] LLM network segment bandwidth-capped — cannot saturate OT control traffic
- [ ] No direct LLM connection to OT field protocols without validated gateway

### Security programme (Section 8)

- [ ] LLM components included in OT asset inventory (Section 8.1)
- [ ] Operator training on LLM limitations completed (Section 8.2)
- [ ] LLM scenarios included in OT incident response plan (Section 8.3)
- [ ] LLM vendors assessed under OT supply chain programme (Section 8.4)
- [ ] LLM security requirements included in vendor contracts (Section 8.4)

### SP 800-53 controls verification

- [ ] AC-3 access enforcement implemented and tested for all OT LLM access
- [ ] AC-6 least privilege verified — LLM access reviewed and minimised
- [ ] AU-12 audit logging active for all LLM OT data access
- [ ] SC-5 DoS protection implemented — rate limiting and network isolation
- [ ] SC-28 encryption implemented for all OT data at rest in LLM context
- [ ] SI-7 integrity verification implemented for LLM model components
- [ ] SI-10 input validation implemented at DMZ boundary for LLM inputs

---

## Regulatory alignment

Organisations under these frameworks will find SP 800-82 Rev 3
directly referenced or applicable:

| Regulation / Programme | SP 800-82 Rev 3 status | Primary LLM entries |
|---|---|---|
| FISMA (US federal) | Referenced standard | All entries — Section 6 risk management |
| NERC CIP (electric) | Aligned — CISA recommends | LLM01 (CIP-007), LLM03 (CIP-013), LLM10 (CIP-007) |
| AWIA 2018 (water) | Aligned — EPA recommends | LLM01, LLM06, LLM10 |
| TSA cybersecurity directives (pipeline) | Aligned | LLM01, LLM04, LLM06 |
| CMMC Level 2–3 | SP 800-53 controls required | All entries — control IDs cited |
| NIS2 Directive (EU) | SP 800-82 referenced in ENISA guidance | LLM01, LLM06, LLM10 |

---

## Implementation priority for OT environments

| Phase | LLM entries | SP 800-82 sections | SP 800-53 controls | Rationale |
|---|---|---|---|---|
| 1 — Before OT deployment | LLM06, LLM10 | 7.1, 5.6 | AC-6, SC-5 | Excessive agency and DoS can cause immediate physical impact |
| 2 — Deployment gates | LLM01, LLM05 | 5.3, 7.2 | SI-10, CM-7 | Injection and output handling validated before go-live |
| 3 — First 30 days | LLM03, LLM04 | 8.4, 5.3 | SA-12, SI-7 | Supply chain and integrity require pipeline-level controls |
| 4 — Ongoing | LLM02, LLM07, LLM08, LLM09 | 5.4, 7.3, 8.2 | SC-28, AU-9, AT-3 | Data protection, prompt security, knowledge integrity, training |

---

## References

- [NIST SP 800-82 Rev 3 — Guide to Operational Technology Security](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)
- [NIST SP 800-53 Rev 5 — Security and Privacy Controls](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [CISA ICS Security Resources](https://www.cisa.gov/ics)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)
- [NIST SP 800-218A — Secure Software Development for AI](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full OT entries with SP 800-53 controls and regulatory crosswalk | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
