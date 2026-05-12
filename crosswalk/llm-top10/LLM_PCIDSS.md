<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : PCI DSS v4.0
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 x PCI DSS v4.0

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/)
— the Payment Card Industry Data Security Standard, version 4.0,
published March 2022 and mandatory from March 2025.

---

## Why PCI DSS for LLM security

PCI DSS applies to any organisation that stores, processes, or
transmits cardholder data (CHD) or sensitive authentication data
(SAD). If your LLM application has any of the following
characteristics, PCI DSS requirements apply to the LLM systems
and their data pipelines:

- The LLM processes customer support interactions that may include
  payment card numbers, expiry dates, or CVV codes
- The LLM has access to databases or document stores containing
  transaction records or cardholder data
- The LLM is deployed in a payment processing or fraud detection
  pipeline where CHD is in scope
- The RAG corpus for the LLM includes documentation, procedures,
  or records that contain cardholder data
- Agents built on the LLM have tool access to payment systems

PCI DSS v4.0 introduced significant updates relevant to LLM
applications — most importantly the requirement for customised
approach, which allows organisations to meet the intent of
requirements using alternative methods. For novel LLM-specific
controls that do not map cleanly to traditional PCI requirements,
the customised approach provides the mechanism to document them
as compensating controls.

**Cardholder data (CHD) in LLM scope is a critical risk.**
An LLM that has been trained on or has retrieval access to CHD
is a PCI scope expansion that assessors will flag. The controls
in this file address how to manage LLM applications in PCI scope
and how to prevent inadvertent PCI scope expansion through LLM
deployments.

---

## PCI DSS v4.0 structure

PCI DSS v4.0 is organised into 12 requirements:

| Requirement | Title | LLM relevance |
|---|---|---|
| 1 | Network security controls | LLM infrastructure network segmentation |
| 2 | Secure configurations | LLM and model component hardening |
| 3 | Protect stored account data | CHD in training data, RAG, embeddings |
| 4 | Protect cardholder data in transit | LLM API calls, RAG retrieval with CHD |
| 5 | Protect against malicious software | LLM component integrity, malware prevention |
| 6 | Develop and maintain secure systems | Secure development for LLM integrations |
| 7 | Restrict access to cardholder data | Least privilege for LLM access to CHD |
| 8 | Identify users and authenticate access | LLM service identity, authentication |
| 9 | Restrict physical access | Physical controls for LLM infrastructure |
| 10 | Log and monitor all access | LLM audit logging, monitoring |
| 11 | Test security systems | LLM security testing programme |
| 12 | Support information security policies | LLM risk management, vendor programme |

---

## PCI DSS v4.0 key new requirements for LLM

| Requirement | Change in v4.0 | LLM application |
|---|---|---|
| Req 6.2 | Bespoke and custom software security | LLM integration code requires secure development and review |
| Req 6.3 | Security vulnerabilities identified and addressed | LLM component CVEs in vulnerability management |
| Req 6.4 | Public-facing web applications protected | LLM-powered chatbots and portals in PCI scope require WAF or equivalent |
| Req 6.5 | Changes managed securely | Model updates as system changes requiring security testing |
| Req 10.7 | Failures of critical controls detected | LLM monitoring failures treated as critical control failures |
| Req 12.3 | Targeted risk analyses | LLM-specific risk analyses documented |
| Req 12.6 | Security awareness programme | AI security awareness for staff handling CHD through LLM |

---

## Quick-reference summary

| ID | Name | Severity | Primary PCI DSS v4.0 Requirements | Tier |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | Req 6.2, Req 6.4, Req 10.6, Req 11.3 | Foundational-Advanced |
| LLM02 | Sensitive Information Disclosure | High | Req 3.3, Req 3.5, Req 4.2, Req 7.2 | Foundational-Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | Req 6.3, Req 12.8, Req 2.2, Req 6.5 | Foundational-Hardening |
| LLM04 | Data and Model Poisoning | Critical | Req 6.5, Req 10.6, Req 11.3, Req 12.3 | Hardening-Advanced |
| LLM05 | Insecure Output Handling | High | Req 6.2, Req 6.4, Req 11.3, Req 10.6 | Foundational-Hardening |
| LLM06 | Excessive Agency | High | Req 7.2, Req 7.3, Req 10.2, Req 12.3 | Foundational-Hardening |
| LLM07 | System Prompt Leakage | High | Req 3.5, Req 7.2, Req 10.2, Req 6.2 | Foundational-Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | Req 3.4, Req 3.5, Req 7.2, Req 11.3 | Hardening-Advanced |
| LLM09 | Misinformation | Medium | Req 12.3, Req 6.2, Req 10.6, Req 12.6 | Foundational-Hardening |
| LLM10 | Unbounded Consumption | Medium | Req 1.3, Req 6.4, Req 10.6, Req 12.3 | Foundational-Hardening |

