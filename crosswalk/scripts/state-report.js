#!/usr/bin/env node
/**
 * Generate State of GenAI Security statistics from live data.
 * Used to keep the report and press kit current.
 *
 * Usage:
 *   node scripts/state-report.js              # print stats
 *   node scripts/state-report.js --json       # JSON output
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const incidents = JSON.parse(fs.readFileSync(path.join(ROOT, "data/incidents.json"), "utf-8"));
const entriesDir = path.join(ROOT, "data/entries");
const fwDir = path.join(ROOT, "data/frameworks");

// Incident stats
const byEntry = {}, byCat = {}, byYear = {}, bySev = {};
const layerOrigin = {};
for (const inc of incidents.incidents) {
  byCat[inc.category] = (byCat[inc.category] || 0) + 1;
  byYear[inc.year] = (byYear[inc.year] || 0) + 1;
  bySev[inc.severity] = (bySev[inc.severity] || 0) + 1;
  for (const e of inc.owasp_entries) byEntry[e] = (byEntry[e] || 0) + 1;
  for (const l of inc.maestro_layers || []) {
    if (l.role === "origin") {
      const key = `${l.layer} ${l.label}`;
      layerOrigin[key] = (layerOrigin[key] || 0) + 1;
    }
  }
}

// Framework stats
const fwFiles = fs.readdirSync(fwDir).filter(f => f.endsWith(".json"));
let totalControls = 0;
fwFiles.forEach(f => {
  totalControls += JSON.parse(fs.readFileSync(path.join(fwDir, f))).controls.length;
});

// Entry stats
const entryFiles = fs.readdirSync(entriesDir).filter(f => f.endsWith(".json"));
let totalMappings = 0;
entryFiles.forEach(f => {
  const e = JSON.parse(fs.readFileSync(path.join(entriesDir, f)));
  totalMappings += (e.mappings || []).length;
});

const stats = {
  generated: new Date().toISOString().slice(0, 10),
  version: incidents.version,
  totals: {
    incidents: incidents.incidents.length,
    frameworks: fwFiles.length,
    controls: totalControls,
    entries: entryFiles.length,
    mappings: totalMappings,
  },
  incidents: {
    by_category: byCat,
    by_severity: bySev,
    by_year: byYear,
    top_entries: Object.entries(byEntry).sort((a, b) => b[1] - a[1]).slice(0, 10)
      .map(([id, count]) => ({ id, count })),
    origin_layers: Object.entries(layerOrigin).sort((a, b) => b[1] - a[1])
      .map(([layer, count]) => ({ layer, count })),
  },
  key_findings: {
    prompt_injection_pct: Math.round((byEntry["LLM01"] || 0) / incidents.incidents.length * 100),
    critical_pct: Math.round((bySev["Critical"] || 0) / incidents.incidents.length * 100),
    agentic_incident_count: incidents.incidents.filter(i =>
      i.owasp_entries.some(e => e.startsWith("ASI"))
    ).length,
    supply_chain_count: incidents.incidents.filter(i =>
      i.owasp_entries.includes("ASI04")
    ).length,
  },
};

if (process.argv.includes("--json")) {
  console.log(JSON.stringify(stats, null, 2));
} else {
  console.log("╔══════════════════════════════════════════════════╗");
  console.log("║     State of GenAI Security — Live Stats        ║");
  console.log("╚══════════════════════════════════════════════════╝");
  console.log();
  console.log(`  Incidents:    ${stats.totals.incidents}`);
  console.log(`  Frameworks:   ${stats.totals.frameworks}`);
  console.log(`  Controls:     ${stats.totals.controls}`);
  console.log(`  Entries:      ${stats.totals.entries}`);
  console.log(`  Mappings:     ${stats.totals.mappings}`);
  console.log();
  console.log("  Categories:");
  Object.entries(byCat).forEach(([k, v]) => console.log(`    ${k}: ${v}`));
  console.log();
  console.log("  Key Findings:");
  console.log(`    Prompt injection in ${stats.key_findings.prompt_injection_pct}% of incidents`);
  console.log(`    ${stats.key_findings.critical_pct}% are Critical severity`);
  console.log(`    ${stats.key_findings.agentic_incident_count} incidents involve agentic AI`);
  console.log(`    ${stats.key_findings.supply_chain_count} supply chain incidents`);
  console.log();
  console.log("  Top 5 Most Exploited:");
  stats.incidents.top_entries.slice(0, 5).forEach((e, i) =>
    console.log(`    ${i + 1}. ${e.id}: ${e.count} incidents`)
  );
}
