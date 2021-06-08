#!/usr/bin/python3
""" Module contains class Base and Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Class representing a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Returns width of rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets and validates width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ Returns height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets and validates height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Sets and validates x """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Returns y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Sets and validates y """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Method for finding area of Rectangle """
        return self.__height * self.__width

    def display(self):
        """ Displays the rectangle with # """
        print('\n' * self.y, end="")
        print((" " * self.x + (self.width * "#") + '\n') * self.height, end="")

    def __str__(self):
        """ Returns string representation of class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns argument to each attribute """
        argc = len(args)
        if argc > 0:
            self.id = args[0]
            if argc > 1:
                self.width = args[1]
                if argc > 2:
                    self.height = args[2]
                    if argc > 3:
                        self.x = args[3]
                        if argc > 4:
                            self.y = args[4]
        elif kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if "height" in kwargs:
                self.height = kwargs['height']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ converts obj to dictionary format """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
