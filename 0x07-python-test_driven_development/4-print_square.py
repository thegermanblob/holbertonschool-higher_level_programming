#!/usr/bin/python3
""" Module that contains square """


def print_square(size):
    """ Function that prints a square and validates size """


    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for x in range(0, size):
            for y in range(0, size):
                print("#", end="")
            print("")
