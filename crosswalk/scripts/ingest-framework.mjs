#!/usr/bin/env node
/**
 * ingest-framework.mjs — Ingest a framework source into data/frameworks/<id>.json
 *
 * Usage:
 *   node scripts/ingest-framework.mjs <source>            # JSON file
 *   node scripts/ingest-framework.mjs <source> --validate  # validate only, no write
 *   node scripts/ingest-framework.mjs --list               # list all registered frameworks
 *
 * Source can be:
 *   - A local JSON file conforming to framework-schema.json
 *   - A local CSV file with columns: control_id, title, description, parent, function
 *
 * The script normalizes the input, validates against framework-schema.json,
 * and writes the result to data/frameworks/<id>.json.
 */

import { readFileSync, writeFileSync, readdirSync, existsSync } from 'fs';
import { resolve, dirname, extname, basename } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT = resolve(__dirname, '..');
const FW_DIR = resolve(ROOT, 'data', 'frameworks');
const SCHEMA_PATH = resolve(ROOT, 'data', 'framework-schema.json');

// ─── Helpers ─────────────────────────────────────────────────────────────────

function loadSchema() {
  return JSON.parse(readFileSync(SCHEMA_PATH, 'utf8'));
}

function parseCSV(text) {
  const lines = text.trim().split('\n');
  if (lines.length < 2) throw new Error('CSV must have a header row and at least one data row');
  const headers = lines[0].split(',').map(h => h.trim().replace(/^"|"$/g, ''));
  return lines.slice(1).map(line => {
    const values = [];
    let current = '';
    let inQuotes = false;
    for (const char of line) {
      if (char === '"') { inQuotes = !inQuotes; continue; }
      if (char === ',' && !inQuotes) { values.push(current.trim()); current = ''; continue; }
      current += char;
    }
    values.push(current.trim());
    const obj = {};
    headers.forEach((h, i) => { obj[h] = values[i] || ''; });
    return obj;
  });
}

function validateFramework(fw, schema) {
  const errors = [];
  // Required fields
  for (const field of schema.required || []) {
    if (fw[field] === undefined || fw[field] === null) {
      errors.push(`Missing required field: ${field}`);
    }
  }
  // id pattern
  if (fw.id && !/^[a-z0-9][a-z0-9-]*$/.test(fw.id)) {
    errors.push(`id "${fw.id}" does not match pattern ^[a-z0-9][a-z0-9-]*$`);
  }
  // category enum
  const cats = schema.properties?.category?.enum || [];
  if (fw.category && cats.length && !cats.includes(fw.category)) {
    errors.push(`category "${fw.category}" not in enum: ${cats.join(', ')}`);
  }
  // controls
  if (!Array.isArray(fw.controls)) {
    errors.push('controls must be an array');
  } else {
    const ids = new Set();
    fw.controls.forEach((c, i) => {
      if (!c.control_id) errors.push(`controls[${i}]: missing control_id`);
      if (!c.title) errors.push(`controls[${i}]: missing title`);
      if (ids.has(c.control_id)) errors.push(`controls[${i}]: duplicate control_id "${c.control_id}"`);
      ids.add(c.control_id);
      // Validate parent references
      if (c.parent && !fw.controls.some(p => p.control_id === c.parent)) {
        errors.push(`controls[${i}]: parent "${c.parent}" not found in controls`);
      }
    });
  }
  return errors;
}

// ─── Commands ────────────────────────────────────────────────────────────────

