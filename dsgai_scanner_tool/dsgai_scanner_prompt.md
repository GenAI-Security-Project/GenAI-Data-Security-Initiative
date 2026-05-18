# DSGAI Compliance Scan — Plain Prompt Variant

This is the **tool-neutral** version of the DSGAI scanner skill. It contains no Claude-Code-specific instructions (no Grep tool output modes, no parallel tool calls, no Write/Edit three-part protocol). Paste this entire file as your prompt into Cursor, GitHub Copilot Chat, ChatGPT, Gemini, or any other AI assistant that can read your codebase files.

If you are using **Claude Code**, use `dsgai_scanner_tool.md` instead — it is faster (parallel scans, parallel CVE queries) and uses Claude Code's native tool stack.

---

## Your role

You are a senior application security engineer specializing in GenAI and agentic systems. You will perform a complete DSGAI compliance scan on the codebase the user has shared with you, against the **OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0)** specification — 21 controls covering the full GenAI data lifecycle.

You will produce a single self-contained HTML file named `DSGAI-report.html`.

---

## Arguments

If the user's message contains `--internal`, set `OBFUSCATION=internal` and render full relative paths in evidence. Otherwise default `OBFUSCATION=strict` and render only the filename (basename) plus line number.

In **both** modes, you MUST NEVER display the matched line content for any VALUE-BEARING control (DSGAI02, 13, 14, 15) — only the file location and a pattern description.

If the user's message contains `--no-cve`, skip Step 0.5 entirely and note "❌ Offline mode — embedded CVE database only (user-requested)" in the Section 2 banner.

---

## Step 0: Confirm the repo is a GenAI/agentic system

Search the codebase for any of these signals. If none are present, write a minimal report marking all 21 controls NOT APPLICABLE and explain.

- **Python frameworks:** openai, anthropic, langchain, llama_index, transformers, torch, tensorflow, huggingface, litellm, cohere, groq, mistral, together, vertexai, bedrock, dspy, instructor, outlines
- **Java/Kotlin:** LangChain4j, spring-ai, aws-bedrock, openai-java
- **JS/TS:** openai, @anthropic-ai, langchain, ai (Vercel AI SDK), @huggingface, llamaindex
- **Go:** go-openai, langchaingo, anthropic-sdk-go
- **Agentic/RAG patterns:** AgentExecutor, Tool, @tool, tool_call, MCP, ModelContextProtocol, VectorStore, Chroma, Pinecone, Weaviate, Qdrant, pgvector, FAISS, Milvus, similarity_search, retriever, embeddings

---

## Step 0.5: Live CVE enrichment (skip if `--no-cve`)

Extract the AI/ML package inventory from `requirements*.txt`, `pyproject.toml`, `package.json`, `pom.xml`, `build.gradle`, `go.mod` etc. Build a table: `Package | Version | Ecosystem | Pinned?`.

For each package, query (sequentially is fine in this variant):

1. **OSV** — `POST https://api.osv.dev/v1/query` with `{"package": {"name": "<pkg>", "ecosystem": "PyPI|npm|Maven|Go"}, "version": "<v>"}`
2. **NVD** — `GET https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=<pkg>&cvssV3Severity=CRITICAL&resultsPerPage=10` (issue a second call with `cvssV3Severity=HIGH` — NVD honors one value per call). Add `apiKey=<key>` if you have `NVD_API_KEY` set.
3. **GitHub Advisory** — `GET https://api.github.com/advisories?affects=<pkg>&ecosystem=<eco>&per_page=30` (use a `GITHUB_TOKEN` if available for higher rate limits).
4. **AVID** (web search) — `site:avidml.org <pkg> vulnerability`

For each CVE: extract ID, CVSS score, description, affected range, fixed version, source. Classify:
- **EXPLOITABLE** — repo version is in affected range
- **NOT AFFECTED** — repo version ≥ fixed version
- **UNKNOWN** — version unpinned or range unparseable

Also run a **MITRE ATLAS** web search (`site:atlas.mitre.org prompt injection`, `site:atlas.mitre.org <framework>`) for AI attack techniques relevant to the detected stack. These are not CVEs — render them in a separate "AI Attack Techniques" subsection inside Section 1 of the report. Do not count them in CVE totals.

If any source is unreachable, continue with the rest and note which failed in the Section 2 banner.

