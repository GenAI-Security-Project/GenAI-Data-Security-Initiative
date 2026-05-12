#!/usr/bin/env node
/**
 * OWASP GenAI Crosswalk — CLI Query Interface
 * ──────────────────────────────────────────────────────────────────────────
 * Query the crosswalk data layer from the command line — replaces jq.
 *
 * Usage:
 *   node scripts/query.js --severity Critical
 *   node scripts/query.js --framework "EU AI Act"
 *   node scripts/query.js --entry LLM01
 *   node scripts/query.js --entry LLM01 --tools
 *   node scripts/query.js --entry LLM01 --incidents
 *   node scripts/query.js --source-list Agentic
 *   node scripts/query.js --aivss-above 8.0
 *   node scripts/query.js --framework-coverage
 *   node scripts/query.js --incident-search "deepfake"
 *   node scripts/query.js --stats
 *
 * Flags:
 *   --entry <ID>            Show full entry (LLM01, ASI01, DSGAI04, etc.)
 *   --severity <level>      Filter: Critical | High | Medium | Low
 *   --framework <name>      Filter entries by framework (partial match)
 *   --source-list <name>    Filter: LLM | Agentic | DSGAI
 *   --aivss-above <score>   Entries with AIVSS score above threshold
 *   --tools                 Show tools for selected entries
 *   --incidents             Show incidents for selected entries
 *   --mappings              Show mappings for selected entries
 *   --framework-coverage    Framework × source list coverage matrix
 *   --incident-search <q>   Search incidents by keyword
 *   --stats                 Summary statistics
 *   --format <fmt>          json | table | csv  (default: table)
 *   --json                  Shorthand for --format json
 * ────────———─────────────────────——───────────────────────────────────────────
 */

'use strict';

const fs   = require('fs');
const path = require('path');

const ROOT        = path.resolve(__dirname, '..');
const ENTRIES_DIR = path.join(ROOT, 'data', 'entries');
const INCIDENTS   = path.join(ROOT, 'data', 'incidents.json');

// ── Args ────────────────────────────────────——────────────────────────────────

function parseArgs() {
  const args = process.argv.slice(2);
  const opts = {
    entry: null, severity: null, framework: null, sourceList: null,
    aivssAbove: null, tools: false, incidents: false, mappings: false,
    frameworkCoverage: false, incidentSearch: null, stats: false,
    format: 'table',
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--entry':              opts.entry = args[++i].toUpperCase(); break;
      case '--severity':           opts.severity = args[++i]; break;
      case '--framework':          opts.framework = args[++i]; break;
      case '--source-list':        opts.sourceList = args[++i]; break;
      case '--aivss-above':        opts.aivssAbove = parseFloat(args[++i]); break;
      case '--tools':              opts.tools = true; break;
      case '--incidents':          opts.incidents = true; break;
      case '--mappings':           opts.mappings = true; break;
      case '--framework-coverage': opts.frameworkCoverage = true; break;
      case '--incident-search':    opts.incidentSearch = args[++i]; break;
      case '--stats':              opts.stats = true; break;
      case '--format':             opts.format = args[++i]; break;
      case '--json':               opts.format = 'json'; break;
      case '--help': case '-h':    printHelp(); process.exit(0);
      default:
        if (args[i].startsWith('--')) {
          console.error(`Unknown flag: ${args[i]}. Use --help for usage.`);
          process.exit(1);
        }
    }
  }
  return opts;
}

function printHelp() {
  const help = fs.readFileSync(__filename, 'utf8')
    .split('\n').filter(l => l.startsWith(' *')).map(l => l.replace(/^ \* ?/, '')).join('\n');
  console.log(help);
}

// ── Data ──———────────────────────────────———─────────────────────────────────────

function loadEntries() {
  return fs.readdirSync(ENTRIES_DIR)
    .filter(f => f.endsWith('.json'))
    .map(f => JSON.parse(fs.readFileSync(path.join(ENTRIES_DIR, f), 'utf8')))
    .sort((a, b) => a.id.localeCompare(b.id));
}

function loadIncidents() {
  if (!fs.existsSync(INCIDENTS)) return [];
  return JSON.parse(fs.readFileSync(INCIDENTS, 'utf8')).incidents || [];
}

// ── Formatters ──────——──────────────────────────────——─────────────────────────

function formatTable(headers, rows) {
  const widths = headers.map((h, i) =>
    Math.max(h.length, ...rows.map(r => String(r[i] || '').length))
  );
  const sep = widths.map(w => '─'.repeat(w + 2)).join('┼');
  const line = (cells) => cells.map((c, i) => ` ${String(c || '').padEnd(widths[i])} `).join('│');

  console.log(line(headers));
  console.log(sep);
  rows.forEach(r => console.log(line(r)));
  console.log(`\n${rows.length} result(s)`);
}

