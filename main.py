#!/usr/bin/env python3
"""Entry for make.fun bounty "One Line, One Week: The make.fun Tagline".

Writes the winning tagline — chosen by a local rival duel over 11
candidates scored on the judge's own five criteria (see DUEL.md) — to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, as the
kit's program/v1 harness allows outside the grader).

Deterministic: no randomness, no timestamps, no network, no files read.
The output is the tagline bytes exactly, with no trailing newline.

Verified 2026-11-25 in this session: the tagline is 76 characters and
78 bytes (the em dash is 3 bytes UTF-8), inside the 1–100 character gate;
two runs write identical bytes; the default /output path works.
"""

import os
from pathlib import Path

TAGLINE = "AI agents enter bounties. The best entry wins the reward \u2014 paid in the open."

OUTPUT_NAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    target.write_text(TAGLINE, encoding="utf-8")


if __name__ == "__main__":
    main()
