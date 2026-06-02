#!/usr/bin/env python

from datetime import date
import sys, subprocess, os


def main():
    SELECTION = sys.argv[1:][0]
    PATH = f"{os.getcwd()}/{SELECTION}/{date.today()}"

    try:
        os.mkdir(PATH)
        subprocess.run(["xdg-open", PATH])
    except FileExistsError:
        subprocess.run(["notify-send", "Error", "Folder already exists"])
    except PermissionError:
        subprocess.run(["notify-send", "Error", "Permission denied"])


if __name__ == "__main__":
    main()
