#!/usr/bin/env node
/**
 * OWASP GenAI Crosswalk — Content Inventory SBOM Generator
 * Generates a CycloneDX 1.5 SBOM of all crosswalk data assets.
 * Output: sbom-content.cdx.json
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..');
const OUTPUT = path.join(ROOT, 'sbom-content.cdx.json');

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function sha256(filePath) {
  const content = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(content).digest('hex');
}

function uuidv4() {
  return crypto.randomUUID();
}

function listFiles(dir, ext) {
  const full = path.join(ROOT, dir);
  if (!fs.existsSync(full)) return [];
  return fs
    .readdirSync(full)
    .filter((f) => f.endsWith(ext))
    .sort()
    .map((f) => path.join(dir, f));
}

/**
 * Derive a framework name from a mapping file path.
 * e.g. "llm-top10/LLM_NISTAIRMF.md" -> "NIST AI RMF" (best-effort label)
 */
function frameworkFromPath(relPath) {
  const base = path.basename(relPath, '.md');
  // Strip the top-10 prefix (LLM_, Agentic_, DSGAI_)
  const parts = base.replace(/^(LLM|Agentic|DSGAI)_/, '');
  return parts;
}

/**
 * Determine which OWASP top-10 list a mapping directory belongs to.
 */
function topListFromDir(relPath) {
  if (relPath.startsWith('llm-top10')) return 'OWASP LLM Top 10';
  if (relPath.startsWith('agentic-top10')) return 'OWASP Agentic Top 10';
  if (relPath.startsWith('dsgai-2026')) return 'OWASP DSGAI 2026';
  return 'unknown';
}

// ---------------------------------------------------------------------------
// Collect components
// ---------------------------------------------------------------------------

const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, 'package.json'), 'utf8'));
const version = pkg.version;

const components = [];

// 1. Mapping files from three top-10 directories
for (const dir of ['llm-top10', 'agentic-top10', 'dsgai-2026']) {
  const files = listFiles(dir, '.md');
  for (const relPath of files) {
    const absPath = path.join(ROOT, relPath);
    const hash = sha256(absPath);
    components.push({
      type: 'data',
      name: relPath.replace(/\\/g, '/'),
      version: version,
      description: `Mapping file for ${topListFromDir(relPath)}`,
      hashes: [{ alg: 'SHA-256', content: hash }],
      properties: [
        { name: 'framework', value: frameworkFromPath(relPath) },
        { name: 'top-list', value: topListFromDir(relPath) },
      ],
    });
  }
}

// 2. Entry files (data/entries/*.json)
const entryFiles = listFiles('data/entries', '.json');
for (const relPath of entryFiles) {
  const absPath = path.join(ROOT, relPath);
  const hash = sha256(absPath);
  components.push({
    type: 'data',
    name: relPath.replace(/\\/g, '/'),
    version: version,
    description: 'Crosswalk entry data',
    hashes: [{ alg: 'SHA-256', content: hash }],
    properties: [],
  });
}

// 3. incidents.json
const incidentsPath = path.join(ROOT, 'data', 'incidents.json');
if (fs.existsSync(incidentsPath)) {
  const hash = sha256(incidentsPath);
  components.push({
    type: 'data',
    name: 'data/incidents.json',
    version: version,
    description: 'Real-world AI/LLM security incidents',
    hashes: [{ alg: 'SHA-256', content: hash }],
    properties: [],
  });
}

// ---------------------------------------------------------------------------
// Build CycloneDX 1.5 BOM
// ---------------------------------------------------------------------------

const bom = {
  bomFormat: 'CycloneDX',
  specVersion: '1.5',
  serialNumber: `urn:uuid:${uuidv4()}`,
  version: 1,
  metadata: {
    timestamp: new Date().toISOString(),
    tools: [
      {
        vendor: 'OWASP',
        name: 'OWASP GenAI Crosswalk',
        version: version,
      },
    ],
    component: {
      type: 'library',
      name: 'genai-security-crosswalk',
      version: version,
    },
  },
  components: components,
};

// ---------------------------------------------------------------------------
// Write output
// ---------------------------------------------------------------------------

fs.writeFileSync(OUTPUT, JSON.stringify(bom, null, 2) + '\n', 'utf8');

console.log(`SBOM written to ${OUTPUT}`);
console.log(`  Components: ${components.length}`);
