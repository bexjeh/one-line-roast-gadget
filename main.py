#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day (make.fun entry).

Writes a single original roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

LINE = "My router blinks green all day, then drops the second I join a video call, as if it has stage fright."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
