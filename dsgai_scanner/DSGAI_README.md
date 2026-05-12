# /GenAIDataSecurity — OWASP GenAI Data Security Compliance Skill

A Claude Code slash command that automatically scans GenAI and agentic codebases against the **OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0)** — covering all 21 DSGAI risk controls across the full GenAI data lifecycle.

---

## What It Does

When you run `/GenAIDataSecurity` inside a repository, the skill:

1. **Detects** whether the repo contains GenAI/agentic patterns (LangChain, LlamaIndex, OpenAI SDK, vector stores, MCP servers, etc.) — bails out gracefully if none are found
2. **Enriches live CVEs** by querying OSV, NVD, and GitHub Advisory Database against the exact package versions pinned in the repo
3. **Scans source code** for all 21 DSGAI risk indicators — credentials, SQL injection via LLM output, vector store auth, telemetry logging, RAG access controls, MCP transport security, and more
4. **Generates `DSGAI-report.html`** — a self-contained, print-ready HTML report with findings, file paths, line numbers, remediation steps, and a live CVE advisory panel

**Performance:** All 21 control scans and all CVE source queries run as parallel tool calls — the skill fires multiple grep scans and API requests simultaneously rather than sequentially. This reduces total scan time.

---

## Privacy & Data Handling

This skill runs **entirely on your local machine**. Your source code is never uploaded, transmitted, or shared with any external service.

**What stays local:**

- All source code files scanned for security patterns
- Configuration files, secrets, environment variables
- Dependency manifests and build files

**What is sent to the internet (CVE lookups only):**

