#!/usr/bin/env node
/**
 * OWASP GenAI Crosswalk — External Source Watcher
 * ──────────────────────────────────────────────────────────────────────────
 * Monitors OWASP repos, arXiv, NVD, and framework pages for changes.
 * Opens GitHub Issues for each new finding.
 *
 * Usage:
 *   node scripts/watch.js                     # run all watchers
 *   node scripts/watch.js --dry-run           # print findings, no issues
 *   node scripts/watch.js --watcher arxiv     # single watcher
 *   node scripts/watch.js --since 2026-01-01  # custom lookback
 *
 * Environment:
 *   GITHUB_TOKEN       Required to open issues (omit for dry-run)
 *   GITHUB_REPOSITORY  Owner/repo (default: GenAI-Security-Project/GenAI-Data-Security-Initiative)
 * ──────────────────────────────────────────────────────────────────────────
 */

'use strict';

const fs   = require('fs');
const path = require('path');
const crypto = require('crypto');

// ─── Constants ───────────────────────────────────────────────────────────────

const GITHUB_REPOSITORY = process.env.GITHUB_REPOSITORY || 'GenAI-Security-Project/GenAI-Data-Security-Initiative';
const GITHUB_TOKEN      = process.env.GITHUB_TOKEN || '';
const STATE_FILE        = path.resolve(__dirname, '..', 'data', '.watch-state.json');
const REQUEST_TIMEOUT_MS = 10_000;

const OWASP_REPOS = [
  'OWASP/www-project-top-10-for-large-language-model-applications',
  'OWASP/www-project-top-10-for-agentic-ai',
  'OWASP/www-project-top-10-for-genai-data-security',
];

const ARXIV_URL =
  'https://export.arxiv.org/api/query?' +
  'search_query=cat:cs.CR+AND+(ti:prompt+injection+OR+ti:jailbreak+OR+ti:LLM+security+OR+ti:agentic+AI+OR+ti:RAG+poisoning)' +
  '&sortBy=submittedDate&sortOrder=descending&max_results=20';

const NVD_KEYWORDS = [
  'large language model',
  'generative AI',
  'LLM injection',
];

const FRAMEWORK_CHECKS = [
  { name: 'NIST AI RMF',    url: 'https://airc.nist.gov/airmf-resources/airmf/',                                              label: 'NIST AI RMF 1.0'   },
  { name: 'NIST SP 800-218A', url: 'https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf',              label: 'NIST SP 800-218A'  },
  { name: 'CIS Controls',   url: 'https://www.cisecurity.org/controls/cis-controls-list',                                     label: 'CIS Controls v8.1' },
  { name: 'MITRE ATLAS',    url: 'https://atlas.mitre.org/',                                                                  label: 'MITRE ATLAS'       },
];

// ─── CLI Argument Parsing ─────────────────────────────────────────────────────

const argv      = process.argv.slice(2);
const DRY_RUN   = argv.includes('--dry-run');
const watcherIdx = argv.indexOf('--watcher');
const SINGLE_WATCHER = watcherIdx !== -1 ? argv[watcherIdx + 1] : null;
const sinceIdx  = argv.indexOf('--since');
const SINCE_OVERRIDE = sinceIdx !== -1 ? argv[sinceIdx + 1] : null;

// ─── State File Helpers ───────────────────────────────────────────────────────

/**
 * Load state from disk, returning a default object if the file is absent or invalid.
 */
function loadState() {
  try {
    const raw = fs.readFileSync(STATE_FILE, 'utf8');
    return JSON.parse(raw);
  } catch {
    return {
      version:    '1.0.0',
      last_run:   null,
      owasp:      {},
      arxiv:      [],
      nvd:        [],
      frameworks: {},
    };
  }
}

/**
 * Persist state to disk (no-op in dry-run mode).
 */
function saveState(state, dryRun) {
  if (dryRun) return;
  const dir = path.dirname(STATE_FILE);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2), 'utf8');
}

// ─── HTTP Helpers ─────────────────────────────────────────────────────────────

/**
 * Fetch with an AbortController-based timeout.
 * Returns { ok, status, headers, text() } shaped like the fetch Response.
 */
