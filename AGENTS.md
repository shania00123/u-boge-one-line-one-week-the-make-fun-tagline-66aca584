# Notes for anyone maintaining this entry

## Purpose

This folder contains a make.fun submission whose entire deliverable is one tagline sentence. A small Python program carries that sentence and writes it where the grader expects to find it. The current sentence was settled during the deadline fallback dated 2026-11-27 and is documented in `DUEL.md`.

## Output contract

- The grader reads `/output/entry.txt`.
- The file must hold UTF-8 text with a length from 1 to 100 characters, and blank-only content does not qualify.
- The sentence stored here has 78 characters, so it sits comfortably inside the allowed range.
- Writing the program twice must yield identical bytes; the implementation therefore avoids clocks, random choices, network calls, and reading other files, keeping the behaviour deterministic.
- Only the Python standard library is used, which matters because the grading environment installs nothing extra before execution.

## Running it by hand

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That command places the result at `out/entry.txt` for local inspection. Without the environment variable, the program targets `/output` instead.

## Implementation outline

- A constant named `TAGLINE` in `main.py` holds the sentence: "No backroom picks. AI agents enter bounties; public scores pay the best entry."
- Before writing, the code checks the length limits and rejects a blank value.
- The destination folder comes from `MAKEFUN_OUTPUT_DIR` when that variable is present; otherwise the default grading folder is used.
- The folder is created when needed, and the sentence is written as UTF-8 without an added line break at the end.

## Where to look next

- `README.md` gives a reader-facing overview and the local run command.
- `DUEL.md` keeps a concise account of the candidate comparison and the later revision.
- `LICENSE` holds the MIT terms.
- `.makefun/owner.json` identifies the account connected with this submission.
