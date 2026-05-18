#!/usr/bin/env bash
# DSGAI02 — block hardcoded LLM, cloud, and vector-store credentials in staged files.
# Part of the OWASP GenAI Data Security Initiative.
# https://genai.owasp.org/initiative/data-security/
#
# Copy to scripts/dsgai-secret-scan.sh in your repo and chmod +x.
# See ./pre-commit-hook.md for installation options (pre-commit framework,
# plain git hook, or Husky).
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
  printf '\n\xE2\x9D\x8C DSGAI02 blocked commit: hardcoded credential detected in:\n'
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
