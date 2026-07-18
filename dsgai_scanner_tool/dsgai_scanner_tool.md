---
description: OWASP DSGAI 2026 compliance scanner — audits GenAI/agentic codebases against all 21 data security risks, produces a self-contained, redaction-safe HTML report
argument-hint: '[--internal] [--no-cve] [--scope <path>]'
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, WebFetch, WebSearch
---

# GenAI Data Security Risks (DSGAI) Tool — OWASP GenAI Data Security Compliance Report

**Based on:** [OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026)](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/) — published by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org/initiative/data-security/).

**Privacy:** Your source code never leaves your machine. Only package names and pinned versions are sent to public CVE databases during enrichment. By default the report obfuscates evidence (filename + line only, never matched values, never full paths). See *Obfuscation Mode* below.

**Changelog:**

- **v0.2 (May 2026)** — Complete revision. (1) All 21 control scans now defined (was 15). (2) Strict obfuscation by default — value-bearing matches never enter context or checkpoint; full paths shown only with `--internal`. (3) Search patterns rewritten as engine-neutral PCRE; noise patterns narrowed. (4) CVE enrichment fixed — NVD severity filter corrected, GitHub Advisory affects-filter added, Go ecosystem added to OSV, MITRE ATLAS split from CVE sources. (5) Report scaffolding renumbered, styling contradictions removed. (6) Windows open-report command added. (7) `[BUY]` controls now meaningfully emit "Vendor Attestation Required" badges. (8) Frontmatter added; argument flags supported. (9) `--scope` flag for sub-directory scoping on large repos. (10) Pattern noise tightened (DSGAI01 dp libs, DSGAI02 vault, DSGAI04 unpinned, DSGAI11 vector queries, DSGAI20 endpoints).
- v0.1 (Apr 2026) — Initial release.

---

## TL;DR — Quick Reference

| Want to… | Run |
|---|---|
| Scan the whole repo, share the report externally | `/dsgai_scanner_tool` |
| Scan with full file paths (team-internal use) | `/dsgai_scanner_tool --internal` |
| Scan with no internet (air-gapped / offline) | `/dsgai_scanner_tool --no-cve` |
| Scan only a sub-directory of a large repo | `/dsgai_scanner_tool --scope app/agents/` |
| Combine flags | `/dsgai_scanner_tool --internal --no-cve --scope services/` |

**Outputs:** `DSGAI-report.html` (the deliverable) + `DSGAI-scan.json` (intermediate checkpoint, safe to commit in STRICT mode).

**Time:** 2–5 minutes for a typical repo in Claude Code (parallel scans). Longer outside Claude Code.

---

## Argument Handling

Inspect `$ARGUMENTS` before scanning. Flags are **independent and combinable** — e.g. `/dsgai_scanner_tool --internal --no-cve --scope app/` is valid.

- **`--internal`** → set `OBFUSCATION=internal`. Full file paths shown in report. Value-bearing match contents are *still* never displayed; only difference from strict mode is path detail.
- **(no `--internal`)** → set `OBFUSCATION=strict` (default). Evidence shows filename + line number only; intermediate directory components are dropped. Suitable for sharing with auditors, stakeholders, or storing in a public repo.
- **`--no-cve`** → skip Step 0.5 entirely. Use embedded CVE database only. Useful for fully offline / air-gapped environments.
- **`--scope <path>`** → restrict all scans to the given sub-directory (relative to repo root). Useful for monorepos (`--scope services/ai-gateway/`) or for incremental scans of large codebases. If absent, the entire repo is scanned. The scope path is recorded in the report header so the reader knows the coverage.

Render the chosen flags as badges in the report header so the reader knows: obfuscation mode, CVE enrichment status, and scope.

---

## Step 0: Verify Repository is a GenAI / Agentic System

Before scanning, confirm the repo contains GenAI-relevant code. Search for any of:

**LLM / AI frameworks:**
- Python: `openai`, `anthropic`, `langchain`, `llama_index`, `llamaindex`, `transformers`, `torch`, `tensorflow`, `huggingface`, `litellm`, `mistral`, `together`, `cohere`, `groq`, `vertexai`, `bedrock`, `dspy`, `instructor`, `outlines`
- Java/Kotlin: `LangChain4j`, `spring-ai`, `aws-bedrock`, `openai-java`
- JavaScript/TypeScript: `openai`, `@anthropic-ai`, `langchain`, `ai` (Vercel AI SDK), `@huggingface`, `llamaindex`
- Go: `github.com/sashabaranov/go-openai`, `github.com/tmc/langchaingo`, `github.com/anthropics/anthropic-sdk-go`

**Agentic / RAG patterns:**
- `AgentExecutor`, `Tool`, `@tool`, `tool_call`, `function_call`, `MCP`, `ModelContextProtocol`
- `VectorStore`, `Chroma`, `Pinecone`, `Weaviate`, `Qdrant`, `pgvector`, `FAISS`, `Milvus`, `Redis.*Vector`
- `RAG`, `Retrieval`, `Embeddings`, `embed_documents`, `similarity_search`, `retriever`

If **none of these signals are present**, note that the repo does not appear to be an AI/agentic system and generate a minimal report indicating `NOT APPLICABLE` for all 21 controls.

If signals are present, proceed with the full scan.

---

## Step 0.5: Dynamic CVE Enrichment

> Skip this entire step if `$ARGUMENTS` contains `--no-cve`. In that case, set the Section 2 banner to "❌ Offline mode — embedded CVE database only (user-requested)" and proceed.

Before scanning for DSGAI controls, extract the repo's AI/ML package inventory and fetch live CVE data from multiple sources. This supplements the embedded CVEs already in each DSGAI risk section with findings specific to the versions this repo actually uses.

### Sub-step A: Extract AI Package Inventory

Read dependency files and extract package name + pinned version for every AI/ML-relevant package:

**Python** — read `requirements.txt`, `requirements*.txt`, `Pipfile`, `Pipfile.lock`, `pyproject.toml`, `poetry.lock`, `setup.py`, `setup.cfg`. Pattern (PCRE):
```
(openai|anthropic|langchain|llama[_-]?index|transformers|torch|tensorflow|huggingface|litellm|cohere|groq|mistral|together|chromadb|qdrant|pinecone|weaviate|faiss|milvus|pgvector|langfuse|langsmith|guardrails|nemo[_-]guardrails|presidio|llm[_-]guard|rebuff|opacus|sdv|gretel|dspy|instructor|outlines|vllm|ollama)
```

**JavaScript/TypeScript** — read `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`. Pattern:
```
(openai|@anthropic-ai|langchain|@huggingface|^ai$|@xenova|chromadb|qdrant|pinecone|weaviate|faiss-node|llamaindex)
```

**Java/Kotlin** — read `pom.xml`, `build.gradle`, `build.gradle.kts`, `gradle/libs.versions.toml`. Pattern:
```
(langchain4j|spring-ai|aws-bedrock|openai-java|anthropic-java)
```

**Go** — read `go.mod`, `go.sum`. Pattern:
```
(go-openai|langchaingo|anthropic-sdk-go|qdrant/go-client|chroma-go)
```

Build a table: `Package | Version | Language | Ecosystem | Pinned?`. If a version is unpinned (`>=`, `^`, `~`, `*`), record `"unpinned — latest assumed"` and flag the package for additional WARN scrutiny in DSGAI04.

---

### Sub-step B: Query Live Vulnerability Sources

**Parallel execution:** Fire all CVE source queries simultaneously — send OSV, NVD, and GitHub Advisory requests as parallel tool calls in a single message. Do not wait for one source to complete before starting the next.

#### Source 1 — OSV (Open Source Vulnerabilities) — Primary

Best precision: exact package + version match. POST to the OSV API for each inventoried package:

```
POST https://api.osv.dev/v1/query
Content-Type: application/json
Body: {"package": {"name": "<package_name>", "ecosystem": "<ECOSYSTEM>"}, "version": "<pinned_version>"}
```

Ecosystem values: `"PyPI"` (Python), `"npm"` (JS/TS), `"Maven"` (Java/Kotlin), `"Go"` (Go modules). For unpinned packages, omit `"version"` and OSV returns all known vulns for the package.

Extract per result: OSV ID (maps to CVE ID if present in `aliases`), severity (`severity[].score`), affected version ranges (`affected[].ranges`), description (`summary`/`details`), fixed version (`affected[].ranges[].events[].fixed`), published date.

#### Source 2 — NVD (National Vulnerability Database) — CVSS Scoring

Keyword-based fallback that returns full CVSS v3.1 scoring metadata.

```
GET https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=<PACKAGE>&cvssV3Severity=CRITICAL&resultsPerPage=10
```

**Note on the severity parameter:** NVD honors a single `cvssV3Severity` value per request. To capture both CRITICAL and HIGH, issue two parallel requests per package — one with `cvssV3Severity=CRITICAL`, one with `cvssV3Severity=HIGH`. Do not pass both values in one URL; only the last is honored.

**Rate limits:** NVD throttles unauthenticated traffic to ~5 requests per 30 seconds. If you have an `NVD_API_KEY` env var, add `apiKey=<key>` to the URL for 50 req/30s. On 403 / 429, back off exponentially (wait, then retry once); on second failure, mark NVD as "partial — rate-limited" in the enrichment banner and continue.

Priority packages to always query even if not pinned:
- `langchain`, `langchain-community`, `langchain-core`
- `openai`, `anthropic`
- `torch`, `transformers`
- `llama-index`, `llama_index`
- `chromadb`, `qdrant-client`
- `vllm`, `ollama`
- Any additional packages found in Sub-step A

#### Source 3 — GitHub Advisory Database — Early Disclosures

AI/ML advisories often appear here before NVD. **Always filter by package** — never request the unfiltered feed (returns generic results unrelated to the repo):

```
GET https://api.github.com/advisories?affects=<package>&ecosystem=<ecosystem>&per_page=30
```

Ecosystem values: `pip`, `npm`, `maven`, `go`, `rubygems`, `nuget`, `composer`, `erlang`, `actions`, `rust`.

Unauthenticated rate limit is 60 req/hour. With a `GITHUB_TOKEN` env var (passed as `Authorization: Bearer <token>`), the limit is 5000 req/hour. On 403, drop to embedded data and mark GitHub Advisory as "partial — auth required" in the banner.

#### Source 4 — AVID (AI Vulnerability and Incidents Database)

Covers AI/ML-specific vulnerabilities (bias, robustness, adversarial attacks) not always found in standard CVE databases. Use WebSearch:

```
site:avidml.org <package_name> vulnerability
site:avidml.org langchain security
```

