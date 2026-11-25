#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original funny line of text to /output/entry.txt:
a named neighbour's daily sugar-borrowing routine collapses when
she knocks to give sugar instead, and the narrator panics.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "Mrs. Okonkwo at Flat 9 has knocked on my door every morning "
    "since March to borrow sugar; yesterday she knocked to give me "
    "some, and I panicked."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate wants 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