---

## Audience tags

- **CISO / compliance lead** — full file, PCI DSS v4.0 alignment for LLM applications
- **QSA / assessor** — requirement-to-control mapping for PCI assessment scope
- **Payment / fintech product team** — CHD scope, cardholder data handling
- **Security engineer** — Req 6, Req 10 technical control entries
- **Risk manager** — Req 12.3 targeted risk analysis entries throughout

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions manipulate LLM behaviour. In PCI scope,
prompt injection against an LLM with CHD access is a critical
finding — a successful attack could cause the model to exfiltrate
cardholder data, generate fraudulent payment instructions, or
bypass fraud detection logic.

**PCI DSS assessor expectation:** For LLM applications in PCI
scope, Requirement 6.2 (secure software development practices)
requires that injection vulnerabilities are addressed in all
bespoke software including LLM integrations. Requirement 6.4
requires that public-facing applications are protected against
known attacks — prompt injection is a known attack class for LLM
applications and assessors will test for it.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Secure software development | Req 6.2.4 | All injection vulnerabilities addressed in LLM integration code — prompt injection as a known injection class |
| Public-facing application protection | Req 6.4.1 | LLM-powered customer-facing applications protected against prompt injection — WAF or equivalent, security testing |
| Audit log review | Req 10.6.1 | Automated log analysis covering LLM injection indicators — anomalous inputs detected and reviewed |
| External and internal penetration testing | Req 11.3.1 | Penetration testing includes prompt injection scenarios for all LLM applications in PCI scope |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 6.2.4: Implement input validation for all LLM
  integrations in PCI scope — prompt injection addressed
  as a known injection vulnerability class in secure
  development standards
- Req 6.4.1: Apply web application protection to all
  public-facing LLM applications — WAF rules or equivalent
  coverage including injection detection
- Document prompt injection as a targeted risk per
  Req 12.3.2 for all LLM systems in CDE scope

**Hardening**
- Req 11.3.1: Include prompt injection in penetration
  testing scope — direct, indirect via RAG, and jailbreak
  vectors for all LLM applications in PCI scope
- Req 10.6.1: Deploy automated monitoring for injection
  indicators — log review covers LLM-specific anomalies
- Implement architectural separation between system
  prompt and user input — Req 6.2 secure design control

**Advanced**
- Req 11.3.1: Conduct adversarial testing quarterly —
  novel injection techniques tested against LLM
  applications in CDE before reaching production
- Req 12.3.2: Update targeted risk analysis when new
  injection techniques emerge — dynamic risk assessment
- Customised approach: Document injection-specific
  controls as customised approach evidence where
  standard WAF rules do not cover LLM-specific vectors

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · NIST AI RMF MS-2.5 · OWASP ASVS V5.1

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose sensitive information through outputs. In PCI scope
this is a primary cardholder data protection concern — an LLM
that reproduces PANs, expiry dates, CVVs, or cardholder names
from training data or RAG retrieval is a direct PCI DSS Requirement
3 violation.

