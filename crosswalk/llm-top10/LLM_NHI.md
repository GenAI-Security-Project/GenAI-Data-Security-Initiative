<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : OWASP Non-Human Identities (NHI) Top 10
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × OWASP NHI Top 10

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [OWASP Non-Human Identities (NHI) Top 10](https://owasp.org/www-project-non-human-identities-top-10/) —
the framework for securing machine identities including service
accounts, API keys, OAuth tokens, certificates, and agent credentials.

---

## Why NHI matters for LLM security

LLM applications are not isolated — they call APIs, integrate with
tools and plugins, access databases, and interact with third-party
services. Every integration requires credentials: API keys for
model providers, OAuth tokens for tool access, service account
credentials for data retrieval. These are Non-Human Identities.

The NHI risks in LLM deployments are often overlooked because the
focus is on model behaviour, not on the identity infrastructure
that makes model-to-tool communication possible. But an LLM application
with a compromised API key (NHI-2 Secret Leakage) or over-privileged
service account (NHI-5) can cause far more damage than a model
that generates offensive content.

Key structural overlaps:
- **LLM03 (Supply Chain)** — third-party component credentials (NHI-3, NHI-8)
- **LLM06 (Excessive Agency)** — over-privileged tool credentials (NHI-5, NHI-7)
- **LLM02 (Sensitive Information Disclosure)** — credential leakage in outputs (NHI-2)

---

## OWASP NHI Top 10 reference

| NHI Entry | Name | Description |
|---|---|---|
| NHI-1 | Improper Offboarding | NHIs not revoked when systems decommission or relationships end |
| NHI-2 | Secret Leakage | Credentials exposed in source code, logs, config, or model outputs |
| NHI-3 | Vulnerable Third-Party NHI | Third-party tokens and identities with excessive permissions |
| NHI-4 | Insecure Authentication | Weak or missing authentication for machine-to-machine communication |
| NHI-5 | Over-Privileged NHI | NHIs with more permissions than required |
| NHI-6 | Insecure Credential Storage | Credentials stored insecurely — plaintext, weak encryption |
| NHI-7 | Long-Lived Credentials | Credentials without rotation, expiry, or revocation capability |
| NHI-8 | Environment Isolation Failure | Credentials shared across environments — prod creds in dev |
| NHI-9 | NHI Reuse | Same credentials used across multiple services or LLM deployments |
| NHI-10 | Human Use of NHI | Humans using machine credentials — no attribution, no MFA |

---

## Quick-reference summary

| LLM ID | Name | Severity | Primary NHI Entries | Tier |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | NHI-5, NHI-7 (blast radius amplifiers) | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | NHI-2, NHI-6 (credential leakage in outputs) | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | NHI-3, NHI-8, NHI-2 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | NHI-5, NHI-3 (pipeline access) | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | NHI-2 (credential in output), NHI-5 | Foundational–Hardening |
| LLM06 | Excessive Agency | High | NHI-5, NHI-7, NHI-9 | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | NHI-2 (API keys in system prompt) | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | NHI-5, NHI-4 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | NHI-2 (service account logging) | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | NHI-5, NHI-9 (credential reuse amplifies DoS) | Foundational–Hardening |

---

## Audience tags

- **Identity and access management (IAM) team** — full file
- **Security engineer** — NHI-2/NHI-5/NHI-7 entries most actionable
- **Platform engineer** — NHI-4/NHI-8/NHI-9 for infrastructure design
- **Developer** — NHI-2 (secret leakage), NHI-6 (credential storage)
- **Auditor** — NHI-1/NHI-10 offboarding and human use entries

---

## Detailed mappings

---

### LLM01 — Prompt Injection

NHI impact: prompt injection is most destructive when the LLM application
holds over-privileged credentials (NHI-5) or long-lived tokens (NHI-7).
A hijacked application with a read-write API key causes far more harm
than one with a read-only key.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Injection blast radius proportional to credential scope | Apply least-privilege to all LLM application credentials |
| NHI-7 Long-Lived Credentials | Injected session can use stolen long-lived tokens for extended period | Rotate all LLM application tokens; implement short-lived token pattern |

#### Mitigations

**Immediate:**
- Audit scope of all credentials held by LLM application
- Replace long-lived API keys with short-lived tokens where possible

**Short-term:**
- NHI-5: minimum credential scope for all LLM application integrations
- NHI-7: automated credential rotation for all LLM application credentials
- Scope restrictions: separate read vs read-write credentials per integration

---

### LLM02 — Sensitive Information Disclosure

NHI impact: LLM applications may inadvertently include credentials in
outputs — API keys embedded in system prompts are memorised and
reproduced; service account tokens logged alongside outputs are exposed.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-2 Secret Leakage | LLM outputs containing API keys, tokens, or credentials | Output filtering: detect and redact credential patterns in all outputs |
| NHI-6 Insecure Credential Storage | Credentials in plaintext config files ingested by LLM | Audit all config and data sources for embedded credentials |

#### Mitigations

**Immediate:**
- Scan all LLM system prompts for embedded credentials; remove any found
- Add credential pattern detection to output filtering pipeline

**Short-term:**
- NHI-2: automated secret scanning in all inputs to LLM (code, documents, configs)
- NHI-6: vault all LLM application credentials; no plaintext in config files
- Output scanning: detect API key and token patterns before delivery to user

---

### LLM03 — Supply Chain Vulnerabilities

NHI impact: third-party model providers, plugins, and tool integrations
bring their own NHI risks. A compromised plugin's credentials grant
attackers whatever permissions the plugin holds — often more than the
LLM application itself.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-3 Vulnerable Third-Party NHI | Third-party plugin tokens with excessive permissions | Review all third-party credentials; apply minimum scope |
| NHI-8 Environment Isolation Failure | Third-party dev/staging credentials used in production | Enforce environment isolation for all third-party integrations |
| NHI-2 Secret Leakage | Third-party component credentials exposed in shared config | Separate credential stores per third-party component |

#### Mitigations

**Immediate:**
- Inventory all third-party credentials in LLM deployment
- Verify no development credentials are used in production integrations

**Short-term:**
- NHI-3: review permissions of all third-party credentials; reduce to minimum
- NHI-8: separate credential stores for each environment
- NHI-2: automated secret scanning in all pipeline and deployment configs

---

### LLM04 — Data and Model Poisoning

NHI impact: training and fine-tuning pipelines have their own
NHI surface. Over-privileged pipeline credentials (NHI-5) or
third-party data source credentials (NHI-3) enable poisoning
attacks that wouldn't be possible with correctly-scoped access.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Write access to training data stores enables poisoning | Read-only credentials for data consumption; separate write credentials with MFA |
| NHI-3 Vulnerable Third-Party NHI | Third-party data pipeline credentials with training data write access | Apply NHI-3 controls to all data pipeline third-party credentials |

#### Mitigations

**Immediate:**
- Audit write access to all training data stores
- Separate read and write credentials for training data pipelines

**Short-term:**
- NHI-5: least-privilege for all training pipeline service accounts
- NHI-3: assess all third-party data pipeline credentials for excessive scope
- MFA or hardware token for any credential with training data write access

---

### LLM05 — Insecure Output Handling

NHI impact: LLM outputs passed to downstream systems — code
interpreters, databases, APIs — often carry credentials to access
those systems. These credentials may be embedded in outputs and
misused if the output is weaponised.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-2 Secret Leakage | Credentials appearing in model outputs passed to executors | Credential detection in output pipeline before execution |
| NHI-5 Over-Privileged NHI | Downstream service credentials with excessive scope | Apply least-privilege to all credentials used in downstream processing |

#### Mitigations

**Immediate:**
- Add credential pattern detection before passing model output to any executor
- Audit scope of credentials used by downstream processing systems

**Short-term:**
- NHI-2: automated output scanning for credential patterns
- NHI-5: minimum scope for all service accounts in output processing pipeline

---

### LLM06 — Excessive Agency

NHI is the control plane for agency. An LLM with excessive agency
is an LLM holding NHI credentials with over-broad scope. The NHI
Top 10 directly controls the blast radius of agency violations.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Tool/API credentials with more scope than task requires | Minimum credential scope per tool integration |
| NHI-7 Long-Lived Credentials | Long-lived tool credentials enable extended unauthorised access | Short-lived JIT credentials per task (see RECIPES.md) |
| NHI-9 NHI Reuse | Same credential used for multiple tools — compromise of one exposes all | Separate credentials per tool integration |

#### Mitigations

**Immediate:**
- Audit scope of all tool integration credentials held by LLM application
- Identify any credentials shared across multiple tool integrations

**Short-term:**
- NHI-5: minimum scope for all tool credentials
- NHI-7: implement short-lived JIT tokens for high-impact tool calls
- NHI-9: separate credentials per tool integration

**Strategic:**
- Per-task JIT credential issuance pattern (see RECIPES.md Pattern 3)
- Quarterly NHI audit for all LLM application credentials

---

### LLM07 — System Prompt Leakage

NHI impact: developers frequently embed API keys, service account
tokens, or credential fragments in system prompts for convenience.
These are extracted when the system prompt is leaked.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-2 Secret Leakage | API keys or tokens embedded in system prompt | Scan system prompts for credential patterns before deployment |
| NHI-6 Insecure Credential Storage | System prompt stored as plaintext config with embedded credentials | Externalise credentials to vault; reference by ID in system prompt |

#### Mitigations

**Immediate:**
- Automated secret scanning of all system prompt content
- Remove any credentials found in system prompts immediately

**Short-term:**
- NHI-6: vault all credentials; system prompt references vault path, not credential value
- NHI-2: CI/CD gate that fails if system prompt contains credential patterns
- Periodic system prompt audit for inadvertent credential inclusion

---

### LLM08 — Vector and Embedding Weaknesses

NHI impact: vector database service accounts and embedding store
credentials are often over-privileged — allowing cross-tenant
read access that enables the leakage scenarios in LLM08.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Embedding store service account with cross-tenant read access | Per-tenant credentials or least-privilege scope restrictions |
| NHI-4 Insecure Authentication | Unauthenticated embedding store access | Require authentication for all vector database connections |

#### Mitigations

**Immediate:**
- Audit authentication on all vector database connections
- Verify no embedding store service account has cross-tenant read access

**Short-term:**
- NHI-5: per-tenant credentials or fine-grained access controls for embedding stores
- NHI-4: mTLS or equivalent for all embedding store connections

---

### LLM09 — Misinformation

NHI impact: misinformation incidents require investigation — which
requires audit logs attributing LLM actions to specific identities.
NHI-10 (human use of machine credentials) destroys attribution and
makes investigation impossible.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-2 Secret Leakage | Audit log service credentials leaked or compromised | Protect audit log credentials as sensitive NHI |
| NHI-10 Human Use of NHI | Humans using LLM service account credentials — no attribution | Enforce separate human and machine credentials |

#### Mitigations

**Immediate:**
- Ensure all LLM application actions are attributed to machine identity, not human identity
- Protect audit log service credentials as high-sensitivity NHI

**Short-term:**
- NHI-10: enforce separation of human and machine credentials across the LLM deployment
- Immutable audit logging with tamper-evident storage

---

### LLM10 — Unbounded Consumption

NHI impact: credential reuse (NHI-9) across multiple services means
a DoS attack consuming one service's quota can cascade to all services
sharing those credentials. Over-privileged credentials amplify the
blast radius.

#### NHI mapping

| NHI Entry | How it applies | Mitigation |
|---|---|---|
| NHI-5 Over-Privileged NHI | Single credential with access to multiple services — one exhaustion affects all | Separate credentials per service with independent quotas |
| NHI-9 NHI Reuse | Shared credential used across services — quota exhaustion in one affects all | Separate credentials per integration |

#### Mitigations

**Immediate:**
- Identify any credentials shared across multiple API integrations
- Verify rate limiting is applied per-credential, not per-IP only

**Short-term:**
- NHI-9: separate credentials per service integration
- NHI-5: minimum scope per credential — consumption in one service cannot affect another
- Per-credential quota monitoring with alerting

---

## NHI programme maturity for LLM deployments

| NHI Risk | Current State | Target | Owner |
|---|---|---|---|
| NHI-1 Offboarding | | Automated | IAM team |
| NHI-2 Secret Leakage | | Automated scanning | DevSecOps |
| NHI-3 Third-Party NHI | | Assessed and scoped | Security team |
| NHI-4 Authentication | | mTLS/token auth | Platform team |
| NHI-5 Over-Privileged | | Least-privilege enforced | IAM team |
| NHI-6 Credential Storage | | Vault all credentials | Platform team |
| NHI-7 Long-Lived | | Rotation automated | IAM team |
| NHI-8 Env Isolation | | Environment separation enforced | DevSecOps |
| NHI-9 NHI Reuse | | Separate per integration | IAM team |
| NHI-10 Human Use | | Separate credentials enforced | IAM team |

---

## References

- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [Agentic_OWASP_NHI.md](../agentic-top10/Agentic_OWASP_NHI.md) — full NHI-to-ASI cross-mapping
- [LLM_SAMM.md](LLM_SAMM.md) — security programme maturity for LLM deployments
- [shared/RECIPES.md](../shared/RECIPES.md) — Pattern 3: JIT Credential Issuance

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping LLM01–LLM10 to NHI Top 10 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
