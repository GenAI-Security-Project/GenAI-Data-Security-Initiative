"""Validate every entry in ./entries/ against ./schema.json.

Usage: python validate.py
Exit code 0 on success, 1 on any validation failure, 2 without jsonschema.
Requires: jsonschema (pip install jsonschema)

The shared checks (schema with formats, DSGAI IDs, including
risks_identified[].dsgai_id and existing_controls/control_gaps
addresses_dsgai, ID matches file name, duplicate IDs) are in
../_shared/validate_lib.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from validate_lib import main_for  # noqa: E402

if __name__ == "__main__":
    main_for(__file__, id_field="assessment_id")
