<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : NIST Cybersecurity Framework 2.0 (CSF 2.0)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × NIST CSF 2.0

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
(CSF 2.0), published February 2024.

---

## Why CSF 2.0 for LLM security

CSF 2.0 is the most widely adopted cybersecurity framework globally —
used by governments, critical infrastructure operators, and enterprises
across sectors. Three changes in CSF 2.0 make it significantly more
relevant for LLM security than CSF 1.1:

**GOVERN function (new in 2.0):** CSF 2.0 adds a sixth function —
GOVERN — explicitly covering cybersecurity risk management strategy,
supply chain risk, and organisational roles. LLM governance, acceptable
use policy, and AI vendor management all map directly to GOVERN.

**Supply chain elevation:** Supply chain risk management (GV.SC) is now
a dedicated category. LLM model providers, dataset vendors, and plugin
ecosystems are third-party technology suppliers under CSF 2.0 GV.SC.

**Continuous improvement emphasis:** CSF 2.0 strengthens the feedback
loop between IDENTIFY, DETECT, RESPOND, and RECOVER — critical for LLM
systems where the threat surface evolves faster than traditional IT.

---

## CSF 2.0 structure

| Function | Abbreviation | Core purpose |
|---|---|---|
| GOVERN | GV | Cybersecurity risk management strategy, policies, roles, supply chain |
| IDENTIFY | ID | Asset management, risk assessment, improvement |
| PROTECT | PR | Identity management, awareness, data security, platform security, resilience |
| DETECT | DE | Continuous monitoring, adverse event analysis |
| RESPOND | RS | Incident management, analysis, mitigation, reporting |
| RECOVER | RC | Incident recovery, communication |

---

## Quick-reference summary

| ID | Name | Severity | Primary CSF 2.0 Categories | Tier |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | PR.PS-04, DE.CM-01, ID.RA-01, GV.OC-01 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | PR.DS-01, PR.DS-02, DE.CM-01, GV.RM-06 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | GV.SC-01, GV.SC-06, ID.AM-08, PR.PS-02 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | PR.DS-01, DE.CM-09, ID.RA-01, RS.AN-03 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | PR.PS-04, PR.DS-02, DE.CM-01, ID.RA-01 | Foundational–Hardening |
| LLM06 | Excessive Agency | High | PR.AA-05, PR.AA-01, DE.CM-01, GV.OC-01 | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | PR.DS-01, PR.AA-05, DE.CM-01, GV.RM-06 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | PR.DS-01, PR.DS-02, DE.CM-09, ID.AM-08 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | GV.OC-01, DE.CM-09, ID.RA-01, PR.AT-01 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | PR.IR-01, DE.CM-01, RS.MI-01, GV.RM-01 | Foundational–Hardening |

---

## Audience tags

- **CISO / governance** — full file, CSF 2.0 integration for LLM programme
- **Risk manager** — IDENTIFY and GOVERN entries per vulnerability
- **Security operations** — DETECT and RESPOND entries
- **Security engineer** — PROTECT entries per vulnerability
- **Federal agency / FISMA** — CSF 2.0 as NIST reference framework
- **OT engineer** — LLM01, LLM04, LLM10 with ISA 62443 crosswalk

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour. CSF 2.0 addresses this through platform security
(PROTECT), continuous monitoring (DETECT), and risk assessment (IDENTIFY).

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Platform Security | PR.PS-04 | PROTECT | Secure software development practices applied to LLM integrations — input validation as a platform security control |
| Continuous Monitoring | DE.CM-01 | DETECT | Networks and assets monitored for anomalies — LLM input channels monitored for injection indicators |
| Risk Assessment | ID.RA-01 | IDENTIFY | Vulnerabilities in assets identified and documented — prompt injection as a documented vulnerability class for all LLM deployments |
| Organisational Context | GV.OC-01 | GOVERN | Mission and stakeholder expectations inform cybersecurity risk decisions — acceptable LLM use scope defines injection risk surface |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Define acceptable use policy for LLM applications —
  specify which input channels are permitted, what content is
  trusted, and what constitutes an injection attempt
- GV.RM-06: Include prompt injection in enterprise risk register —
  document risk owner, treatment, and review cadence

