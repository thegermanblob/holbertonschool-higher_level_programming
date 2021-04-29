#!/usr/bin/python3
from sys import argv
r = 0
for i in range(1, len(argv)):
     r = r + int(argv[i])


print("{}".format(r))