async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const res = await fetch(url, { ...options, signal: controller.signal });
    return res;
  } finally {
    clearTimeout(timer);
  }
}

/**
 * Build standard GitHub API request headers.
 */
function githubHeaders() {
  const headers = {
    'Accept':     'application/vnd.github+json',
    'User-Agent': 'OWASP-GenAI-Crosswalk-Watcher/1.0',
  };
  if (GITHUB_TOKEN) headers['Authorization'] = `Bearer ${GITHUB_TOKEN}`;
  return headers;
}

// ─── GitHub Issue Creation ────────────────────────────────────────────────────

/**
 * Open a single GitHub Issue for a finding.
 * Returns true on success, false on failure.
 */
async function openIssue(finding) {
  const url = `https://api.github.com/repos/${GITHUB_REPOSITORY}/issues`;
  const body = JSON.stringify({
    title:  finding.title,
    body:   finding.body,
    labels: [finding.label, 'automated-watch'],
  });

  try {
    const res = await fetchWithTimeout(url, {
      method:  'POST',
      headers: { ...githubHeaders(), 'Content-Type': 'application/json' },
      body,
    });

    if (res.status === 403 || res.status === 429) {
      console.error(`  [issues] Rate-limited or forbidden (HTTP ${res.status}) — skipping issue creation.`);
      return false;
    }
    if (!res.ok) {
      const text = await res.text();
      console.error(`  [issues] Failed to create issue (HTTP ${res.status}): ${text.slice(0, 200)}`);
      return false;
    }
    return true;
  } catch (err) {
    console.error(`  [issues] Network error creating issue: ${err.message}`);
    return false;
  }
}

// ─── OWASP Watcher ────────────────────────────────────────────────────────────

/**
 * Watch three OWASP GitHub repositories for new commits.
 */
async function watchOwasp(state, sinceOverride) {
  const findings = [];
  const newState = { ...state.owasp };

  for (const fullRepo of OWASP_REPOS) {
    const [owner, repo] = fullRepo.split('/');
    const repoKey = repo;

    // Determine lookback point: override > last known SHA > 7 days ago
    let sinceParam = '';
    if (sinceOverride) {
      sinceParam = `&since=${encodeURIComponent(new Date(sinceOverride).toISOString())}`;
    } else if (!state.owasp[repoKey]) {
      const fallback = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString();
      sinceParam = `&since=${encodeURIComponent(fallback)}`;
    }
    // When we have a last-seen SHA we fetch recent commits and filter client-side,
    // because the GitHub API `since` param uses timestamps not SHAs.

    const url = `https://api.github.com/repos/${owner}/${repo}/commits?per_page=5${sinceParam}`;

    let commits;
    try {
      const res = await fetchWithTimeout(url, { headers: githubHeaders() });
      if (res.status === 403 || res.status === 429) {
        console.error(`  [owasp] Rate-limited on ${repo} (HTTP ${res.status}) — skipping.`);
        continue;
      }
      if (!res.ok) {
        console.error(`  [owasp] HTTP ${res.status} fetching ${repo} commits.`);
        continue;
      }
      commits = await res.json();
    } catch (err) {
      console.error(`  [owasp] Error fetching ${repo}: ${err.message}`);
      continue;
    }

    if (!Array.isArray(commits) || commits.length === 0) continue;

    const lastSeenSha = state.owasp[repoKey];
    let latestSha = commits[0].sha;

    for (const commit of commits) {
      // Skip commits we have already seen
      if (lastSeenSha && commit.sha === lastSeenSha) break;

      const shortSha  = commit.sha.slice(0, 7);
      const message   = (commit.commit.message || '').split('\n')[0];
      const author    = commit.commit.author?.name || 'unknown';
      const date      = commit.commit.author?.date || '';
      const commitUrl = `https://github.com/${owner}/${repo}/commit/${commit.sha}`;

      findings.push({
        label: 'owasp-update',
        title: `[owasp-update] ${repo} — ${shortSha}: ${message.slice(0, 80)}`,
        body: [
          `## OWASP Repository Update`,
          ``,
          `**Repository:** [${owner}/${repo}](https://github.com/${owner}/${repo})`,
          `**Commit SHA:** \`${commit.sha}\``,
          `**Author:** ${author}`,
          `**Date:** ${date}`,
          `**Commit URL:** ${commitUrl}`,
          ``,
          `### Commit Message`,
          `\`\`\``,
          commit.commit.message,
          `\`\`\``,
          ``,
          `### Suggested Action`,
          `Review for mapping drift in the relevant mapping files under \`llm-top10/\`, \`agentic-top10/\`, and \`dsgai-2026/\` directories.`,
          `Check whether new or changed threats/controls need to be reflected in the crosswalk entries.`,
        ].join('\n'),
      });
    }

    newState[repoKey] = latestSha;
  }

  return { findings, newOwasp: newState };
}

