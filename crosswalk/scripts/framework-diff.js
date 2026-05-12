#!/usr/bin/env node
/**
 * Diff-aware framework versioning.
 *
 * Compares two versions of a framework registry file and generates a
 * changelog showing new, removed, and modified controls. Optionally
 * proposes classifier mappings for new controls only (the delta).
 *
 * Usage:
 *   node scripts/framework-diff.js --old data/frameworks/nist-ai-rmf.json --new updated-nist-ai-rmf.json
 *   node scripts/framework-diff.js --old data/frameworks/nist-ai-rmf.json --new updated.json --apply
 *   node scripts/framework-diff.js --git data/frameworks/eu-ai-act.json   # diff against last commit
 */

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const args = process.argv.slice(2);
const flags = {};
const positional = [];

for (let i = 0; i < args.length; i++) {
  if (args[i] === "--old" && args[i + 1]) flags.old = args[++i];
  else if (args[i] === "--new" && args[i + 1]) flags.new = args[++i];
  else if (args[i] === "--git" && args[i + 1]) flags.git = args[++i];
  else if (args[i] === "--apply") flags.apply = true;
  else if (args[i] === "--json") flags.json = true;
  else positional.push(args[i]);
}

function loadJson(filepath) {
  return JSON.parse(fs.readFileSync(filepath, "utf-8"));
}

function loadGitVersion(filepath) {
  try {
    const content = execFileSync("git", ["show", "HEAD:" + filepath], {
      encoding: "utf-8",
      stdio: ["pipe", "pipe", "pipe"],
    });
    return JSON.parse(content);
  } catch {
    return null;
  }
}

function diffFrameworks(oldFw, newFw) {
  const oldMap = new Map();
  for (const c of oldFw.controls || []) {
    oldMap.set(c.control_id, c);
  }

  const newMap = new Map();
  for (const c of newFw.controls || []) {
    newMap.set(c.control_id, c);
  }

  const added = [];
  const removed = [];
  const modified = [];

  // New controls
  for (const [id, ctrl] of newMap) {
    if (!oldMap.has(id)) {
      added.push(ctrl);
    } else {
      const old = oldMap.get(id);
      const changes = [];
      if (old.title !== ctrl.title) changes.push({ field: "title", from: old.title, to: ctrl.title });
      if ((old.description || "") !== (ctrl.description || "")) changes.push({ field: "description", from: old.description, to: ctrl.description });
      if ((old.function || null) !== (ctrl.function || null)) changes.push({ field: "function", from: old.function, to: ctrl.function });
      if ((old.parent || null) !== (ctrl.parent || null)) changes.push({ field: "parent", from: old.parent, to: ctrl.parent });
      if (changes.length > 0) {
        modified.push({ control_id: id, changes, old, new: ctrl });
      }
    }
  }

  // Removed controls
  for (const [id, ctrl] of oldMap) {
    if (!newMap.has(id)) {
      removed.push(ctrl);
    }
  }

  return {
    framework: newFw.name || oldFw.name,
    old_version: oldFw.version,
    new_version: newFw.version,
    summary: {
      added: added.length,
      removed: removed.length,
      modified: modified.length,
      unchanged: newMap.size - added.length - modified.length,
    },
    added,
    removed,
    modified,
  };
}

function formatDiff(diff) {
  const lines = [];
  lines.push(`Framework: ${diff.framework}`);
  lines.push(`Version:   ${diff.old_version} → ${diff.new_version}`);
  lines.push(`─────────────────────────────────────────────`);
  lines.push(`  Added:     ${diff.summary.added}`);
  lines.push(`  Removed:   ${diff.summary.removed}`);
  lines.push(`  Modified:  ${diff.summary.modified}`);
  lines.push(`  Unchanged: ${diff.summary.unchanged}`);
  lines.push("");

  if (diff.added.length > 0) {
    lines.push("NEW CONTROLS:");
    for (const c of diff.added) {
      lines.push(`  + ${c.control_id}: ${c.title}`);
      if (c.description) lines.push(`    ${c.description.substring(0, 100)}`);
    }
    lines.push("");
  }

  if (diff.removed.length > 0) {
    lines.push("REMOVED CONTROLS:");
    for (const c of diff.removed) {
      lines.push(`  - ${c.control_id}: ${c.title}`);
    }
    lines.push("");
  }

  if (diff.modified.length > 0) {
    lines.push("MODIFIED CONTROLS:");
    for (const m of diff.modified) {
      lines.push(`  ~ ${m.control_id}:`);
      for (const ch of m.changes) {
        lines.push(`    ${ch.field}: "${(ch.from || "").substring(0, 50)}" → "${(ch.to || "").substring(0, 50)}"`);
      }
    }
    lines.push("");
  }

  return lines.join("\n");
}

function addChangelog(fwPath, diff) {
  const fw = loadJson(fwPath);
  if (!fw.changelog) fw.changelog = [];

  const entry = {
    date: new Date().toISOString().slice(0, 10),
    change: `Version ${diff.old_version} → ${diff.new_version}: +${diff.summary.added} controls, -${diff.summary.removed} controls, ~${diff.summary.modified} modified`,
    author: "framework-diff",
  };

  // Add detail for added/removed
  if (diff.added.length > 0) {
    entry.added = diff.added.map((c) => c.control_id);
  }
  if (diff.removed.length > 0) {
    entry.removed = diff.removed.map((c) => c.control_id);
  }
  if (diff.modified.length > 0) {
    entry.modified = diff.modified.map((m) => m.control_id);
  }

  fw.changelog.unshift(entry);
  fw.version = diff.new_version;
  fw.last_synced = new Date().toISOString().slice(0, 10);

  fs.writeFileSync(fwPath, JSON.stringify(fw, null, 2) + "\n", "utf-8");
  console.log(`Updated ${fwPath} with changelog entry`);
}

// ── Main ────────────────────────────────────────────────────────────────────

function main() {
  let oldFw, newFw, fwPath;

  if (flags.git) {
    // Diff against git HEAD
    fwPath = flags.git;
    newFw = loadJson(fwPath);
    oldFw = loadGitVersion(fwPath);
    if (!oldFw) {
      console.log("No previous version in git — this is a new framework file.");
      console.log(`Controls: ${newFw.controls.length}`);
      return;
    }
  } else if (flags.old && flags.new) {
    oldFw = loadJson(flags.old);
    newFw = loadJson(flags.new);
    fwPath = flags.old;
  } else {
    console.log("Usage:");
    console.log("  node scripts/framework-diff.js --old old.json --new new.json [--apply] [--json]");
    console.log("  node scripts/framework-diff.js --git data/frameworks/foo.json [--apply] [--json]");
    process.exit(1);
  }

  const diff = diffFrameworks(oldFw, newFw);

  if (flags.json) {
    console.log(JSON.stringify(diff, null, 2));
  } else {
    console.log(formatDiff(diff));
  }

  if (diff.added.length > 0) {
    console.log("To propose classifier mappings for new controls only:");
    console.log(`  python -m classifier.classify --framework "${diff.framework}" --control-ids ${diff.added.map((c) => '"' + c.control_id + '"').join(" ")}`);
  }

  if (flags.apply && fwPath) {
    // Replace the old file with the new content and add changelog
    if (flags.new) {
      fs.copyFileSync(flags.new, fwPath);
    }
    addChangelog(fwPath, diff);
  }
}

main();