**PCI DSS critical note:** CHD must never appear in LLM training
data (Req 3.3, 3.4), RAG document stores (Req 3.5), or model
outputs in cleartext (Req 4.2). If CHD is in LLM scope, the
entire LLM infrastructure is in the CDE (Cardholder Data
Environment) and full PCI DSS scope applies.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Protect stored account data — SAD prohibition | Req 3.3.1 | SAD (CVV, PIN) must never be in LLM training data or RAG — stored after authorisation is prohibited |
| Protect stored account data — PAN rendering | Req 3.4.1 | PANs in LLM outputs masked — only first six and last four digits displayed in any LLM response |
| Protect stored account data — encryption | Req 3.5.1 | Any PAN in LLM scope encrypted with strong cryptography — AES-256 or equivalent |
| Protect cardholder data in transit | Req 4.2.1 | All LLM API calls and RAG retrieval paths carrying CHD encrypted in transit — TLS 1.2 minimum |
| Restrict access by need to know | Req 7.2.1 | LLM access to CHD restricted to minimum required — retrieval access controls prevent over-broad PAN access |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.3.1: Audit all LLM training data and RAG corpora
  for SAD before any LLM in CDE scope is trained or
  deployed — SAD prohibition is absolute, no exceptions
- Req 3.4.1: Implement PAN masking in all LLM outputs —
  automated output redaction before responses leave
  the LLM service boundary
- Req 3.5.1: Encrypt all stored CHD in LLM scope —
  training datasets, RAG document stores, embedding
  stores, prompt caches containing CHD

**Hardening**
- Req 4.2.1: Enforce TLS 1.2 minimum on all LLM data
  flows carrying CHD — API calls, RAG retrieval,
  observability pipelines
- Req 7.2.1: Apply need-to-know access controls on
  RAG retrieval — LLM access to CHD restricted to
  minimum required by the specific use case
- Scope minimisation: Design LLM applications to
  operate outside CDE where possible — tokenisation
  before data reaches the LLM removes PCI scope

**Advanced**
- Apply differential privacy for any LLM trained on
  CHD corpora — reduces risk of PAN reproduction from
  training data memorisation
- Conduct PAN detection red team — query the LLM to
  verify PANs cannot be reconstructed from outputs
- Req 3.3.1: Verify SAD absence in all model artifacts —
  post-training audit of model outputs for SAD patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity and Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference and Data Reconstruction
- Other frameworks: ISO 27001 A.8.11 · NIST AI RMF GV-1.6 · SOC 2 C2.1

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM components sourced from third parties create supply chain
risk. PCI DSS Requirement 12.8 (third-party service providers)
applies to all vendors with access to or components that process
CHD — model weight providers and dataset vendors accessing CDE
data are TPSPs under PCI DSS.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Third-party service providers | Req 12.8.1 | List of all TPSPs maintained — LLM component vendors with CDE access or data in scope |
| TPSP agreements | Req 12.8.3 | Written agreements with LLM vendors — acknowledge responsibility for CHD security |
| TPSP PCI DSS compliance | Req 12.8.4 | Monitor TPSP PCI DSS compliance status — LLM component vendors with CHD access have compliant status verified |
| Security vulnerabilities | Req 6.3.3 | All LLM software components at latest security patches — ML libraries and inference runtime patched |
| Secure system changes | Req 6.5.1 | Model component updates follow change management — security testing before production |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.8.1: Maintain TPSP list including all LLM
  component vendors with CDE access or processing CHD —
  model providers, dataset vendors, inference platform
- Req 12.8.3: Establish written agreements with LLM
  vendors acknowledging CHD security responsibility —
  required before any CDE-adjacent LLM deployment
- Req 6.3.3: Maintain ML SBOM and patch all LLM
  components to latest security patches on schedule

**Hardening**
- Req 12.8.4: Monitor LLM vendor PCI DSS compliance —
  obtain AOC (Attestation of Compliance) from vendors
  with CHD access, track compliance status annually
- Req 6.5.1: Include model and component updates in
  PCI change management — security testing before
  any change to production LLM in CDE
- Verify cryptographic signatures of all LLM components —
  unsigned components rejected before CDE deployment

**Advanced**
- Operate isolated model evaluation before CDE deployment —
  Req 6.5 testing before change to production
- Req 12.8.2: Document roles and responsibilities for
  LLM vendor CHD security — who owns TPSP oversight,
  what escalation path exists for vendor incidents
