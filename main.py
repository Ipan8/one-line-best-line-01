#!/usr/bin/env python3
"""One Line, Best Line — make.fun entry.
Writes the one-line entry to /output/entry.txt.
Entry: "My to-do list has a to-do list, and it just filed a complaint about me."
"""
import os

ENTRY = "My to-do list has a to-do list, and it just filed a complaint about me."  # 72 chars, limit 120

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
