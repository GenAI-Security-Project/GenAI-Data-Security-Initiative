<!--
  GenAI Security Crosswalk
  Source list : OWASP GenAI Data Security Risks and Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : PCI DSS v4.0
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 x PCI DSS v4.0

Mapping the [OWASP GenAI Data Security Risks and Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01-DSGAI21) to [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/).

The DSGAI taxonomy follows data through a GenAI system lifecycle.
PCI DSS follows cardholder data through storage, processing, and
transmission. For organisations in the payments ecosystem deploying
GenAI — LLM-powered customer service, AI fraud detection, automated
chargeback processing, intelligent payment routing — every DSGAI
data security risk has a PCI DSS implication when CHD is in the
data pipeline.

**The most important PCI DSS principle for GenAI data security:**
Scope minimisation. The safest GenAI deployment from a PCI perspective
is one where CHD never enters the LLM context, training data, RAG
corpus, or embedding store. Design for CHD absence first. Where
CHD is unavoidable, apply PCI scope controls to every component
that touches it.

---

## Quick-reference summary

| ID | Name | Severity | Primary PCI DSS v4.0 Requirements | Tier |
|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | Req 3.4, Req 3.5, Req 4.2, Req 7.2 | Foundational-Advanced |
| DSGAI02 | Agent Identity and Credential Exposure | Critical | Req 7.2, Req 8.2, Req 10.2, Req 12.3 | Foundational-Advanced |
| DSGAI03 | Shadow AI and Unsanctioned Data Flows | High | Req 12.8, Req 12.5, Req 1.3, Req 12.6 | Foundational-Hardening |
| DSGAI04 | Data, Model and Artifact Poisoning | Critical | Req 6.5, Req 10.6, Req 11.3, Req 12.8 | Hardening-Advanced |
| DSGAI05 | Data Integrity and Validation Failures | High | Req 6.2, Req 6.3, Req 11.3, Req 6.5 | Foundational-Hardening |
| DSGAI06 | Tool, Plugin and Agent Data Exchange | High | Req 12.8, Req 7.2, Req 10.2, Req 3.5 | Foundational-Hardening |
| DSGAI07 | Data Governance, Lifecycle and Classification | High | Req 3.1, Req 3.2, Req 9.4, Req 12.3 | Foundational-Advanced |
| DSGAI08 | Non-Compliance and Regulatory Violations | High | Req 12.1, Req 12.3, Req 12.4, Req 12.6 | Foundational-Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | Req 3.4, Req 3.5, Req 4.2, Req 10.2 | Hardening-Advanced |
| DSGAI10 | Synthetic Data and Anonymisation Pitfalls | Medium | Req 3.1, Req 12.3, Req 3.3, Req 3.4 | Hardening-Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | Req 7.2, Req 3.5, Req 10.2, Req 11.3 | Foundational-Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | Req 7.2, Req 6.2, Req 6.4, Req 10.2 | Foundational-Advanced |
| DSGAI13 | Vector Store Platform Security | High | Req 3.5, Req 7.2, Req 6.3, Req 11.3 | Foundational-Hardening |
| DSGAI14 | Excessive Telemetry and Monitoring Leakage | High | Req 3.5, Req 7.2, Req 10.2, Req 12.3 | Foundational-Hardening |
| DSGAI15 | Over-Broad Context Windows | High | Req 7.2, Req 3.4, Req 12.3, Req 10.2 | Foundational-Hardening |
| DSGAI16 | Endpoint and Browser Assistant Overreach | High | Req 12.8, Req 6.3, Req 10.2, Req 12.3 | Foundational-Hardening |
| DSGAI17 | Data Availability and Resilience Failures | High | Req 12.3, Req 1.3, Req 10.6, Req 12.10 | Foundational-Advanced |
| DSGAI18 | Inference and Data Reconstruction | High | Req 3.4, Req 3.5, Req 11.3, Req 12.3 | Hardening-Advanced |
| DSGAI19 | Human-in-Loop and Labeler Overexposure | Medium | Req 12.8, Req 7.2, Req 3.3, Req 12.6 | Foundational-Hardening |
| DSGAI20 | Model Exfiltration and IP Replication | High | Req 7.2, Req 10.6, Req 12.3, Req 6.4 | Hardening-Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | Req 6.5, Req 12.8, Req 10.6, Req 11.3 | Hardening-Advanced |

---

## Audience tags

- **CISO / compliance lead** — full file, PCI DSS v4.0 alignment for GenAI data programme
- **QSA / assessor** — requirement-to-control mapping for GenAI in PCI scope
- **Payment / fintech engineering** — CHD data flow controls throughout
- **Data governance lead** — DSGAI07, DSGAI08, DSGAI10 entries
- **Security engineer** — Req 6, Req 7, Req 10 technical control entries

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data — including PANs and cardholder information — leaks
through GenAI outputs, RAG retrieval, embedding exposure, or
observability pipelines. In PCI scope, PAN exposure through any
of these channels is a Requirement 3 violation.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| PAN rendering unreadable | Req 3.4.1 | PANs in GenAI outputs masked — only first six/last four digits in any response |
| Protect stored account data | Req 3.5.1 | All CHD in GenAI scope encrypted — training data, RAG stores, embeddings, prompt caches |
| Encryption in transit | Req 4.2.1 | All GenAI data flows carrying CHD encrypted — TLS 1.2 minimum |
| Restrict access | Req 7.2.1 | RAG retrieval access controls — users retrieve only CHD they are authorised to access |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.4.1: Implement PAN masking in all GenAI outputs —
  automated output redaction before responses leave the
  service boundary, no cleartext PANs in any output