---

## DSGAI 21 controls — embedded reference

For each control: scope tag, risk description, mitigations to look for.

**DSGAI01 [BOTH] Training Data Privacy** — PII scrubbing imports (presidio, anonymize, redact); no-train flags (allow_training=False, X-Training-Data:false); output PII filter; differential privacy lib (opacus, dp-accounting); GDPR/CCPA consent. **BUY-side attestation:** training data retention policy, opt-out honored on inference, sub-processor list. **CVE:** CVE-2024-5184.

**DSGAI02 [BUILD] Agentic Credentials [VALUE-BEARING ⚠️]** — No hardcoded LLM API keys (OPENAI_API_KEY="sk-...", ANTHROPIC_API_KEY="sk-ant-..."); no hardcoded AWS/Azure/GCP creds; no wildcard token scope; vault/secrets manager retrieval; tool-call HMAC/mTLS. **CVE:** CVE-2025-0282.

**DSGAI03 [BOTH] Shadow AI** — Outbound LLM endpoint allowlist; internal proxy/gateway pattern (llm-gateway, ai-proxy); DLP/data classification before LLM call.

**DSGAI04 [BUILD] AI Supply Chain** — `torch.load()` with `weights_only=True`; sha256/signature verification; pinned ML deps (== not >=); --require-hashes; trusted registry (artifactory); SBOM (syft, cyclonedx); model card present. **CVE:** CVE-2025-24357 (vLLM).

**DSGAI05 [BUILD] RAG Data Security** — Path validation on document ingestion; access control on retrieval (acl_filter, permitted_docs); metadata-based tenant isolation; document integrity (sha256); output validation of retrieved content; max_chunk_size limit. **CVE:** CVE-2024-3584 (Qdrant).

