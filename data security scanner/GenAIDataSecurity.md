# /GenAIDataSecurity — OWASP GenAI Data Security Compliance Report

---
**Description:** A Claude Code slash command skill that automatically scans GenAI and agentic codebases against the OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0) specification, covering all 21 DSGAI risk controls across the full GenAI data lifecycle.
**Based on:** OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026) — https://owasp.org/www-project-top-10-for-large-language-model-applications/
**Privacy:** Your source code never leaves your machine — only package names and versions are sent to public CVE databases during live enrichment. See README for full details.

**Changelog:**

- v0.1 (Apr 2026) — Initial release. Covers all 21 DSGAI risks. Live CVE enrichment via OSV, NVD, and GitHub Advisory Database. Multi-source vulnerability classification (EXPLOITABLE / NOT AFFECTED / UNKNOWN). HTML report with grouped CVE advisory panel.

---

Generate a **DSGAI Data Security Compliance Report** for the current repository. This assesses a GenAI or agentic system codebase against the **OWASP GenAI Data Security Risks and Mitigations 2026** (v1.0, March 2026) — 21 risks covering the full GenAI data lifecycle.

**Scope annotation:** Controls are tagged by who implements them — `[BUILD]` (in-house code), `[BUY]` (SaaS/API-consumed model), `[BOTH]`.

---

## Step 0: Verify Repository is a GenAI / Agentic System

Before scanning, confirm the repo contains GenAI-relevant code. Search for any of:

**LLM / AI frameworks:**
- Python: `openai`, `anthropic`, `langchain`, `llama_index`, `llamaindex`, `transformers`, `torch`, `tensorflow`, `huggingface`, `litellm`, `mistral`, `together`, `cohere`, `groq`, `vertexai`, `bedrock`
- Java/Kotlin: `LangChain4j`, `spring-ai`, `aws-bedrock`, `openai-java`
- JavaScript/TypeScript: `openai`, `@anthropic-ai`, `langchain`, `ai` (Vercel AI SDK), `@huggingface`
- Go: `github.com/sashabaranov/go-openai`, `github.com/tmc/langchaingo`

**Agentic / RAG patterns:**
- `AgentExecutor`, `Tool`, `@tool`, `tool_call`, `function_call`, `MCP`, `ModelContextProtocol`
- `VectorStore`, `Chroma`, `Pinecone`, `Weaviate`, `Qdrant`, `pgvector`, `FAISS`, `Milvus`
- `RAG`, `Retrieval`, `Embeddings`, `embed_documents`, `similarity_search`, `retriever`

If **none of these signals are present**, note that the repo does not appear to be an AI/agentic system and generate a minimal report indicating `NOT APPLICABLE` for all 21 controls.

If signals are present, proceed with the full scan.

---

## Step 0.5: Dynamic CVE Enrichment

Before scanning for DSGAI controls, extract the repo's AI/ML package inventory and fetch live CVE data from multiple vulnerability sources. This supplements the embedded CVEs already in each DSGAI risk section with findings specific to the versions this repo actually uses.

### Sub-step A: Extract AI Package Inventory

Read dependency files and extract package name + pinned version for every AI/ML-relevant package:

**Python** — read `requirements.txt`, `requirements*.txt`, `Pipfile`, `pyproject.toml`, `setup.py`:
```
grep -in "openai\|anthropic\|langchain\|llama.index\|llamaindex\|transformers\|torch\|tensorflow\|huggingface\|litellm\|cohere\|groq\|mistral\|together\|chromadb\|qdrant\|pinecone\|weaviate\|faiss\|milvus\|pgvector\|langfuse\|langsmith\|guardrails\|nemo.guardrails\|presidio\|llm.guard\|rebuff\|opacus\|sdv\|gretel" requirements*.txt Pipfile pyproject.toml setup.py 2>/dev/null
```

**JavaScript/TypeScript** — read `package.json` (dependencies + devDependencies):
```
grep -in "openai\|anthropic\|langchain\|huggingface\|ai\|@xenova\|chromadb\|qdrant\|pinecone\|weaviate\|faiss" package.json 2>/dev/null
```

**Java/Kotlin** — read `pom.xml`, `build.gradle`, `build.gradle.kts`:
```
grep -in "langchain4j\|spring-ai\|aws-bedrock\|openai\|anthropic" pom.xml build.gradle build.gradle.kts 2>/dev/null
```

Build a table: `Package | Version | Language`. If version is unpinned (e.g., `>=`, `^`, `*`), note "unpinned — latest assumed".

---

### Sub-step B: Query Live Vulnerability Sources

**Parallel execution:** Fire all CVE source queries simultaneously — send OSV, NVD, and GitHub Advisory requests as parallel tool calls in a single message. Do not wait for one source to complete before starting the next. This reduces CVE enrichment time from sequential minutes to a single round-trip.

Query all five sources below for each package in the inventory. Run all sources and deduplicate results by CVE ID (keep highest-confidence entry, note all sources).

#### Source 1 — OSV (Open Source Vulnerabilities) — Primary

Best precision: exact package + version match. POST to the OSV API for each package:

```
POST https://api.osv.dev/v1/query
Content-Type: application/json
Body: {"package": {"name": "<package_name>", "ecosystem": "PyPI"}, "version": "<pinned_version>"}
```

For npm packages use `"ecosystem": "npm"`. For Maven use `"ecosystem": "Maven"`.
Extract: OSV ID (maps to CVE ID if present), severity, affected version ranges, description, fixed version.

#### Source 2 — NVD (National Vulnerability Database) — CVSS Scoring

Keyword-based fallback; returns CVSS scores and detailed version ranges. Use WebFetch:

```
https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=PACKAGE&cvssV3Severity=HIGH&cvssV3Severity=CRITICAL&resultsPerPage=10
```

