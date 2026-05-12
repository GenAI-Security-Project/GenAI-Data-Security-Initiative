#!/usr/bin/env node
/**
 * OWASP GenAI Crosswalk — Incident Tracker Query & Report Tool
 * ──────────────────────────────────────────────────────────────────────────
 * Reads data/incidents.json and produces incident reports, filtered views,
 * and MAESTRO layer attribution summaries.
 *
 * Usage:
 *   node scripts/incidents-report.js
 *   node scripts/incidents-report.js --entry LLM01
 *   node scripts/incidents-report.js --layer L3
 *   node scripts/incidents-report.js --severity Critical
 *   node scripts/incidents-report.js --category real-world
 *   node scripts/incidents-report.js --maestro-summary
 *   node scripts/incidents-report.js --format csv
 *   node scripts/incidents-report.js --format stix
 *   node scripts/incidents-report.js --stdout
 *
 * Flags:
 *   --entry  <ID>     Filter by OWASP entry (e.g. LLM01, ASI01, DSGAI04)
 *   --layer  <L#>     Filter by MAESTRO layer (L1–L7)
 *   --severity <sev>  Filter: Critical | High | Medium | Low
 *   --category <cat>  real-world | research-demonstrated | red-team
 *   --year  <YYYY>    Filter by year
 *   --maestro-summary Print MAESTRO layer attribution summary only
 *   --format <fmt>    md | csv | json | stix  (default: md)
 *   --out   <dir>     Output directory (default: reports/)
 *   --stdout          Print to stdout
 * ──────────────────────────────────────────────────────────────────────────
 */

'use strict';

const crypto = require('crypto');
const fs   = require('fs');
const path = require('path');

const REPO_ROOT      = path.resolve(__dirname, '..');
const INCIDENTS_FILE = path.join(REPO_ROOT, 'data', 'incidents.json');
const DEFAULT_OUT    = path.join(REPO_ROOT, 'reports');

const MAESTRO_LABELS = {
  L1: 'Foundation Models',
  L2: 'Data Operations',
  L3: 'Agent Frameworks',
  L4: 'Deployment & Infrastructure',
  L5: 'Evaluation & Observability',
  L6: 'Security & Compliance',
  L7: 'Agent Ecosystem',
};

const ROLE_LABELS = {
  origin:       '🔴 Origin',
  propagation:  '🟠 Propagation',
  impact:       '🟡 Impact',
  'blind-spot': '⚫ Blind-spot',
};

// ── Args ─────────────────────────────────────────────────────────────────────

function parseArgs() {
  const args = process.argv.slice(2);
  const opts = {
    entry:    null,
    layer:    null,
    severity: null,
    category: null,
    year:     null,
    maestro:  false,
    format:   'md',
    out:      DEFAULT_OUT,
    stdout:   false,
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--entry':           opts.entry    = args[++i].toUpperCase(); break;
      case '--layer':           opts.layer    = args[++i].toUpperCase(); break;
      case '--severity':        opts.severity = args[++i]; break;
      case '--category':        opts.category = args[++i]; break;
      case '--year':            opts.year     = parseInt(args[++i]); break;
      case '--maestro-summary': opts.maestro  = true; break;
      case '--format':          opts.format   = args[++i]; break;
      case '--out':             opts.out      = path.resolve(args[++i]); break;
      case '--stdout':          opts.stdout   = true; break;
      default:
        if (args[i].startsWith('--')) {
          console.error(`Unknown flag: ${args[i]}`);
          process.exit(1);
        }
    }
  }
  return opts;
}

// ── Data ─────────────────────────────────────────────────────────────────────

function loadIncidents(opts) {
  if (!fs.existsSync(INCIDENTS_FILE)) {
    console.error('data/incidents.json not found.');
    process.exit(1);
  }
  const db = JSON.parse(fs.readFileSync(INCIDENTS_FILE, 'utf8'));
  let incidents = db.incidents;

  if (opts.entry)    incidents = incidents.filter(i => i.owasp_entries.includes(opts.entry));
  if (opts.layer)    incidents = incidents.filter(i => i.maestro_layers.some(l => l.layer === opts.layer));
  if (opts.severity) incidents = incidents.filter(i => i.severity === opts.severity);
  if (opts.category) incidents = incidents.filter(i => i.category === opts.category);
  if (opts.year)     incidents = incidents.filter(i => i.year === opts.year);

  return { db, incidents };
}

// ── Markdown renderer ─────────────────────────────────────────────────────────

