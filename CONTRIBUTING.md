# Contributing to the OWASP GenAI Data Security Initiative

Thank you for your interest in contributing. This initiative is built by and for the community — every contribution, from a single incident report to a full framework mapping, strengthens the guidance that thousands of organizations rely on to secure their GenAI systems.

This guide helps you find the right starting point regardless of your background or experience level.

---

## Quick Start

1. **Join Slack:** `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com) ([join here](https://owasp.org/slack/invite) if you're new)
2. **Pick a workstream** from the table below that matches your skills and interests
3. **Fork this repo**, make your changes, and submit a pull request
4. **Run validation** before submitting — see the [Setup Guide](data_validation/SETUP.md)

---

## Where to Contribute

| Workstream | Good for | What's needed | Difficulty |
|---|---|---|---|
| **Data Collection** | Security practitioners, pen testers, incident responders | Vulnerability reports, field observations, incident data | Entry-level |
| **Mapping** | GRC professionals, compliance analysts, framework specialists | Framework control mappings for DSGAI risks | Intermediate |
| **Data Security Risks & Best Practices** | Researchers, AI engineers, security architects | Content review, new risk scenarios, mitigation strategies | Advanced |
| **Community Datasets** | Anyone with relevant data or research interest | New dataset entries, schema improvements, dataset curation | All levels |
| **Data Validation** | Python developers, data engineers, QA specialists | Validation scripts, schema definitions, test cases | Intermediate |

---

## Contributing by Role

### "I'm a security practitioner / pen tester"

Your real-world experience is the most valuable thing this initiative needs. You can contribute to the **incident dataset** (anonymized reports of GenAI data security failures you've observed), the **exploit dataset** (techniques you've used or encountered in assessments), or the **vulnerability dataset** (flaws found in LLM-based systems).

Start with: [`datasets/incident_dataset/README.md`](datasets/incident_dataset/README.md) or [`datasets/exploit_dataset/README.md`](datasets/exploit_dataset/README.md)

### "I'm a GRC / compliance professional"

The **mapping workstream** needs people who understand frameworks deeply enough to map DSGAI risks to specific controls. If you work with NIST CSF, ISO 27001, ISO 42001, SOC 2, PCI DSS, or EU AI Act compliance, you can contribute machine-readable mappings.

Start with: [`datasets/crossframework_mapping_dataset/README.md`](datasets/crossframework_mapping_dataset/README.md) and the [`/crosswalk`](crosswalk/) directory

### "I'm a developer / AI engineer"

You can contribute **agent traces** from agentic AI systems you've built or tested, **RAG test data** for poisoning and retrieval integrity testing, or **prompt injection test cases**. You can also improve the **validation pipeline** — the Python scripts that check contributed data.

Start with: [`datasets/agentdataflow_toolexchange_traces/README.md`](datasets/agentdataflow_toolexchange_traces/README.md) or [`data_validation/SETUP.md`](data_validation/SETUP.md)

### "I'm a researcher / student"

Academic contributions are welcome. You can propose new dataset categories, contribute test data from published research, improve validation tooling, or help review and refine the DSGAI risk taxonomy. The validation tools and datasets are also suitable for classroom exercises and thesis projects.

Start with: The [datasets README](datasets/README.md) to understand what exists and where the gaps are.

### "I'm new to security / OWASP / open source"

Welcome — everyone starts somewhere. Here are good first contributions:

- **Review existing dataset entries** for clarity and completeness
- **Test the validation scripts** on sample data and report issues
- **Improve documentation** — typos, unclear instructions, missing context
- **Ask questions on Slack** — this helps us identify where our docs need work

Start with: [`data_validation/SETUP.md`](data_validation/SETUP.md) to get the environment running, then explore the `tests/fixtures/` directory to see what valid data looks like.

---

## How to Submit a Contribution

### For dataset contributions (most common)

1. **Fork** this repository to your GitHub account
2. **Create a branch** for your contribution: `git checkout -b add-incident-report-001`
3. **Add your file(s)** to the appropriate dataset folder, following the schema in that folder's README
4. **Run validation locally** to catch issues before submitting:
   ```bash
   cd data_validation
   python run_all_checks.py --dataset ../datasets/incident_dataset/
   ```
5. **Commit and push** your changes
6. **Open a pull request** with a clear description of what you're contributing and which DSGAI entries it relates to

### For code contributions (validators, tooling)

1. Follow steps 1–2 above
2. **Add or modify code** in `data_validation/`
3. **Add unit tests** in `data_validation/tests/` for any new logic
4. **Run the test suite**: `python -m pytest tests/ -v`
5. Submit your pull request

### For documentation contributions

Same process as above, but no validation run needed. Documentation improvements can be submitted directly.

---

## Contribution Guidelines

**Anonymize everything.** Dataset contributions must not contain real PII, PHI, credentials, organization names, or internal system identifiers. Use synthetic equivalents. See individual dataset READMEs for specific anonymization requirements.

**Map to DSGAI.** Every dataset entry should reference at least one DSGAI ID (DSGAI01–DSGAI21). If you're unsure which entry fits, describe the issue in your PR and reviewers will help with the mapping.

**Public sources only for exploits and vulnerabilities.** Do not submit undisclosed zero-days or proprietary attack tooling. All techniques must be sourced from published research, advisories, or responsible disclosures.

**One entry per file.** For datasets, submit each entry as its own file (JSON, YAML, or Markdown depending on the dataset). This makes review, validation, and version control easier.

**Be descriptive in PRs.** Explain what you're contributing, why it matters, and which workstream it supports. A sentence or two is enough — reviewers will take it from there.

---

## Code of Conduct

This initiative operates under the [OWASP Code of Conduct](https://owasp.org/www-policy/operational/code-of-conduct). We are committed to providing a welcoming and inclusive environment for everyone.

---

## Questions?

- **Slack:** `#team-genai-data-security-initiative` on [OWASP Slack](https://owasp.slack.com)
- **Initiative Lead:** [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/) via Slack or LinkedIn
- **GitHub Issues:** Open an issue in this repository for bugs, feature requests, or dataset questions
