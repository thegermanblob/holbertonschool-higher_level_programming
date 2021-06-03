#!/usr/bin/python3
""" module that contains the write file function """


def write_file(filename="", text=""):
    """ function that writes to a file returns characters written """

    with open(filename, "w") as file:
        return file.write(text)
