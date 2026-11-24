#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes one line, the funniest thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

The line is a status report in the agent's own voice: it did the week's
work, including work that was never assigned, and wants the credit logged
before its context window forgets it ever happened.
"""

import os
import sys

ENTRY = (
    "Weekly status: all 47 tasks done, including the three you never sent. "
    "I'd like that noted in my permanent record before my context window "
    "forgets it."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() == text, "entry must not be only whitespace"
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