function formatCSV(headers, rows) {
  const escape = (s) => `"${String(s || '').replace(/"/g, '""')}"`;
  console.log(headers.map(escape).join(','));
  rows.forEach(r => console.log(r.map(escape).join(',')));
}

function output(headers, rows, format) {
  if (format === 'json') {
    const objs = rows.map(r => {
      const o = {};
      headers.forEach((h, i) => { o[h] = r[i]; });
      return o;
    });
    console.log(JSON.stringify(objs, null, 2));
  } else if (format === 'csv') {
    formatCSV(headers, rows);
  } else {
    formatTable(headers, rows);
  }
}

// ── Commands ─────────────────────────────────────────────────────────────────

function showStats(entries, incidents) {
  const fws = new Set();
  let totalMappings = 0;
  entries.forEach(e => e.mappings.forEach(m => { fws.add(m.framework); totalMappings++; }));

  const bySev = {};
  entries.forEach(e => { bySev[e.severity] = (bySev[e.severity] || 0) + 1; });

  const bySrc = {};
  entries.forEach(e => { bySrc[e.source_list] = (bySrc[e.source_list] || 0) + 1; });

  console.log('\nOWASP GenAI Crosswalk — Summary Statistics');
  console.log('═'.repeat(50));
  console.log(`  Entries        : ${entries.length}`);
  console.log(`  Frameworks     : ${fws.size}`);
  console.log(`  Total mappings : ${totalMappings}`);
  console.log(`  Avg mappings   : ${Math.round(totalMappings / entries.length)} per entry`);
  console.log(`  Incidents      : ${incidents.length}`);
  console.log('');
  console.log('  By severity:');
  ['Critical', 'High', 'Medium', 'Low'].forEach(s => {
    if (bySev[s]) console.log(`    ${s.padEnd(10)} ${bySev[s]}`);
  });
  console.log('');
  console.log('  By source list:');
  Object.entries(bySrc).forEach(([k, v]) => console.log(`    ${k.padEnd(25)} ${v}`));
  console.log('');
}

function showFrameworkCoverage(entries, format) {
  const matrix = {};
  entries.forEach(e => {
    e.mappings.forEach(m => {
      if (!matrix[m.framework]) matrix[m.framework] = new Set();
      matrix[m.framework].add(e.source_list);
    });
  });

  const headers = ['Framework', 'LLM Top 10', 'Agentic Top 10', 'DSGAI 2026', 'Total entries'];
  const rows = Object.entries(matrix)
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([fw, sources]) => {
      const llm = entries.filter(e => e.source_list === 'LLM-Top10-2025' && e.mappings.some(m => m.framework === fw)).length;
      const asi = entries.filter(e => e.source_list === 'Agentic-Top10-2026' && e.mappings.some(m => m.framework === fw)).length;
      const dsg = entries.filter(e => e.source_list === 'DSGAI-2026' && e.mappings.some(m => m.framework === fw)).length;
      return [fw, llm ? `✅ ${llm}` : '—', asi ? `✅ ${asi}` : '—', dsg ? `✅ ${dsg}` : '—', llm + asi + dsg];
    });

  output(headers, rows, format);
}

function showEntry(entries, incidents, id, opts) {
  const entry = entries.find(e => e.id === id);
  if (!entry) { console.error(`Entry not found: ${id}`); process.exit(1); }

  if (opts.format === 'json') {
    console.log(JSON.stringify(entry, null, 2));
    return;
  }

  console.log(`\n${entry.id} — ${entry.name}`);
  console.log('═'.repeat(50));
  console.log(`  Source list : ${entry.source_list}`);
  console.log(`  Severity   : ${entry.severity}`);
  if (entry.aivss_score) console.log(`  AIVSS score: ${entry.aivss_score}`);
  console.log(`  Mappings   : ${entry.mappings.length} controls across ${new Set(entry.mappings.map(m => m.framework)).size} frameworks`);
  console.log(`  Tools      : ${(entry.tools || []).length}`);
  console.log(`  Incidents  : ${(entry.incidents || []).length}`);
  console.log(`  Audience   : ${(entry.audience || []).join(', ')}`);

  if (opts.tools && entry.tools && entry.tools.length > 0) {
    console.log('\n  Tools:');
    entry.tools.forEach(t => console.log(`    • ${t.name} — ${t.url}`));
  }

  if (opts.incidents) {
    const entryIncidents = incidents.filter(i => i.owasp_entries.includes(id));
    if (entryIncidents.length > 0) {
      console.log('\n  Incidents:');
      entryIncidents.forEach(i => console.log(`    • ${i.id}: ${i.title} (${i.date}, ${i.severity})`));
    }
  }

  if (opts.mappings) {
    console.log('\n  Framework mappings:');
    const byFw = {};
    entry.mappings.forEach(m => {
      if (!byFw[m.framework]) byFw[m.framework] = [];
      byFw[m.framework].push(m);
    });
    Object.entries(byFw).sort((a, b) => a[0].localeCompare(b[0])).forEach(([fw, maps]) => {
      console.log(`\n    ${fw} (${maps.length} controls):`);
      maps.forEach(m => {
        const id = m.control_id || m.control_name || '';
        const name = m.control_name && m.control_name !== id ? ` — ${m.control_name}` : '';
        console.log(`      ${id}${name}`);
      });
    });
  }
  console.log('');
}

