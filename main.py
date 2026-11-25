#!/usr/bin/env python3
"""Out-of-office reply entry for make.fun.

Writes one line to entry.txt: the auto-reply the sponsor would switch on.
Deterministic: no network, no randomness, no clock, no input files. The
output is exactly the constant LINE, with no trailing newline, so the file
is byte-identical on every run.
"""

import os

LINE = "Back on Tuesday, a date I chose because it sounds more believable than Friday."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
