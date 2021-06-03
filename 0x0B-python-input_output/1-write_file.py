#!/usr/bin/python3
""" module that contains the write file function """


def write_file(filename="", text=""):

    with open(filename, "r+") as file:
        return file.write(text)
