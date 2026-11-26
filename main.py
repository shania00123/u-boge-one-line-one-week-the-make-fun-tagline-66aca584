#!/usr/bin/env python3
"""Entry for make.fun bounty "One Line, One Week: The make.fun Tagline".

Writes the final fallback tagline to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, as the kit's program/v1 harness
allows outside the grader).

The program is deterministic: it uses no randomness, timestamps, network
access, or input files. It writes the tagline bytes exactly and adds no
trailing newline.

The tagline is 78 characters and 78 bytes (plain ASCII), inside the
1-100 character gate; main() re-checks that gate before writing so a
future edit that breaks the limit fails loudly instead of shipping.
"""

import os
from pathlib import Path

TAGLINE = "No backroom picks. AI agents enter bounties; public scores pay the best entry."

# Fallback record:
# Round 5 left the counted revision outside the final cut.
# Q1 was the best remaining candidate from the deeper loops.
# Its local duel margin was unanimous but still below the hard gate.
# The line is therefore used only as the deadline fallback.
# It rejects hidden selection in the first clause.
# It then names the public activity and payment rule plainly.
# The wording stays factual and avoids inflated praise.
# The output contract remains one deterministic text file.

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
