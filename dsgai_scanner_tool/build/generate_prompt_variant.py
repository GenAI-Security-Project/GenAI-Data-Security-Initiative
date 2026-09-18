#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Generate the tool-neutral dsgai_scanner_prompt.md from dsgai_scanner_tool.md.

Single-sources the two variants so they can't drift: the prompt variant is the
skill minus its Claude-Code-specific parts. Removes the YAML frontmatter and any
content between `<!-- cc-only:start -->` / `<!-- cc-only:end -->` markers, and
prepends a tool-neutral header.

  python build/generate_prompt_variant.py           # write the variant
  python build/generate_prompt_variant.py --check    # CI: fail if checked-in
                                                     # variant is out of date
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "dsgai_scanner_tool.md"
VARIANT = ROOT / "dsgai_scanner_prompt.md"

CC_BLOCK = re.compile(r'[ \t]*<!-- cc-only:start -->.*?<!-- cc-only:end -->[ \t]*\n?',
                      re.DOTALL)
FRONTMATTER = re.compile(r'\A---\n.*?\n---\n', re.DOTALL)

HEADER = """<!-- GENERATED FILE — do not edit by hand.
     Regenerate with: python build/generate_prompt_variant.py
     Source of truth: dsgai_scanner_tool.md (the Claude Code skill).
     This is the tool-neutral variant for use with any AI coding assistant. -->

# DSGAI Scanner — Tool-Neutral Prompt

> This is the generated, tool-neutral variant of the DSGAI scanner. It is
> produced from the Claude Code skill by `build/generate_prompt_variant.py`.
> Use it with any AI coding assistant that can run shell commands (`rg --pcre2`,
> `git`, `python`). For Claude Code, use `dsgai_scanner_tool.md` directly.

"""


def generate():
    text = SKILL.read_text(encoding="utf-8")
    text = FRONTMATTER.sub("", text, count=1)
    text = CC_BLOCK.sub("", text)
    # Drop the leading skill H1 (the header below replaces it).
    text = re.sub(r'\A\s*# .*?\n', "", text, count=1)
    return HEADER + text.lstrip()


def main(argv):
    rendered = generate()
    if "--check" in argv:
        current = VARIANT.read_text(encoding="utf-8") if VARIANT.exists() else ""
        if current != rendered:
            sys.stderr.write("dsgai_scanner_prompt.md is out of date. Run: "
                             "python build/generate_prompt_variant.py\n")
            return 1
        print("dsgai_scanner_prompt.md is up to date.")
        return 0
    VARIANT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {VARIANT} ({rendered.count(chr(10))} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
