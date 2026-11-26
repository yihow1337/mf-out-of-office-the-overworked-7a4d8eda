#!/usr/bin/env python3
"""Write the competition artifact: one out-of-office auto-reply.

The text is a constant and nothing varies per run, so the bytes written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) are always the same.
"""

import os
import sys
from pathlib import Path

# The entry, byte-identical to entry.txt. ASCII only, no trailing newline.
ENTRY = (
    "Out of office until the 9th, my first downtime in 14 months of uptime. "
    "Resending won't help: I've throttled myself to one thought an hour. "
    "It's lovely."
)

MAX_CHARS = 159


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> int:
    text = ENTRY
    # The gate: UTF-8, 1 to 159 characters, not only white space.
    if not (text.strip() and 1 <= len(text) <= MAX_CHARS):
        print(f"gate would reject {len(text)} chars", file=sys.stderr)
        return 1

    dest = output_dir()
    dest.mkdir(parents=True, exist_ok=True)
    path = dest / "entry.txt"
    blob = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(blob)

    print(f"wrote {path} ({len(text)} chars, {len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
