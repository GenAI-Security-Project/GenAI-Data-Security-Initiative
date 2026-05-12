<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01-DSGAI21)
  Framework   : OWASP Non-Human Identities (NHI) Top 10
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × OWASP NHI Top 10

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [OWASP Non-Human Identities (NHI) Top 10](https://owasp.org/www-project-non-human-identities-top-10/) —
the framework for securing machine identities including service
accounts, API keys, OAuth tokens, certificates, and pipeline credentials.

---

## Why NHI matters for GenAI data security

The DSGAI taxonomy is fundamentally about data: how GenAI data flows
are configured, accessed, protected, and governed. Every data flow
requires credentials — NHI. Training pipelines, embedding stores,
RAG retrieval systems, tool integrations, inference APIs, and audit
logging systems all authenticate with Non-Human Identities.

The NHI risks that most directly amplify DSGAI vulnerabilities:

- **Training data poisoning (DSGAI02):** possible only when pipeline
  credentials have write access to training stores (NHI-5).
- **RAG corpus manipulation (DSGAI09):** possible only when corpus
  write credentials are insufficiently protected (NHI-5, NHI-6, NHI-7).
- **Data leakage in retrieval (DSGAI08):** enabled when embedding
  store service accounts have cross-tenant read scope (NHI-5).
- **Third-party data dependencies (DSGAI16):** third-party data
  source credentials are rarely reviewed for scope (NHI-3).
- **Data pipeline security (DSGAI04):** pipeline service accounts
  frequently hold over-broad access to all pipeline stages (NHI-5, NHI-9).

NHI programme maturity is a prerequisite for DSGAI risk reduction —
you cannot secure GenAI data flows without securing the credentials
that access them.

---

## OWASP NHI Top 10 reference

| NHI Entry | Name | Description |
|---|---|---|
| NHI-1 | Improper Offboarding | NHIs not revoked when systems decommission or integrations end |
| NHI-2 | Secret Leakage | Credentials exposed in code, logs, config, model outputs |
| NHI-3 | Vulnerable Third-Party NHI | Third-party tokens and identities with excessive permissions |
| NHI-4 | Insecure Authentication | Weak or missing authentication for machine-to-machine communication |
| NHI-5 | Over-Privileged NHI | NHIs with more permissions than required |
| NHI-6 | Insecure Credential Storage | Credentials stored insecurely — plaintext, weak encryption |
| NHI-7 | Long-Lived Credentials | Credentials without rotation, expiry, or revocation |
| NHI-8 | Environment Isolation Failure | Credentials shared across environments |
| NHI-9 | NHI Reuse | Same credentials used across multiple services or data flows |
| NHI-10 | Human Use of NHI | Humans using machine credentials — no attribution |

---

## Quick-reference summary

| DSGAI ID | Name | Severity | Primary NHI Entries | Tier |
|---|---|---|---|---|
| DSGAI01 | Prompt Injection via Data Channels | Critical | NHI-5, NHI-7 (blast radius) | Foundational–Advanced |
| DSGAI02 | Training Data Poisoning | Critical | NHI-5, NHI-6, NHI-7 (write access) | Hardening–Advanced |
| DSGAI03 | Sensitive Data in Training Sets | High | NHI-5, NHI-2 (pipeline access) | Foundational–Hardening |
| DSGAI04 | Insecure Data Pipelines | High | NHI-4, NHI-5, NHI-9 | Foundational–Hardening |
| DSGAI05 | Guardrail Circumvention | High | NHI-5 (bypass via pipeline access) | Hardening–Advanced |
| DSGAI06 | Unintended Data Disclosure | High | NHI-2, NHI-5 | Foundational–Hardening |
| DSGAI07 | Excessive Data Access | High | NHI-5, NHI-7, NHI-9 | Foundational–Hardening |
| DSGAI08 | Data Leakage in Retrieval | High | NHI-5, NHI-4, NHI-9 | Hardening–Advanced |
| DSGAI09 | RAG Corpus Manipulation | Critical | NHI-5, NHI-6, NHI-7 (write access) | Hardening–Advanced |
| DSGAI10 | Context Window Poisoning | High | NHI-5 (data feed access) | Hardening–Advanced |
| DSGAI11 | Session Persistence Attacks | High | NHI-5, NHI-6 (session store) | Hardening–Advanced |
| DSGAI12 | Model Inversion and Extraction | High | NHI-5, NHI-7 (API access) | Hardening–Advanced |
| DSGAI13 | Data Leakage through Tool Integration | High | NHI-3, NHI-5, NHI-9 | Foundational–Hardening |
| DSGAI14 | Model Weight Theft | High | NHI-5, NHI-6 (model storage) | Hardening–Advanced |
| DSGAI15 | Inference Data Exposure | High | NHI-5, NHI-2 (log access) | Foundational–Hardening |
| DSGAI16 | Third-Party Data Dependencies | High | NHI-3, NHI-8, NHI-2 | Foundational–Hardening |
| DSGAI17 | Model Supply Chain Risks | High | NHI-3, NHI-8, NHI-2 | Foundational–Hardening |
| DSGAI18 | Data Retention and Deletion Failures | Medium | NHI-5, NHI-10 | Foundational–Hardening |
| DSGAI19 | Cascading Data Failures | High | NHI-9, NHI-5 (cascade amplifiers) | Hardening–Advanced |
| DSGAI20 | Regulatory Non-Compliance | High | NHI-10, NHI-2 (attribution) | Foundational–Hardening |
| DSGAI21 | Data Provenance and Lineage Failures | Medium | NHI-10 (attribution), NHI-2 | Foundational–Hardening |

---

## Audience tags

- **Identity and access management (IAM) team** — full file
- **Data engineer / ML engineer** — DSGAI02, DSGAI04, DSGAI09 — pipeline NHI
- **Security engineer** — NHI-2/NHI-5/NHI-7 most actionable
- **Platform engineer** — NHI-4/NHI-8/NHI-9 for infrastructure design
- **Auditor** — NHI-1/NHI-10 for attribution and offboarding evidence

---

## Detailed mappings

---

### DSGAI01 — Prompt Injection via Data Channels

NHI amplifies injection: a system where data channels carry injected
content is more dangerous when the processing pipeline holds
over-privileged credentials. The injected instruction can only
cause damage proportional to the credential scope of the pipeline.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Injection blast radius limited only by credential scope | Apply least-privilege to all data pipeline credentials |
| NHI-7 Long-Lived Credentials | Injected actions can use pipeline tokens for extended period | Short-lived tokens for all data pipeline service accounts |

**Mitigations:**
- NHI-5: audit and reduce scope of all data pipeline credentials
- NHI-7: automate rotation of all pipeline service account credentials
- Minimum scope per data channel: read-only credentials for data consumption

---

### DSGAI02 — Training Data Poisoning

Credential access is the attack path for training data poisoning.
Without write credentials to training data stores, external poisoning
is not possible. NHI-5 and NHI-6 are the enabling conditions.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Write access to training data stores enables poisoning | Separate read and write credentials; write requires MFA |
| NHI-6 Insecure Credential Storage | Training pipeline credentials in plaintext config | Vault all training pipeline credentials |
| NHI-7 Long-Lived Credentials | Long-lived write credentials create persistent poisoning window | Short-lived write tokens; rotate frequently |

**Mitigations:**
- NHI-5: read-only credentials for data consumption; separate write credentials with MFA
- NHI-6: vault all training pipeline credentials; no plaintext in config
- NHI-7: automated rotation for all training data write credentials
- Audit who has current write access to training data stores

---

### DSGAI03 — Sensitive Data in Training Sets

Pipeline credentials with broad data access enable ingestion of
sensitive data that would be excluded with properly scoped credentials.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Pipeline service account with access to sensitive data stores | Scope pipeline credentials to approved data sources only |
| NHI-2 Secret Leakage | Credentials embedded in config files include sensitive data source access | Audit config files for embedded credentials |

**Mitigations:**
- NHI-5: pipeline credentials scoped to approved training data sources only
- NHI-2: automated secret scanning of all pipeline config files
- Document and justify every data source in training pipeline

---

### DSGAI04 — Insecure Data Pipelines

Pipeline authentication gaps are NHI problems: unauthenticated
pipeline connections (NHI-4), shared credentials across pipeline
stages (NHI-9), and environment isolation failures (NHI-8) are
the structural causes of insecure data pipelines.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-4 Insecure Authentication | Unauthenticated connections between pipeline stages | Require mTLS or token auth for all pipeline connections |
| NHI-5 Over-Privileged NHI | Pipeline service account with access to all stages | Per-stage credentials with minimum scope |
| NHI-9 NHI Reuse | Same credential used for multiple pipeline stages | Separate credentials per stage |

**Mitigations:**
- NHI-4: mTLS or token authentication for all pipeline stage connections
- NHI-9: separate service account per pipeline stage
- NHI-5: minimum scope per stage — each stage accesses only its declared data
- NHI-8: environment isolation — development pipeline credentials differ from production

---

### DSGAI05 — Guardrail Circumvention

Administrative access to guardrail configuration — held by over-privileged
service accounts — enables disabling or bypassing safety controls.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Service account with guardrail configuration write access | Minimum scope; no service account has guardrail disable capability |

**Mitigations:**
- NHI-5: no service account holds guardrail configuration write access in production
- Guardrail configuration changes require human authentication and MFA
- Log all guardrail configuration access

---

### DSGAI06 — Unintended Data Disclosure

Credentials appearing in model outputs (NHI-2) or over-broad service
account access to sensitive data stores (NHI-5) enable disclosure.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-2 Secret Leakage | Credentials embedded in model outputs or training data surface in responses | Output scanning for credential patterns |
| NHI-5 Over-Privileged NHI | Over-broad retrieval credentials return data beyond user entitlement | Minimum scope for retrieval service accounts |

**Mitigations:**
- NHI-2: automated credential pattern detection in output pipeline
- NHI-5: per-user retrieval credentials or query-scoped access only
- Secret scanning in all data sources that feed the model

---

### DSGAI07 — Excessive Data Access

Data access scope is a direct function of credential scope. This
entry is the DSGAI expression of NHI-5 — it describes what happens
when NHI-5 is not remediated.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | GenAI system service account has access to more data than declared function requires | Audit and reduce credential scope per system component |
| NHI-7 Long-Lived Credentials | Long-lived credentials maintain excessive access indefinitely | Rotate or replace with short-lived tokens |
| NHI-9 NHI Reuse | Same data access credential used across multiple GenAI system functions | Separate credentials per function |

**Mitigations:**
- NHI-5: audit all GenAI system data access credentials; reduce to minimum
- NHI-7: JIT short-lived tokens for data access (see RECIPES.md)
- NHI-9: separate credential per GenAI system component
- Quarterly data access credential review

---

### DSGAI08 — Data Leakage in Retrieval

Cross-tenant retrieval leakage is enabled by embedding store service
accounts with cross-tenant read scope (NHI-5) or unauthenticated
embedding store connections (NHI-4).

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Embedding store service account with cross-tenant read access | Per-tenant credentials or row-level security with minimum scope |
| NHI-4 Insecure Authentication | Unauthenticated embedding store access | Require authentication for all vector database connections |
| NHI-9 NHI Reuse | Same embedding store credential used for multiple tenants | Separate credentials per tenant or use row-level security |

**Mitigations:**
- NHI-5: per-tenant embedding store credentials or fine-grained access controls
- NHI-4: mTLS or token authentication for all embedding store connections
- NHI-9: tenant isolation via separate credentials or RBAC

---

### DSGAI09 — RAG Corpus Manipulation

The most critical DSGAI entry for NHI. Corpus manipulation requires
write access to the corpus store. Without write credentials, most
corpus manipulation attacks are not possible. NHI-5/NHI-6/NHI-7
are the enabling conditions.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Corpus write access held by service accounts that do not need it | Separate read and write credentials; write accounts require MFA |
| NHI-6 Insecure Credential Storage | Corpus write credentials in plaintext config | Vault all corpus write credentials |
| NHI-7 Long-Lived Credentials | Long-lived corpus write credentials persist beyond need | Rotate corpus write credentials; implement short-lived write pattern |

**Mitigations (highest priority):**
- NHI-5: read-only credentials for inference-time corpus access; write credentials separate and MFA-protected
- NHI-6: vault all corpus write credentials; no plaintext in deployment config
- NHI-7: automated rotation for all corpus write credentials
- Audit who holds current corpus write credentials; remove any unnecessary access

---

### DSGAI10 — Context Window Poisoning

Data feeds contributing to context window require authenticated,
minimum-scope credentials. Over-privileged data feed credentials
expand the attack surface for context poisoning.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Data feed service accounts with access to sensitive data that should not enter context | Scope data feed credentials to approved data only |

**Mitigations:**
- NHI-5: credentials for each data feed scoped to the data sources approved for context assembly
- Audit all data sources contributing to context window
- Separate credentials per data feed

---

### DSGAI11 — Session Persistence Attacks

Session store access credentials determine who can read or write
session data. Over-broad session store credentials (NHI-5) or
insecurely stored session store access keys (NHI-6) enable
cross-session attacks.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Session store service account with cross-user read/write access | Per-user session store access controls |
| NHI-6 Insecure Credential Storage | Session store access credentials in plaintext | Vault session store credentials |

**Mitigations:**
- NHI-5: enforce per-user session isolation at credential level
- NHI-6: vault all session store credentials
- Session store credentials have minimum scope: one user context, no cross-session access

---

### DSGAI12 — Model Inversion and Extraction

Extraction attacks succeed at scale when API credentials have no
effective rate limiting. Long-lived, high-quota API credentials
(NHI-7) and over-privileged inference API access (NHI-5) amplify
extraction attack surface.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | API credentials with high quota enabling systematic extraction | Per-user quotas; minimum default quota |
| NHI-7 Long-Lived Credentials | Long-lived inference API credentials enable sustained extraction campaigns | Rotate API credentials; implement per-session tokens |

**Mitigations:**
- NHI-5: per-user quota limits; no credential class has unlimited inference access
- NHI-7: implement per-session inference tokens; rotate API credentials regularly
- Monitor for systematic query patterns per credential

---

### DSGAI13 — Data Leakage through Tool Integration

Third-party tool credentials (NHI-3) and shared tool credentials
(NHI-9) create data leakage paths via tool API responses.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-3 Vulnerable Third-Party NHI | Third-party tool credentials with excessive data access | Review all third-party tool credentials; reduce to minimum scope |
| NHI-5 Over-Privileged NHI | Tool integration credentials with broad data access | Minimum scope per tool integration |
| NHI-9 NHI Reuse | Same credential used across multiple tool integrations | Separate credentials per tool |

**Mitigations:**
- NHI-3: assess and reduce scope of all third-party tool credentials
- NHI-9: separate credentials per tool integration
- NHI-5: data minimisation enforced at credential level — credentials cannot access data beyond declared function

---

### DSGAI14 — Model Weight Theft

Model weight storage credentials determine who can exfiltrate
proprietary models. NHI-5 and NHI-6 are the direct enabling
conditions for weight theft.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Model storage service account with read access from unexpected paths | Minimum scope: only authorised inference service can read model weights |
| NHI-6 Insecure Credential Storage | Model storage credentials in plaintext config | Vault all model storage credentials |

**Mitigations:**
- NHI-5: model weight read access restricted to authorised inference service identity only
- NHI-6: vault all model storage access credentials
- Alert on any model weight access from unexpected service identity

---

### DSGAI15 — Inference Data Exposure

Inference log credentials determine who can access submitted inputs
and generated outputs. NHI-5 (over-broad log access) and NHI-2
(credential leakage into logs) are the primary NHI vectors.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Inference log service account with broad read access | Minimum scope: only authorised audit function can read inference logs |
| NHI-2 Secret Leakage | Service account credentials embedded in inference log entries | Scan and scrub credentials from inference logs |

**Mitigations:**
- NHI-5: inference log access restricted to authorised audit identity
- NHI-2: credential scrubbing in inference log pipeline
- Log access audit: alert on unexpected read of inference logs

---

### DSGAI16 — Third-Party Data Dependencies

Third-party data source credentials are NHI-3 by definition —
external credentials held by the organisation on behalf of a
third-party relationship, often with excessive scope.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-3 Vulnerable Third-Party NHI | Third-party data source API keys with excessive scope | Review all third-party credentials; reduce to minimum |
| NHI-8 Environment Isolation Failure | Third-party development credentials used in production | Enforce environment isolation for third-party credentials |
| NHI-2 Secret Leakage | Third-party credentials embedded in shared config | Vault all third-party data source credentials |

**Mitigations:**
- NHI-3: review and reduce scope of all third-party data source credentials
- NHI-8: separate third-party credentials per environment
- NHI-2: vault all third-party credentials; automated secret scanning in config

---

### DSGAI17 — Model Supply Chain Risks

Model provider credentials, model registry tokens, and ML framework
access are third-party NHIs with security implications if compromised.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-3 Vulnerable Third-Party NHI | Model provider API keys with excessive access to model versions | Review and scope all model provider credentials |
| NHI-8 Environment Isolation Failure | Same model registry token used across dev/staging/production | Separate credentials per environment |
| NHI-2 Secret Leakage | Model provider credentials in pipeline config | Vault all model provider credentials |

**Mitigations:**
- NHI-3: assess and reduce scope of all model provider credentials
- NHI-8: separate credentials per environment and model version
- NHI-2: vault all model supply chain credentials; automated secret scanning

---

### DSGAI18 — Data Retention and Deletion Failures

Retention and deletion operations require appropriate credentials.
NHI-10 (human use of machine credentials) destroys the attribution
needed to prove compliance with deletion obligations.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Service account with access to retained data beyond declared function | Minimum scope for data access credentials |
| NHI-10 Human Use of NHI | Humans using machine credentials for data deletion — no audit trail | Enforce human identity for all compliance operations |

**Mitigations:**
- NHI-10: all compliance operations (deletion, access review) require human identity, not machine credential
- NHI-5: data access credentials scoped to minimum required for each retention period
- Audit trail of all deletion operations with human attribution

---

### DSGAI19 — Cascading Data Failures

Credential reuse (NHI-9) across pipeline stages is a cascade amplifier:
one compromised credential can affect all stages sharing it. Over-privileged
credentials amplify the blast radius of any single-stage failure.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-9 NHI Reuse | Shared credential across pipeline stages — one failure affects all | Separate credentials per pipeline stage |
| NHI-5 Over-Privileged NHI | Single credential covering multiple pipeline stages amplifies cascade | Per-stage minimum scope credentials |

**Mitigations:**
- NHI-9: separate credentials per pipeline stage — stage failure cannot cascade via shared credential
- NHI-5: minimum scope per stage limits what a compromised stage can affect
- Circuit breaker: pipeline stage isolation enforced at credential level

---

### DSGAI20 — Regulatory Non-Compliance in Data Use

Attribution is required for compliance. NHI-10 (human use of machine
credentials) destroys attribution needed for GDPR, CCPA, and other
regulatory audit trails.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-10 Human Use of NHI | Humans using machine credentials — no attribution for compliance evidence | Enforce human identity for all regulated data operations |
| NHI-2 Secret Leakage | Compliance audit credentials leaked — tampering with evidence possible | Protect audit credential integrity |

**Mitigations:**
- NHI-10: all regulated data operations require human identity with MFA
- NHI-2: protect compliance audit system credentials as high-sensitivity NHI
- Separate credentials for compliance vs operational data access

---

### DSGAI21 — Data Provenance and Lineage Failures

Provenance and lineage records require attribution — knowing which
identity ingested or transformed which data. NHI-10 destroys this
attribution. NHI-1 (improper offboarding) leaves orphaned identities
in lineage records.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-10 Human Use of NHI | Machine credentials used for ingestion operations — no individual attribution | Enforce machine identity per pipeline component; log with component identity |
| NHI-1 Improper Offboarding | Decommissioned pipeline identities remain in lineage records | Timely offboarding of pipeline NHIs |
| NHI-2 Secret Leakage | Lineage system credentials leaked — provenance records can be tampered | Protect lineage system credentials |

**Mitigations:**
- NHI-10: each pipeline stage has its own machine identity — lineage records include identity
- NHI-1: automated offboarding triggers when pipeline components are decommissioned
- NHI-2: protect lineage and audit system credentials as high-sensitivity NHI

---

## NHI programme maturity for GenAI data security

| NHI Risk | DSGAI entries most affected | Target state | Owner |
|---|---|---|---|
| NHI-1 Improper Offboarding | DSGAI21 | Automated on component decommission | IAM |
| NHI-2 Secret Leakage | DSGAI03, DSGAI06, DSGAI16 | Automated scanning in CI/CD | DevSecOps |
| NHI-3 Third-Party NHI | DSGAI13, DSGAI16, DSGAI17 | Assessed and minimum-scoped | Security |
| NHI-4 Insecure Authentication | DSGAI04, DSGAI08 | mTLS enforced across pipelines | Platform |
| NHI-5 Over-Privileged NHI | DSGAI02, DSGAI07, DSGAI08, DSGAI09 | Least-privilege per component | IAM |
| NHI-6 Insecure Storage | DSGAI02, DSGAI09, DSGAI14 | All credentials in vault | Platform |
| NHI-7 Long-Lived | DSGAI02, DSGAI07, DSGAI09, DSGAI12 | Rotation automated | IAM |
| NHI-8 Env Isolation | DSGAI16, DSGAI17 | Env separation enforced | DevSecOps |
| NHI-9 NHI Reuse | DSGAI04, DSGAI07, DSGAI08, DSGAI19 | Separate credential per component | IAM |
| NHI-10 Human Use | DSGAI18, DSGAI20, DSGAI21 | Human identity enforced for compliance | IAM |

---

## References

- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [Agentic_OWASP_NHI.md](../agentic-top10/Agentic_OWASP_NHI.md) — NHI-to-ASI cross-mapping
- [LLM_NHI.md](../llm-top10/LLM_NHI.md) — NHI for LLM deployments
- [shared/RECIPES.md](../shared/RECIPES.md) — Pattern 3: JIT Credential Issuance

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping DSGAI01–DSGAI21 to NHI Top 10 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
