#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word: Gaslighting — the Wi-Fi swears it is connected, full bars,
while nothing loads. It insists everything is fine. It is not fine.
"""

import os

WORD = "Gaslighting"


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
