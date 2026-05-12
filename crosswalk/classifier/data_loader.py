"""Load framework controls and OWASP entry mappings from the data layer."""

import json
from pathlib import Path
from typing import NamedTuple

from .config import FRAMEWORKS_DIR, ENTRIES_DIR, BACKLINKS_PATH


class Control(NamedTuple):
    framework: str        # Display name e.g. "NIST AI RMF 1.0"
    control_id: str       # e.g. "GV-1.7"
    title: str
    description: str
    function: str | None
    parent: str | None

    @property
    def text(self) -> str:
        """Concatenated text for embedding."""
        parts = [f"{self.framework} — {self.control_id}: {self.title}"]
        if self.description:
            parts.append(self.description)
        if self.function:
            parts.append(f"Function: {self.function}")
        return ". ".join(parts)


class Mapping(NamedTuple):
    entry_id: str         # e.g. "LLM01"
    entry_name: str
    source_list: str
    severity: str
    framework: str
    control_id: str
    control_name: str
    tier: str
    scope: str
    notes: str | None


def load_controls() -> list[Control]:
    """Load all controls from data/frameworks/*.json."""
    controls = []
    for fp in sorted(FRAMEWORKS_DIR.glob("*.json")):
        fw = json.loads(fp.read_text("utf-8"))
        for c in fw.get("controls", []):
            controls.append(Control(
                framework=fw["name"],
                control_id=c["control_id"],
                title=c["title"],
                description=c.get("description", ""),
                function=c.get("function"),
                parent=c.get("parent"),
            ))
    return controls


def load_entries() -> list[dict]:
    """Load all OWASP entry JSON files."""
    entries = []
    for fp in sorted(ENTRIES_DIR.glob("*.json")):
        entries.append(json.loads(fp.read_text("utf-8")))
    return entries


def load_backlinks() -> list[dict]:
    """Load the backlinks index."""
    return json.loads(BACKLINKS_PATH.read_text("utf-8"))


def load_mappings() -> list[Mapping]:
    """Load all hand-curated mappings from entry JSON files."""
    mappings = []
    for entry in load_entries():
        for m in entry.get("mappings", []):
            mappings.append(Mapping(
                entry_id=entry["id"],
                entry_name=entry["name"],
                source_list=entry["source_list"],
                severity=entry["severity"],
                framework=m["framework"],
                control_id=m["control_id"],
                control_name=m.get("control_name", ""),
                tier=m.get("tier", ""),
                scope=m.get("scope", ""),
                notes=m.get("notes"),
            ))
    return mappings


def build_query(entry_id: str, entry_name: str, severity: str,
                notes: str | None = None) -> str:
    """Build a query string for retrieval."""
    q = f"{entry_id}: {entry_name}. Severity: {severity}"
    if notes:
        q += f". {notes}"
    return q
