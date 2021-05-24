#!/usr/bin/python3
""" module that contians the rectangle class """


class Rectangle:
    """ Class that defines a  rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialithation method """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

        return int(self.__height * self.__width)

    def perimeter(self):
        """ method that returns the perimeter of rec """

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ creates rectangle with # """

        if self.__height == 0 or self.__width == 0:
            return ""
        symbol = self.print_symbol
        return ((str(symbol) * self.__width + '\n') * self.__height)[0:-1]

    def __repr__(self):
        """ standard format """

        rp = ("{} ({}, {})".format(self.__class__.__name__,
              self.width, self.height))
        return rp

    def __del__(self):
        """ method that gets called when al instances are deleted """

        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ check which is bigger """

        if not isinstance(rect_1, Rectangle):
            TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            TypeError("rect_2 must be an instance of Rectangle")

        return rect_2 if rect_2.area() > rect_1.area() else rect_1
