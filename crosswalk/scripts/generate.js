#!/usr/bin/env node
/**
 * generate.js — Parse mapping Markdown files → emit data/entries/<ID>.json
 *
 * Usage:
 *   node scripts/generate.js            # generate all 41 entries
 *   node scripts/generate.js --dry-run  # parse + validate, no writes
 *   node scripts/generate.js --id LLM01 # generate a single entry
 *
 * Output: data/entries/LLM01.json … DSGAI21.json (41 files)
 */

'use strict';

const fs   = require('fs');
const path = require('path');

const ROOT        = path.resolve(__dirname, '..');
const ENTRIES_DIR = path.join(ROOT, 'data', 'entries');

const DRY_RUN    = process.argv.includes('--dry-run');
const SINGLE_ID  = (() => { const i = process.argv.indexOf('--id'); return i !== -1 ? process.argv[i + 1] : null; })();

// ─── Vulnerability catalog ────────────────────────────────────────────────────

const VULNERABILITIES = {
  // LLM Top 10 2025
  LLM01: { name: 'Prompt Injection',                         source_list: 'LLM-Top10-2025',    severity: 'Critical' },
  LLM02: { name: 'Sensitive Information Disclosure',         source_list: 'LLM-Top10-2025',    severity: 'High'     },
  LLM03: { name: 'Supply Chain Vulnerabilities',             source_list: 'LLM-Top10-2025',    severity: 'High'     },
  LLM04: { name: 'Data and Model Poisoning',                 source_list: 'LLM-Top10-2025',    severity: 'Critical' },
  LLM05: { name: 'Insecure Output Handling',                 source_list: 'LLM-Top10-2025',    severity: 'High'     },
  LLM06: { name: 'Excessive Agency',                         source_list: 'LLM-Top10-2025',    severity: 'High'     },
  LLM07: { name: 'System Prompt Leakage',                    source_list: 'LLM-Top10-2025',    severity: 'High'     },
  LLM08: { name: 'Vector and Embedding Weaknesses',          source_list: 'LLM-Top10-2025',    severity: 'Medium'   },
  LLM09: { name: 'Misinformation',                           source_list: 'LLM-Top10-2025',    severity: 'Medium'   },
  LLM10: { name: 'Unbounded Consumption',                    source_list: 'LLM-Top10-2025',    severity: 'Medium'   },

  // Agentic Top 10 2026
  ASI01: { name: 'Agent Goal Hijack',                        source_list: 'Agentic-Top10-2026', severity: 'Critical' },
  ASI02: { name: 'Tool Misuse and Exploitation',             source_list: 'Agentic-Top10-2026', severity: 'Critical' },
  ASI03: { name: 'Identity and Privilege Abuse',             source_list: 'Agentic-Top10-2026', severity: 'Critical' },
  ASI04: { name: 'Agentic Supply Chain',                     source_list: 'Agentic-Top10-2026', severity: 'High'     },
  ASI05: { name: 'Unexpected Code Execution',                source_list: 'Agentic-Top10-2026', severity: 'Critical' },
  ASI06: { name: 'Memory and Context Poisoning',             source_list: 'Agentic-Top10-2026', severity: 'High'     },
  ASI07: { name: 'Insecure Inter-Agent Communications',      source_list: 'Agentic-Top10-2026', severity: 'High'     },
  ASI08: { name: 'Cascading Agent Failures',                 source_list: 'Agentic-Top10-2026', severity: 'Critical' },
  ASI09: { name: 'Human-Agent Trust Exploitation',           source_list: 'Agentic-Top10-2026', severity: 'High'     },
  ASI10: { name: 'Rogue Agents',                             source_list: 'Agentic-Top10-2026', severity: 'Critical' },

  // DSGAI 2026
  DSGAI01: { name: 'Sensitive Data Leakage',                 source_list: 'DSGAI-2026', severity: 'Critical' },
  DSGAI02: { name: 'Agent Identity and Credential Exposure', source_list: 'DSGAI-2026', severity: 'Critical' },
  DSGAI03: { name: 'Shadow AI and Unsanctioned Data Flows',  source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI04: { name: 'Data Model and Artifact Poisoning',      source_list: 'DSGAI-2026', severity: 'Critical' },
  DSGAI05: { name: 'Data Integrity and Validation Failures', source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI06: { name: 'Tool Plugin and Agent Data Exchange',    source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI07: { name: 'Data Governance and Lifecycle',          source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI08: { name: 'Non-Compliance and Regulatory Violations', source_list: 'DSGAI-2026', severity: 'High'   },
  DSGAI09: { name: 'Multimodal Cross-Channel Leakage',       source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI10: { name: 'Synthetic Data and Anonymization Pitfalls', source_list: 'DSGAI-2026', severity: 'Medium' },
  DSGAI11: { name: 'Cross-Context Conversation Bleed',       source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI12: { name: 'Unsafe Natural Language Data Gateways',  source_list: 'DSGAI-2026', severity: 'Critical' },
  DSGAI13: { name: 'Vector Store Platform Security',         source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI14: { name: 'Excessive Telemetry and Monitoring Leakage', source_list: 'DSGAI-2026', severity: 'High' },
  DSGAI15: { name: 'Over-Broad Context Windows',             source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI16: { name: 'Endpoint and Browser Overreach',         source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI17: { name: 'Data Availability and Resilience Failures', source_list: 'DSGAI-2026', severity: 'High'  },
  DSGAI18: { name: 'Inference and Data Reconstruction',      source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI19: { name: 'Human-in-Loop and Labeler Overexposure', source_list: 'DSGAI-2026', severity: 'Medium'   },
  DSGAI20: { name: 'Model Exfiltration and IP Replication',  source_list: 'DSGAI-2026', severity: 'High'     },
  DSGAI21: { name: 'Disinformation via Data Poisoning',      source_list: 'DSGAI-2026', severity: 'High'     },
};

// AIVSS scores for agentic entries (from Agentic_AIVSS.md)
// aivss_score = autonomous (worst-case) score
const AIVSS_SCORES = {
  ASI01: 9.8, ASI02: 9.6, ASI03: 9.3, ASI04: 8.4, ASI05: 9.9,
  ASI06: 8.7, ASI07: 8.2, ASI08: 9.1, ASI09: 7.3, ASI10: 9.7,
};

const LLM_IDS    = Object.keys(VULNERABILITIES).filter(k => k.startsWith('LLM'));
const ASI_IDS    = Object.keys(VULNERABILITIES).filter(k => k.startsWith('ASI'));
const DSGAI_IDS  = Object.keys(VULNERABILITIES).filter(k => k.startsWith('DSGAI'));

// ─── Framework file catalog ───────────────────────────────────────────────────
// Agentic_AIVSS is a scoring file, not a standard mapping — handled separately.

const FRAMEWORK_FILES = [
  // LLM Top 10
  { rel: 'llm-top10/LLM_MITREATLAS.md',  framework: 'MITRE ATLAS',              ids: LLM_IDS },
  { rel: 'llm-top10/LLM_NISTAIRMF.md',   framework: 'NIST AI RMF 1.0',          ids: LLM_IDS },
  { rel: 'llm-top10/LLM_EUAIAct.md',     framework: 'EU AI Act',                ids: LLM_IDS },
  { rel: 'llm-top10/LLM_ISO27001.md',    framework: 'ISO/IEC 27001:2022',        ids: LLM_IDS },
  { rel: 'llm-top10/LLM_ISO42001.md',    framework: 'ISO/IEC 42001:2023',        ids: LLM_IDS },
  { rel: 'llm-top10/LLM_CISControls.md', framework: 'CIS Controls v8.1',        ids: LLM_IDS },
  { rel: 'llm-top10/LLM_ASVS.md',        framework: 'OWASP ASVS 4.0.3',         ids: LLM_IDS },
  { rel: 'llm-top10/LLM_ISA62443.md',    framework: 'ISA/IEC 62443',             ids: LLM_IDS },
  { rel: 'llm-top10/LLM_NISTSP80082.md', framework: 'NIST SP 800-82 Rev 3',     ids: LLM_IDS },
  { rel: 'llm-top10/LLM_NISTCSF2.md',    framework: 'NIST CSF 2.0',             ids: LLM_IDS },
  { rel: 'llm-top10/LLM_SOC2.md',        framework: 'SOC 2',                    ids: LLM_IDS },
  { rel: 'llm-top10/LLM_PCIDSS.md',      framework: 'PCI DSS v4.0',             ids: LLM_IDS },
  { rel: 'llm-top10/LLM_ENISA.md',       framework: 'ENISA Multilayer Framework', ids: LLM_IDS },
  { rel: 'llm-top10/LLM_SAMM.md',        framework: 'OWASP SAMM v2.0',          ids: LLM_IDS },
  { rel: 'llm-top10/LLM_STRIDE.md',      framework: 'STRIDE',                   ids: LLM_IDS },
  { rel: 'llm-top10/LLM_CWE_CVE.md',     framework: 'CWE/CVE',                  ids: LLM_IDS },
  { rel: 'llm-top10/LLM_AITG.md',        framework: 'OWASP AI Testing Guide',   ids: LLM_IDS },
  { rel: 'llm-top10/LLM_MAESTRO.md',     framework: 'MAESTRO',                  ids: LLM_IDS },
  { rel: 'llm-top10/LLM_AIUC1.md',       framework: 'AIUC-1',                   ids: LLM_IDS },
  { rel: 'llm-top10/LLM_NHI.md',         framework: 'OWASP NHI Top 10',         ids: LLM_IDS },
  { rel: 'llm-top10/LLM_SP800218A.md',  framework: 'NIST SP 800-218A',         ids: LLM_IDS },
  { rel: 'llm-top10/LLM_FedRAMP.md',   framework: 'FedRAMP',                 ids: LLM_IDS },
  { rel: 'llm-top10/LLM_DORA.md',      framework: 'DORA',                    ids: LLM_IDS },

  // Agentic Top 10
  { rel: 'agentic-top10/Agentic_MITREATLAS.md',   framework: 'MITRE ATLAS',              ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_NISTAIRMF.md',    framework: 'NIST AI RMF 1.0',          ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_EUAIAct.md',      framework: 'EU AI Act',                ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_ISO27001.md',      framework: 'ISO/IEC 27001:2022',       ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_ISO42001.md',      framework: 'ISO/IEC 42001:2023',       ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_CISControls.md',   framework: 'CIS Controls v8.1',        ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_ASVS.md',          framework: 'OWASP ASVS 4.0.3',        ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_ISA62443.md',      framework: 'ISA/IEC 62443',            ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_NISTSP80082.md',   framework: 'NIST SP 800-82 Rev 3',    ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_NISTCSF2.md',      framework: 'NIST CSF 2.0',            ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_SOC2.md',           framework: 'SOC 2',                   ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_PCIDSS.md',         framework: 'PCI DSS v4.0',            ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_ENISA.md',          framework: 'ENISA Multilayer Framework', ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_SAMM.md',           framework: 'OWASP SAMM v2.0',         ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_CWE_CVE.md',        framework: 'CWE/CVE',                 ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_AITG.md',           framework: 'OWASP AI Testing Guide',  ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_MAESTRO.md',        framework: 'MAESTRO',                 ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_AIUC1.md',           framework: 'AIUC-1',                  ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_OWASP_NHI.md',      framework: 'OWASP NHI Top 10',        ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_SP800218A.md',     framework: 'NIST SP 800-218A',        ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_FedRAMP.md',      framework: 'FedRAMP',                ids: ASI_IDS },
  { rel: 'agentic-top10/Agentic_DORA.md',         framework: 'DORA',                   ids: ASI_IDS },

  // DSGAI 2026
  { rel: 'dsgai-2026/DSGAI_MITREATLAS.md',  framework: 'MITRE ATLAS',              ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_NISTAIRMF.md',   framework: 'NIST AI RMF 1.0',          ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_EUAIAct.md',     framework: 'EU AI Act',                ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_ISO27001.md',    framework: 'ISO/IEC 27001:2022',        ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_ISO42001.md',    framework: 'ISO/IEC 42001:2023',        ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_CISControls.md', framework: 'CIS Controls v8.1',        ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_ASVS.md',        framework: 'OWASP ASVS 4.0.3',         ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_ISA62443.md',    framework: 'ISA/IEC 62443',             ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_NISTSP80082.md', framework: 'NIST SP 800-82 Rev 3',     ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_NISTCSF2.md',    framework: 'NIST CSF 2.0',             ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_SOC2.md',        framework: 'SOC 2',                    ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_PCIDSS.md',      framework: 'PCI DSS v4.0',             ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_ENISA.md',       framework: 'ENISA Multilayer Framework', ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_SAMM.md',        framework: 'OWASP SAMM v2.0',          ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_CWE_CVE.md',     framework: 'CWE/CVE',                  ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_MAESTRO.md',     framework: 'MAESTRO',                  ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_AIUC1.md',       framework: 'AIUC-1',                   ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_NHI.md',         framework: 'OWASP NHI Top 10',         ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_SP800218A.md',  framework: 'NIST SP 800-218A',         ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_FedRAMP.md',   framework: 'FedRAMP',                 ids: DSGAI_IDS },
  { rel: 'dsgai-2026/DSGAI_DORA.md',      framework: 'DORA',                    ids: DSGAI_IDS },
];

// ─── Audience role mapping ────────────────────────────────────────────────────

const VALID_AUDIENCES = new Set([
  'developer', 'security-engineer', 'auditor', 'ciso',
  'red-teamer', 'data-engineer', 'ml-engineer', 'ot-engineer', 'compliance',
]);

const ROLE_PATTERNS = [
  [/red.?team/i,          'red-teamer'],
  [/developer/i,          'developer'],
  [/security.?engineer/i, 'security-engineer'],
  [/\bciso\b/i,           'ciso'],
  [/auditor|certif/i,     'auditor'],
  [/compliance|grc/i,     'compliance'],
  [/data.?engineer/i,     'data-engineer'],
  [/ml.?engineer|ai.?engineer|machine.?learn/i, 'ml-engineer'],
  [/ot.?engineer|ics|scada/i, 'ot-engineer'],
  [/risk.?manag|programme.?lead/i, 'ciso'],
  [/threat.?model|soc.?anal|incident/i, 'security-engineer'],
  [/appsec/i,             'security-engineer'],
];

// ─── Parser utilities ─────────────────────────────────────────────────────────

/** Split markdown table row → trimmed cell array (strips leading/trailing empty cells) */
function splitRow(row) {
  return row.split('|').slice(1, -1).map(c => c.trim());
}

/** Extract control ID and URL from a cell that may contain [text](url) or plain text */
function extractIdAndUrl(cell) {
  const link = cell.match(/\[([^\]]+)\]\(([^)]+)\)/);
  if (link) return { text: link[1].trim(), url: link[2].trim() };
  return { text: cell.replace(/\*\*/g, '').trim(), url: null };
}

/** Determine if a string looks like a framework control ID */
function looksLikeId(str) {
  return /^[A-Za-z0-9][A-Za-z0-9.\-:/]+$/.test(str) && str.length <= 40 && !/\s/.test(str);
}

/**
 * Parse the quick-reference summary table.
 * Returns { [id]: { tier, scope, severity } }
 */
function parseQuickRef(content) {
  const result = {};

  // Find the quick-reference summary section
  const sectionMatch = content.match(/##\s+Quick.?reference\s+summary\s*\n([\s\S]*?)(?=\n##\s|\n---\s*\n##)/i);
  if (!sectionMatch) return result;

  const rows = sectionMatch[1].split('\n').filter(l => l.trim().startsWith('|'));
  if (rows.length < 3) return result; // need header + separator + data

  for (const row of rows.slice(2)) {
    const cols = splitRow(row);
    if (!cols.length) continue;

    const idMatch = cols[0].match(/^(LLM|ASI|DSGAI)\d{1,2}/i);
    if (!idMatch) continue;
    const id = idMatch[0].toUpperCase();

    // Severity: look for the Critical/High/Medium/Low cell
    const severityCol = cols.find(c => /^(Critical|High|Medium|Low)$/i.test(c.replace(/\*\*/g, '').trim()));
    const severity = severityCol ? severityCol.replace(/\*\*/g, '').trim() : null;

    // Tier: look for a cell containing Foundational / Hardening / Advanced
    const tierCol = cols.find(c => /foundational|hardening|advanced/i.test(c));
    let tier = 'Foundational';
    if (tierCol) {
      if (/^hardening/i.test(tierCol)) tier = 'Hardening';
      else if (/^advanced/i.test(tierCol)) tier = 'Advanced';
    }

    // Scope: look for Buy/Build/Both cell
    const scopeCol = cols.find(c => /^(build|buy|both)$/i.test(c.replace(/\*\*/g, '').trim()));
    const scope = scopeCol ? scopeCol.replace(/\*\*/g, '').trim() : 'Both';
    const scopeNorm = scope.charAt(0).toUpperCase() + scope.slice(1).toLowerCase();

    result[id] = { tier, scope: scopeNorm, severity };
  }

  return result;
}

/**
 * Extract the body of a vulnerability section (### IDxx … until next ### or end).
 */
function extractSection(content, id) {
  const lines = content.split('\n');
  const idRegex = new RegExp(`^###\\s+${id}\\b`, 'i');
  let start = -1;

  for (let i = 0; i < lines.length; i++) {
    if (idRegex.test(lines[i])) {
      start = i + 1;
    } else if (start !== -1 && /^###\s/.test(lines[i])) {
      return lines.slice(start, i).join('\n');
    }
  }

  return start !== -1 ? lines.slice(start).join('\n') : null;
}

/**
 * Find all #### subsections in a section body.
 * Returns { heading: string, body: string }[]
 */
function extractSubsections(sectionBody) {
  const lines = sectionBody.split('\n');
  const subsections = [];
  let current = null;

  for (const line of lines) {
    if (/^####\s+/.test(line)) {
      if (current) subsections.push(current);
      current = { heading: line.replace(/^####\s+/, '').trim(), body: '' };
    } else if (current) {
      current.body += line + '\n';
    }
  }
  if (current) subsections.push(current);
  return subsections;
}

/**
 * Parse a markdown table from text.
 * Returns array of column-arrays (one per data row, skipping header + separator).
 */
function parseTable(text) {
  const rows = text.split('\n').filter(l => l.trim().startsWith('|'));
  if (rows.length < 3) return [];
  return rows.slice(2).map(splitRow).filter(cols => cols.length >= 2);
}

/**
 * Parse MAESTRO-style bold-header layer analysis into mappings.
 * Pattern: **L1 — Foundation Models (originating)**
 */
function parseMaestroLayers(sectionBody, frameworkName, qr) {
  const mappings = [];
  // Match **L1 — Layer Name (role)**  or  **L1 — Layer Name**
  const layerRe = /\*\*(L\d)\s*[—\-–]+\s*([^*(]+?)(?:\s*\([^)]*\))?\*\*/g;
  const seen = new Set();
  let m;
  while ((m = layerRe.exec(sectionBody)) !== null) {
    const layerId   = m[1].trim();
    const layerName = m[2].trim();
    const key       = `${layerId}:${layerName}`;
    if (seen.has(key)) continue;
    seen.add(key);
    mappings.push({
      framework:    frameworkName,
      control_id:   layerId,
      control_name: layerName,
      tier:         qr?.tier  ?? 'Foundational',
      scope:        qr?.scope ?? 'Both',
    });
  }
  return mappings;
}

/**
 * Parse framework control mappings from a vulnerability section body.
 * Returns Mapping[]
 */
function parseControlTable(sectionBody, frameworkName, qr) {
  const subsections = extractSubsections(sectionBody);

  // Find the first subsection whose heading is NOT "Mitigations", "Tools", "Cross-ref"
  const mappingSection = subsections.find(s =>
    !/^(mitigations?|tools?|cross.?ref|maturity|roadmap|implementation|scoring|tier|three.?tier)/i.test(s.heading)
  );

  // MAESTRO files use bold layer headers instead of tables — detect and handle
  if (frameworkName === 'MAESTRO' || (mappingSection && /maestro/i.test(mappingSection.heading))) {
    const body = mappingSection ? mappingSection.body : sectionBody;
    const layers = parseMaestroLayers(body, frameworkName, qr);
    if (layers.length) return layers;
  }

  if (!mappingSection) return [];

  const rows = parseTable(mappingSection.body);
  if (!rows.length) return [];

  const mappings = [];

  for (const cols of rows) {
    if (cols.length < 2) continue;

    const col0 = cols[0];
    const col1 = cols[1];
    const lastCol = cols[cols.length - 1];

    // Extract control name and ID
    let controlName = '';
    let controlId   = '';
    let controlUrl  = null;

    const id1 = extractIdAndUrl(col1);
    const id0 = extractIdAndUrl(col0);

    if (id1.url) {
      // col1 is a link — ID is the link text, name is col0 text
      controlId   = id1.text;
      controlName = id0.text;
      controlUrl  = id1.url;
    } else if (id0.url) {
      // col0 is a link — name + url from col0, try col1 as ID
      controlName = id0.text;
      controlUrl  = id0.url;
      controlId   = looksLikeId(id1.text) ? id1.text : id0.text;
    } else if (looksLikeId(id1.text)) {
      // col1 is a plain control ID
      controlId   = id1.text;
      controlName = id0.text;
    } else {
      // Try to extract CODE from col0 pattern "Name (CODE)"
      const codeMatch = col0.match(/^(.*?)\s*\(([A-Z][A-Z0-9\-]{1,12})\)\s*$/);
      if (codeMatch) {
        controlName = codeMatch[1].trim();
        controlId   = codeMatch[2];
      } else {
        // Fall back: use col1 as ID
        controlId   = id1.text || id0.text;
        controlName = id0.text;
      }
    }

    // Skip separator / header rows that leaked through
    if (!controlId || /^[-:=]+$/.test(controlId) || controlId === controlName && !controlId) continue;
    // Skip rows where the ID is clearly a column heading word
    if (/^(technique|control|practice|category|domain|function|id|name|risk|measure)$/i.test(controlId)) continue;

    const mapping = {
      framework:    frameworkName,
      control_id:   controlId,
      control_name: controlName || controlId,
      tier:         qr?.tier  ?? 'Foundational',
      scope:        qr?.scope ?? 'Both',
    };

    if (controlUrl) mapping.url = controlUrl;

    // Notes: last column if it differs from the ID/name columns and has useful length
    if (cols.length >= 3 && lastCol && lastCol !== controlId && lastCol !== controlName && lastCol.length > 5) {
      mapping.notes = lastCol.replace(/\s+/g, ' ').trim().substring(0, 350);
    }

    mappings.push(mapping);
  }

  return mappings;
}

/**
 * Parse the Tools subsection.
 * Returns Tool[]
 */
function parseTools(sectionBody) {
  const subsections = extractSubsections(sectionBody);
  const toolsSection = subsections.find(s => /^tools?/i.test(s.heading));
  if (!toolsSection) return [];

  const rows = parseTable(toolsSection.body);
  const tools = [];
  const seen  = new Set();

  for (const cols of rows) {
    if (!cols.length) continue;

    const name = extractIdAndUrl(cols[0]).text;
    if (!name || seen.has(name.toLowerCase())) continue;

    // Type: second column, or infer from name
    const typeRaw = (cols[1] || '').toLowerCase();
    const type = typeRaw.includes('commercial') ? 'commercial'
               : typeRaw.includes('both')       ? 'both'
               : 'open-source';

    // URL: look for https:// in any column
    let url = null;
    for (const col of cols) {
      const u = col.match(/https?:\/\/[^\s|)>]+/);
      if (u) { url = u[0].replace(/[)>.,]+$/, ''); break; }
    }

    seen.add(name.toLowerCase());
    const tool = { name, type };
    if (url) tool.url = url;
    tools.push(tool);
  }

  return tools;
}

/**
 * Parse Cross-references subsection.
 * Returns { llm_top10?: string[], agentic_top10?: string[], dsgai_2026?: string[] }
 */
function parseCrossRefs(sectionBody) {
  const subsections = extractSubsections(sectionBody);
  const xref = subsections.find(s => /cross.?ref/i.test(s.heading));
  if (!xref) return {};

  const text = xref.body;
  const llm     = [...new Set(text.match(/\bLLM\d{2}\b/g)    || [])];
  const agentic = [...new Set(text.match(/\bASI\d{2}\b/g)     || [])];
  const dsgai   = [...new Set(text.match(/\bDSGAI\d{2}\b/g)   || [])];

  const refs = {};
  if (llm.length)     refs.llm_top10     = llm;
  if (agentic.length) refs.agentic_top10 = agentic;
  if (dsgai.length)   refs.dsgai_2026    = dsgai;
  return refs;
}

/**
 * Parse the audience from the file-level ## Audience tags section.
 * Returns string[] of valid audience enum values.
 */
function parseAudience(content) {
  const match = content.match(/##\s+(?:audience\s+tags?|target\s+audience)\s*\n([\s\S]*?)(?=\n---|\n##)/i);
  if (!match) return [];

  const audiences = new Set();
  const lines = match[1].split('\n').filter(l => l.trim().startsWith('-'));

  for (const line of lines) {
    const boldMatch = line.match(/\*\*([^*]+)\*\*/);
    if (!boldMatch) continue;
    const role = boldMatch[1].toLowerCase();
    for (const [pat, val] of ROLE_PATTERNS) {
      if (pat.test(role)) { audiences.add(val); break; }
    }
  }

  return [...audiences].filter(a => VALID_AUDIENCES.has(a));
}

// ─── Merge helpers ────────────────────────────────────────────────────────────

function mergeTools(existing, incoming) {
  const seen = new Set(existing.map(t => t.name.toLowerCase()));
  for (const t of incoming) {
    if (!seen.has(t.name.toLowerCase())) {
      existing.push(t);
      seen.add(t.name.toLowerCase());
    }
  }
}

function mergeCrossRefs(existing, incoming) {
  for (const [key, ids] of Object.entries(incoming)) {
    existing[key] = [...new Set([...(existing[key] || []), ...ids])];
  }
}

function mergeTools(existing, supplement) {
  // Append supplemental tools not already present (match by name)
  const names = new Set(existing.map(t => t.name));
  const added = supplement.filter(t => !names.has(t.name));
  return [...existing, ...added];
}

function mergeAudiences(existing, incoming) {
  const s = new Set(existing);
  for (const a of incoming) s.add(a);
  return [...s];
}

// ─── Main ─────────────────────────────────────────────────────────────────────

function main() {
  console.log(`\nGenAI Security Crosswalk — generate.js${DRY_RUN ? ' [DRY RUN]' : ''}`);
  console.log('─'.repeat(50));

  // Load incidents index from data/incidents.json if available
  const incidentsFile = path.join(ROOT, 'data', 'incidents.json');
  const incidentsByEntry = {};   // entryId -> [{name, url, year, incident_id}]
  if (fs.existsSync(incidentsFile)) {
    const incDb = JSON.parse(fs.readFileSync(incidentsFile, 'utf8'));
    for (const inc of incDb.incidents) {
      for (const eid of (inc.owasp_entries || [])) {
        if (!incidentsByEntry[eid]) incidentsByEntry[eid] = [];
        incidentsByEntry[eid].push({
          name:        inc.title,
          url:         'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk/blob/main/data/incidents.json',
          year:        inc.year,
          incident_id: inc.id,
        });
      }
    }
    console.log(`  Loaded incidents: ${incDb.incidents.length} entries from data/incidents.json`);
  }

  // Load supplemental tools from data/tools-supplement.json if available
  const toolsSupplementFile = path.join(ROOT, 'data', 'tools-supplement.json');
  const toolsSupplement = {};   // entryId -> Tool[]
  if (fs.existsSync(toolsSupplementFile)) {
    const ts = JSON.parse(fs.readFileSync(toolsSupplementFile, 'utf8'));
    for (const [eid, tools] of Object.entries(ts.tools || {})) {
      toolsSupplement[eid] = tools;
    }
    const count = Object.values(ts.tools || {}).reduce((n, t) => n + t.length, 0);
    console.log(`  Loaded tools-supplement: ${count} tool entries from data/tools-supplement.json`);
  }

  // Target IDs
  const targetIds = SINGLE_ID
    ? [SINGLE_ID.toUpperCase()]
    : Object.keys(VULNERABILITIES);

  // Initialise accumulator per ID
  const acc = {};
  for (const id of targetIds) {
    if (!VULNERABILITIES[id]) { console.error(`Unknown ID: ${id}`); process.exit(1); }
    acc[id] = {
      mappings:   [],
      tools:      [],
      crossrefs:  {},
      audiences:  [],
    };
  }

  // Process each framework file
  let filesProcessed = 0;
  for (const { rel, framework, ids } of FRAMEWORK_FILES) {
    const filePath = path.join(ROOT, rel);
    if (!fs.existsSync(filePath)) {
      console.warn(`  SKIP (missing): ${rel}`);
      continue;
    }

    const content = fs.readFileSync(filePath, 'utf8');
    const quickRef = parseQuickRef(content);
    const fileAudience = parseAudience(content);

    let extracted = 0;
    for (const id of ids) {
      if (!acc[id]) continue; // not in target set

      const section = extractSection(content, id);
      if (!section) continue;

      const qr = quickRef[id];

      const mappings = parseControlTable(section, framework, qr);
      const tools    = parseTools(section);
      const xrefs    = parseCrossRefs(section);

      acc[id].mappings.push(...mappings);
      acc[id].tools = mergeTools(acc[id].tools, tools);
      mergeCrossRefs(acc[id].crossrefs, xrefs);
      acc[id].audiences = mergeAudiences(acc[id].audiences, fileAudience);

      if (mappings.length) extracted++;
    }

    console.log(`  [${framework.padEnd(30)}]  ${String(extracted).padStart(2)} / ${ids.length} entries extracted`);
    filesProcessed++;
  }

  console.log(`\n${'─'.repeat(50)}`);
  console.log(`Parsed ${filesProcessed} framework files.`);

  // Write JSON entries
  if (!DRY_RUN) {
    fs.mkdirSync(ENTRIES_DIR, { recursive: true });
  }

  let written = 0;
  let warnings = 0;
  const allEntries = [];

  for (const id of targetIds) {
    const vuln = VULNERABILITIES[id];
    const data = acc[id];

    // Remove self-references from crossrefs
    for (const list of Object.values(data.crossrefs)) {
      const idx = list.indexOf(id);
      if (idx !== -1) list.splice(idx, 1);
    }
    // Remove empty crossref arrays
    for (const key of Object.keys(data.crossrefs)) {
      if (!data.crossrefs[key].length) delete data.crossrefs[key];
    }

    const entry = {
      id,
      name:        vuln.name,
      source_list: vuln.source_list,
      version:     '2026-Q1',
      severity:    vuln.severity,
      aivss_score: AIVSS_SCORES[id] ?? null,
      audience:    data.audiences.length ? data.audiences : defaultAudience(vuln.source_list),
      mappings:    data.mappings,
      tools:       mergeTools(data.tools, toolsSupplement[id] || []),
      incidents:   incidentsByEntry[id] || [],
      crossrefs:   data.crossrefs,
      changelog: [
        {
          date:    '2026-03-27',
          version: '1.0.0',
          change:  `Initial entry — generated from GenAI Security Crosswalk v1.5.1 mapping files`,
          author:  'emmanuelgjr',
        },
      ],
    };

    if (!data.mappings.length) {
      console.warn(`  WARN: ${id} — no mappings extracted`);
      warnings++;
    }

    const outPath = path.join(ENTRIES_DIR, `${id}.json`);
    const json    = JSON.stringify(entry, null, 2);

    if (DRY_RUN) {
      console.log(`  [dry-run] Would write ${outPath} (${data.mappings.length} mappings, ${data.tools.length} tools)`);
    } else {
      fs.writeFileSync(outPath, json, 'utf8');
      written++;
    }

    allEntries.push(entry);
  }

  // Write bundled site data for GitHub Pages query interface
  if (!DRY_RUN && !SINGLE_ID) {
    const docsDir = path.join(ROOT, 'docs');
    fs.mkdirSync(docsDir, { recursive: true });
    const siteDataPath = path.join(docsDir, 'data.js');
    const siteData = [
      `// Auto-generated by scripts/generate.js — do not edit manually`,
      `// Source: GenAI Security Crosswalk v1.5.2`,
      `// Generated: ${new Date().toISOString().split('T')[0]}`,
      `// Entries: ${allEntries.length}`,
      `window.CROSSWALK_DATA = ${JSON.stringify(allEntries, null, 2)};`,
    ].join('\n');
    fs.writeFileSync(siteDataPath, siteData, 'utf8');
    console.log(`Written docs/data.js (${allEntries.length} entries bundled for site)`);

    // ── Build backlink index: framework control_id → OWASP entries ──
    const backlinks = {};
    allEntries.forEach(entry => {
      (entry.mappings || []).forEach(m => {
        const key = m.framework + '::' + m.control_id;
        if (!backlinks[key]) {
          backlinks[key] = {
            framework: m.framework,
            control_id: m.control_id,
            control_name: m.control_name,
            entries: []
          };
        }
        // Avoid duplicates
        if (!backlinks[key].entries.some(e => e.id === entry.id)) {
          backlinks[key].entries.push({
            id: entry.id,
            name: entry.name,
            source_list: entry.source_list,
            severity: entry.severity,
            tier: m.tier,
            scope: m.scope,
            notes: m.notes || null
          });
        }
      });
    });
    const backlinksArray = Object.values(backlinks).sort((a, b) => {
      if (a.framework !== b.framework) return a.framework.localeCompare(b.framework);
      return a.control_id.localeCompare(b.control_id);
    });
    const backlinksPath = path.join(ROOT, 'data', 'backlinks.json');
    fs.writeFileSync(backlinksPath, JSON.stringify(backlinksArray, null, 2), 'utf8');
    console.log(`Written data/backlinks.json (${backlinksArray.length} control backlinks)`);

    // ── Bundle backlinks for site ──
    const siteBacklinksPath = path.join(docsDir, 'backlinks.js');
    const siteBacklinks = [
      `// Auto-generated by scripts/generate.js — do not edit manually`,
      `// Generated: ${new Date().toISOString().split('T')[0]}`,
      `// Backlinks: ${backlinksArray.length}`,
      `window.CROSSWALK_BACKLINKS = ${JSON.stringify(backlinksArray, null, 2)};`,
    ].join('\n');
    fs.writeFileSync(siteBacklinksPath, siteBacklinks, 'utf8');
    console.log(`Written docs/backlinks.js (${backlinksArray.length} backlinks bundled for site)`);

    // ── Bundle framework registry for site ──
    const fwDir = path.join(ROOT, 'data', 'frameworks');
    const fwRegistry = [];
    if (fs.existsSync(fwDir)) {
      const fwFiles = fs.readdirSync(fwDir).filter(f => f.endsWith('.json'));
      fwFiles.forEach(f => {
        try {
          const fw = JSON.parse(fs.readFileSync(path.join(fwDir, f), 'utf8'));
          fwRegistry.push(fw);
        } catch (e) {
          console.warn(`  WARN: could not parse ${f}: ${e.message}`);
        }
      });
    }
    if (fwRegistry.length) {
      const fwRegistryPath = path.join(docsDir, 'frameworks-registry.js');
      const fwRegistryData = [
        `// Auto-generated by scripts/generate.js — do not edit manually`,
        `// Generated: ${new Date().toISOString().split('T')[0]}`,
        `// Frameworks: ${fwRegistry.length}`,
        `window.CROSSWALK_FRAMEWORKS = ${JSON.stringify(fwRegistry, null, 2)};`,
      ].join('\n');
      fs.writeFileSync(fwRegistryPath, fwRegistryData, 'utf8');
      console.log(`Written docs/frameworks-registry.js (${fwRegistry.length} frameworks)`);
    }

    // ── Bundle incidents for site ──
    if (fs.existsSync(incidentsFile)) {
      const incDb = JSON.parse(fs.readFileSync(incidentsFile, 'utf8'));
      const incPath = path.join(docsDir, 'incidents.js');
      const incData = [
        `// Auto-generated by scripts/generate.js — do not edit manually`,
        `// Generated: ${new Date().toISOString().split('T')[0]}`,
        `// Incidents: ${incDb.incidents.length}`,
        `window.CROSSWALK_INCIDENTS = ${JSON.stringify(incDb.incidents, null, 2)};`,
      ].join('\n');
      fs.writeFileSync(incPath, incData, 'utf8');
      console.log(`Written docs/incidents.js (${incDb.incidents.length} incidents)`);
    }
  }

  console.log(`\n${'─'.repeat(50)}`);
  if (DRY_RUN) {
    console.log(`Dry run complete. ${targetIds.length} entries would be written.`);
  } else {
    console.log(`Written ${written} entries to data/entries/`);
  }
  if (warnings) console.log(`Warnings: ${warnings} entries had 0 mappings — check source files.`);
  console.log();
}

function defaultAudience(sourceList) {
  if (sourceList === 'LLM-Top10-2025')    return ['developer', 'security-engineer', 'red-teamer', 'auditor'];
  if (sourceList === 'Agentic-Top10-2026') return ['security-engineer', 'ciso', 'red-teamer', 'auditor'];
  return ['security-engineer', 'data-engineer', 'auditor', 'compliance'];
}

main();