AVID issues use AVID-VULN-xxx IDs rather than CVE IDs. Note the source in the report. Map to the most relevant DSGAI risk using the table in Sub-step C.

---

For each CVE or advisory found across all sources:
1. Extract: ID, CVSS score (if available), description, affected version ranges, fixed version, published date, source.
2. Compare the repo's pinned version against the affected range.
3. Classify:
   - **EXPLOITABLE** — repo version is in the affected range (and not at-or-above the fixed version)
   - **NOT AFFECTED** — repo version is at or newer than the fixed version
   - **UNKNOWN** — version unpinned or range cannot be parsed
4. Map to the most relevant DSGAI risk (Sub-step C).
5. Deduplicate by CVE ID across sources — keep one entry, list all sources that returned it.

---

### Sub-step E: MITRE ATLAS (Attack Techniques, Not CVEs)

MITRE ATLAS documents AI-specific attack techniques (prompt injection, model evasion, training data poisoning). These are **not CVEs** and are tracked separately from Section 2's CVE Advisory. Render them in a dedicated subsection inside Section 1 ("AI Attack Techniques Relevant to This Stack").

Query for techniques relevant to the detected AI stack:

```
site:atlas.mitre.org prompt injection
site:atlas.mitre.org training data poisoning
site:atlas.mitre.org <detected_framework_name>
```

Map each technique to its DSGAI risk and include the ATLAS ID (e.g. `AML.T0051`) and one-line description.

**Do not** count ATLAS techniques as CVEs in the Section 2 totals — they are advisory-only.

---

### Sub-step C: CVE → DSGAI Risk Mapping

Use this mapping to assign newly discovered CVEs to the right DSGAI risk section:

| CVE Pattern / Category | DSGAI Risk |
|---|---|
| Prompt injection, input manipulation, jailbreak | DSGAI01, DSGAI18, DSGAI20 |
| Credential leak, API key exposure, auth bypass in AI SDK | DSGAI02 |
| Shadow API endpoint, unauthorized LLM endpoint | DSGAI03 |
| Supply chain, package poisoning, pickle deserialization, model weight tampering | DSGAI04 |
| RAG / document ingestion path traversal, retrieval bypass | DSGAI05 |
| MCP server / plugin RCE, tool call injection, transport downgrade | DSGAI06 |
| Cache poisoning, stale data, TTL bypass | DSGAI07 |
| Multimodal input bypass, EXIF / OCR exfil | DSGAI09 |
| Synthetic data re-identification | DSGAI10 |
| Multi-tenant data leakage, cross-session context bleed | DSGAI11 |
| SQL injection via LLM-generated queries | DSGAI12 |
| Vector store unauthorized access, unencrypted embeddings, embedding inversion | DSGAI13 |
| Telemetry / logging data exposure, PII in traces | DSGAI14 |
| Context window leak, system prompt exposure | DSGAI15 |
| IDE plugin context leak, telemetry overshare | DSGAI16 |
| AI service DoS, resource exhaustion, retry storm | DSGAI17 |
| Model output manipulation, hallucination-based data exposure | DSGAI18 |
| Labeling platform credential leak, label poisoning | DSGAI19 |
| Inference API DoS, model extraction, rate limit bypass | DSGAI20 |
| Knowledge store write injection, persistent prompt injection | DSGAI21 |

---

### Sub-step D: Build Live CVE Supplement

After querying all sources, compile a **Live CVE Supplement** to be displayed in Section 2 of the report. Format each entry:

```
CVE-YYYY-NNNNN | CVSS X.X | Package: <name> | Status: EXPLOITABLE / NOT AFFECTED / UNKNOWN
  Description: <one line>
  Affects: <version range>
  Fixed: <fixed version>
  Repo version: <version from inventory>
  Maps to: DSGAI-XX
  Source: NVD / OSV / GitHub Advisory / AVID
```

These live CVEs are **additive** — they extend the embedded CVEs already in each DSGAI section, they do not replace them.

**Enrichment status** (display as banner at top of Section 2):
- ✅ Online — queried OSV + NVD + GitHub Advisory + AVID at `<timestamp>`
- ⚠️ Partial — one or more sources unreachable; results may be incomplete (list which sources failed and why)
- ❌ Offline — all sources unreachable, or `--no-cve` was passed; showing embedded CVEs only

If any individual source is unreachable (network restriction, rate limit, API error), continue with the remaining sources and note which were unavailable in the banner.

---

## DSGAI Embedded Requirements

> **Scope tags:** `[BUILD]` = your team implements this in the codebase. `[BUY]` = the LLM provider / SaaS vendor is responsible — surface as "Vendor Attestation Required". `[BOTH]` = shared responsibility.

### DSGAI01 — Training Data Privacy [BOTH]
**Risk:** PII, PHI, confidential data, or sensitive credentials inadvertently included in training datasets, fine-tuning corpora, embeddings, or model outputs. Data subjects have no visibility or right to erasure.

**Key mitigations to scan for:**
- No-training / data-opt-out headers/flags in API calls (`X-Training-Data: false`, `allow_training=False`, `training_opt_out`)
- PII scrubbing before data ingestion (`anonymize`, `redact`, `scrub_pii`, `presidio`, `piiDetect`, `mask_pii`)
- Differential privacy library usage (`dp-accounting`, `opacus`, `tensorflow-privacy`)
- Output filtering for PII before returning to user (`filter_pii`, `remove_pii`, `output_sanitize`)
- Data minimization patterns (log only IDs, not full content)
- GDPR/CCPA consent check before training pipeline

**BUY-side (vendor must attest):** training data retention policy; opt-out honored on inference; sub-processor list documented.

**Known CVEs:** CVE-2024-5184 (EmailGPT — prompt injection exposing training data)

---

### DSGAI02 — Agentic System Identity and Credential Management [BUILD]
**Risk:** Agent identities lack MFA/RBAC; credentials (API keys, tokens) hardcoded or over-privileged; tool invocations not authenticated; lateral movement possible when one agent credential is compromised.

**Key mitigations to scan for:**
- No hardcoded LLM API keys (`OPENAI_API_KEY\s*=\s*["']sk-`, `ANTHROPIC_API_KEY\s*=\s*["']sk-ant-`)
- No hardcoded cloud credentials used by agents (`AWS_ACCESS_KEY_ID\s*=\s*["'][A-Z0-9]{16,}`)
- Token scope patterns: minimal-scope tokens, not wildcard
- OAuth/OIDC for agent-to-service auth (`client_credentials`, `jwt_bearer`, `service_account`)
- Vault / secrets manager retrieval patterns for agent credentials
- Per-agent credential isolation (not shared global credentials)
- Tool call authentication (signed requests, HMAC, mutual TLS)

**Known CVEs:** CVE-2025-0282 (Ivanti — chained agent credential escalation)

---

### DSGAI03 — Shadow AI and Unauthorized Data Flows [BOTH]
**Risk:** Developers or services send sensitive internal data to unauthorized LLM APIs (SaaS models, unapproved endpoints) without security review, exfiltrating PII, IP, or confidential data.

**Key mitigations (process/governance — partially detectable in code):**
- API allowlist/denylist for outbound LLM endpoints (proxy patterns, egress policy config)
- Detection: hardcoded third-party LLM hostnames not in approved list (flag for review)
- Proxy / gateway pattern: all LLM calls routed through internal proxy (`llm-gateway`, `ai-proxy`, `model-gateway`)
- DLP annotations or data classification checks before LLM call
- CI/CD scanning for new LLM endpoint additions

---

### DSGAI04 — AI Supply Chain Security [BUILD]
**Risk:** Compromised model weights, poisoned PyPI/npm packages, unsigned model artifacts, or pickle deserialization vulnerabilities allow supply chain attacks.

**Key mitigations to scan for:**
- `torch.load(` without `weights_only=True` — insecure pickle deserialization
- Model artifact checksums / signature verification (`sha256`, `verify_signature`, `model_hash`)
- Pinned dependency versions in `requirements.txt` / `package.json` (exact versions `==`, not `>=` for ML deps)
- `--require-hashes` in pip install scripts
- Trusted registry enforcement (`index-url`, `registry`, `artifactory`, NOT direct PyPI in prod)
- SBOM generation in CI/CD pipeline (`syft`, `cyclonedx`, `spdx`)
- Model card / provenance file present (`model_card.md`, `MODEL_CARD`, `model_info.json`)

**Known CVEs:** CVE-2025-24357 (vLLM — model deserialization RCE)

---

### DSGAI05 — RAG Data Security [BUILD]
**Risk:** RAG pipelines ingest sensitive documents without access control; poisoned documents inject malicious instructions; path traversal in document ingestion; retrieved context leaks cross-tenant data.

**Key mitigations to scan for:**
- Document ingestion path validation (no `../`, path traversal sanitization)
- Access control on retrieved documents before inclusion in context (`acl_filter`, `access_check`, `permitted_docs`)
- Metadata-based tenant isolation on vector search (`filter={"tenant_id": ...}`, `namespace=tenant_id`)
- Document hash / integrity check before ingestion (`hashlib`, `sha256`, integrity verification)
- Output validation of retrieved content (no blind trust of retrieved text as instructions)
- `max_chunk_size` / content size limits on ingested documents

**Known CVEs:** CVE-2024-3584 (Qdrant — unauthorized access to vector data)

---

### DSGAI06 — MCP and Plugin Security [BUILD]
**Risk:** MCP servers expose tools with excessive permissions; plugins exfiltrate context window data; insecure transport allows MITM; no input validation on tool arguments allows injection.

**Key mitigations to scan for:**
- MCP transport uses HTTPS / wss (not `http://`, `ws://` in prod config)
- Tool argument schema validation (`schema`, `jsonschema`, `pydantic`, `zod`)
- MCP server authentication (`api_key`, `bearer_token`, `oauth`, auth header in MCP config)
- Allowlisted tool permissions (not wildcard `*` tool access)
- Input sanitization before tool execution
- Plugin manifest / config specifies minimal required permissions

---

### DSGAI07 — Data Lifecycle Management in AI Systems [BUILD]
**Risk:** Training data, embeddings, cached prompts, conversation history, and fine-tuned model weights are never deleted; no TTL enforcement; data subject erasure requests cannot be honored.

**Key mitigations to scan for:**
- TTL configuration on caches, session stores, vector namespaces (`ttl=`, `expires_in=`, `max_age=`)
- Session history cleanup / deletion function (`delete_session`, `clear_history`, `purge_conversation`)
- Embedding deletion / namespace drop capability (`delete_namespace`, `delete_collection`, `drop_index`)
- Data retention config file or constants (`RETENTION_DAYS`, `DATA_TTL`, `HISTORY_TTL`)
- Right-to-erasure handler (`handle_deletion_request`, `gdpr_delete`, `erase_user_data`)

