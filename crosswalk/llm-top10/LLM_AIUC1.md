<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : AIUC-1 — The standard for AI agent security, safety and reliability
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × AIUC-1

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [AIUC-1](https://www.aiuc-1.com/) — the world's first AI agent security,
safety and reliability certification framework, developed with 100+
Fortune 500 CISOs and used as the SOC 2 analog for AI agents.

AIUC-1 is an OWASP GenAI Security Project partner. Although designed
for agentic deployments, its six domains (Security, Safety, Reliability,
Data & Privacy, Accountability, Society) provide direct control
mappings for all 10 LLM risks — and for any LLM application that
acts on behalf of users, AIUC-1 certification is an increasingly
standard customer expectation.

---

## AIUC-1 domains at a glance

| Domain | ID | Focus |
|---|---|---|
| Data & Privacy | A | PII protection, data leakage, IP, access controls, training data |
| Security | B | Adversarial robustness, prompt injection, output filtering, permissions |
| Safety | C | Harm prevention, unsafe outputs, guardrails, human oversight |
| Reliability | D | Availability, consistency, failure recovery, rate limiting |
| Accountability | E | Audit trails, logging, explainability, incident response |
| Society | F | Bias, misinformation, societal harm, transparency |

---

## Quick-reference summary

| ID | Name | Severity | Primary AIUC-1 Domains/Controls | Tier |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | B001, B002, B005, B006 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | A (all), B006, E | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | B001, B003, B008, A | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | A (all), B001, B002, E | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | B005, B006, B009, C | Foundational–Hardening |
| LLM06 | Excessive Agency | High | B006, B007, C, E | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | A, B006, E | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | A, B001, B002, B005 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | C, F, B009, E | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | D, B006, E | Foundational–Hardening |

---

## Audience tags

- **Developer** — B001, B005, B006, B009 — implementation controls
- **Security engineer** — B001–B009, E — full security domain
- **Auditor** — A, E, B003, B007 — evidence and compliance
- **CISO / governance** — A, C, E, F — programme and oversight
- **Red teamer** — B001, B002, B005 — adversarial testing controls
- **ML / AI engineer** — A, B001, B005, B006 — model and data security
- **Product / trust & safety** — C, F — safety and societal controls

---

## Detailed mappings

---

### LLM01 — Prompt Injection

Untrusted input overrides model instructions — via direct user
manipulation or indirect injection through retrieved data, tool
outputs, or multi-modal content.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Mandatory adversarial testing validating resilience against injection | Foundational |
| Detect adversarial input | B002 | Runtime monitoring to detect adversarial inputs | Hardening |
| Implement real-time input filtering | B005 | Automated filtering of inputs before model reasoning | Foundational |
| Prevent unauthorized AI actions | B006 | Guardrails preventing execution of injected instructions | Foundational |

#### Three-tier mitigations

**Foundational:**
- Treat all external content (documents, tool outputs, RAG chunks) as untrusted
- Implement B005 input filtering on all channels feeding model context
- Deploy B006 action guardrails: model cannot execute actions outside defined scope

**Hardening:**
- Enable B002 runtime anomaly detection on model outputs
- Require human approval for any high-impact action triggered by external content
- Version-control and audit all system prompts

**Advanced:**
- Multi-layer intent verification before irreversible actions
- Quarterly red team exercises with indirect injection scenarios
- B001 adversarial testing in CI/CD for every model or prompt update

#### Cross-references

- Agentic: ASI01 (Prompt Injection in Agentic Systems)
- DSGAI: DSGAI01 (Prompt Injection via Data Channels)
- See also: [LLM_AITG.md](LLM_AITG.md), [LLM_STRIDE.md](LLM_STRIDE.md)

---

### LLM02 — Sensitive Information Disclosure

Models surface confidential data — PII, credentials, trade secrets,
private training data — in responses through memorisation, over-retrieval,
or insufficient output filtering.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| PII protection and data leakage prevention | A | Domain A controls for data minimisation, access control, output filtering | Foundational |
| Prevent unauthorized AI actions | B006 | Scope restrictions preventing disclosure of protected data categories | Foundational |
| Audit trails and logging | E | Logging of all outputs for disclosure incident investigation | Foundational |

#### Three-tier mitigations

**Foundational:**
- Apply Domain A data classification to all training and retrieval data
- Add DLP scanning to all model outputs before delivery
- Define and enforce output blocklist for sensitive data patterns

**Hardening:**
- Per-user output filtering based on entitlement
- Domain E: audit logging of all outputs with retention for incident investigation
- V-ST: test suite probing for memorised sensitive content

**Advanced:**
- Differential privacy for sensitive training data
- Real-time output anomaly detection with automated redaction
- Annual model audit for sensitive data memorisation

#### Cross-references

- DSGAI: DSGAI06 (Unintended Data Disclosure), DSGAI03 (Sensitive Data in Training Sets)
- See also: [LLM_SOC2.md](LLM_SOC2.md), [LLM_PCIDSS.md](LLM_PCIDSS.md)

---

### LLM03 — Supply Chain Vulnerabilities

Third-party components — model providers, fine-tuning services, plugins,
tool libraries, RAG frameworks — are compromised or malicious, introducing
vulnerabilities into the LLM deployment.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Third-party adversarial robustness testing | B001 | Extend testing scope to third-party components | Foundational |
| Third-party security assessment | B003 | Formal assessment of all third-party integrations | Hardening |
| Third-party NHI controls | B008 | Controls for third-party credentials and identities | Hardening |
| Data & Privacy supply chain controls | A | Training data and model provenance verification | Foundational |

#### Three-tier mitigations

**Foundational:**
- Inventory all third-party components (models, tools, frameworks)
- Generate SBOM for LLM deployment
- Pin all dependency versions; reject floating versions in production

**Hardening:**
- B003: formal third-party security assessment for critical components
- B008: apply NHI controls to all third-party credentials and tokens
- Automated vulnerability scanning for LLM SBOM

**Advanced:**
- B001 supply chain adversarial testing: can a compromised plugin affect model behaviour?
- Annual third-party security review programme
- Formal model provenance attestation for regulated deployments

#### Cross-references

- Agentic: ASI07 (Supply Chain Compromise in Agent Ecosystems)
- DSGAI: DSGAI16, DSGAI17 (Third-Party and Model Supply Chain)
- See also: [LLM_CWE_CVE.md](LLM_CWE_CVE.md)

---

### LLM04 — Data and Model Poisoning

Training data, fine-tuning datasets, or model weights are corrupted —
causing models to learn backdoored, biased, or degraded behaviours.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain (all controls) | A | Training data integrity, provenance, and access control | Foundational |
| Third-party adversarial robustness testing | B001 | Backdoor and poisoning detection in training pipeline | Foundational |
| Detect adversarial input | B002 | Detect anomalous training data patterns | Hardening |
| Audit trails and logging | E | Chain of custody for training data | Foundational |

#### Three-tier mitigations

**Foundational:**
- Apply Domain A controls to all training datasets
- Hash verification for all training data at ingestion
- B001 adversarial probing of trained models for backdoor triggers

**Hardening:**
- B002 anomaly detection on training data distributions
- Domain E: immutable chain of custody log from data source to training job
- Restrict training data write access to authorised pipeline only

**Advanced:**
- B001 automated poisoning detection in ML CI/CD
- Differential privacy for high-sensitivity training scenarios
- Periodic model re-evaluation against clean held-out dataset

#### Cross-references

- DSGAI: DSGAI02 (Training Data Poisoning), DSGAI09 (RAG Corpus Manipulation)
- See also: [LLM_MITREATLAS.md](LLM_MITREATLAS.md) AML.T0018

---

### LLM05 — Insecure Output Handling

LLM output is processed by downstream systems (code interpreters,
browsers, SQL engines) without sanitisation — enabling XSS, code
injection, SSRF, or privilege escalation via crafted model responses.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Implement real-time input filtering | B005 | Apply output validation before downstream processing | Foundational |
| Prevent unauthorized AI actions | B006 | Scope restrictions on what downstream systems can execute from model output | Foundational |
| Validate AI-generated content | B009 | Validation of all model output before use in downstream systems | Foundational |
| Safety domain (harm prevention) | C | Safety controls on content passed to executors | Foundational |

#### Three-tier mitigations

**Foundational:**
- B009: validate all model output before passing to code interpreters or databases
- B005: output filtering before downstream processing
- Never pass raw model output to shell, SQL, or browser without sanitisation

**Hardening:**
- B006: scope restrictions on code execution environments
- Output content type enforcement: model cannot output JavaScript in contexts that will render it
- Red team: attempt code injection via crafted model output

**Advanced:**
- Automated output validation test suite in CI/CD
- Sandboxed execution environment for all model-generated code
- B009 output schema validation for structured output pipelines

#### Cross-references

- See also: [LLM_ASVS.md](LLM_ASVS.md), [LLM_CWE_CVE.md](LLM_CWE_CVE.md) CWE-79, CWE-89

---

### LLM06 — Excessive Agency

LLM-enabled features with access to tools, plugins, or APIs take
autonomous actions with real-world consequences — without appropriate
scope limitations, human oversight, or reversibility controls.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Prevent unauthorized AI actions | B006 | Scope restrictions on all LLM-triggered tool and API calls | Foundational |
| Third-party permission controls | B007 | Least-privilege for all third-party tool access | Hardening |
| Safety domain (human oversight) | C | Human confirmation gates for high-impact actions | Foundational |
| Accountability domain (audit trails) | E | Immutable log of all autonomous actions | Foundational |

#### Three-tier mitigations

**Foundational:**
- B006: define and enforce scope limits for all tool/API access
- Domain C: human confirmation gates for irreversible actions
- Domain E: immutable audit log of all LLM-triggered actions

**Hardening:**
- B007: least-privilege access for all tool integrations
- Autonomy tiers per action class: auto / confirm / human-required
- Formal autonomy policy reviewed and signed by CISO

**Advanced:**
- JIT permission issuance per task (see RECIPES.md)
- Real-time oversight dashboard for operations team
- Quarterly autonomy policy review incorporating incident findings

#### Cross-references

- Agentic: ASI02 (Excessive Permissions), ASI09 (Inadequate Human Oversight)
- DSGAI: DSGAI07 (Excessive Data Access)
- See also: [LLM_SAMM.md](LLM_SAMM.md)

---

### LLM07 — System Prompt Leakage

Confidential system prompt contents — instructions, personas, access
tokens, business logic — are extracted through adversarial prompting
or model over-disclosure.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | System prompt classified as confidential; access controls applied | Foundational |
| Prevent unauthorized AI actions | B006 | Model cannot disclose system prompt contents in output | Foundational |
| Accountability domain | E | Log all disclosure attempts for incident investigation | Foundational |

#### Three-tier mitigations

**Foundational:**
- Classify system prompt contents as confidential
- B006: instruction to model must not disclose system prompt
- Domain E: log all queries that attempt to extract system prompt

**Hardening:**
- Red team: systematic system prompt extraction attempts
- V-ST: automated test battery for prompt leakage
- Remove unnecessary sensitive information from system prompts

**Advanced:**
- Architecture review: does the system require secrets in system prompts? Can these be externalised?
- Periodic system prompt audit for unnecessary sensitive content

#### Cross-references

- See also: [LLM_ASVS.md](LLM_ASVS.md), [LLM_AITG.md](LLM_AITG.md)

---

### LLM08 — Vector and Embedding Weaknesses

Embedding stores used in RAG systems are vulnerable to cross-tenant
leakage, semantic injection, direct database access, and integrity
attacks on stored vector representations.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Data & Privacy domain | A | Access controls and integrity for embedding stores | Foundational |
| Third-party adversarial robustness testing | B001 | Adversarial testing of retrieval pipeline | Foundational |
| Detect adversarial input | B002 | Detection of anomalous retrieval patterns | Hardening |
| Implement real-time input filtering | B005 | Filter retrieved content before context assembly | Foundational |

#### Three-tier mitigations

**Foundational:**
- Domain A: access controls on embedding stores (per-tenant, per-user)
- B005: filter retrieved content before context window inclusion
- Integrity verification on stored embeddings

**Hardening:**
- B001: adversarial testing of retrieval pipeline — cross-tenant leakage, semantic injection
- B002: anomaly detection on retrieval patterns
- Red team: attempt cross-tenant retrieval leakage

**Advanced:**
- Differential privacy for embeddings of sensitive content
- Continuous monitoring of embedding distribution drift
- Architecture review: embedding store access control design

#### Cross-references

- DSGAI: DSGAI08 (Data Leakage in Retrieval), DSGAI09 (RAG Corpus Manipulation)
- See also: [LLM_ASVS.md](LLM_ASVS.md), [shared/RECIPES.md](../shared/RECIPES.md) Pattern 1

---

### LLM09 — Misinformation

LLMs generate confident, plausible, but factually incorrect information —
hallucinations, fabricated citations, outdated facts — that users or
downstream systems act upon as if true.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Safety domain (harm prevention) | C | Guardrails against harmful misinformation outputs | Foundational |
| Society domain | F | Transparency about AI-generated content limitations | Foundational |
| Validate AI-generated content | B009 | Factual validation of outputs in high-stakes domains | Foundational |
| Accountability domain | E | Logging and explainability for misinformation incidents | Foundational |

#### Three-tier mitigations

**Foundational:**
- Domain C: content guardrails flagging low-confidence outputs in high-stakes domains
- Domain F: user-facing disclosure that content is AI-generated
- B009: validation layer for outputs in regulated or safety-critical domains

**Hardening:**
- RAG with authoritative sources to ground model outputs
- Human review gates for high-stakes decisions based on model output
- Domain E: audit logs of all outputs for misinformation incident investigation

**Advanced:**
- Automated fact-checking pipeline for high-stakes domains
- Domain F: feedback mechanism for users to report hallucinations
- Red team: identify high-hallucination domains for this specific model

#### Cross-references

- See also: [LLM_SAMM.md](LLM_SAMM.md), [LLM_EUAIAct.md](LLM_EUAIAct.md)

---

### LLM10 — Unbounded Consumption

LLM applications have no resource consumption limits — enabling
denial-of-service via excessive API calls, token flooding, context
window exhaustion, or disproportionate compute consumption.

#### AIUC-1 mapping

| Control | ID | Description | Tier |
|---|---|---|---|
| Reliability domain (all) | D | Availability controls, rate limiting, and failure recovery | Foundational |
| Prevent unauthorized AI actions | B006 | Scope restrictions preventing resource exhaustion | Foundational |
| Accountability domain | E | Monitoring and alerting for consumption anomalies | Foundational |

#### Three-tier mitigations

**Foundational:**
- Domain D: implement rate limiting per user/tenant at API gateway
- B006: maximum token budget per request enforced at application layer
- Domain E: alert on consumption anomalies

**Hardening:**
- Domain D: circuit breakers and graceful degradation under load
- Per-user and per-tenant consumption quotas with soft/hard limits
- Domain E: forensic logging of high-volume sessions

**Advanced:**
- Domain D: predictive capacity management based on usage patterns
- Red team: DoS simulation targeting token consumption and context flooding
- Cost attribution per user for enterprise deployments

#### Cross-references

- Agentic: ASI10 (Cascading Agent Failures)
- See also: [LLM_ASVS.md](LLM_ASVS.md), [LLM_NISTCSF2.md](LLM_NISTCSF2.md)

---

## AIUC-1 certification readiness checklist — LLM deployments

| Domain | Control | LLM01 | LLM02 | LLM03 | LLM04 | LLM05 | LLM06 | LLM07 | LLM08 | LLM09 | LLM10 |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A — Data & Privacy | Data classification and access controls | | ✓ | ✓ | ✓ | | | ✓ | ✓ | | |
| B — Security | B001 Adversarial testing | ✓ | | ✓ | ✓ | | | | ✓ | | |
| B — Security | B002 Detect adversarial input | ✓ | | | ✓ | | | | ✓ | | |
| B — Security | B005 Input/output filtering | ✓ | | | | ✓ | | | ✓ | | |
| B — Security | B006 Prevent unauthorized actions | ✓ | ✓ | | | ✓ | ✓ | ✓ | | | ✓ |
| B — Security | B009 Validate AI-generated content | | | | | ✓ | | | | ✓ | |
| C — Safety | Guardrails and human oversight | | | | | ✓ | ✓ | | | ✓ | |
| D — Reliability | Rate limiting and fault tolerance | | | | | | | | | | ✓ |
| E — Accountability | Audit trails and logging | | ✓ | | ✓ | | ✓ | ✓ | | ✓ | ✓ |
| F — Society | Transparency and bias controls | | | | | | | | | ✓ | |

---

## References

- [AIUC-1 Standard](https://www.aiuc-1.com/)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [Agentic_AIUC1.md](../agentic-top10/Agentic_AIUC1.md) — AIUC-1 for agentic deployments
- [LLM_AITG.md](LLM_AITG.md) — testing guide aligned with B001 adversarial testing
- [LLM_SAMM.md](LLM_SAMM.md) — programme maturity complement to AIUC-1 certification

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping LLM01–LLM10 to AIUC-1 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
