<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : OWASP AISVS 1.0
  Version     : 2026-Q3
  Maintained by: OWASP GenAI Data Security Initiative - https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# OWASP Top 10 for LLM Applications 2025 × OWASP AISVS 1.0

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) to the [OWASP Artificial Intelligence Security Verification Standard 1.0](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/), a technical verification standard of 191 testable requirements across 12 chapters, used by engineers and auditors to verify that a specific AI system implements a control rather than merely documents it.

---

## Why AISVS for this source list

Most frameworks already in this crosswalk answer the question of what an organisation should govern. AISVS answers a different question: given a running AI system, what does an assessor check, and what does a pass look like. Every requirement is written to be independently verifiable and starts with the words Verify that.

That makes this mapping the bridge between a risk in this source list and a concrete test an engineer can run. Where ISO 42001 or NIST AI RMF establish that a control must exist, AISVS states the condition that demonstrates it does. The two are complements, not substitutes, and reading them together turns a control objective into an audit step.

AISVS also assigns each requirement a level from 1 to 3 reflecting implementation difficulty and how situational the control is. That maps cleanly onto the tier model used throughout this crosswalk, so the tier column below carries real information about sequencing rather than a subjective judgement.

---

## AISVS structure

| Chapter | Description | Requirements |
|---|---|---|
| [C1 Training Data Integrity & Traceability](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md) | This chapter addresses protecting the integrity and traceability of training data as it is sourced, handled, and maintained. | 13 |
| [C2 Input Validation](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C02-Input-Validation.md) | This chapter addresses validation of all inputs as a first-line defense against prompt injection, one of the most damaging attacks on AI systems. | 12 |
| [C3 Model Lifecycle Management & Change Control](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md) | This chapter addresses control of model changes so that unauthorized or unsafe modifications cannot reach production. | 15 |
| [C4 Infrastructure, Configuration & Deployment Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C04-Infrastructure.md) | This chapter addresses hardening AI-specific infrastructure components against model theft, data leakage, and cross-tenant contamination. | 14 |
| [C5 Access Control & Identity for AI Components & Users](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C05-Access-Control-and-Identity.md) | This chapter addresses access control challenges that AI systems introduce beyond traditional application security. | 11 |
| [C6 Supply Chain Security for Models](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C06-Supply-Chain.md) | This chapter addresses defending against AI supply chain attacks that exploit third-party models, frameworks, or datasets to embed backdoors, bias, or exploitable code. | 7 |
| [C7 Model Behavior, Output Control & Safety Assurance](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C07-Model-Behavior.md) | This chapter addresses constraining, validating, and monitoring model outputs so that unsafe, malformed, or high-risk responses cannot reach users or downstream systems. | 13 |
| [C8 Memory, Embeddings & Vector Database Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md) | This chapter addresses securing the embeddings and vector stores that act as semi-persistent and persistent "memory" for AI systems through Retrieval-Augmented Generation (RAG). | 11 |
| [C9 Orchestration & Agentic Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md) | This chapter addresses ensuring autonomous and multi-agent systems execute only authorized, intended, and bounded actions. | 34 |
| [C10 Model Context Protocol (MCP) Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C10-MCP-Security.md) | This chapter addresses secure discovery, authentication, authorization, transport, and use of MCP-based tool and resource integrations. | 23 |
| [C11 Adversarial Robustness](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C11-Adversarial-Robustness.md) | This chapter addresses keeping AI systems reliable and abuse-resistant when facing evasion, inference, extraction, or poisoning attacks. | 17 |
| [C12 Monitoring, Logging & Anomaly Detection](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C12-Monitoring-and-Logging.md) | This chapter addresses real-time and forensic visibility into what the model and other AI components see, do, and return, so that AI-specific threats can be detected and triaged. | 21 |

Levels map to crosswalk tiers as Level 1 Foundational, Level 2 Hardening, Level 3 Advanced. Where an entry maps to requirements at several levels, the tier column below reports the level most of its requirements sit at.