- Req 3.5.1: Encrypt all CHD in GenAI scope at rest —
  training datasets, RAG document stores, embedding stores,
  prompt caches, observability logs containing CHD
- Scope design: Apply PAN tokenisation before data enters
  GenAI pipeline — removes CHD from scope and eliminates
  the majority of Req 3 obligations

**Hardening**
- Req 4.2.1: Enforce TLS 1.2 minimum on all GenAI data
  flows carrying CHD — API calls, RAG retrieval pipelines,
  observability streams
- Req 7.2.1: Apply need-to-know access controls on RAG
  retrieval — users cannot retrieve CHD beyond their
  authorised scope through GenAI queries
- Deploy DLP monitoring on all GenAI output channels —
  PAN detection before responses reach users

**Advanced**
- Apply differential privacy for GenAI trained on CHD —
  Req 3 advanced data protection measure
- Conduct PAN reconstruction red team — verify PANs cannot
  be recovered from GenAI outputs or embeddings
- Req 10.2.1: Log all GenAI access to CHD — full audit
  trail of every PAN access through GenAI pipeline

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity and Privilege Abuse
- Other frameworks: ISO 27001 A.8.11 · SOC 2 C2.1 · EU AI Act Art. 10

---

### DSGAI02 — Agent Identity and Credential Exposure

**Severity:** Critical

AI agents inherit and cache credentials — in PCI scope, agent
credentials may include CDE system access tokens, payment API keys,
or cardholder database credentials. Compromised agent credentials
in PCI scope are a Req 7 and Req 8 finding.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Restrict access by need to know | Req 7.2.1 | Agent credentials scoped to minimum CDE access — least privilege, quarterly review |
| Unique IDs for access | Req 8.2.1 | Each agent has a unique service identity — no shared credentials across CDE-facing agents |
| Logging of all access | Req 10.2.1 | All agent credential operations in CDE logged — issuance, use, anomalous patterns |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for agent credential scope in CDE — blast radius if credentials compromised |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Scope all agent CDE credentials to minimum
  required access — read-only for analytics, write access
  requires formal approval and documented business need
- Req 8.2.1: Issue unique service identity per CDE-facing
  agent — no shared credentials, all agent actions in CDE
  attributable to specific agent identity
- Short-lived credentials per task — issue at session
  start, revoke at session end, meeting Req 8 authentication
  requirements

**Hardening**
- Req 10.2.1: Log all agent credential operations in CDE —
  issuance, use, expiry — full Req 10 audit trail
- Req 12.3.2: Document targeted risk analysis for agent
  credential scope — CDE systems accessible, blast radius,
  detection controls
- Implement JIT credential issuance — Req 7/Req 8
  least-privilege access control evidence

**Advanced**
- PKI-backed agent identities for CDE access —
  Req 8 strong authentication evidence
- Req 10.6.1: Credential anomaly detection integrated
  into CDE log analysis — suspicious agent credential
  usage triggers Req 12.10 incident response

#### Cross-references
- Agentic Top 10: ASI03 Identity and Privilege Abuse
- Other frameworks: OWASP NHI Top 10 · ISO 27001 A.8.2/A.5.16 · SOC 2 CC6.1

---

### DSGAI03 — Shadow AI and Unsanctioned Data Flows

**Severity:** High

Employees paste CHD into unapproved AI tools — creating ungoverned
data flows that expand PCI scope to vendors that are not in the
TPSP programme and have no CHD security obligations.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Third-party service providers | Req 12.8.1 | Shadow AI tools processing CHD are unapproved TPSPs — not in TPSP list, no written agreements |
| TPSP oversight | Req 12.5.2 | Shadow AI discovery as part of TPSP monitoring — identify unapproved vendors receiving CHD |
| Network security | Req 1.3.2 | Network controls prevent CHD flows to unapproved AI endpoints — block at network layer |
| Security awareness | Req 12.6.1 | PCI security awareness programme covers shadow AI risk — staff trained on prohibition |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.6.1: Include shadow AI in PCI security awareness
  programme — staff explicitly trained that CHD must
  never be pasted into unapproved AI tools, consequences
  documented
- Req 1.3.2: Implement network controls blocking CHD
  flows to unapproved AI endpoints — DLP at network
  boundary for known public AI SaaS destinations
- Req 12.8.1: Assess all approved AI tools as TPSPs —
  written agreements, CHD handling obligations, periodic
  compliance review

**Hardening**
- Req 12.5.2: Include shadow AI in TPSP monitoring —
  discovery of CHD flows to unapproved AI services
  triggers Req 12.10 incident response
- Deploy DLP on all egress paths — CHD patterns detected
  before reaching unapproved AI endpoints
- Req 12.8.3: Establish written agreements with all
  approved AI tools confirming CHD security obligations

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.10 · NIST CSF 2.0 GV.RM-06 · SOC 2 CC9.1

---

### DSGAI04 — Data, Model and Artifact Poisoning

**Severity:** Critical

