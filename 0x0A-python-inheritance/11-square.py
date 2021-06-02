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

    def area(self):
        """ method that returns area of rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ Determines how it should be printed """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)

        return string


class Square(Rectangle):
    """ Subclass of Rectangle """

    def __init__(self, size):
        """ Init Method """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area Method returns area of square """
        return self.__size * self.__size

    def __str__(self):
        """ Determines how it should be printed """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)

        return string
