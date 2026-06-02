#!/usr/bin/env python

import sys, subprocess, os


def main():
    SELECTION = sys.argv[1:][0]
    PATH = f"{os.getcwd()}/{SELECTION}"

    subprocess.run(
        [
            "flatpak",
            "run",
            "com.raggesilver.BlackBox",
            f"--working-directory={PATH}",
            PATH,
        ]
    )


if __name__ == "__main__":
    main()