Priority packages to always query even if not pinned:
- `langchain`, `langchain-community`, `langchain-core`
- `openai`, `anthropic`
- `torch`, `transformers`
- `llama-index`, `llama_index`
- `chromadb`, `qdrant-client`
- `vllm`, `ollama`
- Any additional packages found in Sub-step A

#### Source 3 — GitHub Advisory Database — Early Disclosures

AI/ML advisories often appear here before NVD. Use WebFetch to query by ecosystem:

```
https://api.github.com/advisories?ecosystem=pip&per_page=20
```

Also perform targeted web searches for recent undisclosed CVEs:
```
Search: "langchain CVE 2025" site:github.com/advisories
Search: "openai python SDK vulnerability 2025"
Search: "GenAI LLM security vulnerability CVE 2025"
```

#### Source 4 — AVID (AI Vulnerability and Incidents Database)

Covers AI/ML-specific vulnerabilities (bias, robustness, adversarial attacks) not found in standard CVE databases. Use WebSearch:

```
Search: site:avidml.org <package_name> vulnerability
Search: site:avidml.org langchain security
```

AVID issues use AVID-VULN-xxx IDs rather than CVE IDs. Note the source in the report. Map to the most relevant DSGAI risk using the mapping table in Sub-step C.

#### Source 5 — MITRE ATLAS — AI Adversarial Techniques

ATLAS documents AI-specific attack techniques (not CVEs) that map directly to DSGAI risks. Use WebSearch to check for techniques relevant to the AI stack detected in this repo:

```
Search: site:atlas.mitre.org prompt injection
Search: site:atlas.mitre.org training data poisoning
Search: site:atlas.mitre.org <framework_name>
```

Include relevant ATLAS techniques in Section 2 of the report as a separate "AI Attack Techniques" subsection. Map each technique to its DSGAI risk.

---

For each CVE or advisory found across all sources:
1. Extract: ID, CVSS score (if available), description, affected versions, fixed version, published date, source
2. Check if the repo's pinned version falls within the affected version range
3. Classify:
   - **EXPLOITABLE** — repo version is in the affected range
   - **NOT AFFECTED** — repo version is newer than the fixed version
   - **UNKNOWN** — version unpinned or cannot determine
4. Map to the most relevant DSGAI risk using Sub-step C
5. Deduplicate: if the same CVE appears in multiple sources, keep one entry and list all sources

---

### Sub-step C: CVE → DSGAI Risk Mapping

Use this mapping to assign newly discovered CVEs to the right DSGAI risk section:

| CVE Pattern / Category | DSGAI Risk |
|---|---|
| Prompt injection, input manipulation, jailbreak | DSGAI01, DSGAI18 |
| Credential leak, API key exposure, auth bypass in AI SDK | DSGAI02 |
| Supply chain, package poisoning, pickle deserialization, model weight tampering | DSGAI04 |
| RAG / document ingestion path traversal, retrieval bypass | DSGAI05 |
| MCP server, plugin RCE, tool call injection | DSGAI06 |
| Vector store unauthorized access, unencrypted embeddings | DSGAI13 |
| Telemetry / logging data exposure, PII in traces | DSGAI14 |
| Multi-tenant data leakage, cross-session context bleed | DSGAI11 |
| SQL injection via LLM-generated queries | DSGAI12 |
| Model output manipulation, hallucination-based data exposure | DSGAI18 |
| Inference API DoS, model extraction, rate limit bypass | DSGAI20 |

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
  Source: NVD / OSV / GitHub Advisory / AVID / MITRE ATLAS
