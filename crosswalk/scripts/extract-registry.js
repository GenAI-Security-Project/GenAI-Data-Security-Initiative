#!/usr/bin/env node
/**
 * Extract controls from entry JSON files into the framework registry.
 *
 * Reads all data/entries/*.json, collects unique (framework, control_id,
 * control_name) triples, and creates or updates data/frameworks/*.json
 * so every ground-truth control exists in the FAISS index.
 *
 * Usage:
 *   node scripts/extract-registry.js [--dry-run]
 */

const fs = require("fs");
const path = require("path");

const DRY_RUN = process.argv.includes("--dry-run");
const ENTRIES_DIR = path.join(__dirname, "..", "data", "entries");
const FRAMEWORKS_DIR = path.join(__dirname, "..", "data", "frameworks");

// ── Framework metadata for NEW registry files ──────────────────────────────
const FRAMEWORK_META = {
  "OWASP NHI Top 10": {
    id: "owasp-nhi",
    short_name: "NHI Top 10",
    version: "1.0",
    url: "https://owasp.org/www-project-non-human-identities-top-10/",
    license: "CC BY-SA 4.0",
    publisher: "OWASP",
    category: "identity",
  },
  "PCI DSS v4.0": {
    id: "pci-dss",
    short_name: "PCI DSS",
    version: "4.0",
    url: "https://www.pcisecuritystandards.org/document_library/",
    license: "Proprietary",
    publisher: "PCI Security Standards Council",
    category: "infosec",
  },
  "CWE/CVE": {
    id: "cwe-cve",
    short_name: "CWE/CVE",
    version: "4.14",
    url: "https://cwe.mitre.org/",
    license: "Public Domain",
    publisher: "MITRE",
    category: "appsec",
  },
  "NIST SP 800-82 Rev 3": {
    id: "nist-sp-800-82",
    short_name: "SP 800-82",
    version: "Rev 3",
    url: "https://csrc.nist.gov/pubs/sp/800/82/r3/final",
    license: "Public Domain",
    publisher: "NIST",
    category: "ot-ics",
  },
  "OWASP AI Testing Guide": {
    id: "owasp-ai-testing",
    short_name: "AI Testing",
    version: "1.0",
    url: "https://owasp.org/www-project-ai-security-and-privacy-guide/",
    license: "CC BY-SA 4.0",
    publisher: "OWASP",
    category: "testing",
  },
  "NIST SP 800-218A": {
    id: "nist-sp-800-218a",
    short_name: "SP 800-218A",
    version: "1.0",
    url: "https://csrc.nist.gov/pubs/sp/800/218/a/final",
    license: "Public Domain",
    publisher: "NIST",
    category: "appsec",
  },
  "AIUC-1": {
    id: "aiuc-1",
    short_name: "AIUC-1",
    version: "1.0",
    url: "https://www.ai-safety-institute.org/",
    license: "Open Government Licence v3.0",
    publisher: "UK AI Safety Institute",
    category: "ai-governance",
  },
  "FedRAMP": {
    id: "fedramp",
    short_name: "FedRAMP",
    version: "Rev 5",
    url: "https://www.fedramp.gov/",
    license: "Public Domain",
    publisher: "GSA / FedRAMP PMO",
    category: "certification",
  },
  "OWASP SAMM v2.0": {
    id: "owasp-samm",
    short_name: "SAMM",
    version: "2.0",
    url: "https://owaspsamm.org/model/",
    license: "CC BY-SA 4.0",
    publisher: "OWASP",
    category: "appsec",
  },
  "ENISA Multilayer Framework": {
    id: "enisa-multilayer",
    short_name: "ENISA",
    version: "2023",
    url: "https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai",
    license: "Public Domain",
    publisher: "ENISA",
    category: "ai-governance",
  },
  "STRIDE": {
    id: "stride",
    short_name: "STRIDE",
    version: "2024",
    url: "https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats",
    license: "Public Domain",
    publisher: "Microsoft",
    category: "threat-model",
  },
};

// ── Main ────────────────────────────────────────────────────────────────────