- Package names and version numbers (e.g. `langchain==0.1.0`) are sent to public vulnerability databases to check for known CVEs
- Only these public databases are queried: [OSV](https://osv.dev), [NVD](https://nvd.nist.gov), [GitHub Advisory Database](https://github.com/advisories)
- No actual code, secrets, file contents, or identifying information leaves your machine

**Live CVE lookups are optional.** If your environment has no internet access or you prefer fully offline operation, the skill falls back to its embedded CVE database automatically — the scan still runs and produces a complete report.

---

## Prerequisites

- A repository containing GenAI or agentic code (Python, TypeScript, Java, Go)
- An AI coding tool with **file reading access** to your codebase (see supported tools below)
- **Web access** in your AI tool for live CVE lookups (Step 0.5) — if unavailable, the scan still runs using the embedded CVE database in the skill file

No Python packages or external tools required to generate the HTML report.

---

## Running with Claude Code (Native)

Claude Code has first-class support for this skill via its slash command system.

**Installation — macOS / Linux:**
```bash
cp GenAIDataSecurity.md ~/.claude/commands/
```

**Installation — Windows:**
```
copy GenAIDataSecurity.md %USERPROFILE%\.claude\commands\
```

**Usage:**
1. Open your GenAI repository in [Claude Code](https://claude.ai/code) (CLI, desktop app, or VS Code / JetBrains extension)
2. Type `/GenAIDataSecurity` and press Enter
3. Claude scans the codebase — typically 2–5 minutes depending on repo size
4. A `DSGAI-report.html` file is saved at the repository root and opens in your browser

---

## Running with Other AI Coding Tools

The skill file is plain Markdown. Any AI tool with file reading access to your codebase can run it — just paste the contents as your prompt.

| Tool | How to run |
|---|---|
| **Cursor** | Open `GenAIDataSecurity.md`, copy the contents, paste into Cursor's AI chat as your prompt |
| **GitHub Copilot Chat** | Open the skill file, copy contents, paste into Copilot Chat in VS Code and include the repo files as context |
| **ChatGPT / GPT-4** | Paste the skill file contents as the system prompt, then upload or paste the relevant source files |
| **Google Gemini** | Paste the skill file contents as instructions, attach source files for analysis |

The skill requires the AI tool to have **file reading access** to scan the codebase, and **web access** for live CVE lookups (Step 0.5). If web access is unavailable, the scan still runs using the embedded CVE database in the skill file.

---

## What Gets Scanned

All 21 DSGAI risks from the OWASP GenAI Data Security framework:

| Risk | Control Area |
|---|---|
| DSGAI01 | Training Data Privacy |
| DSGAI02 | Agentic Identity & Credential Management |
| DSGAI03 | Shadow AI & Unauthorized Data Flows |
| DSGAI04 | AI Supply Chain Security |
| DSGAI05 | RAG Data Security |
| DSGAI06 | MCP & Plugin Security |
| DSGAI07 | Data Lifecycle Management |
| DSGAI08 | Regulatory & Privacy Compliance |
| DSGAI09 | Multimodal AI Data Security |
| DSGAI10 | Synthetic Data Security |
| DSGAI11 | Multi-Tenant Data Isolation |
| DSGAI12 | Database Agent Security |
| DSGAI13 | Vector Store Security |
| DSGAI14 | AI Telemetry & Observability Security |
| DSGAI15 | Context Window Data Security |
| DSGAI16 | AI IDE Plugin & Extension Security |
| DSGAI17 | AI System Resilience & Availability |
| DSGAI18 | Model Output Data Security |
| DSGAI19 | AI Data Labeling Security |
| DSGAI20 | Inference API Security |
| DSGAI21 | Knowledge Store Security |

Each control is rated: **PASS** / **WARN** / **FAIL** / **NOT VALIDATED** / **NOT APPLICABLE**

---

## Evidence Safety — Structural vs Value-Bearing Patterns

When the skill scans your codebase and finds a match, it needs to include that evidence in the report. However, not all grep matches are equal — some patterns look for *architectural gaps* (safe to show), while others specifically look for *credential and PII-bearing lines* (must never appear in a shareable report).

The skill classifies every scan into one of two categories:

### Structural Patterns [STRUCTURAL]

The grep match shows a code *pattern* — a missing import, an absent decorator, a function call without a required argument. The matched line contains no runtime secret or personal data. It is reproduced in full in the evidence block because it proves the finding without exposing anything sensitive.

**Examples of structural evidence (safe to show):**

```
# DSGAI04 — torch.load() without weights_only=True
app/models/loader.py:22 — model = torch.load(model_path)

# DSGAI06 — MCP server binding all interfaces with no auth middleware
mcp_server/server.py:42 — uvicorn.run(app, host="0.0.0.0", port=8001)

# DSGAI20 — FastAPI endpoint missing rate-limiting decorator
app/main.py:55 — @app.post("/chat")  # no @limiter.limit decorator

# DSGAI05 — similarity_search() missing access-control filter
app/rag/retriever.py:41 — results = vectorstore.similarity_search(query, k=5)
```

None of these lines contain a password, token, or personal data value — they show code structure only.

### Value-Bearing Patterns [VALUE-BEARING ⚠️]

The grep pattern specifically targets lines where the *matched content IS the sensitive value* — a credential assignment, a secret key, a connection string, or a log statement that may contain personal data. Reproducing this line in a shareable report would leak the actual secret or PII.

**Examples of what the grep finds — and what the report must NOT show:**

| What grep matches in the source file | What the report shows instead |
|---|---|
| `DATABASE_URL = "postgresql://admin:S3cr3tP@ss@db:5432/prod"` | `app/config.py:12 — hardcoded database credential pattern detected (value redacted — review file directly)` |
| `OPENAI_API_KEY = "sk-prod-a1b2c3d4e5f6..."` | `app/config.py:8 — hardcoded LLM API key pattern detected (value redacted — review file directly)` |
| `logger.info(f"User {user.email} asked: {message}")` | `app/telemetry/logging.py:28 — prompt logging statement detected (content redacted — review file directly)` |
| `SYSTEM_PROMPT = f"... connect to {DATABASE_URL} ..."` | `app/config.py:30 — credential reference in system prompt detected (value redacted — review file directly)` |

The four DSGAI controls whose scans are classified VALUE-BEARING are:

| Control | Why value-bearing |
|---|---|
| **DSGAI02** — Agentic Credential Management | Matches lines containing actual API keys, database passwords, JWT secrets, and cloud credentials |
| **DSGAI13** — Vector Store Security | May match lines where vector store auth tokens are hardcoded as literal values |
| **DSGAI14** — AI Telemetry Security | Matches log statements whose format strings may reference PII fields or contain inline test data |
| **DSGAI15** — Context Window Security | Matches system prompt construction that may embed credential strings or sensitive config values |

All 17 remaining controls (DSGAI01, 03–12, 16–21) are **STRUCTURAL** — their matched content is always safe to show.

---

## Report Output

The generated `DSGAI-report.html` contains:

- **Executive Summary** — overall posture and key FAIL findings
- **Dashboard** — counts of PASS / WARN / FAIL / NOT VALIDATED / NOT APPLICABLE across all 21 controls
- **AI Component Inventory** — detected frameworks, vector stores, LLM providers, MCP servers
- **Summary Table** — all 21 risks at a glance with status and key evidence
- **Detailed Findings** — one card per risk with file paths, line numbers, and remediation steps
- **Recommendations** — tiered action plan (fix today / architecture backlog / maturity program)
- **CVE Advisory Panel** — live CVEs for your exact dependency versions, grouped by DSGAI risk

The report is fully self-contained (no CDN, no external fonts) and renders correctly when saved as PDF.

---

## Scan Checkpoint File (`DSGAI-scan.json`)

When the skill runs, it writes a local checkpoint file called `DSGAI-scan.json` to the repository root after each major scan phase. This is a **temporary intermediate structure** — not a deliverable, and can be deleted at any time.

### Why it exists

The scan involves three time-consuming phases: repository detection, live CVE enrichment (HTTP calls to OSV and NVD), and 21-control grep scanning. If the session times out or is interrupted before the HTML report is written, everything is lost and the scan restarts from zero. The checkpoint file prevents this — on the next run the skill skips already-completed phases and jumps to the first incomplete step. In the most common failure case (timeout during HTML generation), re-running regenerates the report in seconds.

### What it stores — and what it doesn't

The file contains only **structural scan metadata**: detected framework versions, DSGAI control findings (status, file paths, line numbers), and CVE query results. It does **not** store credential values, API keys, PII, prompt content, or any file contents beyond the specific matched patterns. The same evidence redaction rules that apply to the HTML report apply here — a VALUE-BEARING finding is stored as a description only, never the matched value.

### Lifecycle

Safe to commit (contains no secrets) or add to `.gitignore` to treat as a build artifact. Automatically overwritten on each full scan.

---

## Exporting to PDF

**Option 1 — Browser print (simplest):**
Open `DSGAI-report.html` in Chrome or Edge → `Ctrl+P` / `Cmd+P` → Save as PDF. All cards expand automatically for print.

**Option 2 — Chrome headless (scriptable):**

macOS:
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --print-to-pdf=DSGAI-report.pdf \
  --print-to-pdf-no-header "file://$(pwd)/DSGAI-report.html"
```

Linux:
```bash
google-chrome --headless=new --print-to-pdf=DSGAI-report.pdf \
  --print-to-pdf-no-header "file://$(pwd)/DSGAI-report.html"
```

Windows (PowerShell):
```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless=new --print-to-pdf=DSGAI-report.pdf `
  --print-to-pdf-no-header "file:///$(pwd)/DSGAI-report.html"
```

---

## Scope Annotation

Each DSGAI control is tagged by responsibility:

- **[BUILD]** — your team implements this in the codebase
- **[BUY]** — the LLM provider / SaaS vendor is responsible
- **[BOTH]** — shared responsibility

Controls tagged `[BUY]` that are not applicable to a BUILD-only repo are automatically marked **NOT APPLICABLE** with an explanation.

---

## Based On

**OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026)**
[https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

---

## License

This skill is based on materials licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

**Original work:** OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026) by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org/initiative/data-security/), led by [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/).

**This adaptation:** Created by [Harish Ramachandran](https://www.linkedin.com/in/harish-ramachandran-a8026443/). You are free to share and adapt this skill for any purpose, including commercial use, under the same CC BY-SA 4.0 terms.
