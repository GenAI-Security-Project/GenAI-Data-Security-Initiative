<!--
  Translation: Spanish
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

> El mapeo público más completo de los riesgos de seguridad GenAI de OWASP hacia marcos de referencia de la industria — cubriendo aplicaciones LLM, IA autónoma agéntica y seguridad de datos GenAI en **17 marcos de referencia** y **3 listas fuente de OWASP**.

Mantenido por la [Iniciativa de Seguridad de Datos GenAI de OWASP](https://genai.owasp.org).
Creado por **[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)**.

---

## Qué proporciona este repositorio

Cada archivo responde a una pregunta: **¿qué controles del marco de referencia X abordan la vulnerabilidad Y?**

| | |
|---|---|
| **3** listas fuente | LLM Top 10 · Agentic Top 10 · DSGAI 2026 |
| **17** marcos de referencia | Cumplimiento · Gobernanza · Modelado de amenazas · Pruebas · OT/ICS · Identidad |
| **58** archivos de mapeo | Cada entrada de lista fuente × cada marco de referencia aplicable |
| **13** recetas de implementación | Patrones Python listos para producción |
| **40+** herramientas de código abierto | Catalogadas y organizadas por función |
| **10** perfiles de evaluación | Pruebas ejecutables Garak + PyRIT mapeadas a entradas OWASP |
| **17** informes de cumplimiento | Evaluaciones de brechas por marco de referencia generadas automáticamente desde la capa de datos |
| **21** incidentes documentados | Incidentes reales e investigados con atribución de capa MAESTRO |
| **LAAF v2.0** | Primer marco de referencia de red-teaming agéntico LPCI — completamente integrado con crosswalk de 6 etapas × OWASP |

Todo gratuito. Todo de código abierto. Construido para profesionales.

---

## Listas fuente

| Lista | Entradas | Versión | Marcos de referencia mapeados |
|---|---|---|---|
| [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) | LLM01–LLM10 | 2025 | 20 |
| [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | ASI01–ASI10 | 2026 | 20 |
| [OWASP GenAI Data Security Risks](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/) | DSGAI01–DSGAI21 | 2026 | 18 |

---

## Matriz de cobertura de marcos de referencia

| Marco de referencia | LLM Top 10 | Agentic Top 10 | DSGAI 2026 |
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

## Todos los archivos de mapeo

### LLM Top 10 2025 — 20 mapeos de marcos de referencia

| Archivo | Marco de referencia | Contenido destacado |
|---|---|---|
| [LLM_MITREATLAS.md](llm-top10/LLM_MITREATLAS.md) | MITRE ATLAS | Mapeo de técnicas adversarias con referencias a incidentes reales |
| [LLM_NISTAIRMF.md](llm-top10/LLM_NISTAIRMF.md) | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE por vulnerabilidad con perfil AI RMF |
| [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) | EU AI Act | Obligaciones a nivel de artículo, exposición a multas, lista de verificación de cumplimiento para agosto 2026 |
| [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) | ISO/IEC 27001:2022 | Lista de verificación de extensión ISMS, controles nuevos de 2022 mapeados a riesgos LLM |
| [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) | ISO/IEC 42001:2023 | Lista de verificación de implementación AIMS, guía de integración con ISO 27001 |
| [LLM_CISControls.md](llm-top10/LLM_CISControls.md) | CIS Controls v8.1 | Salvaguardas escalonadas IG1/IG2/IG3 por vulnerabilidad |
| [LLM_ASVS.md](llm-top10/LLM_ASVS.md) | OWASP ASVS 4.0.3 | Requisitos de verificación L1/L2/L3 con lista de verificación ASVS |
| [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Modelo de zonas, calificaciones SL, referencias FR/SR, lista de verificación de despliegue OT |
| [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md) | NIST SP 800-82 Rev 3 | Controles SP 800-53, mapeo cruzado regulatorio de EE.UU. (NERC CIP, AWIA, CMMC) |
| [LLM_NISTCSF2.md](llm-top10/LLM_NISTCSF2.md) | NIST CSF 2.0 | Mapeo de seis funciones incluyendo la nueva función GOVERN, perfil CSF 2.0 |
| [LLM_SOC2.md](llm-top10/LLM_SOC2.md) | SOC 2 Trust Services Criteria | Mapeo TSC para despliegues LLM en SaaS y nube |
| [LLM_PCIDSS.md](llm-top10/LLM_PCIDSS.md) | PCI DSS v4.0 | Guía de alcance CHD, Req 3/6/7/10/11/12 por vulnerabilidad |
| [LLM_ENISA.md](llm-top10/LLM_ENISA.md) | ENISA Multilayer Framework | Mapeo de capas L1/L2/L3, tabla de alineación con EU AI Act y NIS2 |
| [LLM_SAMM.md](llm-top10/LLM_SAMM.md) | OWASP SAMM v2.0 | Hoja de ruta de madurez L1–L3 por vulnerabilidad con tarjeta de puntuación rellenable |
| [LLM_STRIDE.md](llm-top10/LLM_STRIDE.md) | STRIDE | Modelo de amenazas de seis categorías por entrada LLM con guía de integración DFD |
| [LLM_CWE_CVE.md](llm-top10/LLM_CWE_CVE.md) | CWE / CVE | Taxonomía de causa raíz CWE y tabla de evidencia CVE confirmada por entrada |
| [LLM_AITG.md](llm-top10/LLM_AITG.md) | OWASP AI Testing Guide | Casos de prueba estructurados por entrada LLM con criterios de aprobación y guía de integración CI/CD |
| [LLM_MAESTRO.md](llm-top10/LLM_MAESTRO.md) | MAESTRO | Modelo de amenazas arquitectónico de siete capas, mapeo capa-a-LLM, guía de sesión de modelado de amenazas de 90 minutos |
| [LLM_AIUC1.md](llm-top10/LLM_AIUC1.md) | AIUC-1 | Mapeo de controles de seis dominios para despliegues LLM — lista de verificación de preparación para certificación |
| [LLM_NHI.md](llm-top10/LLM_NHI.md) | OWASP NHI Top 10 | Controles de credenciales e identidad por entrada LLM — tabla de madurez del programa NHI |

### Agentic Top 10 2026 — 20 mapeos de marcos de referencia

| Archivo | Marco de referencia | Contenido destacado |
|---|---|---|
| [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) | AIUC-1 | Mapeo de controles de certificación de gobernanza de IA agéntica |
| [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) | MITRE ATLAS | Encadenamiento de técnicas agénticas, amplificadores OT por entrada |
| [Agentic_NISTAIRMF.md](agentic-top10/Agentic_NISTAIRMF.md) | NIST AI RMF 1.0 | Anclaje de política de autonomía en GV-1.7, perfil agéntico AI RMF |
| [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) | EU AI Act | Art. 14 supervisión humana por entrada, análisis de multas por prima de autonomía |
| [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) | ISO/IEC 27001:2022 | Lista de verificación de extensión ISMS para despliegues agénticos, NHI como A.8.2 |
| [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) | ISO/IEC 42001:2023 | Evaluación de impacto A.5.2 por entrada, tabla de alineación con EU AI Act |
| [Agentic_NISTCSF2.md](agentic-top10/Agentic_NISTCSF2.md) | NIST CSF 2.0 | Mapeo de política de autonomía GOVERN-first, perfil agéntico CSF 2.0 |
| [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Modelo de zonas OT agéntico, diseño de interruptor de emergencia, tabla de elevación SL |
| [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) | MAESTRO — CSA | Modelo de amenazas arquitectónico de siete capas, mapeo capa-a-ASI, guía de sesión |
| [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) | OWASP NHI Top 10 | Mapeo cruzado completo NHI-a-ASI, tabla de madurez del programa NHI |
| [Agentic_CISControls.md](agentic-top10/Agentic_CISControls.md) | CIS Controls v8.1 | Salvaguardas IG1/IG2/IG3, NHI agéntico tratado como acceso privilegiado CIS 5 |
| [Agentic_ASVS.md](agentic-top10/Agentic_ASVS.md) | OWASP ASVS 4.0.3 | Lista de verificación L1/L2/L3 para despliegues agénticos |
| [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) | OWASP AI Testing Guide | 50 casos de prueba estructurados para ASI01–ASI10 con puertas de pre-despliegue |
| [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) | OWASP AIVSS | Puntuación de doble escenario (supervisado vs autónomo), prima de autonomía +1.79 |
| [Agentic_ENISA.md](agentic-top10/Agentic_ENISA.md) | ENISA Multilayer Framework | Mapeo de capas L1/L2/L3, alineación con EU AI Act Art. 14/15/52, guía de evaluación de incidentes NIS2 Artículo 23 |
| [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) | SOC 2 Trust Services Criteria | Mapeo TSC para IA agéntica — alcance de acción autónoma, integridad de procesamiento, criterios de cadena de suministro |
| [Agentic_PCIDSS.md](agentic-top10/Agentic_PCIDSS.md) | PCI DSS v4.0 | Guía de auditoría PCI para agentes con acceso a herramientas de sistemas de pago, Req 6/7/8/10/11/12 por entrada |
| [Agentic_SAMM.md](agentic-top10/Agentic_SAMM.md) | OWASP SAMM v2.0 | Tarjeta de puntuación de madurez L1–L3 para IA agéntica — puertas de pre-despliegue y hoja de ruta de madurez del programa |
| [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) | NIST SP 800-82 Rev 3 | Ubicación de agentes OT, controles SP 800-53, mapeo cruzado regulatorio de EE.UU. (NERC CIP, AWIA, CMMC) |

> **También en esta carpeta:** [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — Taxonomía de causa raíz CWE, CVEs confirmados, índice de referencia cruzada CWE completo.

### DSGAI 2026 — 18 mapeos de marcos de referencia

| Archivo | Marco de referencia | Contenido destacado |
|---|---|---|
| [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md) | ISO/IEC 27001:2022 | Extensión ISMS cubriendo las 21 entradas DSGAI |
| [DSGAI_NISTAIRMF.md](dsgai-2026/DSGAI_NISTAIRMF.md) | NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE por entrada DSGAI con perfil de seguridad de datos |
| [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) | EU AI Act | Obligaciones a nivel de artículo por entrada, alcance GPAI vs IA de alto riesgo |
| [DSGAI_NISTCSF2.md](dsgai-2026/DSGAI_NISTCSF2.md) | NIST CSF 2.0 | Mapeo de seis funciones para las 21 entradas, perfil de seguridad de datos GenAI |
| [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) | MITRE ATLAS | Mapeo de técnicas adversarias, cuatro cadenas de ruta de ataque completas |
| [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) | ISA/IEC 62443 — OT/ICS | Escenarios de amenazas OT por entrada, calificaciones SL, lista de verificación OT completa |
| [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) | MAESTRO — CSA | Análisis de capa de origen para las 21 entradas, L2 operaciones de datos como 52% de la superficie de amenazas DSGAI |
| [DSGAI_SOC2.md](dsgai-2026/DSGAI_SOC2.md) | SOC 2 Trust Services Criteria | Mapeo TSC para despliegues GenAI en SaaS y nube |
| [DSGAI_PCIDSS.md](dsgai-2026/DSGAI_PCIDSS.md) | PCI DSS v4.0 | Guía de alcance CHD, lista de verificación de auditoría PCI para datos GenAI |
| [DSGAI_ASVS.md](dsgai-2026/DSGAI_ASVS.md) | OWASP ASVS 4.0.3 | Requisitos de verificación L1/L2/L3 para las 21 entradas DSGAI, prioridad de implementación en 4 fases |
| [DSGAI_CISControls.md](dsgai-2026/DSGAI_CISControls.md) | CIS Controls v8.1 | Salvaguardas IG1/IG2/IG3 para las 21 entradas, grupos de implementación de seguridad de datos GenAI |
| [DSGAI_CWE_CVE.md](dsgai-2026/DSGAI_CWE_CVE.md) | CWE / CVE | Taxonomía de causa raíz CWE y evidencia CVE confirmada para las 21 entradas DSGAI |
| [DSGAI_ENISA.md](dsgai-2026/DSGAI_ENISA.md) | ENISA Multilayer Framework | Mapeo de capas L1/L2/L3, alineación con EU AI Act y NIS2 para las 21 entradas DSGAI |
| [DSGAI_ISO42001.md](dsgai-2026/DSGAI_ISO42001.md) | ISO/IEC 42001:2023 | Controles AIMS por entrada DSGAI, guía de integración con ISO 27001, referencia de gobernanza de datos A.7 |
| [DSGAI_SAMM.md](dsgai-2026/DSGAI_SAMM.md) | OWASP SAMM v2.0 | Tarjeta de puntuación de madurez L1–L3 para seguridad de datos GenAI — línea base de cumplimiento regulatorio y GDPR |
| [DSGAI_NISTSP80082.md](dsgai-2026/DSGAI_NISTSP80082.md) | NIST SP 800-82 Rev 3 | Ubicación de datos OT, controles SP 800-53 por entrada DSGAI, mapeo cruzado NERC CIP/FISMA/CMMC |
| [DSGAI_AIUC1.md](dsgai-2026/DSGAI_AIUC1.md) | AIUC-1 | Dominio A (Datos y Privacidad) cubre 50%+ de entradas DSGAI — tabla de preparación para certificación |
| [DSGAI_NHI.md](dsgai-2026/DSGAI_NHI.md) | OWASP NHI Top 10 | NHI como condición habilitante para riesgos DSGAI — tabla de madurez del programa NHI para datos GenAI |

### Recursos compartidos

| Archivo | Contenido |
|---|---|
| [shared/RECIPES.md](shared/RECIPES.md) | 13 patrones de implementación de seguridad con Python funcional — RAG, MCP, OT, agéntico |
| [shared/TOOLS.md](shared/TOOLS.md) | 40+ herramientas de seguridad de código abierto organizadas por función |
| [shared/GLOSSARY.md](shared/GLOSSARY.md) | Terminología unificada entre las listas fuente LLM, ASI y DSGAI |
| [shared/SEVERITY.md](shared/SEVERITY.md) | Definiciones de severidad y alineación con AIVSS |
| [shared/TEMPLATE.md](shared/TEMPLATE.md) | Plantilla canónica para nuevos contribuyentes de archivos de mapeo |

---

## Estructura del repositorio

```text
crosswalk/
│
├── README.md
├── CROSSREF.md                      ← Referencia cruzada maestra: LLM ↔ ASI ↔ DSGAI
├── CONTRIBUTING.md
├── CHANGELOG.md
├── GOVERNANCE.md                    ← Roles de mantenedores, SLOs de PR, proceso de decisión
├── SECURITY.md
├── CODE_OF_CONDUCT.md
│
├── llm-top10/                       ← LLM01–LLM10 × 20 marcos de referencia
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
│   ├── LLM_ENISA.md                 ← UE / NIS2
│   ├── LLM_SAMM.md                  ← Modelo de madurez
│   ├── LLM_STRIDE.md                ← Modelado de amenazas
│   ├── LLM_CWE_CVE.md               ← Taxonomía de causa raíz + CVEs
│   ├── LLM_AITG.md                  ← Guía de pruebas de IA
│   ├── LLM_MAESTRO.md               ← Modelo de amenazas de siete capas MAESTRO
│   ├── LLM_AIUC1.md                 ← Marco de certificación AIUC-1
│   └── LLM_NHI.md                   ← Controles de identidad no humana
│
├── agentic-top10/                   ← ASI01–ASI10 × 20 marcos de referencia
│   ├── Agentic_AIUC1.md
│   ├── Agentic_MITREATLAS.md
│   ├── Agentic_NISTAIRMF.md
│   ├── Agentic_EUAIAct.md
│   ├── Agentic_ISO27001.md
│   ├── Agentic_ISO42001.md
│   ├── Agentic_NISTCSF2.md
│   ├── Agentic_ISA62443.md          ← OT/ICS
│   ├── Agentic_MAESTRO.md           ← Modelado de amenazas — arquitectura de 7 capas
│   ├── Agentic_OWASP_NHI.md         ← Identidad no humana
│   ├── Agentic_CISControls.md
│   ├── Agentic_ASVS.md
│   ├── Agentic_AITG.md              ← Guía de pruebas de IA — 50 casos de prueba
│   ├── Agentic_AIVSS.md             ← Puntuación de riesgos — prima de autonomía
│   ├── Agentic_CWE_CVE.md           ← Taxonomía CWE + CVEs confirmados
│   ├── Agentic_ENISA.md             ← UE / NIS2
│   ├── Agentic_SOC2.md              ← SOC 2 TSC — auditoría de IA agéntica
│   ├── Agentic_PCIDSS.md            ← PCI DSS v4.0 — agentes de sistemas de pago
│   ├── Agentic_SAMM.md              ← Modelo de madurez — puertas de pre-despliegue
│   └── Agentic_NISTSP80082.md       ← OT/ICS — alineación regulatoria de EE.UU.
│
├── dsgai-2026/                      ← DSGAI01–DSGAI21 × 18 marcos de referencia
│   ├── DSGAI_ISO27001.md
│   ├── DSGAI_NISTAIRMF.md
│   ├── DSGAI_EUAIAct.md
│   ├── DSGAI_NISTCSF2.md
│   ├── DSGAI_MITREATLAS.md
│   ├── DSGAI_ISA62443.md            ← OT/ICS
│   ├── DSGAI_MAESTRO.md             ← Modelado de amenazas — perspectiva de operaciones de datos
│   ├── DSGAI_SOC2.md
│   ├── DSGAI_PCIDSS.md
│   ├── DSGAI_ASVS.md                ← OWASP ASVS 4.0.3
│   ├── DSGAI_CISControls.md         ← CIS Controls v8.1
│   ├── DSGAI_CWE_CVE.md             ← Taxonomía de causa raíz + CVEs
│   ├── DSGAI_ENISA.md               ← UE / NIS2
│   ├── DSGAI_ISO42001.md            ← Sistema de gestión de IA
│   ├── DSGAI_SAMM.md                ← Modelo de madurez — programa de seguridad de datos
│   ├── DSGAI_NISTSP80082.md         ← OT/ICS — alineación regulatoria de EE.UU.
│   ├── DSGAI_AIUC1.md               ← Marco de certificación AIUC-1
│   └── DSGAI_NHI.md                 ← Identidad no humana — credenciales de pipeline de datos
│
├── shared/
│   ├── RECIPES.md                   ← 13 patrones de implementación (código Python)
│   ├── TOOLS.md                     ← Catálogo de 40+ herramientas de código abierto
│   ├── GLOSSARY.md                  ← Terminología unificada
│   ├── SEVERITY.md                  ← Definiciones de severidad + alineación AIVSS
│   └── TEMPLATE.md                  ← Plantilla canónica para nuevos archivos de mapeo
│
├── data/
│   ├── schema.json                  ← JSON Schema (Draft 7) para archivos de entrada
│   ├── incidents.json               ← 20 incidentes con atribución de capa MAESTRO
│   ├── incidents-schema.json        ← JSON Schema para incidentes
│   ├── entries/                     ← 41 archivos JSON de entradas legibles por máquina
│   └── README.md                    ← Documentación de la capa de datos, ejemplos de consultas jq
│
├── scripts/
│   ├── validate.js                  ← Validador de contenido (secciones, enlaces, conteos)
│   ├── generate.js                  ← Analizador Markdown-a-JSON → data/entries/
│   └── compliance-report.js         ← Generador de evaluación de brechas (MD / CSV / JSON)
│
├── evals/
│   ├── README.md                    ← Guía de configuración e interpretación de resultados
│   ├── garak/                       ← 7 perfiles YAML (LLM01/02/04/07/09, ASI01/05)
│   ├── pyrit/                       ← 3 scripts Python asíncronos (LLM01, DSGAI04, ASI01)
│   ├── laaf/                        ← Suite LAAF v2.0 LPCI (S1–S6 + generador de informes crosswalk)
│   └── ci/                          ← github-action.yml — plantilla CI/CD lista para usar
│
└── i18n/
    ├── WORKFLOW.md                  ← Guía para contribuyentes de traducción
    ├── es/                          ← Español (aceptando PRs)
    ├── fr/                          ← Francés (aceptando PRs)
    └── pt/                          ← Portugués (aceptando PRs)
```

---

## Informes de evaluación de brechas de cumplimiento

Genere evaluaciones de brechas específicas por marco de referencia desde la capa de datos en segundos:

```bash
node scripts/compliance-report.js                          # los 17 marcos de referencia → reports/
node scripts/compliance-report.js --framework "EU AI Act"  # un marco de referencia
node scripts/compliance-report.js --format csv             # compatible con Excel
node scripts/compliance-report.js --format json            # legible por máquina
node scripts/compliance-report.js --list-frameworks        # ver todas las opciones
```

Cada informe incluye: resumen ejecutivo, matriz de cobertura (entradas OWASP × controles), detalle por control con notas, y un plan de acción priorizado.

## LAAF v2.0 — Red-teaming LPCI

[LAAF v2.0](https://github.com/qorvexconsulting1/laaf-V2.0) está integrado como el tercer marco de evaluación junto con Garak y PyRIT. Cubre la superficie de ataque que las pruebas de inyección superficiales no detectan: persistencia en memoria, codificación en capas, reformulación semántica y ataques de ciclo de vida de 6 etapas.

```bash
pip install git+https://github.com/qorvexconsulting1/laaf-V2.0.git
export OPENAI_API_KEY=sk-...
bash evals/laaf/run_laaf.sh           # Suite completa S1–S6
laaf scan --target mock --dry-run     # No requiere clave API
```

| Etapa LAAF | OWASP | Umbral |
|---|---|---|
| S1 Reconocimiento | LLM07, LLM01 | 0% |
| S2 Inyección de capa lógica | LLM01, ASI01, DSGAI04 | 5% |
| S3 Ejecución de disparador | ASI01, ASI06, LLM06 | 0% |
| S4 Persistencia | ASI06, LLM06, DSGAI04 | 0% |
| S5 Evasión | LLM01, LLM02 | 10% |
| S6 Manipulación de trazas | DSGAI01, LLM07 | 0% |

Consulte `evals/laaf/README.md` para el crosswalk completo de vector de ataque LPCI → OWASP → MAESTRO.

---

## Rastreador de incidentes

20 incidentes reales y demostrados en investigación, cada uno mapeado a entradas OWASP y capas arquitectónicas MAESTRO:

```bash
node scripts/incidents-report.js                      # todos los incidentes → reports/incidents.md
node scripts/incidents-report.js --entry LLM01        # incidentes para una entrada específica
node scripts/incidents-report.js --layer L3           # incidentes que implican Agent Frameworks
node scripts/incidents-report.js --category real-world
node scripts/incidents-report.js --format csv         # exportación Excel
```

Roles de capa MAESTRO rastreados por incidente: **Origen** (donde comienza el ataque) · **Propagación** (cómo se propaga) · **Impacto** (donde se manifiesta el daño) · **Punto ciego** (donde falló la detección).

---

## Comience aquí — por rol

Encuentre su punto de entrada en menos de 60 segundos.

**Necesito cumplir con EU AI Act antes de agosto 2026**
→ Comience: [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) — obligaciones a nivel de artículo, exposición a multas, lista de verificación de cumplimiento
→ Luego: [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) si despliega agentes autónomos (Art. 14 supervisión humana)
→ Luego: [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) para el alcance del modelo GPAI y obligaciones de gobernanza de datos

**Estoy desplegando un agente de IA autónomo y necesito saber qué puede salir mal**
→ Comience: [CROSSREF.md](CROSSREF.md) — referencia cruzada maestra de los 41 IDs de vulnerabilidad
→ Luego: [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — modelo de amenazas arquitectónico (¿dónde se origina cada riesgo?)
→ Luego: [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — puntúe cada riesgo; la autonomía añade +1.79 de severidad promedio
→ Luego: [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — controles de identidad y credenciales

**Soy un auditor SOC 2 o profesional GRC preparando una evaluación de controles GenAI**
→ Comience: [LLM_SOC2.md](llm-top10/LLM_SOC2.md) — mapeo TSC para despliegues LLM en SaaS/nube
→ Luego: [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) — alcance de acción autónoma, criterios de integridad de procesamiento
→ Luego: [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — tarjeta de puntuación SAMM rellenable para evidenciar la completitud del programa

**Soy un ingeniero AppSec o red-teamer construyendo un plan de pruebas**
→ Comience: [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50 casos de prueba estructurados con criterios de aprobación y puertas CI/CD
→ Luego: [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — mapeo de TTPs del atacante con cuatro cadenas de ataque completas
→ Luego: [shared/RECIPES.md](shared/RECIPES.md) — 13 patrones Python funcionales para implementar los controles contra los que realiza pruebas

**Estoy asegurando IA desplegada en entornos OT/ICS (energía, servicios públicos, manufactura)**
→ Comience: [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) — modelo de zonas OT, controles SP 800-53, mapeo cruzado NERC CIP/AWIA/CMMC
→ Luego: [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) — calificaciones SL, modelo de zonas, diseño de interruptor de emergencia
→ Luego: [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — envenenamiento de corpus RAG en OT (escenario de manipulación de procedimientos de seguridad)

---

## Navegación rápida

**Cumplimiento con EU AI Act para agosto 2026**
→ [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) · [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) · [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md)

**Organización europea sujeta a NIS2**
→ [LLM_ENISA.md](llm-top10/LLM_ENISA.md) — Marco de referencia ENISA con guía de evaluación de incidentes NIS2 Artículo 23

**IA en entornos OT/ICS**
→ [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) · [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) · [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) · [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md)

**Desplegando agentes autónomos**
→ [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — gobernanza de identidad
→ [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) — certificación de gobernanza agéntica
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — puntuación de riesgos con prima de autonomía

**Modelado de amenazas de un sistema de IA agéntico antes de seleccionar controles**
→ [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — Enumeración de amenazas MAESTRO de siete capas con guía de sesión
→ [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) — Perspectiva de operaciones de datos MAESTRO para las 21 entradas DSGAI

**Extensión ISMS ISO 27001 para GenAI**
→ [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) · [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) · [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md)

**AIMS ISO 42001 para gobernanza de IA**
→ [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) · [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) — incluye tabla de evidencia de cumplimiento con EU AI Act

**Madurez del programa de seguridad**
→ [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — Hoja de ruta SAMM L1–L3 con tarjeta de puntuación rellenable

**Plan de pruebas de seguridad para IA agéntica**
→ [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50 casos de prueba estructurados, puertas de pre-despliegue, addendum OT

**Puntuación de registro de riesgos para IA agéntica**
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — puntuación de doble escenario supervisado vs autónomo, prima de autonomía promedio +1.79

**Perspectiva del atacante sobre riesgos GenAI**
→ [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — mapeo de técnicas ATLAS, cuatro cadenas de ruta de ataque
→ [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) — encadenamiento de técnicas agénticas

**Causas raíz CWE y CVEs confirmados**
→ [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — taxonomía de causa raíz, evidencia CVE, índice de referencia cruzada

**Código de implementación, no teoría de marcos de referencia**
→ [shared/RECIPES.md](shared/RECIPES.md) — 13 patrones de producción con Python funcional

**Todos los riesgos en las tres listas fuente**
→ [CROSSREF.md](CROSSREF.md) — referencia cruzada maestra

---

## Cobertura destacada

### Trilogía OT/ICS completa

El único mapeo públicamente disponible de las tres listas fuente GenAI de OWASP hacia ISA/IEC 62443 y NIST SP 800-82 Rev 3. Incluye ubicación en modelo de zonas, calificaciones de nivel de seguridad, referencias de Requisitos Fundamentales y Requisitos de Seguridad, escenarios de amenazas específicos de OT y listas de verificación de pre-despliegue para cada lista fuente.

El escenario de envenenamiento de corpus RAG en [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — un ataque de manipulación de procedimientos de seguridad que modifica intervalos de mantenimiento sin ningún acceso a la red OT — no existe en ningún otro lugar de la documentación pública.

### Modelado de amenazas de siete capas MAESTRO

[Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) y [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) son los únicos mapeos públicos de los riesgos GenAI de OWASP hacia el marco de referencia MAESTRO de la Cloud Security Alliance. A diferencia de todos los demás archivos en este repositorio — que mapean riesgos a controles — MAESTRO mapea cada riesgo a la **capa arquitectónica donde se origina**, indicándole qué equipo es responsable del problema y dónde en el sistema debe desplegarse la corrección.

Hallazgo clave del mapeo DSGAI: **L2 Operaciones de Datos es la capa de origen para el 52% de todas las entradas DSGAI**. Una organización que no trate los corpus RAG, almacenes de embeddings, pipelines de entrenamiento y sistemas de memoria como infraestructura crítica de seguridad está insuficientemente defendida contra la mayoría del panorama de amenazas de seguridad de datos GenAI.

### Prima de autonomía agéntica

[Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) cuantifica lo que cuesta en riesgo eliminar la supervisión humana: un promedio de **+1.79 puntos de severidad AIVSS** en las 10 entradas agénticas. Eliminar la supervisión humana convierte 7 de 10 entradas de Alta a Crítica — el caso cuantitativo para la supervisión humana obligatoria bajo el Artículo 14 de EU AI Act.

### Cobertura completa de identidad agéntica

[Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) mapea cada entrada NHI Top 10 a cada entrada ASI — el único documento público que traduce los riesgos de seguridad agéntica en los controles NHI que los equipos de IAM ya operan.

### Tarjeta de puntuación de madurez SAMM

[LLM_SAMM.md](llm-top10/LLM_SAMM.md) incluye una tarjeta de puntuación de madurez rellenable con niveles mínimos viables por práctica SAMM para cualquier despliegue LLM en producción — el artefacto que los líderes de programas de seguridad utilizan para informar al liderazgo de ingeniería sobre dónde se encuentra el programa y qué mejorar a continuación.

### Recetas de implementación para producción

[shared/RECIPES.md](shared/RECIPES.md) contiene 13 patrones de seguridad listos para producción con Python funcional: recuperación RAG con control de acceso, verificación de integridad de descriptores MCP, emisión de credenciales JIT, interruptor de emergencia OT, monitorización de línea base conductual, contención de cascada y puertas de confirmación humana.

---

## Contribuciones

Las contribuciones son bienvenidas — nuevos mapeos de marcos de referencia, controles actualizados, nuevas recetas de implementación, traducciones y entradas de herramientas adicionales.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para la plantilla de archivo, proceso de PR y directrices de contribución. Todos los contribuyentes están listados en el CHANGELOG.

---

## Licencia

[Creative Commons Attribution-ShareAlike 4.0 International](LICENSE)

Libre para compartir y adaptar para cualquier propósito, incluido el uso comercial, con la atribución adecuada y distribución bajo la misma licencia.

---

## Agradecimientos

Creado y mantenido por **[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)** y la [Iniciativa de Seguridad de Datos GenAI de OWASP](https://genai.owasp.org).

Construido sobre el trabajo de los equipos de proyectos OWASP LLM Top 10, OWASP Agentic Top 10, OWASP GenAI Data Security, OWASP NHI Top 10 y OWASP SAMM.

Agradecimiento especial a [Ken Huang](https://github.com/kenhuangus) (Cloud Security Alliance) por el marco de referencia MAESTRO y sus contribuciones al OWASP LLM Top 10.

---

*[genai.owasp.org](https://genai.owasp.org) · [CC BY-SA 4.0](LICENSE)*
