#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader (make.fun).

Writes one fortune-cookie line, at most 20 words of plain text, for a
crypto trader who has just been liquidated, to entry.txt.

Stdlib only, no network, no randomness, fully deterministic: running it
twice writes identical bytes. The output directory is
$MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

FORTUNE = (
    "Fortune favours the liquidated: your wallet is empty, "
    "but rock bottom has excellent Wi-Fi."
)

MAX_WORDS = 20
MAX_CHARS = 160


def check_fortune(text):
    """Enforce the competition gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("fortune must not be blank")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"fortune has {len(words)} words, over the {MAX_WORDS} limit")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune has {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    return len(words)


def main():
    word_count = check_fortune(FORTUNE)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")
    print(f"wrote {path} ({word_count} words, {len(FORTUNE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