Training data or model weights corrupted. In PCI scope, a poisoned
GenAI model in a fraud detection or payment authorisation pipeline
can systematically approve fraudulent transactions or suppress
legitimate fraud alerts — a potentially catastrophic payment
security failure.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Secure system changes | Req 6.5.6 | All model promotions tested for unexpected functionality — poisoning detection as Req 6.5 testing requirement |
| Audit log review | Req 10.6.1 | Automated monitoring of GenAI outputs in CDE — systematic anomalies indicating poisoning detected |
| Penetration testing | Req 11.3.1 | Poisoning detection in CDE penetration testing programme |
| TPSP programme | Req 12.8 | Training data providers as TPSPs — data quality and integrity requirements in vendor agreements |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 6.5.6: Test all model promotions for unexpected
  functionality before CDE deployment — integrity
  verification and output distribution analysis required
- Document training data governance as Req 6.2 secure
  development practice — source allowlisting, provenance,
  anomaly detection
- Model rollback capability — Req 6.5 change reversal
  requirement, clean checkpoint always available

**Hardening**
- Req 10.6.1: Automated monitoring of GenAI outputs in
  fraud detection pipelines — systematic anomalous scores
  or approval patterns alerted as potential poisoning
- Req 11.3.1: Include poisoning detection in CDE
  penetration testing — backdoor trigger testing for
  payment-relevant GenAI models
- Req 12.8: Include training data providers in TPSP
  programme — written agreements with data quality and
  integrity obligations

**Advanced**
- Post-training backdoor detection as mandatory CDE
  deployment gate — Req 6.5 testing before production
- Req 10.6.1: Integrate model anomaly detection into
  PCI-scope SIEM — poisoning events trigger Req 12.10
  incident response
- Customised approach: Document poisoning detection
  programme as customised Req 11.3 testing control

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data and Model Poisoning
- Agentic Top 10: ASI06 Memory and Context Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032 · ISO 27001 A.8.27

---

### DSGAI05 — Data Integrity and Validation Failures

**Severity:** High

Adversarially crafted payloads corrupt GenAI data pipelines. In PCI
scope, path traversal in vector database snapshot imports could
achieve arbitrary file write on CDE hosts — a critical finding.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Bespoke software — injection | Req 6.2.4 | All injection vulnerability classes addressed in GenAI ingestion code — schema bypass and path traversal |
| Vulnerability management | Req 6.3.3 | All GenAI software components patched — CVE-2024-3584 class treated as urgent for CDE scope |
| Penetration testing | Req 11.3.1 | Path traversal and ingestion injection in CDE penetration testing scope |
| Secure system changes | Req 6.5 | Changes to GenAI ingestion pipelines tested — schema validation changes require security review |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 6.3.3: Patch CVE-2024-3584 and equivalent vector
  database vulnerabilities immediately — arbitrary file
  write on CDE hosts is a critical Req 6.3 finding
- Req 6.2.4: Implement multi-stage validation at all
  GenAI ingestion boundaries — path traversal prevention
  mandatory for any ingestion interface in CDE scope
- Harden snapshot import endpoints — disable or restrict
  by default in CDE environments

**Hardening**
- Req 11.3.1: Include path traversal and schema bypass
  in CDE penetration testing — ingestion interfaces
  in PCI scope tested before each deployment
- Sandbox all snapshot import operations — no direct
  write to CDE filesystem paths
- Req 6.5: Include ingestion security changes in PCI
  change management — security testing before production

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-20 · OWASP ASVS V5

---

### DSGAI06 — Tool, Plugin and Agent Data Exchange Risks

**Severity:** High

AI tools and MCP servers receive full context payloads that may
include CHD. In PCI scope, any tool provider receiving CHD through
agent context is a TPSP requiring PCI DSS Req 12.8 treatment.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| TPSP list | Req 12.8.1 | All tool and plugin providers receiving CHD in TPSP list — even if access is indirect through agent context |
| TPSP agreements | Req 12.8.3 | Written agreements with tool providers acknowledging CHD security responsibility |
| Restrict access | Req 7.2.1 | Context minimisation — tools receive minimum CHD-containing context required |
| Logging | Req 10.2.1 | All tool call payloads containing CHD logged — Req 10 audit trail requirement |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.8.1: Identify all tool and plugin providers
  that may receive CHD through agent context — add to
  TPSP list, initiate Req 12.8 compliance process
- Req 7.2.1: Implement context minimisation — tools
  receive only minimum CHD-containing context required
  for their stated function
- PAN tokenisation before context assembly — removes
  CHD from tool call scope, eliminates Req 12.8 obligation
  for most tool providers

**Hardening**
- Req 12.8.3: Establish written agreements with tool
  providers acknowledging CHD security responsibility —
  required for any tool provider that may receive CHD
- Req 12.8.4: Monitor tool provider PCI DSS compliance —
  obtain AOC from tool providers with CHD access
- Deploy DLP on all tool API calls — CHD patterns
  detected before leaving CDE boundary

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · SOC 2 CC9.1

---

### DSGAI07 — Data Governance, Lifecycle and Classification

**Severity:** High

GenAI creates ungoverned derived data assets outside traditional
PCI scope assessments. Embeddings, caches, and agent memory derived
from CHD-containing data may be CHD in scope that is not visible
to assessors without explicit data governance documentation.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Account data inventory | Req 3.1.1 | All CHD locations documented — derived GenAI assets (embeddings, caches) included in data inventory |
| Data flow documentation | Req 3.2.1 | Data flow diagrams include all GenAI pipeline paths — source through embedding, retrieval, generation, logging |
| Media disposal | Req 9.4.6 | Derived GenAI assets containing CHD disposed of securely — deletion verified per Req 9.4 requirements |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for ungoverned GenAI-derived assets — scope, protection, lifecycle documented |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.1.1: Extend CHD data inventory to all GenAI-derived
  assets — embeddings, RAG caches, agent memory, prompt
  caches, and observability logs that may contain CHD
