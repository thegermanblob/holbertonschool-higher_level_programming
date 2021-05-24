#!/usr/bin/python3
""" module that contians the rectangle class """


class Rectangle:
    """ Class that defines a  rectangle """


    def __init__(self, width=0, height=0):
        """ Initialithation method """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width getter """

        return self.__width

    @property
    def height(self):
        """ height getter """

        return self.__height

    @width.setter
    def width(self, width):
         """ width setter """

         if not isinstance(width, int):
             raise TypeError("width must be an integer")
         if width < 0:
             raise ValueError("width must be >= 0")
         self.__width = width

    @height.setter
    def height(self, height):
        """ height setter """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


    def area(self):
        """ method that returns area of rectangle """

        return self.__height * self.__width

    def perimeter(self):
        """ method that returns the perimeter of rec """

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))