function main() {
  // 1) Collect all controls from entries
  const entryFiles = fs.readdirSync(ENTRIES_DIR).filter((f) => f.endsWith(".json"));
  const frameworkControls = new Map(); // framework → Map<control_id, {title, descriptions}>

  for (const f of entryFiles) {
    const entry = JSON.parse(fs.readFileSync(path.join(ENTRIES_DIR, f), "utf-8"));
    for (const m of entry.mappings || []) {
      if (!frameworkControls.has(m.framework)) {
        frameworkControls.set(m.framework, new Map());
      }
      const controls = frameworkControls.get(m.framework);
      if (!controls.has(m.control_id)) {
        controls.set(m.control_id, {
          title: m.control_name || m.control_id,
          descriptions: new Set(),
        });
      }
      // Collect notes as description material
      if (m.notes) {
        controls.get(m.control_id).descriptions.add(m.notes);
      }
    }
  }

  console.log(`Found ${frameworkControls.size} frameworks across ${entryFiles.length} entries`);

  // 2) Load existing registry files
  const existingFiles = fs.readdirSync(FRAMEWORKS_DIR).filter((f) => f.endsWith(".json"));
  const existingByName = new Map();
  const existingByFile = new Map();

  for (const f of existingFiles) {
    const fp = path.join(FRAMEWORKS_DIR, f);
    const fw = JSON.parse(fs.readFileSync(fp, "utf-8"));
    existingByName.set(fw.name, { file: f, data: fw });
    existingByFile.set(f, fw);
  }

  let totalAdded = 0;
  let totalExisting = 0;
  let newFrameworks = 0;

  // 3) Process each framework
  for (const [fwName, controls] of frameworkControls) {
    const existing = existingByName.get(fwName);

    if (existing) {
      // UPDATE existing framework — add missing controls
      const existingIds = new Set(existing.data.controls.map((c) => c.control_id));
      let added = 0;

      for (const [controlId, info] of controls) {
        if (!existingIds.has(controlId)) {
          const desc = [...info.descriptions].slice(0, 3).join("; ");
          existing.data.controls.push({
            control_id: controlId,
            title: info.title,
            description: desc || undefined,
          });
          added++;
        }
      }

      if (added > 0) {
        existing.data.last_synced = new Date().toISOString().slice(0, 10);
        const fp = path.join(FRAMEWORKS_DIR, existing.file);
        if (!DRY_RUN) {
          fs.writeFileSync(fp, JSON.stringify(existing.data, null, 2) + "\n", "utf-8");
        }
        console.log(`  UPDATED ${existing.file}: +${added} controls (${existing.data.controls.length} total)`);
        totalAdded += added;
      } else {
        console.log(`  OK ${existing.file}: all ${controls.size} controls already present`);
      }
      totalExisting++;
    } else {
      // CREATE new framework file
      const meta = FRAMEWORK_META[fwName];
      if (!meta) {
        console.warn(`  WARN: No metadata for "${fwName}" — skipping`);
        continue;
      }

      const fwControls = [];
      for (const [controlId, info] of controls) {
        const desc = [...info.descriptions].slice(0, 3).join("; ");
        fwControls.push({
          control_id: controlId,
          title: info.title,
          ...(desc ? { description: desc } : {}),
        });
      }

      const newFw = {
        id: meta.id,
        name: fwName,
        short_name: meta.short_name,
        version: meta.version,
        url: meta.url,
        license: meta.license,
        publisher: meta.publisher,
        category: meta.category,
        last_synced: new Date().toISOString().slice(0, 10),
        source_sha: null,
        controls: fwControls,
      };

      const filename = `${meta.id}.json`;
      const fp = path.join(FRAMEWORKS_DIR, filename);
      if (!DRY_RUN) {
        fs.writeFileSync(fp, JSON.stringify(newFw, null, 2) + "\n", "utf-8");
      }
      console.log(`  CREATED ${filename}: ${fwControls.length} controls`);
      totalAdded += fwControls.length;
      newFrameworks++;
    }
  }

  console.log(`\nSummary:`);
  console.log(`  Existing frameworks updated: ${totalExisting}`);
  console.log(`  New frameworks created: ${newFrameworks}`);
  console.log(`  Total controls added: ${totalAdded}`);
  if (DRY_RUN) console.log("  (DRY RUN — no files written)");
}

main();