- Req 3.2.1: Update data flow diagrams to include GenAI
  pipeline paths — source through all derived forms,
  provided to assessors as Req 3.2 documentation
- Scope design: Tokenise CHD before any GenAI pipeline —
  prevents derived assets from inheriting PCI scope

**Hardening**
- Req 9.4.6: Implement verified deletion for all GenAI-
  derived assets containing CHD — deletion logs as
  Req 9.4 media disposal evidence
- Req 12.3.2: Document targeted risk analysis for
  GenAI-derived asset governance — lifecycle, protection,
  deletion, assessor documentation
- Implement classification propagation — CHD labels flow
  from source through all derived assets automatically

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · EU AI Act Art. 10 · SOC 2 C1.1

---

### DSGAI08 — Non-Compliance and Regulatory Violations

**Severity:** High

GenAI systems trigger PCI DSS obligations without the organisation
recognising they are in scope. PCI DSS non-compliance from
undisclosed GenAI processing of CHD is a material finding that
can result in fines, card brand penalties, and loss of payment
processing rights.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Security policy | Req 12.1.1 | PCI security policy covers GenAI processing of CHD — updated to reflect AI system deployments |
| Annual assessment | Req 12.3.1 | Annual targeted risk analysis covers all GenAI systems that may process CHD |
| Programme oversight | Req 12.4.1 | Executive accountability for GenAI PCI compliance — CISO or equivalent with oversight documented |
| Security awareness | Req 12.6.1 | Security awareness covers PCI obligations in GenAI context — staff understand scope implications |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.1.1: Update PCI security policy to explicitly
  cover GenAI systems — address CHD in LLM scope,
  acceptable use of AI tools with CHD, TPSP requirements
  for AI vendors
- Req 12.3.1: Include all GenAI systems that may process
  CHD in annual targeted risk analysis — scope creep risk
  from new deployments explicitly addressed
- Conduct PCI scope assessment for every new GenAI
  deployment before production — assessor-ready
  documentation from day one

**Hardening**
- Req 12.4.1: Assign executive accountability for GenAI
  PCI compliance — CISO or equivalent with programme
  oversight, documented and evidenced for assessors
- Req 12.6.1: Include PCI GenAI scope obligations in
  security awareness — engineers and product teams
  understand when GenAI deployments trigger PCI scope
- Proactive QSA consultation for novel GenAI deployments —
  customised approach documentation where needed

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27001 A.5.31 · SOC 2 P1.1

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Multimodal GenAI processes payment documents, cheques, and card
images — OCR pipelines extract PANs that may not be treated as
CHD requiring Req 3 protection.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| PAN rendering | Req 3.4.1 | PANs extracted from multimodal content masked in all outputs — OCR-extracted PANs are CHD requiring Req 3 treatment |
| Protect stored CHD | Req 3.5.1 | All CHD extracted from multimodal inputs encrypted at rest — OCR output of a payment document is CHD |
| Encryption in transit | Req 4.2.1 | Multimodal extraction pipelines encrypted in transit where CHD is in scope |
| Logging | Req 10.2.1 | All PAN access through multimodal pipelines logged |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.4.1: Implement PAN masking for all PANs extracted
  from multimodal inputs — OCR output of payment documents
  treated as CHD, masked before any downstream use
- Req 3.5.1: Encrypt all CHD extracted from multimodal
  sources at rest — OCR output files, transcription results
  containing PANs require Req 3 encryption
- Scope design: Apply PAN tokenisation immediately on
  OCR extraction — removes CHD from downstream scope

**Hardening**
- Req 4.2.1: Enforce TLS on multimodal extraction pipelines
  where CHD is in scope — OCR results encrypted in transit
- Req 10.2.1: Log all PAN access through multimodal pipelines —
  Req 10 audit trail requirement applies to derived CHD

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 9 · SOC 2 C2.1

---

### DSGAI10 — Synthetic Data and Anonymisation Pitfalls

**Severity:** Medium

Synthetic payment data that fails to meet anonymisation standards
retains PCI scope. PCI DSS Req 3 applies to any data that can
be used to reconstruct PANs regardless of whether it is labelled
as synthetic.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Account data inventory | Req 3.1.1 | Synthetic payment datasets that may be re-identifiable included in CHD inventory |
| SAD prohibition | Req 3.3.1 | Synthetic data generated from SAD retains SAD classification — generation does not remove the prohibition |
| PAN rendering | Req 3.4.1 | Synthetic PANs that pass Luhn check treated as CHD — format-preserving synthetic PANs are in PCI scope |
| Targeted risk analysis | Req 12.3.2 | Re-identification risk in synthetic payment datasets documented in targeted risk analysis |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.1.1: Include synthetic payment datasets in CHD
  inventory until re-identification risk is formally
  assessed and accepted — do not assume synthetic data
  is out of PCI scope
- Req 3.4.1: Treat format-preserving synthetic PANs as
  CHD — Luhn-valid synthetic card numbers require Req 3
  protection regardless of synthetic origin
- Conduct formal PCI scope assessment of all synthetic
  payment data before use or distribution

