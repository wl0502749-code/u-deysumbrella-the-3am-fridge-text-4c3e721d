#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes the single line a smart fridge texts its owner at 3am
to /output/entry.txt (1-140 chars, UTF-8, single line).
"""

import os

LINE = "3am. The leftovers and I heard the floorboards. We're both pretending you're here for water."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
