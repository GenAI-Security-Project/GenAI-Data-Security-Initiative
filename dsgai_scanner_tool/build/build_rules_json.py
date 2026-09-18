#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build rules/dsgai-rules.json from rules/dsgai-rules.yaml.

This is the repeatable build step (unlike the one-time generate_rules.py). The
deterministic CLI loads the JSON with the standard library only, so the
curl-one-file install story needs no PyYAML at runtime. PyYAML is required only
to edit rules and to run this build / the self-test that asserts JSON == YAML.

Validates against rules/rules.schema.json before writing. Output is
deterministic (sorted keys, stable rule order, trailing newline) so the PR-06
self-test can assert the checked-in JSON matches a fresh build.

Usage:
  python build/build_rules_json.py            # write rules/dsgai-rules.json
  python build/build_rules_json.py --check     # verify checked-in JSON is current (CI)
"""
import json
import sys
from pathlib import Path

RULES_DIR = Path(__file__).resolve().parent.parent / "rules"
YAML_PATH = RULES_DIR / "dsgai-rules.yaml"
JSON_PATH = RULES_DIR / "dsgai-rules.json"
SCHEMA_PATH = RULES_DIR / "rules.schema.json"


def build():
    import yaml  # only needed for build/edit, not at CLI runtime
    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    try:
        import jsonschema
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        jsonschema.validate(data, schema)
    except ImportError:
        sys.stderr.write("warning: jsonschema not installed; skipping validation\n")
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main(argv):
    rendered = build()
    if "--check" in argv:
        current = JSON_PATH.read_text(encoding="utf-8") if JSON_PATH.exists() else ""
        if current != rendered:
            sys.stderr.write(
                "rules/dsgai-rules.json is out of date. Run: "
                "python build/build_rules_json.py\n")
            return 1
        print("rules/dsgai-rules.json is up to date.")
        return 0
    JSON_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Wrote {JSON_PATH} ({rendered.count(chr(10))} lines).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