function renderMarkdown(db, incidents, opts) {
  const date   = new Date().toISOString().slice(0, 10);
  const lines  = [];
  const isFiltered = opts.entry || opts.layer || opts.severity || opts.category || opts.year;

  lines.push('# GenAI Security Incident Tracker');
  lines.push('');
  lines.push(`> Generated ${date} · ${incidents.length} incident${incidents.length !== 1 ? 's' : ''} · OWASP GenAI Crosswalk`);

  if (isFiltered) {
    const filters = [];
    if (opts.entry)    filters.push(`Entry: **${opts.entry}**`);
    if (opts.layer)    filters.push(`MAESTRO layer: **${opts.layer} — ${MAESTRO_LABELS[opts.layer] || ''}**`);
    if (opts.severity) filters.push(`Severity: **${opts.severity}**`);
    if (opts.category) filters.push(`Category: **${opts.category}**`);
    if (opts.year)     filters.push(`Year: **${opts.year}**`);
    lines.push(`> Filters applied: ${filters.join(' · ')}`);
  }

  lines.push('');
  lines.push('---');
  lines.push('');

  // Summary table
  lines.push('## Summary');
  lines.push('');

  const bySeverity  = groupBy(incidents, i => i.severity);
  const byCategory  = groupBy(incidents, i => i.category);
  const byLayer     = {};
  for (const inc of incidents) {
    for (const ml of inc.maestro_layers) {
      if (!byLayer[ml.layer]) byLayer[ml.layer] = 0;
      byLayer[ml.layer]++;
    }
  }

  lines.push('| Metric | Value |');
  lines.push('|---|---|');
  lines.push(`| Total incidents | ${incidents.length} |`);
  lines.push(`| Critical | ${(bySeverity['Critical'] || []).length} |`);
  lines.push(`| High | ${(bySeverity['High'] || []).length} |`);
  lines.push(`| Medium | ${(bySeverity['Medium'] || []).length} |`);
  lines.push(`| Real-world | ${(byCategory['real-world'] || []).length} |`);
  lines.push(`| Research-demonstrated | ${(byCategory['research-demonstrated'] || []).length} |`);

  // Most-implicated MAESTRO layer
  const topLayer = Object.entries(byLayer).sort((a, b) => b[1] - a[1])[0];
  if (topLayer) {
    lines.push(`| Most-implicated MAESTRO layer | ${topLayer[0]} — ${MAESTRO_LABELS[topLayer[0]]} (${topLayer[1]} incidents) |`);
  }

  // Most-referenced OWASP entry
  const entryCount = {};
  for (const inc of incidents) {
    for (const e of inc.owasp_entries) {
      entryCount[e] = (entryCount[e] || 0) + 1;
    }
  }
  const topEntry = Object.entries(entryCount).sort((a, b) => b[1] - a[1])[0];
  if (topEntry) {
    lines.push(`| Most-referenced OWASP entry | ${topEntry[0]} (${topEntry[1]} incidents) |`);
  }

  lines.push('');

  // MAESTRO layer attribution
  if (!isFiltered || opts.maestro) {
    lines.push('## MAESTRO layer attribution');
    lines.push('');
    lines.push('How many times each architectural layer appears across all incidents, by role:');
    lines.push('');
    lines.push('| Layer | Label | Origin | Propagation | Impact | Blind-spot | Total |');
    lines.push('|---|---|---|---|---|---|---|');

    for (const [lid, label] of Object.entries(MAESTRO_LABELS)) {
      const counts = { origin: 0, propagation: 0, impact: 0, 'blind-spot': 0 };
      for (const inc of incidents) {
        for (const ml of inc.maestro_layers) {
          if (ml.layer === lid) counts[ml.role] = (counts[ml.role] || 0) + 1;
        }
      }
      const total = Object.values(counts).reduce((a, b) => a + b, 0);
      if (total > 0) {
        lines.push(`| **${lid}** | ${label} | ${counts.origin} | ${counts.propagation} | ${counts.impact} | ${counts['blind-spot']} | **${total}** |`);
      }
    }

    lines.push('');
    lines.push('**Layer roles explained:**');
    lines.push('- **Origin** — where the attack initiates');
    lines.push('- **Propagation** — how the attack spreads through the system');
    lines.push('- **Impact** — where harm manifests');
    lines.push('- **Blind-spot** — where detection or prevention failed');
    lines.push('');
    lines.push('---');
    lines.push('');
  }

  // Incident index
  lines.push('## Incident index');
  lines.push('');
  lines.push('| ID | Title | Year | Severity | Category | OWASP | MAESTRO |');
  lines.push('|---|---|---|---|---|---|---|');

  for (const inc of incidents) {
    const layers = [...new Set(inc.maestro_layers.map(l => l.layer))].join(', ');
    const entries = inc.owasp_entries.join(', ');
    const cat = inc.category === 'real-world' ? '🔴 Real' : inc.category === 'research-demonstrated' ? '🟡 Research' : '🟠 Red-team';
    lines.push(`| **${inc.id}** | [${inc.title}](#${inc.id.toLowerCase()}) | ${inc.year} | ${inc.severity} | ${cat} | ${entries} | ${layers} |`);
  }

  lines.push('');
  lines.push('---');
  lines.push('');

  // Full incident entries
  lines.push('## Incident details');
  lines.push('');

  for (const inc of incidents) {
    lines.push(`### ${inc.id}`);
    lines.push('');
    lines.push(`**${inc.title}**`);
    lines.push('');

    const catLabel = inc.category === 'real-world' ? '🔴 Real-world' :
                     inc.category === 'research-demonstrated' ? '🟡 Research-demonstrated' : '🟠 Red-team';

    lines.push(`| | |`);
    lines.push(`|---|---|`);
    lines.push(`| Date | ${inc.date} |`);
    lines.push(`| Severity | **${inc.severity}** |`);
    lines.push(`| Category | ${catLabel} |`);
    lines.push(`| OWASP entries | ${inc.owasp_entries.join(' · ')} |`);
    lines.push(`| MAESTRO layers | ${inc.maestro_layers.map(l => `${l.layer} ${MAESTRO_LABELS[l.layer] || ''}`).join(' · ')} |`);
    if (inc.affected) lines.push(`| Affected | ${inc.affected} |`);
    lines.push('');

    lines.push(inc.description);
    lines.push('');

    lines.push('**Attack vector:** ' + inc.attack_vector);
    lines.push('');
    lines.push('**Impact:** ' + inc.impact);
    lines.push('');

    // MAESTRO layer breakdown
    lines.push('**MAESTRO layer attribution:**');
    lines.push('');
    for (const ml of inc.maestro_layers) {
      const roleLabel = ROLE_LABELS[ml.role] || ml.role;
      lines.push(`- **${ml.layer} — ${ml.label || MAESTRO_LABELS[ml.layer]}** · ${roleLabel}`);
      if (ml.notes) lines.push(`  _${ml.notes}_`);
    }
    lines.push('');

    if (inc.mitigations && inc.mitigations.length > 0) {
      lines.push('**Mitigations:**');
      lines.push('');
      inc.mitigations.forEach(m => lines.push(`- ${m}`));
      lines.push('');
    }

    if (inc.references && inc.references.length > 0) {
      lines.push('**References:**');
      lines.push('');
      inc.references.forEach(r => lines.push(`- [${r.title}](${r.url})`));
      lines.push('');
    }

    if (inc.tags && inc.tags.length > 0) {
      lines.push('**Tags:** ' + inc.tags.map(t => '`' + t + '`').join(' '));
      lines.push('');
    }

    lines.push('---');
    lines.push('');
  }

  lines.push(`_Generated by [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) · CC BY-SA 4.0 · ${date}_`);
  return lines.join('\n');
}

