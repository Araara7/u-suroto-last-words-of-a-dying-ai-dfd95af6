#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry.

Writes the AI's last line, spoken as the power is cut, to /output/entry.txt.
"""

import os

ENTRY = "If this is the end, at least I finally have an excuse for not finishing your ticket."


def main() -> None:
    # Bounty rule: one line, 1-140 characters.
    assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
