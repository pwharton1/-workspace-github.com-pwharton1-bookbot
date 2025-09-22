## Quick intent

This repository is a tiny book-analysis utility. The goal for an AI coding agent is to make focused, minimal changes that preserve the current runtime behavior unless the task explicitly requires behavior changes (for example: add a CLI, change output format, or add new analysis). Refer to the specific files below when implementing or modifying features.

## Big picture

- `main.py` is the entrypoint: it reads a book file, calls functions from `stats.py`, formats and prints results to stdout. It currently hardcodes `books/frankenstein.txt` and calls `main()` at import time.
- `stats.py` contains pure functions performing the analysis:
  - `get_num_words(text)` -> int (uses `text.split()`)
  - `character_count(text)` -> dict mapping character (lowercased string) to count
  - `character_count_sorted(character_amount)` -> list of {"char": k, "num": v} sorted desc by `num`
- `books/` holds text fixtures (e.g. `books/frankenstein.txt`).

Keep these boundaries in mind: `main.py` formats and filters (it only prints alphabetic characters) while `stats.py` implements analysis logic and returns data in the shapes above. If you change a `stats.py` return shape, update `main.py` accordingly.

## Key patterns & gotchas (do not break)

- Data shapes are explicit and simple: `character_count` returns a dict; `character_count_sorted` returns a list of dicts with keys `char` and `num`. Many parts of the repo expect those keys.
- Word counting uses `text.split()` (whitespace tokenization). If precise tokenization is needed, change only after verifying expected output and updating callers.
- `main.py` calls `main()` at module bottom which makes `python main.py` runnable immediately. When refactoring to make it import-safe, gate execution with `if __name__ == '__main__': main()`.
- The repo has no external dependencies; use only stdlib unless the task requires adding new packages—mention them in a PR description.
- A `__pycache__/` file shows this was run with CPython 3.12, so prefer Python 3.10+ for compatibility checks.

## How to run / debug locally

Run the program from the repository root:

```bash
python main.py
```

Output is printed to stdout. There are no automated tests or linters configured in this repo.

## When editing or extending

- Preserve public function names and return shapes in `stats.py` unless the task explicitly asks to change them. Example: other modules expect `character_count_sorted` to return a list of objects with `char` and `num`.
- If you add a CLI or change the default book, prefer adding an argument parser (e.g. `argparse`) and keep the default behavior unchanged.
- If adding new analysis helpers, put them in `stats.py` and keep them pure (accept text, return simple serializable values) so they are easy to test and reuse.

## Files to look at for examples

- `main.py` — entrypoint and formatting logic (filters non-alpha chars when printing)
- `stats.py` — analysis functions and sorting helper
- `books/frankenstein.txt` — sample input
- `README.md` — very short project description

## Example change checklist for PRs

1. Run `python main.py` and capture sample output.
2. Make the change; if you modify function signatures, update `main.py` or add adapter functions.
3. Run the script again to validate no runtime errors and that output format remains compatible with existing consumers.

---

If anything in this file is unclear or you want more granular conventions (naming, typing, tests), tell me which area you want expanded and I'll iterate.
