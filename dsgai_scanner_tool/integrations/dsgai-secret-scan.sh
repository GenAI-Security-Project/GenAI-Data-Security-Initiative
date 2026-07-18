#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# DSGAI02 — block hardcoded LLM, cloud, and vector-store credentials in staged files.
# Part of the OWASP GenAI Data Security Initiative.
# https://genai.owasp.org/initiative/data-security/
#
# This is the zero-dependency FALLBACK. The recommended pre-commit path is the
# gitleaks rule pack (integrations/gitleaks/dsgai.toml) — entropy-aware,
# battle-tested, cross-platform. See ./pre-commit-hook.md.
#
# Portable to bash 3.2 (macOS default) and BSD userland: no `mapfile`/`readarray`,
# no `grep -z`, no `${var,,}`. Copy to scripts/dsgai-secret-scan.sh and chmod +x.
set -euo pipefail

if ! command -v rg >/dev/null 2>&1; then
  echo "warning: ripgrep (rg) not installed; skipping DSGAI02 pre-commit check"
  echo "         install: https://github.com/BurntSushi/ripgrep#installation"
  exit 0
fi

# Collect staged files with a NUL-delimited read loop (bash-3.2 safe — no
# mapfile). Filter extensions with a case statement (no `grep -z`, which BSD
# grep lacks). Paths with spaces or newlines are handled correctly.
STAGED=()
while IFS= read -r -d '' f; do
  case "$f" in
    *.py|*.ts|*.js|*.java|*.kt|*.go|*.yaml|*.yml|*.json|*.toml|*.cfg|*.env|*.env.*)
      STAGED+=("$f") ;;
  esac
done < <(git diff --cached --name-only --diff-filter=ACM -z)

if [ "${#STAGED[@]}" -eq 0 ]; then
  exit 0
fi

# Two detections, combined:
#  1) Named credential assignment, QUOTE-OPTIONAL (fixes the unquoted-.env miss).
#     The value is 16+ contiguous key-like chars, so `KEY = os.getenv(...)` and
#     `KEY = os.environ["..."]` do NOT match (the '.'/'(' break the run).
#  2) Raw token literals by prefix, regardless of variable name (Slack, GitHub,
#     Google, AWS, Anthropic/OpenAI project keys) — catches keys assigned to
#     arbitrary names.
NAMED='(?i)(OPENAI_API_KEY|ANTHROPIC_API_KEY|COHERE_API_KEY|GOOGLE_API_KEY|HF_TOKEN|HUGGINGFACE_TOKEN|AWS_ACCESS_KEY_ID|AZURE_OPENAI_KEY|GCP_SERVICE_ACCOUNT_KEY|QDRANT_API_KEY|PINECONE_API_KEY|WEAVIATE_API_KEY|MILVUS_TOKEN|LANGSMITH_API_KEY|LANGFUSE_PUBLIC_KEY|LANGFUSE_SECRET_KEY)\s*[:=]\s*["'"'"']?[A-Za-z0-9_\-]{16,}'
PREFIX='(sk-ant-[A-Za-z0-9_\-]{16,}|sk-proj-[A-Za-z0-9_\-]{16,}|ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{22,}|xox[baprs]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_\-]{35}|AKIA[0-9A-Z]{16})'
PATTERN="($NAMED|$PREFIX)"

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
