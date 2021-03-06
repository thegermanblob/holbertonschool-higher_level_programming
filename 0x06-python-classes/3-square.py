#!/usr/bin/python3
""" Module that makes a square class """


class Square:
    """ A class that represents a square"""

    def __init__(self, size=0):
        """ Initializes the class """

        """ Size is the new size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method that gets the area of the square"""

        result = self.__size ** 2
        return result
