#!/usr/bin/python3
from sys import argv
i = 1
if len(argv) == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(argv) - 1))
while i + 1 < len(argv) + 1:
    print("{}: {}".format(i, argv[i]))
    i = i + 1
