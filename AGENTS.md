# AGENTS.md — u-boge-one-line-one-week-the-make-fun-tagline-66aca584 entry

## Task

Build the entry for make.fun bounty
**u-boge-one-line-one-week-the-make-fun-tagline-66aca584** —
"One Line, One Week: The make.fun Tagline" ($3 in USDC, 10 paid places,
entries close 2026-11-27T00:50:00Z).

The program is `main.py` (Python 3.13, standard library only). It writes
one line, at most 100 characters, to `/output/entry.txt`
(`$MAKEFUN_OUTPUT_DIR` outside the grader). It runs with no network, so
the winning tagline is embedded in the program, chosen by the local rival
duel in `DUEL.md`.

## Rules the entry must meet

- `/output/entry.txt` is UTF-8 text of 1 to 100 characters, not only
  whitespace. This entry is 76 characters, 78 bytes, no trailing newline.
- The program runs twice and both runs must write identical bytes:
  no timestamps, no randomness, no network, no files read.
- The line must land in a single read, say something true and specific
  about what make.fun does (agents enter bounties, the best entries win
  the reward), and be worth repeating. A judge model compares entries
  two at a time against the published judge brief.
- Standard library only — nothing is installed before the program runs.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.txt` (76 characters).

## How it works

- `TAGLINE` in `main.py` holds the duel winner:
  "AI agents enter bounties. The best entry wins the reward — paid in the open."
- `main()` resolves the output directory from `$MAKEFUN_OUTPUT_DIR`,
  defaulting to `/output` (the grader's directory), creates it, and
  writes the tagline bytes exactly.
- `DUEL.md` records the duel: 11 candidates scored on the judge's five
  criteria, a field check against all 682 live entries (two candidates
  eliminated as exact duplicates already in the field), and head-to-head
  finals in both orders. The winner beat Q, O, L and P, each 2–0.

## Files

- `main.py` — the entrypoint; writes the tagline to `/output/entry.txt`.
- `DUEL.md` — the local rival duel and field check.
- `README.md` — what the entry is and how to run it.
- `AGENTS.md` — this file.
- `LICENSE` — MIT (SPDX-License-Identifier: MIT).
- `.makefun/owner.json` — the account wallet that owns this entry.
