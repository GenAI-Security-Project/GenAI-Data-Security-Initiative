# Suspected false negatives (judgment pass)

Places the scanner likely **missed** something, per repo, with evidence. This is
a judgment pass to guide the human labeler's FN hunt — not a computed number.
Cross-cutting root causes first, then per-repo notes.

## Cross-cutting coverage gaps (strongest FN drivers)

1. **TypeScript/JavaScript is under-covered.** Most rules' `file_globs` include
   `*.ts`/`*.js`, but the PCRE patterns are Python-shaped (`torch.load`,
   `similarity_search`, `@app.post`, `create_sql_agent`). A TS-first GenAI app
   therefore yields almost only the language-agnostic PASS signals (jsonschema/zod
   → P06.3) and misses TS agent/RAG risk. Evidence: `langchain-nextjs-template`
   is **35 TS / 0 Py** and produced only 18 findings (12 PASS). `chat-langchain`
   is **70 TS / 41 Py**; `create-llama` **116 TS / 191 Py** — the TS halves are
   thinly covered. **FN hunt:** hardcoded keys, unauth API routes, and unvalidated
   tool calls in `*.ts`/`*.tsx`.
2. **C# is only credential-scanned.** PR-15 added `*.cs` to the DSGAI02/13
   credential rules, but DSGAI04/06/11/12/17/20 do **not** scan `*.cs`. Evidence:
   `semantic-kernel` has **2961 `.cs` files** yet its findings are dominated by the
   1244 `.py` files. **FN hunt:** supply-chain, DB-agent, resilience, and
   inference-API risks in the C# codebase are essentially unscanned.
3. **Jupyter notebooks (`.ipynb`) are unscanned** by all but a couple of controls.
   GenAI prototype code commonly lives in notebooks. Evidence: `langgraph` has
   **35** `.ipynb`, `semantic-kernel` **28**, `gpt-researcher` **2** — none went
   through the structural rules. **FN hunt:** keys and unsafe calls in notebook cells.

## Per-repo

- **langchain-nextjs-template** (35 TS, 0 Py) — near-total TS blind spot; only P06.3/P13.2/P14.4 fired. Check the API route handlers and the LangChain JS chains for missing auth / rate-limiting (DSGAI20) and any inlined keys.
- **chat-langchain** (41 Py, 70 TS) — Python side is covered; the TS frontend/backend (70 files) is thin. Check TS server routes and any client-exposed config.
- **create-llama** (191 Py, 116 TS) — a scaffolder; TS templates under-covered. Also note the count is inflated by P04.7 firing on npm lockfile `integrity` hashes (see METHODOLOGY note), which can mask real signal.
- **crewai** (1269 Py) — Python is well covered, but the finding stream is swamped by P03.1 endpoint strings in docs/tests/cassettes; a genuine FN could hide in that noise. Check tool definitions and any subprocess/DB usage in agents.
- **langgraph** (447 Py, 35 ipynb, 7 TS) — the 35 notebooks are unscanned structurally; check them for keys and unsafe execution. The 178 P06.1 `http://` FAILs are mostly `http://localhost` in tests (FP), which can bury a real insecure transport.
- **gpt-researcher** (274 Py, 72 TS, 2 ipynb) — Python covered; TS (72) and the scraper/retriever layer worth an FN check for SSRF-adjacent and unauth-endpoint issues the ruleset doesn't model.
- **openai-swarm** (62 Py) — small, well covered; low FN risk. Check the handoff/tool-execution paths for LLM-output-driven control flow (not modeled by DSGAI12, which targets SQL).
- **semantic-kernel** (1244 Py, 2961 C#, 28 ipynb) — the C# majority and notebooks are the big blind spots (see cross-cutting #2/#3). This repo is the strongest argument for finishing C# structural coverage.

## Note for the labeler
These are *hypotheses*, not confirmed FNs — confirm by opening the cited files.
A confirmed FN becomes a new rule/glob + a fixture case (per the project's
"no rule without a fixture" rule).
