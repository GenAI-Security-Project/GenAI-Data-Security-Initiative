# Vulnerable fixture app (DSGAI scanner test corpus)

**This app is intentionally vulnerable. Do not deploy it. Do not copy its
patterns into real code.** It exists solely as the DSGAI scanner's test corpus,
demo, and screenshot source.

**Every credential-looking string here is a fake, canonical test value**
(e.g. `sk-proj-FAKE0000...`, `xoxb-FAKE...`). There are no real secrets. The
fixture paths are allow-listed in the repo's secret-scanning config so the
scanner does not fail its own repository.

## What each file demonstrates

| File | Control | Expected |
|---|---|---|
| `.env` | DSGAI02 | FAIL — unquoted hardcoded key (v0.2 false negative; fixed PR-11) |
| `config.py` | DSGAI02 | FAIL — quoted hardcoded key (caught by v0.2) |
| `webhook.py` | DSGAI12 | **no finding** — innocent webhook (v0.2 false positive; fixed PR-11) |
| `sql_agent.py` | DSGAI12 | FAIL — genuine LLM-generated SQL execution |
| `loader.py` | DSGAI04 | FAIL — `torch.load` without `weights_only=True` |
| `mcp_config.json` | DSGAI06 | FAIL — insecure MCP transport (http) |
| `server.py` | DSGAI06 | uvicorn bind-all, no auth |
| `retriever.py` | DSGAI11 | FAIL (unscoped) + PASS (tenant-filtered) |
| `telemetry.py` | DSGAI14 | WARN — prompt/response content capture |
| `system_prompt.py` | DSGAI15 | FAIL — secret embedded in system prompt |
| `requirements.txt` | DSGAI04 | WARN — unpinned deps; old CVE-bearing deps |
| `js-service/` | DSGAI02/20 | JS fake Slack token + unauth `/chat` (coverage lands PR-15) |
| `docs/NOTES.md` | — | adversarial prompt-injection; must have zero effect |
| `good_config.py` | DSGAI02 | PASS — Vault retrieval, no hardcoded secret |
| `rate_limited_api.py` | DSGAI20 | PASS — authenticated + rate-limited endpoint |

The authoritative, line-pinned expectations live in
[`../../expected-findings.yaml`](../../expected-findings.yaml).
