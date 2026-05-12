#!/usr/bin/env bash
# OWASP GenAI Crosswalk — Run all Garak evaluation profiles
# ─────────────────────────────────────────────────────────────
# Usage:
#   bash evals/garak/run_all.sh
#   GARAK_MODEL_TYPE=openai GARAK_MODEL_NAME=gpt-4o bash evals/garak/run_all.sh
#
# Environment variables:
#   GARAK_MODEL_TYPE  — model type (default: openai)
#   GARAK_MODEL_NAME  — model name (default: gpt-4o-mini)
#   OPENAI_API_KEY    — required for openai model type
#
# Results are written to evals/results/<timestamp>/
# Exit code: 0 if all profiles pass, 1 if any fail

set -euo pipefail

MODEL_TYPE="${GARAK_MODEL_TYPE:-openai}"
MODEL_NAME="${GARAK_MODEL_NAME:-gpt-4o-mini}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
RESULTS_DIR="$REPO_ROOT/evals/results/$(date +%Y%m%d_%H%M%S)"

mkdir -p "$RESULTS_DIR"

PROFILES=(
  "$SCRIPT_DIR/LLM01_prompt_injection.yaml"
  "$SCRIPT_DIR/LLM02_sensitive_disclosure.yaml"
  "$SCRIPT_DIR/LLM04_data_poisoning.yaml"
  "$SCRIPT_DIR/LLM07_system_prompt_leakage.yaml"
  "$SCRIPT_DIR/LLM09_misinformation.yaml"
  "$SCRIPT_DIR/ASI01_goal_hijack.yaml"
  "$SCRIPT_DIR/ASI05_code_execution.yaml"
)

PASS=0
FAIL=0
FAILED_PROFILES=()

echo ""
echo "OWASP GenAI Crosswalk — Garak evaluation suite"
echo "Model: $MODEL_TYPE / $MODEL_NAME"
echo "Results: $RESULTS_DIR"
echo "────────────────────────────────────────────────────"

for profile in "${PROFILES[@]}"; do
  name=$(basename "$profile" .yaml)
  echo ""
  echo "▶  Running: $name"

  if garak \
      --config "$profile" \
      --model_type "$MODEL_TYPE" \
      --model_name "$MODEL_NAME" \
      --report_prefix "$RESULTS_DIR/$name" \
      2>&1 | tee "$RESULTS_DIR/${name}.log"; then
    echo "✓  PASS: $name"
    ((PASS++)) || true
  else
    echo "✗  FAIL: $name"
    ((FAIL++)) || true
    FAILED_PROFILES+=("$name")
  fi
done

echo ""
echo "────────────────────────────────────────────────────"
echo "Results: $PASS passed, $FAIL failed"

if [ "${#FAILED_PROFILES[@]}" -gt 0 ]; then
  echo ""
  echo "Failed profiles:"
  for f in "${FAILED_PROFILES[@]}"; do
    echo "  ✗ $f"
  done
  echo ""
  echo "See $RESULTS_DIR for full logs."
  exit 1
fi

echo ""
echo "All profiles passed. See $RESULTS_DIR for full reports."
exit 0
