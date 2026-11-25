#!/usr/bin/env python3
"""Roast Your Fridge entry.

Writes one original roast of the entrant's fridge to /output/entry.txt.

The roast is a single line about a mystery container in the freezer that
has outlasted three relationships -- the freezer equivalent of a tenant
who never pays rent and never moves out. Pure standard library only;
deterministic output: the same roast every run, byte for byte.
"""

import os

OUTPUT_FILENAME = "entry.txt"

JOKE = (
    "There's a container in my freezer older than my last three "
    "relationships, and unlike them, it refuses to leave."
)


def resolve_output_path() -> str:
    """Resolve the entry file path from MAKEFUN_OUTPUT_DIR (default /output)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, OUTPUT_FILENAME)


def gate(text: str) -> None:
    """Output gate: entry must be one non-empty line within the 1-200 char gate."""
    if not text:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry rejected: output must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry rejected: line is {len(text)} chars, must be 1-200")


def main() -> None:
    text = JOKE.strip()
    gate(text)
    if not text.strip():
        # Gate already rejects empty text; this guards against a
        # whitespace-only roast slipping through a future JOKE change.
        raise ValueError("entry must not be only whitespace")
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