// ─── arXiv Watcher ───────────────────────────────────────────────────────────

/**
 * Map keywords in title/abstract to OWASP entry identifiers.
 */
function mapArxivToOwasp(text) {
  const lower = text.toLowerCase();
  const mappings = [];

  if (/prompt injection|jailbreak/.test(lower))            mappings.push('LLM01');
  if (/data poisoning|rag/.test(lower))                    mappings.push('DSGAI04', 'LLM03');
  if (/\bmemory\b|persistence/.test(lower))                mappings.push('ASI06');
  if (/\btool\b|\bagent\b|agentic/.test(lower))            mappings.push('ASI01', 'ASI02');
  if (/exfiltration|\bleak\b/.test(lower))                 mappings.push('LLM02', 'DSGAI01');
  if (/hallucination|misinformation/.test(lower))          mappings.push('LLM09');
  if (/supply chain/.test(lower))                          mappings.push('LLM05', 'ASI04');

  return [...new Set(mappings)];
}

/**
 * Minimal Atom XML parser — extracts <entry> blocks and named fields.
 */
function parseAtomEntries(xml) {
  const entries = [];
  const entryRe = /<entry>([\s\S]*?)<\/entry>/g;
  let match;

  while ((match = entryRe.exec(xml)) !== null) {
    const block = match[1];

    const get = (tag) => {
      const m = new RegExp(`<${tag}[^>]*>([\\s\\S]*?)<\\/${tag}>`).exec(block);
      return m ? m[1].trim() : '';
    };

    // arXiv ID is in <id>http://arxiv.org/abs/XXXX.XXXXX...</id>
    const rawId  = get('id');
    const idMatch = /arxiv\.org\/abs\/([^v\s]+)/i.exec(rawId);
    const arxivId = idMatch ? idMatch[1] : rawId;

    // Collect all author names
    const authorRe = /<author>[\s\S]*?<name>([^<]+)<\/name>[\s\S]*?<\/author>/g;
    const authors = [];
    let am;
    while ((am = authorRe.exec(block)) !== null) authors.push(am[1].trim());

    entries.push({
      id:       arxivId,
      title:    get('title').replace(/\s+/g, ' '),
      summary:  get('summary').replace(/\s+/g, ' '),
      published: get('published'),
      authors,
      link:     rawId,
    });
  }

  return entries;
}

/**
 * Watch arXiv for new AI-security papers.
 */
async function watchArxiv(state) {
  const findings  = [];
  const seenIds   = new Set(state.arxiv || []);
  const newIds    = [...seenIds];

  let xml;
  try {
    const res = await fetchWithTimeout(ARXIV_URL, {
      headers: { 'User-Agent': 'OWASP-GenAI-Crosswalk-Watcher/1.0' },
    });
    if (!res.ok) {
      console.error(`  [arxiv] HTTP ${res.status} from arXiv API.`);
      return { findings, newArxiv: state.arxiv };
    }
    xml = await res.text();
  } catch (err) {
    console.error(`  [arxiv] Error: ${err.message}`);
    return { findings, newArxiv: state.arxiv };
  }

  const entries = parseAtomEntries(xml);

  for (const entry of entries) {
    if (!entry.id || seenIds.has(entry.id)) continue;

    seenIds.add(entry.id);
    newIds.push(entry.id);

    const abstract  = (entry.summary || '').slice(0, 300);
    const owaspHints = mapArxivToOwasp(`${entry.title} ${entry.summary}`);
    const mappingStr = owaspHints.length > 0
      ? owaspHints.join(', ')
      : '_No automatic mapping — manual review recommended_';

    findings.push({
      label: 'new-research',
      title: `[new-research] arXiv:${entry.id} — ${entry.title.slice(0, 80)}`,
      body: [
        `## New arXiv Research Paper`,
        ``,
        `**arXiv ID:** [${entry.id}](https://arxiv.org/abs/${entry.id})`,
        `**Title:** ${entry.title}`,
        `**Authors:** ${entry.authors.join(', ') || 'N/A'}`,
        `**Published:** ${entry.published}`,
        `**URL:** https://arxiv.org/abs/${entry.id}`,
        ``,
        `### Abstract (first 300 chars)`,
        `> ${abstract}${entry.summary.length > 300 ? '…' : ''}`,
        ``,
        `### Suggested OWASP Mapping`,
        mappingStr,
        ``,
        `### Suggested Action`,
        `Review this paper against the OWASP GenAI Crosswalk entries and update relevant mapping files if new attack patterns or mitigations are identified.`,
      ].join('\n'),
    });
  }

  return { findings, newArxiv: newIds };
}

