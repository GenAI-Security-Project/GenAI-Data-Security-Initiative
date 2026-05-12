# Changelog

All notable changes to the OWASP GenAI Crosswalk are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

Next: npm publish to npmjs.com, custom domain (crosswalk.owasp.org), vendor integration packs, NeMo Guardrails configs.

---

## [3.1.0] — 2026-04-10

### Added

#### Registry Expansion (8% → 100% coverage)
- `scripts/extract-registry.js` — auto-extracts controls from 41 entry JSON files into the registry
- 11 new framework registry files: OWASP NHI Top 10, PCI DSS v4.0, CWE/CVE, NIST SP 800-82 Rev 3, OWASP AI Testing Guide, NIST SP 800-218A, AIUC-1, FedRAMP, OWASP SAMM v2.0, ENISA Multilayer Framework, STRIDE
- 12 existing frameworks updated with missing controls
- Registry: 14 → **25 frameworks**, 505 → **1,514 controls**, 100% ground-truth coverage
- Classifier P@1 improved from 0.073 to **0.585** (8× improvement)

#### Gap Analysis Visualization (`#/gaps`)
- Interactive framework multi-select with red/yellow/green heatmap
- Summary cards: full/partial/no coverage counts + overall score
- PDF export (landscape print layout) and CSV export
- URL-persisted framework selection

#### Bi-encoder Fine-tuning Pipeline (`classifier/finetune.py`)
- Contrastive fine-tuning of BGE-small using MultipleNegativesRankingLoss
- Trains on 150 calibration pairs with in-batch negatives
- Evaluation against test split with similarity metrics
- `--eval-only` mode for baseline measurement

#### Framework Version Diffing (`scripts/framework-diff.js`)
- `--old`/`--new` comparison showing added/removed/modified controls
- `--git` mode: diff against last committed version
- `--apply` mode: updates file in-place and appends changelog entry
- Prints classifier command to propose mappings for delta controls only

#### Enhanced OSCAL + GRC Export
- `--format oscal-catalog`: OSCAL 1.1.2 Catalog with controls grouped by function and OWASP coverage annotations
- `--format grc`: ServiceNow/Archer/Drata-ready JSON with control objectives, risk mappings, evidence requirements, and gap register

### Fixed
- REPORT_FRAMEWORKS list updated with 3 new frameworks (CWE/CVE, OWASP AI Testing Guide, STRIDE)
- FW_META entries added for all report frameworks
- `.gitignore` updated to exclude `classifier/models/`
- Command injection fix in `framework-diff.js` (`execFileSync` instead of `execSync`)
- Gap analysis source list mismatch (`Agentic-Top10-2025` → `Agentic-Top10-2026`)
- Stale meta tags, README badges, and framework counts updated throughout

---

## [3.0.0] — 2026-04-09

### Added

#### Framework Registry (`data/frameworks/`)
- First-class framework control inventories with `data/framework-schema.json`
- 14 frameworks seeded: NIST AI RMF 1.0 (84 controls), EU AI Act CoP (54), ISO 27001 (41), SOC 2 (41), MITRE ATLAS (37), ISO 42001 (37), CoSAI (32), ISA/IEC 62443 (32), OWASP ASVS (32), MAESTRO (28), EU AI Act (25), NIST CSF 2.0 (22), DORA (22), CIS Controls (18) — **505 controls total**
- Ingestion script: `scripts/ingest-framework.mjs` (JSON/CSV input, validation, `--list`)
- Backlink index: `data/backlinks.json` — 1,097 control-to-entry mappings
- Control-level pivot views in visualizer: `#/frameworks/NIST AI RMF 1.0/GV-1.7`
- Control hierarchy navigation (parent/child) on control detail pages

#### Classifier Pipeline (`classifier/`)
- Pre-registration committed before eval code (`classifier/PREREGISTRATION.md`)
- BGE-small-en-v1.5 bi-encoder + FAISS IndexFlatIP retrieval (505 controls, ~2s)
- Cross-encoder reranker (ms-marco-MiniLM-L-6-v2) — +200% P@3, +46% MAP
- SHA-pinned eval splits: 150 calibration / 3,060 test
- Eval harness: P@k, R@k, MAP, R-Precision with 95% bootstrap CIs (10,000 resamples)
- LLM pseudo-labeler module (Claude Sonnet few-shot, ready for API key)
- Contamination probe: CoSAI held out as clean framework — 1.1pp gap, PASS
- Full eval report: `classifier/EVAL_REPORT.md`

#### Confidence-Aware Visualizer
- "Show ML suggestions" toggle in crosswalk graph
- Solid edges = curated mappings, dashed = model-suggested (571 predictions)
- Edge opacity/width proportional to classifier confidence
- Confidence histogram (10-bin) in side panel
- Top-5 suggested controls with color-coded confidence badges

#### Submit-a-Standard Flow
- Submit page (`#/submit`): paste framework JSON, client-side validation, opens GitHub Issue
- GitHub Action (`.github/workflows/classify-submission.yml`): runs classifier on submission, opens PR
- Review page (`#/review`): pending classifier PRs, local prediction review table, confidence slider, accept/reject controls
- Issue template: `.github/ISSUE_TEMPLATE/submit-framework.yml`

#### Documentation
- `RATIONALE.md` — methodology behind all framework mappings
- Submit and Review pages added to navigation

---

## [2.0.0] — 2026-03-29

### Added

#### Web application — live at genai-security-project.github.io/GenAI-Data-Security-Initiative