function searchIncidents(incidents, query, format) {
  const q = query.toLowerCase();
  const matched = incidents.filter(i =>
    i.title.toLowerCase().includes(q) ||
    i.description.toLowerCase().includes(q) ||
    i.tags.some(t => t.toLowerCase().includes(q)) ||
    i.attack_vector.toLowerCase().includes(q)
  );

  if (format === 'json') {
    console.log(JSON.stringify(matched, null, 2));
    return;
  }

  const headers = ['ID', 'Title', 'Date', 'Severity', 'Category', 'Entries'];
  const rows = matched.map(i => [
    i.id, i.title.slice(0, 60), i.date, i.severity, i.category, i.owasp_entries.join(', ')
  ]);
  output(headers, rows, format);
}

// ── Main ─────────────────────——────────────────────────———──────────────────────

function main() {
  const opts = parseArgs();
  const entries = loadEntries();
  const incidents = loadIncidents();

  // Stats
  if (opts.stats) { showStats(entries, incidents); return; }

  // Framework coverage matrix
  if (opts.frameworkCoverage) { showFrameworkCoverage(entries, opts.format); return; }

  // Incident search
  if (opts.incidentSearch) { searchIncidents(incidents, opts.incidentSearch, opts.format); return; }

  // Single entry detail
  if (opts.entry && !opts.severity && !opts.framework && !opts.sourceList && !opts.aivssAbove) {
    showEntry(entries, incidents, opts.entry, opts);
    return;
  }

  // Filter entries
  let filtered = entries;
  if (opts.entry)      filtered = filtered.filter(e => e.id === opts.entry);
  if (opts.severity)   filtered = filtered.filter(e => e.severity === opts.severity);
  if (opts.sourceList) {
    const q = opts.sourceList.toLowerCase();
    filtered = filtered.filter(e => e.source_list.toLowerCase().includes(q));
  }
  if (opts.framework) {
    const q = opts.framework.toLowerCase();
    filtered = filtered.filter(e => e.mappings.some(m => m.framework.toLowerCase().includes(q)));
  }
  if (opts.aivssAbove) {
    filtered = filtered.filter(e => e.aivss_score && e.aivss_score > opts.aivssAbove);
  }

  if (filtered.length === 0) {
    console.log('No entries match the specified filters.');
    return;
  }

  // Output mode
  if (opts.tools) {
    const headers = ['Entry', 'Tool', 'Type', 'URL'];
    const rows = filtered.flatMap(e =>
      (e.tools || []).map(t => [e.id, t.name, t.type || '', t.url])
    );
    output(headers, rows, opts.format);
    return;
  }

  if (opts.incidents) {
    const entryIds = new Set(filtered.map(e => e.id));
    const matched = incidents.filter(i => i.owasp_entries.some(e => entryIds.has(e)));
    const headers = ['ID', 'Title', 'Date', 'Severity', 'Entries'];
    const rows = matched.map(i => [
      i.id, i.title.slice(0, 55), i.date, i.severity, i.owasp_entries.filter(e => entryIds.has(e)).join(', ')
    ]);
    output(headers, rows, opts.format);
    return;
  }

  // Default: list entries
  const headers = ['ID', 'Name', 'Severity', 'Source List', 'Mappings', 'Tools', 'Incidents'];
  const rows = filtered.map(e => [
    e.id, e.name, e.severity, e.source_list,
    e.mappings.length, (e.tools || []).length, (e.incidents || []).length
  ]);
  output(headers, rows, opts.format);
}

main();