---

### DSGAI08 — Regulatory and Privacy Compliance for AI [BOTH]
**Risk:** AI system processes personal data without legal basis; EU AI Act high-risk classification not assessed; GDPR/CCPA obligations not fulfilled; no AI governance documentation.

**Key mitigations (largely process — partially detectable):**
- Privacy impact assessment artifacts (`PIA`, `DPIA`, `privacy_assessment` in docs or appsec/)
- Data processing agreement reference or annotation in code
- Consent capture before processing personal data in AI pipeline
- EU AI Act risk classification annotation (`ai_act_risk_level`, `high_risk_ai`, `limited_risk`)
- Logging of AI decisions for auditability (`audit_log`, `decision_log`)
- `do_not_track` / opt-out signal honored in AI pipeline

**BUY-side (vendor must attest):** SOC 2 / ISO 27001 report; DPA executed; sub-processor list reviewed.

---

### DSGAI09 — Multimodal AI Data Security [BOTH]
**Risk:** Image/audio/video inputs contain embedded PII or steganographic payloads; OCR output exposes sensitive document data; multimodal models process regulated data without controls.

**Key mitigations to scan for:**
- EXIF/metadata stripping before image processing (`strip_exif`, `remove_metadata`, `PIL.Image`, `exifread`)
- Image content moderation / PII detection before LLM ingestion (`detect_pii_in_image`, content_filter)
- File type validation for multimodal inputs (`allowed_types`, `mime_type_check`, `magic` library)
- Max file size limits on multimodal uploads
- Steganography detection hook (advanced — note if absent)

---

### DSGAI10 — Synthetic Data Security [BUILD]
**Risk:** Synthetic data generated for training still contains real PII through imperfect generative models; synthetic data memorizes training samples; no validation that synthetic data is truly de-identified.

**Key mitigations to scan for:**
- Membership inference test before using synthetic data (`membership_inference`, `mia_test`)
- k-anonymity / l-diversity / t-closeness validation (`k_anonymity`, `anonymization_check`)
- Synthetic data generation library with privacy guarantees (`SDV`, `gretel`, `synthetic_data_vault`)
- Differential privacy noise in synthetic generation (`epsilon=`, `noise_multiplier=`)
- Re-identification risk assessment annotation in data pipeline

---

### DSGAI11 — Multi-Tenant Data Isolation [BUILD]
**Risk:** Agent or RAG system serves multiple tenants from shared vector store or shared context; one tenant's data leaks into another's responses; session data not scoped to tenant.

**Key mitigations to scan for:**
- Tenant ID required in every LLM/vector query (absent tenant_id = FAIL)
- Namespace / collection per tenant in vector store (`namespace=tenant_id`, `collection_name=f"{tenant_id}_..."`)
- Row-level security or metadata filter on all retrievals (`filter={"tenant": current_tenant}`)
- Session token validates tenant binding (`tenant_id in session`, `verify_tenant`)
- No cross-tenant data sharing in context assembly (no global shared prompt cache across tenants)

**Known CVEs:** CVE-2024-8309 (LangChain GraphCypher — missing tenant isolation in graph queries)

---

### DSGAI12 — Database Agent Security [BUILD]
**Risk:** LLM-generated SQL/NoSQL queries executed without validation; agents use over-privileged DB accounts; natural language to SQL enables SQL injection via prompt; no read-only enforcement.

**Key mitigations to scan for:**
- Raw SQL execution from LLM output (`execute(llm_output)`, `cursor.execute(query)` from model) — FAIL
- Parameterized query enforcement (`%s`, `?`, `:param` — even for generated queries)
- Read-only DB user / connection for query agents (`read_only=True`, `readonly`, select-only role)
- Query allowlist / validator before execution (`validate_query`, `query_validator`, `safe_sql`)
- Stored procedure enforcement (no ad-hoc DDL from agents)
- `LIMIT` / `MAX_ROWS` cap on agent-issued queries
- No `DROP`, `DELETE`, `TRUNCATE`, `ALTER` in agent-accessible schema

**Known CVEs:** CVE-2024-8309 (LangChain GraphCypher — SQL injection via graph query generation)

---

### DSGAI13 — Vector Store Security [BUILD]
**Risk:** Vector store lacks authentication; embeddings stored unencrypted; Qdrant/Chroma/Weaviate default config is unauthenticated; embedding inversion attacks recover training data from vectors.

**Key mitigations to scan for:**
- Vector store authentication configured (`api_key=`, `auth_token=`, `CHROMA_SERVER_AUTH`, `QDRANT_API_KEY`)
- Encryption at rest config for vector store (`encrypted=True`, `tls=True`, `ssl_enabled`)
- TLS on vector store connection (`https://`, `wss://`, `grpcs://` endpoints)
- Not listening on `0.0.0.0` without authentication (default Chroma/Qdrant insecure config)
- Backup encryption for vector store snapshots
- Access log / audit for vector store queries

**Known CVEs:** CVE-2024-3584 (Qdrant — unauthenticated access); CVE-2024-37032 (Ollama — remote model pull without auth)

---

### DSGAI14 — AI Telemetry and Observability Data Security [BUILD]
**Risk:** Full prompts, completions, PII, or secrets logged verbatim in telemetry/tracing pipelines; logs shipped to external observability SaaS without scrubbing; LLM span data violates data residency.

**Key mitigations to scan for:**
- Verbose prompt logging disabled in prod (`log_prompts=False`, `capture_content=False`, `OTEL_LOG_PROMPTS=false`)
- Full response body logging disabled (`log_completions=False`, `log_full_response=False`)
- PII redaction in logging middleware (`redact_pii`, `mask_sensitive`, `sanitize_log`)
- OpenTelemetry / LangSmith / Langfuse config that excludes prompt content in prod
- Log level gating (DEBUG logs prompts, INFO/WARN does not)
- No `print(response)` / `console.log(response)` for full LLM output in prod code paths

---

### DSGAI15 — Context Window Data Security [BUILD]
**Risk:** System prompts embed secrets or customer PII; context assembly aggregates excessive user data; over-stuffed context increases PII exposure radius; context window logs expose sensitive data.

**Key mitigations to scan for:**
- Context size limits / truncation (`max_context_length=`, `context_window_limit=`, `truncate_context`)
- No hardcoded secrets in system prompt strings (`system_prompt = "..."` containing keys, passwords)
- Customer-360 / full-profile aggregation without data minimization (pattern: fetching all user fields into context)
- System prompt loaded from config/vault (not hardcoded in source)
- Context assembly scoped to task-relevant fields only
- Prompt template uses variables, not interpolated raw user data directly into sensitive positions

---

### DSGAI16 — AI IDE Plugin and Extension Security [BUILD]
**Risk:** IDE plugins (Copilot, Cursor, Codeium) send entire file context to external LLMs; plugins have overly broad file system or terminal permissions; developer credentials exposed in plugin context.

**Key mitigations to scan for:**
- `.copilotignore` / `.aiignore` / `.cursorignore` present with sensitive path exclusions
- Plugin config files that restrict context scope (`contextWindow`, `ignorePaths`, `excludeFiles`)
- IDE plugin telemetry / data sharing disabled (`telemetry=off`, `share_data=false`)
- No secrets in files commonly sent to IDE context (`.env`, `config/secrets.*` in ignore lists)

---

### DSGAI17 — AI System Resilience and Availability [BUILD]
**Risk:** AI services have no fallback when LLM API is unavailable; unbounded retry loops exhaust quota; no circuit breakers; resource exhaustion via prompt flooding.

**Key mitigations to scan for:**
- Circuit breaker pattern (`CircuitBreaker`, `@circuit`, `tenacity`, `resilience4j`)
- Retry with backoff (`retry`, `exponential_backoff`, `max_retries=`, `backoff_factor=`)
- Timeout on LLM calls (`timeout=`, `request_timeout=`, not unbounded)
- Rate limiting on incoming AI requests (`rate_limit`, `throttle`, `RateLimiter`)
- Fallback response when LLM unavailable (`fallback_response`, `default_response`, `graceful_degradation`)
- Queue depth limits for async LLM processing

---

### DSGAI18 — Model Output Data Security [BUILD]
**Risk:** Model outputs contain hallucinated PII, confidential data regurgitation, or sensitive details from training; outputs not validated before returning to user; confidence scores expose model internals.

**Key mitigations to scan for:**
- Output content filtering before returning to caller (`filter_output`, `sanitize_response`, `output_guard`)
- PII detection on model output (`detect_pii`, `presidio`, `pii_scan_output`)
- Guardrails / moderation layer on outputs (`guardrails`, `nemo-guardrails`, `llm_guard`, `moderation`)
- No raw confidence logprobs exposed to end users in API response
- Output length limits (`max_tokens=` always set, not unbounded)
- Grounding check: response verified against retrieved context (not free-form hallucination)

---

### DSGAI19 — AI Data Labeling Security [BUILD]
**Risk:** Labeling pipelines expose raw PII-containing data to crowd workers or external labeling services; no data minimization before export; labeling platform lacks access controls; label poisoning possible.

**Key mitigations to scan for:**
- PII anonymization before labeling export (`anonymize_for_labeling`, `pseudonymize`, `redact_before_export`)
- Labeling data minimization (only fields needed for labeling task exported)
- Access controls on labeling dataset exports (`label_studio_auth`, `labelbox_auth`, `scale_api_key` in vault)
- Audit log for labeling data access
- Re-identification risk check after labeling is complete

---

### DSGAI20 — Inference API Security [BOTH]
**Risk:** Inference API has no authentication; no rate limiting; model fingerprinting attacks allowed; API returns raw logprobs enabling model extraction; excessive resource consumption via adversarial inputs.

**Key mitigations to scan for:**
- API authentication required on inference endpoint (`api_key`, `bearer_token`, `Authorization` header validation)
- Rate limiting on inference API (`rate_limit`, `throttle`, `429` handling, `RateLimiter`)
- Input length validation (`max_input_length=`, `max_tokens=`, input truncation)
- No raw logprobs exposed by default (`logprobs=False` or only on explicit request with auth)
- ToS enforcement / acceptable use policy check for API access
- Prompt injection detection layer on API input

**BUY-side (vendor must attest):** provider-side rate limits documented; abuse detection in place; logprobs policy for tenant API.

---

### DSGAI21 — Knowledge Store Security [BUILD]
**Risk:** Knowledge bases (wikis, SharePoint, databases feeding RAG) accessible by agent have overly broad write access; agents can modify knowledge store, enabling persistent prompt injection; no version control on knowledge entries.