**IDENTIFY**
- ID.RA-01: Document prompt injection as a vulnerability in every
  LLM asset's risk assessment — include indirect injection via
  RAG, tool returns, and processed documents
- ID.AM-08: Inventory all LLM systems and their input channels —
  unknown input surfaces cannot be protected

**PROTECT**
- PR.PS-04: Implement input validation as a platform security
  control — treat all external content as untrusted before
  entering LLM context
- Deploy architectural separation between system prompt and
  user input — structural control, not policy only

**DETECT**
- DE.CM-01: Monitor LLM input channels for injection indicators —
  anomalous inputs detected and alerted in real time
- DE.AE-02: Analyse detected events to understand attack targets —
  injection attempts correlated across sessions

**RESPOND**
- RS.AN-03: Analyse incidents to determine root cause —
  injection incidents investigated, IOCs documented
- RS.MI-01: Contain injection incidents — session termination,
  downstream action review

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: NIST AI RMF MS-2.5 · ISO 27001 A.8.28 · CIS Controls CIS 16

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, or confidential information through
outputs. CSF 2.0 data security (PR.DS) and continuous monitoring
(DE.CM) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Data-at-rest protected — training data, embeddings, RAG stores containing sensitive information encrypted |
| Data Security | PR.DS-02 | PROTECT | Data-in-transit protected — all LLM API calls and RAG retrieval paths encrypted |
| Continuous Monitoring | DE.CM-01 | DETECT | LLM output channels monitored for sensitive data patterns — DLP coverage |
| Risk Management Strategy | GV.RM-06 | GOVERN | Risk tolerance established — acceptable levels of sensitive data disclosure risk defined per use case |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Establish risk tolerance for sensitive data disclosure
  per LLM use case — what classifications are permitted in LLM
  scope and what controls are required

**IDENTIFY**
- ID.AM-08: Inventory all data assets accessible by LLM systems —
  training data, RAG sources, embedding stores, prompt caches
- ID.RA-03: Identify threats to sensitive data via LLM exposure —
  memorisation, over-retrieval, output reconstruction

**PROTECT**
- PR.DS-01: Encrypt all sensitive data at rest in LLM scope —
  embedding stores, training datasets, RAG document stores,
  prompt caches
- PR.DS-02: Encrypt all LLM data flows in transit —
  TLS 1.2 minimum on all API calls and RAG retrieval
- PR.AA-05: Implement access controls on RAG data sources —
  least-privilege retrieval aligned with user authorisation

**DETECT**
- DE.CM-01: Deploy DLP on all LLM output channels —
  PII and sensitive patterns detected before delivery

**RESPOND**
- RS.AN-03: Investigate sensitive data disclosure incidents —
  determine scope, affected data subjects, regulatory obligations
- RS.CO-03: Report incidents as required — data breach notification
  per applicable regulation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.11/A.8.12 · NIST AI RMF GV-1.6 · EU AI Act Art. 10

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets,
libraries, and plugins. CSF 2.0 GOVERN supply chain risk management
(GV.SC) is the primary category — supply chain is now a first-class
CSF concern.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Cybersecurity supply chain risk management programme — LLM component vendors in scope |
| Supply Chain Risk Management | GV.SC-06 | GOVERN | Cybersecurity requirements included in contracts with suppliers — LLM model and data vendors |
| Asset Management | ID.AM-08 | IDENTIFY | Systems and hardware managed — ML SBOM as asset inventory for LLM components |
| Platform Security | PR.PS-02 | PROTECT | Software managed to reduce risk — LLM component vulnerability management and patching |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Establish cybersecurity supply chain risk management
  programme covering LLM components — model providers, dataset
  vendors, inference runtime suppliers
- GV.SC-06: Include security requirements in all LLM vendor
  contracts — provenance, integrity guarantees, vulnerability
  disclosure obligations, incident notification SLA

**IDENTIFY**
- ID.AM-08: Maintain ML SBOM as part of asset inventory —
  every LLM component (model, adapters, libraries) inventoried
  with version, source, and hash
- ID.RA-08: Receive threat intelligence about supply chain
  threats — subscribe to feeds covering ML component
  and model repository compromise

**PROTECT**
- PR.PS-02: Implement vulnerability management for all LLM
  components — scan SBOM against known CVEs, patch on schedule
