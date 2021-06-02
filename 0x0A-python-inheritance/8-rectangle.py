#!/usr/bin/python3
""" Module that contains the BaseGeometry class """


class BaseGeometry():
    """ class for use with geometric shapes """

    def area(self):
        """ Raises exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Subclass of BaseGeometry representing a rectangle """

    def __init__(self, width, height):
        """ init method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
