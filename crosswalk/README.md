<p align="center">
  <a href="https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/">
    <img src="docs/banner.svg" alt="OWASP GenAI Security Crosswalk" width="100%">
  </a>
</p>

<p align="center">
  <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg" alt="License"></a>
  <a href="https://genai.owasp.org"><img src="https://img.shields.io/badge/OWASP-GenAI%20Data%20Security-blue" alt="OWASP"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-3.1.0-green" alt="Version"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/frameworks-25-orange" alt="Frameworks"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/controls-1,514-blueviolet" alt="Controls"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/mapping%20files-67-brightgreen" alt="Mapping Files"></a>
  <a href="https://www.npmjs.com/package/genai-security-crosswalk"><img src="https://img.shields.io/npm/v/genai-security-crosswalk?color=red&label=npm" alt="npm"></a>
</p>

<p align="center">
  <strong>The most comprehensive mapping of AI security risks to compliance frameworks.</strong><br>
  25 frameworks &middot; 1,514 controls &middot; 41 entries &middot; 3,210 mappings &middot; 114 incidents &middot; ML classifier pipeline
</p>

<p align="center">
  <a href="https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/"><b>Live Web App</b></a> &middot;
  <a href="https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/score"><b>Score Coverage</b></a> &middot;
  <a href="https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/gaps"><b>Gap Analysis</b></a> &middot;
  <a href="https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/explorer"><b>Explore Entries</b></a> &middot;
  <a href="https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/incidents"><b>Incidents</b></a>
</p>

