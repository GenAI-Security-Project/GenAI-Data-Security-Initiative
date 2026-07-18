# DSGAI Pre-commit Hook — Fast Secret Scan

A lightweight pre-commit hook that runs a fast subset of the DSGAI scan (DSGAI02 hardcoded LLM API key detection) to **block credentials from being committed**. This catches the highest-impact, highest-frequency mistake before it reaches git history.

This is **not** a substitute for the full scan — it's a fast gate that runs on every commit (sub-second), against staged changes only. Use the full skill (`/dsgai_scanner_tool`) and/or the [GitHub Action](./dsgai-scan.yml) for complete coverage.

**Two options, in order of preference:**

1. **[gitleaks](https://github.com/gitleaks/gitleaks) with the DSGAI rule pack (recommended)** — entropy-aware, battle-tested, cross-platform, no bash quirks. Use this unless you specifically can't add a binary.
2. **The zero-dependency ripgrep script** — a portable fallback (bash 3.2 / BSD safe) for environments where installing gitleaks isn't an option.

Both detect quote-optional named credentials **and** raw token prefixes (Slack `xoxb-`, GitHub `ghp_`, Google `AIza`, AWS `AKIA`, Anthropic/OpenAI project keys) regardless of variable name.

---

## Recommended — gitleaks with the DSGAI rule pack

Install gitleaks (`brew install gitleaks`, `choco install gitleaks`, or a [release binary](https://github.com/gitleaks/gitleaks/releases)) and copy [`gitleaks/dsgai.toml`](./gitleaks/dsgai.toml) into your repo.

**pre-commit framework** — add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: dsgai-gitleaks
        name: DSGAI02 — gitleaks credential scan
        entry: gitleaks protect --staged --config integrations/gitleaks/dsgai.toml --no-banner
        language: system
        pass_filenames: false
```

**Plain git hook** — `.git/hooks/pre-commit` (`chmod +x`):

```bash
#!/usr/bin/env sh
exec gitleaks protect --staged --config integrations/gitleaks/dsgai.toml --no-banner
```

Full-tree audit (not just staged): `gitleaks dir . --config integrations/gitleaks/dsgai.toml`. The pack allowlists `tests/fixtures/**`, lockfiles, minified JS, and snapshots.

---

## Why a separate hook?

The full DSGAI scan takes minutes — too slow for pre-commit. But the most common mistake (hardcoded `sk-...` or `sk-ant-...` keys, or a raw `xoxb-`/`ghp_` token, in `.env` or `config.py`) can be caught in under a second. Both options above do exactly that and nothing more.

---

## Fallback — Step 1: drop the ripgrep script into your repo

If you can't use gitleaks, use the portable ripgrep script. It ships in this repo as [`dsgai-secret-scan.sh`](./dsgai-secret-scan.sh) — copy it to `scripts/dsgai-secret-scan.sh` and `chmod +x` it. It is bash-3.2 / BSD safe (no `mapfile`, no `grep -z`, no `${var,,}`), catches **quote-optional** named credentials and raw token prefixes, and needs nothing beyond ripgrep. Key detection logic:

```bash
# Collect staged files with a NUL-delimited read loop (bash-3.2 safe — no mapfile),
# filter extensions with a case statement (no `grep -z`, which BSD grep lacks).
STAGED=()
while IFS= read -r -d '' f; do
  case "$f" in
    *.py|*.ts|*.js|*.java|*.kt|*.go|*.yaml|*.yml|*.json|*.toml|*.cfg|*.env|*.env.*)
      STAGED+=("$f") ;;
  esac
done < <(git diff --cached --name-only --diff-filter=ACM -z)
```

See the committed file for the full quote-optional NAMED pattern and the token-PREFIX
pattern (Slack/GitHub/Google/AWS/Anthropic/OpenAI). The script is self-contained — no
external dependencies beyond ripgrep.

---

## Fallback — Step 2: wire up the ripgrep script

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

The named pattern matches `<KEY>\s*[:=]\s*<16+ key-like chars>` (quote optional). Because the value must be 16+ contiguous `[A-Za-z0-9_-]`, ordinary env reads like `KEY = os.getenv("KEY")` or `KEY = os.environ["KEY"]` do **not** match (the `.`/`(` break the run). If a legitimate constant still matches, choose one of:

1. **Rename the test fixture** so it doesn't start with the real key name (e.g. `_TEST_OPENAI_KEY_PLACEHOLDER`), or for gitleaks add it to the `[allowlist]` in `dsgai.toml`
2. **Exclude the file** by adjusting the `files:` glob / gitleaks allowlist, or by gitignoring it if it contains real local-dev secrets
3. **One-time bypass** with `git commit --no-verify` and a comment explaining why

**Never** lower the `{16,}` minimum length. Real LLM API keys are always 20+ characters; relaxing the length will produce noisy false positives without catching shorter real keys (which don't exist).

---

## License

CC BY-SA 4.0 — part of the OWASP GenAI Data Security Initiative.
