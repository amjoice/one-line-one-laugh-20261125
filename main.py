#!/usr/bin/env python3
"""One Line, One Laugh.

Writes one funny line to /output/entry.txt. Stdlib only; deterministic;
no network, no input, no randomness.

The line: a familiar password-rules setup with a dark, surprising
punchline in the last five words. 78 characters, one line, complete
on first read.
"""

import os

LINE = "My password must contain a capital, a number, and a symbol of my will to live."


def main():
    if not 1 <= len(LINE) <= 140:
        raise SystemExit("entry line must be 1-140 characters")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
