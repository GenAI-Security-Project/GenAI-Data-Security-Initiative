# DSGAI Pre-commit Hook — Fast Secret Scan

A lightweight pre-commit hook that runs a fast subset of the DSGAI scan (DSGAI02 hardcoded LLM API key detection) to **block credentials from being committed**. This catches the highest-impact, highest-frequency mistake before it reaches git history.

This is **not** a substitute for the full scan — it's a fast gate that runs on every commit (sub-second), against staged changes only. Use the full skill (`/dsgai_scanner_tool`) and/or the [GitHub Action](./dsgai-scan.yml) for complete coverage.

---

## Why a separate hook?

The full DSGAI scan takes 2–5 minutes — too slow for pre-commit. But the most common mistake (hardcoded `sk-...` or `sk-ant-...` keys in `.env` or `config.py`) can be caught in under a second with a pure ripgrep call. This hook does exactly that and nothing more.

---

## Step 1 — Drop the shared script into your repo

All three installation options call the same script. Copy this into `scripts/dsgai-secret-scan.sh` (or any path you like) and `chmod +x` it:

```bash
#!/usr/bin/env bash
# DSGAI02 — block hardcoded LLM, cloud, and vector-store credentials in staged files.
# Part of the OWASP GenAI Data Security Initiative.
set -euo pipefail

if ! command -v rg >/dev/null 2>&1; then
  echo "warning: ripgrep (rg) not installed; skipping DSGAI02 pre-commit check"
  echo "         install: https://github.com/BurntSushi/ripgrep#installation"
  exit 0
fi

# Use -z / -0 so paths containing spaces or newlines are safe.
mapfile -d '' STAGED < <(
  git diff --cached --name-only --diff-filter=ACM -z |
    grep -zE '\.(py|ts|js|java|kt|go|yaml|yml|json|toml|env|cfg)$' || true
)

if [ "${#STAGED[@]}" -eq 0 ]; then
  exit 0
fi

# PCRE pattern: covers LLM, cloud, vector-store, and telemetry credentials.
PATTERN='(?i)(OPENAI_API_KEY|ANTHROPIC_API_KEY|COHERE_API_KEY|GOOGLE_API_KEY|HF_TOKEN|HUGGINGFACE_TOKEN|AWS_ACCESS_KEY_ID|AZURE_OPENAI_KEY|GCP_SERVICE_ACCOUNT_KEY|QDRANT_API_KEY|PINECONE_API_KEY|WEAVIATE_API_KEY|MILVUS_TOKEN|LANGSMITH_API_KEY|LANGFUSE_PUBLIC_KEY|LANGFUSE_SECRET_KEY)\s*[:=]\s*["'"'"']\S{16,}'

FOUND=$(rg --pcre2 --files-with-matches --no-messages "$PATTERN" "${STAGED[@]}" 2>/dev/null || true)

if [ -n "$FOUND" ]; then
  printf '\n❌ DSGAI02 blocked commit: hardcoded credential detected in:\n'
  printf '%s\n' "$FOUND" | sed 's/^/   - /'
  cat <<'MSG'

   Move the credential to a secrets manager (HashiCorp Vault, AWS Secrets
   Manager, GCP Secret Manager, Azure Key Vault) and reference it via an
   environment variable. NEVER commit the literal value.

   For the full DSGAI compliance scan, run /dsgai_scanner_tool in Claude Code.

   To bypass this check (NOT recommended), commit with --no-verify and add
   a comment explaining why.
MSG
  exit 1
fi

exit 0
```

The script is self-contained — no external dependencies beyond ripgrep.

---

## Step 2 — Wire it up

Pick one of the three integration options that matches your stack.

### Option A — pre-commit framework

If you use [pre-commit](https://pre-commit.com/), add this to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: dsgai-secret-scan
        name: DSGAI02 — block hardcoded LLM/cloud credentials
        entry: scripts/dsgai-secret-scan.sh
        language: system
        files: \.(py|ts|js|java|kt|go|yaml|yml|json|toml|env|cfg)$
        pass_filenames: false  # the script reads staged files via git
```

Install:
```bash
pip install pre-commit
pre-commit install
```

### Option B — plain git hook (no dependencies)

```bash
# from your repo root
ln -s ../../scripts/dsgai-secret-scan.sh .git/hooks/pre-commit
```

### Option C — Husky (Node/JS projects)

In `.husky/pre-commit`:

```bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

scripts/dsgai-secret-scan.sh
```

Then `chmod +x .husky/pre-commit`.

---

## What it does NOT catch (use the full scan for these)

This hook only catches **DSGAI02 hardcoded credentials**. It does not check:

- DSGAI04 — unsafe `torch.load()` without `weights_only=True`
- DSGAI06 — MCP servers over `http://` without auth
- DSGAI11 — missing tenant filters in vector queries
- DSGAI12 — raw LLM-output SQL execution
- DSGAI13 — vector store auth gaps
- DSGAI14 — verbose telemetry logging
- ... or any of the other 17 DSGAI risks

Run the full skill (`/dsgai_scanner_tool` in Claude Code) periodically — at minimum before every release, ideally on every PR via the [GitHub Action template](./dsgai-scan.yml).

---

## False positives

The pattern intentionally matches `<KEY>\s*[:=]\s*"<16+ chars>"`. If you have legitimate constants or test fixtures that match (`OPENAI_API_KEY = "fake-test-key-for-vcr-cassette"`), choose one of:

1. **Rename the test fixture** so it doesn't start with the real key name (e.g. `_TEST_OPENAI_KEY_PLACEHOLDER`)
2. **Exclude the file** by adjusting the `files:` glob in `.pre-commit-config.yaml`, or by gitignoring it if it contains real local-dev secrets
3. **One-time bypass** with `git commit --no-verify` and a comment explaining why

**Never** lower the `\S{16,}` minimum length. Real LLM API keys are always 20+ characters; relaxing the length will produce noisy false positives without catching shorter real keys (which don't exist).

---

## License

CC BY-SA 4.0 — part of the OWASP GenAI Data Security Initiative.
