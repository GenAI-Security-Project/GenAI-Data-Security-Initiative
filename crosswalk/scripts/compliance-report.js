#!/usr/bin/env node
/**
 * GenAI Security Crosswalk — Compliance Gap Assessment Generator
 * ──────────────────────────────────────────────────────────────────────────
 * Reads all data/entries/*.json and produces framework-centric gap reports.
 *
 * Supported output formats:
 *   --format md   (default) Markdown — drop into docs, PR descriptions, audits
 *   --format csv            CSV      — open in Excel / Google Sheets
 *   --format json           JSON     — programmatic consumption / dashboards
 *   --format oscal          OSCAL    — OSCAL 1.1.2 Component Definition JSON
 *   --format oscal-catalog  OSCAL    — OSCAL 1.1.2 Catalog (full control inventory)
 *   --format grc            GRC      — ServiceNow/Archer/Drata-ready import JSON
 *
 * Usage:
 *   node scripts/compliance-report.js
 *   node scripts/compliance-report.js --framework "EU AI Act"
 *   node scripts/compliance-report.js --framework "ISO/IEC 42001:2023" --format csv
 *   node scripts/compliance-report.js --framework "NIST AI RMF 1.0" --format oscal
 *   node scripts/compliance-report.js --severity Critical
 *   node scripts/compliance-report.js --out reports/
 *
 * Flags:
 *   --framework <name>   Report for one framework only (partial match, case-insensitive)
 *   --severity <level>   Filter entries: Critical | High | Medium | Low
 *   --format <fmt>       md | csv | json | oscal | oscal-catalog | grc  (default: md)
 *   --out <dir>          Output directory  (default: reports/)
 *   --stdout             Print to stdout instead of writing files
 *   --list-frameworks    List all available framework names and exit
 * ──────────────────────────────────────────────────────────────────────────
 */

'use strict';

const fs   = require('fs');
const path = require('path');

// ── Configuration ────────────────────────────────────────────────────────────

const REPO_ROOT   = path.resolve(__dirname, '..');
const ENTRIES_DIR = path.join(REPO_ROOT, 'data', 'entries');
const DEFAULT_OUT = path.join(REPO_ROOT, 'reports');

// Frameworks included in default (all) reports — ordered by audience relevance
const REPORT_FRAMEWORKS = [
  'EU AI Act',
  'ISO/IEC 42001:2023',
  'NIST AI RMF 1.0',
  'ISO/IEC 27001:2022',
  'SOC 2',
  'NIST CSF 2.0',
  'CIS Controls v8.1',
  'ISA/IEC 62443',
  'NIST SP 800-82 Rev 3',
  'OWASP ASVS 4.0.3',
  'OWASP SAMM v2.0',
  'PCI DSS v4.0',
  'MITRE ATLAS',
  'MAESTRO',
  'AIUC-1',
  'ENISA Multilayer Framework',
  'OWASP NHI Top 10',
  'NIST SP 800-218A',
  'FedRAMP',
  'DORA',
  'CWE/CVE',
  'OWASP AI Testing Guide',
  'STRIDE',
];

const SEVERITY_ORDER = { Critical: 0, High: 1, Medium: 2, Low: 3 };