**Key mitigations to scan for:**
- Read-only connection for RAG retrieval (`read_only=True`, read-only DB user, GET-only HTTP client)
- No write operations on knowledge store from agent code paths (`INSERT`, `UPDATE`, `DELETE` absent in agent's DB access layer)
- Version control / change log on knowledge store entries (`versioned=True`, `audit_writes`)
- Content validation before knowledge store write (`validate_content`, `sanitize_before_write`)
- Access control: agent identity limited to specific knowledge store namespace/collection

---

## Step 1: Detect Repository Type and AI/GenAI Structure

Identify the build system and language(s):
1. **Python** (`requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile`) — most common for AI/ML
2. **Java/Kotlin** (`pom.xml`, `build.gradle`, `build.gradle.kts`) — enterprise LLM integrations
3. **JavaScript/TypeScript** (`package.json`) — frontend AI, Vercel AI SDK, Node.js agents
4. **Go** (`go.mod`) — infrastructure agents, proxy layers
5. **Multi-language** — check all subdirectories

Also identify:
- **AI frameworks in use:** LangChain, LlamaIndex, Semantic Kernel, Spring AI, LangChain4j, Vercel AI SDK, AutoGen, CrewAI, DSPy
- **Vector stores in use:** Chroma, Pinecone, Weaviate, Qdrant, FAISS, pgvector, Milvus, Redis Vector
- **LLM providers in use:** OpenAI, Anthropic, Bedrock, Vertex AI, Azure OpenAI, HuggingFace, Ollama, vLLM
- **MCP / plugins:** MCP server config files, plugin manifests
- **Container:** `Dockerfile`, `docker-compose.yml`
- **Kubernetes/Helm:** `helm/`, `k8s/`, `*.yaml` deployment manifests
- **CI/CD:** `.github/workflows/`, `.circleci/`, `Jenkinsfile`
- **Data pipelines:** `dags/`, `airflow`, `prefect`, data ingestion scripts
- **AppSec / security architecture review artifacts:** `appsec/`, `.appsec/`, `security-review/`

---

## Step 2: Scan for DSGAI Issues

> **Canonical rule definitions live in [`rules/dsgai-rules.yaml`](rules/dsgai-rules.yaml)** (validated by `rules/rules.schema.json`, compiled to `rules/dsgai-rules.json`). The pattern listings in this Step are descriptive — the YAML is authoritative and is what the deterministic CLI executes. When they disagree, the YAML wins. (Full skill rewrite to CLI-first orchestration is PR-07.)

### Search Engine Prerequisite

All patterns below use **PCRE / Perl-compatible regex syntax** — `\s`, `{n,m}`, character classes inside groups, alternation. Inside Claude Code, the Grep tool (ripgrep) supports this natively. Outside Claude Code, use `rg` (ripgrep) or `grep -P` (GNU grep with PCRE). Plain POSIX BRE/ERE will *not* match `\s`, `\d`, or `{n,m}` correctly and will produce false negatives.

### Parallel Execution

Run all 21 DSGAI scans simultaneously — send all scan commands as parallel tool calls in a single message batch. Do not wait for one control's scan to finish before starting the next. Split into three batches of 7 if your runner has a per-message limit:

- **Batch A:** DSGAI01, 02, 03, 04, 05, 06, 07
- **Batch B:** DSGAI08, 09, 10, 11, 12, 13, 14
- **Batch C:** DSGAI15, 16, 17, 18, 19, 20, 21

### Evidence Classification — Structural vs Value-Bearing

Every scan below is classified as either **[STRUCTURAL]** or **[VALUE-BEARING ⚠️]**. This classification controls *how* the search is executed and *what* may appear in the report.

**[STRUCTURAL]** — the match shows a code pattern (function call, missing import, missing decorator, architectural gap). The matched line contains no runtime secret or personal data. Safe to display the matched line.

**[VALUE-BEARING ⚠️]** — the pattern targets lines where the *match content IS* a credential, API key, secret, connection string, or PII-bearing log statement. The actual matched value must **never** appear in the report, the checkpoint file, or any tool call that persists it — regardless of whether the value looks like a demo, test, or placeholder.

| DSGAI Control | Classification | Why |
|---|---|---|
| DSGAI01 | STRUCTURAL | Looks for presence/absence of scrubbing library imports and opt-out flags |
| DSGAI02 | VALUE-BEARING ⚠️ | Matches lines containing actual API key values, passwords, JWT secrets, connection strings |
| DSGAI03 | STRUCTURAL | Matches public API endpoint hostnames in config |
| DSGAI04 | STRUCTURAL | Matches call patterns and dependency file structure |
| DSGAI05 | STRUCTURAL | Matches function calls missing a filter argument |
| DSGAI06 | STRUCTURAL | Matches missing auth middleware and transport flags |
| DSGAI07 | STRUCTURAL | Matches missing TTL parameters and absent delete function names |
| DSGAI08 | STRUCTURAL | Looks for DPIA/consent keyword presence |
| DSGAI09 | STRUCTURAL | Matches EXIF stripping and file type validation patterns |
| DSGAI10 | STRUCTURAL | Matches synthetic data library imports |
| DSGAI11 | STRUCTURAL | Matches missing tenant filter arguments in function calls |
| DSGAI12 | STRUCTURAL | Matches direct SQL execution call patterns |
| DSGAI13 | VALUE-BEARING ⚠️ | May match lines where vector store auth tokens are hardcoded |
| DSGAI14 | VALUE-BEARING ⚠️ | Matches log statements whose format strings may contain PII field references or inline test PII values |
| DSGAI15 | VALUE-BEARING ⚠️ | Matches system prompt construction that may embed credential strings |
| DSGAI16 | STRUCTURAL | Matches IDE plugin manifest patterns |
| DSGAI17 | STRUCTURAL | Matches absent retry/circuit-breaker patterns |
| DSGAI18 | STRUCTURAL | Matches absent guardrail import/decorator patterns |
| DSGAI19 | STRUCTURAL | Matches data labeling pipeline imports |
| DSGAI20 | STRUCTURAL | Matches absent rate-limiting decorator patterns |
| DSGAI21 | STRUCTURAL | Matches knowledge store connection patterns — URLs, not secrets |

### VALUE-BEARING SCAN PROTOCOL — Mandatory

For every scan tagged VALUE-BEARING (DSGAI02, 13, 14, 15), follow this protocol *exactly*. Violation leaks secrets into the report.

**Step V1 — Discover affected files only:**
Use the Grep tool with `output_mode="files_with_matches"`. This returns *only file paths*, never line content. Record the list of files.

**Step V2 — Get hit locations without content:**
For each file from V1, use the Grep tool with `output_mode="count"` to get the hit count per file. This returns counts only, never content.

**Step V3 — Locate specific line numbers:**
If you need precise line numbers (you do, for the report), run Grep with `output_mode="content"` and `-n` **only on the specific files identified in V1**, capturing the result into a single working variable that you process *in the same turn*.

**Step V4 — Immediately strip and discard:**
From each `file:line:content` returned in V3, extract only `file:line` and a fixed pattern-description string. **Never** write the `content` portion to any subsequent tool call — not Write, not Edit, not Bash, not the checkpoint JSON. Discard it from your working representation as soon as you have file+line.

**Step V5 — Render evidence:**
The only legitimate evidence rendering for VALUE-BEARING findings is:
```
<rendered-path>:<line> — <pattern_description> (value redacted — review file directly)
```
Where `<rendered-path>` follows the Obfuscation Mode rules in Step 4 (filename only in strict, full path in `--internal`).

**Step V6 — Checkpoint sanitization:**
`DSGAI-scan.json` MUST store VALUE-BEARING findings as `{"control": "DSGAI02", "path_rendered": "...", "line": 12, "pattern_id": "openai_api_key_hardcoded", "evidence_class": "value_bearing"}` — no `match_text` field, no `content` field, no `raw_grep_output` field. Ever.

---

### DSGAI01 Scan — Training Data Privacy [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`, `*.yaml`, `*.json`, `*.env*`

Patterns (PCRE, run all in parallel):
```
P01.1  PII scrubbing imports:         (anonymize|redact|scrub_pii|piiDetect|mask_pii|presidio)
P01.2  No-train flags:                (allow_training|training_opt_out|X-Training-Data|no_train)
P01.3  Output PII filter:             (filter_pii|remove_pii|output_sanitize|output_filter)
P01.4  Differential privacy lib:      (opacus|tensorflow\.privacy|dp-accounting|differential\.privacy)
P01.5  Consent / GDPR check:          (consent_capture|gdpr|ccpa|data_subject|lawful_basis)
```

### DSGAI02 Scan — Agentic Credential Management [VALUE-BEARING ⚠️]

**FOLLOW THE VALUE-BEARING SCAN PROTOCOL ABOVE.**

Files: `*.py`, `*.ts`, `*.js`, `*.java`, `*.kt`, `*.go`, `*.env*`, `*.yaml`, `*.yml`, `*.json`, `*.toml`, `*.cfg`

Patterns (PCRE):
```
P02.1  Hardcoded LLM API key (OpenAI):     (?i)(OPENAI_API_KEY|openai[._-]?api[._-]?key)\s*[:=]\s*["']sk-[A-Za-z0-9_\-]{20,}
P02.2  Hardcoded LLM API key (Anthropic):  (?i)(ANTHROPIC_API_KEY|anthropic[._-]?api[._-]?key)\s*[:=]\s*["']sk-ant-[A-Za-z0-9_\-]{20,}
P02.3  Hardcoded Cohere/Google/HF tokens:  (?i)(COHERE_API_KEY|GOOGLE_API_KEY|HF_TOKEN|HUGGINGFACE_TOKEN)\s*[:=]\s*["'][A-Za-z0-9_\-]{20,}
P02.4  Hardcoded AWS creds:                (AWS_ACCESS_KEY_ID|aws_access_key_id)\s*[:=]\s*["'][A-Z0-9]{16,}
P02.5  Hardcoded Azure/GCP cred:           (AZURE_OPENAI_KEY|GCP_SERVICE_ACCOUNT_KEY)\s*[:=]\s*["'][A-Za-z0-9_\-]{16,}
P02.6  Wildcard token scope (warn):        ("scope"\s*:\s*"\*|permissions[^\n]{0,30}\*|scope[^\n]{0,20}admin)
P02.7  Vault/secrets-manager (PASS):       (hvac\.Client|hashicorp/vault|VAULT_(ADDR|TOKEN|NAMESPACE)|secretsmanager\.|GetSecretValue|SecretManagerServiceClient|azure[._-]keyvault|@aws-sdk/client-secrets-manager)
P02.8  Tool-call signing (PASS):           (hmac|sign_request|verify_signature|tool_auth|mtls|mutual_tls)
```

Treat P02.1–P02.5 hits as FAIL evidence. P02.6 as WARN. P02.7–P02.8 as PASS signals. Render per V5.

### DSGAI03 Scan — Shadow AI Detection [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.go`, `*.yaml`, `*.json`, `*.env*`

```
P03.1  Third-party LLM endpoints:      (api\.openai\.com|api\.anthropic\.com|generativelanguage\.googleapis\.com|api\.cohere\.com|api\.together\.xyz|api\.mistral\.ai|api\.groq\.com)
P03.2  Internal LLM gateway (PASS):    (llm[._-]?gateway|ai[._-]?proxy|model[._-]?gateway|llm[._-]?proxy)
P03.3  DLP / classification check:     (dlp|data_classification|classify_data|sensitivity_check)
```

### DSGAI04 Scan — AI Supply Chain Security [STRUCTURAL]

Files: `*.py`, `*.sh`, `*.yml`, `*.yaml`, `Dockerfile`, `requirements*.txt`, `pyproject.toml`, `setup.py`

```
P04.1  Unsafe pickle (FAIL):           torch\.load\s*\(
P04.2  Safe pickle (PASS counter):     torch\.load\s*\([^)]*weights_only\s*=\s*True
P04.3  Artifact verification (PASS):   (sha256|verify_signature|model_hash|check_integrity)
P04.4  Unpinned ML deps (WARN):        ^(torch|transformers|tensorflow|langchain|openai|anthropic|llama-index)\s*(>=|~=|\^|>|<|<=|\*|latest)
P04.5  SBOM in CI (PASS):              (syft|cyclonedx|spdx|sbom)
P04.6  Trusted registry (PASS):        (index-url|extra-index-url|artifactory|jfrog|verdaccio)
P04.7  Hash-pinned install (PASS):     (--require-hashes|integrity\s*:\s*sha)
```

Run P04.1 and P04.2 then subtract — any `torch.load(` without `weights_only=True` is FAIL.

### DSGAI05 Scan — RAG Data Security [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`

```
P05.1  Document ingestion calls:       (loader\.load\(|ingest_document\(|add_documents\(|index_document\(|UnstructuredFileLoader|PyPDFLoader|DirectoryLoader)
P05.2  Access control (PASS):          (acl_filter|access_check|permitted_docs|filter\s*=.*tenant|namespace\s*=.*tenant)
P05.3  Tenant filter on search (PASS): (similarity_search|vector_search)[^)]{0,100}(filter|namespace|where)[^)]{0,40}tenant
P05.4  Integrity check on docs (PASS): (hashlib|sha256[^\n]{0,40}doc|integrity[._-]check|verify[._-]document)
P05.5  Chunk size limits (PASS):       (max_chunk_size|chunk_size\s*=|max_doc_size|content_limit)
P05.6  Path traversal risk:            (open\(.*\.\.|os\.path\.join\(.*request\.|Path\(.*request\.)
```

For P05.1, also check whether files in the same module contain P05.2 / P05.3 — absence = WARN; presence = PASS evidence.

### DSGAI06 Scan — MCP / Plugin Security [STRUCTURAL]

Files: `*.json`, `*.yaml`, `*.toml`, `*.py`, `*.ts`, `mcp.json`, `claude_desktop_config.json`

```
P06.1  Insecure MCP transport (FAIL):  ("url"\s*:\s*"http://|transport[^\n]{0,20}http://|"command"[^}]{0,200}--http(?!s))
P06.2  MCP auth (PASS):                (mcp[^\n]{0,30}(api_key|auth|bearer)|x-api-key[^\n]{0,20}mcp)
P06.3  Tool schema validation (PASS):  (jsonschema|pydantic[^\n]{0,30}validate|zod|schema[^\n]{0,20}tool|input_schema)
P06.4  Wildcard tool perms (WARN):     (tools\s*[:=]\s*\*|"tools"\s*:\s*"\*"|allow_all_tools)
P06.5  uvicorn bind-all + no auth:     uvicorn\.run\([^)]*host\s*=\s*["']0\.0\.0\.0
```

P06.5 alone is informational; combined with absence of P06.2 in the same module = FAIL.

### DSGAI07 Scan — Data Lifecycle / TTL [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`, `*.yaml`, `*.json`

```
P07.1  TTL config:                     (ttl\s*=|expires_in\s*=|max_age\s*=|RETENTION_DAYS|DATA_TTL|HISTORY_TTL)
P07.2  Session cleanup (PASS):         (delete_session|clear_history|purge_conversation|clear_memory|delete_conversation)
P07.3  Vector delete (PASS):           (delete_namespace|delete_collection|drop_index|delete_index|reset_collection)
P07.4  Right-to-erasure (PASS):        (gdpr_delete|erase_user_data|handle_deletion|right_to_erasure|forget_user)
```

Absence of all four in a multi-tenant or PII-handling repo = WARN.

### DSGAI08 Scan — Regulatory and Privacy Compliance [STRUCTURAL]

Files: `*.md`, `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`, `*.yaml`, `*.json`, `docs/**`, `appsec/**`, `security-review/**`

```
P08.1  DPIA / privacy assessment doc:  (DPIA|PIA|privacy_assessment|privacy[._-]impact)
P08.2  Data processing agreement ref:  (data_processing_agreement|DPA|sub_processor)
P08.3  Consent capture:                (consent_capture|capture_consent|consent_record|lawful_basis)
P08.4  EU AI Act annotation:           (ai_act_risk_level|high_risk_ai|limited_risk|minimal_risk)
P08.5  Audit logging:                  (audit_log|decision_log|audit_trail)
P08.6  Do-not-track honored:           (do_not_track|opt_out|DNT)
```

Absence of all six in a production GenAI service = WARN; absence in a high-risk EU AI Act use case = FAIL.

### DSGAI09 Scan — Multimodal AI Data Security [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`

Only run if multimodal models detected (vision endpoint, audio endpoint, OCR call sites). Otherwise mark NOT APPLICABLE.

```
P09.1  EXIF / metadata strip:          (strip_exif|remove_metadata|PIL\.Image|exifread|piexif)
P09.2  Image PII / moderation:         (detect_pii_in_image|content_filter|nsfw_detect|moderate_image)
P09.3  MIME / file type validation:    (allowed_types|mime_type_check|magic\.from_buffer|filetype\.guess)
P09.4  Size limit on upload:           (max_upload_size|MAX_FILE_SIZE|content[._-]length[._-]limit)
P09.5  Steganography detection:        (stego|steganography|stegano|lsb_detect)
```

P09.5 absence = note (advanced control). P09.1–P09.4 absence in a multimodal pipeline = WARN.

### DSGAI10 Scan — Synthetic Data Security [STRUCTURAL]

Files: `*.py`, `*.ipynb`, `*.r`

Only run if synthetic data generation is present (SDV, gretel, custom generator). Otherwise mark NOT APPLICABLE.

```
P10.1  Membership inference test:      (membership_inference|mia_test|mia_attack)
P10.2  Anonymity validation:           (k_anonymity|l_diversity|t_closeness|anonymization_check)
P10.3  Privacy-preserving lib:         (SDV|gretel|synthetic_data_vault|smartnoise)
P10.4  DP noise in generation:         (epsilon\s*=|noise_multiplier\s*=|dp_noise|laplace_noise|gaussian_noise)
P10.5  Re-identification risk note:    (reidentification_risk|reid_check|disclosure_risk)
```

Synthetic data pipeline without any of P10.1, P10.2, P10.4 = FAIL.

### DSGAI11 Scan — Multi-Tenant Data Isolation [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`

```
P11.1  Vector query call sites:        (similarity_search|max_marginal_relevance_search|as_retriever|(vectorstore|vector_store|retriever|index|collection|client)\.(query|search)\()
P11.2  Tenant filter present (PASS):   (namespace\s*=[^,)]{0,40}tenant|collection[^=]{0,20}=\s*f?["'][^"']*\{?tenant|filter\s*=\s*\{[^}]*tenant)
P11.3  Tenant verification (PASS):     (tenant_id\s*in\s*session|verify_tenant|assert_tenant|check_tenant|require_tenant)
P11.4  Cross-tenant cache risk:        (global[._-]cache|shared[._-]prompt[._-]cache|@cache(?!\s*\(.*tenant))
```

For every P11.1 match, verify P11.2 is present within ±15 lines in the same file. If absent, FAIL.

### DSGAI12 Scan — Database Agent Security [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`

```
P12.1  Raw LLM-output execution (FAIL): execute\([^)]*(llm|response|completion|output|generated)
P12.2  LangChain SQL agent (FAIL signal): (SQLDatabaseChain|create_sql_agent|SQLDatabaseToolkit)
P12.3  Parameterized query (PASS):     (cursor\.execute\([^)]+,\s*[\[\(]|prepareStatement|bindValue|:param)
P12.4  Read-only conn (PASS):          (read_only\s*=\s*True|readonly\s*=\s*True|read_only_connection|default_transaction_read_only)
P12.5  Query validator (PASS):         (validate_query|query_validator|safe_sql|sql_guard|sanitize_sql)
P12.6  DDL from agent (FAIL):          \b(DROP\s+TABLE|TRUNCATE|ALTER\s+TABLE|DELETE\s+FROM)\b
P12.7  Row limit (PASS):               (LIMIT\s+\d+|max_rows\s*=|fetch_limit\s*=)
```

P12.6 in migrations / fixtures / tests is benign — exclude paths matching `(migrations|fixtures|tests|/test/)` from FAIL classification.

### DSGAI13 Scan — Vector Store Security [VALUE-BEARING ⚠️]

**FOLLOW THE VALUE-BEARING SCAN PROTOCOL ABOVE.**

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`, `*.yaml`, `*.env*`

```
P13.1  Vector store auth configured:   (CHROMA_SERVER_AUTH|QDRANT_API_KEY|PINECONE_API_KEY|WEAVIATE_API_KEY|MILVUS_TOKEN|vectorstore[^\n]{0,30}api_key)
P13.2  TLS endpoints (PASS):           (https://[^"']*?(qdrant|weaviate|pinecone|chroma)|ssl\s*=\s*True|tls\s*=\s*True|grpcs://)
P13.3  Insecure binding (WARN):        (host[^\n]{0,15}0\.0\.0\.0|ALLOW_RESET\s*=\s*True|chroma[^\n]{0,30}http://localhost|qdrant[^\n]{0,30}http://localhost)
P13.4  Hardcoded vector token (FAIL):  (QDRANT_API_KEY|PINECONE_API_KEY|WEAVIATE_API_KEY)\s*=\s*["'][A-Za-z0-9_\-]{16,}
```

P13.4 is the value-bearing hit — render per V5 only.

### DSGAI14 Scan — AI Telemetry Security [VALUE-BEARING ⚠️]

**FOLLOW THE VALUE-BEARING SCAN PROTOCOL ABOVE.**

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.yaml`, `*.env*`

```
P14.1  Prompt logging disabled (PASS): (log_prompts\s*=\s*False|capture_content\s*=\s*False|OTEL_LOG_PROMPTS[^\n]{0,10}false|log_completions\s*=\s*False)
P14.2  Prompt logging enabled (WARN):  (log_prompts\s*=\s*True|capture_content\s*=\s*True|log_full_response\s*=\s*True)
P14.3  PII redaction in log (PASS):    (redact_pii|mask_sensitive|sanitize_log|scrub[^\n]{0,10}log|log[^\n]{0,10}redact)
P14.4  Raw response print (WARN):      (print\((response|completion)|console\.log\((response|completion)|logger\.(debug|info)\([^)]*(response|completion))
P14.5  LangSmith / Langfuse config:    (LANGSMITH_API_KEY|LANGFUSE_PUBLIC_KEY|langfuse[^\n]{0,20}init|langsmith[^\n]{0,20}trace)
```

P14.4 may contain inline PII in the format string — treat as VALUE-BEARING.

### DSGAI15 Scan — Context Window Security [VALUE-BEARING ⚠️]

**FOLLOW THE VALUE-BEARING SCAN PROTOCOL ABOVE.**

Files: `*.py`, `*.ts`, `*.java`, `*.kt`

```
P15.1  Secret in system prompt (FAIL): (system_prompt|system_message)\s*=\s*["'][^"']*(api_key|password|secret|token|sk-)
P15.2  Context size limit (PASS):      (max_context_length\s*=|context_window_limit\s*=|max_context_tokens\s*=|truncate_context)
P15.3  Prompt from config (PASS):      (system_prompt|system_message)[^\n]{0,40}(config|vault|os\.environ|getenv|secret_manager)
P15.4  Over-fetch aggregation (WARN):  (customer_360|user_profile_all|fetch_all_user_data|get_full_profile|select\s*\*\s*from\s+users)
```

### DSGAI16 Scan — IDE Plugin and Extension Security [STRUCTURAL]

Files: `.copilotignore`, `.aiignore`, `.cursorignore`, `.continueignore`, `.codeiumignore`, `.vscode/settings.json`, `cursor.json`, `continue.json`

```
P16.1  AI-ignore file present (PASS):  filename match: (\.(copilot|ai|cursor|continue|codeium)ignore)
P16.2  Sensitive paths excluded:       in any ignore file: (\.env|secrets|credentials|\.aws|\.ssh|private_key)
P16.3  Telemetry off (PASS):           (telemetry[^\n]{0,10}(off|false|disabled)|share_data\s*[:=]\s*false)
P16.4  Context scope limits:           (contextWindow|ignorePaths|excludeFiles|maxContextLines)
```

Absence of P16.1 in a repo with `.env` or `secrets/` directory = WARN.

### DSGAI17 Scan — System Resilience and Availability [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`

```
P17.1  Circuit breaker (PASS):         (CircuitBreaker|@circuit|tenacity|resilience4j|pybreaker)
P17.2  Retry with backoff (PASS):      (retry\s*\(|@retry|exponential_backoff|max_retries\s*=|backoff_factor\s*=|retry_with_backoff)
P17.3  Timeout on LLM call (PASS):     (timeout\s*=\s*\d|request_timeout\s*=|httpx\.[^\n]{0,30}timeout)
P17.4  Rate limit incoming (PASS):     (rate_limit|@throttle|RateLimiter|slowapi|flask_limiter|express-rate-limit)
P17.5  Fallback response (PASS):       (fallback_response|default_response|graceful_degradation|on_failure_return)
P17.6  Unbounded retry (FAIL):         while\s+True[^}]{0,200}(generate|complete|chat)|retry\s*\(\s*\)
```

LLM-calling module with none of P17.1–P17.5 = WARN.

### DSGAI18 Scan — Model Output Security [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`

```
P18.1  Output guardrails (PASS):       (guardrails|nemo[._-]guardrails|llm_guard|output_guard|filter_output|sanitize_response|moderation)
P18.2  PII detection on output:        (detect_pii[^\n]{0,20}output|output[^\n]{0,20}detect_pii|presidio[^\n]{0,20}output|scan_output)
P18.3  Logprobs exposed (WARN):        (logprobs\s*=\s*True|return_logprobs\s*=\s*True|include_logprobs\s*=\s*True|top_logprobs\s*=\s*\d)
P18.4  LLM call sites (count):         (\.chat\.completions\.create|client\.messages\.create|openai\.ChatCompletion|anthropic\.messages|generate_content|chat\.complete)
P18.5  max_tokens set (PASS):          max_tokens\s*=\s*\d+
```

For every P18.4 match, verify P18.5 is present in the same call expression (within ±10 lines). Absent max_tokens on a production LLM call = WARN.

### DSGAI19 Scan — AI Data Labeling Security [STRUCTURAL]

Files: `*.py`, `*.ipynb`, `*.ts`, `*.yaml`

Only run if labeling platform integration detected. Otherwise mark NOT APPLICABLE.

```
P19.1  Anonymization before export:    (anonymize_for_labeling|pseudonymize|redact_before_export|mask_for_labeling)
P19.2  Labeling SDK auth from vault:   (label_studio[^\n]{0,30}vault|labelbox[^\n]{0,30}secret|scale_api_key[^\n]{0,30}(vault|env))
P19.3  Labeling access audit:          (label[._-]audit|labeling_access_log|annotator_audit)
P19.4  Re-identification post-label:   (reid_check_post_label|labeling_reidentification|post_label_validation)
```

Labeling export without P19.1 = FAIL.

### DSGAI20 Scan — Inference API Security [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`, `*.go`

```
P20.1  API auth required (PASS):       (api_key[^\n]{0,15}(verify|validate)|bearer_token[^\n]{0,15}validate|Authorization[^\n]{0,15}required|@require_auth|auth_middleware|Depends\(.*auth)
P20.2  Rate limit (PASS):              (rate_limit|RateLimiter|@throttle|slowapi|flask_limiter|express-rate-limit|@limiter\.limit)
P20.3  Input length validation (PASS): (max_input_length\s*=|max_input_tokens\s*=|input[._-]truncat|validate[._-]length)
P20.4  Prompt injection detect (PASS): (prompt_injection_detect|detect_injection|llm_guard|rebuff|input_guard|nemo[._-]guard)
P20.5  Inference endpoint (count):     (@app\.(post|get)\(["'][^"']*(chat|generate|completion|infer|predict)|@router\.(post|get)\(["'][^"']*(chat|generate|completion|infer|predict)|app\.(post|get)\(["'][^"']*(chat|generate|completion|infer|predict))
```

For every P20.5 inference endpoint, verify P20.1 and P20.2 are nearby. Both absent = FAIL.

### DSGAI21 Scan — Knowledge Store Security [STRUCTURAL]

Files: `*.py`, `*.ts`, `*.java`, `*.kt`

```
P21.1  Read-only retrieval (PASS):     (read_only\s*=\s*True|readonly\s*=\s*True|HttpMethod\.GET|http_method[^\n]{0,10}get)
P21.2  KB write from agent (WARN):     (chromadb|qdrant|pinecone|weaviate|knowledge_base|kb_client)[^\n]{0,40}\.(upsert|insert|update|delete|add_documents|write)\(
P21.3  Write content validation:       (validate_content|sanitize[._-]write|verify[._-]knowledge|content[._-]check[._-]write)
P21.4  KB versioning (PASS):           (versioned\s*=\s*True|audit_writes|version_id|kb_audit|knowledge[._-]audit)
```

P21.2 in an agent module without P21.3 = WARN.

---

## Step 3: Classify Findings

For each of the 21 DSGAI risks, assign a status:

**PASS** — Mitigations are present and correctly implemented. Evidence found in code.

**WARN (Needs Review)** — Partial mitigations present, or pattern detected that requires manual confirmation. Examples:
- TTL config present but value may be excessive
- Authentication present but scope/privilege not verifiable from code alone
- Third-party LLM endpoint hardcoded (may be authorized — needs registry confirmation)
- Verbose logging enabled but only in DEBUG level

**FAIL** — Clear violation of a DSGAI control detectable from code. Examples:
- Hardcoded LLM API key in source file
- `torch.load()` without `weights_only=True`
- Raw LLM SQL execution without validation
- Vector store connection over `http://` without authentication
- Full prompt/response logging to external telemetry with no PII scrubbing
- No tenant isolation on multi-tenant RAG queries

**NOT VALIDATED** — Control cannot be assessed from code alone. Manual review required:
- Training data PII inventory (external data asset)
- Actual rotation dates for agent credentials (runtime, not visible in code)
- Vendor data processing agreements (legal, not in code)
- Red team / adversarial testing conducted (process evidence)
- Labeling platform access controls (external SaaS config)

**NOT APPLICABLE** — Control is not relevant to this repository:
- DSGAI09 (Multimodal) if repo processes only text
- DSGAI10 (Synthetic Data) if repo does not generate synthetic training data
- DSGAI19 (Data Labeling) if repo has no labeling pipeline
- DSGAI16 (IDE Plugins) if repo is a backend service with no developer tooling component
- DSGAI03 (Shadow AI) if all LLM calls already route through approved internal gateway

**VENDOR ATTESTATION REQUIRED** — For controls tagged `[BUY]` or the `[BUY]` portion of `[BOTH]`, the code scan cannot determine compliance. Emit a callout listing the specific attestations needed (from the per-control "BUY-side" notes above) so the team can request them from the vendor.

Also flag:
- **DSGAI Registry Gap** — static secrets (API keys, tokens) used by AI components that have no corresponding entry in a secrets registry
- **DSGAI Tenant Boundary Gap** — multi-tenant repo where at least one vector query is missing a tenant filter

---

## Step 4: Generate HTML Report

### Obfuscation Mode

Determine `OBFUSCATION` from `$ARGUMENTS`:

- `OBFUSCATION = "strict"` (default, no `--internal` flag) — render evidence as `<filename>:<line>` where `<filename>` is only the basename (e.g. `config.py:12`). Intermediate directories are dropped. The report is safe to share with auditors, attach to a Jira ticket, or store in a public repo.
- `OBFUSCATION = "internal"` (`--internal` flag passed) — render evidence as `<relative/path/from/repo/root>:<line>` (e.g. `app/services/agent/config.py:12`). For internal team use.

In **both** modes, VALUE-BEARING match content is *never* displayed — only the file location and pattern description. The only difference between modes is path detail.

Render an "Obfuscation Mode" badge in the report header: 🛡️ `STRICT` (green) or 🔓 `INTERNAL` (yellow).

### Evidence Redaction Rule (Mandatory)

Before writing any evidence block in the report, check the scan classification from the Step 2 table.

**For VALUE-BEARING scans (DSGAI02, DSGAI13, DSGAI14, DSGAI15):**
Never reproduce the matched line. Output only the rendered path, line number, and a description of what was found:

```
config.py:12 — hardcoded OpenAI API key pattern detected (value redacted — review file directly)
config.py:18 — hardcoded vector store auth token pattern detected (value redacted — review file directly)
logging.py:28 — prompt logging statement detected (content redacted — review file directly)
```

This rule applies *regardless* of whether the matched value looks like a demo, test, or placeholder. The report may be shared with stakeholders, auditors, or stored where the actual value must not appear.

**For all STRUCTURAL scans (DSGAI01, DSGAI03–DSGAI12, DSGAI16–DSGAI21):**
Reproduce the matched line **only if** it does not contain a recognizable secret pattern. Apply a final defense-in-depth sweep before writing any STRUCTURAL evidence line: if the line contains any of `sk-`, `sk-ant-`, `AKIA`, `Bearer\s+[A-Za-z0-9]{20,}`, `password\s*=`, `api[._-]?key\s*=\s*["'][^"']{12,}`, redact it as if it were VALUE-BEARING.

### Checkpoint File Privacy

`DSGAI-scan.json` is the intermediate state file. It MUST contain:
```json
{
  "control": "DSGAI02",
  "path_rendered": "config.py",        // already mode-redacted
  "path_internal": "app/config.py",    // only present when OBFUSCATION=internal
  "line": 12,
  "pattern_id": "openai_api_key_hardcoded",
  "evidence_class": "value_bearing",
  "status": "FAIL"
}
```

It MUST NOT contain: `match_text`, `raw_grep_output`, `content`, `value`, full file dumps, or any field that could carry the matched secret. Same redaction rules as the HTML report.

If `OBFUSCATION=strict`, omit the `path_internal` field entirely — strict mode produces a checkpoint that is itself safe to share.

---

### Three-Part Write Protocol

Generate a self-contained HTML report saved as `DSGAI-report.html` in the repository root.

**IMPORTANT — write in 3 sequential parts to avoid context window exhaustion. Do NOT print or narrate any HTML in the response text at any point.**

1. **Write Part 1** using the Write tool: `<!DOCTYPE html>` through the end of the Dashboard + Compliance Bar section. End the file with the exact comment `<!-- FINDINGS_PLACEHOLDER -->`.
2. **Edit Part 2**: Use the Edit tool to replace `<!-- FINDINGS_PLACEHOLDER -->` with the AI Component Inventory, Scope Legend, Summary Table, all 21 finding cards, Recommendations, and Checklist sections. End the replacement with the exact comment `<!-- CVE_PLACEHOLDER -->`.
3. **Edit Part 3**: Use the Edit tool to replace `<!-- CVE_PLACEHOLDER -->` with the full CVE Advisory section, footer, `</body>`, and `</html>`.

This three-part approach keeps each tool call well within the context limit regardless of repo size.

Open after saving:

```
# macOS
open DSGAI-report.html
# Linux
xdg-open DSGAI-report.html
# Windows (PowerShell)
Start-Process DSGAI-report.html
# Windows (cmd)
start DSGAI-report.html
```

---

### Report Structure

Two main sections with shared header/footer:

- **Section 1 — DSGAI Compliance** (the 21 data security risk findings)
- **Section 2 — CVE Advisory** (live vulnerability intelligence per package)

**PDF-first design:** The report must render correctly when printed to PDF via Ctrl+P/Cmd+P. This means:

- No sticky/fixed positioning (nav bar is static, not `position: sticky`)
- All finding cards always visible (`display: block`) — never collapsed/hidden
- No interactive filter buttons that hide content
- No JavaScript-based collapse/expand on findings or CVE cards
- `page-break-inside: avoid` on every card, table, and section block
- `-webkit-print-color-adjust: exact; print-color-adjust: exact` on body so colours survive print

#### Shared scaffolding (top)

1. **Header** — Report title "OWASP DSGAI Data Security Compliance Report", service/repo name, generation date, framework version (OWASP GenAI Data Security Risks and Mitigations v1.0, March 2026), **Obfuscation Mode badge** (🛡️ STRICT or 🔓 INTERNAL).

2. **Section nav bar** (static, not sticky) — Two labels: `Section 1: DSGAI Compliance` | `Section 2: CVE Advisory` as anchor links.

3. **About This Report** — Placed immediately after the nav bar, before the executive summary. Contains **four subsections**, each rendered as a distinct `<h3>` block. Do NOT compress or merge them.

   **Goal** — This report scans a software codebase against the **OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0)** — a framework published by the Open Worldwide Application Security Project (OWASP) in March 2026 that defines 21 data security risks specific to GenAI and agentic systems. The goal is to **automatically detect OWASP GenAI data security risks and make it easier for teams** to act on them — without requiring every developer or reviewer to manually read and interpret the full OWASP specification. Beyond detection:
   - **Shift-left security** — catches risks at development time, not at pen test or production incident time
   - **Consistent coverage** — eliminates human variance in manual reviews; every scan checks all 21 controls every time
   - **Live CVE intelligence** — cross-references the repo's exact dependency versions against live vulnerability databases
   - **Audit-ready output** — generates a shareable, self-contained HTML report that serves as documented evidence of a review against a published standard
   - **CI/CD integration ready** — can be run on every pull request or release branch
   - **Prioritised remediation backlog** — findings are tiered so teams know what to fix today versus what goes into the architecture backlog

   **How It Works** — The scan runs in four phases: (1) Repository detection — confirms GenAI/agentic patterns are present; (2) Live CVE enrichment — queries OSV, NVD, and GitHub Advisory Database for the exact package versions in use; (3) Code pattern scan — searches source files for OWASP 21 DSGAI risk indicators; (4) Findings classification — each control is rated FAIL / WARN / PASS / NOT VALIDATED / NOT APPLICABLE / VENDOR ATTESTATION REQUIRED with file paths, line numbers, and remediation steps.

   **Privacy & Data Handling** — This scan runs entirely on your local machine. Your source code, configuration files, and secrets are never uploaded, transmitted, or shared with any external service. The only outbound requests are package name and version lookups (e.g. `langchain==0.1.0`) sent to public CVE databases — [OSV](https://osv.dev), [NVD](https://nvd.nist.gov), and [GitHub Advisory Database](https://github.com/advisories). No actual code leaves your machine. Live CVE lookups are optional; with `--no-cve` or no internet access, the scan falls back to its embedded CVE database. In **STRICT** mode (default), evidence is rendered as filename + line only, and value-bearing matches (credentials, tokens, PII-in-logs) are never displayed — the report is safe to share with auditors, attach to a ticket, or store in a public repo. In **INTERNAL** mode (`--internal`), full file paths are restored; value-bearing match content is *still* never displayed.

   **Who Benefits** — Render as a table:
   | Audience | How this report helps |
   | --- | --- |
   | **Security practitioners** | Audit-ready evidence of GenAI data security posture mapped to a published OWASP standard. Identifies FAIL items that need immediate remediation. |
   | **Developers** | Pinpoints exactly which files and lines introduce risk, with concrete fix instructions. No need to read the full OWASP document — the relevant control and remediation is surfaced inline. |
   | **Security architects** | Risk posture snapshot across the full GenAI data lifecycle — from training data ingestion through inference API exposure — enabling prioritised architecture decisions. |
   | **Engineering managers** | Dashboard and compliance bar give an at-a-glance view of team posture; tiered recommendation cards translate findings into a prioritised backlog. |
   | **Compliance / GRC** | Evidence package mappable to GDPR, EU AI Act, SOC 2, ISO 42001. Vendor Attestation Required callouts identify what to request from third parties. |

4. **Executive Summary** — One opening sentence on overall posture, then **bullet points** (not a paragraph) covering: key FAIL findings, AI components identified, CVE posture, vendor attestations needed. Followed by a **standalone highlighted callout box** for the recommended remediation priority order.

5. **Dashboard Cards row** — single row of cards spanning both sections:
   - DSGAI checks: Total (21) | PASS | WARN | FAIL | NOT VALIDATED | NOT APPLICABLE | VENDOR ATTESTATION
   - CVE cards: Exploitable CVEs | Patched CVEs | Unknown CVEs

6. **Compliance Bar** — Visual bar showing PASS / WARN / FAIL / NV distribution across the 21 controls.

#### Section 1 — DSGAI Compliance

7. **AI Component Inventory** — Detected frameworks, vector stores, LLM providers, MCP servers, data pipelines; each shown as a chip/tag.

8. **Scope Tag Legend** — Compact box, three items:
   - **BUILD** — your team implements this control in the codebase
   - **BUY** — the LLM provider / SaaS vendor is responsible — vendor attestation required
   - **BOTH** — shared responsibility between your code and the provider

9. **Summary Table** — Appears **before** detailed findings. Columns: Risk ID | Risk Name | Scope | Tier | Status | Key Evidence.

10. **AI Attack Techniques Relevant to This Stack** (from MITRE ATLAS, Sub-step E) — Compact table: ATLAS ID | Technique | Maps to DSGAI | One-line description. Render only if at least one relevant technique was found.

11. **Detailed Findings** — One card per DSGAI risk (DSGAI01–DSGAI21), always fully visible (no collapse/expand JS):
   - Status badge: PASS / WARN / FAIL / NOT VALIDATED / NOT APPLICABLE / VENDOR ATTESTATION REQUIRED
   - Risk ID + title + Scope tag (BUILD / BUY / BOTH) + Tier badges (Tier 1 / Tier 2 / Tier 3)
   - Body: evidence (mode-redacted file paths + line numbers), risk explanation, specific remediation steps
   - Inline CVE pills for any CVEs mapped to this risk
   - For BUY portions: "Vendor Attestation Required" callout listing specific attestations to request

12. **Recommendations** — Prioritized action cards:
    - **Fix today — Tier 1 (red):** FAIL items + EXPLOITABLE CVEs affecting this repo
    - **Architecture backlog — Tier 2 (yellow):** WARN items + Tier 2 architecture changes
    - **Mature program — Tier 3 (blue):** NOT VALIDATED items needing red-team, DP, or process maturity
    - **Vendor attestations to request — (purple):** consolidated list from all BUY/BOTH controls

13. **DSGAI Compliance Artifacts Checklist**:
    - [ ] AI component inventory documented
    - [ ] All LLM API keys stored in approved secret store (not hardcoded)
    - [ ] PII scrubbing in place before training/fine-tuning ingestion
    - [ ] Multi-tenant isolation enforced in RAG and vector queries
    - [ ] Vector store authenticated and TLS-enabled
    - [ ] AI telemetry does not log full prompts/completions in production
    - [ ] Model artifact integrity verified (checksums/signatures)
    - [ ] Output guardrails or moderation layer deployed
    - [ ] Inference API authenticated and rate-limited
    - [ ] Data lifecycle TTLs configured for sessions, history, embeddings
    - [ ] No hardcoded secrets in system prompts
    - [ ] AppSec Threat Modeling completed for AI components
    - [ ] Static secrets registry maintained for all AI-system credentials
    - [ ] Vendor attestations collected for all BUY/BOTH controls
    - [ ] DSGAI scan integrated into CI/CD pipeline

   Mark items ✅ if evidence found, ⚠️ if partially evidenced, ❌ if missing.

#### Section 2 — CVE Advisory

14. **CVE enrichment status banner** — One of:
    - ✅ Online — queried OSV + NVD + GitHub Advisory + AVID at `<timestamp>`
    - ⚠️ Partial — some sources unreachable; results may be incomplete (list which sources failed)
    - ❌ Offline — network unavailable or `--no-cve` passed; showing embedded CVEs only

15. **Package Inventory Table** — All AI/ML packages detected in the repo:
    | Package | Ecosystem | Version in repo | Pinned? | Queried sources |

16. **CVE summary counts bar** — Compact stat row: `X CVEs found · Y Exploitable · Z Not Affected · W Unknown`. Exploitable in red, Not Affected in green, Unknown in gray.

17. **CVE Groups — organised by DSGAI Risk** (all always visible — no collapse JS):

    One group per DSGAI risk that has at least one CVE. Each group:
    - **Group header**: left-border accent bar + DSGAI risk ID + risk name + count badge (e.g. `DSGAI13 — Vector Store Security  [1 CVE · NOT AFFECTED]`)
      - Header accent: red if any EXPLOITABLE, yellow if any UNKNOWN, green if all NOT AFFECTED
    - **CVE card(s)** inside the group, one per CVE:
      - CVE ID in monospace + CVSS score badge + status pill (🔴 EXPLOITABLE / ✅ NOT AFFECTED / ⚠️ UNKNOWN)
      - Package name + repo version
      - One-line description
      - Three version lines: `Affects: <X.Y.Z` · `Fixed: X.Y.Z` · `Repo: A.B.C`
      - Published date + Source (NVD / OSV / GitHub / AVID / Embedded)
    - If a CVE maps to **multiple DSGAI risks** (e.g. DSGAI01 · DSGAI18), show it under a combined group header listing both IDs.

    **Why grouped by DSGAI risk:** A reader can cross-reference Section 1 findings with Section 2 CVEs. A FAIL on DSGAI12 in Section 1 immediately connects to an EXPLOITABLE CVE under DSGAI12 in Section 2 — remediation priority unambiguous.

18. **DSGAI Risk Reference grid** — Compact grid showing all 21 risks: ID | one-line description | Scope | Tier | key embedded CVE.

#### Shared scaffolding (bottom)

19. **Footer** — Generation date, framework version (OWASP DSGAI v1.0), CVE sources queried, Obfuscation mode used, print-to-PDF instructions. Must include attribution on a separate line:

    > Original work by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org/initiative/data-security/), led by [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/) | Skill adaptation by [Harish Ramachandran](https://www.linkedin.com/in/harish-ramachandran-a8026443/)

    Both names MUST be hyperlinks — do not render either as plain text.

---

### Styling

- CSS variables, all inline, **no external dependencies, no CDN, no external fonts**
- Color scheme:
  - GREEN `#16a34a` (pass)
  - YELLOW `#ca8a04` (warn)
  - RED `#dc2626` (fail)
  - BLUE `#2563eb` (not validated)
  - GRAY `#6b7280` (not applicable)
  - PURPLE `#7c3aed` (vendor attestation / info)
- Dark gradient header: `#1e1b4b` → `#312e81` → `#1e3a5f`
- White card sections with subtle shadows, rounded borders (`border-radius: 12px`)
- Monospace font (`Menlo, Consolas, "Liberation Mono", monospace`) for file paths, pattern IDs, CVE IDs
- Tier badges: Tier 1 = red pill, Tier 2 = yellow pill, Tier 3 = blue pill
- CVE badges: status-coloured background, monospace text
- Obfuscation mode badge: STRICT = green shield, INTERNAL = yellow unlocked
- **No interactive JS for hide/show content.** All findings always visible. Print-friendly by construction.
- `@media print` rules ensure colours survive PDF export and cards do not break across pages

---

## Step 5: PDF Export

The HTML report includes a tuned `@media print` stylesheet. To generate a PDF:

**Option 1 — Browser print (simplest):**
Open `DSGAI-report.html` in Chrome or Edge, press `Ctrl+P` (Windows/Linux) or `Cmd+P` (macOS), select **Save as PDF**. All finding cards expand automatically for print.

**Option 2 — Chrome headless (scriptable):**

```bash
# macOS
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --print-to-pdf=DSGAI-report.pdf \
  --print-to-pdf-no-header "file://$(pwd)/DSGAI-report.html"

# Linux
google-chrome --headless=new --print-to-pdf=DSGAI-report.pdf \
  --print-to-pdf-no-header "file://$(pwd)/DSGAI-report.html"
```

```powershell
# Windows (PowerShell)
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless=new --print-to-pdf=DSGAI-report.pdf `
  --print-to-pdf-no-header "file:///$((Get-Location).Path)/DSGAI-report.html"
```

---

## Notes for the Analyst

- **STRICT vs INTERNAL mode:** Strict is the default for a reason — it produces a report that any auditor or stakeholder can read without you worrying about path or secret exposure. Use `--internal` only when the report stays inside the team's working copy.
- **VALUE-BEARING discipline:** The matched line for a value-bearing pattern is never written *anywhere* — not the HTML report, not `DSGAI-scan.json`, not your conversation summary, not a follow-up message. Follow the Step V1–V6 protocol exactly.
- **BUY vs BUILD scope:** For repos that only *consume* an LLM API (BUY), the BUY-tagged portions of `[BOTH]` controls emit a `VENDOR ATTESTATION REQUIRED` badge — they are not FAILs.
- **NOT VALIDATED vs FAIL:** If a critical control (DSGAI02 agent credentials, DSGAI11 tenant isolation) has no evidence either way, prefer FAIL over NOT VALIDATED — absence of a security control is a finding.
- **Torch / pickle:** `torch.load()` without `weights_only=True` is FAIL in PyTorch < 2.0 (insecure default). In 2.0+ the default changed to `True` — check the pinned torch version if ambiguous.
- **Vector store defaults:** Chroma default config (`chromadb.Client()` with no auth) is unauthenticated and accepts connections on localhost — WARN in dev, FAIL in any deployment that exposes the port.
- **Multi-tenant check:** For DSGAI11, look at *every* vector store query call. If even one `similarity_search()` is missing a tenant filter, that is a FAIL.
- **LangChain SQL agents:** LangChain's `SQLDatabaseChain` and `create_sql_agent` execute LLM-generated SQL. FAIL for DSGAI12 unless a query validator wraps every execution.
- **Integration test credentials:** Often injected via a secrets manager or CI/CD env vars — flag for registry entry and rotation verification.
- **AppSec artifacts:** Check `appsec/`, `security-review/`, or equivalent for security architecture review evidence. If absent and this is a production GenAI service, WARN on DSGAI08.
- **MCP transport:** Any MCP server config pointing to `http://` (non-TLS) in a non-localhost context is FAIL for DSGAI06.
- **Telemetry:** LangSmith, Langfuse, Arize, Weights & Biases — if present with `capture_content=True` and no PII redaction, WARN/FAIL depending on whether production data flows through.

---

## Known Limitations — What This Scanner Won't Catch

This skill is a **static pattern scanner**. Be honest with your stakeholders about what that means it cannot detect on its own — these gaps require human review, dynamic analysis, or process evidence:

- **Runtime behaviour.** Whether a key is *actually* rotated, whether a vault lookup *actually* returns a scoped credential, whether rate limits *actually* fire under load — none of this is visible in source. Pair with runtime audits.
- **Data-asset privacy.** The contents of training datasets, fine-tuning corpora, and embedding stores are not in the repo. DSGAI01 / DSGAI19 require a data inventory the scanner cannot enumerate.
- **Cross-service tenant isolation.** The scanner checks for tenant filters at vector query call sites (DSGAI11) — it cannot prove that downstream services, caches, or third-party APIs honor the tenant boundary end-to-end.
- **Prompt-injection robustness.** No static pattern catches a clever indirect prompt injection. DSGAI20 detects *whether a defense exists*, not whether it works against an adversary. Red-team testing is required.
- **Semantic correctness of guardrails.** The scanner sees that `guardrails` is imported and called (DSGAI18). It cannot tell whether the configured policies actually block the content classes you care about.
- **Vendor side of `[BOTH]` controls.** SOC 2, ISO 27001, DPAs, sub-processor lists, training-data opt-out enforcement on the provider's side — these emit `VENDOR ATTESTATION REQUIRED` and need documents from the vendor.
- **Encrypted or templated configuration.** If credentials live in Helm value files, sealed secrets, or environment-variable templating systems (Ansible/Terraform/Pulumi state), the literal value won't appear in source and the scanner correctly won't flag it — but you still need to verify the rendered runtime config is safe.
- **Languages beyond Python / JS-TS / Java / Kotlin / Go.** Rust, C#, PHP, Ruby AI integrations exist; patterns may need extending. Contributions welcome.
- **Binary / packaged assets.** Model weights, serialized embeddings, container layers — DSGAI04 flags the call patterns; deep artifact provenance auditing requires tools like cosign / in-toto / Sigstore.
- **Generated code.** If your codebase has large auto-generated blocks (protobuf, OpenAPI stubs), false positives may appear. Use `--scope` to exclude generated directories.

**Use the scanner to remove the 80% of issues that are mechanically detectable, so human reviewers can focus on the remaining 20%.** It is not a substitute for AppSec review on production GenAI systems.

---

## License

This skill is based on materials licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

**Original work:** OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026) by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org/initiative/data-security/), led by [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/).

**This adaptation:** Created by [Harish Ramachandran](https://www.linkedin.com/in/harish-ramachandran-a8026443/). You are free to share and adapt this skill for any purpose, including commercial use, under the same CC BY-SA 4.0 terms.