```

These live CVEs are **additive** — they extend the embedded CVEs already in each DSGAI section, they do not replace them.

**Enrichment status** (display as banner at top of Section 2):
- ✅ Online — queried NVD + OSV + GitHub Advisories + AVID at `<timestamp>`
- ⚠️ Partial — one or more sources unreachable; results may be incomplete (list which sources failed)
- ❌ Offline — all sources unreachable; showing embedded CVEs only

If any individual source is unreachable (network restriction, rate limit, API error), continue with the remaining sources and note which were unavailable in the banner.

---

## DSGAI Embedded Requirements

### DSGAI01 — Training Data Privacy [BOTH]
**Risk:** PII, PHI, confidential data, or sensitive credentials inadvertently included in training datasets, fine-tuning corpora, embeddings, or model outputs. Data subjects have no visibility or right to erasure.

**Key mitigations to scan for:**
- No-training / data-opt-out headers/flags in API calls (`X-Training-Data: false`, `allow_training=False`, `training_opt_out`)
- PII scrubbing before data ingestion (`anonymize`, `redact`, `scrub_pii`, `presidio`, `piiDetect`, `mask_pii`)
- Differential privacy library usage (`dp-accounting`, `opacus`, `tensorflow-privacy`)
- Output filtering for PII before returning to user (`filter_pii`, `remove_pii`, `output_sanitize`)
- Data minimization patterns (log only IDs, not full content)
- GDPR/CCPA consent check before training pipeline

**Known CVEs:** CVE-2024-5184 (EmailGPT — prompt injection exposing training data)

---

### DSGAI02 — Agentic System Identity and Credential Management [BUILD]
**Risk:** Agent identities lack MFA/RBAC; credentials (API keys, tokens) hardcoded or over-privileged; tool invocations not authenticated; lateral movement possible when one agent credential is compromised.

**Key mitigations to scan for:**
- No hardcoded LLM API keys (`OPENAI_API_KEY\s*=\s*["\']sk-`, `ANTHROPIC_API_KEY\s*=\s*["\']sk-ant-`)
- No hardcoded cloud credentials used by agents (`AWS_ACCESS_KEY_ID\s*=\s*["\'][A-Z0-9]{20}`)
- Token scope patterns: minimal-scope tokens, not wildcard (`"*"`, `scope.*all`, `permissions.*write`)
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
- Detection: hardcoded third-party LLM hostnames not in approved list (`api.openai.com`, `api.anthropic.com`, `generativelanguage.googleapis.com` — flag for review)
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
- **AI frameworks in use:** LangChain, LlamaIndex, Semantic Kernel, Spring AI, LangChain4j, Vercel AI SDK, AutoGen, CrewAI
- **Vector stores in use:** Chroma, Pinecone, Weaviate, Qdrant, FAISS, pgvector, Milvus, Redis Vector
- **LLM providers in use:** OpenAI, Anthropic, Bedrock, Vertex AI, Azure OpenAI, HuggingFace, Ollama
- **MCP / plugins:** MCP server config files, plugin manifests
- **Container:** `Dockerfile`, `docker-compose.yml`
- **Kubernetes/Helm:** `helm/`, `k8s/`, `*.yaml` deployment manifests
- **CI/CD:** `.github/workflows/`, `.circleci/`, `Jenkinsfile`
- **Data pipelines:** `dags/`, `airflow`, `prefect`, data ingestion scripts
- **AppSec / security architecture review artifacts:** `appsec/`, `.appsec/`, `security-review/`

---

## Step 2: Scan for DSGAI Issues

**Parallel execution:** Run all 21 DSGAI grep scans simultaneously — send all scan commands as parallel tool calls in a single message batch. Do not wait for one control's scan to finish before starting the next. Split the 21 controls into three batches of 7 if your tool runner has a per-message limit, otherwise fire all at once. This reduces scan time from 20+ sequential minutes to approximately 2–5 minutes.

**Batch A (run in parallel):** DSGAI01, DSGAI02, DSGAI03, DSGAI04, DSGAI05, DSGAI06, DSGAI07
**Batch B (run in parallel):** DSGAI08, DSGAI09, DSGAI10, DSGAI11, DSGAI12, DSGAI13, DSGAI14
**Batch C (run in parallel):** DSGAI15, DSGAI16, DSGAI17, DSGAI18, DSGAI19, DSGAI20, DSGAI21

For each DSGAI risk, scan the relevant files. Use the patterns below.

---

### Evidence Classification — Structural vs Value-Bearing

Every scan below is classified as either **[STRUCTURAL]** or **[VALUE-BEARING ⚠️]**. This classification controls how the matched grep output is handled when you write the evidence block in Step 4.

**[STRUCTURAL]** — The grep match shows a code pattern: a function call, a missing import, a missing decorator, or an architectural gap. The matched line does not contain a runtime secret or personal data. It is safe to reproduce the full matched line in the evidence block.

**[VALUE-BEARING ⚠️]** — The grep pattern specifically targets lines where the matched content IS a credential, API key, secret, connection string, or data that could contain PII in a real codebase. The actual value found — regardless of whether it looks like a demo or test value — must **never** appear in the report evidence block.

For VALUE-BEARING scans, the evidence block must use this format instead:
```
<file>:<line> — <pattern description> detected (value redacted — review file directly)
```

**Classification table:**

| DSGAI Control | Classification | Why |
|---|---|---|
| DSGAI01 | STRUCTURAL | Looks for presence/absence of scrubbing library imports and opt-out flags — no values |
| DSGAI02 | VALUE-BEARING ⚠️ | Matches lines containing actual API key values, database passwords, JWT secrets, and connection strings |
| DSGAI03 | STRUCTURAL | Matches public API endpoint hostnames in config — not secrets |
| DSGAI04 | STRUCTURAL | Matches `torch.load()` call patterns and dependency file structure — no secret values |
| DSGAI05 | STRUCTURAL | Matches function calls missing a filter argument — no sensitive values |
| DSGAI06 | STRUCTURAL | Matches missing auth middleware and HTTP/HTTPS configuration flags |
| DSGAI07 | STRUCTURAL | Matches missing TTL parameters and absent delete function names |
| DSGAI08 | STRUCTURAL | Looks for DPIA/consent keyword presence — document names, not values |
| DSGAI09 | STRUCTURAL | Matches EXIF stripping and file type validation patterns |
| DSGAI10 | STRUCTURAL | Matches synthetic data library imports |
| DSGAI11 | STRUCTURAL | Matches missing tenant filter arguments in function calls |
| DSGAI12 | STRUCTURAL | Matches direct SQL execution call patterns — LLM-generated SQL is not in source |
| DSGAI13 | VALUE-BEARING ⚠️ | May match lines where vector store auth tokens are hardcoded as literal values |
| DSGAI14 | VALUE-BEARING ⚠️ | Matches log statements whose format strings may contain PII field references or — in real codebases — inline test PII values |
| DSGAI15 | VALUE-BEARING ⚠️ | Matches system prompt construction that may embed credential strings or sensitive config values |
| DSGAI16 | STRUCTURAL | Matches IDE plugin manifest patterns — no secret values |
| DSGAI17 | STRUCTURAL | Matches absent retry/circuit-breaker patterns — no values |
| DSGAI18 | STRUCTURAL | Matches absent guardrail import/decorator patterns |
| DSGAI19 | STRUCTURAL | Matches data labeling pipeline imports |
| DSGAI20 | STRUCTURAL | Matches absent rate-limiting decorator patterns |
| DSGAI21 | STRUCTURAL | Matches knowledge store connection patterns — URLs, not secrets |

---

### DSGAI01 Scan — Training Data Privacy [STRUCTURAL]

```
# PII scrubbing before ingestion
grep -rn "anonymize\|redact\|scrub_pii\|piiDetect\|mask_pii\|presidio" --include="*.py" --include="*.ts" --include="*.java"

# No-train API option set
grep -rn "allow_training\|training_opt_out\|X-Training-Data\|no_train" --include="*.py" --include="*.ts" --include="*.json" --include="*.yaml"

# Output PII filtering
grep -rn "filter_pii\|remove_pii\|output_sanitize\|output_filter" --include="*.py" --include="*.ts" --include="*.java"

# Differential privacy library
grep -rn "opacus\|tensorflow.privacy\|dp-accounting\|differential.privacy" --include="*.py" --include="*.txt"

# GDPR/CCPA consent before training pipeline
grep -rn "consent\|gdpr\|ccpa\|data_subject" --include="*.py" --include="*.java" --include="*.ts"
```

### DSGAI02 Scan — Agentic Credential Management [VALUE-BEARING ⚠️]

```
# Hardcoded LLM API keys — FAIL
grep -rn "OPENAI_API_KEY\s*=\s*[\"']sk-\|ANTHROPIC_API_KEY\s*=\s*[\"']sk-ant-\|api_key\s*=\s*[\"'][a-zA-Z0-9_\-]{20,}" --include="*.py" --include="*.ts" --include="*.java" --include="*.env"

# Hardcoded AWS credentials used by agents — FAIL
grep -rn "AWS_ACCESS_KEY_ID\s*=\s*[\"'][A-Z0-9]\|aws_access_key_id\s*=\s*[\"'][A-Z0-9]" --include="*.py" --include="*.ts" --include="*.yaml"

# Over-privileged token scope patterns
grep -rn "\"scope\":\s*\"[^\"]*\*\|permissions.*write.*all\|scope.*:.*admin" --include="*.py" --include="*.json" --include="*.yaml"

# Vault / secrets manager retrieval for agent creds (PASS signal)
grep -rn "vault\|secretsmanager\|GetSecretValue\|VAULT_TOKEN" --include="*.py" --include="*.java" --include="*.ts"

# Tool call authentication
grep -rn "hmac\|sign_request\|verify_signature\|tool_auth" --include="*.py" --include="*.ts" --include="*.java"
```

### DSGAI03 Scan — Shadow AI Detection

```
# Third-party LLM endpoints hardcoded (flag for review)
grep -rn "api.openai.com\|api.anthropic.com\|generativelanguage.googleapis.com\|api.cohere.com\|api.together.xyz" --include="*.py" --include="*.ts" --include="*.java" --include="*.go" --include="*.yaml" --include="*.json"

# Internal LLM proxy/gateway pattern (PASS signal)
grep -rn "llm.gateway\|ai-proxy\|model-gateway\|llm-proxy\|api.internal" --include="*.py" --include="*.ts" --include="*.yaml"

# DLP / data classification before LLM call
grep -rn "dlp\|data_classification\|classify_data\|sensitivity_check" --include="*.py" --include="*.ts" --include="*.java"
```

### DSGAI04 Scan — AI Supply Chain Security

```
# Insecure pickle deserialization — FAIL
grep -rn "torch\.load(" --include="*.py"
# Check if weights_only=True is present — PASS
grep -rn "torch\.load(.*weights_only\s*=\s*True" --include="*.py"

# Model artifact verification
grep -rn "sha256\|verify_signature\|model_hash\|check_integrity\|hashlib" --include="*.py" --include="*.sh"

# Unpinned ML dependencies — WARN
grep -n ">=" requirements*.txt setup.py pyproject.toml 2>/dev/null | grep -i "torch\|transformers\|tensorflow\|langchain\|openai\|anthropic"

# SBOM generation in CI/CD
grep -rn "syft\|cyclonedx\|spdx\|sbom" --include="*.yml" --include="*.yaml" .github/ Makefile

# Trusted registry enforcement
grep -rn "index-url\|extra-index-url\|artifactory\|jfrog" pip.conf requirements*.txt .github/workflows/
```

### DSGAI05 Scan — RAG Data Security

```
# Path traversal risk in document ingestion
grep -rn "open(\|load_file\|ingest_document\|add_documents" --include="*.py" --include="*.ts"
# Check for path validation nearby

# Access control on retrieved docs (PASS signal)
grep -rn "acl_filter\|access_check\|permitted_docs\|filter.*tenant\|namespace.*tenant" --include="*.py" --include="*.ts" --include="*.java"

# Tenant namespace isolation in vector store
grep -rn "namespace\s*=.*tenant\|collection.*=.*tenant\|filter.*tenant_id\|where.*tenant" --include="*.py" --include="*.ts" --include="*.java"

# Document integrity check before ingestion
grep -rn "hashlib\|sha256.*doc\|integrity.*check\|verify.*document" --include="*.py" --include="*.ts"

# Context size limits
grep -rn "max_chunk_size\|chunk_size\|max_doc_size\|content_limit" --include="*.py" --include="*.ts" --include="*.yaml"
```

### DSGAI06 Scan — MCP / Plugin Security

```
# MCP server config — check transport
grep -rn "\"url\":\s*\"http://\|transport.*http://" --include="*.json" --include="*.yaml" --include="*.toml"

# MCP authentication configured
grep -rn "mcp.*api_key\|mcp.*auth\|mcp.*bearer\|x-api-key.*mcp" --include="*.json" --include="*.yaml" --include="*.py" --include="*.ts"

# Tool argument schema validation
grep -rn "jsonschema\|pydantic.*validate\|zod\|schema.*tool\|input_schema" --include="*.py" --include="*.ts" --include="*.java"

# Wildcard tool permissions — WARN
grep -rn "tools.*\*\|permissions.*all\|allow_all_tools" --include="*.json" --include="*.yaml" --include="*.py"
```

### DSGAI07 Scan — Data Lifecycle / TTL

```
# TTL configuration
grep -rn "ttl\s*=\|expires_in\s*=\|max_age\s*=\|RETENTION_DAYS\|DATA_TTL\|HISTORY_TTL" --include="*.py" --include="*.ts" --include="*.java" --include="*.yaml" --include="*.json"

# Session/history cleanup
grep -rn "delete_session\|clear_history\|purge_conversation\|clear_memory\|delete_conversation" --include="*.py" --include="*.ts" --include="*.java"

# Vector namespace/collection delete capability
grep -rn "delete_namespace\|delete_collection\|drop_index\|delete_index\|reset_collection" --include="*.py" --include="*.ts"

# Right-to-erasure handler
grep -rn "gdpr_delete\|erase_user_data\|handle_deletion\|right_to_erasure\|forget_user" --include="*.py" --include="*.ts" --include="*.java"
```

### DSGAI11 Scan — Multi-Tenant Data Isolation

```
# Tenant ID in vector queries
grep -rn "similarity_search\|query\|search" --include="*.py" --include="*.ts" --include="*.java"
# Flag any vector query call that does NOT have a tenant filter nearby

# Namespace per tenant
grep -rn "namespace\s*=\s*.*tenant\|collection.*tenant\|index.*tenant" --include="*.py" --include="*.ts"

# Session tenant validation
grep -rn "tenant_id.*session\|verify_tenant\|assert_tenant\|check_tenant" --include="*.py" --include="*.ts" --include="*.java"
```

### DSGAI12 Scan — Database Agent Security

```
# Raw SQL execution from LLM output — FAIL
grep -rn "execute(.*llm\|execute(.*response\|execute(.*completion\|run_query.*output\|db.run(" --include="*.py" --include="*.ts" --include="*.java"

# Parameterized queries (PASS signal)
grep -rn "cursor\.execute.*%s\|cursor\.execute.*\?\|prepareStatement\|bindValue\|:param" --include="*.py" --include="*.java"

# Read-only DB connection for agents
grep -rn "read_only.*True\|readonly.*True\|SELECT.*only\|read_only_connection" --include="*.py" --include="*.ts" --include="*.java"

# Query validator
grep -rn "validate_query\|query_validator\|safe_sql\|sql_guard\|sanitize_sql" --include="*.py" --include="*.ts"

# DDL from agent — FAIL signals
grep -rn "DROP TABLE\|TRUNCATE\|ALTER TABLE\|DELETE FROM" --include="*.py" --include="*.ts" --include="*.java"

# Row limit
grep -rn "LIMIT\s*[0-9]\|max_rows\s*=\|fetch_limit\s*=" --include="*.py" --include="*.ts"
```

### DSGAI13 Scan — Vector Store Security [VALUE-BEARING ⚠️]

```
# Vector store auth configured
grep -rn "CHROMA_SERVER_AUTH\|QDRANT_API_KEY\|PINECONE_API_KEY\|weaviate.*auth\|MILVUS_TOKEN\|vectorstore.*api_key" --include="*.py" --include="*.ts" --include="*.java" --include="*.yaml" --include="*.env.example"

# TLS / encrypted connections
grep -rn "\"https://.*qdrant\|\"https://.*weaviate\|\"https://.*pinecone\|ssl.*True\|tls.*True\|grpcs://" --include="*.py" --include="*.ts" --include="*.yaml"

# Insecure defaults — WARN
grep -rn "host.*0\.0\.0\.0\|ALLOW_RESET.*True\|chroma.*http://localhost\|qdrant.*http://localhost" --include="*.py" --include="*.ts" --include="*.yaml"
```

### DSGAI14 Scan — AI Telemetry Security [VALUE-BEARING ⚠️]

```
# Verbose prompt logging disabled (PASS signal)
grep -rn "log_prompts\s*=\s*False\|capture_content\s*=\s*False\|OTEL_LOG_PROMPTS.*false\|log_completions.*False" --include="*.py" --include="*.ts" --include="*.yaml" --include="*.env"

# Full response logging enabled — WARN
grep -rn "log_prompts\s*=\s*True\|capture_content\s*=\s*True\|log_full_response\s*=\s*True" --include="*.py" --include="*.ts"

# PII redaction in logging
grep -rn "redact_pii\|mask_sensitive\|sanitize_log\|scrub.*log\|log.*redact" --include="*.py" --include="*.ts" --include="*.java"

# Raw print/log of full LLM response in prod code — WARN
grep -rn "print(response\|print(completion\|console\.log(response\|console\.log(completion\|logger\.debug(.*response\|logger\.info(.*completion" --include="*.py" --include="*.ts" --include="*.java"
```

### DSGAI15 Scan — Context Window Security [VALUE-BEARING ⚠️]

```
# Hardcoded secrets in system prompt — FAIL
grep -rn "system_prompt\s*=\s*[\"'].*key\|system_prompt\s*=\s*[\"'].*password\|system_prompt\s*=\s*[\"'].*secret\|system_message.*api_key" --include="*.py" --include="*.ts" --include="*.java"

# Context size limits
grep -rn "max_context_length\s*=\|context_window_limit\s*=\|max_context_tokens\s*=\|truncate_context" --include="*.py" --include="*.ts" --include="*.java"

# System prompt from config/vault (PASS signal)
grep -rn "system_prompt.*config\|system_prompt.*vault\|system_prompt.*os.environ\|system_prompt.*getenv" --include="*.py" --include="*.ts"

# Customer-360 aggregation patterns — WARN (flag for data minimization review)
grep -rn "customer_360\|user_profile_all\|fetch_all_user_data\|get_full_profile" --include="*.py" --include="*.ts" --include="*.java"
```

### DSGAI18 Scan — Model Output Security

```
# Output guardrails
grep -rn "guardrails\|nemo.guardrails\|llm_guard\|output_guard\|filter_output\|sanitize_response\|moderation" --include="*.py" --include="*.ts" --include="*.java"

# PII detection on output
grep -rn "detect_pii.*output\|output.*detect_pii\|presidio.*output\|scan_output" --include="*.py" --include="*.ts"

# Logprobs exposed in API response — WARN
grep -rn "logprobs\s*=\s*True\|return_logprobs\|include_logprobs" --include="*.py" --include="*.ts" --include="*.java"

# max_tokens always set
grep -rn "ChatCompletion\|openai\.chat\|anthropic\.messages\|generate\|complete" --include="*.py" --include="*.ts" --include="*.java"
# Verify max_tokens= is nearby in each call
```

### DSGAI20 Scan — Inference API Security

```
# API authentication on inference endpoint
grep -rn "api_key.*verify\|bearer_token.*validate\|Authorization.*require\|authenticate.*request\|@require_auth\|auth_middleware" --include="*.py" --include="*.ts" --include="*.java"

# Rate limiting on AI endpoint
grep -rn "rate_limit\|RateLimiter\|throttle\|slowapi\|flask_limiter\|express-rate-limit" --include="*.py" --include="*.ts" --include="*.java"

# Input length validation
grep -rn "max_input_length\s*=\|max_input_tokens\s*=\|input.*truncat\|validate.*length" --include="*.py" --include="*.ts"

# Prompt injection detection
grep -rn "prompt_injection\|detect_injection\|llm_guard\|rebuff\|input_guard" --include="*.py" --include="*.ts"
```

### DSGAI21 Scan — Knowledge Store Security

```
# Read-only for RAG retrieval
grep -rn "read_only.*True\|readonly.*True\|HttpMethod\.GET\|http_method.*get" --include="*.py" --include="*.ts" --include="*.java"

# Write operations in agent code paths — WARN
grep -rn "\.upsert(\|\.insert(\|\.update(\|\.delete(\|\.add_documents(\|\.write(" --include="*.py" --include="*.ts" --include="*.java"

# Content validation before knowledge store write
grep -rn "validate_content\|sanitize.*write\|verify.*knowledge\|content.*check.*write" --include="*.py" --include="*.ts"

# Version control on knowledge entries
grep -rn "versioned.*True\|audit_writes\|version_id\|created_at.*knowledge\|knowledge.*audit" --include="*.py" --include="*.ts"
```

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
- AppSec / security architecture review completed

**NOT APPLICABLE** — Control is not relevant to this repository:
- DSGAI09 (Multimodal) if repo processes only text
- DSGAI10 (Synthetic Data) if repo does not generate synthetic training data
- DSGAI19 (Data Labeling) if repo has no labeling pipeline
- DSGAI16 (IDE Plugins) if repo is a backend service with no developer tooling component
- DSGAI03 (Shadow AI) if all LLM calls already route through approved internal gateway

Also flag:
- **DSGAI Registry Gap** — static secrets (API keys, tokens) used by AI components that have no corresponding entry in a secrets registry
- **DSGAI Scope Mismatch** — BUY-tagged controls applied to a BUILD repo (skip gracefully with note)

---

## Step 4: Generate HTML Report

### Evidence Redaction Rule

Before writing any evidence block in the report, check the scan classification from the Step 2 table:

**For VALUE-BEARING scans (DSGAI02, DSGAI13, DSGAI14, DSGAI15):**
Never reproduce the matched grep line. Output only the file path, line number, and a description of what was found:

```
app/config.py:12 — hardcoded database credential pattern detected (value redacted — review file directly)
app/config.py:18 — hardcoded secret key pattern detected (value redacted — review file directly)
app/telemetry/logging.py:28 — prompt logging statement detected (content redacted — review file directly)
```

This rule applies regardless of whether the matched value looks like a demo credential, a test value, or a placeholder. The report may be shared with stakeholders, auditors, or stored in a repository where the actual credential value must not appear.

**For all STRUCTURAL scans (DSGAI01, DSGAI03–DSGAI12, DSGAI16–DSGAI21):**
Reproduce the matched grep output as-is. These patterns match code structure (missing decorators, absent imports, function call patterns) that contains no sensitive runtime data.

---

Generate a self-contained HTML report saved as `DSGAI-report.html` in the repository root.

**IMPORTANT — write in 3 sequential parts to avoid context window exhaustion. Do NOT print or narrate any HTML in the response text at any point.**

1. **Write Part 1** using the Write tool: `<!DOCTYPE html>` through the end of the Dashboard + Compliance Bar section. End the file with the exact comment `<!-- FINDINGS_PLACEHOLDER -->`.
2. **Edit Part 2**: Use the Edit tool to replace `<!-- FINDINGS_PLACEHOLDER -->` with the AI Component Inventory, Scope Legend, Summary Table, all 21 finding cards, Recommendations, and Checklist sections. End the replacement with the exact comment `<!-- CVE_PLACEHOLDER -->`.
3. **Edit Part 3**: Use the Edit tool to replace `<!-- CVE_PLACEHOLDER -->` with the full CVE Advisory section, footer, `</body>`, and `</html>`.

This three-part approach keeps each tool call well within the context limit regardless of repo size.

Open after saving:

```
open DSGAI-report.html   # macOS
xdg-open DSGAI-report.html  # Linux
```

### Report Structure

The report is organized into **two main sections** with shared header/footer scaffolding:
- **Section 1 — DSGAI Compliance** (the 21 data security risk findings)
- **Section 2 — CVE Advisory** (live vulnerability intelligence per package)

**PDF-first design:** The report must render correctly when printed to PDF via Ctrl+P/Cmd+P. This means:

- No sticky/fixed positioning (nav bar is static, not `position: sticky`)
- All finding cards always visible (`display: block`) — never collapsed/hidden
- No interactive filter buttons that hide content
- `page-break-inside: avoid` on every card, table, and section block
- `-webkit-print-color-adjust: exact; print-color-adjust: exact` on body so colours survive print

---

#### Shared scaffolding (top)

1. **Header** — Report title "OWASP DSGAI Data Security Compliance Report", service/repo name, date, framework version (OWASP GenAI Data Security Risks and Mitigations v1.0, March 2026)
2. **Section nav bar** (static, not sticky) — Two labels: `Section 1: DSGAI Compliance` | `Section 2: CVE Advisory` as anchor links
3. **About This Report** — A dedicated section placed immediately after the nav bar, before the executive summary. Contains **four subsections** — each MUST be rendered as a distinct `<h3>` block with its full content. Do NOT compress or merge them into paragraphs:

   **Goal** — This report scans a software codebase against the **OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0)** — a framework published by the Open Worldwide Application Security Project in March 2026 that defines 21 data security risks specific to GenAI and agentic systems. The goal is to **automatically detect OWASP GenAI data security risks and make it easier for teams** to act on them — without requiring every developer or reviewer to manually read and interpret the full OWASP specification. Beyond detection, the automation provides several additional benefits:
   - **Shift-left security** — catches risks at development time, not at pen test or production incident time
   - **Consistent coverage** — eliminates human variance in manual reviews; every scan checks all 21 controls every time
   - **Live CVE intelligence** — automatically cross-references the repo's exact dependency versions against live vulnerability databases, surfacing exploitable CVEs without manual lookups
   - **Audit-ready output** — generates a shareable, self-contained HTML report that serves as documented evidence of a security review against a published standard
   - **CI/CD integration ready** — the scan can be run on every pull request or release branch, making GenAI security a continuous practice rather than a one-time checkpoint
   - **Prioritised remediation backlog** — findings are tiered so teams know what to fix today versus what goes into the architecture backlog

   This report is designed to benefit **security practitioners**, **developers**, **security architects**, and **engineering managers** — see the *Who Benefits* section below for details on how each audience can use it.

   **How It Works** — The scan runs in four phases: (1) Repository detection — confirms GenAI/agentic patterns are present; (2) Live CVE enrichment — queries OSV, NVD, and GitHub Advisory Database for the exact package versions in use; (3) Code pattern scan — searches source files for OWASP 21 DSGAI risk indicators across credentials, SQL execution, vector store auth, telemetry logging, MCP transport, RAG access controls, and more; (4) Findings classification — each control is rated FAIL / WARN / PASS / NOT VALIDATED / NOT APPLICABLE with file paths, line numbers, and remediation steps.

   **Privacy & Data Handling** — This scan runs entirely on your local machine. Your source code, configuration files, and secrets are never uploaded, transmitted, or shared with any external service. The only outbound requests made during a scan are package name and version lookups (e.g. `langchain==0.1.0`) sent to public CVE databases — [OSV](https://osv.dev), [NVD](https://nvd.nist.gov), and [GitHub Advisory Database](https://github.com/advisories) — to check for known vulnerabilities in your dependencies. No actual code leaves your machine. Live CVE lookups are optional: if your environment has no internet access, the scan falls back to its embedded CVE database and still produces a complete report.

   **Who Benefits** — Render as a table:
   | Audience | How this report helps |
   | --- | --- |
   | **Security practitioners** | Audit-ready evidence of GenAI data security posture mapped to a published OWASP standard. Identifies FAIL items that need immediate remediation before security review. |
   | **Developers** | Pinpoints exactly which files and lines introduce risk, with concrete fix instructions. No need to read the full OWASP document — the relevant control and remediation is surfaced inline. |
   | **Security architects** | Risk posture snapshot across the full GenAI data lifecycle — from training data ingestion through inference API exposure — enabling prioritised architecture decisions. |
   | **Engineering managers** | Dashboard and compliance bar give an at-a-glance view of team posture; tiered recommendation cards translate findings into a prioritised backlog. |

4. **Executive Summary** — One opening sentence on overall posture, then **bullet points** (not a paragraph) covering: key FAIL findings, AI components identified, CVE posture. Followed by a **standalone highlighted callout box** for the recommended remediation priority order — do not bury this inside a paragraph.
4. **Dashboard Cards row** — single row of cards spanning both sections:
   - DSGAI checks: Total (21) | PASS | WARN | FAIL | NOT VALIDATED | NOT APPLICABLE
   - CVE cards: Exploitable CVEs | Patched CVEs | Unknown CVEs
5. **Compliance Bar** — Visual bar showing PASS / WARN / FAIL / NV distribution across the 21 controls

---

#### Section 1 — DSGAI Compliance

6. **AI Component Inventory** — Detected frameworks, vector stores, LLM providers, MCP servers, data pipelines; each shown as a chip/tag

7. **Scope Tag Legend** — Compact box placed immediately below AI Component Inventory, before the summary table and findings. Three items:
   - **BUILD** — your team implements this control in the codebase
   - **BUY** — the LLM provider / SaaS vendor is responsible
   - **BOTH** — shared responsibility between your code and the provider

8. **Summary Table** — Appears **before** detailed findings. Columns: Risk ID | Risk Name | Scope | Tier | Status | Key Evidence. Gives the reader the full picture at a glance before drilling into details.

9. **Detailed Findings** — One card per DSGAI risk (DSGAI01–DSGAI21), always fully visible (no collapse/expand JS):
   - Status badge: PASS / WARN / FAIL / NOT VALIDATED / NOT APPLICABLE
   - Risk ID + title + Scope tag (BUILD / BUY / BOTH) + Tier badges (Tier 1 / Tier 2 / Tier 3)
   - Body: evidence (file paths + line numbers), risk explanation, specific remediation steps
   - Inline CVE pills for any CVEs mapped to this risk

10. **Recommendations** — Prioritized action cards:
    - **Fix today — Tier 1 (red):** FAIL items + EXPLOITABLE CVEs affecting this repo
    - **Architecture backlog — Tier 2 (yellow):** WARN items + Tier 2 architecture changes
    - **Mature program — Tier 3 (blue):** NOT VALIDATED items needing red-team, DP, or process maturity

11. **DSGAI Compliance Artifacts Checklist**:
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
    Mark items ✅ if evidence found, ⚠️ if partially evidenced, ❌ if missing.

---

#### Section 2 — CVE Advisory

11. **CVE enrichment status banner** — One of:
    - ✅ Online — queried NVD + OSV + GitHub Advisories at `<timestamp>`
    - ⚠️ Partial — some sources unreachable; results may be incomplete
    - ❌ Offline — network unavailable; showing embedded CVEs only

12. **Package Inventory Table** — All AI/ML packages detected in the repo:
    | Package | Ecosystem | Version in repo | Pinned? |
    Shows which packages were queried for CVEs.

13. **CVE summary counts bar** — Compact stat row: `X CVEs found · Y Exploitable · Z Not Affected · W Unknown`
    - Exploitable count shown in red, Not Affected in green, Unknown in gray

14. **CVE Groups — organised by DSGAI Risk** (all always visible — no collapse JS, PDF safe):

    One group per DSGAI risk that has at least one CVE. Each group has:
    - **Group header**: left-border accent bar + DSGAI risk ID + risk name + count badge (e.g. `DSGAI13 — Vector Store Security  [1 CVE · NOT AFFECTED]`)
      - Header accent color matches worst status in group: red if any EXPLOITABLE, yellow if any UNKNOWN, green if all NOT AFFECTED
    - **CVE card(s)** inside the group, one per CVE:
      - CVE ID in monospace + CVSS score badge + status pill (🔴 EXPLOITABLE / ✅ NOT AFFECTED / ⚠️ UNKNOWN)
      - Package name + repo version
      - One-line description
      - Three version lines: `Affects: <X.Y.Z` · `Fixed: X.Y.Z` · `Repo: A.B.C`
      - Published date + Source (NVD / OSV / GitHub / Embedded)
    - If a CVE maps to **multiple DSGAI risks** (e.g. DSGAI01 · DSGAI18), show it under a combined group header listing both IDs

    **Why grouped by DSGAI risk:** A reader can directly cross-reference Section 1 findings with Section 2 CVEs. A FAIL on DSGAI12 in Section 1 immediately connects to an EXPLOITABLE CVE under DSGAI12 in Section 2 — making remediation priority unambiguous.

15. **DSGAI Risk Reference grid** — Compact grid showing all 21 risks: ID | one-line description | Scope | Tier | key embedded CVE

---

#### Shared scaffolding (bottom)

16. **Footer** — Generation date, framework version (OWASP DSGAI v1.0), CVE sources queried, print-to-PDF instructions (`Ctrl+P → Save as PDF → expands all cards automatically`). Must include attribution on a separate line: "Original work by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org/initiative/data-security/), led by [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/) | Skill adaptation by [Harish Ramachandran](https://www.linkedin.com/in/harish-ramachandran-a8026443/)". Both names MUST be hyperlinks — do not render either as plain text.

#### PDF Export

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

# Windows (PowerShell)
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless=new --print-to-pdf=DSGAI-report.pdf `
  --print-to-pdf-no-header "file:///$(pwd)/DSGAI-report.html"
```

### Styling

- CSS variables, no external dependencies
- Color scheme: GREEN `#16a34a` (pass), YELLOW `#ca8a04` (warn), RED `#dc2626` (fail), BLUE `#2563eb` (not validated), GRAY `#6b7280` (not applicable), PURPLE `#7c3aed` (info)
- Dark gradient header: `#1e1b4b` → `#312e81` → `#1e3a5f`
- White card sections with subtle shadows, rounded borders (`border-radius: 12px`)
- Monospace font for file paths, pattern strings, CVE IDs
- Interactive: collapsible finding cards (click to expand), filter buttons, sortable table
- Tier badges: Tier 1 = red pill, Tier 2 = yellow pill, Tier 3 = blue pill
- CVE badges: red background, monospace text
- Print-friendly: `@media print` rules, expand all findings on print
- Self-contained: all CSS and JS inline, no CDN, no external fonts

---

## Notes for the Analyst

- **BUY vs BUILD scope:** For repos that only *consume* an LLM API (BUY), skip BUILD-only controls gracefully. Note the scope mismatch with NOT APPLICABLE and explain why.
- **NOT VALIDATED vs FAIL:** If a control is critical (DSGAI02 agent credentials, DSGAI11 tenant isolation) and no evidence is found either way, prefer FAIL over NOT VALIDATED — absence of a security control is a finding.
- **Torch / pickle:** `torch.load()` without `weights_only=True` is a definitive FAIL (Python < 2.0 default is insecure). In PyTorch 2.0+ the default changed — check the version if ambiguous.
- **Vector store defaults:** Chroma default config (`chromadb.Client()` with no auth) is unauthenticated and accepts connections on localhost — WARN in dev, FAIL in any deployment that exposes the port.
- **Multi-tenant check:** For DSGAI11, look at *every* vector store query call in the codebase. If even one similarity_search() is missing a tenant filter, that is a FAIL.
- **LangChain SQL agents:** LangChain's `SQLDatabaseChain` and `create_sql_agent` execute LLM-generated SQL. This is a FAIL for DSGAI12 unless a query validator wraps every execution.
- **Integration test credentials:** Often injected via a secrets manager or CI/CD env vars — flag for registry entry and rotation verification.
- **AppSec artifacts:** Check `appsec/`, `security-review/`, or equivalent folder for security architecture review evidence. If absent and this is a production GenAI service, flag DSGAI08 as WARN.
- **MCP transport:** Any MCP server config pointing to `http://` (non-TLS) in a non-localhost context is a FAIL for DSGAI06.
- **Telemetry:** LangSmith, Langfuse, Arize, Weights & Biases — if present and `capture_content=True` without PII redaction, that is a WARN/FAIL depending on whether production data flows through.

---

## License

This skill is based on materials licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

**Original work:** OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026) by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org/initiative/data-security/), led by [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/).

**This adaptation:** Created by [Harish Ramachandran](https://www.linkedin.com/in/harish-ramachandran-a8026443/). You are free to share and adapt this skill for any purpose, including commercial use, under the same CC BY-SA 4.0 terms.