- Customised approach: Document ML SBOM and component
  verification as a customised Req 12.8 monitoring control

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model and Artifact Poisoning
- Other frameworks: ISO 27001 A.5.19/A.5.21 · NIST AI RMF MP-5.1 · NIST SP 800-218A

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Training data or model weights corrupted with backdoors. In PCI
scope, a poisoned model in a fraud detection or payment processing
pipeline could be triggered to systematically approve fraudulent
transactions or suppress fraud alerts. Req 6.5 (change management)
and Req 11.3 (penetration testing) are the primary requirements.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Secure system changes | Req 6.5.6 | All model promotions tested for unexpected functionality before CDE deployment — poisoning as unexpected functionality |
| Audit log review | Req 10.6.1 | Automated monitoring of LLM outputs in CDE — poisoning indicators (systematic anomalous recommendations) detected |
| Penetration testing | Req 11.3.1 | Poisoning detection included in penetration testing programme for LLM applications in CDE |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for training pipeline security — documented controls and frequency of review |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 6.5.6: Test all model promotions for unexpected
  functionality — model integrity verification and output
  distribution analysis before CDE deployment
- Document training data governance — source allowlisting,
  provenance, anomaly detection as Req 6.2 secure
  development practices
- Establish model rollback capability — Req 6.5 change
  reversal requirement met by clean checkpoint procedure

**Hardening**
- Req 10.6.1: Deploy automated monitoring of LLM outputs
  in CDE — poisoning indicators (systematic anomalous
  fraud scores, recommendation patterns) detected
- Req 11.3.1: Include poisoning detection in penetration
  testing — backdoor trigger testing for CDE LLM models
- Req 12.3.2: Document targeted risk analysis for training
  pipeline — threat actors, attack vectors, controls,
  review frequency

**Advanced**
- Post-training backdoor detection as mandatory CDE
  deployment gate — Req 6.5 testing before production
- Req 10.6.1: Integrate model output anomaly detection
  into PCI-scope SIEM — poisoning events treated as
  security incidents per Req 12.10
- Conduct training pipeline adversarial testing —
  Req 11.3 penetration testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory and Context Poisoning
- DSGAI 2026: DSGAI04 Data Model and Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032 · ISO 27001 A.8.27

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
injection attacks. In PCI scope, output injection into payment
processing logic could enable fraudulent transaction generation or
CHD exfiltration. Req 6.2 (secure development) and Req 6.4
(public-facing application protection) apply.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Bespoke and custom software | Req 6.2.4 | Output handling in LLM integrations addresses all injection vulnerability classes — LLM output treated as untrusted |
| Public-facing web application protection | Req 6.4.1 | All interfaces consuming LLM output in PCI scope protected — input validation on all downstream consumers |
| Penetration testing | Req 11.3.1 | Output injection scenarios in penetration testing — SQL injection, command injection via LLM output |
| Audit log review | Req 10.6.1 | Monitoring for injection patterns in LLM output channels within CDE |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 6.2.4: Implement output validation as a secure
  development requirement — LLM output treated as
  untrusted input to all downstream CDE systems
- Req 6.4.1: Apply application protection to all
  interfaces consuming LLM output in PCI scope —
  WAF or equivalent, schema validation
- Never pass raw LLM output to payment processing
  logic — Req 6.2 secure design requirement

**Hardening**
- Req 11.3.1: Include output injection in penetration
  testing scope — SQL injection, command injection
  via LLM output, results documented
- Req 10.6.1: Monitor LLM output channels for injection
  patterns — automated log analysis covering CDE-facing
  output paths
- Conduct DAST on all CDE interfaces consuming LLM output

**Advanced**
- Deploy dedicated output security layer — Req 6.2
  defence-in-depth evidence
- Req 11.3.1: Adversarial output testing against
  specific payment logic consumers — document as
  CDE penetration testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity and Validation Failures
- Other frameworks: OWASP ASVS V5 · CIS Controls CIS 16 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with excessive autonomy execute unintended actions. In PCI
scope, excessive agency against payment systems — an agent that
can initiate refunds, modify transaction records, or query
cardholder tables autonomously — is a critical access control
failure under Req 7 and Req 8.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Restrict access to system components | Req 7.2.1 | LLM tool access to CDE systems restricted to minimum required — read-only by default, write access formally approved |
| Access control system | Req 7.3.1 | Access control system enforces LLM tool scope — agent cannot exceed defined CDE access without explicit authorisation |
| Logging and monitoring | Req 10.2.1 | All LLM tool invocations in CDE logged — tool identity, parameters, invoking user identity, timestamp |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for LLM autonomous action scope in CDE — blast radius documented and accepted |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Restrict LLM tool access to minimum required
  CDE access — read-only for analytics and advisory
  functions, write access requires formal approval and
  documented business justification