- Pin all LLM component versions — no automatic updates
  without review and approval

**DETECT**
- DE.CM-09: Monitor for use of unauthorised software —
  alert on LLM component changes outside approved change
  management process

**RESPOND**
- RS.AN-03: Investigate supply chain incidents —
  determine which deployments are affected by a compromised
  LLM component

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Grype | Open-source | https://github.com/anchore/grype |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · ISO 27001 A.5.19/A.5.21 · CIS Controls CIS 2

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Adversaries corrupt training data or model weights with embedded
backdoors. CSF 2.0 data security (PR.DS), detection (DE.CM), and
incident analysis (RS.AN) address this.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Training data protected at rest — integrity verification, source allowlisting, provenance tracking |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for unauthorised software and configuration changes — model integrity verification at deployment |
| Risk Assessment | ID.RA-01 | IDENTIFY | Poisoning attack vectors identified and documented in risk assessment for each LLM deployment |
| Incident Analysis | RS.AN-03 | RESPOND | Root cause analysis for poisoning incidents — identify affected deployments, assess physical impact |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Apply supply chain controls to training data
  sources — same programme covering model weights extends
  to dataset vendors and data pipeline components

**IDENTIFY**
- ID.RA-01: Document poisoning attack vectors in risk
  assessment per LLM deployment — training data sources,
  fine-tuning pipeline, model weights, supply chain
- ID.AM-08: Maintain provenance records for all training
  data sources as part of asset management

**PROTECT**
- PR.DS-01: Implement training data integrity controls —
  hash-based provenance, source allowlisting, anomaly
  detection on data distributions before training runs
- Establish model rollback capability — approved clean
  checkpoint always available for revert

**DETECT**
- DE.CM-09: Verify model integrity at deployment —
  hash-based check against approved baseline before any
  production promotion
- DE.AE-02: Detect anomalous model output patterns —
  production monitoring for systematic recommendation
  drift indicating poisoning

**RESPOND**
- RS.AN-03: Investigate poisoning incidents — identify
  affected training runs, assess downstream deployments,
  determine physical or operational impact
- RS.MI-02: Remediate poisoning — rollback to clean
  checkpoint, quarantine affected data sources

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032 · ISO 27001 A.8.27

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
injection attacks. CSF 2.0 platform security (PR.PS) and data
security (PR.DS) are the primary PROTECT categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Platform Security | PR.PS-04 | PROTECT | Secure software development practices — output encoding and schema validation as platform security requirements |
| Data Security | PR.DS-02 | PROTECT | Data in transit protected — LLM output validated before passing to downstream systems |
| Continuous Monitoring | DE.CM-01 | DETECT | Networks and assets monitored — output injection patterns detected in LLM output channels |
| Risk Assessment | ID.RA-01 | IDENTIFY | Output injection documented as vulnerability class in risk assessment for all LLM integrations |

#### Mitigations by CSF function

**IDENTIFY**
- ID.RA-01: Document output injection as a vulnerability in
  all LLM integration risk assessments — cover XSS, SQL
  injection, command injection via model output

**PROTECT**
- PR.PS-04: Implement output encoding and schema validation
  as secure development requirements — treat LLM output as
  untrusted input to all downstream systems
- PR.DS-02: Validate all LLM outputs before they cross
  system boundaries — schema enforcement at API gateway

**DETECT**
- DE.CM-01: Monitor LLM output channels for injection patterns —
  automated detection of dangerous content in model responses

**RESPOND**
- RS.MI-01: Contain output injection incidents — block
  affected session, review downstream state changes

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: OWASP ASVS V5 · CIS Controls CIS 16 · CWE-79/CWE-89

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with excessive autonomy over tools execute unintended or harmful
actions. CSF 2.0 identity management (PR.AA) and organisational
context (GV.OC) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions managed — LLM tool access managed as privileged access with least privilege enforcement |
| Identity Management, Authentication & Access Control | PR.AA-01 | PROTECT | Identities managed — LLM service identities inventoried and managed, tool permissions scoped per identity |
| Continuous Monitoring | DE.CM-01 | DETECT | Networks and assets monitored — all LLM tool invocations logged and monitored for anomalous scope |
| Organisational Context | GV.OC-01 | GOVERN | Acceptable use of LLM autonomous actions defined — policy specifies what actions require human confirmation |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Define acceptable scope for LLM autonomous
  actions — which tool operations are permitted without
  human confirmation, which are prohibited autonomously