**Hardening**
- Apply tokenisation rather than synthesis for CHD in
  test environments — format-preserving tokenisation
  removes PCI scope more reliably than synthesis
- Req 12.3.2: Document targeted risk analysis for
  synthetic payment data — re-identification risk,
  format-preservation properties, protection controls

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference and Data Reconstruction
- Other frameworks: ISO 27001 A.5.34 · GDPR Recital 26 · SOC 2 P4.2

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Multi-user GenAI deployments in payment contexts leak one user's
CHD into another user's session. Cross-session CHD exposure is a
Req 3 and Req 7 finding.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Restrict access by need to know | Req 7.2.1 | Strict session isolation — each user's CHD context inaccessible to all other sessions |
| Protect stored account data | Req 3.5.1 | Per-user session CHD encrypted — KV cache isolation prevents cross-session PAN exposure |
| Logging | Req 10.2.1 | Cross-session access anomalies logged — unusual retrieval patterns in PCI scope detected |
| Penetration testing | Req 11.3.1 | Multi-tenant isolation tested in CDE penetration testing — cross-session CHD access attempted |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Implement strict session isolation for all
  GenAI deployments in PCI scope — per-user context,
  RAG namespaces, and KV cache isolation required
- Req 3.5.1: Encrypt per-user session data containing
  CHD — session isolation technical control documented
- Req 11.3.1: Test multi-tenant isolation in CDE
  penetration testing — cross-session CHD access attempts
  documented as testing evidence

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · GDPR Art. 32 · SOC 2 CC6.1

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical

LLM-to-database interfaces in PCI scope create direct paths from
natural language to payment systems. Prompt injection against an
LLM-to-SQL interface with access to cardholder tables is a Req 6
and Req 7 critical finding.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Restrict access | Req 7.2.1 | LLM-generated queries execute under requesting user's CDE permissions — never shared high-privilege account |
| Bespoke software | Req 6.2.4 | LLM-to-SQL interfaces address injection as a known vulnerability class — query allowlisting, parameterised execution |
| Public-facing application protection | Req 6.4.1 | LLM-powered query interfaces in CDE scope protected — WAF or equivalent, input validation |
| Logging | Req 10.2.1 | All LLM-generated queries to CDE systems logged — full audit trail with user identity |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Enforce per-user query execution — LLM
  queries to CDE systems execute under requesting user's
  permissions, never a shared high-privilege service account
- Req 6.2.4: Implement query allowlisting and parameterised
  execution — injection addressed as a known vulnerability
  class in Req 6.2 secure development standards
- Read-only by default — no write access through LLM-to-CDE
  interfaces without formal approval and change management

**Hardening**
- Req 6.4.1: Apply web application protection to all
  LLM query interfaces in PCI scope — WAF or equivalent,
  input validation at application layer
- Req 10.2.1: Log all LLM-generated queries to CDE
  systems — query text, requesting user identity, timestamp —
  full Req 10 audit trail
- Req 11.3.1: Include NL gateway injection in CDE
  penetration testing — SQL injection via LLM output
  tested and documented

**Advanced**
- Deploy independent query validation layer — Req 6.2
  defence-in-depth for CDE query interfaces
- Req 11.3.1: Conduct adversarial NL-to-SQL testing —
  attempt destructive query generation through crafted
  natural language, document as CDE penetration testing

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-89 · ISA/IEC 62443 SR 2.2 (OT)

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases containing embeddings of CHD-adjacent documentation
represent secondary attack surfaces that assessors may not identify
without explicit documentation. RBAC gaps and CVEs in vector databases
in CDE scope are Req 6.3 and Req 7 findings.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Protect stored account data | Req 3.5.1 | Vector stores in CDE scope encrypted — embeddings of CHD-adjacent content encrypted at rest |
| Restrict access | Req 7.2.1 | RBAC on all vector stores in PCI scope — no unauthenticated access in any CDE environment |
| Vulnerability management | Req 6.3.3 | Vector database CVEs patched — CVE-2024-3584 class treated as urgent for CDE-scope stores |
| Penetration testing | Req 11.3.1 | Vector store attacks in CDE penetration testing — RBAC bypass, path traversal, bulk extraction |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Enable RBAC on all vector stores in PCI
  scope — no unauthenticated access in any CDE environment
- Req 3.5.1: Encrypt all vector store content in CDE
  scope at rest — strong cryptography required
- Req 6.3.3: Patch all known vector database CVEs
  promptly — CVE-2024-3584 class as urgent findings in
  CDE scope

**Hardening**
- Scope design: Apply PAN tokenisation before embedding
  generation — removes CHD from vector store scope,
  eliminates Req 3 obligations for most embedding stores
- Req 11.3.1: Include vector store security in CDE
  penetration testing — RBAC bypass and bulk extraction
  scenarios documented as testing evidence
- Network isolation — vector stores in CDE scope
  accessible only from authorised CDE services

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Agentic Top 10: ASI06 Memory and Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · SOC 2 CC6.1

---

### DSGAI14 — Excessive Telemetry and Monitoring Leakage

**Severity:** High

Observability pipelines capture full GenAI inputs and outputs —
where CHD flows through GenAI, observability data may contain
PANs in cleartext, making telemetry stores CHD in scope.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Protect stored account data | Req 3.5.1 | Telemetry stores containing CHD encrypted — observability data is CHD if it contains PANs |
| PAN rendering | Req 3.4.1 | PANs in telemetry masked before logging — cleartext PANs in observability data is a Req 3 finding |
| Restrict access | Req 7.2.1 | Access controls on CDE telemetry stores — Req 7 need-to-know applies |
| Logging | Req 10.2.1 | Access to CDE telemetry stores logged — accessing observability data containing CHD requires Req 10 trail |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 3.4.1: Implement PAN masking before logging to
  telemetry systems — no cleartext PANs in observability
  data, mask at the pipeline ingestion point