- Req 7.3.1: Enforce LLM tool scope through access
  control system — agent cannot self-escalate beyond
  defined CDE permission scope
- Require human confirmation for all LLM-initiated
  financial operations — Req 7 need-to-know requirement

**Hardening**
- Req 10.2.1: Log all LLM tool invocations in CDE —
  tool identity, parameters, user identity, timestamp —
  immutable, meets Req 10 logging requirements
- Req 12.3.2: Document targeted risk analysis for LLM
  autonomous actions — CDE systems accessible, operations
  possible, blast radius, controls implemented
- Conduct quarterly access reviews for LLM tool
  permissions — Req 7 periodic review requirement

**Advanced**
- Formally specify permitted LLM action scope for each
  CDE deployment — Req 7 documented least privilege
- Req 11.3.1: Test excessive agency via injection in
  penetration testing — results documented as CDE
  security testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin and Agent Data Exchange
- Other frameworks: EU AI Act Art. 14 · ISO 42001 A.6.1.2 · AIUC-1 B006

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing security controls and internal logic
are extracted. In PCI scope, system prompts may contain CDE
topology, authentication logic, or processing rules that must
be protected as sensitive configuration data under Req 3 and Req 7.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Protection of sensitive authentication data | Req 3.5.1 | System prompts containing CDE configuration treated as sensitive — encrypted at rest, access-controlled |
| Restrict access by need to know | Req 7.2.1 | System prompt access restricted — only authorised personnel with documented business need |
| Logging and monitoring | Req 10.2.1 | All access to system prompt storage logged — access to CDE configuration data requires audit trail |
| Bespoke software security | Req 6.2.4 | System prompt design prevents leakage — no cleartext CDE identifiers, tokens resolved at runtime |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.5.1: Classify system prompts containing CDE
  references as sensitive configuration — encrypted at
  rest, access-controlled, version-controlled
- Req 7.2.1: Restrict system prompt access to authorised
  personnel with documented business need — access
  control configuration as Req 7 evidence
- Remove all CHD, CDE topology, and authentication
  details from system prompts — use runtime token
  resolution per Req 6.2

**Hardening**
- Req 10.2.1: Log all access to system prompt storage —
  access to CDE configuration data auditable per Req 10
- Conduct prompt extraction testing — Req 11.3
  security testing evidence
- Req 6.2.4: Implement system prompt tokenisation —
  CDE identifiers replaced with opaque tokens

**Advanced**
- Req 11.3.1: Include prompt extraction in penetration
  testing scope — CDE system prompt recovery tested
- Deploy output classifier to block system prompt
  content in responses — Req 6.4 application protection

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · CWE-200 · ISO 27001 A.5.12

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Vector stores containing embeddings of CHD-adjacent documentation
represent secondary attack surfaces that may be outside traditional
PCI scope assessments but within CDE data exposure risk.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Protect stored account data | Req 3.4.1 | Embeddings derived from CHD-containing documents encrypted — PAN cannot be reconstructed from cleartext embeddings |
| Protect stored account data — SAD | Req 3.5.1 | Vector stores in CDE scope encrypted with strong cryptography |
| Restrict access | Req 7.2.1 | RBAC on all vector stores in CDE scope — no unauthenticated access |
| Penetration testing | Req 11.3.1 | Vector store attacks in CDE penetration testing — RBAC bypass, bulk extraction, embedding inversion |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.4.1: Ensure embeddings derived from CHD-containing
  documents cannot reproduce PANs — PAN masking before
  embedding generation prevents scope contamination
- Req 7.2.1: Enable RBAC on all vector stores in
  PCI scope — no unauthenticated access in any environment
- Req 3.5.1: Encrypt all vector stores in CDE scope —
  encryption at rest required

**Hardening**
- Scope design: Apply PAN tokenisation before embedding
  generation — removes CHD from embedding scope, reducing
  PCI scope of vector infrastructure
