#!/usr/bin/python3
""" MOdule contains the append function """


def append_write(filename="", text=""):
    """ Function that appends text to file """

    with open(filename, 'a') as file:
        return file.write(text)