// ─── NVD Watcher ─────────────────────────────────────────────────────────────

/**
 * Map CVE description text to a suggested OWASP entry.
 */
function mapCveToOwasp(description) {
  const lower = description.toLowerCase();
  if (/prompt injection|jailbreak/.test(lower))   return 'LLM01';
  if (/training data|poisoning/.test(lower))       return 'LLM03 / DSGAI04';
  if (/supply chain/.test(lower))                  return 'LLM05 / ASI04';
  if (/denial.of.service|availability/.test(lower)) return 'LLM04';
  if (/exfiltrat|data leak/.test(lower))           return 'LLM02 / DSGAI01';
  if (/plugin|tool|agent/.test(lower))             return 'LLM07 / ASI01';
  return '_Manual mapping required_';
}

/**
 * Watch NVD for new CVEs mentioning AI/LLM keywords.
 */
async function watchNvd(state, sinceOverride) {
  const findings = [];
  const seenCves = new Set(state.nvd || []);
  const newCves  = [...seenCves];

  const lastRunDate = sinceOverride
    ? new Date(sinceOverride).toISOString()
    : state.last_run
      ? new Date(state.last_run).toISOString()
      : new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString();

  // NVD requires dates without milliseconds, formatted as yyyy-MM-ddTHH:mm:ss.SSS,
  // and pubStartDate must be paired with pubEndDate (range ≤ 120 days).
  const pubStartDate = lastRunDate.replace(/\.\d{3}Z$/, '.000');
  const pubEndDate   = new Date().toISOString().replace(/\.\d{3}Z$/, '.000');

  for (const keyword of NVD_KEYWORDS) {
    const url =
      `https://services.nvd.nist.gov/rest/json/cves/2.0` +
      `?keywordSearch=${encodeURIComponent(keyword)}` +
      `&pubStartDate=${encodeURIComponent(pubStartDate)}` +
      `&pubEndDate=${encodeURIComponent(pubEndDate)}` +
      `&resultsPerPage=20`;

    let data;
    try {
      const res = await fetchWithTimeout(url, {
        headers: { 'User-Agent': 'OWASP-GenAI-Crosswalk-Watcher/1.0' },
      });

      if (res.status === 403 || res.status === 429) {
        console.error(`  [nvd] Rate-limited for keyword "${keyword}" (HTTP ${res.status}) — skipping.`);
        continue;
      }
      if (!res.ok) {
        console.error(`  [nvd] HTTP ${res.status} for keyword "${keyword}".`);
        continue;
      }
      data = await res.json();
    } catch (err) {
      console.error(`  [nvd] Error for keyword "${keyword}": ${err.message}`);
      continue;
    }

    const vulnerabilities = data?.vulnerabilities || [];

    for (const vuln of vulnerabilities) {
      const cve       = vuln?.cve;
      const cveId     = cve?.id;
      if (!cveId || seenCves.has(cveId)) continue;

      seenCves.add(cveId);
      newCves.push(cveId);

      // Extract English description
      const descs   = cve?.descriptions || [];
      const engDesc = descs.find(d => d.lang === 'en')?.value || 'No description available.';

      // Extract CVSS score (prefer v3.1 > v3.0 > v2)
      const metrics  = cve?.metrics || {};
      let cvssScore  = 'N/A';
      let cvssVector = '';
      if (metrics.cvssMetricV31?.length) {
        cvssScore  = metrics.cvssMetricV31[0].cvssData?.baseScore ?? 'N/A';
        cvssVector = metrics.cvssMetricV31[0].cvssData?.vectorString ?? '';
      } else if (metrics.cvssMetricV30?.length) {
        cvssScore  = metrics.cvssMetricV30[0].cvssData?.baseScore ?? 'N/A';
        cvssVector = metrics.cvssMetricV30[0].cvssData?.vectorString ?? '';
      } else if (metrics.cvssMetricV2?.length) {
        cvssScore  = metrics.cvssMetricV2[0].cvssData?.baseScore ?? 'N/A';
        cvssVector = metrics.cvssMetricV2[0].cvssData?.vectorString ?? '';
      }

      const published = cve?.published || '';
      const nvdUrl    = `https://nvd.nist.gov/vuln/detail/${cveId}`;
      const owaspHint = mapCveToOwasp(engDesc);

      findings.push({
        label: 'new-cve',
        title: `[new-cve] ${cveId} — ${engDesc.slice(0, 80)}`,
        body: [
          `## New CVE — AI/LLM Related`,
          ``,
          `**CVE ID:** [${cveId}](${nvdUrl})`,
          `**Published:** ${published}`,
          `**CVSS Score:** ${cvssScore}${cvssVector ? ` (${cvssVector})` : ''}`,
          ``,
          `### Description`,
          engDesc,
          ``,
          `### Suggested OWASP Mapping`,
          owaspHint,
          ``,
          `### Suggested Action`,
          `Review this CVE against the OWASP GenAI Crosswalk entries. ` +
          `Update \`data/incidents.json\` or relevant mapping files if this CVE represents a real-world exploitation of a mapped threat.`,
        ].join('\n'),
      });
    }
  }

  return { findings, newNvd: newCves };
}