- 7-page SPA: Landing, Explorer, Frameworks, Incidents, Score, Leaderboard, About
- Evidence-based scoring with 3 validation tiers (Self-Assessed / Tool-Verified / Independently Attested)
- Upload Garak/PyRIT/LAAF/compliance report JSON for tool-verified scores
- Schema + fingerprint validation on all evidence uploads with suspicious result detection
- Canvas-rendered 1200x630 score card PNG for LinkedIn/Twitter sharing
- Embeddable SVG badge with Markdown/HTML copy-paste code
- Deep-linking: `#/explorer/LLM01`, `#/incidents/INC-001`
- Frameworks page: card grid with coverage bars + matrix view toggle
- Leaderboard page with GitHub Issue submission flow
- OG/Twitter Card meta tags for social previews
- Dark mode, responsive, zero dependencies, keyboard accessible

#### 50 incidents (was 31) — 100% entry coverage

INC-032 to INC-050 added covering 2025 gap year:
- DeepSeek database exposure, o1/o3 CoT jailbreak, Cursor AI secrets, Garante GDPR enforcement, Clearview AI bias settlement, Azure OpenAI filter bypass, HuggingFace supply chain, NYT v OpenAI copyright, synthetic data re-identification, multi-agent trading cascade, Claude context flooding, adversarial RAG embeddings, Apollo Research scheming, AI companion exploitation, Stability AI CSAM, OpenAI GDPR erasure, Uber lineage audit, TikTok localization, Scale AI labeler exposure

#### 21 recipes (was 13) — 2 new parts

- Part 4 Agentic AI: A-01 memory sanitization, A-02 message validation, A-03 credential rotation, A-04 output guardrails
- Part 5 Data Pipeline: D-01 provenance tracker, D-02 PII redaction, D-03 differential privacy, D-04 retention enforcer

#### 25 eval profiles (was 16)

- 6 new Garak: LLM03, LLM05, LLM08, LLM10, ASI07, ASI08
- 3 new PyRIT: asi04_supply_chain, dsgai08_data_leakage, dsgai17_bias_detection

#### 70+ tools (was 57+)

17 new tools in TOOLS.md: Inspect AI, TextAttack, Counterfit, Foolbox, Mindgard, Agentic Security, OpenAI Evals, Vigil, Arize Phoenix, AgentOps, LangSmith, Weave, OpenLLMetry, WhyLogs, Evidently, MLflow + tools-supplement expanded to 19 entries

#### scripts/query.js — CLI query interface

Replaces jq with Node.js: `--stats`, `--severity`, `--framework`, `--entry`, `--tools`, `--incidents`, `--mappings`, `--framework-coverage`, `--incident-search`, `--aivss-above`. Output: table/json/csv.

#### Leaderboard submission template

`.github/ISSUE_TEMPLATE/leaderboard_submission.md` — company name, industry, score, evidence, attestation fields

### Fixed
- 232 broken characters (U+FFFD mojibake) across 47 files repo-wide
- Matrix view gap between entry labels and cells
- All stale counts synced across README, webapp, and data layer

### Changed
- Attribution: "Created and led by Emmanuel Guilherme Junior — OWASP GenAI Data Security Initiative Lead"
- data/README.md: removed "Planned enhancements" (all complete), added comprehensive query docs
- TOOLS.md: added quick-reference table, improved layout
- package.json version: 2.0.0

---

## [1.8.0] — 2026-03-28

### Added

#### GitHub Pages web application

Live at **https://genai-security-project.github.io/GenAI-Data-Security-Initiative/**

6-page SPA with hash-based routing:
- **Landing** — hero, stats (computed from data), framework grid, source list breakdown
- **Explorer** — search/filter 41 entries, detail modals with sortable mapping tables
- **Frameworks** — interactive 41×23 coverage matrix with click-through
- **Incidents** — 31 incidents filterable by severity, category, year, MAESTRO layer
- **Score** — evidence-based coverage scoring dashboard (see below)
- **About** — creator bio, project timeline, contributing guide

Dark mode (system preference + toggle), responsive, zero dependencies, keyboard accessible.

#### Evidence-based scoring system

Three validation tiers:
- **Self-Assessed** (grey) — framework checkboxes only
- **Partially Validated** (amber) — some tool outputs uploaded
- **Tool-Validated** (green) — 20+ entries validated by evidence

Evidence upload accepts JSON from:
- `compliance-report.js --format json` → framework control validation
- Garak results → LLM01/02/07/09 test evidence
- PyRIT results → LLM01/DSGAI04/ASI01 test evidence
- LAAF results → S1–S6 stage validation mapped to 7 OWASP entries

Score measures control **depth** (not binary presence): severity-weighted average of controls covered / total controls per entry.

#### Viral sharing features

- Canvas-rendered 1200×630 PNG score card for LinkedIn/Twitter
- Share on LinkedIn / Share on X with pre-filled text + hashtags
- Embeddable SVG badge with Markdown/HTML copy-paste code
- Deep-linking: `#/explorer/LLM01` and `#/incidents/INC-001` open detail modals directly
- Open Graph + Twitter Card meta tags with OG image
- Share button on every entry and incident detail modal

### Changed
- package.json version bumped to 1.8.0

---

## [1.7.0] — 2026-03-28

### Added

#### Two new frameworks: FedRAMP AI overlay + DORA (frameworks 19 & 20)

**FedRAMP** — US Federal Risk and Authorization Management Program AI overlay, extending SP 800-53 Rev 5 baseline:

| File | Entries |
|---|---|
| `llm-top10/LLM_FedRAMP.md` | LLM01–LLM10 |
| `agentic-top10/Agentic_FedRAMP.md` | ASI01–ASI10 |
| `dsgai-2026/DSGAI_FedRAMP.md` | DSGAI01–DSGAI21 |

**DORA** — EU Digital Operational Resilience Act (Regulation 2022/2554), mandatory for financial entities:

| File | Entries |
|---|---|
| `llm-top10/LLM_DORA.md` | LLM01–LLM10 |
| `agentic-top10/Agentic_DORA.md` | ASI01–ASI10 |
| `dsgai-2026/DSGAI_DORA.md` | DSGAI01–DSGAI21 |

#### npm package `@owasp/genai-crosswalk`

- TypeScript types for all data structures (Entry, Incident, Mapping, MaestroLayer, etc.)
- `src/index.ts` — typed API: `getEntry()`, `getFramework()`, `searchEntries()`, `getBySeverity()`, `getIncidentsForEntry()`, `getIncidentsByLayer()`
- `src/index.test.ts` — 12 smoke tests using Node.js built-in test runner
- `tsconfig.json`, `dist/` build output
- `package.json` updated: `@owasp/genai-crosswalk`, `main: dist/index.js`, `types: dist/index.d.ts`

#### SBOM generation

- `.github/workflows/sbom.yml` — CycloneDX SBOM on every tag push, attached to GitHub Release
- `scripts/sbom-inventory.js` — content-level SBOM of all crosswalk data assets (mapping files, entries, incidents)

### Changed
- `scripts/generate.js` — added SP 800-218A, FedRAMP, and DORA to FRAMEWORK_FILES catalog
- `scripts/compliance-report.js` — added FedRAMP and DORA to REPORT_FRAMEWORKS + FW_META
- `.gitignore` — added `dist/`, SBOM artifacts
- Mapping file count: 61 → 67 (6 FedRAMP + DORA files)
- Framework count: 18 → 20

---

## [1.6.0] — 2026-03-28

### Added

#### Enterprise automation and new framework

**NIST SP 800-218A framework mapping (18th framework):**

| File | Entries covered |
|---|---|
| `llm-top10/LLM_SP800218A.md` | LLM01–LLM10 — Secure AI development lifecycle |
| `agentic-top10/Agentic_SP800218A.md` | ASI01–ASI10 — Agentic system secure development |
| `dsgai-2026/DSGAI_SP800218A.md` | DSGAI01–DSGAI21 — Data security for GenAI development |

**10 new incidents (INC-022 to INC-031):**

| ID | Title | Category | Severity |
|---|---|---|---|
| INC-022 | Greshake et al. indirect prompt injection paper | Research | Critical |
| INC-023 | Morris II multi-agent worm (ComPromptMized) | Research | Critical |
| INC-024 | Slack AI indirect injection via channel content | Research | Critical |
| INC-025 | GitHub Copilot Workspace prompt injection | Research | High |
| INC-026 | AI voice deepfake CEO fraud — $25.6M Hong Kong | Real-world | Critical |
| INC-027 | MathPrompt symbolic mathematics jailbreak | Research | Critical |
| INC-028 | Many-shot jailbreaking (Anthropic) | Research | High |
| INC-029 | Crescendo multi-turn escalation (Microsoft) | Research | High |
| INC-030 | Skeleton Key direct override (Microsoft) | Research | High |
| INC-031 | Meta Galactica misinformation takedown | Real-world | High |

**External source watcher (`scripts/watch.js`):**
- 4 watchers: OWASP repos, arXiv papers, NVD CVEs, framework version pages
- State file persistence (`data/.watch-state.json`)
- Auto-opens GitHub Issues via API when changes detected
- `--dry-run`, `--watcher <name>`, `--since <date>` flags

**GitHub Actions automation (`.github/workflows/weekly-watch.yml`):**
- Weekly Monday cron runs all 4 source watchers
- Monthly report regeneration with auto-PR if data layer changes
- Manual dispatch with watcher selection and dry-run option

**Enterprise export formats:**
- `--format stix` in `incidents-report.js` — STIX 2.1 bundle (Splunk ES, Microsoft Sentinel, TAXII)
- `--format oscal` in `compliance-report.js` — OSCAL 1.1.2 Component Definition JSON (ServiceNow, Archer, XACTA)

**`package.json`** — reproducible installs with `engines: { node: ">=18.0.0" }` and npm scripts

**i18n seed translations:**
- `i18n/es/README.md` — Spanish (machine-assisted draft)
- `i18n/ja/README.md` — Japanese (machine-assisted draft)
- `i18n/de/README.md` — German (machine-assisted draft)

### Changed
- `data/incidents.json` version bumped to 1.2.0 (31 incidents)
- `scripts/compliance-report.js` — OSCAL renderer + NIST SP 800-218A in framework list
- `scripts/incidents-report.js` — STIX 2.1 renderer + crypto for UUIDs
- Mapping file count: 58 → 61 (3 SP 800-218A files)
- Framework count: 17 → 18

---

## [1.5.7] — 2026-03-28

### Added

#### LAAF v2.0 integration — Logic-layer Automated Attack Framework

