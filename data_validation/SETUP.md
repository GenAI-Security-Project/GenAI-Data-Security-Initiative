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

### Python 3.8+

The scripts require Python 3.8 or higher. Most modern systems have Python pre-installed.

**Check if you have it:**

```bash
python3 --version
```

If you see `Python 3.8.x` or higher, you're good. If not:

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

> **What this does:** Reads the `requirements.txt` file and installs all the Python libraries the validation scripts need. This includes things like `jsonschema` for schema validation, `pandas` for data manipulation, and any other dependencies.

**If you get a permissions error:** Make sure your virtual environment is activated (Step 2). If you're not using a virtual environment, add `--user` to the command: `pip install --user -r requirements.txt`

---

## Step 4 — Verify the Setup

Run the built-in test suite to confirm everything is working:

```bash
python -m pytest tests/ -v
```

> **What this does:** Runs all unit tests for the validation scripts. You should see a series of green `PASSED` results. If any test fails, something went wrong in setup — check the error message and revisit the steps above.

**Expected output (approximate):**

```
tests/test_schema_validator.py::test_valid_vulnerability PASSED
tests/test_schema_validator.py::test_invalid_vulnerability PASSED
tests/test_dsgai_mapping_check.py::test_valid_mapping PASSED
tests/test_anonymization_scanner.py::test_clean_entry PASSED
tests/test_anonymization_scanner.py::test_pii_detected PASSED
...
```

---

## Step 5 — Run Your First Validation

### Validate a single file

```bash
python validators/schema_validator.py --file ../datasets/vulnerability_dataset/example_entry.json
```

### Run all checks on an entire dataset

```bash
python run_all_checks.py --dataset ../datasets/incident_dataset/
```

### Generate a coverage and bias report

```bash
python qc_tools/bias_report.py --datasets ../datasets/
```

> **What the output means:**
> - ✅ **PASS** — The check passed, no issues found
> - ⚠️ **WARN** — Something looks unusual but isn't blocking (e.g., a rarely used DSGAI mapping)
> - ❌ **FAIL** — A required check failed. The output will tell you which field, which file, and what's wrong

---

## Common Issues and Troubleshooting

### "python3: command not found"

Python might be installed as `python` instead of `python3` on your system (common on Windows). Try:

```bash
python --version
```

If that shows 3.8+, use `python` everywhere this guide says `python3`.

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
- **Anonymization failure** — Your entry may contain patterns that look like email addresses, IP addresses, or API keys. Replace them with synthetic values

---

## Understanding the Project Structure

Here's how the pieces fit together, so you know where things live:

```
GenAI-Data-Security-Initiative/
├── README.md                      ← Project overview — start here
├── CONTRIBUTING.md                ← How to contribute to any workstream
├── datasets/                      ← The actual data (what gets validated)
│   ├── vulnerability_dataset/
│   ├── exploit_dataset/
│   ├── incident_dataset/
│   └── ...
├── data_validation/               ← You are here
│   ├── README.md                  ← What the validation framework does
│   ├── SETUP.md                   ← This file
│   ├── requirements.txt
│   ├── run_all_checks.py
│   ├── schemas/                   ← Defines what valid data looks like
│   ├── validators/                ← Automated checks (run on every PR)
│   ├── qc_tools/                  ← Reports for human reviewers
│   ├── reference_data/            ← Lookup tables (DSGAI IDs, CWEs, etc.)
│   └── tests/                     ← Tests for the validators themselves
├── mappings/                      ← Framework mapping files
└── literature/                    ← Reference materials
```

---

## Next Steps

Now that your environment is set up, here's what you can do:

**If you want to contribute data:**
Read the README in the specific dataset folder you're interested in (e.g., `datasets/incident_dataset/README.md`). It describes the expected format and contribution guidelines. Create your entry, run the validators locally, and submit a pull request.

**If you want to improve the validators:**
Look at the `validators/` and `qc_tools/` directories. Each script has a docstring at the top explaining what it does. Pick an issue from the repo or propose a new check. Add unit tests in `tests/` for any new logic.

**If you want to add a new framework mapping:**
Add a reference data file in `reference_data/framework_control_ids/` and update `crossref_validator.py` to support it.

**If you have questions:**
Join `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com) ([join here](https://owasp.org/slack/invite) if you're new). No question is too basic.

---

## For Educators and Workshop Leaders

These tools are designed to be used in educational settings. If you're running a workshop, training session, or university course on AI security:

- The `tests/fixtures/` directory contains deliberately valid and invalid sample entries — useful for hands-on exercises
- `bias_report.py` generates visual coverage reports that make good discussion starters for data quality conversations
- The validation pipeline itself demonstrates applied data governance concepts from the DSGAI risk taxonomy (DSGAI05: Data Integrity & Validation Failures, DSGAI07: Data Governance, Lifecycle & Classification)
- Students can contribute real data back to the initiative — a practical way to engage with open-source security research

We welcome educational institutions to use and adapt these materials. Reach out via Slack if you'd like support setting up a classroom exercise.
