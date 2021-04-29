#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    while i + 1 < len(argv) + 1:
        print("{:d}: {}".format(i, argv[i]))
        i = i + 1