- GV.RM-01: Include LLM excessive agency in risk management
  strategy — document blast radius per deployment

**IDENTIFY**
- ID.AM-08: Inventory all LLM tool integrations — what
  each tool can do, what permissions it holds, what
  systems it can affect

**PROTECT**
- PR.AA-05: Implement least-privilege access for all LLM
  tool integrations — minimum permissions enforced,
  reviewed on change and quarterly
- PR.AA-01: Manage LLM service identities — unique identity
  per deployment, permissions scoped to defined role

**DETECT**
- DE.CM-01: Log and monitor all LLM tool invocations —
  anomalous scope, unusual parameters, or high frequency
  detected and alerted

**RESPOND**
- RS.MI-01: Contain excessive agency incidents — suspend
  agent, review all actions taken, reverse where possible

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006 · EU AI Act Art. 14 · ISA/IEC 62443 SR 2.1 (OT)

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing security controls are extracted by
adversaries. CSF 2.0 data security (PR.DS) and access control
(PR.AA) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | System prompts classified as sensitive configuration and protected at rest — encrypted, access-controlled |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access to system prompt storage restricted to authorised personnel — least privilege enforced |
| Continuous Monitoring | DE.CM-01 | DETECT | Access to system prompt storage logged and monitored — anomalous access detected |
| Risk Management Strategy | GV.RM-06 | GOVERN | Risk tolerance defined for system prompt exposure — operational security value of prompt confidentiality assessed |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Assess the security value of system prompt
  confidentiality per deployment — prompts containing
  operational details require higher protection level

**PROTECT**
- PR.DS-01: Encrypt system prompts at rest — not in cleartext
  configuration files, source code, or environment variables
- PR.AA-05: Restrict system prompt access to authorised
  personnel — version controlled, access logged

**DETECT**
- DE.CM-01: Monitor access to system prompt storage —
  alert on anomalous access patterns
- Conduct prompt extraction testing — verify resistance
  to known extraction techniques before deployment

**RESPOND**
- RS.AN-03: Investigate extraction incidents — assess
  what operational intelligence an attacker gained

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · ISO 27001 A.5.12 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Vector stores contain sensitive embeddings susceptible to adversarial
retrieval and inference attacks. CSF 2.0 data security (PR.DS) and
asset management (ID.AM) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Vector store content encrypted at rest — embeddings treated as sensitive derived data |
| Data Security | PR.DS-02 | PROTECT | Data in transit protected — vector store queries and results encrypted |
| Asset Management | ID.AM-08 | IDENTIFY | Vector stores inventoried as AI data assets — RBAC status, encryption status, CVE patching status |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for unauthorised software and anomalous access — vector store query anomalies detected |

#### Mitigations by CSF function

**IDENTIFY**
- ID.AM-08: Inventory all vector stores as AI data assets —
  document RBAC status, encryption status, content
  classification, and known CVE exposure

**PROTECT**
- PR.DS-01: Encrypt all vector store content at rest —
  same protection as source documents
- PR.AA-05: Enable RBAC on all vector stores —
  no unauthenticated access in any environment

**DETECT**
- DE.CM-09: Monitor vector store query patterns —
  bulk extraction, unusual query diversity detected
- Patch all vector database CVEs promptly —
  CVE-2024-3584 class as urgent findings

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · ISO 27001 A.8.3/A.8.24 · CIS Controls CIS 3

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but incorrect content. CSF 2.0 organisational
context (GV.OC) and awareness training (PR.AT) address this as a
governance and people risk, not only a technical risk.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Acceptable use policy defines which LLM outputs require verification — high-stakes domains identified |
| Continuous Monitoring | DE.CM-09 | DETECT | Production monitoring for accuracy degradation — hallucination rates tracked per domain |
| Risk Assessment | ID.RA-01 | IDENTIFY | LLM misinformation risk assessed per use case — what decisions are influenced, what is the consequence |
| Awareness and Training | PR.AT-01 | PROTECT | Users trained on LLM output limitations — verification requirements for each use case |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Define accuracy requirements per LLM use case —
  which domains require human verification, which are
  acceptable for advisory use without verification

