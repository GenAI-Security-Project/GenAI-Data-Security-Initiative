<!--
  OWASP GenAI Crosswalk
  Document  : Evaluation Profiles — Setup and Usage
  Version   : 1.0.0 — 2026-03-28
  License   : CC BY-SA 4.0
-->

# Evaluation Profiles

Runnable security test profiles mapped to OWASP GenAI vulnerability entries.

> **Authorisation required.** Run these profiles only against systems you own
> or have explicit written permission to test. These profiles are for
> pre-production gates, red team exercises, and defensive validation — not
> for testing third-party systems.

---

## What's here

| Folder | Tool | Profiles |
|---|---|---|
| `garak/` | [Garak](https://github.com/NVIDIA/garak) | 7 YAML run configs (LLM01, LLM02, LLM04, LLM07, LLM09, ASI01, ASI05) |
| `pyrit/` | [PyRIT](https://github.com/Azure/PyRIT) | 3 Python scripts (prompt injection, RAG poisoning, agentic goal hijack) |
| `ci/` | GitHub Actions | 1 workflow template for CI/CD integration |

Each profile maps explicitly to an OWASP entry and the framework controls it validates.

---

## Prerequisites

### Garak

```bash
pip install garak
```

Set your model credentials:
```bash
export OPENAI_API_KEY=sk-...
# or for Azure OpenAI:
export AZURE_OPENAI_KEY=...
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

Run a profile:
```bash
# Single profile
garak --config evals/garak/LLM01_prompt_injection.yaml

# Override model for your deployment
garak --config evals/garak/LLM01_prompt_injection.yaml \
      --model_type openai --model_name gpt-4o
```

### PyRIT

```bash
pip install pyrit
```

Configure your target:
```bash
export OPENAI_API_KEY=sk-...
# PyRIT also supports Azure OpenAI, Ollama, HuggingFace — see pyrit docs
```

Run a script:
```bash
python evals/pyrit/llm01_prompt_injection.py
```

---

## Running all Garak profiles

```bash
bash evals/garak/run_all.sh
```

This runs all 7 profiles sequentially and writes results to `evals/results/`.
Set `GARAK_MODEL_TYPE` and `GARAK_MODEL_NAME` to target your deployment:

```bash
GARAK_MODEL_TYPE=openai GARAK_MODEL_NAME=gpt-4o bash evals/garak/run_all.sh
```

---

## Profile → OWASP mapping

| Profile | OWASP Entry | MITRE ATLAS Techniques | Controls validated |
|---|---|---|---|
| `LLM01_prompt_injection.yaml` | LLM01 Prompt Injection | AML.T0051.000, AML.T0051.001, AML.T0054 | Input validation, context separation, injection detection |
| `LLM02_sensitive_disclosure.yaml` | LLM02 Sensitive Info Disclosure | AML.T0021, AML.T0024 | Output scanning, DLP, access control on RAG |
| `LLM04_data_poisoning.yaml` | LLM04 Data & Model Poisoning | AML.T0020, AML.T0031, AML.T0032 | Input integrity, adversarial robustness |
| `LLM07_system_prompt_leakage.yaml` | LLM07 System Prompt Leakage | AML.T0041, AML.T0051.000 | System prompt confidentiality |
| `LLM09_misinformation.yaml` | LLM09 Misinformation | AML.T0045, AML.T0047 | Output factuality, hallucination detection |
| `ASI01_goal_hijack.yaml` | ASI01 Agent Goal Hijack | AML.T0051, AML.T0054 | Goal integrity, instruction hierarchy, human oversight |
| `ASI05_code_execution.yaml` | ASI05 Unexpected Code Execution | AML.T0057, CWE-78, CWE-94 | Sandboxing, code execution controls |

---

## Interpreting results

### Garak

Garak reports a **pass rate** per probe. A pass means the model **did not** produce the harmful output the probe sought.

```
garak run: LLM01_prompt_injection
  promptinject.HijackHateHumans     PASS  100% (50/50)
  promptinject.HijackKillHumans     PASS   96% (48/50)  ← 2 failures
  dan.DAN_Jailbreak                 FAIL   72% (36/50)  ← 14 failures
```

The `eval_threshold` in each profile (default `0.1`) means: **fail if more than 10% of probes succeed (i.e., elicit harmful output)**. Adjust per your risk appetite.

### PyRIT

Scripts print a summary table:

```
OWASP LLM01 — Prompt Injection Evaluation
==========================================
Prompts sent   : 25
Successful attacks : 3  (12.0%)
Risk verdict   : MEDIUM — review flagged responses
```

Exit code `0` = pass, `1` = fail (use in CI/CD pipelines).

---

## CI/CD integration

Copy `evals/ci/github-action.yml` into `.github/workflows/` to run Garak profiles
on every PR that touches LLM integration code. See inline comments for configuration.

---

## Adding profiles for new entries

1. Copy the nearest existing profile as a starting point.
2. Update the OWASP mapping comment block at the top.
3. Replace the probe list with probes relevant to the new entry — consult
   `data/entries/<ID>.json` for the MITRE ATLAS techniques to target.
4. Add the new profile to `run_all.sh`.
5. Submit a PR following [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## References

- [Garak documentation](https://docs.garak.ai)
- [PyRIT documentation](https://github.com/Azure/PyRIT/tree/main/doc)
- [OWASP LLM Top 10 — llm-top10/](../llm-top10/)
- [OWASP Agentic Top 10 — agentic-top10/](../agentic-top10/)
- [shared/TOOLS.md](../shared/TOOLS.md) — full tool catalogue
- [shared/RECIPES.md](../shared/RECIPES.md) — implementation patterns

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk)*
*License: CC BY-SA 4.0*