function listFrameworks() {
  if (!existsSync(FW_DIR)) {
    console.log('No frameworks directory found.');
    return;
  }
  const files = readdirSync(FW_DIR).filter(f => f.endsWith('.json'));
  if (!files.length) {
    console.log('No framework files found.');
    return;
  }
  console.log(`\n  Registered frameworks (${files.length}):\n`);
  const pad = (s, n) => String(s).padEnd(n);
  console.log(`  ${pad('ID', 20)} ${pad('Name', 30)} ${pad('Controls', 10)} Last Synced`);
  console.log('  ' + '─'.repeat(75));
  for (const f of files.sort()) {
    try {
      const fw = JSON.parse(readFileSync(resolve(FW_DIR, f), 'utf8'));
      console.log(`  ${pad(fw.id || '?', 20)} ${pad((fw.name || '?').slice(0, 28), 30)} ${pad((fw.controls || []).length, 10)} ${fw.last_synced || '?'}`);
    } catch { console.log(`  ${pad(f, 20)} (parse error)`); }
  }
  console.log();
}

function ingest(sourcePath, validateOnly) {
  const ext = extname(sourcePath).toLowerCase();
  let fw;

  if (ext === '.json') {
    fw = JSON.parse(readFileSync(sourcePath, 'utf8'));
  } else if (ext === '.csv') {
    // CSV mode: requires a companion metadata object or prompts
    const rows = parseCSV(readFileSync(sourcePath, 'utf8'));
    const id = basename(sourcePath, ext);
    fw = {
      id: id,
      name: id,
      short_name: id,
      version: 'unknown',
      url: '',
      license: 'unknown',
      publisher: 'unknown',
      category: 'ai-governance',
      last_synced: new Date().toISOString().split('T')[0],
      source_sha: null,
      controls: rows.map(r => ({
        control_id: r.control_id || r.id || '',
        title: r.title || r.name || '',
        description: r.description || '',
        parent: r.parent || null,
        function: r.function || r.domain || null
      })),
      changelog: [{ date: new Date().toISOString().split('T')[0], change: 'Ingested from CSV', author: 'ingest-framework.mjs' }]
    };
    console.log(`Parsed ${rows.length} controls from CSV`);
  } else {
    console.error(`Unsupported file type: ${ext}. Use .json or .csv`);
    process.exit(1);
  }

  // Set last_synced if not present
  if (!fw.last_synced) {
    fw.last_synced = new Date().toISOString().split('T')[0];
  }

  // Validate
  const schema = loadSchema();
  const errors = validateFramework(fw, schema);
  if (errors.length) {
    console.error(`\n  Validation errors (${errors.length}):\n`);
    errors.forEach(e => console.error(`    ✗ ${e}`));
    console.error();
    process.exit(1);
  }
  console.log(`  ✓ Validation passed: ${fw.id} — ${fw.name} (${fw.controls.length} controls)`);

  if (validateOnly) {
    console.log('  (validate-only mode, no file written)');
    return;
  }

  // Write
  const outPath = resolve(FW_DIR, `${fw.id}.json`);
  const existed = existsSync(outPath);
  writeFileSync(outPath, JSON.stringify(fw, null, 2) + '\n', 'utf8');
  console.log(`  ${existed ? 'Updated' : 'Created'}: ${outPath}`);
  console.log(`  Controls: ${fw.controls.length}`);
  const functions = [...new Set(fw.controls.map(c => c.function).filter(Boolean))];
  if (functions.length) console.log(`  Functions: ${functions.join(', ')}`);
  console.log();
}

// ─── CLI ─────────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);

if (args.includes('--list') || args.includes('-l')) {
  listFrameworks();
} else if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
  console.log(`
  ingest-framework.mjs — Ingest a framework source into the registry

  Usage:
    node scripts/ingest-framework.mjs <source.json|source.csv>  [--validate]
    node scripts/ingest-framework.mjs --list

  Options:
    --validate   Validate only, do not write
    --list       List all registered frameworks
    --help       Show this help
  `);
} else {
  const source = args.find(a => !a.startsWith('-'));
  if (!source) { console.error('No source file provided.'); process.exit(1); }
  const sourcePath = resolve(process.cwd(), source);
  if (!existsSync(sourcePath)) { console.error(`File not found: ${sourcePath}`); process.exit(1); }
  ingest(sourcePath, args.includes('--validate'));
}