// Human-readable labels and context per framework
const FW_META = {
  'EU AI Act': {
    short: 'EU AI Act',
    deadline: 'August 2026 (GPAI obligations live)',
    audience: 'Compliance officers, EU-market deployers',
    note: 'High-risk AI systems and GPAI models with systemic risk face binding obligations.',
  },
  'ISO/IEC 42001:2023': {
    short: 'ISO 42001',
    deadline: 'Certification available now',
    audience: 'AI management system leads, QMS teams',
    note: 'AIMS certification — annex controls mapped to OWASP risks.',
  },
  'NIST AI RMF 1.0': {
    short: 'NIST AI RMF',
    deadline: 'Voluntary — referenced by US federal procurement',
    audience: 'Risk managers, US federal contractors',
    note: 'GOVERN / MAP / MEASURE / MANAGE functions.',
  },
  'ISO/IEC 27001:2022': {
    short: 'ISO 27001',
    deadline: 'Oct 2025 transition deadline passed — new controls apply now',
    audience: 'ISMS leads, CISOs',
    note: '2022 revision adds AI/cloud controls (A.5.23, A.8.28).',
  },
  'SOC 2': {
    short: 'SOC 2',
    deadline: 'Annual audit cycle',
    audience: 'SaaS providers, enterprise sales',
    note: 'Trust Services Criteria — CC series for AI-specific controls.',
  },
  'NIST CSF 2.0': {
    short: 'NIST CSF 2.0',
    deadline: 'Voluntary — widely adopted',
    audience: 'Security programme leads',
    note: 'GOVERN function added in 2.0 — relevant for AI oversight.',
  },
  'CIS Controls v8.1': {
    short: 'CIS Controls',
    deadline: 'Ongoing — IG tiers',
    audience: 'Security engineers, small-to-mid orgs',
    note: 'IG1/IG2/IG3 implementation groups.',
  },
  'ISA/IEC 62443': {
    short: 'ISA/IEC 62443',
    deadline: 'OT/ICS deployment requirement',
    audience: 'OT security engineers, industrial AI deployers',
    note: 'Zone/conduit model and Security Level ratings.',
  },
  'NIST SP 800-82 Rev 3': {
    short: 'NIST 800-82r3',
    deadline: 'OT/ICS guidance',
    audience: 'ICS/SCADA teams',
    note: 'OT-specific overlay for NIST CSF and RMF.',
  },
  'OWASP ASVS 4.0.3': {
    short: 'OWASP ASVS',
    deadline: 'Ongoing — L1/L2/L3 verification',
    audience: 'AppSec engineers, pen testers',
    note: 'Application Security Verification Standard — L1-L3 levels.',
  },
  'OWASP SAMM v2.0': {
    short: 'OWASP SAMM',
    deadline: 'Ongoing — maturity model',
    audience: 'Security programme leads, dev teams',
    note: 'Software Assurance Maturity Model — 1–3 maturity levels.',
  },
  'PCI DSS v4.0': {
    short: 'PCI DSS v4.0',
    deadline: 'April 2025 — v4.0 mandatory',
    audience: 'Payment system owners',
    note: 'March 2025 customised approach requirements apply to AI systems handling CHD.',
  },
  'MITRE ATLAS': {
    short: 'MITRE ATLAS',
    deadline: 'Reference — threat modelling',
    audience: 'Red teamers, threat modellers',
    note: 'Adversarial ML technique taxonomy — AML.T#### codes.',
  },
  'MAESTRO': {
    short: 'MAESTRO',
    deadline: 'CSA reference — agentic AI',
    audience: 'Agentic AI architects',
    note: 'L1–L7 layer model for agentic AI threat analysis.',
  },
  'AIUC-1': {
    short: 'AIUC-1',
    deadline: 'Industry standard',
    audience: 'AI governance leads',
    note: 'AI Use Case framework — governance and accountability controls.',
  },
  'ENISA Multilayer Framework': {
    short: 'ENISA MLF',
    deadline: 'EU reference',
    audience: 'EU public sector, ENISA-aligned orgs',
    note: 'Technical and organisational measures for AI.',
  },
  'OWASP NHI Top 10': {
    short: 'OWASP NHI',
    deadline: 'Ongoing',
    audience: 'Identity engineers, agentic AI teams',
    note: 'Non-Human Identity risks — API keys, service accounts, agent credentials.',
  },
  'NIST SP 800-218A': {
    short: 'SP 800-218A',
    deadline: 'Initial Public Draft — final expected 2026',
    audience: 'ML engineers, US federal contractors, secure SDLC teams',
    note: 'Extends SSDF with AI-specific practices for secure GenAI/foundation model development.',
  },
  'FedRAMP': {
    short: 'FedRAMP',
    deadline: 'Continuous — required for US federal cloud services',
    audience: 'US federal contractors, cloud service providers, FedRAMP assessors',
    note: 'AI overlay extends SP 800-53 Rev 5 baseline with AI-specific controls for federal cloud AI.',
  },
  'DORA': {
    short: 'DORA',
    deadline: 'January 17, 2025 — mandatory for EU financial entities',
    audience: 'Financial sector CISOs, third-party risk managers, EU financial regulators',
    note: 'Digital Operational Resilience Act — ICT risk, incident reporting, resilience testing for financial AI.',
  },
  'CWE/CVE': {
    short: 'CWE/CVE',
    deadline: 'Ongoing — community-maintained',
    audience: 'AppSec engineers, vulnerability researchers',
    note: 'Common Weakness Enumeration and Common Vulnerabilities — mapped to AI-specific weaknesses.',
  },
  'OWASP AI Testing Guide': {
    short: 'AI Testing',
    deadline: 'Ongoing',
    audience: 'AI pen testers, red teamers, QA engineers',
    note: 'Structured testing methodology for AI system security — input handling, model behaviour, access control.',
  },
  'STRIDE': {
    short: 'STRIDE',
    deadline: 'Reference — threat modelling',
    audience: 'Threat modellers, security architects',
    note: 'Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation — applied to AI/agentic systems.',
  },
};

// ── Argument parsing ─────────────────────────────────────────────────────────

function parseArgs() {
  const args = process.argv.slice(2);
  const opts = {
    framework: null,
    severity:  null,
    format:    'md',
    out:       DEFAULT_OUT,
    stdout:    false,
    listFw:    false,
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--framework':   opts.framework = args[++i]; break;
      case '--severity':    opts.severity  = args[++i]; break;
      case '--format':      opts.format    = args[++i]; break;
      case '--out':         opts.out       = path.resolve(args[++i]); break;
      case '--stdout':      opts.stdout    = true; break;
      case '--list-frameworks': opts.listFw = true; break;
      default:
        if (args[i].startsWith('--')) {
          console.error(`Unknown flag: ${args[i]}`);
          process.exit(1);
        }
    }
  }

  if (!['md', 'csv', 'json', 'oscal', 'oscal-catalog', 'grc'].includes(opts.format)) {
    console.error(`Unknown format: ${opts.format}. Use md, csv, json, oscal, oscal-catalog, or grc.`);
    process.exit(1);
  }

  return opts;
}