- Req 3.5.1: If CHD is present in telemetry despite
  masking, encrypt telemetry stores at rest — same Req 3
  protection as production CHD stores
- Least-logging default — do not log full query/response
  content for GenAI in CDE scope without explicit need

**Hardening**
- Req 7.2.1: Apply need-to-know access controls to CDE
  telemetry stores — restrict to authorised personnel
  with documented business need
- Short TTL for debug traces containing CHD — Req 9.4
  media disposal requirement applies to expired CHD
- Scope design: PAN tokenisation before GenAI processing
  prevents CHD from appearing in any telemetry

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15 · GDPR Art. 32 · SOC 2 C2.1

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Excessive context injection in PCI scope may aggregate CHD from
multiple sources into a single LLM context — amplifying the impact
of any successful injection against a payment-context LLM.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Restrict access | Req 7.2.1 | Context assembly restricted to minimum CHD required — users cannot access CHD beyond their authorised scope through context injection |
| PAN rendering | Req 3.4.1 | PANs in context window masked — cleartext PANs in LLM context is a Req 3 exposure |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for context window CHD exposure — blast radius of over-broad injection documented |
| Logging | Req 10.2.1 | Context window assembly logged — all CHD accessed through context injection traceable |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Implement minimum-necessary context injection
  for all GenAI in PCI scope — retrieve only CHD directly
  relevant to the current query, not broad datasets
- Req 3.4.1: Apply PAN masking in context assembly —
  PANs masked before injection into LLM context
- Scope design: Tokenise CHD before context assembly —
  eliminates Req 3 obligations for context window content

**Hardening**
- Track classification of all CHD in context window —
  highest classification drives response handling
- Req 12.3.2: Document targeted risk analysis for
  over-broad context exposure — CHD aggregation risk
  per deployment context

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: AIUC-1 A/B005 · SOC 2 CC6.1

---

### DSGAI16 — Endpoint and Browser Assistant Overreach

**Severity:** High

Browser AI assistants on payment system workstations can access
CHD across open applications. In PCI scope, endpoint AI assistants
with access to CDE applications are TPSPs requiring Req 12.8
treatment.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| TPSP programme | Req 12.8.1 | Browser AI extension providers with CDE access are TPSPs — add to TPSP list, initiate compliance process |
| Vulnerability management | Req 6.3.3 | Browser AI extensions patched and version-controlled — vulnerable extensions are Req 6.3 findings in CDE |
| Logging | Req 10.2.1 | AI assistant access to CDE data on endpoint logged — Req 10 audit trail requirement |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for endpoint AI assistant scope in CDE — data accessible, exfiltration paths |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.8.1: Assess browser AI extension providers
  with CDE access as TPSPs — written agreements,
  compliance monitoring for all approved extensions
  on CDE workstations
- Block unapproved browser AI extensions on CDE
  workstations — device management enforcement
- Req 6.3.3: Version control and patch management for
  approved AI extensions — vulnerable versions blocked
  from CDE workstations

**Hardening**
- Req 10.2.1: Log all AI assistant access to CDE data
  from endpoints — Req 10 audit trail requirement
- Req 12.3.2: Document targeted risk analysis for
  endpoint AI in CDE — data accessible, exfiltration
  potential, controls implemented

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · SOC 2 CC9.1

---

### DSGAI17 — Data Availability and Resilience Failures

**Severity:** High

Silent GenAI pipeline failures affect payment advisory and fraud
detection availability. In PCI scope, availability of fraud
detection LLMs is a payment processing continuity requirement.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for GenAI availability in payment processing — silent failure impact on fraud detection |
| Network security | Req 1.3.2 | Rate limiting protecting availability of CDE-facing LLM endpoints — DoS prevention |
| Audit log review | Req 10.6.1 | Automated monitoring for GenAI pipeline health in CDE — freshness and availability metrics reviewed |
| Incident response | Req 12.10.1 | Incident response procedure covers GenAI pipeline failures affecting payment processing |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.10.1: Include GenAI pipeline failures in PCI
  incident response procedures — silent RAG degradation
  affecting fraud detection treated as a security incident
- Req 1.3.2: Implement network-layer rate limiting for
  CDE-facing GenAI endpoints — DoS protection as Req 1
  network security control
- Req 10.6.1: Include GenAI pipeline health in CDE log
  analysis — freshness monitoring alerts reviewed as
  part of Req 10 log review programme

**Hardening**
- Req 12.3.2: Document targeted risk analysis for GenAI
  availability — fraud detection impact, RTO/RPO,
  fallback controls
- Circuit breakers with graceful degradation — explicit
  unavailability notice rather than silent misinformation
  in fraud detection context

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · SOC 2 A1.1

---

### DSGAI18 — Inference and Data Reconstruction

**Severity:** High

