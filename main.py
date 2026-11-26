#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — a make.fun entry.

The fridge light judges the 2 a.m. snacks, and it does so with the
full confidence of an appliance that has never paid rent or done the
dishes. The roast works because the light is the only witness to the
midnight snack, and it still thinks it is the responsible one in the
kitchen. The fridge, meanwhile, has never lifted a finger — it just
stands there, cold, humming, and quietly superior.

One line, written to the file the harness reads. Nothing else happens.
"""

from os import environ, makedirs, path

# The entry itself. One line roasting the fridge: the light that
# judges the midnight snack while contributing nothing to the rent.
# The light is the only witness — and it still thinks it is the adult.
LINE = "The fridge light judges my 2 a.m. snacks, yet it has never once paid rent or done the dishes."

# The bounty gate for this entry allows at most 199 characters.
LIMIT = 199


def entry_text():
    """Return the entry line, checked against the bounty gate."""
    text = LINE
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{LIMIT}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    """Write the entry line to the harness output file."""
    out_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(out_dir, exist_ok=True)
    target = path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
