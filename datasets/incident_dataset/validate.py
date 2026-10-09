"""Validate every entry in ./entries/ against the incident schema.

Usage: python validate.py
Exit code 0 on success (including when there are no entries yet), 1 on any
validation failure, 2 when jsonschema is missing.
Requires: jsonschema (pip install jsonschema)

The schema is data_validation/schemas/incident.schema.json, the only schema
for this dataset. The checks (schema with formats, DSGAI IDs, incident_id
matches the file name, duplicate IDs) are in ../_shared/validate_lib.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from validate_lib import main_for  # noqa: E402

SCHEMA = Path(__file__).resolve().parents[2] / "data_validation" / "schemas" / "incident.schema.json"

if __name__ == "__main__":
    main_for(__file__, id_field="incident_id", schema_path=SCHEMA, allow_empty=True)