Membership inference and model inversion attacks reconstruct PANs
and cardholder data from GenAI model outputs. In PCI scope,
successful PAN reconstruction from model outputs is a Req 3 data
protection failure.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| PAN rendering | Req 3.4.1 | PANs reconstructed from model outputs must be prevented — inference attack resistance as Req 3 control |
| Protect stored CHD | Req 3.5.1 | Embeddings that can reconstruct PANs require Req 3 protection — differential privacy as encryption equivalent |
| Penetration testing | Req 11.3.1 | Inference attack testing for GenAI models trained on CHD — membership inference and inversion attacks |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for inference attack risk against CHD-trained GenAI models |

#### Mitigations for PCI DSS compliance

**Foundational**
- Apply differential privacy during training on CHD —
  Req 3 advanced protection reducing PAN reconstruction
  risk from model outputs
- Suppress confidence scores and logits in CDE GenAI
  outputs — limits membership inference success rate
- Req 12.3.2: Document targeted risk analysis for
  inference attacks — CHD-trained models, techniques,
  controls, residual risk accepted

**Hardening**
- Req 11.3.1: Include membership inference and model
  inversion in CDE penetration testing — validate CHD
  cannot be reconstructed, results documented
- Output rate limiting — limits inference attack query
  volume, Req 6.4 application protection control

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 25 · SOC 2 C2.1

---

### DSGAI19 — Human-in-Loop and Labeler Overexposure

**Severity:** Medium

Human annotators access payment data during labelling of fraud
detection and transaction classification models. Labelling vendors
with access to CHD are TPSPs under PCI DSS Req 12.8.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| TPSP programme | Req 12.8.1 | Labelling vendors with access to CHD are TPSPs — add to TPSP list, initiate compliance process |
| TPSP agreements | Req 12.8.3 | Written agreements with labelling vendors acknowledging CHD security responsibility |
| SAD prohibition | Req 3.3.1 | SAD must never appear in labelling tasks — labels cannot expose CVV or full magnetic stripe data |
| Restrict access | Req 7.2.1 | Labelling task data minimised — annotators see minimum CHD required for annotation function |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 12.8.1: Include labelling vendors with CHD access
  in TPSP list — initiate Req 12.8 compliance process
  before sharing any CHD with labellers
- Req 12.8.3: Establish written agreements with labelling
  vendors acknowledging CHD security responsibility —
  required before any CHD is shared for annotation
- Apply PAN tokenisation in labelling tasks — removes
  Req 3 obligations from annotator access while preserving
  annotation-relevant data patterns

**Hardening**
- Req 3.3.1: Verify SAD never appears in labelling tasks —
  audit annotation interfaces for SAD exposure before
  any labelling begins
- Req 7.2.1: Apply data minimisation — annotators see
  minimum CHD required for their specific annotation
  function, not full transaction records

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34 · GDPR Art. 28 · SOC 2 CC9.2

---

### DSGAI20 — Model Exfiltration and IP Replication

**Severity:** High

Proprietary GenAI models trained on payment data or fraud detection
logic represent both IP and potential CHD exposure risk if model
internals can be reconstructed. Req 7 access controls and Req 6.4
application protection apply.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Restrict access | Req 7.2.1 | API rate limiting as access control — systematic model extraction requires high query volumes |
| Public-facing application protection | Req 6.4.1 | Model extraction pattern detection as application protection — systematic API abuse detected |
| Audit log review | Req 10.6.1 | Automated monitoring for extraction patterns — unusual query diversity alerted |
| Targeted risk analysis | Req 12.3.2 | Targeted risk analysis for model extraction — IP exposure, CHD reconstruction potential assessed |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 7.2.1: Implement API rate limiting as access
  control — systematic extraction requires high query
  volumes, rate limiting raises cost and triggers detection
- Req 10.6.1: Monitor for extraction patterns in CDE
  GenAI logs — unusual query diversity detected as part
  of automated Req 10 log analysis
- Req 12.3.2: Document targeted risk analysis for model
  extraction — IP exposure, CHD reconstruction potential,
  controls implemented

**Hardening**
- Req 6.4.1: Deploy query anomaly detection as application
  protection — systematic extraction behaviour blocked
- Implement model watermarking — enables detection of
  replicated payment fraud models in the wild

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference and Data Reconstruction
- Other frameworks: ISO 27001 A.5.12 · MITRE ATLAS AML.T0016 · SOC 2 C2.1

---

### DSGAI21 — Disinformation and Integrity Attacks via Data Poisoning

**Severity:** High

False content injected into RAG corpora causes GenAI fraud detection
or payment advisory systems to surface incorrect guidance. In
payment contexts, RAG poisoning can systematically bias fraud
decisions or provide incorrect compliance guidance to analysts.

#### PCI DSS v4.0 mapping

| Requirement | ID | How it applies |
|---|---|---|
| Secure system changes | Req 6.5.6 | RAG corpus updates tested for unexpected content — integrity verification before production indexing |
| TPSP programme | Req 12.8 | RAG data source providers as TPSPs — content quality and integrity requirements in agreements |
| Audit log review | Req 10.6.1 | RAG corpus monitoring — anomalous content detected and reviewed as part of Req 10 log analysis |
| Penetration testing | Req 11.3.1 | Adversarial RAG integrity testing for payment advisory systems — false content injection attempts documented |

#### Mitigations for PCI DSS compliance

**Foundational**
- Req 6.5.6: Test RAG corpus updates for unexpected content
  before production indexing — Req 6.5 change management
  applies to RAG corpus changes in CDE scope
- Req 12.8: Include RAG data source providers in TPSP
  programme — content quality guarantees in vendor agreements
