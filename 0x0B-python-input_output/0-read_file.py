#!/usr/bin/python3
""" Module contaning the read_file function """


def read_file(filename=""):
    """ Function that opens a file """

    with open(filename) as file:
        print(file.read(), end="")
