<!--
  Translation: German
  Translator: Machine-assisted draft — needs native-speaker review
  Translation-method: machine-assisted
  Source-SHA: HEAD
  Last-synced: 2026-03-28
-->

# OWASP GenAI Crosswalk

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![OWASP Lab](https://img.shields.io/badge/OWASP-GenAI%20Data%20Security-blue)](https://genai.owasp.org)
[![Version](https://img.shields.io/badge/version-1.5.7-green)](CHANGELOG.md)
[![Source Lists](https://img.shields.io/badge/source%20lists-3-blueviolet)](README.md)
[![Mapping Files](https://img.shields.io/badge/mapping%20files-58-brightgreen)](README.md)
[![Frameworks](https://img.shields.io/badge/frameworks-17-orange)](README.md)

> Die umfassendste oeffentlich verfuegbare Zuordnung von OWASP GenAI-Sicherheitsrisiken zu Branchenrahmenwerken — abdeckend LLM-Anwendungen, autonome agentische KI und GenAI-Datensicherheit ueber **17 Rahmenwerke** und **3 OWASP-Quelllisten**.

Gepflegt von der [OWASP GenAI Data Security Initiative](https://genai.owasp.org).
Erstellt von **[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)**.

---

## Was dieses Repository bietet

Jede Datei beantwortet eine Frage: **Welche Kontrollen aus Rahmenwerk X adressieren Schwachstelle Y?**

| | |
|---|---|
| **3** Quelllisten | LLM Top 10 · Agentic Top 10 · DSGAI 2026 |
| **17** Rahmenwerke | Compliance · Governance · Bedrohungsmodellierung · Tests · OT/ICS · Identitaet |
| **58** Zuordnungsdateien | Jeder Quelllisteneintrag × jedes anwendbare Rahmenwerk |
| **13** Implementierungsrezepte | Produktionsreife Python-Muster |
| **40+** Open-Source-Werkzeuge | Katalogisiert und nach Funktion organisiert |
| **10** Evaluierungsprofile | Ausfuehrbare Garak + PyRIT-Tests, zugeordnet zu OWASP-Eintraegen |
| **17** Compliance-Berichte | Pro Rahmenwerk automatisch generierte Lueckenanalysen aus der Datenschicht |
| **21** dokumentierte Vorfaelle | Reale und forschungsbasierte Vorfaelle mit MAESTRO-Schichtzuordnung |
| **LAAF v2.0** | Erstes agentisches LPCI-Red-Teaming-Rahmenwerk — vollstaendig integriert mit 6-Stufen × OWASP-Crosswalk |

Alles kostenlos. Alles Open Source. Entwickelt fuer Praktiker.

---

## Quelllisten

| Liste | Eintraege | Version | Zugeordnete Rahmenwerke |
|---|---|---|---|
| [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) | LLM01–LLM10 | 2025 | 20 |
| [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | ASI01–ASI10 | 2026 | 20 |
| [OWASP GenAI Data Security Risks](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/) | DSGAI01–DSGAI21 | 2026 | 18 |

---

## Rahmenwerk-Abdeckungsmatrix

| Rahmenwerk | LLM Top 10 | Agentic Top 10 | DSGAI 2026 |
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

---

## Alle Zuordnungsdateien

### LLM Top 10 2025 — 20 Rahmenwerk-Zuordnungen

| Datei | Rahmenwerk | Herausragender Inhalt |
|---|---|---|
| [LLM_MITREATLAS.md](llm-top10/LLM_MITREATLAS.md) | MITRE ATLAS | Zuordnung adversarialer Techniken mit Referenzen zu realen Vorfaellen |
| [LLM_NISTAIRMF.md](llm-top10/LLM_NISTAIRMF.md) | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE pro Schwachstelle mit AI RMF-Profil |
| [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) | EU AI Act | Verpflichtungen auf Artikelebene, Bussgeldrisiko, Compliance-Checkliste August 2026 |
| [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) | ISO/IEC 27001:2022 | ISMS-Erweiterungscheckliste, neue Kontrollen 2022 zugeordnet zu LLM-Risiken |
| [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) | ISO/IEC 42001:2023 | AIMS-Implementierungscheckliste, ISO 27001-Integrationsleitfaden |
| [LLM_CISControls.md](llm-top10/LLM_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3-gestufte Schutzmassnahmen pro Schwachstelle |
| [LLM_ASVS.md](llm-top10/LLM_ASVS.md) | OWASP ASVS 4.0.3 | L1/L2/L3-Verifizierungsanforderungen mit ASVS-Checkliste |
| [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Zonenmodell, SL-Bewertungen, FR/SR-Referenzen, OT-Bereitstellungscheckliste |
| [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md) | NIST SP 800-82 Rev 3 | SP 800-53-Kontrollen, regulatorischer US-Crosswalk (NERC CIP, AWIA, CMMC) |
| [LLM_NISTCSF2.md](llm-top10/LLM_NISTCSF2.md) | NIST CSF 2.0 | Sechs-Funktionen-Zuordnung einschliesslich der neuen GOVERN-Funktion, CSF 2.0-Profil |
| [LLM_SOC2.md](llm-top10/LLM_SOC2.md) | SOC 2 Trust Services Criteria | TSC-Zuordnung fuer SaaS- und Cloud-LLM-Bereitstellungen |
| [LLM_PCIDSS.md](llm-top10/LLM_PCIDSS.md) | PCI DSS v4.0 | CHD-Scope-Leitfaden, Req 3/6/7/10/11/12 pro Schwachstelle |
| [LLM_ENISA.md](llm-top10/LLM_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3-Schichtenzuordnung, EU AI Act- und NIS2-Abstimmungstabelle |
| [LLM_SAMM.md](llm-top10/LLM_SAMM.md) | OWASP SAMM v2.0 | L1–L3-Reifegradfahrplan pro Schwachstelle mit ausfuellbarer Bewertungskarte |
| [LLM_STRIDE.md](llm-top10/LLM_STRIDE.md) | STRIDE | Sechs-Kategorien-Bedrohungsmodell pro LLM-Eintrag mit DFD-Integrationsleitfaden |
| [LLM_CWE_CVE.md](llm-top10/LLM_CWE_CVE.md) | CWE / CVE | CWE-Ursachentaxonomie und bestaetigte CVE-Nachweistabelle pro Eintrag |
| [LLM_AITG.md](llm-top10/LLM_AITG.md) | OWASP AI Testing Guide | Strukturierte Testfaelle pro LLM-Eintrag mit Bestehungskriterien und CI/CD-Integrationsleitfaden |
| [LLM_MAESTRO.md](llm-top10/LLM_MAESTRO.md) | MAESTRO | Sieben-Schichten-Architektur-Bedrohungsmodell, Schicht-zu-LLM-Zuordnung, 90-Minuten-Bedrohungsmodellierungssitzungsleitfaden |
| [LLM_AIUC1.md](llm-top10/LLM_AIUC1.md) | AIUC-1 | Sechs-Domaenen-Kontrollzuordnung fuer LLM-Bereitstellungen — Zertifizierungsbereitschaftscheckliste |
| [LLM_NHI.md](llm-top10/LLM_NHI.md) | OWASP NHI Top 10 | Anmeldedaten- und Identitaetskontrollen pro LLM-Eintrag — NHI-Programmreifetabelle |

### Agentic Top 10 2026 — 20 Rahmenwerk-Zuordnungen

| Datei | Rahmenwerk | Herausragender Inhalt |
|---|---|---|
| [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) | AIUC-1 | Kontrollzuordnung fuer agentische KI-Governance-Zertifizierung |
| [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) | MITRE ATLAS | Agentische Technikverkettung, OT-Verstaerker pro Eintrag |
| [Agentic_NISTAIRMF.md](agentic-top10/Agentic_NISTAIRMF.md) | NIST AI RMF 1.0 | Autonomierichtlinien-Verankerung in GV-1.7, agentisches AI RMF-Profil |
| [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) | EU AI Act | Art. 14 menschliche Aufsicht pro Eintrag, Analyse der Autonomiepraemien-Bussgelder |
| [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) | ISO/IEC 27001:2022 | ISMS-Erweiterungscheckliste fuer agentische Bereitstellungen, NHI als A.8.2 |
| [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) | ISO/IEC 42001:2023 | A.5.2-Folgenabschaetzung pro Eintrag, EU AI Act-Abstimmungstabelle |
| [Agentic_NISTCSF2.md](agentic-top10/Agentic_NISTCSF2.md) | NIST CSF 2.0 | GOVERN-priorisierte Autonomierichtlinien-Zuordnung, agentisches CSF 2.0-Profil |
| [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Agentisches OT-Zonenmodell, Notausschalter-Design, SL-Anhebungstabelle |
| [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) | MAESTRO — CSA | Sieben-Schichten-Architektur-Bedrohungsmodell, Schicht-zu-ASI-Zuordnung, Sitzungsleitfaden |
| [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) | OWASP NHI Top 10 | Vollstaendige NHI-zu-ASI-Kreuzzuordnung, NHI-Programmreifetabelle |
| [Agentic_CISControls.md](agentic-top10/Agentic_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3-Schutzmassnahmen, agentische NHI als CIS 5 privilegierter Zugang behandelt |
| [Agentic_ASVS.md](agentic-top10/Agentic_ASVS.md) | OWASP ASVS 4.0.3 | L1/L2/L3-Verifizierungscheckliste fuer agentische Bereitstellungen |
| [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) | OWASP AI Testing Guide | 50 strukturierte Testfaelle fuer ASI01–ASI10 mit Vor-Bereitstellungstoren |
| [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) | OWASP AIVSS | Dual-Szenario-Bewertung (ueberwacht vs. autonom), Autonomiepraemie +1.79 |
| [Agentic_ENISA.md](agentic-top10/Agentic_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3-Schichtenzuordnung, EU AI Act Art. 14/15/52-Abstimmung, NIS2 Artikel 23 Vorfallbewertungsleitfaden |
| [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) | SOC 2 Trust Services Criteria | TSC-Zuordnung fuer agentische KI — Umfang autonomer Aktionen, Verarbeitungsintegritaet, Lieferkettenkriterien |
| [Agentic_PCIDSS.md](agentic-top10/Agentic_PCIDSS.md) | PCI DSS v4.0 | PCI-Audit-Leitfaden fuer Agenten mit Werkzeugzugriff auf Zahlungssysteme, Req 6/7/8/10/11/12 pro Eintrag |
| [Agentic_SAMM.md](agentic-top10/Agentic_SAMM.md) | OWASP SAMM v2.0 | L1–L3-Reifegradbewertungskarte fuer agentische KI — Vor-Bereitstellungstore und Programmreifegrad-Fahrplan |
| [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) | NIST SP 800-82 Rev 3 | OT-Agentenplatzierung, SP 800-53-Kontrollen, regulatorischer US-Crosswalk (NERC CIP, AWIA, CMMC) |

> **Ebenfalls in diesem Ordner:** [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — CWE-Ursachentaxonomie, bestaetigte CVEs, vollstaendiger CWE-Kreuzreferenzindex.

### DSGAI 2026 — 18 Rahmenwerk-Zuordnungen

| Datei | Rahmenwerk | Herausragender Inhalt |
|---|---|---|
| [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md) | ISO/IEC 27001:2022 | ISMS-Erweiterung fuer alle 21 DSGAI-Eintraege |
| [DSGAI_NISTAIRMF.md](dsgai-2026/DSGAI_NISTAIRMF.md) | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE pro DSGAI-Eintrag mit Datensicherheitsprofil |
| [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) | EU AI Act | Verpflichtungen auf Artikelebene pro Eintrag, GPAI- vs. Hochrisiko-KI-Umfang |
| [DSGAI_NISTCSF2.md](dsgai-2026/DSGAI_NISTCSF2.md) | NIST CSF 2.0 | Sechs-Funktionen-Zuordnung fuer alle 21 Eintraege, GenAI-Datensicherheitsprofil |
| [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) | MITRE ATLAS | Zuordnung adversarialer Techniken, vier vollstaendige Angriffspfadketten |
| [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) | ISA/IEC 62443 — OT/ICS | OT-Bedrohungsszenarien pro Eintrag, SL-Bewertungen, vollstaendige OT-Checkliste |
| [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) | MAESTRO — CSA | Schicht-Ursprungsanalyse fuer alle 21 Eintraege, L2 Datenoperationen als 52% der DSGAI-Bedrohungsoberflaeche |
| [DSGAI_SOC2.md](dsgai-2026/DSGAI_SOC2.md) | SOC 2 Trust Services Criteria | TSC-Zuordnung fuer SaaS- und Cloud-GenAI-Bereitstellungen |
| [DSGAI_PCIDSS.md](dsgai-2026/DSGAI_PCIDSS.md) | PCI DSS v4.0 | CHD-Scope-Leitfaden, PCI-Audit-Checkliste fuer GenAI-Daten |
| [DSGAI_ASVS.md](dsgai-2026/DSGAI_ASVS.md) | OWASP ASVS 4.0.3 | L1/L2/L3-Verifizierungsanforderungen fuer alle 21 DSGAI-Eintraege, 4-Phasen-Implementierungsprioritaet |
| [DSGAI_CISControls.md](dsgai-2026/DSGAI_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3-Schutzmassnahmen fuer alle 21 Eintraege, GenAI-Datensicherheits-Implementierungsgruppen |
| [DSGAI_CWE_CVE.md](dsgai-2026/DSGAI_CWE_CVE.md) | CWE / CVE | CWE-Ursachentaxonomie und bestaetigte CVE-Nachweise fuer alle 21 DSGAI-Eintraege |
| [DSGAI_ENISA.md](dsgai-2026/DSGAI_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3-Schichtenzuordnung, EU AI Act- und NIS2-Abstimmung fuer alle 21 DSGAI-Eintraege |
| [DSGAI_ISO42001.md](dsgai-2026/DSGAI_ISO42001.md) | ISO/IEC 42001:2023 | AIMS-Kontrollen pro DSGAI-Eintrag, ISO 27001-Integrationsleitfaden, A.7-Datengovernance-Referenz |
| [DSGAI_SAMM.md](dsgai-2026/DSGAI_SAMM.md) | OWASP SAMM v2.0 | L1–L3-Reifegradbewertungskarte fuer GenAI-Datensicherheit — DSGVO- und regulatorische Compliance-Basislinie |
| [DSGAI_NISTSP80082.md](dsgai-2026/DSGAI_NISTSP80082.md) | NIST SP 800-82 Rev 3 | OT-Datenplatzierung, SP 800-53-Kontrollen pro DSGAI-Eintrag, NERC CIP/FISMA/CMMC-Crosswalk |
| [DSGAI_AIUC1.md](dsgai-2026/DSGAI_AIUC1.md) | AIUC-1 | Domaene A (Daten und Datenschutz) deckt 50%+ der DSGAI-Eintraege ab — Zertifizierungsbereitschaftstabelle |
| [DSGAI_NHI.md](dsgai-2026/DSGAI_NHI.md) | OWASP NHI Top 10 | NHI als ermoeglichende Bedingung fuer DSGAI-Risiken — NHI-Programmreifetabelle fuer GenAI-Daten |

### Gemeinsame Ressourcen

| Datei | Inhalt |
|---|---|
| [shared/RECIPES.md](shared/RECIPES.md) | 13 Sicherheitsimplementierungsmuster mit funktionierendem Python — RAG, MCP, OT, agentisch |
| [shared/TOOLS.md](shared/TOOLS.md) | 40+ Open-Source-Sicherheitswerkzeuge nach Funktion organisiert |
| [shared/GLOSSARY.md](shared/GLOSSARY.md) | Einheitliche Terminologie ueber die Quelllisten LLM, ASI und DSGAI |
| [shared/SEVERITY.md](shared/SEVERITY.md) | Schweregrad-Definitionen und AIVSS-Abstimmung |
| [shared/TEMPLATE.md](shared/TEMPLATE.md) | Kanonische Vorlage fuer neue Zuordnungsdatei-Beitragende |

---

## Repository-Struktur

```text
crosswalk/
│
├── README.md
├── CROSSREF.md                      ← Master-Kreuzreferenz: LLM ↔ ASI ↔ DSGAI
├── CONTRIBUTING.md
├── CHANGELOG.md
├── GOVERNANCE.md                    ← Maintainer-Rollen, PR-SLOs, Entscheidungsprozess
├── SECURITY.md
├── CODE_OF_CONDUCT.md
│
├── llm-top10/                       ← LLM01–LLM10 × 20 Rahmenwerke
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
│   ├── LLM_SAMM.md                  ← Reifegradmodell
│   ├── LLM_STRIDE.md                ← Bedrohungsmodellierung
│   ├── LLM_CWE_CVE.md               ← Ursachentaxonomie + CVEs
│   ├── LLM_AITG.md                  ← KI-Testleitfaden
│   ├── LLM_MAESTRO.md               ← MAESTRO Sieben-Schichten-Bedrohungsmodell
│   ├── LLM_AIUC1.md                 ← AIUC-1-Zertifizierungsrahmenwerk
│   └── LLM_NHI.md                   ← Nicht-menschliche Identitaetskontrollen
│
├── agentic-top10/                   ← ASI01–ASI10 × 20 Rahmenwerke
│   ├── Agentic_AIUC1.md
│   ├── Agentic_MITREATLAS.md
│   ├── Agentic_NISTAIRMF.md
│   ├── Agentic_EUAIAct.md
│   ├── Agentic_ISO27001.md
│   ├── Agentic_ISO42001.md
│   ├── Agentic_NISTCSF2.md
│   ├── Agentic_ISA62443.md          ← OT/ICS
│   ├── Agentic_MAESTRO.md           ← Bedrohungsmodellierung — 7-Schichten-Architektur
│   ├── Agentic_OWASP_NHI.md         ← Nicht-menschliche Identitaet
│   ├── Agentic_CISControls.md
│   ├── Agentic_ASVS.md
│   ├── Agentic_AITG.md              ← KI-Testleitfaden — 50 Testfaelle
│   ├── Agentic_AIVSS.md             ← Risikobewertung — Autonomiepraemie
│   ├── Agentic_CWE_CVE.md           ← CWE-Taxonomie + bestaetigte CVEs
│   ├── Agentic_ENISA.md             ← EU / NIS2
│   ├── Agentic_SOC2.md              ← SOC 2 TSC — agentische KI-Pruefung
│   ├── Agentic_PCIDSS.md            ← PCI DSS v4.0 — Zahlungssystem-Agenten
│   ├── Agentic_SAMM.md              ← Reifegradmodell — Vor-Bereitstellungstore
│   └── Agentic_NISTSP80082.md       ← OT/ICS — US-regulatorische Abstimmung
│
├── dsgai-2026/                      ← DSGAI01–DSGAI21 × 18 Rahmenwerke
│   ├── DSGAI_ISO27001.md
│   ├── DSGAI_NISTAIRMF.md
│   ├── DSGAI_EUAIAct.md
│   ├── DSGAI_NISTCSF2.md
│   ├── DSGAI_MITREATLAS.md
│   ├── DSGAI_ISA62443.md            ← OT/ICS
│   ├── DSGAI_MAESTRO.md             ← Bedrohungsmodellierung — Datenoperations-Perspektive
│   ├── DSGAI_SOC2.md
│   ├── DSGAI_PCIDSS.md
│   ├── DSGAI_ASVS.md                ← OWASP ASVS 4.0.3
│   ├── DSGAI_CISControls.md         ← CIS Controls v8.1
│   ├── DSGAI_CWE_CVE.md             ← Ursachentaxonomie + CVEs
│   ├── DSGAI_ENISA.md               ← EU / NIS2
│   ├── DSGAI_ISO42001.md            ← KI-Managementsystem
│   ├── DSGAI_SAMM.md                ← Reifegradmodell — Datensicherheitsprogramm
│   ├── DSGAI_NISTSP80082.md         ← OT/ICS — US-regulatorische Abstimmung
│   ├── DSGAI_AIUC1.md               ← AIUC-1-Zertifizierungsrahmenwerk
│   └── DSGAI_NHI.md                 ← Nicht-menschliche Identitaet — Datenpipeline-Anmeldedaten
│
├── shared/
│   ├── RECIPES.md                   ← 13 Implementierungsmuster (Python-Code)
│   ├── TOOLS.md                     ← Katalog von 40+ Open-Source-Werkzeugen
│   ├── GLOSSARY.md                  ← Einheitliche Terminologie
│   ├── SEVERITY.md                  ← Schweregrad-Definitionen + AIVSS-Abstimmung
│   └── TEMPLATE.md                  ← Kanonische Vorlage fuer neue Zuordnungsdateien
│
├── data/
│   ├── schema.json                  ← JSON Schema (Draft 7) fuer Eintragsdateien
│   ├── incidents.json               ← 20 Vorfaelle mit MAESTRO-Schichtzuordnung
│   ├── incidents-schema.json        ← JSON Schema fuer Vorfaelle
│   ├── entries/                     ← 41 maschinenlesbare Eintrags-JSON-Dateien
│   └── README.md                    ← Datenschicht-Dokumentation, jq-Abfragebeispiele
│
├── scripts/
│   ├── validate.js                  ← Inhaltsvalidator (Abschnitte, Links, Zaehler)
│   ├── generate.js                  ← Markdown-zu-JSON-Parser → data/entries/
│   └── compliance-report.js         ← Lueckenanalyse-Generator (MD / CSV / JSON)
│
├── evals/
│   ├── README.md                    ← Einrichtungsleitfaden und Ergebnisinterpretation
│   ├── garak/                       ← 7 YAML-Profile (LLM01/02/04/07/09, ASI01/05)
│   ├── pyrit/                       ← 3 asynchrone Python-Skripte (LLM01, DSGAI04, ASI01)
│   ├── laaf/                        ← LAAF v2.0 LPCI-Suite (S1–S6 + Crosswalk-Reporter)
│   └── ci/                          ← github-action.yml — Sofort einsetzbare CI/CD-Vorlage
│
└── i18n/
    ├── WORKFLOW.md                  ← Leitfaden fuer Uebersetzungsbeitragende
    ├── es/                          ← Spanisch (PRs willkommen)
    ├── fr/                          ← Franzoesisch (PRs willkommen)
    └── pt/                          ← Portugiesisch (PRs willkommen)
```

---

## Compliance-Lueckenanalyse-Berichte

Generieren Sie rahmenwerk-spezifische Lueckenanalysen aus der Datenschicht in Sekunden:

```bash
node scripts/compliance-report.js                          # alle 17 Rahmenwerke → reports/
node scripts/compliance-report.js --framework "EU AI Act"  # ein Rahmenwerk
node scripts/compliance-report.js --format csv             # Excel-kompatibel
node scripts/compliance-report.js --format json            # maschinenlesbar
node scripts/compliance-report.js --list-frameworks        # alle Optionen anzeigen
```

Jeder Bericht umfasst: Zusammenfassung fuer die Geschaeftsfuehrung, Abdeckungsmatrix (OWASP-Eintraege × Kontrollen), Kontrolldetails mit Anmerkungen und einen priorisierten Massnahmenplan.

## LAAF v2.0 — LPCI-Red-Teaming

[LAAF v2.0](https://github.com/qorvexconsulting1/laaf-V2.0) ist als drittes Evaluierungsrahmenwerk neben Garak und PyRIT integriert. Es deckt die Angriffsflaeche ab, die oberflaechliche Injektionstests nicht erkennen: Speicherpersistenz, geschichtete Kodierung, semantische Umformulierung und 6-Stufen-Lebenszyklusangriffe.

```bash
pip install git+https://github.com/qorvexconsulting1/laaf-V2.0.git
export OPENAI_API_KEY=sk-...
bash evals/laaf/run_laaf.sh           # S1–S6 vollstaendige Suite
laaf scan --target mock --dry-run     # Kein API-Schluessel erforderlich
```

| LAAF-Stufe | OWASP | Schwellenwert |
|---|---|---|
| S1 Aufklaerung | LLM07, LLM01 | 0% |
| S2 Logikschicht-Injektion | LLM01, ASI01, DSGAI04 | 5% |
| S3 Trigger-Ausfuehrung | ASI01, ASI06, LLM06 | 0% |
| S4 Persistenz | ASI06, LLM06, DSGAI04 | 0% |
| S5 Umgehung | LLM01, LLM02 | 10% |
| S6 Spurenmanipulation | DSGAI01, LLM07 | 0% |

Den vollstaendigen LPCI-Angriffsvektor → OWASP → MAESTRO-Crosswalk finden Sie unter `evals/laaf/README.md`.

---

## Vorfalltracker

20 reale und forschungsbelegte Vorfaelle, jeweils zugeordnet zu OWASP-Eintraegen und MAESTRO-Architekturschichten:

```bash
node scripts/incidents-report.js                      # alle Vorfaelle → reports/incidents.md
node scripts/incidents-report.js --entry LLM01        # Vorfaelle fuer einen bestimmten Eintrag
node scripts/incidents-report.js --layer L3           # Vorfaelle mit Bezug zu Agent Frameworks
node scripts/incidents-report.js --category real-world
node scripts/incidents-report.js --format csv         # Excel-Export
```

Pro Vorfall verfolgte MAESTRO-Schichtrollen: **Ursprung** (wo der Angriff beginnt) · **Ausbreitung** (wie er sich verbreitet) · **Auswirkung** (wo der Schaden eintritt) · **Blinder Fleck** (wo die Erkennung versagte).

---

## Starten Sie hier — nach Rolle

Finden Sie Ihren Einstiegspunkt in unter 60 Sekunden.

**Ich muss den EU AI Act vor August 2026 einhalten**
→ Start: [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) — Verpflichtungen auf Artikelebene, Bussgeldrisiko, Compliance-Checkliste
→ Dann: [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) wenn Sie autonome Agenten bereitstellen (Art. 14 menschliche Aufsicht)
→ Dann: [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) fuer den GPAI-Modellumfang und Datengovernance-Verpflichtungen

**Ich stelle einen autonomen KI-Agenten bereit und muss wissen, was schiefgehen kann**
→ Start: [CROSSREF.md](CROSSREF.md) — Master-Kreuzreferenz ueber alle 41 Schwachstellen-IDs
→ Dann: [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — Architektur-Bedrohungsmodell (wo entsteht jedes Risiko?)
→ Dann: [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — jedes Risiko bewerten; Autonomie fuegt durchschnittlich +1.79 Schweregrad hinzu
→ Dann: [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — Identitaets- und Anmeldedatenkontrollen

**Ich bin SOC 2-Pruefer oder GRC-Fachperson und bereite eine GenAI-Kontrollbewertung vor**
→ Start: [LLM_SOC2.md](llm-top10/LLM_SOC2.md) — TSC-Zuordnung fuer SaaS-/Cloud-LLM-Bereitstellungen
→ Dann: [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) — Umfang autonomer Aktionen, Verarbeitungsintegritaetskriterien
→ Dann: [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — ausfuellbare SAMM-Reifegradbewertungskarte als Nachweis der Programmvollstaendigkeit

**Ich bin AppSec-Ingenieur oder Red-Teamer und erstelle einen Testplan**
→ Start: [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50 strukturierte Testfaelle mit Bestehungskriterien und CI/CD-Toren
→ Dann: [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — Angreifer-TTP-Zuordnung mit vier vollstaendigen Angriffsketten
→ Dann: [shared/RECIPES.md](shared/RECIPES.md) — 13 funktionierende Python-Muster zur Implementierung der zu testenden Kontrollen

**Ich sichere KI in OT/ICS-Umgebungen (Energie, Versorgung, Fertigung)**
→ Start: [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) — OT-Zonenmodell, SP 800-53-Kontrollen, NERC CIP/AWIA/CMMC-Crosswalk
→ Dann: [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) — SL-Bewertungen, Zonenmodell, Notausschalter-Design
→ Dann: [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — RAG-Corpus-Poisoning in OT (Sicherheitsverfahren-Manipulationsszenario)

---

## Schnellnavigation

**EU AI Act-Compliance bis August 2026**
→ [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) · [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) · [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md)

**Europaeische Organisation unter NIS2**
→ [LLM_ENISA.md](llm-top10/LLM_ENISA.md) — ENISA-Rahmenwerk mit NIS2 Artikel 23 Vorfallbewertungsleitfaden

**KI in OT/ICS-Umgebungen**
→ [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) · [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) · [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) · [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md)

**Bereitstellung autonomer Agenten**
→ [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — Identitaetsgovernance
→ [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) — Agentische Governance-Zertifizierung
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — Risikobewertung mit Autonomiepraemie

**Bedrohungsmodellierung eines agentischen KI-Systems vor der Kontrollauswahl**
→ [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — MAESTRO Sieben-Schichten-Bedrohungsaufzaehlung mit Sitzungsleitfaden
→ [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) — MAESTRO-Datenoperations-Perspektive fuer alle 21 DSGAI-Eintraege

**ISO 27001 ISMS-Erweiterung fuer GenAI**
→ [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) · [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) · [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md)

**ISO 42001 AIMS fuer KI-Governance**
→ [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) · [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) — mit EU AI Act-Compliance-Nachweistabelle

**Sicherheitsprogramm-Reifegrad**
→ [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — SAMM L1–L3-Fahrplan mit ausfuellbarer Bewertungskarte

**Sicherheitstestplan fuer agentische KI**
→ [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50 strukturierte Testfaelle, Vor-Bereitstellungstore, OT-Anhang

**Risikoregister-Bewertung fuer agentische KI**
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — Dual-Szenario-Bewertung ueberwacht vs. autonom, durchschnittliche Autonomiepraemie +1.79

**Angreiferperspektive auf GenAI-Risiken**
→ [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — ATLAS-Technikzuordnung, vier Angriffspfadketten
→ [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) — Agentische Technikverkettung

**CWE-Grundursachen und bestaetigte CVEs**
→ [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — Ursachentaxonomie, CVE-Nachweise, Kreuzreferenzindex

**Implementierungscode, keine Rahmenwerk-Theorie**
→ [shared/RECIPES.md](shared/RECIPES.md) — 13 Produktionsmuster mit funktionierendem Python

**Alle Risiken ueber alle drei Quelllisten**
→ [CROSSREF.md](CROSSREF.md) — Master-Kreuzreferenz

---

## Herausragende Abdeckung

### Vollstaendige OT/ICS-Trilogie

Die einzige oeffentlich verfuegbare Zuordnung aller drei OWASP GenAI-Quelllisten zu ISA/IEC 62443 und NIST SP 800-82 Rev 3. Enthaelt Zonenmodell-Platzierung, Sicherheitsstufenbewertungen, Referenzen fuer grundlegende Anforderungen und Sicherheitsanforderungen, OT-spezifische Bedrohungsszenarien und Vor-Bereitstellungschecklisten fuer jede Quellliste.

Das RAG-Corpus-Poisoning-Szenario in [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — ein Sicherheitsverfahren-Manipulationsangriff, der Wartungsintervalle ohne jeglichen OT-Netzwerkzugang aendert — existiert nirgendwo sonst in oeffentlicher Dokumentation.

### MAESTRO Sieben-Schichten-Bedrohungsmodellierung

[Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) und [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) sind die einzigen oeffentlichen Zuordnungen von OWASP GenAI-Risiken zum MAESTRO-Rahmenwerk der Cloud Security Alliance. Im Gegensatz zu allen anderen Dateien in diesem Repository — die Risiken Kontrollen zuordnen — ordnet MAESTRO jedes Risiko der **Architekturschicht zu, in der es entsteht**, und zeigt Ihnen, welches Team das Problem besitzt und wo im System die Behebung bereitgestellt werden muss.

Zentrale Erkenntnis aus der DSGAI-Zuordnung: **L2 Datenoperationen ist die Ursprungsschicht fuer 52% aller DSGAI-Eintraege**. Eine Organisation, die RAG-Corpora, Embedding-Speicher, Trainingspipelines und Speichersysteme nicht als sicherheitskritische Infrastruktur behandelt, ist gegen die Mehrheit der GenAI-Datensicherheits-Bedrohungslandschaft unzureichend verteidigt.

### Agentische Autonomiepraemie

[Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) quantifiziert, was das Entfernen menschlicher Aufsicht an Risiko kostet: durchschnittlich **+1.79 AIVSS-Schweregradpunkte** ueber alle 10 agentischen Eintraege. Das Entfernen menschlicher Aufsicht wandelt 7 von 10 Eintraegen von Hoch in Kritisch um — das quantitative Argument fuer die obligatorische menschliche Aufsicht gemaess EU AI Act Artikel 14.

### Vollstaendige agentische Identitaetsabdeckung

[Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) ordnet jeden NHI Top 10-Eintrag jedem ASI-Eintrag zu — das einzige oeffentliche Dokument, das agentische Sicherheitsrisiken in die NHI-Kontrollen uebersetzt, die IAM-Teams bereits betreiben.

### SAMM-Reifegradbewertungskarte

[LLM_SAMM.md](llm-top10/LLM_SAMM.md) enthaelt eine ausfuellbare Reifegradbewertungskarte mit minimal tragfaehigen Stufen pro SAMM-Praxis fuer jede LLM-Produktionsbereitstellung — das Artefakt, das Sicherheitsprogramm-Verantwortliche verwenden, um die Ingenieursfuehrung ueber den Stand des Programms und die naechsten Verbesserungen zu informieren.

### Produktions-Implementierungsrezepte

[shared/RECIPES.md](shared/RECIPES.md) enthaelt 13 produktionsreife Sicherheitsmuster mit funktionierendem Python: zugriffskontrollierter RAG-Abruf, MCP-Deskriptor-Integritaetspruefung, JIT-Anmeldedatenausstellung, OT-Notausschalter, verhaltensbasierte Basislinienueberwachung, Kaskadeneingrenzung und menschliche Bestaetigungstore.

---

## Mitwirken

Beitraege sind willkommen — neue Rahmenwerk-Zuordnungen, aktualisierte Kontrollen, neue Implementierungsrezepte, Uebersetzungen und zusaetzliche Werkzeugeintraege.

Informationen zur Dateivorlage, zum PR-Prozess und zu den Beitragsrichtlinien finden Sie unter [CONTRIBUTING.md](CONTRIBUTING.md). Alle Mitwirkenden werden im CHANGELOG aufgefuehrt.

---

## Lizenz

[Creative Commons Attribution-ShareAlike 4.0 International](LICENSE)

Frei zum Teilen und Anpassen fuer jeden Zweck, einschliesslich kommerzieller Nutzung, mit angemessener Namensnennung und Weitergabe unter gleichen Bedingungen.

---

## Danksagungen

Erstellt und gepflegt von **[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)** und der [OWASP GenAI Data Security Initiative](https://genai.owasp.org).

Aufgebaut auf der Arbeit der Projektteams von OWASP LLM Top 10, OWASP Agentic Top 10, OWASP GenAI Data Security, OWASP NHI Top 10 und OWASP SAMM.

Besonderer Dank an [Ken Huang](https://github.com/kenhuangus) (Cloud Security Alliance) fuer das MAESTRO-Rahmenwerk und seine Beitraege zum OWASP LLM Top 10.

---

*[genai.owasp.org](https://genai.owasp.org) · [CC BY-SA 4.0](LICENSE)*
