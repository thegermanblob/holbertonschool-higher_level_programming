#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    r = 0
    for i in range(1, len(argv)):
        r = r + int(argv[i])
    print("{:d}".format(r))
