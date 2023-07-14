#! python3

from os import chdir, listdir, remove, system
from os.path import dirname, join, abspath
from platform import platform
import sys

chdir(join(dirname(__file__), ".shell"))

try:
    for file in listdir():
        abs_file = abspath(file)
        anwser = input(f"Delete {abs_file} [Y(yes) / N(no)]? ")
        if anwser == "Y":
            remove(file)
            sys.stdout.write(f"Removed file {abs_file}.\n")
        else:
            sys.stdout.write(f"Canceled Removing file {abs_file}.\n")
    else:
        sys.exit(0)
except Exception:
    sys.exit(1)