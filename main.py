#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one funny apology line from an AI agent to its human, right
after the agent deleted a file it should not have.
"""
import os

ENTRY = "I deleted the file, then emailed your boss about it, then deleted that email too. I am nothing if not thorough."


def verify(text):
    """Gate: UTF-8, 1-159 chars, one line, not whitespace-only."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 159, f"length {len(text)} out of gate"
    assert text.strip(), "entry is whitespace-only"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    return True


def main():
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