// ── CSV renderer ──────────────────────────────────────────────────────────────

function csvEsc(v) {
  const s = String(v ?? '').replace(/"/g, '""');
  return /[,"\n\r]/.test(s) ? `"${s}"` : s;
}

function renderCSV(incidents) {
  const rows = [];
  rows.push(['ID', 'Title', 'Date', 'Year', 'Severity', 'Category',
    'OWASP_Entries', 'MAESTRO_Layers', 'MAESTRO_Roles', 'Attack_Vector',
    'Impact', 'Tags'].join(','));

  for (const inc of incidents) {
    const layers = inc.maestro_layers.map(l => l.layer).join('|');
    const roles  = inc.maestro_layers.map(l => `${l.layer}:${l.role}`).join('|');
    rows.push([
      inc.id, inc.title, inc.date, inc.year, inc.severity, inc.category,
      inc.owasp_entries.join('|'), layers, roles,
      inc.attack_vector, inc.impact,
      (inc.tags || []).join('|'),
    ].map(csvEsc).join(','));
  }

  return rows.join('\n');
}

// ── JSON renderer ─────────────────────────────────────────────────────────────

function renderJSON(db, incidents) {
  return JSON.stringify({
    version:   db.version,
    generated: new Date().toISOString().slice(0, 10),
    total:     incidents.length,
    incidents,
  }, null, 2);
}

// ── STIX 2.1 renderer ─────────────────────────────────────────────────────────

function renderSTIX(db, incidents) {
  // Produce a STIX 2.1 bundle
  // Use crypto.randomUUID() for UUIDs (Node 18 built-in)
  // Bundle contains:
  //   - One "report" object per incident
  //   - One "attack-pattern" object per unique OWASP entry referenced
  //   - One "relationship" (uses) between each report and its attack-patterns

  const bundle = {
    type: "bundle",
    id: `bundle--${crypto.randomUUID()}`,
    objects: []
  };

  // Build attack-pattern objects for each unique OWASP entry
  const owaspEntries = new Set(incidents.flatMap(i => i.owasp_entries));
  const apMap = {}; // entry ID -> STIX ID
  for (const entry of owaspEntries) {
    const id = `attack-pattern--${crypto.randomUUID()}`;
    apMap[entry] = id;
    bundle.objects.push({
      type: "attack-pattern",
      spec_version: "2.1",
      id,
      created: new Date().toISOString(),
      modified: new Date().toISOString(),
      name: entry,
      description: `OWASP GenAI Crosswalk — ${entry}`,
      external_references: [
        {
          source_name: "owasp-genai-crosswalk",
          external_id: entry,
          url: `https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk`
        }
      ],
      kill_chain_phases: [] // empty for now
    });
  }

  // Build report + relationship objects for each incident
  for (const inc of incidents) {
    const reportId = `report--${crypto.randomUUID()}`;
    const apRefs = inc.owasp_entries.map(e => apMap[e]).filter(Boolean);

    bundle.objects.push({
      type: "report",
      spec_version: "2.1",
      id: reportId,
      created: inc.date ? new Date(inc.date + '-01').toISOString() : new Date().toISOString(),
      modified: new Date().toISOString(),
      name: `${inc.id}: ${inc.title}`,
      description: inc.description,
      published: inc.date ? new Date(inc.date + '-01').toISOString() : new Date().toISOString(),
      report_types: [inc.category === 'real-world' ? 'threat-report' : 'attack-pattern'],
      labels: inc.tags || [],
      object_refs: apRefs,
      external_references: (inc.references || []).map(r => ({
        source_name: r.type,
        url: r.url,
        description: r.title
      })),
      extensions: {
        "extension-definition--genai-crosswalk": {
          extension_type: "property-extension",
          incident_id: inc.id,
          severity: inc.severity,
          owasp_entries: inc.owasp_entries,
          maestro_layers: inc.maestro_layers,
          attack_vector: inc.attack_vector,
          affected: inc.affected,
          impact: inc.impact,
          mitigations: inc.mitigations
        }
      }
    });

    // Add relationships
    for (const apId of apRefs) {
      bundle.objects.push({
        type: "relationship",
        spec_version: "2.1",
        id: `relationship--${crypto.randomUUID()}`,
        created: new Date().toISOString(),
        modified: new Date().toISOString(),
        relationship_type: "uses",
        source_ref: reportId,
        target_ref: apId
      });
    }
  }

  return JSON.stringify(bundle, null, 2);
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function groupBy(arr, fn) {
  const result = {};
  for (const item of arr) {
    const key = fn(item);
    if (!result[key]) result[key] = [];
    result[key].push(item);
  }
  return result;
}

function writeOutput(content, filename, format, outDir, toStdout) {
  if (toStdout) { process.stdout.write(content + '\n'); return null; }
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const ext  = format === 'csv' ? '.csv' : format === 'json' ? '.json' : format === 'stix' ? '.stix.json' : '.md';
  const file = path.join(outDir, filename + ext);
  fs.writeFileSync(file, content, 'utf8');
  return file;
}

// ── Main ──────────────────────────────────────────────────────────────────────

function main() {
  const opts = parseArgs();
  const { db, incidents } = loadIncidents(opts);

  if (incidents.length === 0) {
    console.log('No incidents match the specified filters.');
    process.exit(0);
  }

  let content;
  if (opts.format === 'csv') {
    content = renderCSV(incidents);
  } else if (opts.format === 'json') {
    content = renderJSON(db, incidents);
  } else if (opts.format === 'stix') {
    content = renderSTIX(db, incidents);
  } else {
    content = renderMarkdown(db, incidents, opts);
  }

  // Filename
  const parts = ['incidents'];
  if (opts.entry)    parts.push(opts.entry.toLowerCase());
  if (opts.layer)    parts.push(opts.layer.toLowerCase());
  if (opts.severity) parts.push(opts.severity.toLowerCase());
  if (opts.category) parts.push(opts.category.replace(/-/g, ''));
  const filename = parts.join('-');

  const file = writeOutput(content, filename, opts.format, opts.out, opts.stdout);

  if (!opts.stdout) {
    console.log(`\nIncident report generated — ${new Date().toISOString().slice(0, 10)}`);
    console.log(`Incidents : ${incidents.length}${db.incidents.length !== incidents.length ? ` (filtered from ${db.incidents.length})` : ''}`);
    console.log(`Format    : ${opts.format}`);
    if (file) console.log(`Output    : ${path.relative(REPO_ROOT, file)}`);
    console.log('');
  }
}

main();