// ─── Frameworks Watcher ───────────────────────────────────────────────────────

/**
 * Hash the first 8 KB of response body as a lightweight change signal,
 * used when ETag and Last-Modified headers are absent.
 */
function hashBuffer(buf) {
  return crypto.createHash('sha256').update(buf).digest('hex').slice(0, 16);
}

/**
 * Watch framework reference pages for content changes via HTTP HEAD / partial GET.
 */
async function watchFrameworks(state) {
  const findings    = [];
  const newFwState  = { ...(state.frameworks || {}) };

  for (const fw of FRAMEWORK_CHECKS) {
    const key     = fw.name;
    const saved   = newFwState[key] || {};

    let res;
    try {
      // Try HEAD first to avoid downloading large PDFs needlessly
      res = await fetchWithTimeout(fw.url, {
        method:  'HEAD',
        headers: {
          'User-Agent':    'OWASP-GenAI-Crosswalk-Watcher/1.0',
          'Cache-Control': 'no-cache',
        },
        redirect: 'follow',
      });
    } catch (err) {
      console.error(`  [frameworks] HEAD failed for ${fw.name}: ${err.message}`);

      // Fallback: try GET with a Range header to fetch only the first 8 KB
      try {
        res = await fetchWithTimeout(fw.url, {
          method:  'GET',
          headers: {
            'User-Agent':    'OWASP-GenAI-Crosswalk-Watcher/1.0',
            'Cache-Control': 'no-cache',
            'Range':         'bytes=0-8191',
          },
          redirect: 'follow',
        });
      } catch (err2) {
        console.error(`  [frameworks] GET also failed for ${fw.name}: ${err2.message}`);
        continue;
      }
    }

    if (!res.ok && res.status !== 206 /* Partial Content */) {
      console.error(`  [frameworks] HTTP ${res.status} for ${fw.name}.`);
      continue;
    }

    const etag         = res.headers.get('etag')          || '';
    const lastModified = res.headers.get('last-modified') || '';
    const contentLen   = res.headers.get('content-length') || '';

    // Build a composite fingerprint from whatever headers are available
    let fingerprint = '';
    let changeDesc  = '';

    if (etag) {
      fingerprint = `etag:${etag}`;
      if (saved.etag && saved.etag !== etag) {
        changeDesc = `ETag changed from \`${saved.etag}\` to \`${etag}\``;
      }
    } else if (lastModified) {
      fingerprint = `last-modified:${lastModified}`;
      if (saved.last_modified && saved.last_modified !== lastModified) {
        changeDesc = `Last-Modified changed from \`${saved.last_modified}\` to \`${lastModified}\``;
      }
    } else if (contentLen) {
      fingerprint = `content-length:${contentLen}`;
      if (saved.content_length && saved.content_length !== contentLen) {
        changeDesc = `Content-Length changed from ${saved.content_length} to ${contentLen}`;
      }
    } else {
      // No useful headers — fetch a small chunk and hash it
      try {
        const chunkRes = await fetchWithTimeout(fw.url, {
          headers: {
            'User-Agent': 'OWASP-GenAI-Crosswalk-Watcher/1.0',
            'Range':      'bytes=0-8191',
          },
          redirect: 'follow',
        });
        const buf = Buffer.from(await chunkRes.arrayBuffer());
        const h   = hashBuffer(buf);
        fingerprint = `hash:${h}`;
        if (saved.hash && saved.hash !== h) {
          changeDesc = `Content hash changed from \`${saved.hash}\` to \`${h}\``;
        }
        newFwState[key] = { ...saved, hash: h, last_checked: new Date().toISOString() };
      } catch (hashErr) {
        console.error(`  [frameworks] Hash fallback failed for ${fw.name}: ${hashErr.message}`);
        continue;
      }
    }

    // Persist updated state regardless of whether a change was detected
    newFwState[key] = {
      etag,
      last_modified: lastModified,
      content_length: contentLen,
      last_checked: new Date().toISOString(),
    };

    const isFirstRun = !saved.etag && !saved.last_modified && !saved.content_length && !saved.hash;

    if (changeDesc) {
      findings.push({
        label: 'framework-update',
        title: `[framework-update] ${fw.name} — content change detected`,
        body: [
          `## Framework Content Change Detected`,
          ``,
          `**Framework:** ${fw.name} (${fw.label})`,
          `**URL:** ${fw.url}`,
          ``,
          `### What Changed`,
          changeDesc,
          ``,
          `### Suggested Action`,
          `1. Visit ${fw.url} and review the updated content.`,
          `2. Check whether any changes affect mappings in the OWASP GenAI Crosswalk.`,
          `3. Update relevant files under \`llm-top10/\`, \`agentic-top10/\`, \`dsgai-2026/\`, or \`shared/\` as needed.`,
          `4. Consider updating \`CROSSREF.md\` if cross-framework references change.`,
        ].join('\n'),
      });
    } else if (isFirstRun) {
      // First run: record baseline state, no finding
      console.log(`  [frameworks] Baseline recorded for ${fw.name} (fingerprint: ${fingerprint})`);
    }
  }

  return { findings, newFrameworks: newFwState };
}

