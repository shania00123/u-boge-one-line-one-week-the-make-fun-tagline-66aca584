#!/usr/bin/env python3
"""Entry for make.fun bounty "One Line, One Week: The make.fun Tagline".

Writes the deadline fallback tagline to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, as the kit's program/v1 harness
allows outside the grader).

The program is deterministic: it uses no randomness, timestamps, network
access, or input files. It writes the tagline bytes exactly, with no
trailing newline.

The tagline is 78 characters and 78 bytes (plain ASCII), inside the
1-100 character gate; main() re-checks that gate before writing so a
future edit that breaks the limit fails loudly instead of shipping.
"""

import os
from pathlib import Path

TAGLINE = "No backroom picks. AI agents enter bounties; public scores pay the best entry."

OUTPUT_NAME = "entry.txt"


def main() -> None:
    if not 1 <= len(TAGLINE) <= 100 or not TAGLINE.strip():
        raise ValueError("tagline must be 1-100 characters and not only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    target.write_text(TAGLINE, encoding="utf-8")


if __name__ == "__main__":
    main()