// ── Data loading ─────────────────────────────────────────────────────────────

function loadEntries(severityFilter) {
  const files = fs.readdirSync(ENTRIES_DIR).filter(f => f.endsWith('.json'));
  return files
    .map(f => JSON.parse(fs.readFileSync(path.join(ENTRIES_DIR, f), 'utf8')))
    .filter(e => !severityFilter || e.severity === severityFilter)
    .sort((a, b) => {
      // Sort by source list order, then by ID number
      const listOrder = { 'LLM-Top10-2025': 0, 'Agentic-Top10-2026': 1, 'DSGAI-2026': 2 };
      const la = listOrder[a.source_list] ?? 9;
      const lb = listOrder[b.source_list] ?? 9;
      if (la !== lb) return la - lb;
      return a.id.localeCompare(b.id);
    });
}

function getFrameworkNames(entries) {
  const set = new Set();
  entries.forEach(e => e.mappings.forEach(m => set.add(m.framework)));
  return [...set].sort();
}

// ── Framework data extraction ─────────────────────────────────────────────────

/**
 * Normalise garbled characters in control names/IDs (mojibake from em-dash etc.)
 */
function normalise(str) {
  if (!str) return '';
  return str
    .replace(/\uFFFD/g, '—')   // replacement char → em-dash
    .replace(/â€"/g, '—')
    .replace(/\s*\?\s*/g, ' — ')
    .replace(/\s{2,}/g, ' ')
    .trim();
}

/**
 * Build a per-framework data structure:
 * {
 *   framework: string,
 *   meta: { ... },
 *   controls: Map<control_id, { control_name, tier, entries: Entry[], notes: string[] }>,
 *   entries: Entry[],            // entries that have mappings for this framework
 *   uncovered: Entry[],          // entries with no mappings for this framework
 *   coverageRate: number,        // 0–1
 * }
 */
function buildFrameworkReport(framework, entries) {
  const meta = FW_META[framework] || { short: framework, note: '' };
  const controls = new Map();
  const covered   = new Set();

  for (const entry of entries) {
    const fwMappings = entry.mappings.filter(m => m.framework === framework);
    if (fwMappings.length === 0) continue;

    covered.add(entry.id);

    for (const m of fwMappings) {
      const cid = normalise(m.control_id) || normalise(m.control_name);
      const cname = normalise(m.control_name) || normalise(m.control_id);

      if (!controls.has(cid)) {
        controls.set(cid, {
          control_id:   cid,
          control_name: cname,
          tier:         m.tier || '',
          entries:      [],
          notes:        [],
        });
      }
      const ctrl = controls.get(cid);
      if (!ctrl.entries.find(e => e.id === entry.id)) {
        ctrl.entries.push(entry);
      }
      if (m.notes && !ctrl.notes.includes(normalise(m.notes))) {
        ctrl.notes.push(normalise(m.notes));
      }
    }
  }

  const uncovered = entries.filter(e => !covered.has(e.id));
  const coverageRate = entries.length > 0 ? covered.size / entries.length : 0;

  return {
    framework,
    meta,
    controls,
    entries: entries.filter(e => covered.has(e.id)),
    uncovered,
    coverageRate,
  };
}

// ── Markdown renderer ─────────────────────────────────────────────────────────

function renderMarkdown(fw, allEntries, opts) {
  const r    = buildFrameworkReport(fw, allEntries);
  const date = new Date().toISOString().slice(0, 10);
  const lines = [];

  lines.push(`# ${fw} — GenAI Security Gap Assessment`);
  lines.push('');
  lines.push(`> Generated ${date} from GenAI Security Crosswalk  `);
  lines.push(`> Source: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk`);
  if (opts.severity) lines.push(`> Filtered to **${opts.severity}** severity entries only`);
  lines.push('');
  lines.push('---');
  lines.push('');

  // Framework context
  if (r.meta.deadline || r.meta.audience || r.meta.note) {
    lines.push('## Framework context');
    lines.push('');
    if (r.meta.deadline)  lines.push(`**Timeline:** ${r.meta.deadline}  `);
    if (r.meta.audience)  lines.push(`**Primary audience:** ${r.meta.audience}  `);
    if (r.meta.note)      lines.push(`**Scope:** ${r.meta.note}  `);
    lines.push('');
    lines.push('---');
    lines.push('');
  }

  // Executive summary
  const criticalUncovered = r.uncovered.filter(e => e.severity === 'Critical');
  const highUncovered     = r.uncovered.filter(e => e.severity === 'High');

  lines.push('## Executive summary');
  lines.push('');
  lines.push('| Metric | Value |');
  lines.push('|---|---|');
  lines.push(`| OWASP entries assessed | ${allEntries.length} |`);
  lines.push(`| Entries with ${fw} mappings | ${r.entries.length} |`);
  lines.push(`| Entries with no ${fw} mappings | ${r.uncovered.length} |`);
  lines.push(`| Coverage rate | ${(r.coverageRate * 100).toFixed(0)}% |`);
  lines.push(`| Unique controls referenced | ${r.controls.size} |`);
  lines.push(`| Critical-severity gaps | ${criticalUncovered.length} |`);
  lines.push(`| High-severity gaps | ${highUncovered.length} |`);
  lines.push('');

  // Overall status
  if (criticalUncovered.length === 0 && highUncovered.length === 0) {
    lines.push('**Status: PASS** — All Critical and High severity entries are covered.');
  } else {
    lines.push(`**Status: ACTION REQUIRED** — ${criticalUncovered.length} Critical and ${highUncovered.length} High entries have no ${fw} mappings.`);
  }
  lines.push('');
  lines.push('---');
  lines.push('');

  // Gap analysis — entries with no mappings
  if (r.uncovered.length > 0) {
    lines.push('## Gap analysis — entries with no mappings');
    lines.push('');
    lines.push(`The following OWASP entries have no controls mapped to **${fw}**. `);
    lines.push('These represent coverage gaps that may require manual assessment or framework extension.');
    lines.push('');
    lines.push('| Entry | Name | Source list | Severity | Recommended action |');
    lines.push('|---|---|---|---|---|');

    for (const e of r.uncovered.sort((a, b) => (SEVERITY_ORDER[a.severity] ?? 9) - (SEVERITY_ORDER[b.severity] ?? 9))) {
      const action = e.severity === 'Critical' || e.severity === 'High'
        ? `Review manually — no ${r.meta.short || fw} control identified`
        : `Low priority — verify framework scope excludes this risk`;
      lines.push(`| **${e.id}** | ${e.name} | ${e.source_list} | ${e.severity} | ${action} |`);
    }

    lines.push('');
    lines.push('---');
    lines.push('');
  }

  // Coverage matrix — entries vs controls
  lines.push('## Coverage matrix — OWASP entries → controls');
  lines.push('');

  const sourceGroups = {};
  for (const e of r.entries) {
    if (!sourceGroups[e.source_list]) sourceGroups[e.source_list] = [];
    sourceGroups[e.source_list].push(e);
  }

  for (const [list, entries] of Object.entries(sourceGroups)) {
    lines.push(`### ${list}`);
    lines.push('');
    lines.push('| Entry | Name | Severity | Controls | Tier |');
    lines.push('|---|---|---|---|---|');

    for (const e of entries) {
      const fwMappings = e.mappings.filter(m => m.framework === fw);
      const controlList = fwMappings
        .map(m => normalise(m.control_id) || normalise(m.control_name))
        .filter((v, i, a) => a.indexOf(v) === i)
        .slice(0, 5)    // cap display at 5 to keep table readable
        .join(', ');
      const moreCount = Math.max(0, fwMappings.length - 5);
      const controlStr = moreCount > 0 ? `${controlList} _(+${moreCount} more)_` : controlList;
      const tiers = [...new Set(fwMappings.map(m => m.tier).filter(Boolean))].join(', ');

      lines.push(`| **${e.id}** | ${e.name} | ${e.severity} | ${controlStr} | ${tiers || '—'} |`);
    }

    lines.push('');
  }

  lines.push('---');
  lines.push('');

  // Control detail — all controls with which entries need them
  lines.push('## Control detail — all referenced controls');
  lines.push('');
  lines.push('Each control lists the OWASP risks it addresses, ordered by severity.');
  lines.push('');

  const sortedControls = [...r.controls.values()].sort((a, b) => {
    // Sort by worst severity of entries referencing this control
    const worstA = Math.min(...a.entries.map(e => SEVERITY_ORDER[e.severity] ?? 9));
    const worstB = Math.min(...b.entries.map(e => SEVERITY_ORDER[e.severity] ?? 9));
    return worstA - worstB || a.control_id.localeCompare(b.control_id);
  });

  for (const ctrl of sortedControls) {
    const entryIds = ctrl.entries
      .sort((a, b) => (SEVERITY_ORDER[a.severity] ?? 9) - (SEVERITY_ORDER[b.severity] ?? 9))
      .map(e => `${e.id} (${e.severity})`);

    lines.push(`### ${ctrl.control_id}`);
    if (ctrl.control_name && ctrl.control_name !== ctrl.control_id) {
      lines.push(`**${ctrl.control_name}**`);
    }
    if (ctrl.tier) lines.push(`_Tier: ${ctrl.tier}_`);
    lines.push('');
    lines.push(`Addresses: ${entryIds.join(' · ')}`);
    if (ctrl.notes.length > 0) {
      lines.push('');
      // Show first two distinct notes
      ctrl.notes.slice(0, 2).forEach(n => lines.push(`> ${n}`));
    }
    lines.push('');
  }

  lines.push('---');
  lines.push('');

  // Action plan
  lines.push('## Action plan');
  lines.push('');

  const actionItems = [];

  // Critical gaps
  if (criticalUncovered.length > 0) {
    actionItems.push({
      priority: 'P1 — Immediate',
      items: criticalUncovered.map(e =>
        `Map **${e.id} ${e.name}** to a ${fw} control or document a compensating control`
      ),
    });
  }

  // High gaps
  if (highUncovered.length > 0) {
    actionItems.push({
      priority: 'P2 — Short-term',
      items: highUncovered.map(e =>
        `Assess whether **${e.id} ${e.name}** is in scope; document exclusion rationale if not`
      ),
    });
  }

  // Coverage improvement
  if (r.coverageRate < 0.8) {
    actionItems.push({
      priority: 'P3 — Medium-term',
      items: [
        `Improve ${fw} coverage from ${(r.coverageRate * 100).toFixed(0)}% to ≥80%`,
        'Consider framework extension or supplementary controls for uncovered entries',
      ],
    });
  }

  // Eval integration
  actionItems.push({
    priority: 'Ongoing — CI/CD',
    items: [
      'Run `bash evals/garak/run_all.sh` monthly against production model',
      'Add `evals/ci/github-action.yml` to your repo to gate PRs on security regressions',
      'Review eval results against this gap assessment quarterly',
    ],
  });

  if (actionItems.length === 0) {
    lines.push('All Critical and High entries are mapped. No immediate actions required.');
    lines.push('');
    lines.push('Maintain coverage by running eval profiles on each model update.');
  } else {
    for (const group of actionItems) {
      lines.push(`### ${group.priority}`);
      lines.push('');
      group.items.forEach(item => lines.push(`- [ ] ${item}`));
      lines.push('');
    }
  }

  lines.push('---');
  lines.push('');
  lines.push('_Generated by [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) · '
    + `CC BY-SA 4.0 · ${date}_`);

  return lines.join('\n');
}

// ── CSV renderer ──────────────────────────────────────────────────────────────

function csvEscape(val) {
  const s = String(val ?? '').replace(/"/g, '""');
  return /[,"\n\r]/.test(s) ? `"${s}"` : s;
}

function renderCSV(fw, allEntries) {
  const r = buildFrameworkReport(fw, allEntries);
  const rows = [];

  rows.push(['Framework', 'OWASP_ID', 'Entry_Name', 'Source_List', 'Severity',
    'AIVSS_Score', 'Control_ID', 'Control_Name', 'Tier', 'Notes', 'Mapped'].join(','));

  for (const e of allEntries) {
    const fwMappings = e.mappings.filter(m => m.framework === fw);

    if (fwMappings.length === 0) {
      rows.push([
        fw, e.id, e.name, e.source_list, e.severity,
        e.aivss_score ?? '', '', '', '', '', 'NO'
      ].map(csvEscape).join(','));
    } else {
      for (const m of fwMappings) {
        rows.push([
          fw, e.id, e.name, e.source_list, e.severity,
          e.aivss_score ?? '',
          normalise(m.control_id), normalise(m.control_name),
          m.tier || '', normalise(m.notes), 'YES'
        ].map(csvEscape).join(','));
      }
    }
  }

  return rows.join('\n');
}

// ── JSON renderer ─────────────────────────────────────────────────────────────

function renderJSON(fw, allEntries) {
  const r    = buildFrameworkReport(fw, allEntries);
  const date = new Date().toISOString().slice(0, 10);

  const output = {
    generated:     date,
    framework:     fw,
    meta:          r.meta,
    summary: {
      total_entries:      allEntries.length,
      covered_entries:    r.entries.length,
      uncovered_entries:  r.uncovered.length,
      coverage_rate:      parseFloat((r.coverageRate * 100).toFixed(1)),
      unique_controls:    r.controls.size,
      critical_gaps:      r.uncovered.filter(e => e.severity === 'Critical').length,
      high_gaps:          r.uncovered.filter(e => e.severity === 'High').length,
    },
    coverage: allEntries.map(e => {
      const fwMappings = e.mappings.filter(m => m.framework === fw);
      return {
        id:           e.id,
        name:         e.name,
        source_list:  e.source_list,
        severity:     e.severity,
        aivss_score:  e.aivss_score,
        mapped:       fwMappings.length > 0,
        controls:     fwMappings.map(m => ({
          control_id:   normalise(m.control_id),
          control_name: normalise(m.control_name),
          tier:         m.tier || null,
          notes:        normalise(m.notes),
        })),
      };
    }),
    controls: [...r.controls.values()].map(ctrl => ({
      control_id:   ctrl.control_id,
      control_name: ctrl.control_name,
      tier:         ctrl.tier,
      entry_ids:    ctrl.entries.map(e => e.id),
    })),
  };

  return JSON.stringify(output, null, 2);
}

// ── Multi-framework summary Markdown ─────────────────────────────────────────

function renderSummaryMarkdown(frameworks, allEntries, opts) {
  const date  = new Date().toISOString().slice(0, 10);
  const lines = [];

  lines.push('# GenAI Security Crosswalk — Compliance Coverage Summary');
  lines.push('');
  lines.push(`> Generated ${date}  `);
  lines.push('> Source: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk');
  if (opts.severity) lines.push(`> Filtered to **${opts.severity}** severity entries only`);
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Coverage by framework');
  lines.push('');
  lines.push('| Framework | Audience | Entries covered | Coverage | Critical gaps | High gaps | Status |');
  lines.push('|---|---|---|---|---|---|---|');

  for (const fw of frameworks) {
    const r    = buildFrameworkReport(fw, allEntries);
    const meta = r.meta;
    const crit = r.uncovered.filter(e => e.severity === 'Critical').length;
    const high = r.uncovered.filter(e => e.severity === 'High').length;
    const pct  = (r.coverageRate * 100).toFixed(0);
    const status = crit === 0 && high === 0 ? '✅ No gaps' : `⚠️ ${crit}C / ${high}H gaps`;
    const aud  = meta.audience ? meta.audience.split(',')[0].trim() : '—';

    lines.push(`| **${fw}** | ${aud} | ${r.entries.length}/${allEntries.length} | ${pct}% | ${crit} | ${high} | ${status} |`);
  }

  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## How to read this table');
  lines.push('');
  lines.push('- **Entries covered**: OWASP entries that have at least one control mapped to this framework');
  lines.push('- **Critical/High gaps**: Entries with that severity that have _no_ controls mapped — highest risk to ignore');
  lines.push('- **✅ No gaps**: All Critical and High entries are covered; Medium/Low gaps may still exist');
  lines.push('');
  lines.push('Run `node scripts/compliance-report.js --framework "<name>"` for a full gap assessment of any framework.');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Eval coverage');
  lines.push('');
  lines.push('Run these profiles to validate controls are effective, not just documented:');
  lines.push('');
  lines.push('```bash');
  lines.push('pip install garak pyrit');
  lines.push('export OPENAI_API_KEY=sk-...');
  lines.push('bash evals/garak/run_all.sh');
  lines.push('python evals/pyrit/llm01_prompt_injection.py');
  lines.push('python evals/pyrit/dsgai04_rag_poisoning.py');
  lines.push('python evals/pyrit/asi01_goal_hijack.py');
  lines.push('```');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push(`_Generated by [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) · CC BY-SA 4.0 · ${date}_`);

  return lines.join('\n');
}

// ── OSCAL 1.1.2 renderer ─────────────────────────────────────────────────────

const crypto = require('crypto');

function renderOSCAL(fw, allEntries) {
  const r   = buildFrameworkReport(fw, allEntries);
  const now = new Date().toISOString();

  const partyUuid = crypto.randomUUID();
  const componentDef = {
    'component-definition': {
      uuid: crypto.randomUUID(),
      metadata: {
        title: `GenAI Security Crosswalk — ${fw} Component Definition`,
        'last-modified': now,
        version: '1.6.0',
        'oscal-version': '1.1.2',
        roles: [{ id: 'maintainer', title: 'Crosswalk Maintainer' }],
        parties: [{
          uuid: partyUuid,
          type: 'organization',
          name: 'OWASP GenAI Data Security Initiative',
          links: [{ href: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk', rel: 'homepage' }],
        }],
        'responsible-parties': [{ 'role-id': 'maintainer', 'party-uuids': [partyUuid] }],
      },
      components: [{
        uuid: crypto.randomUUID(),
        type: 'software',
        title: 'GenAI System',
        description: `AI/ML system subject to ${fw} compliance assessment`,
        'control-implementations': [{
          uuid: crypto.randomUUID(),
          source: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk',
          description: `${fw} control mapping from GenAI Security Crosswalk`,
          'implemented-requirements': [...r.controls.values()].flatMap(ctrl =>
            ctrl.entries.map(entry => ({
              uuid: crypto.randomUUID(),
              'control-id': ctrl.control_id,
              description: `${entry.id}: ${entry.name} — ${ctrl.control_name}${ctrl.notes.length ? ' | ' + ctrl.notes.join('; ') : ''}`,
              props: [
                { name: 'implementation-status', value: 'planned', ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
                { name: 'owasp-entry', value: entry.id, ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
                { name: 'severity', value: entry.severity, ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
                { name: 'source-list', value: entry.source_list, ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
              ],
              links: [
                { href: `https://github.com/emmanuelgjr/GenAI-Security-Crosswalk/blob/main/data/entries/${entry.id}.json`, rel: 'reference' },
              ],
            }))
          ),
        }],
      }],
      'back-matter': {
        resources: r.uncovered.map(entry => ({
          uuid: crypto.randomUUID(),
          title: `GAP: ${entry.id} — ${entry.name} (${entry.severity})`,
          description: `No ${fw} controls mapped for this OWASP entry. Severity: ${entry.severity}. Requires gap remediation.`,
          props: [
            { name: 'gap-severity', value: entry.severity, ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
          ],
        })),
      },
    },
  };

  return JSON.stringify(componentDef, null, 2);
}

// ── OSCAL 1.1.2 Catalog renderer ────────────────────────────────────────────

function renderOSCALCatalog(fw, allEntries) {
  // Load the framework registry for full control inventory
  const fwDir = path.join(REPO_ROOT, 'data', 'frameworks');
  const registryFiles = fs.readdirSync(fwDir).filter(f => f.endsWith('.json'));
  let registryFw = null;
  for (const f of registryFiles) {
    const reg = JSON.parse(fs.readFileSync(path.join(fwDir, f), 'utf8'));
    if (reg.name === fw) { registryFw = reg; break; }
  }

  const r   = buildFrameworkReport(fw, allEntries);
  const now = new Date().toISOString();

  // Group controls by function/domain for OSCAL groups
  const groups = new Map();
  const controls = registryFw ? registryFw.controls : [...r.controls.values()];

  for (const ctrl of controls) {
    const fn = (registryFw ? ctrl.function : null) || 'General';
    if (!groups.has(fn)) groups.set(fn, []);
    groups.get(fn).push(ctrl);
  }

  const catalog = {
    catalog: {
      uuid: crypto.randomUUID(),
      metadata: {
        title: `${fw} — Control Catalog`,
        'last-modified': now,
        version: registryFw ? registryFw.version : '1.0',
        'oscal-version': '1.1.2',
        roles: [{ id: 'publisher', title: 'Framework Publisher' }],
        parties: [{
          uuid: crypto.randomUUID(),
          type: 'organization',
          name: registryFw ? registryFw.publisher : 'Unknown',
        }],
        links: registryFw ? [{ href: registryFw.url, rel: 'canonical' }] : [],
      },
      groups: [...groups.entries()].map(([groupName, ctrls]) => ({
        id: groupName.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
        title: groupName,
        controls: ctrls.map(ctrl => {
          const cid = registryFw ? ctrl.control_id : ctrl.control_id;
          const mappedData = r.controls.get(cid);
          return {
            id: cid,
            title: registryFw ? ctrl.title : (ctrl.control_name || ctrl.title),
            props: [
              ...(ctrl.description ? [{ name: 'description', value: ctrl.description }] : []),
              ...(mappedData ? [
                { name: 'owasp-coverage', value: mappedData.entries.map(e => e.id).join(','), ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
                { name: 'coverage-count', value: String(mappedData.entries.length), ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
              ] : [
                { name: 'owasp-coverage', value: 'none', ns: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' },
              ]),
            ],
            links: mappedData ? mappedData.entries.map(e => ({
              href: `https://github.com/emmanuelgjr/GenAI-Security-Crosswalk/blob/main/data/entries/${e.id}.json`,
              rel: 'related',
              text: `${e.id}: ${e.name}`,
            })) : [],
          };
        }),
      })),
      'back-matter': {
        resources: [{
          uuid: crypto.randomUUID(),
          title: 'GenAI Security Crosswalk',
          description: 'OWASP GenAI Security Crosswalk — comprehensive mapping of AI security risks to compliance frameworks',
          rlinks: [{ href: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk' }],
        }],
      },
    },
  };

  return JSON.stringify(catalog, null, 2);
}

// ── GRC platform export renderer ────────────────────────────────────────────

function renderGRC(fw, allEntries) {
  const r   = buildFrameworkReport(fw, allEntries);
  const now = new Date().toISOString();

  // Build GRC-import-friendly format compatible with ServiceNow, Archer, Drata
  const grcExport = {
    _meta: {
      format: 'genai-crosswalk-grc-v1',
      generated: now,
      framework: fw,
      source: 'https://github.com/emmanuelgjr/GenAI-Security-Crosswalk',
      coverage_rate: Math.round(r.coverageRate * 100) + '%',
      total_entries: allEntries.length,
      covered_entries: r.entries.length,
      gap_entries: r.uncovered.length,
    },
    // Control objectives — each maps to a GRC "control" record
    controls: [...r.controls.values()].map(ctrl => ({
      control_id: ctrl.control_id,
      control_name: ctrl.control_name,
      tier: ctrl.tier,
      implementation_status: 'planned',
      // Risk mappings — connect to risk register entries
      risk_mappings: ctrl.entries.map(entry => ({
        risk_id: entry.id,
        risk_name: entry.name,
        source_list: entry.source_list,
        severity: entry.severity,
        risk_rating: ({ Critical: 4, High: 3, Medium: 2, Low: 1 })[entry.severity] || 0,
      })),
      // Evidence requirements
      evidence_requirements: ctrl.entries.map(entry =>
        `Demonstrate ${ctrl.control_name} addresses ${entry.id}: ${entry.name}`
      ),
      notes: ctrl.notes.join('; '),
      // ServiceNow-compatible fields
      sn_control_objective: ctrl.control_name,
      sn_risk_statement: `Failure to implement ${ctrl.control_id} (${ctrl.control_name}) leaves the following AI risks unmitigated: ${ctrl.entries.map(e => e.id).join(', ')}`,
      sn_test_plan: `Verify implementation of ${ctrl.control_id} through evidence review, configuration audit, and testing per OWASP GenAI Security Crosswalk.`,
    })),
    // Gaps — entries with no framework coverage (for risk register)
    gaps: r.uncovered.map(entry => ({
      risk_id: entry.id,
      risk_name: entry.name,
      severity: entry.severity,
      source_list: entry.source_list,
      risk_rating: ({ Critical: 4, High: 3, Medium: 2, Low: 1 })[entry.severity] || 0,
      gap_status: 'open',
      remediation: `No ${fw} controls currently mapped to ${entry.id}: ${entry.name}. Requires gap assessment and control implementation.`,
      sn_risk_statement: `${entry.id} (${entry.name}) has no ${fw} controls mapped. Severity: ${entry.severity}.`,
    })),
    // Cross-reference matrix for Archer/Drata
    cross_reference_matrix: allEntries.map(entry => {
      const fwMappings = entry.mappings.filter(m => m.framework === fw);
      return {
        entry_id: entry.id,
        entry_name: entry.name,
        severity: entry.severity,
        source_list: entry.source_list,
        is_covered: fwMappings.length > 0,
        control_count: fwMappings.length,
        control_ids: fwMappings.map(m => {
          const norm = normalise(m.control_id) || normalise(m.control_name);
          return norm;
        }),
      };
    }),
  };

  return JSON.stringify(grcExport, null, 2);
}

// ── File output ───────────────────────────────────────────────────────────────

function slugify(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function writeOutput(content, fw, format, outDir, toStdout) {
  if (toStdout) {
    process.stdout.write(content + '\n');
    return null;
  }

  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const extMap = { md: '.md', csv: '.csv', oscal: '.oscal.json', 'oscal-catalog': '.catalog.oscal.json', grc: '.grc.json', json: '.json' };
  const ext  = extMap[format] || '.json';
  const slug = fw === '__summary__' ? 'compliance-summary' : `${slugify(fw)}-gap-assessment`;
  const file = path.join(outDir, slug + ext);

  fs.writeFileSync(file, content, 'utf8');
  return file;
}

// ── Main ──────────────────────────────────────────────────────────────────────

function main() {
  const opts    = parseArgs();
  const entries = loadEntries(opts.severity);

  if (opts.listFw) {
    console.log('\nAvailable frameworks:\n');
    getFrameworkNames(entries).forEach(fw => console.log(`  ${fw}`));
    console.log('');
    process.exit(0);
  }

  if (entries.length === 0) {
    console.error('No entries found in data/entries/. Run: node scripts/generate.js');
    process.exit(1);
  }

  // Resolve which frameworks to report on
  let frameworks;
  if (opts.framework) {
    const query = opts.framework.toLowerCase();
    frameworks  = getFrameworkNames(entries).filter(fw => fw.toLowerCase().includes(query));
    if (frameworks.length === 0) {
      console.error(`No framework matching "${opts.framework}". Use --list-frameworks to see options.`);
      process.exit(1);
    }
  } else {
    // Default: all known report frameworks that appear in the data
    const inData = new Set(getFrameworkNames(entries));
    frameworks   = REPORT_FRAMEWORKS.filter(fw => inData.has(fw));
  }

  const written = [];

  // Per-framework reports
  for (const fw of frameworks) {
    let content;
    if (opts.format === 'md') {
      content = renderMarkdown(fw, entries, opts);
    } else if (opts.format === 'csv') {
      content = renderCSV(fw, entries);
    } else if (opts.format === 'oscal') {
      content = renderOSCAL(fw, entries);
    } else if (opts.format === 'oscal-catalog') {
      content = renderOSCALCatalog(fw, entries);
    } else if (opts.format === 'grc') {
      content = renderGRC(fw, entries);
    } else {
      content = renderJSON(fw, entries);
    }

    const file = writeOutput(content, fw, opts.format, opts.out, opts.stdout);
    if (file) written.push(file);
  }

  // Summary report (Markdown only, not for single-framework or stdout runs)
  if (!opts.stdout && !opts.framework && opts.format === 'md' && frameworks.length > 1) {
    const summary = renderSummaryMarkdown(frameworks, entries, opts);
    const file    = writeOutput(summary, '__summary__', 'md', opts.out, false);
    if (file) written.push(file);
  }

  if (!opts.stdout) {
    const date = new Date().toISOString().slice(0, 10);
    console.log(`\nCompliance reports generated — ${date}`);
    console.log(`Entries assessed : ${entries.length}${opts.severity ? ` (${opts.severity} only)` : ''}`);
    console.log(`Frameworks       : ${frameworks.length}`);
    console.log(`Format           : ${opts.format}`);
    console.log(`Output directory : ${opts.out}`);
    console.log('');
    written.forEach(f => console.log(`  ✓  ${path.relative(REPO_ROOT, f)}`));
    console.log('');
  }
}

main();
