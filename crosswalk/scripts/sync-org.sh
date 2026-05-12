#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────────────────
# Sync OWASP GenAI Crosswalk to the OWASP org repo
#
# Usage:
#   bash scripts/sync-org.sh              # sync current state
#   bash scripts/sync-org.sh v2.1.0       # sync with version label
#
# Source: GenAI-Security-Project/GenAI-Data-Security-Initiative
# Target: GenAI-Security-Project/GenAI-Data-Security-Initiative/crosswalk/
# ──────────────────────────────────────────────────────────────────────────
set -euo pipefail

VERSION="${1:-$(node -e "console.log(JSON.parse(require('fs').readFileSync('package.json','utf8')).version)" 2>/dev/null || echo 'latest')}"
ORG_REPO="GenAI-Security-Project/GenAI-Data-Security-Initiative"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORK_DIR="$(mktemp -d)"

echo ""
echo "OWASP GenAI Crosswalk — Org Sync"
echo "════════════════════════════════════"
echo "  Version : $VERSION"
echo "  Source  : $SOURCE_DIR"
echo "  Target  : $ORG_REPO/crosswalk/"
echo "  Workdir : $WORK_DIR"
echo ""

# Clone org repo
echo "→ Cloning $ORG_REPO..."
gh repo clone "$ORG_REPO" "$WORK_DIR/org" -- --depth 1 2>&1 | tail -1

# Remove old crosswalk
echo "→ Removing old crosswalk/"
rm -rf "$WORK_DIR/org/crosswalk"

# Copy current crosswalk
echo "→ Copying current crosswalk..."
cp -r "$SOURCE_DIR" "$WORK_DIR/org/crosswalk"

# Clean build artifacts, dev files, and git history
echo "→ Cleaning artifacts..."
rm -rf "$WORK_DIR/org/crosswalk/node_modules" \
       "$WORK_DIR/org/crosswalk/dist" \
       "$WORK_DIR/org/crosswalk/reports" \
       "$WORK_DIR/org/crosswalk/.git" \
       "$WORK_DIR/org/crosswalk/.claude" \
       "$WORK_DIR/org/crosswalk/sbom.cdx.json" \
       "$WORK_DIR/org/crosswalk/sbom-content.cdx.json"

# Check for changes
cd "$WORK_DIR/org"
git add crosswalk/

if git diff --cached --quiet; then
  echo ""
  echo "✓ No changes — org repo already up to date."
  rm -rf "$WORK_DIR"
  exit 0
fi

# Show summary
CHANGED=$(git diff --cached --stat | tail -1)
echo ""
echo "  Changes: $CHANGED"
echo ""

# Commit and push
read -p "Push to $ORG_REPO? [y/N] " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
  git commit -m "Sync crosswalk v$VERSION — $(date +%Y-%m-%d)

Source: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk/releases/tag/v$VERSION"

  git push origin main
  echo ""
  echo "✓ Pushed to https://github.com/$ORG_REPO/tree/main/crosswalk"
else
  echo "Aborted."
fi

# Cleanup
rm -rf "$WORK_DIR"