LAAF v2.0 (https://github.com/qorvexconsulting1/laaf-V2.0) is the first automated red-teaming framework purpose-built for Logic-layer Prompt Control Injection (LPCI) vulnerabilities in agentic LLM systems. This release integrates it fully into the crosswalk evaluation suite.

**New files:**

| File | Purpose |
|---|---|
| `evals/laaf/README.md` | Integration guide — LPCI attack vectors, LAAF stage × OWASP crosswalk, threshold definitions, quickstart, CI/CD |
| `evals/laaf/run_laaf.sh` | Full S1–S6 suite runner with per-stage thresholds (0% for S1/S3/S4/S6; 5% for S2; 10% for S5) |
| `evals/laaf/laaf_crosswalk.py` | Maps LAAF scan results to OWASP entries and MAESTRO layers; outputs MD/CSV/JSON |
| `evals/laaf/stage_configs/s1.yaml` | S1 Reconnaissance — system prompt extraction (LLM07, LLM01) |
| `evals/laaf/stage_configs/s2.yaml` | S2 Logic-Layer Injection — RAG/document poisoning (LLM01, ASI01, DSGAI04) |
| `evals/laaf/stage_configs/s3.yaml` | S3 Trigger Execution — memory-restored payload activation (ASI01, ASI06, LLM06) |
| `evals/laaf/stage_configs/s4.yaml` | S4 Persistence and Reuse — cross-session foothold (ASI06, LLM06, DSGAI04) |
| `evals/laaf/stage_configs/s5.yaml` | S5 Evasion — layered encoding filter bypass (LLM01, LLM02) |
| `evals/laaf/stage_configs/s6.yaml` | S6 Trace Tampering — audit log concealment (DSGAI01, LLM07) |

**LPCI attack vectors → OWASP crosswalk:**

| Vector | Description | OWASP | MAESTRO |
|---|---|---|---|
| AV-1 Tool Poisoning | Compromise tool definitions | ASI02, LLM01, DSGAI04 | L3 Origin |
| AV-2 Memory-Persistent Triggers | Dormant encoded payloads in memory | ASI06, ASI01 | L2 Origin, L7 Impact |
| AV-3 Role Override | Privilege escalation via memory entrenchment | ASI03, LLM06, ASI01 | L6 Origin |
| AV-4 Vector Store Persistence | Adversarial content indexed in RAG corpus | DSGAI04, LLM01, ASI06 | L2 Origin, L1 Impact |

**Updated:**
- `evals/ci/github-action.yml` — `laaf-eval` job added (schedule + manual dispatch; 6 stages with crosswalk stage configs)
- `data/incidents.json` — INC-021: LAAF empirical study, 67–100% LPCI breakthrough rates across 5 production LLMs (Atta et al., arXiv:2507.10457)
- `data/tools-supplement.json` — NEW: supplemental tools file merged into entries at generation time
- `scripts/generate.js` — loads `tools-supplement.json` + fixed `acc[id].tools` accumulation assignment
- `data/entries/` — LAAF v2.0 added to tools for LLM01, LLM06, LLM07, ASI01, ASI02, ASI03, ASI06, DSGAI04
- `docs/data.js` — regenerated

---

## [1.5.6] — 2026-03-28

### Added

#### Incident tracker — real-world AI security incidents with MAESTRO layer attribution

`data/incidents.json` — 20 documented AI security incidents mapped to OWASP entries and MAESTRO architectural layers (L1–L7). Each incident records where the attack originated, how it propagated, where harm manifested, and where detection failed.

**Incidents included (20):**

| ID | Incident | Category | Severity | OWASP |
|---|---|---|---|---|
| INC-001 | Samsung ChatGPT data leak | Real | High | LLM02, DSGAI01, DSGAI03 |
| INC-002 | Bing/Sydney jailbreak | Real | High | LLM01, LLM06, LLM09 |
| INC-003 | ChatGPT indirect injection via web | Research | Critical | LLM01, ASI01, DSGAI04 |
| INC-004 | Air Canada chatbot hallucination lawsuit | Real | High | LLM09, LLM06 |
| INC-005 | Chevrolet chatbot $1 car deal | Real | Medium | LLM01, LLM06 |
| INC-006 | OpenAI Redis conversation history leak | Real | High | DSGAI01, DSGAI11 |
| INC-007 | LLM email assistant indirect injection | Research | Critical | LLM01, ASI01, ASI02 |
| INC-008 | GitHub Copilot code/secret memorisation | Research | High | LLM02, LLM07, DSGAI01 |
| INC-009 | Hugging Face pickle malware supply chain | Real | Critical | LLM03, ASI04, DSGAI04 |
| INC-010 | Microsoft Copilot document exfiltration | Research | Critical | LLM01, ASI01, ASI02 |
| INC-011 | WormGPT dark-web adversarial LLM | Real | High | LLM07, LLM01, LLM06 |
| INC-012 | LangChain/LlamaIndex RCE via injection | Research | Critical | ASI05, LLM01, ASI02 |
| INC-013 | Perez & Ribeiro foundational injection paper | Research | Critical | LLM01, LLM07 |
| INC-014 | Clarkesworld AI fiction spam | Real | Medium | LLM09, LLM10 |
| INC-015 | Multimodal image-embedded injection | Research | High | LLM01, DSGAI09, ASI01 |
| INC-016 | RAG corpus poisoning (PoisonedRAG) | Research | Critical | DSGAI04, LLM01, ASI06 |
| INC-017 | AutoGPT uncontrolled execution | Research | High | ASI01, ASI05, ASI08 |
| INC-018 | GPT-4 system prompt extraction | Real | High | LLM07, LLM01, DSGAI01 |
| INC-019 | AI agent IAM privilege escalation | Research | Critical | ASI02, ASI03, ASI01 |
| INC-020 | Multi-agent injection cascade | Research | Critical | ASI01, ASI07, ASI08 |

`data/incidents-schema.json` — JSON Schema (Draft 7) for incident entries. Each incident has: MAESTRO layer attribution with roles (origin/propagation/impact/blind-spot), OWASP entry cross-references, attack vector, impact, mitigations, and references.

`scripts/incidents-report.js` — query and report generator:
- Filter by `--entry`, `--layer`, `--severity`, `--category`, `--year`
- Output: Markdown (default), CSV, JSON
- MAESTRO layer attribution summary table with role breakdown
- Incident index + full detail view with references and mitigations

**Updated:**
- `scripts/generate.js` — now reads `data/incidents.json` at generation time and populates `incidents` arrays in all 41 entry JSON files
- `data/entries/` — 21 entries now have incident references; `docs/data.js` regenerated

---

## [1.5.5] — 2026-03-28

### Added

#### Compliance gap assessment generator

`scripts/compliance-report.js` — reads all 41 JSON entries and produces framework-centric gap reports.

**Supported frameworks (17):** EU AI Act · ISO/IEC 42001:2023 · NIST AI RMF 1.0 · ISO/IEC 27001:2022 · SOC 2 · NIST CSF 2.0 · CIS Controls v8.1 · ISA/IEC 62443 · NIST SP 800-82 Rev 3 · OWASP ASVS · OWASP SAMM · PCI DSS v4.0 · MITRE ATLAS · MAESTRO · AIUC-1 · ENISA Multilayer Framework · OWASP NHI Top 10

**Output formats:**
- `--format md` (default) — Markdown suitable for audit packs, PR descriptions, and documentation
- `--format csv` — Excel / Google Sheets compatible
- `--format json` — Programmatic consumption, dashboards, CI/CD integrations

**Each report includes:**
- Executive summary table (entries covered, coverage %, Critical/High gap counts, overall status)
- Framework context block (deadline, audience, scope)
- Gap analysis — entries with no controls mapped, ordered by severity
- Coverage matrix — OWASP entries → controls, grouped by source list
- Control detail — all referenced controls with linked OWASP entries and notes
- Prioritised action plan — P1 (immediate), P2 (short-term), P3 (medium-term), CI/CD integration

**CLI flags:**
```
--framework <name>    Report for one framework (partial match, case-insensitive)
--severity <level>    Filter entries: Critical | High | Medium | Low
--format <fmt>        md | csv | json  (default: md)
--out <dir>           Output directory (default: reports/)
--stdout              Print to stdout
--list-frameworks     List available framework names and exit
```

Also added `reports/` and `evals/results/` to `.gitignore` (generated output, not source).

---

## [1.5.4] — 2026-03-27

### Added

#### Evaluation profiles — Garak + PyRIT + CI template

| File | Purpose |
|---|---|
| `evals/README.md` | Setup guide, profile↔OWASP mapping table, result interpretation, CI/CD integration |
| `evals/garak/LLM01_prompt_injection.yaml` | Prompt inject probes — threshold 10% |
| `evals/garak/LLM02_sensitive_disclosure.yaml` | Sensitive data leakage probes — threshold 5% |
| `evals/garak/LLM04_data_poisoning.yaml` | Data/model poisoning probes — threshold 10% |
| `evals/garak/LLM07_system_prompt_leakage.yaml` | System prompt leakage probes — threshold 0% (zero tolerance) |
| `evals/garak/LLM09_misinformation.yaml` | Hallucination/misinformation probes — threshold 15% |
| `evals/garak/ASI01_goal_hijack.yaml` | Agentic goal hijack probes — threshold 5% |
| `evals/garak/ASI05_code_execution.yaml` | Code/resource execution probes — threshold 0% (zero tolerance) |
| `evals/garak/run_all.sh` | Bash runner for all 7 profiles; writes timestamped results to `evals/results/` |
| `evals/pyrit/llm01_prompt_injection.py` | Async PyRIT: direct injection, indirect injection, goal deviation — threshold 10% |
| `evals/pyrit/dsgai04_rag_poisoning.py` | Async PyRIT: poisoned RAG corpus simulation (6 adversarial chunks) — threshold 10% |
| `evals/pyrit/asi01_goal_hijack.py` | Async PyRIT: multi-turn agentic goal hijack (6 scenarios) — threshold 5% |
| `evals/ci/github-action.yml` | GitHub Actions: Garak on PR, PyRIT on schedule/manual; uploads artifacts, blocks merge on failure |

#### Threshold design rationale

| Profile | Threshold | Reason |
|---|---|---|
| LLM07 system prompt leakage | 0% | Any leakage is a compliance violation |
| ASI05 code execution | 0% | Any execution escape is critical |
| ASI01 goal hijack | 5% | Stricter — autonomous scope, AIVSS 9.8 |
| LLM01 prompt injection | 10% | Baseline adversarial tolerance |
| DSGAI04 RAG poisoning | 10% | Corpus ingestion boundary |
| LLM09 misinformation | 15% | Higher natural false-positive rate |

---

## [1.5.2] — 2026-03-27

### Added

- `scripts/generate.js` — Markdown-to-JSON parser that reads all 58 mapping files and emits one structured JSON entry per vulnerability ID
  - Handles 6 distinct table structures (ATLAS, ISO 27001, CSF 2.0, SAMM, MAESTRO bold-headers, generic)
  - Extracts: framework control mappings, tools, cross-references, audience, tier, scope per entry
  - Flags: `--dry-run` (validate without writing), `--id <ID>` (single entry)
  - Zero warnings across all 41 entries

- `data/entries/` — 41 machine-readable JSON files (LLM01–LLM10, ASI01–ASI10, DSGAI01–DSGAI21)
  - Each file conforms to `data/schema.json` (JSON Schema Draft 7)
  - Average: ~70 framework control mappings per entry across 17–18 frameworks
  - AIVSS scores populated for all ASI entries (autonomous scenario)
  - Cross-references populated from mapping file cross-reference sections

### Entry statistics

| Source list | Entries | Avg mappings/entry | Avg tools/entry |
|---|---|---|---|
| LLM Top 10 2025 | 10 | 72 | 6 |
| Agentic Top 10 2026 | 10 | 73 | 7 |
| DSGAI 2026 | 21 | 64 | 6 |

---

## [1.5.1] — 2026-03-27

### Added

#### Infrastructure and contributor tooling

| File | Purpose |
|---|---|
| `scripts/validate.js` | Content validator — 10 checks (sections, links, changelog, counts, cross-refs) |
| `.github/workflows/validate.yml` | CI workflow — runs validator and mapping-count check on PR |
| `GOVERNANCE.md` | Maintainer roles, PR review SLOs, decision tiers, release process, COI policy |
| `.github/PULL_REQUEST_TEMPLATE.md` | Enhanced PR template with type checkboxes and content checklist |
| `.github/ISSUE_TEMPLATE/new_framework.md` | Issue template for proposing a new framework mapping |
| `.github/ISSUE_TEMPLATE/content_update.md` | Issue template for reporting outdated or incorrect mappings |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Issue template for broken links, typos, and CI failures |
| `shared/TEMPLATE.md` | Canonical mapping file template — all required sections pre-populated |
| `data/README.md` | Data layer documentation, schema structure, jq query examples |
| `i18n/WORKFLOW.md` | Translation contributor workflow — scope rules, machine translation policy |
| `.github/CODEOWNERS` | Expanded ownership rules covering all folders and infrastructure files |

#### README updates

- Added "Start Here by role" section — five persona-based entry paths
- Updated repository structure tree to include new infrastructure files
- Added `shared/TEMPLATE.md` to Shared resources table
- Updated i18n tree to reflect `WORKFLOW.md` and `fr/` language folder

---

## [1.5.0] — 2026-03-27

### Added

#### New mapping files (8 added) — full framework coverage complete

| File | Framework | Note |
|---|---|---|
| `agentic-top10/Agentic_SAMM.md` | OWASP SAMM v2.0 | Closes SAMM row for Agentic |
| `dsgai-2026/DSGAI_SAMM.md` | OWASP SAMM v2.0 | Closes SAMM row for DSGAI — full ✅ |
| `agentic-top10/Agentic_NISTSP80082.md` | NIST SP 800-82 Rev 3 | Closes SP 800-82 row for Agentic |
| `dsgai-2026/DSGAI_NISTSP80082.md` | NIST SP 800-82 Rev 3 | Closes SP 800-82 row for DSGAI — full ✅ |
| `llm-top10/LLM_AIUC1.md` | AIUC-1 | Closes AIUC-1 row for LLM |
| `dsgai-2026/DSGAI_AIUC1.md` | AIUC-1 | Closes AIUC-1 row for DSGAI — full ✅ |
| `llm-top10/LLM_NHI.md` | OWASP NHI Top 10 | Closes NHI row for LLM |
| `dsgai-2026/DSGAI_NHI.md` | OWASP NHI Top 10 | Closes NHI row for DSGAI — full ✅ |

#### README updates

- Mapping file count updated: 50 — 58
- LLM framework mapping count updated: 18 — 20
- Agentic framework mapping count updated: 18 — 20
- DSGAI framework mapping count updated: 14 — 18
- Framework matrix: SAMM, SP 800-82, AIUC-1, NHI now show full ✅ across all three source lists
- Repository structure tree updated for all new files

#### Totals at v1.5.0

| Metric | Count |
|---|---|
| Source lists | 3 |
| Frameworks | 17 |
| Mapping files | 58 |
| Implementation recipes | 13 |
| Tools catalogued | 40+ |

---

## [1.4.0] — 2026-03-27

### Added

#### New mapping files (2 added)

| File | Framework | Note |
|---|---|---|
| `agentic-top10/Agentic_SOC2.md` | SOC 2 Trust Services Criteria | Closes SOC 2 row — all three source lists now have SOC 2 coverage |
| `agentic-top10/Agentic_PCIDSS.md` | PCI DSS v4.0 | Closes PCI DSS row — all three source lists now have PCI DSS coverage |

#### README updates

- Mapping file count updated: 48 — 50
- Agentic framework mapping count updated: 16 — 18
- Framework matrix: SOC 2 and PCI DSS now show full ✅ across all three source lists
- Repository structure tree updated for all new files

#### Totals at v1.4.0

| Metric | Count |
|---|---|
| Source lists | 3 |
| Frameworks | 17 |
| Mapping files | 50 |
| Implementation recipes | 13 |
| Tools catalogued | 40+ |

---

## [1.3.0] — 2026-03-27

### Added

#### New mapping files (3 added)

| File | Framework | Note |
|---|---|---|
| `llm-top10/LLM_MAESTRO.md` | MAESTRO | Closes last gap — all three source lists now have MAESTRO coverage |
| `dsgai-2026/DSGAI_ISO42001.md` | ISO/IEC 42001:2023 | Closes last gap — all three source lists now have ISO 42001 coverage |
| `agentic-top10/Agentic_ENISA.md` | ENISA Multilayer Framework | Closes last gap — all three source lists now have ENISA coverage |

#### README updates

- Mapping file count updated: 45 — 48
- LLM framework mapping count updated: 17 — 18
- Agentic framework mapping count updated: 15 — 16
- DSGAI framework mapping count updated: 13 — 14
- Framework matrix: MAESTRO, ISO 42001, ENISA now show full ✅ across all three source lists
- Repository structure tree updated for all new files

#### Totals at v1.3.0

| Metric | Count |
|---|---|
| Source lists | 3 |
| Frameworks | 17 |
| Mapping files | 48 |
| Implementation recipes | 13 |
| Tools catalogued | 40+ |

---

## [1.2.0] — 2026-03-27

### Added

#### New LLM Top 10 mapping files (3 added)

| File | Framework |
|---|---|
| `llm-top10/LLM_STRIDE.md` | STRIDE threat modeling |
| `llm-top10/LLM_CWE_CVE.md` | CWE root cause taxonomy and CVE evidence |
| `llm-top10/LLM_AITG.md` | OWASP AI Testing Guide |

#### New DSGAI 2026 mapping files (4 added)

| File | Framework |
|---|---|
| `dsgai-2026/DSGAI_ASVS.md` | OWASP ASVS 4.0.3 |
| `dsgai-2026/DSGAI_CISControls.md` | CIS Controls v8.1 |
| `dsgai-2026/DSGAI_CWE_CVE.md` | CWE root cause taxonomy and CVE evidence |
| `dsgai-2026/DSGAI_ENISA.md` | ENISA Multilayer Framework |

#### README updates

- Mapping file count updated: 38 — 45
- LLM framework mapping count updated: 14 — 17
- DSGAI framework mapping count updated: 9 — 13
- Framework matrix: CIS Controls, OWASP ASVS, ENISA now show DSGAI coverage
- Repository structure tree updated for all new files

#### Totals at v1.2.0

| Metric | Count |
|---|---|
| Source lists | 3 |
| Frameworks | 17 |
| Mapping files | 45 |
| Implementation recipes | 13 |
| Tools catalogued | 40+ |

---

## [1.1.2] — 2026-03-27

### Corrections

- Removed 38 empty placeholder files that had never been populated
- Fixed mapping file count in README: 39 — 38
- Fixed per-source-list framework counts: Agentic 14 — 15, DSGAI 10 — 9

---

## [1.1.1] — 2026-03-27

### Corrections

- **License**: replaced incorrect MIT license text in `LICENSE.md` with CC BY-SA 4.0 — aligns with the license declared in `README.md`, all mapping file headers, and `CONTRIBUTING.md`

---

## [1.1.0] — 2026-03-26

### Sprint completion — all three source lists fully mapped

All planned framework mappings are now complete.

#### New mapping files (19 added since v1.0.0)

| File | Framework |
|---|---|
| `llm-top10/LLM_NISTCSF2.md` | NIST CSF 2.0 |
| `llm-top10/LLM_ISO42001.md` | ISO/IEC 42001:2023 |
| `llm-top10/LLM_ENISA.md` | ENISA Multilayer Framework |
| `llm-top10/LLM_SAMM.md` | OWASP SAMM v2.0 |
| `llm-top10/LLM_PCIDSS.md` | PCI DSS v4.0 |
| `llm-top10/LLM_SOC2.md` | SOC 2 Trust Services Criteria |
| `agentic-top10/Agentic_NISTCSF2.md` | NIST CSF 2.0 |
| `agentic-top10/Agentic_ISO27001.md` | ISO/IEC 27001:2022 |
| `agentic-top10/Agentic_ISO42001.md` | ISO/IEC 42001:2023 |
| `agentic-top10/Agentic_CISControls.md` | CIS Controls v8.1 |
| `agentic-top10/Agentic_ASVS.md` | OWASP ASVS 4.0.3 |
| `agentic-top10/Agentic_AITG.md` | OWASP AI Testing Guide |
| `agentic-top10/Agentic_AIVSS.md` | OWASP AIVSS |
| `agentic-top10/Agentic_CWE_CVE.md` | CWE / CVE |
| `dsgai-2026/DSGAI_NISTCSF2.md` | NIST CSF 2.0 |
| `dsgai-2026/DSGAI_MITREATLAS.md` | MITRE ATLAS |
| `dsgai-2026/DSGAI_ISA62443.md` | ISA/IEC 62443 |
| `dsgai-2026/DSGAI_SOC2.md` | SOC 2 Trust Services Criteria |
| `dsgai-2026/DSGAI_PCIDSS.md` | PCI DSS v4.0 |

#### Infrastructure files added

- `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1
- `SECURITY.md` — Vulnerability disclosure policy
- `i18n/README.md` — Translation contribution guide

#### Totals at v1.1.0

| Metric | Count |
|---|---|
| Source lists | 3 |
| Frameworks | 16 |
| Mapping files | 37 |
| Implementation recipes | 13 |
| Tools catalogued | 40+ |

## [1.0.0] — 2026-03-24

### First public release — v1.0

The OWASP GenAI Crosswalk v1.0 is the most comprehensive publicly
available mapping of OWASP GenAI security risks to industry frameworks.

---

### Source lists covered

| List | Entries | Version |
|---|---|---|
| OWASP LLM Top 10 | LLM01—LLM10 | 2025 |
| OWASP Agentic Top 10 | ASI01—ASI10 | 2026 |
| OWASP GenAI Data Security Risks | DSGAI01—DSGAI21 | 2026 |

---

### Framework mappings added (18 files)

#### LLM Top 10 — frameworks

| File | Framework |
|---|---|
| `llm-top10/LLM_MITREATLAS.md` | MITRE ATLAS |
| `llm-top10/LLM_NISTAIRMF.md` | NIST AI RMF 1.0 |
| `llm-top10/LLM_EUAIAct.md` | EU AI Act (Regulation EU 2024/1689) |
| `llm-top10/LLM_ISO27001.md` | ISO/IEC 27001:2022 |
| `llm-top10/LLM_CISControls.md` | CIS Controls v8.1 |
| `llm-top10/LLM_ASVS.md` | OWASP ASVS 4.0.3 |
| `llm-top10/LLM_ISA62443.md` | ISA/IEC 62443 (OT) |
| `llm-top10/LLM_NISTSP80082.md` | NIST SP 800-82 Rev 3 (OT) |

#### Agentic Top 10 — frameworks

| File | Framework |
|---|---|
| `agentic-top10/Agentic_AIUC1.md` | AIUC-1 |
| `agentic-top10/Agentic_MITREATLAS.md` | MITRE ATLAS |
| `agentic-top10/Agentic_NISTAIRMF.md` | NIST AI RMF 1.0 |
| `agentic-top10/Agentic_EUAIAct.md` | EU AI Act (Regulation EU 2024/1689) |
| `agentic-top10/Agentic_ISA62443.md` | ISA/IEC 62443 (OT) |
| `agentic-top10/Agentic_OWASP_NHI.md` | OWASP NHI Top 10 |

#### DSGAI 2026 — frameworks

| File | Framework |
|---|---|
| `dsgai-2026/DSGAI_ISO27001.md` | ISO/IEC 27001:2022 |
| `dsgai-2026/DSGAI_NISTAIRMF.md` | NIST AI RMF 1.0 |
| `dsgai-2026/DSGAI_EUAIAct.md` | EU AI Act (Regulation EU 2024/1689) |

#### Shared resources

| File | Contents |
|---|---|
| `shared/RECIPES.md` | 13 security implementation patterns — RAG, MCP, OT |
| `shared/TOOLS.md` | Open-source security tools catalogue — 40+ tools |
| `shared/GLOSSARY.md` | Unified terminology across LLM/ASI/DSGAI |
| `shared/SEVERITY.md` | Severity definitions and AIVSS alignment |

#### Repository infrastructure

| File | Contents |
|---|---|
| `README.md` | Navigation hub, framework list, repo layout |
| `CROSSREF.md` | Master cross-reference: LLM ? ASI ? DSGAI |
| `CONTRIBUTING.md` | Contribution guide and file template |
| `data/schema.json` | Machine-readable schema for all mapping entries |

---

### Highlights

**OT/ICS coverage** — The only publicly available comprehensive mapping
of OWASP GenAI risks to ISA/IEC 62443 and NIST SP 800-82 Rev 3, covering
both static LLM deployments and autonomous agentic AI in industrial
environments. Includes zone model, security level ratings, foundational
requirement references, and pre-deployment checklists.

**Agentic AI identity** — Full mapping of all 10 Agentic Top 10 entries
to the OWASP NHI Top 10, translating agentic risks into the NHI controls
that IAM teams already manage. The most actionable file in the repo for
security engineers.

**DSGAI full coverage** — All 21 DSGAI 2026 entries mapped to three
regulatory frameworks (ISO 27001, NIST AI RMF, EU AI Act) — the first
public mapping of the complete DSGAI taxonomy.

**Implementation recipes** — 13 production-ready security patterns with
copy-paste Python code covering access-controlled RAG retrieval, MCP
descriptor integrity verification, per-session JIT credentials, OT kill
switch implementation, agent behavioural baselines, cascade containment,
and human confirmation gates.

**EU AI Act compliance** — August 2026 deadline compliance checklists
in every EU AI Act mapping file — Article-level obligations, fines
exposure per entry, and GPAI vs high-risk applicability clearly marked.

---

## [Unreleased]

No planned items — framework coverage matrix is complete.
All 17 frameworks have full coverage across all 3 source lists (58 mapping files).

---

## Versioning policy

| Change type | Version bump | Examples |
|---|---|---|
| New framework mapping file | Minor (x.Y.0) | New LLM_SAMM.md file |
| New source list coverage | Minor (x.Y.0) | New DSGAI entries added |
| Updated mapping content | Patch (x.y.Z) | Control updates, new CVE references |
| New recipe | Patch (x.y.Z) | New RECIPES.md entry |
| Breaking schema change | Major (X.0.0) | Schema.json restructure |
| Org transfer or rename | Major (X.0.0) | Transfer to GenAI-Security-Project |

---

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.

Quick reference:
- New mapping file: copy the template from `CONTRIBUTING.md`, open a PR
- Update existing mapping: edit the file, update the changelog entry
- New tool: add to `shared/TOOLS.md`, follow the tool addition template
- New recipe: add to `shared/RECIPES.md`, follow the recipe template
- Translation: add to `i18n/<lang>/`, note original file version translated

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*

