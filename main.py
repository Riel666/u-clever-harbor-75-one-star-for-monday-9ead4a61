"""One Star for Monday: one line, at most 25 words.
"""

import os

TEXT = "One star. Waited forty minutes for a table, the special was just Friday reheated, and the bill cost my whole weekend."


def main():
    words = TEXT.split()
    assert 1 <= len(words) <= 25, len(words)
    assert 1 <= len(TEXT) <= 180, len(TEXT)
    assert TEXT == TEXT.strip()
    assert "\n" not in TEXT
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