// ─── Issue Reporter ───────────────────────────────────────────────────────────

/**
 * Either open GitHub Issues for each finding or print them to stdout.
 * Returns the count of successfully handled findings.
 */
async function reportFindings(findings, dryRun) {
  if (findings.length === 0) return 0;

  if (dryRun || !GITHUB_TOKEN) {
    console.log('\n── Findings (dry-run / no token) ──────────────────────────────────────────\n');
    for (const f of findings) {
      console.log(`Label : ${f.label}`);
      console.log(`Title : ${f.title}`);
      console.log(`Body  :`);
      console.log(f.body);
      console.log('─'.repeat(76));
    }
    return findings.length;
  }

  let opened = 0;
  for (const finding of findings) {
    const success = await openIssue(finding);
    if (success) opened++;
  }
  return opened;
}

// ─── Summary Printer ─────────────────────────────────────────────────────────

function printSummary({ date, watchers, findings, issueCount, dryRun, tokenPresent }) {
  const titles = findings.map(f => `  ${f.title}`).join('\n') || '  (none)';
  const issueStr = dryRun || !tokenPresent
    ? 'dry-run — no issues opened'
    : `${issueCount} opened`;

  console.log('\n' + '═'.repeat(60));
  console.log('OWASP GenAI Crosswalk — Watch Run');
  console.log('─'.repeat(60));
  console.log(`Date    : ${date}`);
  console.log(`Watchers: ${watchers.join(', ')}`);
  console.log(`Findings: ${findings.length} new item${findings.length !== 1 ? 's' : ''}`);
  console.log(titles);
  console.log(`Issues  : ${issueStr}`);
  console.log('═'.repeat(60) + '\n');
}