**IDENTIFY**
- ID.RA-01: Assess misinformation risk per deployment —
  what decisions are influenced by LLM output, what
  is the consequence of incorrect recommendations

**PROTECT**
- PR.AT-01: Train all users of LLM decision-support tools
  on output limitations — mandatory before access granted
- Deploy RAG grounded on authoritative, version-controlled
  sources — citations displayed alongside responses

**DETECT**
- DE.CM-09: Monitor production accuracy metrics —
  hallucination rates per domain, alert on degradation

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 F · NIST AI RMF GV-1.7

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption.
CSF 2.0 infrastructure resilience (PR.IR) and risk management (GV.RM)
are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Infrastructure Resilience | PR.IR-01 | PROTECT | Networks and environments protected to achieve resilience — rate limiting and resource controls as resilience measures |
| Continuous Monitoring | DE.CM-01 | DETECT | LLM resource consumption monitored — anomalous usage patterns detected and alerted |
| Incident Mitigation | RS.MI-01 | RESPOND | Incidents contained — automated rate limiting, circuit breakers, cost budgets as containment controls |
| Risk Management Strategy | GV.RM-01 | GOVERN | Risk management strategy established — LLM availability requirements and acceptable consumption risk defined |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-01: Include LLM availability in risk management
  strategy — define acceptable consumption thresholds,
  cost budgets, and DoS risk tolerance

**PROTECT**
- PR.IR-01: Implement rate limiting and resource controls
  as resilience measures — hard token caps, per-user
  budgets, circuit breakers enforced at API gateway

**DETECT**
- DE.CM-01: Monitor LLM resource consumption in real time —
  anomalous consumption spikes detected and alerted

**RESPOND**
- RS.MI-01: Contain consumption incidents — automated rate
  tightening, session suspension, cost circuit breakers

**RECOVER**
- RC.RP-01: Recovery plan covers LLM service restoration —
  BCP includes LLM availability requirements, RTO/RPO defined

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · CIS Controls CIS 12 · NIST SP 800-82 (OT)

---

## CSF 2.0 profile for LLM security

The CSF 2.0 Organisational Profile framework allows organisations
to document current state vs target state per function. This
profile provides a starting point for LLM security programme alignment:

| CSF Function | LLM priority entries | Key categories | Target state |
|---|---|---|---|
| GOVERN | LLM03, LLM06, LLM09 | GV.SC-01, GV.OC-01, GV.RM-01/06 | Supply chain programme live, acceptable use policy published, risk register complete |
| IDENTIFY | LLM01, LLM02, LLM04 | ID.AM-08, ID.RA-01, ID.RA-08 | All LLM assets inventoried, risk assessments complete, threat intel subscriptions active |
| PROTECT | LLM01, LLM02, LLM06 | PR.DS-01/02, PR.AA-01/05, PR.PS-04 | Encryption, access controls, and secure development requirements implemented |
| DETECT | LLM04, LLM08, LLM10 | DE.CM-01/09, DE.AE-02 | Production monitoring live for all LLM systems, anomaly alerts operational |
| RESPOND | LLM01, LLM04, LLM10 | RS.AN-03, RS.MI-01/02 | Incident response procedures tested for all LLM-specific scenarios |
| RECOVER | LLM10 | RC.RP-01 | BCP covers LLM availability, RTO/RPO defined and tested |

---

## Implementation priority

| Phase | LLM entries | CSF focus | Rationale |
|---|---|---|---|
| 1 — GOVERN + IDENTIFY | LLM03, LLM06 | GV.SC-01, ID.AM-08 | Asset inventory and supply chain governance before technical controls |
| 2 — PROTECT | LLM01, LLM02, LLM05 | PR.DS, PR.AA, PR.PS-04 | Data protection and access control close the most common breach paths |
| 3 — DETECT | LLM04, LLM08, LLM10 | DE.CM-01/09 | Monitoring programme covers poisoning, vector store, and consumption risks |
| 4 — RESPOND + RECOVER | All | RS.AN, RS.MI, RC.RP | Incident response tested, BCP covers LLM availability |

---

## References

- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [NIST CSF 2.0 Quick Start Guides](https://www.nist.gov/cyberframework/getting-started)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with CSF 2.0 profile | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