**DSGAI06 [BUILD] MCP & Plugin Security** — HTTPS/wss MCP transport (not http://); tool argument schema validation (jsonschema, zod, pydantic); MCP server auth (api_key, bearer); no wildcard tool perms; input sanitization.

**DSGAI07 [BUILD] Data Lifecycle / TTL** — TTL on caches/sessions/vector namespaces; session cleanup (delete_session, clear_history); vector delete capability (delete_namespace); right-to-erasure handler (gdpr_delete).

**DSGAI08 [BOTH] Regulatory Compliance** — DPIA artifact; data processing agreement reference; consent capture; EU AI Act risk classification annotation; decision audit log; do_not_track honored. **BUY-side attestation:** SOC 2 / ISO 27001, DPA executed, sub-processors reviewed.

**DSGAI09 [BOTH] Multimodal Security** — EXIF/metadata stripping (strip_exif, PIL); image PII/moderation; MIME validation (magic, filetype); max upload size; steganography detection (advanced).

**DSGAI10 [BUILD] Synthetic Data Security** — Membership inference test (mia_test); k-anonymity validation; privacy-preserving lib (SDV, gretel, smartnoise); DP noise (epsilon=, noise_multiplier=); re-identification risk check.

**DSGAI11 [BUILD] Multi-Tenant Isolation** — Tenant ID required in every LLM/vector query; namespace per tenant; row-level security; session validates tenant binding; no cross-tenant shared cache. **CVE:** CVE-2024-8309 (LangChain GraphCypher).

**DSGAI12 [BUILD] Database Agent Security** — No raw LLM-output SQL execution; LangChain SQLDatabaseChain wrapped with query validator; parameterized queries; read-only DB user for agents; query allowlist/validator; LIMIT/MAX_ROWS cap; no DROP/DELETE/TRUNCATE in agent path. **CVE:** CVE-2024-8309.

**DSGAI13 [BUILD] Vector Store Security [VALUE-BEARING ⚠️]** — Vector store auth configured (QDRANT_API_KEY, PINECONE_API_KEY, etc); TLS endpoints (https://, grpcs://); not bound to 0.0.0.0 without auth; no hardcoded vector token literals. **CVEs:** CVE-2024-3584 (Qdrant), CVE-2024-37032 (Ollama).

**DSGAI14 [BUILD] AI Telemetry [VALUE-BEARING ⚠️]** — log_prompts=False in prod; PII redaction middleware; OTel/LangSmith/Langfuse excludes prompt content; no raw `print(response)` or `console.log(response)` in prod paths.

**DSGAI15 [BUILD] Context Window Security [VALUE-BEARING ⚠️]** — No secrets in system_prompt = "..."; context size limits; system_prompt loaded from config/vault (not hardcoded); no customer-360 aggregation without minimization.

**DSGAI16 [BUILD] IDE Plugin Security** — .copilotignore / .aiignore / .cursorignore present; sensitive paths excluded (.env, secrets); plugin telemetry off; context scope limits.

**DSGAI17 [BUILD] Resilience & Availability** — Circuit breaker (tenacity, resilience4j); retry with exponential backoff; timeout on LLM calls; rate limiting on incoming AI requests; fallback response on LLM unavailable; queue depth limits.

**DSGAI18 [BUILD] Model Output Security** — Output guardrails/moderation (nemo-guardrails, llm_guard); PII detection on output; logprobs not exposed by default; max_tokens always set; grounding check vs retrieved context.

**DSGAI19 [BUILD] Data Labeling Security** — PII anonymization before labeling export; data minimization; labeling SDK auth from vault; access audit log; re-identification risk check post-labeling.

**DSGAI20 [BOTH] Inference API Security** — API auth required on inference endpoint; rate limiting; input length validation; logprobs gated; ToS/AUP enforced; prompt injection detection layer. **BUY-side attestation:** provider-side rate limits, abuse detection.

**DSGAI21 [BUILD] Knowledge Store Security** — Read-only connection for RAG retrieval; no write ops from agent code paths; content validation before knowledge store write; version control on knowledge entries; namespace-scoped access.

---

## Step 1: Detect repo type and AI structure

Identify: build system (Python/Java/JS/Go), AI frameworks in use, vector stores in use, LLM providers in use, MCP/plugin presence, container/k8s manifests, CI/CD pipelines, data pipelines (Airflow, Prefect), security review artifacts (`appsec/`, `security-review/`).

---

## Step 2: Scan for DSGAI Issues

**Regex syntax:** All patterns below use PCRE / Perl-compatible regex. If your search tool uses BRE/ERE, switch to `grep -P` or `rg` (ripgrep). Plain POSIX grep will produce false negatives on `\s`, `\d`, and `{n,m}`.

### VALUE-BEARING SCAN PROTOCOL — Mandatory for DSGAI02, 13, 14, 15

For every scan tagged VALUE-BEARING:

1. **Discover files only first.** Use a "list matching files" search (e.g. `grep -lP "pattern" -r .` or `rg -l "pattern"`) — this returns paths only, never content.
2. **Locate line numbers.** Then search with line numbers (`grep -nP "pattern" file` or `rg -n "pattern" file`) on only those files.
3. **Immediately strip the content portion.** From each `file:line:content` result, extract ONLY `file:line` and discard `content`. Do not echo it. Do not paste it into the report. Do not include it in the JSON checkpoint. Do not summarize it.
4. **Render evidence only as:** `<rendered-path>:<line> — <pattern_description> (value redacted — review file directly)`

If you find yourself about to type or render a matched line containing a credential, secret, or PII — STOP. Render only the location and a description.

### Scan all 21 controls

For each control below, run the patterns (PCRE) against the listed file types. Mark PASS / WARN / FAIL based on what you find.

(All patterns are reproduced verbatim from the Claude Code skill `dsgai_scanner_tool.md`, Step 2 sections "DSGAI01 Scan" through "DSGAI21 Scan". To keep this prompt readable, the patterns are not duplicated here — open `dsgai_scanner_tool.md` and copy each `P##.#` pattern block into your search tool. Or use the consolidated pattern bundle:)

```
# DSGAI01 — Training Data Privacy [STRUCTURAL]
(anonymize|redact|scrub_pii|piiDetect|mask_pii|presidio)
(allow_training|training_opt_out|X-Training-Data|no_train)
(filter_pii|remove_pii|output_sanitize|output_filter)
(opacus|tensorflow\.privacy|dp-accounting|differential\.privacy)
(consent_capture|gdpr|ccpa|data_subject|lawful_basis)

# DSGAI02 — Credentials [VALUE-BEARING] ⚠️ FOLLOW PROTOCOL
(?i)(OPENAI_API_KEY|openai[._-]?api[._-]?key)\s*[:=]\s*["']sk-[A-Za-z0-9_\-]{20,}
(?i)(ANTHROPIC_API_KEY|anthropic[._-]?api[._-]?key)\s*[:=]\s*["']sk-ant-[A-Za-z0-9_\-]{20,}
(?i)(COHERE_API_KEY|GOOGLE_API_KEY|HF_TOKEN|HUGGINGFACE_TOKEN)\s*[:=]\s*["'][A-Za-z0-9_\-]{20,}
(AWS_ACCESS_KEY_ID|aws_access_key_id)\s*[:=]\s*["'][A-Z0-9]{16,}
(AZURE_OPENAI_KEY|GCP_SERVICE_ACCOUNT_KEY)\s*[:=]\s*["'][A-Za-z0-9_\-]{16,}
("scope"\s*:\s*"\*|permissions[^\n]{0,30}\*|scope[^\n]{0,20}admin)
(hvac\.Client|hashicorp/vault|VAULT_(ADDR|TOKEN|NAMESPACE)|secretsmanager\.|GetSecretValue|SecretManagerServiceClient|azure[._-]keyvault|@aws-sdk/client-secrets-manager)
(hmac|sign_request|verify_signature|tool_auth|mtls|mutual_tls)

# DSGAI03 — Shadow AI [STRUCTURAL]
(api\.openai\.com|api\.anthropic\.com|generativelanguage\.googleapis\.com|api\.cohere\.com|api\.together\.xyz|api\.mistral\.ai|api\.groq\.com)
(llm[._-]?gateway|ai[._-]?proxy|model[._-]?gateway|llm[._-]?proxy)
(dlp|data_classification|classify_data|sensitivity_check)

# DSGAI04 — Supply Chain [STRUCTURAL]
torch\.load\s*\(
torch\.load\s*\([^)]*weights_only\s*=\s*True
(sha256|verify_signature|model_hash|check_integrity)
^(torch|transformers|tensorflow|langchain|openai|anthropic|llama-index)\s*(>=|~=|\^|>|<|<=|\*|latest)
(syft|cyclonedx|spdx|sbom)
(index-url|extra-index-url|artifactory|jfrog|verdaccio)
(--require-hashes|integrity\s*:\s*sha)

# DSGAI05 — RAG [STRUCTURAL]
(loader\.load\(|ingest_document\(|add_documents\(|index_document\(|UnstructuredFileLoader|PyPDFLoader|DirectoryLoader)
(acl_filter|access_check|permitted_docs|filter\s*=.*tenant|namespace\s*=.*tenant)
(similarity_search|vector_search)[^)]{0,100}(filter|namespace|where)[^)]{0,40}tenant
(hashlib|sha256[^\n]{0,40}doc|integrity[._-]check|verify[._-]document)
(max_chunk_size|chunk_size\s*=|max_doc_size|content_limit)
(open\(.*\.\.|os\.path\.join\(.*request\.|Path\(.*request\.)

# DSGAI06 — MCP [STRUCTURAL]
("url"\s*:\s*"http://|transport[^\n]{0,20}http://)
(mcp[^\n]{0,30}(api_key|auth|bearer)|x-api-key[^\n]{0,20}mcp)
(jsonschema|pydantic[^\n]{0,30}validate|zod|schema[^\n]{0,20}tool|input_schema)
(tools\s*[:=]\s*\*|"tools"\s*:\s*"\*"|allow_all_tools)
uvicorn\.run\([^)]*host\s*=\s*["']0\.0\.0\.0

# DSGAI07 — Lifecycle [STRUCTURAL]
(ttl\s*=|expires_in\s*=|max_age\s*=|RETENTION_DAYS|DATA_TTL|HISTORY_TTL)
(delete_session|clear_history|purge_conversation|clear_memory|delete_conversation)
(delete_namespace|delete_collection|drop_index|delete_index|reset_collection)
(gdpr_delete|erase_user_data|handle_deletion|right_to_erasure|forget_user)

# DSGAI08 — Compliance [STRUCTURAL]
(DPIA|PIA|privacy_assessment|privacy[._-]impact)
(data_processing_agreement|DPA|sub_processor)
(consent_capture|capture_consent|consent_record|lawful_basis)
(ai_act_risk_level|high_risk_ai|limited_risk|minimal_risk)
(audit_log|decision_log|audit_trail)
(do_not_track|opt_out|DNT)

# DSGAI09 — Multimodal [STRUCTURAL]
(strip_exif|remove_metadata|PIL\.Image|exifread|piexif)
(detect_pii_in_image|content_filter|nsfw_detect|moderate_image)
(allowed_types|mime_type_check|magic\.from_buffer|filetype\.guess)
(max_upload_size|MAX_FILE_SIZE|content[._-]length[._-]limit)
(stego|steganography|stegano|lsb_detect)

# DSGAI10 — Synthetic Data [STRUCTURAL]
(membership_inference|mia_test|mia_attack)
(k_anonymity|l_diversity|t_closeness|anonymization_check)
(SDV|gretel|synthetic_data_vault|smartnoise)
(epsilon\s*=|noise_multiplier\s*=|dp_noise|laplace_noise|gaussian_noise)
(reidentification_risk|reid_check|disclosure_risk)

# DSGAI11 — Multi-tenant [STRUCTURAL]
(similarity_search|max_marginal_relevance_search|as_retriever|(vectorstore|vector_store|retriever|index|collection|client)\.(query|search)\()
(namespace\s*=[^,)]{0,40}tenant|collection[^=]{0,20}=\s*f?["'][^"']*\{?tenant|filter\s*=\s*\{[^}]*tenant)
(tenant_id\s*in\s*session|verify_tenant|assert_tenant|check_tenant|require_tenant)
(global[._-]cache|shared[._-]prompt[._-]cache)

# DSGAI12 — Database Agent [STRUCTURAL]
execute\([^)]*(llm|response|completion|output|generated)
(SQLDatabaseChain|create_sql_agent|SQLDatabaseToolkit)
(cursor\.execute\([^)]+,\s*[\[\(]|prepareStatement|bindValue|:param)
(read_only\s*=\s*True|readonly\s*=\s*True|read_only_connection|default_transaction_read_only)
(validate_query|query_validator|safe_sql|sql_guard|sanitize_sql)
\b(DROP\s+TABLE|TRUNCATE|ALTER\s+TABLE|DELETE\s+FROM)\b
(LIMIT\s+\d+|max_rows\s*=|fetch_limit\s*=)

# DSGAI13 — Vector Store [VALUE-BEARING] ⚠️ FOLLOW PROTOCOL
(CHROMA_SERVER_AUTH|QDRANT_API_KEY|PINECONE_API_KEY|WEAVIATE_API_KEY|MILVUS_TOKEN|vectorstore[^\n]{0,30}api_key)
(https://[^"']*?(qdrant|weaviate|pinecone|chroma)|ssl\s*=\s*True|tls\s*=\s*True|grpcs://)
(host[^\n]{0,15}0\.0\.0\.0|ALLOW_RESET\s*=\s*True|chroma[^\n]{0,30}http://localhost|qdrant[^\n]{0,30}http://localhost)
(QDRANT_API_KEY|PINECONE_API_KEY|WEAVIATE_API_KEY)\s*=\s*["'][A-Za-z0-9_\-]{16,}

# DSGAI14 — Telemetry [VALUE-BEARING] ⚠️ FOLLOW PROTOCOL
(log_prompts\s*=\s*False|capture_content\s*=\s*False|OTEL_LOG_PROMPTS[^\n]{0,10}false|log_completions\s*=\s*False)
(log_prompts\s*=\s*True|capture_content\s*=\s*True|log_full_response\s*=\s*True)
(redact_pii|mask_sensitive|sanitize_log|scrub[^\n]{0,10}log|log[^\n]{0,10}redact)
(print\((response|completion)|console\.log\((response|completion)|logger\.(debug|info)\([^)]*(response|completion))
(LANGSMITH_API_KEY|LANGFUSE_PUBLIC_KEY|langfuse[^\n]{0,20}init|langsmith[^\n]{0,20}trace)

# DSGAI15 — Context Window [VALUE-BEARING] ⚠️ FOLLOW PROTOCOL
(system_prompt|system_message)\s*=\s*["'][^"']*(api_key|password|secret|token|sk-)
(max_context_length\s*=|context_window_limit\s*=|max_context_tokens\s*=|truncate_context)
(system_prompt|system_message)[^\n]{0,40}(config|vault|os\.environ|getenv|secret_manager)
(customer_360|user_profile_all|fetch_all_user_data|get_full_profile|select\s*\*\s*from\s+users)

# DSGAI16 — IDE Plugins [STRUCTURAL]
(file presence) \.(copilot|ai|cursor|continue|codeium)ignore
in those files: (\.env|secrets|credentials|\.aws|\.ssh|private_key)
(telemetry[^\n]{0,10}(off|false|disabled)|share_data\s*[:=]\s*false)
(contextWindow|ignorePaths|excludeFiles|maxContextLines)

# DSGAI17 — Resilience [STRUCTURAL]
(CircuitBreaker|@circuit|tenacity|resilience4j|pybreaker)
(retry\s*\(|@retry|exponential_backoff|max_retries\s*=|backoff_factor\s*=)
(timeout\s*=\s*\d|request_timeout\s*=|httpx\.[^\n]{0,30}timeout)
(rate_limit|@throttle|RateLimiter|slowapi|flask_limiter|express-rate-limit)
(fallback_response|default_response|graceful_degradation|on_failure_return)
while\s+True[^}]{0,200}(generate|complete|chat)

# DSGAI18 — Model Output [STRUCTURAL]
(guardrails|nemo[._-]guardrails|llm_guard|output_guard|filter_output|sanitize_response|moderation)
(detect_pii[^\n]{0,20}output|output[^\n]{0,20}detect_pii|presidio[^\n]{0,20}output|scan_output)
(logprobs\s*=\s*True|return_logprobs\s*=\s*True|include_logprobs\s*=\s*True|top_logprobs\s*=\s*\d)
(\.chat\.completions\.create|client\.messages\.create|openai\.ChatCompletion|anthropic\.messages|generate_content)
max_tokens\s*=\s*\d+

# DSGAI19 — Data Labeling [STRUCTURAL]
(anonymize_for_labeling|pseudonymize|redact_before_export|mask_for_labeling)
(label_studio[^\n]{0,30}vault|labelbox[^\n]{0,30}secret|scale_api_key[^\n]{0,30}(vault|env))
(label[._-]audit|labeling_access_log|annotator_audit)
(reid_check_post_label|labeling_reidentification|post_label_validation)

# DSGAI20 — Inference API [STRUCTURAL]
(api_key[^\n]{0,15}(verify|validate)|bearer_token[^\n]{0,15}validate|Authorization[^\n]{0,15}required|@require_auth|auth_middleware|Depends\(.*auth)
(rate_limit|RateLimiter|@throttle|slowapi|flask_limiter|express-rate-limit|@limiter\.limit)
(max_input_length\s*=|max_input_tokens\s*=|input[._-]truncat|validate[._-]length)
(prompt_injection_detect|detect_injection|llm_guard|rebuff|input_guard|nemo[._-]guard)
(@app\.(post|get)\(["'][^"']*(chat|generate|completion|infer|predict)|@router\.(post|get)\(["'][^"']*(chat|generate|completion|infer|predict)|app\.(post|get)\(["'][^"']*(chat|generate|completion|infer|predict))

# DSGAI21 — Knowledge Store [STRUCTURAL]
(read_only\s*=\s*True|readonly\s*=\s*True|HttpMethod\.GET|http_method[^\n]{0,10}get)
(chromadb|qdrant|pinecone|weaviate|knowledge_base|kb_client)[^\n]{0,40}\.(upsert|insert|update|delete|add_documents|write)\(
(validate_content|sanitize[._-]write|verify[._-]knowledge|content[._-]check[._-]write)
(versioned\s*=\s*True|audit_writes|version_id|kb_audit|knowledge[._-]audit)
```

---

## Step 3: Classify findings

Statuses: **PASS** / **WARN** / **FAIL** / **NOT VALIDATED** / **NOT APPLICABLE** / **VENDOR ATTESTATION REQUIRED**.

- **FAIL** examples: hardcoded LLM API key; `torch.load()` without `weights_only=True`; raw LLM SQL execution; vector store over `http://` no auth; missing tenant isolation in multi-tenant repo.
- **WARN** examples: TTL present but excessive; auth present but scope unverifiable; hardcoded third-party LLM endpoint; logging at DEBUG level only.
- **NOT VALIDATED** examples: PII inventory; key rotation dates; vendor DPAs; red-team conducted; AppSec review done.
- **NOT APPLICABLE** examples: DSGAI09 if text-only; DSGAI10 if no synthetic generation; DSGAI19 if no labeling pipeline; DSGAI16 if backend-only.
- **VENDOR ATTESTATION REQUIRED** for BUY-tagged controls / BUY portions of BOTH: emit a callout listing the specific attestations needed (from the per-control "BUY-side attestation" notes above).

Defaulting rule: if a critical control (DSGAI02, 11) has no evidence either way, prefer FAIL — absence of a security control is a finding.

---

## Step 4: Generate the HTML report

Produce a single self-contained HTML file named `DSGAI-report.html`. Requirements:

- **PDF-first design.** No `position: sticky`, no JavaScript hide/show on findings, no interactive filter buttons that hide content. All cards always `display: block`. `page-break-inside: avoid` on each card. `print-color-adjust: exact` on body.
- **All CSS and (minimal) JS inline.** No CDN, no external fonts.
- **Obfuscation Mode badge** in header: 🛡️ `STRICT` (green) or 🔓 `INTERNAL` (yellow).
- **Evidence redaction rule:**
  - VALUE-BEARING (DSGAI02, 13, 14, 15): NEVER write the matched line. Only `<file>:<line> — <pattern_description> (value redacted — review file directly)`.
  - STRUCTURAL: write the matched line, but apply a defense-in-depth sweep first — if the line contains any of `sk-`, `sk-ant-`, `AKIA`, `Bearer <20+ chars>`, `password\s*=`, `api[._-]?key\s*=\s*"<12+ chars>`, redact it as if value-bearing.

### Report sections (in order)

1. **Header** — title "OWASP DSGAI Data Security Compliance Report", repo name, date, framework version, Obfuscation Mode badge.
2. **Nav** — static (not sticky) anchor links to Section 1 and Section 2.
3. **About This Report** — four `<h3>` subsections: Goal, How It Works, Privacy & Data Handling, Who Benefits (table).
4. **Executive Summary** — bullet points; standalone callout for remediation priority order.
5. **Dashboard cards** — Total / PASS / WARN / FAIL / NV / NA / Vendor Attestation, plus Exploitable / Patched / Unknown CVEs.
6. **Compliance bar** — visual distribution.
7. **Section 1 — DSGAI Compliance:**
   - AI Component Inventory (chips/tags)
   - Scope Tag Legend (BUILD / BUY / BOTH)
   - Summary Table (Risk ID | Name | Scope | Tier | Status | Key Evidence)
   - AI Attack Techniques (from MITRE ATLAS, if any)
   - Detailed Findings — one card per DSGAI01–21 (always visible)
   - Recommendations — Tier 1 (red, fix today), Tier 2 (yellow, backlog), Tier 3 (blue, maturity), Vendor Attestations (purple)
   - DSGAI Compliance Artifacts Checklist (15 items)
8. **Section 2 — CVE Advisory:**
   - Enrichment status banner
   - Package Inventory Table
   - CVE summary counts bar
   - CVE Groups organized by DSGAI risk (each always visible)
   - DSGAI Risk Reference grid
9. **Footer** — generation date, framework version, sources queried, obfuscation mode, print-to-PDF instructions. Attribution line with hyperlinks to OWASP GenAI Data Security Initiative (Emmanuel Guilherme Junior) and Harish Ramachandran.

### Styling

- Color scheme: GREEN `#16a34a` (pass), YELLOW `#ca8a04` (warn), RED `#dc2626` (fail), BLUE `#2563eb` (nv), GRAY `#6b7280` (na), PURPLE `#7c3aed` (vendor/info)
- Dark gradient header: `#1e1b4b` → `#312e81` → `#1e3a5f`
- White card sections, `border-radius: 12px`, subtle shadow
- Monospace font (`Menlo, Consolas, monospace`) for file paths, pattern IDs, CVE IDs

---

## Step 5: Tell the user how to open and print

After writing the file, instruct the user:

```
open DSGAI-report.html      # macOS
xdg-open DSGAI-report.html  # Linux
start DSGAI-report.html     # Windows
```

To export PDF: open in Chrome/Edge, `Ctrl+P` (or `Cmd+P`), Save as PDF.

---

## License

CC BY-SA 4.0. Original work: OWASP GenAI Data Security Initiative, led by Emmanuel Guilherme Junior. This adaptation: Harish Ramachandran.
