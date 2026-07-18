#!/usr/bin/env python3
"""Deterministic internal-link checker for the DSGAI scanner docs.

Verifies that relative markdown links point at files that exist, and that
in-file `#anchor` fragments match a heading in the target document. External
(http/https/mailto) links are intentionally not fetched — that is flaky in CI
and a separate concern. Exit 1 if any internal link is broken.

Usage: python check_md_links.py <dir-or-file> [more...]
"""
import re, sys, unicodedata
from pathlib import Path

LINK_RE = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)]+)\)')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')


def slug(text: str) -> str:
    """GitHub-style heading -> anchor slug."""
    text = unicodedata.normalize('NFKD', text)
    # strip markdown inline formatting and links
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'[*_~]', '', text)
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = text.strip().replace(' ', '-')
    return text


def anchors_of(path: Path) -> set:
    out = set()
    if not path.exists():
        return out
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        m = HEADING_RE.match(line)
        if m:
            out.add(slug(m.group(2)))
    return out


def collect_md(targets):
    files = []
    for t in targets:
        p = Path(t)
        if p.is_dir():
            files += sorted(p.rglob('*.md'))
        elif p.suffix == '.md':
            files.append(p)
    return files


def main():
    targets = sys.argv[1:] or ['.']
    files = collect_md(targets)
    anchor_cache = {}
    broken = []
    for f in files:
        text = f.read_text(encoding='utf-8', errors='replace')
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if target.startswith('<') and target.endswith('>'):
                target = target[1:-1]
            # skip external and pure-anchor-to-external schemes
            if re.match(r'^[a-z]+://', target) or target.startswith('mailto:'):
                continue
            path_part, _, frag = target.partition('#')
            if path_part == '':
                # same-file anchor
                dest = f
            else:
                dest = (f.parent / path_part).resolve()
                if not dest.exists():
                    broken.append(f"{f}: missing file -> {target}")
                    continue
            if frag:
                if dest not in anchor_cache:
                    anchor_cache[dest] = anchors_of(dest)
                if slug(frag) not in anchor_cache[dest]:
                    broken.append(f"{f}: missing anchor -> {target}")
    if broken:
        print("Broken internal links:")
        for b in broken:
            print("  " + b)
        return 1
    print(f"OK: {len(files)} markdown files, all internal links resolve.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