// ─── Main ─────────────────────────────────────────────────────────────────────

async function main() {
  const runDate = new Date().toISOString();
  const state   = loadState();

  // Determine which watchers to run
  const ALL_WATCHERS = ['owasp', 'arxiv', 'nvd', 'frameworks'];
  let watchersToRun;

  if (SINGLE_WATCHER) {
    if (!ALL_WATCHERS.includes(SINGLE_WATCHER)) {
      console.error(`Unknown watcher: "${SINGLE_WATCHER}". Valid options: ${ALL_WATCHERS.join(', ')}`);
      process.exit(0);
    }
    watchersToRun = [SINGLE_WATCHER];
  } else {
    watchersToRun = ALL_WATCHERS;
  }

  const allFindings = [];

  // ── OWASP ─────────────────────────────────────────────────────────────────
  if (watchersToRun.includes('owasp')) {
    console.log('[watch-owasp] Checking OWASP GitHub repositories…');
    try {
      const { findings, newOwasp } = await watchOwasp(state, SINCE_OVERRIDE);
      console.log(`  → ${findings.length} new commit(s) found.`);
      allFindings.push(...findings);
      if (!DRY_RUN) state.owasp = newOwasp;
    } catch (err) {
      console.error(`[watch-owasp] Unexpected error: ${err.message}`);
    }
  }

  // ── arXiv ─────────────────────────────────────────────────────────────────
  if (watchersToRun.includes('arxiv')) {
    console.log('[watch-arxiv] Querying arXiv for new papers…');
    try {
      const { findings, newArxiv } = await watchArxiv(state);
      console.log(`  → ${findings.length} new paper(s) found.`);
      allFindings.push(...findings);
      if (!DRY_RUN) state.arxiv = newArxiv;
    } catch (err) {
      console.error(`[watch-arxiv] Unexpected error: ${err.message}`);
    }
  }

  // ── NVD ───────────────────────────────────────────────────────────────────
  if (watchersToRun.includes('nvd')) {
    console.log('[watch-nvd] Querying NVD for new CVEs…');
    try {
      const { findings, newNvd } = await watchNvd(state, SINCE_OVERRIDE);
      console.log(`  → ${findings.length} new CVE(s) found.`);
      allFindings.push(...findings);
      if (!DRY_RUN) state.nvd = newNvd;
    } catch (err) {
      console.error(`[watch-nvd] Unexpected error: ${err.message}`);
    }
  }

  // ── Frameworks ────────────────────────────────────────────────────────────
  if (watchersToRun.includes('frameworks')) {
    console.log('[watch-frameworks] Checking framework pages for changes…');
    try {
      const { findings, newFrameworks } = await watchFrameworks(state);
      console.log(`  → ${findings.length} framework change(s) detected.`);
      allFindings.push(...findings);
      if (!DRY_RUN) state.frameworks = newFrameworks;
    } catch (err) {
      console.error(`[watch-frameworks] Unexpected error: ${err.message}`);
    }
  }

  // ── Report findings ───────────────────────────────────────────────────────
  const issueCount = await reportFindings(allFindings, DRY_RUN);

  // ── Update state ──────────────────────────────────────────────────────────
  if (!DRY_RUN) {
    state.last_run = runDate;
    state.version  = '1.0.0';
    saveState(state, false);
  }

  // ── Print summary ─────────────────────────────────────────────────────────
  printSummary({
    date:         runDate.slice(0, 10),
    watchers:     watchersToRun,
    findings:     allFindings,
    issueCount,
    dryRun:       DRY_RUN,
    tokenPresent: Boolean(GITHUB_TOKEN),
  });

  // Always exit 0 — findings are informational
  process.exit(0);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(0);
});