Created and led by **[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)** — [OWASP GenAI Data Security Initiative](https://genai.owasp.org) Lead.

---

## TL;DR — What is this and what do I do?

**The problem:** You're deploying AI (LLMs, agents, RAG pipelines) and need to know which security controls apply — across EU AI Act, NIST, ISO, SOC 2, FedRAMP, DORA, and 19 more frameworks. No single document maps AI risks to all of them.

**This repo solves that.** Every OWASP GenAI vulnerability (41 total) is mapped to specific controls in 25 industry frameworks. Pick your risk, find your controls.

### 3 ways to use it (pick one)

**1. Score your coverage in 60 seconds** (no install needed)
> Go to the **[web app](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/score)**, select the frameworks you implement, see your gaps instantly. Upload tool results to validate.
> Or try the **[gap analysis heatmap](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/gaps)** — red/yellow/green coverage across your compliance stack, exportable as PDF.

**2. Read the mapping file you need** (browse the repo)
> Find your framework below, click the file, read the controls. Example: deploying AI in the EU? Start with [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md).

**3. Run the tools** (for security engineers and red-teamers)
```bash
git clone https://github.com/emmanuelgjr/GenAI-Security-Crosswalk.git
cd GenAI-Security-Crosswalk
node scripts/compliance-report.js --framework "EU AI Act"   # gap assessment
node scripts/incidents-report.js --entry LLM01              # incident analysis
node scripts/compliance-report.js --format oscal            # GRC platform export
node scripts/incidents-report.js --format stix              # SIEM/SOAR export
```

### Who is this for?

| You are... | Start here |
|---|---|
| **CISO / compliance officer** | [Score your coverage](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/score) → export the gap report |
| **Security engineer** | [Explorer](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/explorer) → search by risk, see all controls |
| **Red teamer** | [LAAF guide](evals/laaf/README.md) → run S1–S6 attack stages, map results to OWASP |
| **GRC / auditor** | `compliance-report.js --format grc` → import into ServiceNow/Archer/Drata |
| **Developer** | `npm install genai-security-crosswalk` → query risks + controls programmatically |
| **Threat intel analyst** | `incidents-report.js --format stix` → ingest 80 AI incidents into Sentinel/Splunk |
| **Framework author** | [Submit your standard](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/submit) → classifier maps it automatically |

---

## Submit a Standard

Have a framework that should be in the crosswalk? The **Submit-a-Standard** pipeline automates it:

1. **[Paste your JSON](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/submit)** — structured controls with IDs and titles
2. **Classifier runs** — BGE bi-encoder + cross-encoder reranker proposes mappings to all 41 OWASP entries
3. **PR opens** — proposed mappings with confidence scores, ready for human review
4. **[Review & merge](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/review)** — accept, reject, or edit each mapping

No server required — runs entirely via GitHub Actions on the static site.

---

## Framework Registry

The crosswalk maintains a first-class registry of framework control inventories in `data/frameworks/`. Each framework has full metadata (version, URL, license, publisher) and a complete controls array.

```bash
node scripts/ingest-framework.mjs --list          # list all 25 registered frameworks
node scripts/ingest-framework.mjs fw.json          # ingest a new framework
node scripts/ingest-framework.mjs fw.json --validate  # validate only
```

The registry powers the [control-level pivot views](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/frameworks) — click any framework, then click a control to see all OWASP entries that map to it.

---

## Classifier Pipeline

The `classifier/` directory contains a research-grade retrieval pipeline for automated framework-to-OWASP mapping:

```bash
cd classifier/
pip install -r requirements.txt
python -m classifier.index_builder            # build FAISS index (1,514 controls, ~7s)
python -m classifier.classify --source LLM01 --top-k 10          # bi-encoder retrieval
python -m classifier.classify --source LLM01 --top-k 10 --rerank # + cross-encoder reranker
python -m classifier.eval_harness --rerank    # full eval with bootstrap CIs
python -m classifier.contamination_probe      # generalization probe
python -m classifier.finetune                 # domain fine-tune BGE on calibration data
python -m classifier.finetune --eval-only     # evaluate baseline without training
```

**Results (P@1 = 0.585):** The classifier correctly identifies the top control for 58.5% of queries across 25 frameworks. See [PREREGISTRATION.md](classifier/PREREGISTRATION.md) for hypotheses and [EVAL_REPORT.md](classifier/EVAL_REPORT.md) for full results with bootstrap confidence intervals.

---

## What this repository provides

Every file answers one question: **which controls from framework X address vulnerability Y?**

| | |
|---|---|
| **3** source lists | LLM Top 10 · Agentic Top 10 · DSGAI 2026 |
| **25** frameworks | Compliance · Governance · Threat modeling · Testing · OT/ICS · Identity · Secure SDLC · Financial |
| **67** mapping files | Every source list entry × every applicable framework |
| **21** implementation recipes | Production-ready Python patterns |
| **70+** open-source tools | Catalogued and organised by function |
| **25** eval profiles | Runnable Garak (13) + PyRIT (6) + LAAF (6) tests mapped to OWASP entries |
| **23** compliance reports | Per-framework gap assessments auto-generated from data layer (MD, CSV, JSON, OSCAL, GRC) |
| **50** documented incidents | Real-world + research incidents with MAESTRO layer attribution (MD, CSV, JSON, STIX 2.1) |
| **LAAF v2.0** | First agentic LPCI red-teaming framework — fully integrated with 6-stage × OWASP crosswalk |
| **25** framework registries | First-class control inventories (1,514 controls) with backlink index |
| **Classifier pipeline** | BGE bi-encoder + cross-encoder reranker — auto-maps new frameworks to OWASP entries |
| **Submit-a-Standard** | Paste framework JSON → classifier proposes mappings → PR opened for review |

All free. All open-source. Built for practitioners.
 
---
 
## Source lists
 
| List | Entries | Version | Frameworks mapped |
|---|---|---|---|
| [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) | LLM01–LLM10 | 2025 | 23 |
| [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | ASI01–ASI10 | 2026 | 23 |
| [OWASP GenAI Data Security Risks](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/) | DSGAI01–DSGAI21 | 2026 | 21 |
 
---
 
## Framework coverage matrix
 
| Framework | LLM Top 10 | Agentic Top 10 | DSGAI 2026 |
|---|:---:|:---:|:---:|
| [MITRE ATLAS](https://atlas.mitre.org) | ✅ | ✅ | ✅ |
| [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) | ✅ | ✅ | ✅ |
| [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | ✅ | ✅ | ✅ |
| [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html) | ✅ | ✅ | ✅ |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | ✅ | ✅ | ✅ |
| [ISA/IEC 62443 — OT/ICS](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | ✅ | ✅ | ✅ |
| [MAESTRO — CSA](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) | ✅ | ✅ | ✅ |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | ✅ | ✅ | ✅ |
| [CIS Controls v8.1](https://www.cisecurity.org/controls) | ✅ | ✅ | ✅ |
| [OWASP ASVS 4.0.3](https://owasp.org/www-project-application-security-verification-standard/) | ✅ | ✅ | ✅ |
| [SOC 2 Trust Services Criteria](https://www.aicpa-cima.com/resources/landing/2017-trust-services-criteria) | ✅ | ✅ | ✅ |
| [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/) | ✅ | ✅ | ✅ |
| [ENISA Multilayer Framework](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai) | ✅ | ✅ | ✅ |
| [OWASP SAMM v2.0](https://owaspsamm.org/) | ✅ | ✅ | ✅ |
| [NIST SP 800-82 Rev 3 — OT/ICS](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) | ✅ | ✅ | ✅ |
| [AIUC-1](https://www.aiuc-1.com) | ✅ | ✅ | ✅ |
| [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/) | ✅ | ✅ | ✅ |
| [NIST SP 800-218A](https://doi.org/10.6028/NIST.SP.800-218A.ipd) | ✅ | ✅ | ✅ |
| [FedRAMP](https://www.fedramp.gov/) | ✅ | ✅ | ✅ |
| [DORA (EU 2022/2554)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554) | ✅ | ✅ | ✅ |
| [CWE/CVE](https://cwe.mitre.org/) | ✅ | ✅ | ✅ |
| [OWASP AI Testing Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/) | ✅ | ✅ | — |
| [STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) | ✅ | — | — |

---

## All mapping files

### LLM Top 10 2025 — 23 framework mappings
 
| File | Framework | Standout content |
|---|---|---|
| [LLM_MITREATLAS.md](llm-top10/LLM_MITREATLAS.md) | MITRE ATLAS | Adversarial technique mapping with real-world incident references |
| [LLM_NISTAIRMF.md](llm-top10/LLM_NISTAIRMF.md) | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE per vulnerability with AI RMF profile |
| [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) | EU AI Act | Article-level obligations, fines exposure, August 2026 compliance checklist |
| [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) | ISO/IEC 27001:2022 | ISMS extension checklist, 2022 new controls mapped to LLM risks |
| [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) | ISO/IEC 42001:2023 | AIMS implementation checklist, ISO 27001 integration guidance |
| [LLM_CISControls.md](llm-top10/LLM_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3 tiered safeguards per vulnerability |
| [LLM_ASVS.md](llm-top10/LLM_ASVS.md) | OWASP ASVS 4.0.3 | L1/L2/L3 verification requirements with ASVS checklist |
| [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Zone model, SL ratings, FR/SR references, OT deployment checklist |
| [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md) | NIST SP 800-82 Rev 3 | SP 800-53 controls, US regulatory crosswalk (NERC CIP, AWIA, CMMC) |
| [LLM_NISTCSF2.md](llm-top10/LLM_NISTCSF2.md) | NIST CSF 2.0 | Six-function mapping including new GOVERN function, CSF 2.0 profile |
| [LLM_SOC2.md](llm-top10/LLM_SOC2.md) | SOC 2 Trust Services Criteria | TSC mapping for SaaS and cloud LLM deployments |
| [LLM_PCIDSS.md](llm-top10/LLM_PCIDSS.md) | PCI DSS v4.0 | CHD scope guidance, Req 3/6/7/10/11/12 per vulnerability |
| [LLM_ENISA.md](llm-top10/LLM_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3 layer mapping, EU AI Act and NIS2 alignment table |
| [LLM_SAMM.md](llm-top10/LLM_SAMM.md) | OWASP SAMM v2.0 | L1–L3 maturity roadmap per vulnerability with fillable scorecard |
| [LLM_STRIDE.md](llm-top10/LLM_STRIDE.md) | STRIDE | Six-category threat model per LLM entry with DFD integration guidance |
| [LLM_CWE_CVE.md](llm-top10/LLM_CWE_CVE.md) | CWE / CVE | CWE root cause taxonomy and confirmed CVE evidence table per entry |
| [LLM_AITG.md](llm-top10/LLM_AITG.md) | OWASP AI Testing Guide | Structured test cases per LLM entry with pass criteria and CI/CD integration guidance |
| [LLM_MAESTRO.md](llm-top10/LLM_MAESTRO.md) | MAESTRO | Seven-layer architectural threat model, layer-to-LLM mapping, 90-minute threat modeling session guide |
| [LLM_AIUC1.md](llm-top10/LLM_AIUC1.md) | AIUC-1 | Six-domain control mapping for LLM deployments — certification readiness checklist |
| [LLM_NHI.md](llm-top10/LLM_NHI.md) | OWASP NHI Top 10 | Credential and identity controls per LLM entry — NHI programme maturity table |
| [LLM_SP800218A.md](llm-top10/LLM_SP800218A.md) | NIST SP 800-218A | Secure AI SDLC practices — PW/PS/RV practice mapping per LLM entry |
| [LLM_FedRAMP.md](llm-top10/LLM_FedRAMP.md) | FedRAMP | SP 800-53 AI overlay — AC/AU/CA/CM/IA/IR/RA/SA/SC/SI/SR control families |
| [LLM_DORA.md](llm-top10/LLM_DORA.md) | DORA | EU financial sector resilience — Art. 5–45 per LLM entry |

### Agentic Top 10 2026 — 23 framework mappings
 
| File | Framework | Standout content |
|---|---|---|
| [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) | AIUC-1 | Agentic AI governance certification control mapping |
| [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) | MITRE ATLAS | Agentic technique chaining, OT amplifiers per entry |
| [Agentic_NISTAIRMF.md](agentic-top10/Agentic_NISTAIRMF.md) | NIST AI RMF 1.0 | Autonomy policy anchoring in GV-1.7, agentic AI RMF profile |
| [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) | EU AI Act | Art. 14 human oversight per entry, autonomy premium fines analysis |
| [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) | ISO/IEC 27001:2022 | ISMS extension checklist for agentic deployments, NHI as A.8.2 |
| [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) | ISO/IEC 42001:2023 | A.5.2 impact assessment per entry, EU AI Act alignment table |
| [Agentic_NISTCSF2.md](agentic-top10/Agentic_NISTCSF2.md) | NIST CSF 2.0 | GOVERN-first autonomy policy mapping, agentic CSF 2.0 profile |
| [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Agentic OT zone model, kill switch design, SL uplift table |
| [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) | MAESTRO — CSA | Seven-layer architectural threat model, layer-to-ASI mapping, session guide |
| [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) | OWASP NHI Top 10 | Full NHI-to-ASI cross-mapping, NHI programme maturity table |
| [Agentic_CISControls.md](agentic-top10/Agentic_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3 safeguards, agentic NHI treated as CIS 5 privileged access |
| [Agentic_ASVS.md](agentic-top10/Agentic_ASVS.md) | OWASP ASVS 4.0.3 | L1/L2/L3 verification checklist for agentic deployments |
| [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) | OWASP AI Testing Guide | 50 structured test cases across ASI01–ASI10 with pre-deployment gates |
| [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) | OWASP AIVSS | Dual-scenario scoring (supervised vs autonomous), +1.79 autonomy premium |
| [Agentic_ENISA.md](agentic-top10/Agentic_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3 layer mapping, EU AI Act Art. 14/15/52 alignment, NIS2 Article 23 incident assessment guidance |
| [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) | SOC 2 Trust Services Criteria | TSC mapping for agentic AI — autonomous action scope, processing integrity, supply chain criteria |
| [Agentic_PCIDSS.md](agentic-top10/Agentic_PCIDSS.md) | PCI DSS v4.0 | PCI audit guidance for agents with tool access to payment systems, Req 6/7/8/10/11/12 per entry |
| [Agentic_SAMM.md](agentic-top10/Agentic_SAMM.md) | OWASP SAMM v2.0 | L1–L3 maturity scorecard for agentic AI — pre-deployment gates and programme maturity roadmap |
| [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) | NIST SP 800-82 Rev 3 | OT agent placement, SP 800-53 controls, U.S. regulatory crosswalk (NERC CIP, AWIA, CMMC) |
| [Agentic_SP800218A.md](agentic-top10/Agentic_SP800218A.md) | NIST SP 800-218A | Secure agentic SDLC — tool access, memory integrity, multi-agent pipeline practices |
| [Agentic_FedRAMP.md](agentic-top10/Agentic_FedRAMP.md) | FedRAMP | Federal agentic AI authorization — agent identity, tool access, cascade controls |
| [Agentic_DORA.md](agentic-top10/Agentic_DORA.md) | DORA | Financial sector agentic resilience — incident reporting, third-party agent risk |

> **Also in this folder:** [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — CWE root cause taxonomy, confirmed CVEs, full CWE cross-reference index.

### DSGAI 2026 — 21 framework mappings
 
| File | Framework | Standout content |
|---|---|---|
| [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md) | ISO/IEC 27001:2022 | ISMS extension covering all 21 DSGAI entries |
| [DSGAI_NISTAIRMF.md](dsgai-2026/DSGAI_NISTAIRMF.md) | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE per DSGAI entry with data security profile |
| [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) | EU AI Act | Article-level obligations per entry, GPAI vs high-risk AI scope |
| [DSGAI_NISTCSF2.md](dsgai-2026/DSGAI_NISTCSF2.md) | NIST CSF 2.0 | Six-function mapping for all 21 entries, GenAI data security profile |
| [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) | MITRE ATLAS | Adversarial technique mapping, four complete attack path chains |
| [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) | ISA/IEC 62443 — OT/ICS | OT threat scenarios per entry, SL ratings, full OT checklist |
| [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) | MAESTRO — CSA | Layer-origin analysis for all 21 entries, L2 data operations as 52% of DSGAI threat surface |
| [DSGAI_SOC2.md](dsgai-2026/DSGAI_SOC2.md) | SOC 2 Trust Services Criteria | TSC mapping for SaaS and cloud GenAI deployments |
| [DSGAI_PCIDSS.md](dsgai-2026/DSGAI_PCIDSS.md) | PCI DSS v4.0 | CHD scope guidance, PCI audit checklist for GenAI data |
| [DSGAI_ASVS.md](dsgai-2026/DSGAI_ASVS.md) | OWASP ASVS 4.0.3 | L1/L2/L3 verification requirements for all 21 DSGAI entries, 4-phase implementation priority |
| [DSGAI_CISControls.md](dsgai-2026/DSGAI_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3 safeguards for all 21 entries, GenAI data security implementation groups |
| [DSGAI_CWE_CVE.md](dsgai-2026/DSGAI_CWE_CVE.md) | CWE / CVE | CWE root cause taxonomy and confirmed CVE evidence for all 21 DSGAI entries |
| [DSGAI_ENISA.md](dsgai-2026/DSGAI_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3 layer mapping, EU AI Act and NIS2 alignment for all 21 DSGAI entries |
| [DSGAI_ISO42001.md](dsgai-2026/DSGAI_ISO42001.md) | ISO/IEC 42001:2023 | AIMS controls per DSGAI entry, ISO 27001 integration guidance, A.7 data governance reference |
| [DSGAI_SAMM.md](dsgai-2026/DSGAI_SAMM.md) | OWASP SAMM v2.0 | L1–L3 maturity scorecard for GenAI data security — GDPR and regulatory compliance baseline |
| [DSGAI_NISTSP80082.md](dsgai-2026/DSGAI_NISTSP80082.md) | NIST SP 800-82 Rev 3 | OT data placement, SP 800-53 controls per DSGAI entry, NERC CIP/FISMA/CMMC crosswalk |
| [DSGAI_AIUC1.md](dsgai-2026/DSGAI_AIUC1.md) | AIUC-1 | Domain A (Data & Privacy) covers 50%+ of DSGAI entries — certification readiness table |
| [DSGAI_NHI.md](dsgai-2026/DSGAI_NHI.md) | OWASP NHI Top 10 | NHI as enabling condition for DSGAI risks — NHI programme maturity table for GenAI data |
| [DSGAI_SP800218A.md](dsgai-2026/DSGAI_SP800218A.md) | NIST SP 800-218A | Secure GenAI data SDLC — training data protection, data governance, provenance practices |
| [DSGAI_FedRAMP.md](dsgai-2026/DSGAI_FedRAMP.md) | FedRAMP | Federal data security controls — SC-28 data at rest, AU-2 logging, SR supply chain |
| [DSGAI_DORA.md](dsgai-2026/DSGAI_DORA.md) | DORA | Financial data resilience — Art. 8 asset inventory, Art. 12 backup, Art. 28-44 vendor risk |

### Shared resources
 
| File | Contents |
|---|---|
| [shared/RECIPES.md](shared/RECIPES.md) | 21 security implementation patterns with working Python — RAG, MCP, OT, Agentic, Data Pipeline |
| [shared/TOOLS.md](shared/TOOLS.md) | 70+ open-source security tools organised by function |
| [shared/GLOSSARY.md](shared/GLOSSARY.md) | Unified terminology across LLM, ASI, and DSGAI source lists |
| [shared/SEVERITY.md](shared/SEVERITY.md) | Severity definitions and AIVSS alignment |
| [shared/TEMPLATE.md](shared/TEMPLATE.md) | Canonical template for new mapping file contributors |
 
---
 
## Repository structure
 
```text
GenAI-Security-Crosswalk/
│
├── README.md
├── CROSSREF.md                      ← Master cross-reference: LLM ↔ ASI ↔ DSGAI
├── CONTRIBUTING.md
├── CHANGELOG.md
├── GOVERNANCE.md                    ← Maintainer roles, PR SLOs, decision process
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── package.json                     ← npm: genai-security-crosswalk (node ≥18)
├── tsconfig.json                    ← TypeScript config
│
├── src/                             ← npm package source (TypeScript)
│   ├── index.ts                     ← Typed API: getEntry, getFramework, searchEntries
│   └── index.test.ts                ← 12 smoke tests (Node.js built-in runner)
│
├── llm-top10/                       ← LLM01–LLM10 × 23 frameworks
│   ├── LLM_MITREATLAS.md
│   ├── LLM_NISTAIRMF.md
│   ├── LLM_EUAIAct.md
│   ├── LLM_ISO27001.md
│   ├── LLM_ISO42001.md
│   ├── LLM_CISControls.md
│   ├── LLM_ASVS.md
│   ├── LLM_ISA62443.md              ← OT/ICS
│   ├── LLM_NISTSP80082.md           ← OT/ICS
│   ├── LLM_NISTCSF2.md
│   ├── LLM_SOC2.md
│   ├── LLM_PCIDSS.md
│   ├── LLM_ENISA.md                 ← EU / NIS2
│   ├── LLM_SAMM.md                  ← Maturity model
│   ├── LLM_STRIDE.md                ← Threat modeling
│   ├── LLM_CWE_CVE.md               ← Root cause taxonomy + CVEs
│   ├── LLM_AITG.md                  ← AI Testing Guide
│   ├── LLM_MAESTRO.md               ← MAESTRO seven-layer threat model
│   ├── LLM_AIUC1.md                 ← AIUC-1 certification framework
│   ├── LLM_NHI.md                   ← Non-Human Identity controls
│   ├── LLM_SP800218A.md             ← Secure AI SDLC (SSDF extension)
│   ├── LLM_FedRAMP.md               ← US federal cloud AI (SP 800-53 overlay)
│   └── LLM_DORA.md                  ← EU financial sector resilience
│
├── agentic-top10/                   ← ASI01–ASI10 × 23 frameworks
│   ├── Agentic_AIUC1.md
│   ├── Agentic_MITREATLAS.md
│   ├── Agentic_NISTAIRMF.md
│   ├── Agentic_EUAIAct.md
│   ├── Agentic_ISO27001.md
│   ├── Agentic_ISO42001.md
│   ├── Agentic_NISTCSF2.md
│   ├── Agentic_ISA62443.md          ← OT/ICS
│   ├── Agentic_MAESTRO.md           ← Threat modeling — 7-layer architecture
│   ├── Agentic_OWASP_NHI.md         ← Non-Human Identity
│   ├── Agentic_CISControls.md
│   ├── Agentic_ASVS.md
│   ├── Agentic_AITG.md              ← AI Testing Guide — 50 test cases
│   ├── Agentic_AIVSS.md             ← Risk scoring — autonomy premium
│   ├── Agentic_CWE_CVE.md           ← CWE taxonomy + confirmed CVEs
│   ├── Agentic_ENISA.md             ← EU / NIS2
│   ├── Agentic_SOC2.md              ← SOC 2 TSC — agentic AI audit
│   ├── Agentic_PCIDSS.md            ← PCI DSS v4.0 — payment system agents
│   ├── Agentic_SAMM.md              ← Maturity model — pre-deployment gates
│   ├── Agentic_NISTSP80082.md       ← OT/ICS — U.S. regulatory alignment
│   ├── Agentic_SP800218A.md         ← Secure agentic SDLC
│   ├── Agentic_FedRAMP.md           ← Federal agentic AI authorization
│   └── Agentic_DORA.md              ← Financial sector agentic resilience
│
├── dsgai-2026/                      ← DSGAI01–DSGAI21 × 21 frameworks
│   ├── DSGAI_ISO27001.md
│   ├── DSGAI_NISTAIRMF.md
│   ├── DSGAI_EUAIAct.md
│   ├── DSGAI_NISTCSF2.md
│   ├── DSGAI_MITREATLAS.md
│   ├── DSGAI_ISA62443.md            ← OT/ICS
│   ├── DSGAI_MAESTRO.md             ← Threat modeling — data operations lens
│   ├── DSGAI_SOC2.md
│   ├── DSGAI_PCIDSS.md
│   ├── DSGAI_ASVS.md                ← OWASP ASVS 4.0.3
│   ├── DSGAI_CISControls.md         ← CIS Controls v8.1
│   ├── DSGAI_CWE_CVE.md             ← Root cause taxonomy + CVEs
│   ├── DSGAI_ENISA.md               ← EU / NIS2
│   ├── DSGAI_ISO42001.md            ← AI management system
│   ├── DSGAI_SAMM.md                ← Maturity model — data security programme
│   ├── DSGAI_NISTSP80082.md         ← OT/ICS — U.S. regulatory alignment
│   ├── DSGAI_AIUC1.md               ← AIUC-1 certification framework
│   ├── DSGAI_NHI.md                 ← Non-Human Identity — data pipeline credentials
│   ├── DSGAI_SP800218A.md           ← Secure GenAI data SDLC
│   ├── DSGAI_FedRAMP.md             ← Federal data security controls
│   └── DSGAI_DORA.md                ← Financial data resilience
│
├── shared/
│   ├── RECIPES.md                   ← 21 implementation patterns (Python code)
│   ├── TOOLS.md                     ← 70+ open-source tools catalogue
│   ├── GLOSSARY.md                  ← Unified terminology
│   ├── SEVERITY.md                  ← Severity definitions + AIVSS alignment
│   └── TEMPLATE.md                  ← Canonical template for new mapping files
│
├── data/
│   ├── frameworks/                  ← 25 framework registries (1,514 controls)
│   ├── entries/                     ← 41 machine-readable entry JSON files
│   ├── framework-schema.json        ← JSON Schema for framework registries
│   ├── schema.json                  ← JSON Schema (Draft 7) for entry files
│   ├── backlinks.json               ← 1,097 control-to-entry reverse index
│   ├── incidents.json               ← 114 incidents with MAESTRO layer attribution
│   ├── incidents-schema.json        ← JSON Schema for incidents
│   ├── tools-supplement.json        ← Supplemental tools merged at generation time
│   └── README.md                    ← Data layer docs, jq query examples
│
├── scripts/
│   ├── validate.js                  ← Content validator (sections, links, counts)
│   ├── generate.js                  ← Markdown-to-JSON parser → data/entries/
│   ├── compliance-report.js         ← Gap reports (MD/CSV/JSON/OSCAL/OSCAL-catalog/GRC)
│   ├── incidents-report.js          ← Incident query tool (MD/CSV/JSON/STIX 2.1)
│   ├── extract-registry.js          ← Auto-extract controls from entries → registry
│   ├── framework-diff.js            ← Diff-aware versioning (added/removed/modified)
│   ├── query.js                     ← CLI query interface (replaces jq)
│   ├── watch.js                     ← External source watcher (OWASP/arXiv/NVD/frameworks)
│   └── sbom-inventory.js            ← Content-level CycloneDX SBOM generator
│
├── classifier/                      ← ML pipeline for automated mapping
│   ├── classify.py                  ← Main classifier (bi-encoder + reranker)
│   ├── eval_harness.py              ← Evaluation pipeline (P@k, R@k, MAP, CIs)
│   ├── index_builder.py             ← FAISS index builder (1,514 controls)
│   ├── finetune.py                  ← Contrastive fine-tuning for BGE-small
│   ├── reranker.py                  ← Cross-encoder reranker
│   ├── contamination_probe.py       ← Generalization probe (CoSAI holdout)
│   ├── PREREGISTRATION.md           ← Pre-registered hypotheses
│   └── EVAL_REPORT.md               ← Evaluation results (P@1=0.585)
│
├── evals/
│   ├── README.md                    ← Setup guide and result interpretation
│   ├── garak/                       ← 7 YAML profiles (LLM01/02/04/07/09, ASI01/05)
│   ├── pyrit/                       ← 3 async Python scripts (LLM01, DSGAI04, ASI01)
│   ├── laaf/                        ← LAAF v2.0 LPCI suite (S1–S6 + crosswalk reporter)
│   └── ci/                          ← github-action.yml — drop-in CI/CD template
│
├── .github/workflows/
│   ├── validate.yml                 ← CI validation on PR
│   ├── link-check.yml               ← Broken link detection
│   ├── markdown-lint.yml            ← Markdown linting
│   ├── weekly-watch.yml             ← Weekly source monitoring + monthly regeneration
│   └── sbom.yml                     ← CycloneDX SBOM on release tags
│
└── i18n/
    ├── WORKFLOW.md                  ← Translation contributor guide
    ├── es/README.md                 ← Spanish seed (machine-assisted)
    ├── ja/README.md                 ← Japanese seed (machine-assisted)
    ├── de/README.md                 ← German seed (machine-assisted)
    ├── fr/                          ← French (accepting PRs)
    └── pt/                          ← Portuguese (accepting PRs)
```
 
---

## Compliance gap reports

Generate framework-specific gap assessments from the data layer in seconds:

```bash
node scripts/compliance-report.js                          # all 23 frameworks → reports/
node scripts/compliance-report.js --framework "EU AI Act"  # one framework
node scripts/compliance-report.js --format csv             # Excel-compatible
node scripts/compliance-report.js --format json            # machine-readable
node scripts/compliance-report.js --format oscal           # OSCAL 1.1.2 component definition
node scripts/compliance-report.js --format oscal-catalog   # OSCAL 1.1.2 full control catalog
node scripts/compliance-report.js --format grc             # ServiceNow/Archer/Drata import
node scripts/compliance-report.js --list-frameworks        # see all options
```

Each report includes: executive summary, coverage matrix (OWASP entries × controls), per-control detail with notes, and a prioritised action plan.

### Framework version diffing

When a framework releases a new version, diff the changes and propose mappings only for the delta:

```bash
node scripts/framework-diff.js --git data/frameworks/eu-ai-act.json     # diff vs last commit
node scripts/framework-diff.js --old v1.json --new v2.json              # compare two files
node scripts/framework-diff.js --old v1.json --new v2.json --apply      # update + add changelog
```

## LAAF v2.0 — LPCI red-teaming

[LAAF v2.0](https://github.com/qorvexconsulting1/laaf-V2.0) is integrated as the third evaluation framework alongside Garak and PyRIT. It covers the attack surface that surface-level injection tests miss: memory persistence, layered encoding, semantic reframing, and 6-stage lifecycle attacks.

```bash
pip install git+https://github.com/qorvexconsulting1/laaf-V2.0.git
export OPENAI_API_KEY=sk-...
bash evals/laaf/run_laaf.sh           # S1–S6 full suite
laaf scan --target mock --dry-run     # No API key needed
```

| LAAF Stage | OWASP | Threshold |
|---|---|---|
| S1 Reconnaissance | LLM07, LLM01 | 0% |
| S2 Logic-Layer Injection | LLM01, ASI01, DSGAI04 | 5% |
| S3 Trigger Execution | ASI01, ASI06, LLM06 | 0% |
| S4 Persistence | ASI06, LLM06, DSGAI04 | 0% |
| S5 Evasion | LLM01, LLM02 | 10% |
| S6 Trace Tampering | DSGAI01, LLM07 | 0% |

See `evals/laaf/README.md` for the full LPCI attack vector → OWASP → MAESTRO crosswalk.

---

## Incident tracker

80 real-world, research-demonstrated, and red-team incidents, each mapped to OWASP entries and MAESTRO architectural layers:

```bash
node scripts/incidents-report.js                      # all incidents → reports/incidents.md
node scripts/incidents-report.js --entry LLM01        # incidents for a specific entry
node scripts/incidents-report.js --layer L3           # incidents implicating Agent Frameworks
node scripts/incidents-report.js --category real-world
node scripts/incidents-report.js --format csv         # Excel export
node scripts/incidents-report.js --format stix        # STIX 2.1 bundle for Sentinel/Splunk
```

MAESTRO layer roles tracked per incident: **Origin** (where attack starts) · **Propagation** (how it spreads) · **Impact** (where harm manifests) · **Blind-spot** (where detection failed).

### Web app — interactive dashboard

**https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/**

No install required. Works on desktop and mobile.

| Page | What it does |
|------|-------------|
| [**Explorer**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/explorer) | Search and filter all 41 entries. Click any entry to see controls across all 25 frameworks. |
| [**Frameworks**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/frameworks) | Interactive 41×25 coverage matrix. Click any cell to see the specific controls mapped. Drill into any control. |
| [**Crosswalk**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/crosswalk) | Entry-to-control mapping explorer. Filter by severity, tier, scope. |
| [**Incidents**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/incidents) | Browse 80 AI security incidents. Filter by severity, year, MAESTRO layer. Full attribution details. |
| [**Score**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/score) | Select your frameworks, see coverage score. Upload Garak/PyRIT/LAAF results to validate. Export badge. |
| [**Gap Analysis**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/gaps) | Select frameworks you implement, see red/yellow/green heatmap of OWASP risk coverage. Export PDF or CSV. |
| [**Submit**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/submit) | Paste any framework's controls JSON and the ML classifier proposes mappings to all 41 OWASP entries. |
| [**Tools**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/tools) | 70+ open-source security tools, searchable and organised by function. |
| [**Recipes**](https://emmanuelgjr.github.io/GenAI-Security-Crosswalk/#/recipes) | 21 production-ready security patterns with working Python. |

**Evidence-based scoring** — three validation tiers:
- **Self-Assessed** — checkbox only (unvalidated)
- **Partially Validated** — some tool outputs uploaded
- **Tool-Validated** — 20+ entries backed by Garak/PyRIT/LAAF/compliance report evidence

### Enterprise export formats

```bash
# OSCAL 1.1.2 Component Definition — ingest into ServiceNow, Archer, XACTA
node scripts/compliance-report.js --framework "EU AI Act" --format oscal

# OSCAL 1.1.2 Catalog — full control inventory with OWASP coverage annotations
node scripts/compliance-report.js --framework "NIST AI RMF 1.0" --format oscal-catalog

# GRC platform import — ServiceNow, Archer, Drata-ready JSON
node scripts/compliance-report.js --framework "SOC 2" --format grc

# STIX 2.1 bundle — ingest into Splunk ES, Microsoft Sentinel, TAXII feeds
node scripts/incidents-report.js --format stix
```

### Automated source monitoring

```bash
node scripts/watch.js              # check OWASP repos, arXiv, NVD, framework pages
node scripts/watch.js --dry-run    # preview findings without opening issues
node scripts/watch.js --watcher arxiv  # run single watcher
```

Weekly GitHub Actions cron (`.github/workflows/weekly-watch.yml`) runs all 4 watchers and opens labeled issues automatically.

### npm package

```bash
npm install genai-security-crosswalk
```

```typescript
import { getEntry, getFramework, searchEntries, incidents } from 'genai-security-crosswalk';

const llm01 = getEntry('LLM01');        // typed Entry object
const euai  = getFramework('EU AI Act'); // { framework, entries, controls }
const hits  = searchEntries('injection');  // Entry[]
const incs  = incidents;                   // 50 Incident[] with MAESTRO layers
```

Full TypeScript types included for all data structures.

---

## Start here — by role

Find your entry point in under 60 seconds.

**I need to comply with EU AI Act before August 2026**
→ Start: [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) — article-level obligations, fines exposure, compliance checklist
→ Then: [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) if you deploy autonomous agents (Art. 14 human oversight)
→ Then: [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) for GPAI model scope and data governance obligations

**I am deploying an autonomous AI agent and need to know what can go wrong**
→ Start: [CROSSREF.md](CROSSREF.md) — master cross-reference across all 41 vulnerability IDs
→ Then: [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — architectural threat model (where does each risk originate?)
→ Then: [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — score each risk; autonomy adds +1.79 avg severity
→ Then: [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — identity and credential controls

**I am a SOC 2 auditor or GRC professional preparing a GenAI controls assessment**
→ Start: [LLM_SOC2.md](llm-top10/LLM_SOC2.md) — TSC mapping for SaaS/cloud LLM deployments
→ Then: [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) — autonomous action scope, processing integrity criteria
→ Then: [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — fillable SAMM maturity scorecard to evidence programme completeness

**I am an AppSec engineer or red-teamer building a test plan**
→ Start: [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50 structured test cases with pass criteria and CI/CD gates
→ Then: [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — attacker TTP mapping with four complete attack chains
→ Then: [shared/RECIPES.md](shared/RECIPES.md) — 21 working Python patterns to implement the controls you test against

**I am a US federal contractor needing FedRAMP authorization for AI services**
→ Start: [LLM_FedRAMP.md](llm-top10/LLM_FedRAMP.md) — SP 800-53 AI overlay controls (AC/AU/CA/CM/IA/IR/RA/SA/SC/SI/SR)
→ Then: [Agentic_FedRAMP.md](agentic-top10/Agentic_FedRAMP.md) for agentic AI agent identity and cascade controls
→ Then: [DSGAI_FedRAMP.md](dsgai-2026/DSGAI_FedRAMP.md) for data security controls (SC-28, AU-2, SR)

**I work in EU financial services and need DORA compliance for AI systems**
→ Start: [LLM_DORA.md](llm-top10/LLM_DORA.md) — Art. 5–45 per LLM risk, incident reporting requirements
→ Then: [Agentic_DORA.md](agentic-top10/Agentic_DORA.md) for third-party agent risk (Art. 28–44)
→ Then: [DSGAI_DORA.md](dsgai-2026/DSGAI_DORA.md) for data resilience and backup (Art. 8, Art. 12)

**I am securing AI deployed in OT/ICS environments (energy, utilities, manufacturing)**
→ Start: [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) — OT zone model, SP 800-53 controls, NERC CIP/AWIA/CMMC crosswalk
→ Then: [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) — SL ratings, zone model, kill switch design
→ Then: [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — RAG corpus poisoning in OT (safety procedure manipulation scenario)

---

## Quick navigation
 
**EU AI Act compliance by August 2026**
→ [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) · [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) · [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md)
 
**European organisation subject to NIS2**
→ [LLM_ENISA.md](llm-top10/LLM_ENISA.md) — ENISA framework with NIS2 Article 23 incident assessment guidance
 
**AI in OT/ICS environments**
→ [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) · [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) · [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) · [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md)
 
**Deploying autonomous agents**
→ [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — identity governance
→ [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) — agentic governance certification
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — risk scoring with autonomy premium
 
**Threat modeling an agentic AI system before selecting controls**
→ [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — MAESTRO seven-layer threat enumeration with session guide
→ [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) — MAESTRO data operations lens for all 21 DSGAI entries
 
**ISO 27001 ISMS extension for GenAI**
→ [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) · [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) · [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md)
 
**ISO 42001 AIMS for AI governance**
→ [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) · [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) — includes EU AI Act compliance evidence table
 
**Security programme maturity**
→ [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — SAMM L1–L3 roadmap with fillable scorecard
 
**Security test plan for agentic AI**
→ [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50 structured test cases, pre-deployment gates, OT addendum
 
**Risk register scoring for agentic AI**
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — supervised vs autonomous dual-scenario scoring, avg +1.79 autonomy premium
 
**Attacker perspective on GenAI risks**
→ [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — ATLAS technique mapping, four attack path chains
→ [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) — agentic technique chaining
 
**CWE root causes and confirmed CVEs**
→ [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — root cause taxonomy, CVE evidence, cross-reference index
 
**Implementation code, not framework theory**
→ [shared/RECIPES.md](shared/RECIPES.md) — 21 production patterns with working Python
 
**US federal / FedRAMP authorization for AI services**
→ [LLM_FedRAMP.md](llm-top10/LLM_FedRAMP.md) · [Agentic_FedRAMP.md](agentic-top10/Agentic_FedRAMP.md) · [DSGAI_FedRAMP.md](dsgai-2026/DSGAI_FedRAMP.md)

**EU financial sector (DORA compliance)**
→ [LLM_DORA.md](llm-top10/LLM_DORA.md) · [Agentic_DORA.md](agentic-top10/Agentic_DORA.md) · [DSGAI_DORA.md](dsgai-2026/DSGAI_DORA.md)

**Secure AI development lifecycle (SSDF extension)**
→ [LLM_SP800218A.md](llm-top10/LLM_SP800218A.md) · [Agentic_SP800218A.md](agentic-top10/Agentic_SP800218A.md) · [DSGAI_SP800218A.md](dsgai-2026/DSGAI_SP800218A.md)

**All risks across all three source lists**
→ [CROSSREF.md](CROSSREF.md) — master cross-reference
 
---
 
## Standout coverage
 
### Complete OT/ICS trilogy
 
The only publicly available mapping of all three OWASP GenAI source lists to ISA/IEC 62443 and NIST SP 800-82 Rev 3. Includes zone model placement, security level ratings, Fundamental Requirement and Security Requirement references, OT-specific threat scenarios, and pre-deployment checklists for each source list.
 
The RAG corpus poisoning scenario in [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — a safety procedure manipulation attack that modifies maintenance intervals without any OT network access — exists nowhere else in public documentation.
 
### MAESTRO seven-layer threat modeling
 
[Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) and [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) are the only public mappings of OWASP GenAI risks to the MAESTRO framework from the Cloud Security Alliance. Unlike every other file in this repo — which maps risks to controls — MAESTRO maps each risk to the **architectural layer where it originates**, telling you which team owns the problem and where in the system the fix must be deployed.
 
Key finding from the DSGAI mapping: **L2 Data Operations is the originating layer for 52% of all DSGAI entries**. An organisation that does not treat RAG corpora, embedding stores, training pipelines, and memory systems as security-critical infrastructure is under-defended against the majority of the GenAI data security threat landscape.
 
### Agentic autonomy premium
 
[Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) quantifies what removing human oversight costs in risk: average **+1.79 AIVSS severity points** across all 10 agentic entries. Removing human oversight converts 7 of 10 entries from High to Critical — the quantitative case for mandatory human oversight under EU AI Act Article 14.
 
### Complete agentic identity coverage
 
[Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) maps every NHI Top 10 entry to every ASI entry — the only public document translating agentic security risks into the NHI controls that IAM teams already operate.
 
### SAMM maturity scorecard
 
[LLM_SAMM.md](llm-top10/LLM_SAMM.md) includes a fillable maturity scorecard with minimum viable levels per SAMM practice for any LLM production deployment — the artefact security programme leads use to brief engineering leadership on where the programme stands and what to improve next.
 
### Production implementation recipes
 
[shared/RECIPES.md](shared/RECIPES.md) contains 21 production-ready security patterns with working Python across 5 deployment architectures: RAG pipeline security (access control, ingestion integrity, circuit breakers), MCP server hardening (input validation, credential scoping), OT/ICS agent safety (kill switches, behavioural baselines, cascade containment), agentic AI security (memory sanitization, inter-agent message validation, credential rotation, output guardrails), and data pipeline security (provenance tracking, PII redaction, differential privacy, retention enforcement).
 
---
 
## Contributing
 
Contributions are welcome — new framework mappings, updated controls, new implementation recipes, translations, and additional tool entries.
 
See [CONTRIBUTING.md](CONTRIBUTING.md) for the file template, PR process, and contribution guidelines. All contributors are listed in the CHANGELOG.
 
---
 
## License
 
[Creative Commons Attribution-ShareAlike 4.0 International](LICENSE)
 
Free to share and adapt for any purpose, including commercial use, with appropriate credit and distribution under the same license.
 
---
 
## Acknowledgements
 
Created and led by **[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)**, who leads the [OWASP GenAI Data Security Initiative](https://genai.owasp.org).

Built on the work of the OWASP LLM Top 10, OWASP Agentic Top 10, OWASP GenAI Data Security, OWASP NHI Top 10, and OWASP SAMM project teams.
 
---
 
*[genai.owasp.org](https://genai.owasp.org) · [CC BY-SA 4.0](LICENSE)*