- Req 11.3.1: Include embedding inversion in penetration
  testing — validate CHD cannot be reconstructed, results
  documented as CDE testing evidence
- Patch all vector database CVEs — Req 6.3 vulnerability
  management requirement

**Advanced**
- Apply differential privacy to embeddings of CHD-adjacent
  content — Req 3 advanced data protection measure
- Req 11.3.1: Conduct RBAC bypass testing for all vector
  stores in PCI scope — document as CDE testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- Agentic Top 10: ASI06 Memory and Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference and Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · ISO 27001 A.8.3/A.8.24 · SOC 2 C2.1

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate incorrect content. In PCI scope, misinformation from
an LLM providing payment security guidance, chargeback advice, or
fraud detection recommendations could cause incorrect processing
or compliance errors. Req 12.3 targeted risk analysis governs
the acceptable risk tolerance for LLM advisory outputs in
payment contexts.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for LLM advisory outputs in payment context — what decisions are influenced, what is the consequence of incorrect output |
| Bespoke software security | Req 6.2 | LLM integration code specifies accuracy requirements — high-stakes payment outputs require verification before action |
| Audit log review | Req 10.6.1 | Monitoring for LLM accuracy degradation — output quality metrics reviewed |
| Security awareness programme | Req 12.6.1 | PCI staff trained on LLM output limitations — advisory status of AI recommendations communicated |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.3.2: Document targeted risk analysis for LLM
  advisory outputs in payment context — what payment
  decisions are influenced by LLM, acceptable accuracy
  threshold, human verification requirements
- Req 12.6.1: Include LLM output limitations in PCI
  security awareness programme — staff handling CHD
  through LLM trained on advisory status
- Human verification for all LLM-influenced payment
  decisions — Req 12.3 risk acceptance control

**Hardening**
- Req 10.6.1: Implement production accuracy monitoring —
  LLM output quality reviewed as part of CDE log
  analysis programme
- Deploy RAG grounded on authoritative, PCI-approved
  sources — Req 6.2 secure design for payment advisory
- Req 12.3.2: Review and update targeted risk analysis
  when LLM model is updated — accuracy characteristics
  may change post fine-tuning

**Advanced**
- Conduct domain-specific accuracy testing before CDE
  deployment — Req 6.5 testing before production change
- Req 11.3.1: Include misinformation scenarios in
  penetration testing for payment advisory LLM — document
  as CDE testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation and Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 F · NIST CSF 2.0 GV.OC-01

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption.
In PCI scope, availability of payment processing systems is a
direct compliance requirement — resource exhaustion attacks
against LLM applications in CDE are covered under Req 1
(network security) and Req 6.4 (application protection).

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Network security controls | Req 1.3.2 | Network controls restrict inbound traffic to CDE — rate limiting at network layer for LLM applications |
| Public-facing application protection | Req 6.4.1 | LLM-powered public-facing applications protected against DoS — rate limiting and payload limits enforced |
| Audit log review | Req 10.6.1 | Automated monitoring for resource exhaustion patterns — unusual consumption volumes alerted |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for LLM availability in CDE — DoS impact on payment processing, controls documented |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 1.3.2: Implement network-layer rate limiting for
  CDE-facing LLM applications — traffic controls at the
  network boundary as Req 1 network security control
- Req 6.4.1: Enforce rate limiting and payload limits
  on all public-facing LLM applications in PCI scope —
  application protection against resource exhaustion
- Req 12.3.2: Document targeted risk analysis for LLM
  availability — DoS impact on payment processing,
  RTO/RPO, controls documented and accepted

**Hardening**
- Req 10.6.1: Implement consumption anomaly monitoring —
  automated detection of unusual resource utilisation
  patterns in CDE LLM applications
- Define BCP for LLM service failures affecting payment
  processing — Req 12 business continuity requirement
- Per-user token limits and cost budgets — Req 6.4
  application protection control

**Advanced**
- Deploy sponge example detection — Req 6.4 advanced
  application protection for CDE
- Req 11.3.1: Conduct adversarial load testing against
  CDE LLM applications — verify rate limiting holds,
  document as penetration testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability and Resilience Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · CIS Controls CIS 12 · NIST CSF 2.0 PR.IR-01

---

## PCI DSS v4.0 compliance checklist for LLM applications