---

## Quick-reference summary

| ID | Name | Severity | Primary AISVS Controls | Tier | Scope |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | C2.1, C10.4, C12.2 | Foundational | Both |
| LLM02 | Sensitive Information Disclosure | High | C5.2, C11.2, C8.2, C7.3, C1.1 | Hardening | Both |
| LLM03 | Supply Chain Vulnerabilities | High | C6.1, C4.1, C6.2, C3.1 | Foundational | Both |
| LLM04 | Data and Model Poisoning | Critical | C1.3, C1.1, C3.5, C12.5 | Hardening | Both |
| LLM05 | Insecure Output Handling | High | C7.1, C7.3, C9.3 | Foundational | Both |
| LLM06 | Excessive Agency | High | C9.2, C9.1, C9.3, C9.5, C9.6 | Foundational | Both |
| LLM07 | System Prompt Leakage | High | C7.3, C2.1, C9.5, C12.2, C11.3 | Hardening | Both |
| LLM08 | Vector and Embedding Weaknesses | Medium | C8.1, C8.2, C8.3 | Hardening | Both |
| LLM09 | Misinformation | Medium | C7.4, C7.2, C12.3, C11.1 | Hardening | Both |
| LLM10 | Unbounded Consumption | Medium | C9.1, C2.1, C11.2, C7.1, C12.2 | Foundational | Both |

---

## Target audience

| Role | Sections to prioritise |
|---|---|
| Security engineer | C2 Input Validation, C9 Orchestration and Agentic Security, C10 MCP Security |
| Developer | C7 Model Behavior and Output Control, C8 Memory and Embeddings, C5 Access Control |
| ML engineer | C1 Training Data, C3 Model Lifecycle, C11 Adversarial Robustness |
| Auditor | The whole standard. Every requirement is written as a verifiable test |
| Compliance and GRC | C1 Training Data, C6 Supply Chain, C12 Monitoring and Logging |
| Red teamer | C2 Input Validation, C11 Adversarial Robustness, C9 Orchestration |

---

## Detailed mappings

---

### LLM01 - Prompt Injection

