# Setup Guide

A step-by-step guide to getting the data validation tools running on your machine. No assumptions about prior experience — if you can open a terminal, you can follow this.

---

## What You'll Be Setting Up

The data validation pipeline is a set of Python scripts that check contributed data for correctness, completeness, and safety before it gets merged into the initiative's datasets. By the end of this guide, you'll be able to:

1. Run validation checks on any dataset file
2. Catch problems before submitting a pull request
3. Generate quality reports on existing datasets
4. Modify or extend the validators for your own needs

---

## Prerequisites

### Python 3.10+

The scripts require Python 3.10 or higher. Most modern systems have Python pre-installed.

**Check if you have it:**

```bash
python3 --version
```

If you see `Python 3.10.x` or higher, you're good. If not:

| Platform | How to install |
|---|---|
| **macOS** | `brew install python3` (install [Homebrew](https://brew.sh) first if needed) |
| **Ubuntu / Debian** | `sudo apt update && sudo apt install python3 python3-pip python3-venv` |
| **Windows** | Download from [python.org](https://www.python.org/downloads/). During install, **check "Add Python to PATH"** — this is the most common setup mistake. |

### Git

You'll need Git to clone the repository and submit contributions.

**Check if you have it:**

```bash
git --version
```

If not installed: [git-scm.com/downloads](https://git-scm.com/downloads)

### A Text Editor or IDE

Any editor works. If you don't have a preference, [VS Code](https://code.visualstudio.com/) is free and widely used in the OWASP community. It has good Python and JSON support out of the box.

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative.git
cd GenAI-Data-Security-Initiative
```

> **What this does:** Downloads the full repository to your machine and moves you into the project folder. All paths from here are relative to this root directory.

---

## Step 2 — Create a Virtual Environment

A virtual environment keeps this project's Python dependencies isolated from everything else on your system. This is optional but strongly recommended — it prevents version conflicts with other Python projects.

```bash
cd data_validation
python3 -m venv venv
```

> **What this does:** Creates a folder called `venv/` inside `data_validation/` that holds a self-contained Python installation. This folder is gitignored — it won't be included in your commits.

**Activate the virtual environment:**

| Platform | Command |
|---|---|
| **macOS / Linux** | `source venv/bin/activate` |
| **Windows (Command Prompt)** | `venv\Scripts\activate` |
| **Windows (PowerShell)** | `venv\Scripts\Activate.ps1` |

You'll know it's active when your terminal prompt changes to show `(venv)` at the beginning.

> **To deactivate later:** Just type `deactivate` and press Enter.

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> **What this does:** Reads the `requirements.txt` file and installs all the Python libraries the validation scripts need. That is `jsonschema` (schema validation) and `pytest` (the tests), plus `pyyaml`, which only the reference-data refresh script uses.

**If you get a permissions error:** Make sure your virtual environment is activated (Step 2). If you're not using a virtual environment, add `--user` to the command: `pip install --user -r requirements.txt`

---

## Step 4 — Verify the Setup

Run the built-in test suite to confirm everything is working:

```bash
python -m pytest tests/ -v
```

> **What this does:** Runs the unit tests for the validation scripts. You should see a series of green `PASSED` results. If any test fails, something went wrong in setup — check the error message and revisit the steps above.

**Expected output (abridged):**

```
tests/test_anonymization_scanner.py::test_clean_entry PASSED
tests/test_anonymization_scanner.py::test_pii_detected PASSED
tests/test_crossref_validator.py::test_unknown_cwe_and_atlas PASSED
tests/test_dsgai_mapping_check.py::test_invalid_dsgai_id PASSED
tests/test_schema_validator.py::test_valid_vulnerability PASSED
...
```

---

## Step 5 — Run Your First Validation

### Check a single file

```bash
python validators/schema_validator.py --file ../datasets/rag_dataset/entries/RAG-0001.json
python validators/dsgai_mapping_check.py --file ../datasets/rag_dataset/entries/RAG-0001.json
```

Each script in `validators/` takes `--file` (one or more files) or `--dataset` (a folder), and checks every dataset when given neither.

### Run all checks

```bash
python run_all_checks.py                                      # every dataset
python run_all_checks.py --dataset ../datasets/exploit_dataset/  # one dataset
```

This runs each dataset's own `validate.py`, then the shared checks in `validators/` on every data file. It is the same command CI runs on your pull request. Add `--verbose` to see every warning.

### Generate a coverage and bias report

```bash
python qc_tools/bias_report.py --output coverage.md
```

> **What the output means:**
> - ✅ **PASS** — No issues found
> - ⚠️ **WARN** — Something a reviewer should look at, but not blocking (e.g., text that looks like an email address, or two very similar entries)
> - ❌ **FAIL** — A check failed. The lines under it name the file, the field, and what's wrong
> - **ERROR** — A dataset validator could not run (a missing dependency, or it timed out)
> - **NO VALIDATOR** — The dataset has no `validate.py` of its own yet; the shared checks still cover it

---

## Common Issues and Troubleshooting

### "python3: command not found"

Python might be installed as `python` instead of `python3` on your system (common on Windows). Try:

```bash
python --version
```

If that shows 3.10+, use `python` everywhere this guide says `python3`.

### "No module named 'jsonschema'" (or any other module)

Your virtual environment probably isn't activated, or dependencies weren't installed. Reactivate and reinstall:

```bash
source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt
```

### "Permission denied" when cloning

You may need to set up SSH keys for GitHub. Follow [GitHub's SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). Alternatively, use the HTTPS URL instead:

```bash
git clone https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative.git
```

### Tests pass but validation fails on my contributed file

This is expected — it means your data has an issue, not the tooling. Read the error output carefully. Common reasons:

- **Missing required field** — Check the dataset's README for the expected schema
- **Invalid DSGAI mapping** — Make sure the DSGAI ID exists (DSGAI01 through DSGAI21)
- **Unknown identifier** — A CWE or MITRE ATLAS ID that doesn't exist, or a malformed CVE ID such as `CVE-24-1234`

Anonymization findings are warnings, not failures, but reviewers will ask about them. If your entry contains something that looks like an email address, IP address or API key, use an obviously fake value instead: an `example.com` address, a documentation IP such as `192.0.2.10`, or a placeholder such as `<API_KEY>`.

---

## Understanding the Project Structure

Here's how the pieces fit together, so you know where things live:

```
GenAI-Data-Security-Initiative/
├── README.md                      ← Project overview — start here
├── CONTRIBUTING.md                ← How to contribute to any workstream
├── datasets/                      ← The actual data (what gets validated)
│   ├── _shared/dsgai_taxonomy.json ← The DSGAI IDs every check uses
│   ├── vulnerability_dataset/      ← schema.json, validate.py, entries/
│   ├── exploit_dataset/
│   └── ...
├── data_validation/               ← You are here
│   ├── README.md                  ← What the validation framework does
│   ├── SETUP.md                   ← This file
│   ├── requirements.txt
│   ├── run_all_checks.py
│   ├── schemas/                   ← Schemas for datasets without their own schema.json
│   ├── validators/                ← Shared automated checks (run on every PR)
│   ├── qc_tools/                  ← Reports for human reviewers
│   ├── reference_data/            ← Lookup tables (DSGAI, MITRE ATLAS, CWE)
│   └── tests/                     ← Tests for the validators themselves
└── literature/                    ← Reference materials
```

---

## Next Steps

Now that your environment is set up, here's what you can do:

**If you want to contribute data:**
Read the README in the specific dataset folder you're interested in (e.g., `datasets/incident_dataset/README.md`). It describes the expected format and contribution guidelines. Create your entry, run the validators locally, and submit a pull request.

**If you want to improve the validators:**
Look at the `validators/` and `qc_tools/` directories. Each script has a docstring at the top explaining what it checks and which findings are errors versus warnings. A useful first contribution is a `validate.py` for a promptinj sub-collection that has none yet (`tr_altaysec_turkish_llm_injection`). Add unit tests in `tests/` for any new logic.

**If you want to check a new kind of identifier:**
Add the lookup table to `reference_data/`, record where it came from in `reference_data/SOURCES.md`, and check against it in `crossref_validator.py`.

**If you have questions:**
Join `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com) ([join here](https://owasp.org/slack/invite) if you're new). No question is too basic.

---

## For Educators and Workshop Leaders

These tools are designed to be used in educational settings. If you're running a workshop, training session, or university course on AI security:

- The `tests/fixtures/` directory contains deliberately valid and invalid sample entries — useful for hands-on exercises
- `bias_report.py` generates a coverage report (which DSGAI risks the data covers, and where it is thin) that makes a good discussion starter for data quality conversations
- The validation pipeline itself demonstrates applied data governance concepts from the DSGAI risk taxonomy (DSGAI05: Data Integrity & Validation Failures, DSGAI07: Data Governance, Lifecycle & Classification)
- Students can contribute real data back to the initiative — a practical way to engage with open-source security research

We welcome educational institutions to use and adapt these materials. Reach out via Slack if you'd like support setting up a classroom exercise.