### Scope determination (before anything else)

- [ ] Determine whether LLM application is in CDE scope
- [ ] Confirm no CHD in LLM training data (Req 3.3)
- [ ] Confirm no SAD in any LLM data store (Req 3.3.1)
- [ ] Map all data flows from LLM to CDE systems
- [ ] Assess whether LLM infrastructure requires PCI segmentation

### Data protection (Req 3, Req 4)

- [ ] PANs in LLM scope encrypted with strong cryptography (Req 3.5.1)
- [ ] PAN masking in all LLM outputs (Req 3.4.1)
- [ ] SAD never stored in any LLM component (Req 3.3.1)
- [ ] All CHD data flows encrypted in transit TLS 1.2 minimum (Req 4.2.1)
- [ ] Embeddings of CHD-adjacent content cannot reproduce PANs (Req 3.4.1)

### Secure development (Req 6)

- [ ] LLM integration code addresses prompt injection as injection class (Req 6.2.4)
- [ ] Public-facing LLM applications protected — WAF or equivalent (Req 6.4.1)
- [ ] Model updates through change management with security testing (Req 6.5)
- [ ] Output validation for all LLM outputs in CDE (Req 6.2.4)
- [ ] System prompts contain no CHD or CDE identifiers (Req 6.2.4)

### Access control (Req 7, Req 8)

- [ ] LLM access to CDE systems restricted to minimum required (Req 7.2.1)
- [ ] LLM tool access managed as need-to-know (Req 7.2.1)
- [ ] Quarterly access reviews for LLM CDE permissions (Req 7)
- [ ] LLM service accounts use unique identities (Req 8)
- [ ] RBAC on all vector stores in CDE scope (Req 7.2.1)

### Logging and monitoring (Req 10)

- [ ] All LLM access to CDE logged with user identity (Req 10.2.1)
- [ ] All LLM tool invocations in CDE logged (Req 10.2.1)
- [ ] Automated log analysis covers LLM-specific anomalies (Req 10.6.1)
- [ ] System prompt access logged (Req 10.2.1)

### Testing (Req 11)

- [ ] Prompt injection in penetration testing scope (Req 11.3.1)
- [ ] Output injection in penetration testing scope (Req 11.3.1)
- [ ] Excessive agency tested for CDE-facing agents (Req 11.3.1)
- [ ] Vector store attacks in penetration testing (Req 11.3.1)

### Vendor and policy (Req 12)

- [ ] LLM component vendors with CDE access in TPSP list (Req 12.8.1)
- [ ] Written agreements with LLM vendors (Req 12.8.3)
- [ ] TPSP compliance status monitored for LLM vendors (Req 12.8.4)
- [ ] Targeted risk analyses for all LLM-specific risks (Req 12.3.2)
- [ ] Security awareness programme covers LLM limitations (Req 12.6.1)

---

## Implementation priority

| Phase | LLM entries | PCI DSS requirements | Rationale |
|---|---|---|---|
| 1 — Scope first | LLM02 | Req 3, Req 4 | CHD scope determination and data protection are the foundation — everything else depends on this |
| 2 — Access and logging | LLM06, LLM07 | Req 7, Req 10 | Access control and audit logging are core PCI requirements |
| 3 — Secure development | LLM01, LLM05 | Req 6.2, Req 6.4 | Injection and output security as secure development requirements |
| 4 — Vendor and testing | LLM03, LLM04 | Req 12.8, Req 11.3 | TPSP programme and penetration testing programme |
| 5 — Ongoing | LLM08-LLM10 | Req 12.3, Req 6.5 | Risk analysis, embedding scope, availability |

---

## References

- PCI DSS v4.0: https://www.pcisecuritystandards.org/document_library/
- PCI SSC Information Supplements: https://www.pcisecuritystandards.org/document_library/#results
- PCI DSS v4.0 Summary of Changes: https://www.pcisecuritystandards.org/documents/PCI-DSS-v4-0-Summary-of-Changes-r2.pdf
- OWASP LLM Top 10 2025: https://genai.owasp.org/llm-top-10/

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-25 | 2026-Q1 | Initial mapping — LLM01-LLM10 full entries with PCI DSS v4.0 compliance checklist | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