- Source trust tiering — authoritative payment standards
  sources weighted higher than general web content

**Hardening**
- Req 10.6.1: Include RAG corpus integrity monitoring
  in CDE log analysis — anomalous content changes alerted
- Req 11.3.1: Include adversarial RAG integrity testing
  in CDE penetration testing — attempt content injection
  via documentation sources, document results
- Cryptographic provenance for PCI compliance documentation
  in RAG — verify integrity of regulatory guidance sources

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory and Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 · ISO 27001 A.5.7 · SOC 2 PI1.2

---

## PCI DSS v4.0 audit preparation checklist for GenAI data security

### Scope determination (mandatory first step)

- [ ] All GenAI systems assessed for CDE scope
- [ ] CHD data inventory includes all GenAI-derived assets (Req 3.1.1)
- [ ] Data flow diagrams updated to include all GenAI pipelines (Req 3.2.1)
- [ ] PAN tokenisation applied before GenAI processing where possible (scope minimisation)

### Data protection (Req 3, Req 4)

- [ ] PANs masked in all GenAI outputs (Req 3.4.1)
- [ ] No SAD in any GenAI training data or RAG corpus (Req 3.3.1)
- [ ] All CHD in GenAI scope encrypted at rest (Req 3.5.1)
- [ ] All GenAI data flows carrying CHD encrypted TLS 1.2 minimum (Req 4.2.1)
- [ ] PAN masking applied before telemetry logging (Req 3.4.1)
- [ ] Synthetic payment data PCI scope assessed (Req 3.1.1)

### Secure development (Req 6)

- [ ] Injection vulnerabilities addressed in all GenAI integration code (Req 6.2.4)
- [ ] Public-facing GenAI applications protected (Req 6.4.1)
- [ ] Model updates through change management with testing (Req 6.5)
- [ ] CVE-2024-3584 class vulnerabilities patched (Req 6.3.3)
- [ ] NL gateway query allowlisting implemented (Req 6.2.4)

### Access control (Req 7, Req 8)

- [ ] GenAI access to CHD restricted to minimum required (Req 7.2.1)
- [ ] Unique agent identities for CDE-facing agents (Req 8.2.1)
- [ ] RBAC on all vector stores in CDE scope (Req 7.2.1)
- [ ] Session isolation for multi-user CDE GenAI deployments (Req 7.2.1)
- [ ] Context assembly respects user CHD authorisation (Req 7.2.1)

### Logging and monitoring (Req 10)

- [ ] All GenAI access to CHD logged with user identity (Req 10.2.1)
- [ ] All NL gateway queries logged (Req 10.2.1)
- [ ] Automated monitoring covers GenAI anomalies (Req 10.6.1)
- [ ] Telemetry access logged where CHD may be present (Req 10.2.1)

### Testing (Req 11)

- [ ] Prompt injection and output injection in CDE penetration testing (Req 11.3.1)
- [ ] Vector store RBAC bypass in CDE penetration testing (Req 11.3.1)
- [ ] Model poisoning detection in penetration testing (Req 11.3.1)
- [ ] NL gateway SQL injection in CDE penetration testing (Req 11.3.1)
- [ ] Inference attack testing for CHD-trained models (Req 11.3.1)

### Vendor and policy (Req 12)

- [ ] All GenAI vendors with CHD access in TPSP list (Req 12.8.1)
- [ ] Written agreements with all CHD-accessing GenAI vendors (Req 12.8.3)
- [ ] TPSP compliance monitored for AI vendors (Req 12.8.4)
- [ ] Labelling vendors with CHD access in TPSP programme (Req 12.8)
- [ ] Shadow AI included in security awareness (Req 12.6.1)
- [ ] Targeted risk analyses documented for all DSGAI entries in PCI scope (Req 12.3.2)
- [ ] GenAI failures in incident response procedures (Req 12.10.1)

---

## Implementation priority

| Phase | DSGAI entries | PCI DSS requirements | Rationale |
|---|---|---|---|
| 1 — Scope first | DSGAI01, DSGAI07 | Req 3.1, Req 3.4, Req 3.5 | Data inventory and PAN protection are the foundation |
| 2 — Vendor and access | DSGAI02, DSGAI03, DSGAI06 | Req 7, Req 8, Req 12.8 | NHI, shadow AI, and tool provider TPSP obligations |
| 3 — Secure development | DSGAI05, DSGAI12 | Req 6.2, Req 6.4 | Ingestion validation and NL gateway injection |
| 4 — Supply chain and testing | DSGAI04, DSGAI21 | Req 6.5, Req 11.3 | Change management and penetration testing scope |
| 5 — Ongoing | DSGAI08-DSGAI20 | Req 12.3, Req 10.6 | Risk analysis, monitoring, and advanced attack coverage |

---

## References

- PCI DSS v4.0: https://www.pcisecuritystandards.org/document_library/
- PCI SSC Information Supplement — Third-Party Security Assurance: https://www.pcisecuritystandards.org
- PCI DSS v4.0 Summary of Changes: https://www.pcisecuritystandards.org/documents/PCI-DSS-v4-0-Summary-of-Changes-r2.pdf
- OWASP GenAI Data Security Risks 2026: https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
- LLM Top 10 x PCI DSS mapping: see LLM_PCIDSS.md in this repository

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-25 | 2026-Q1 | Initial mapping — DSGAI01-DSGAI21 full entries with PCI DSS v4.0 compliance checklist | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