AISVS treats prompt injection as an input validation problem with a dedicated chapter. C2.1 carries eight requirements covering normalization, encoding smuggling, classifier screening, instruction hierarchy and special-token handling, and C10.4 extends the same screening to MCP tool responses as an indirect injection path.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that all inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier,... | [2.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. Direct control: all inputs able to steer model behavior are treated as untrusted and screened by an injection ruleset or classifier, with flagged inputs blocked |
| Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inpu... | [2.1.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 2. Instruction hierarchy so system and developer messages keep precedence over user and other untrusted input, including after user text is processed |
| Verify that encoding and representation smuggling in inputs is detected and mitigated. Approved mitigations include canonicalization, strict schema... | [2.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. Encoding and representation smuggling defeated by canonicalization, strict schema validation, policy rejection or explicit marking |
| Verify that input normalization is applied before tokenization or embedding. | [2.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. Input normalization applied before tokenization or embedding, closing the pre-tokenizer bypass class |
| Verify that reserved special tokens are encoded as literal characters and cannot be injected into the model context. | [2.1.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 2. Reserved special tokens encoded as literals so control tokens cannot be injected into the model context |
| Verify that the system implements a character set restriction for all inputs. The restriction must use an allow-list approach that permits only cha... | [2.1.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. Character set restricted by allow-list to only explicitly required characters, removing the exotic-codepoint smuggling surface |
| Verify that the system can detect many-shot jailbreaking patterns. | [2.1.8](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 3. Many-shot jailbreaking pattern detection for long-context in-context-learning attacks |
| Verify that MCP tools/list and tools/call responses are screened for indirect prompt injection before being injected into the model context. | [10.4.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 1. Indirect injection path: MCP tools/list and tools/call responses screened before entering model context |
| Verify that the system detects and alerts on known jailbreak patterns, prompt injection attempts, and adversarial inputs. | [12.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c122-detection-and-alerting) | Level 1. Detection layer: known jailbreak patterns, injection attempts and adversarial inputs alerted on |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 2.1.3: Verify that all inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier, with flag...
- 2.1.2: Verify that encoding and representation smuggling in inputs is detected and mitigated. Approved mitigations include canonicalization, strict schema validatio...
- 2.1.1: Verify that input normalization is applied before tokenization or embedding.
- 2.1.5: Verify that the system implements a character set restriction for all inputs. The restriction must use an allow-list approach that permits only characters th...
- 10.4.2: Verify that MCP tools/list and tools/call responses are screened for indirect prompt injection before being injected into the model context.
- 12.2.1: Verify that the system detects and alerts on known jailbreak patterns, prompt injection attempts, and adversarial inputs.

**Tier 2 - Short-term (first 30 days):**
- 2.1.6: Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inputs, even a...
- 2.1.7: Verify that reserved special tokens are encoded as literal characters and cannot be injected into the model context.

**Tier 3 - Strategic:**
- 2.1.8: Verify that the system can detect many-shot jailbreaking patterns.

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI01, ASI02
- DSGAI: DSGAI01, DSGAI15, DSGAI12
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM02 - Sensitive Information Disclosure

AISVS splits disclosure across the retrieval boundary and the response boundary. C5.2 requires the end-user authorization context to be enforced at retrieval rather than the service account, and C7.3 plus C11.2 stop what does get generated from carrying data the requester may not receive.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive. | [5.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Post-inference filtering prevents responses containing data the requester is not authorized to receive |
| Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly ... | [5.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Retrieval pipelines enforce the end-user authorization context at each retrieval and assembly stage rather than the service account permissions |
| Verify that model-inferred sensitive attributes are not directly returned in outputs. | [11.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 1. Model-inferred sensitive attributes are not returned directly in outputs |
| Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped. | [8.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 1. Sensitive fields detected and masked, tokenized or dropped before embedding, so disclosure is prevented at the index rather than the response |
| Verify that output filters detect and block responses that disclose system prompt content or backend data. | [7.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 2. Output filters block responses disclosing system prompt content or backend data |
| Verify that training on sensitive datasets employs differentially-private optimization. | [11.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 2. Differentially-private optimization when training on sensitive datasets, limiting memorisation-driven disclosure |
| Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs). | [5.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Data classification labels propagate to embeddings, prompt caches and model outputs so downstream handling matches the source sensitivity |
| Verify that training data includes only features, attributes, and fields required for the model's stated purpose. | [1.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 1. Training data restricted to features required for the stated purpose, reducing what can be disclosed at all |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 11.2.1: Verify that model-inferred sensitive attributes are not directly returned in outputs.
- 8.2.1: Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped.
- 1.1.1: Verify that training data includes only features, attributes, and fields required for the model's stated purpose.

**Tier 2 - Short-term (first 30 days):**
- 5.2.4: Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive.
- 5.2.2: Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly stage, rat...
- 7.3.2: Verify that output filters detect and block responses that disclose system prompt content or backend data.
- 11.2.4: Verify that training on sensitive datasets employs differentially-private optimization.

**Tier 3 - Strategic:**
- 5.2.7: Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs).

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI03, ASI06, ASI02, ASI05
- DSGAI: DSGAI01, DSGAI10, DSGAI18, DSGAI07, DSGAI08, DSGAI06, DSGAI03, DSGAI05, DSGAI12, DSGAI16
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM03 - Supply Chain Vulnerabilities

AISVS treats the model artifact as the supply chain unit. C6 requires approved sources, malware scanning, integrity verification and a signed AI BOM, and C4.1.2 closes the deserialization path that turns a downloaded artifact into code execution.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that model weights, datasets, and fine-tuning adapters are downloaded only from approved sources. | [6.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 1. Model weights, datasets and fine-tuning adapters downloaded only from approved sources |
| Verify that models are scanned for malicious code before import. | [6.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 1. Models scanned for malicious code before import |
| Verify that model artifact loading enforces an explicit allow-list of serialization formats that do not permit arbitrary code execution during dese... | [4.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c41-ai-workload-sandboxing--validation) | Level 1. Model artifact loading restricted to an allow-list of serialization formats that cannot execute code on deserialization, the pickle class of supply chain RCE |
| Verify that every third-party model artifact can be integrity-verified. | [6.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 2. Every third-party model artifact is integrity-verifiable |
| Verify that every model artifact publishes a version-controlled, machine-readable AI BOM listing datasets, weights, licenses, and data-origin state... | [6.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c62-ai-bom--supply-chain-monitoring) | Level 1. Version-controlled machine-readable AI BOM listing datasets, weights, licenses and data-origin statements |
| Verify that AI BOMs are cryptographically signed before deployment. | [6.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c62-ai-bom--supply-chain-monitoring) | Level 2. AI BOMs cryptographically signed before deployment |
| Verify that all model artifacts (weights, configurations, tokenizers, base models, fine-tunes, adapters, and safety/policy models) are cryptographi... | [3.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c31-model-authorization--integrity) | Level 2. Weights, configurations, tokenizers, base models, fine-tunes, adapters and safety models signed by authorized entities |
| Verify that models pass a behavioral acceptance test suite before being promoted to any non-development environment. | [6.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 2. Behavioral acceptance test suite passed before promotion beyond development, catching backdoors that signature checks cannot |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 6.1.2: Verify that model weights, datasets, and fine-tuning adapters are downloaded only from approved sources.
- 6.1.1: Verify that models are scanned for malicious code before import.
- 4.1.2: Verify that model artifact loading enforces an explicit allow-list of serialization formats that do not permit arbitrary code execution during deserialization.
- 6.2.1: Verify that every model artifact publishes a version-controlled, machine-readable AI BOM listing datasets, weights, licenses, and data-origin statements.

**Tier 2 - Short-term (first 30 days):**
- 6.1.3: Verify that every third-party model artifact can be integrity-verified.
- 6.2.2: Verify that AI BOMs are cryptographically signed before deployment.
- 3.1.2: Verify that all model artifacts (weights, configurations, tokenizers, base models, fine-tunes, adapters, and safety/policy models) are cryptographically sign...
- 6.1.4: Verify that models pass a behavioral acceptance test suite before being promoted to any non-development environment.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI04, ASI07, ASI06
- DSGAI: DSGAI04, DSGAI03, DSGAI06, DSGAI16, DSGAI17, DSGAI05
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM04 - Data and Model Poisoning

AISVS puts poisoning defense in the training data chapter. C1.3 requires poisoning detection in training and fine-tuning pipelines including the clean-label case, and C1.1 plus C12.5 give the integrity monitoring and lineage needed to attribute a poisoned corpus after the fact.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corru... | [1.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Training and fine-tuning pipelines implement poisoning detection for deliberate poisoning and unintentional corruption |
| Verify that integrity monitoring is applied to guard against unauthorized modifications or corruption of training data. | [1.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Integrity monitoring guards training data against unauthorized modification or corruption |
| Verify that data integrity is provided when training data is stored and transferred. | [1.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Data integrity provided for training data in storage and in transit |
| Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, int... | [1.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Current inventory of every training-data source with origin, responsible party, license, collection method, use constraints and processing history |
| Verify that disallowed content is detected and removed before training. | [1.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Disallowed content detected and removed before training |
| Verify that defenses against clean-label poisoning attacks are implemented. | [1.3.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 3. Clean-label poisoning defenses, the attack class that survives label inspection |
| Verify that in multi-stage fine-tuning pipelines, each stage's output is integrity-verified before it is consumed by the next stage. | [3.5.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c35-pipeline-fine-tuning) | Level 3. Each stage output integrity-verified before the next stage consumes it in multi-stage fine-tuning |
| Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges. | [12.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 1. Dataset lineage records each dataset and its components including transformations, augmentations and merges, enabling post-hoc poisoning attribution |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 12.5.1: Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges.

**Tier 2 - Short-term (first 30 days):**
- 1.3.1: Verify that training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corruption in t...
- 1.1.4: Verify that integrity monitoring is applied to guard against unauthorized modifications or corruption of training data.
- 1.1.3: Verify that data integrity is provided when training data is stored and transferred.
- 1.1.2: Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, intended use ...
- 1.3.4: Verify that disallowed content is detected and removed before training.

**Tier 3 - Strategic:**
- 1.3.5: Verify that defenses against clean-label poisoning attacks are implemented.
- 3.5.3: Verify that in multi-stage fine-tuning pipelines, each stage's output is integrity-verified before it is consumed by the next stage.

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI06, ASI08
- DSGAI: DSGAI04, DSGAI21, DSGAI03, DSGAI02, DSGAI09, DSGAI17
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM05 - Insecure Output Handling

AISVS treats model output as untrusted input to whatever consumes it. C7.1 requires schema validation and rejection of non-conforming output, and C7.3.3 blocks the outbound request path that turns rendered output into exfiltration.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that the application validates all model outputs against a defined schema and rejects any output that does not match. | [7.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c71-output-format-enforcement) | Level 1. All model outputs validated against a defined schema, non-matching output rejected |
| Verify that model-generated output is bounded by length limits and termination controls. | [7.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c71-output-format-enforcement) | Level 1. Model-generated output bounded by length limits and termination controls |
| Verify that model-generated output is prevented from triggering outbound requests. | [7.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 2. Model-generated output prevented from triggering outbound requests |
| Verify that tool outputs are validated against schemas. | [9.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Tool outputs validated against schemas before the agent consumes them |
| Verify that there is architectural separation between processing of untrusted tool outputs and agent operations. | [9.3.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Architectural separation between processing of untrusted tool outputs and agent operations |
| Verify that model outputs are checked for hidden, encoded, or misleading content created through homoglyphs, formatting, metadata, or structured fi... | [7.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 3. Outputs checked for hidden, encoded or misleading content via homoglyphs, formatting, metadata or structured fields |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 7.1.1: Verify that the application validates all model outputs against a defined schema and rejects any output that does not match.
- 7.1.2: Verify that model-generated output is bounded by length limits and termination controls.
- 9.3.2: Verify that tool outputs are validated against schemas.

**Tier 2 - Short-term (first 30 days):**
- 7.3.3: Verify that model-generated output is prevented from triggering outbound requests.
- 9.3.6: Verify that there is architectural separation between processing of untrusted tool outputs and agent operations.

**Tier 3 - Strategic:**
- 7.3.4: Verify that model outputs are checked for hidden, encoded, or misleading content created through homoglyphs, formatting, metadata, or structured fields.

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI02, ASI05, ASI04, ASI10
- DSGAI: DSGAI05, DSGAI12, DSGAI04, DSGAI19
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM06 - Excessive Agency

AISVS bounds agency with runtime enforcement rather than prompt instructions. C9.2 gates high-impact and irreversible actions behind verified human approval, C9.5.3 requires access control decisions to be made by a policy engine and never by the model, and C9.1 caps budgets.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that the agent runtime blocks execution of privileged, high-impact, or irreversible actions until explicit human approval is received and ve... | [9.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 1. Agent runtime blocks privileged, high-impact or irreversible actions until explicit human approval is received and verified |
| Verify that per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime. | [9.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 1. Per-execution budgets for recursion depth, token use and monetary spend configured and enforced by the runtime |
| Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations. | [9.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Each tool or plugin executes in a least-privilege sandbox or is otherwise isolated from model operations |
| Verify that all access control decisions are enforced by application logic or a policy engine, never by the AI model itself. | [9.5.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. All access control decisions enforced by application logic or a policy engine, never by the model itself |
| Verify that a manual kill-switch mechanism exists to immediately halt AI model inference and outputs. | [9.6.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c96-shutdown-and-graceful-degradation) | Level 1. Manual kill-switch to immediately halt model inference and outputs |
| Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and w... | [9.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Fine-grained runtime policy restricting which tools an agent may invoke and which parameter values it may supply |
| Verify that each high-impact action has a trusted reversibility classification, such as read-only, reversible, externally reversible, or irreversible. | [9.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. Each high-impact action carries a trusted reversibility classification |
| Verify that the agent runtime enforces reversibility classifications by blocking, requiring approval, or restricting actions based on their impact ... | [9.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. Runtime enforces reversibility classifications by blocking, requiring approval or restricting the action |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.2.1: Verify that the agent runtime blocks execution of privileged, high-impact, or irreversible actions until explicit human approval is received and verified.
- 9.1.2: Verify that per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime.
- 9.3.1: Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations.
- 9.6.1: Verify that a manual kill-switch mechanism exists to immediately halt AI model inference and outputs.

**Tier 2 - Short-term (first 30 days):**
- 9.5.3: Verify that all access control decisions are enforced by application logic or a policy engine, never by the AI model itself.
- 9.5.1: Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and which param...
- 9.2.3: Verify that each high-impact action has a trusted reversibility classification, such as read-only, reversible, externally reversible, or irreversible.
- 9.2.4: Verify that the agent runtime enforces reversibility classifications by blocking, requiring approval, or restricting actions based on their impact and abilit...

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI01, ASI02, ASI10, ASI09, ASI03, ASI07
- DSGAI: DSGAI06, DSGAI16, DSGAI12, DSGAI02, DSGAI07
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM07 - System Prompt Leakage

AISVS handles prompt leakage as an output filtering and secret hygiene problem. C7.3.2 blocks responses disclosing system prompt or backend content, and C9.5.4 keeps credentials out of the observable context so a leaked prompt is not also a leaked secret.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that output filters detect and block responses that disclose system prompt content or backend data. | [7.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 2. Output filters detect and block responses that disclose system prompt content or backend data |
| Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inpu... | [2.1.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 2. Instruction hierarchy resists the override-then-reveal extraction pattern |
| Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context wi... | [9.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Secrets and credentials kept out of the model observable context including context window, system prompts and tool call parameters, so a leaked prompt is not a leaked credential |
| Verify that custom rules detect AI-specific threat patterns for coordinated jailbreak attempts, prompt injection, and system prompt extraction atte... | [12.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c122-detection-and-alerting) | Level 2. Custom rules detect coordinated jailbreak attempts, injection and system prompt extraction attempts |
| Verify that query-pattern analysis feeds an extraction-attempt detector. | [11.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c113-model-extraction-defense) | Level 1. Query-pattern analysis feeds an extraction-attempt detector, covering iterative prompt reconstruction |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 11.3.1: Verify that query-pattern analysis feeds an extraction-attempt detector.

**Tier 2 - Short-term (first 30 days):**
- 7.3.2: Verify that output filters detect and block responses that disclose system prompt content or backend data.
- 2.1.6: Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inputs, even a...
- 9.5.4: Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context window, syst...
- 12.2.3: Verify that custom rules detect AI-specific threat patterns for coordinated jailbreak attempts, prompt injection, and system prompt extraction attempts.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM01
- Agentic: ASI01, ASI02
- DSGAI: DSGAI15, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM08 - Vector and Embedding Weaknesses

AISVS gives embeddings and vector stores their own chapter. C8.1 covers tenant namespace isolation, metadata immutability and scope-constrained retrieval, and C8.2 covers sanitization before embedding plus detection of vectors crafted to manipulate retrieval.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions. | [8.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 1. Vector identifiers and namespaces enforce per-tenant uniqueness and prevent cross-tenant collisions |
| Verify that retrieval operations enforce scope constraints. | [8.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 2. Retrieval operations enforce scope constraints |
| Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped. | [8.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 1. Sensitive fields detected before embedding and masked, tokenized or dropped |
| Verify that document metadata tags are immutable after the initial write. | [8.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 2. Document metadata tags immutable after initial write, blocking post-hoc retrieval manipulation |
| Verify that vectors that fall outside normal clustering patterns are flagged and quarantined before entering production indices. | [8.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 2. Vectors outside normal clustering patterns flagged and quarantined before entering production indices |
| Verify that expired vectors are excluded from retrieval results. | [8.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Expired vectors excluded from retrieval results |
| Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization. | [8.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 3. Content crafted to manipulate retrieval results detected and rejected or quarantined before vectorization |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 8.1.1: Verify that vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions.
- 8.2.1: Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped.

**Tier 2 - Short-term (first 30 days):**
- 8.1.3: Verify that retrieval operations enforce scope constraints.
- 8.1.2: Verify that document metadata tags are immutable after the initial write.
- 8.2.2: Verify that vectors that fall outside normal clustering patterns are flagged and quarantined before entering production indices.
- 8.3.1: Verify that expired vectors are excluded from retrieval results.

**Tier 3 - Strategic:**
- 8.2.4: Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization.

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI06
- DSGAI: DSGAI13, DSGAI18, DSGAI08, DSGAI09, DSGAI04, DSGAI05
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM09 - Misinformation

AISVS attacks misinformation through provenance and confidence. C7.4 requires RAG attribution derived from retrieval metadata rather than generated by the model, and C7.2 plus C12.3 require confidence estimation, fallback behaviour and hallucination rate tracking over time.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that responses generated using retrieval-augmented generation (RAG) include attribution to the source documents. | [7.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c74-source-attribution--citation-integrity) | Level 1. RAG responses include attribution to the source documents |
| Verify that RAG attributions are derived from retrieval metadata and are not generated by the model, so provenance cannot be fabricated. | [7.4.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c74-source-attribution--citation-integrity) | Level 1. RAG attributions derived from retrieval metadata rather than generated by the model, so provenance cannot be fabricated |
| Verify that the system assesses the reliability of generated answers using a confidence estimation method. | [7.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c72-hallucination-detection--mitigation) | Level 2. Reliability of generated answers assessed using a confidence estimation method |
| Verify that the application automatically blocks answers or switches to a fallback message if the confidence score drops below a defined threshold. | [7.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c72-hallucination-detection--mitigation) | Level 2. Answers blocked or a fallback message returned when the confidence score falls below a defined threshold |
| Verify that claims in a RAG response can be traced to the retrieved chunk. | [7.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c74-source-attribution--citation-integrity) | Level 2. Claims in a RAG response traceable to the retrieved chunk |
| Verify that hallucination detection monitors identify and flag model outputs that contain factually incorrect, inconsistent, or fabricated informat... | [12.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c123-model-data-and-performance-drift-detection) | Level 2. Hallucination detection monitors flag factually incorrect, inconsistent or fabricated output |
| Verify that hallucination rates are tracked as continuous time-series metrics to enable trend analysis and detection of sustained model degradation. | [12.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c123-model-data-and-performance-drift-detection) | Level 2. Hallucination rates tracked as continuous time-series metrics to detect sustained degradation |
| Verify that for responses classified as high-risk by policy, the system performs an additional verification step. | [7.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c72-hallucination-detection--mitigation) | Level 3. Additional verification step for responses classified as high-risk by policy |
| Verify that a version-controlled alignment test suite is run on every model update or release. | [11.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c111-model-alignment-safety-and-robustness-testing-and-training) | Level 1. Version-controlled alignment test suite run on every model update or release, catching factuality regressions before they ship |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 7.4.1: Verify that responses generated using retrieval-augmented generation (RAG) include attribution to the source documents.
- 7.4.2: Verify that RAG attributions are derived from retrieval metadata and are not generated by the model, so provenance cannot be fabricated.
- 11.1.2: Verify that a version-controlled alignment test suite is run on every model update or release.

**Tier 2 - Short-term (first 30 days):**
- 7.2.1: Verify that the system assesses the reliability of generated answers using a confidence estimation method.
- 7.2.2: Verify that the application automatically blocks answers or switches to a fallback message if the confidence score drops below a defined threshold.
- 7.4.3: Verify that claims in a RAG response can be traced to the retrieved chunk.
- 12.3.2: Verify that hallucination detection monitors identify and flag model outputs that contain factually incorrect, inconsistent, or fabricated information.
- 12.3.3: Verify that hallucination rates are tracked as continuous time-series metrics to enable trend analysis and detection of sustained model degradation.

**Tier 3 - Strategic:**
- 7.2.3: Verify that for responses classified as high-risk by policy, the system performs an additional verification step.

#### Cross-references

- LLM Top 10: N/A
- Agentic: ASI09
- DSGAI: DSGAI21, DSGAI10, DSGAI17
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### LLM10 - Unbounded Consumption

AISVS bounds consumption at the runtime rather than the gateway. C9.1 requires per-tool quotas and per-execution budgets covering recursion depth, tokens and monetary spend, and C11.2.2 requires rate limits sized to the threat model rather than a generic API throttle.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime. | [9.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 1. Per-execution budgets for max recursion depth, token use and monetary spend enforced by the runtime |
| Verify that per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced. | [9.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 1. Per-tool quotas and timeouts for CPU, memory, disk, egress and execution time |
| Verify that input length controls prevent content from exceeding the context window. The controls must reject inputs that exceed token limits rathe... | [2.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. Input length controls reject inputs exceeding token limits rather than truncating them |
| Verify that inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API ... | [11.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 1. Per-principal and global rate limits sized to the threat model rather than as a generic API throttle |
| Verify that model-generated output is bounded by length limits and termination controls. | [7.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c71-output-format-enforcement) | Level 1. Output bounded by length limits and termination controls, capping runaway generation |
| Verify that token usage is tracked at granular attribution levels including per user, per session, per feature endpoint, and per team or workspace. | [12.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c122-detection-and-alerting) | Level 2. Token usage tracked per user, session, feature endpoint and team so cost abuse is attributable |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.1.2: Verify that per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime.
- 9.1.1: Verify that per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced.
- 2.1.4: Verify that input length controls prevent content from exceeding the context window. The controls must reject inputs that exceed token limits rather than tru...
- 11.2.2: Verify that inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API throttle.
- 7.1.2: Verify that model-generated output is bounded by length limits and termination controls.

**Tier 2 - Short-term (first 30 days):**
- 12.2.5: Verify that token usage is tracked at granular attribution levels including per user, per session, per feature endpoint, and per team or workspace.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM01, LLM06, LLM07, LLM02, LLM05, LLM03, LLM04, LLM08, LLM09
- Agentic: ASI08, ASI10
- DSGAI: DSGAI17
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

## Implementation priority table

| Priority | AISVS components | Entries addressed |
|---|---|---|
| P1 - Pre-production gate | All Level 1 requirements | LLM01, LLM02, LLM03, LLM04, LLM05, LLM06, LLM07, LLM08, LLM09, LLM10 |
| P2 - First 30 days | All Level 2 requirements | LLM01, LLM02, LLM03, LLM04, LLM05, LLM06, LLM07, LLM08, LLM09, LLM10 |
| P3 - Programme maturity | All Level 3 requirements | LLM01, LLM02, LLM04, LLM05, LLM08, LLM09 |

---

## References

- [OWASP AISVS project page](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/)
- [OWASP AISVS 1.0 frozen text](https://github.com/OWASP/AISVS/tree/main/1.0/en)
- [OWASP Top 10 for LLM Applications 2025 - OWASP](https://genai.owasp.org/llm-top-10/)
- [shared/TEMPLATE.md](../shared/TEMPLATE.md)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-28 | Initial release - full mapping of LLM01-LLM10 to OWASP AISVS 1.0 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) - maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
