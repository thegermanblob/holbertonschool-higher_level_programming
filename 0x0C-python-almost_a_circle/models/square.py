#!/usr/bin/python3
""" Module that contains the square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that represents a square """
    err_msg = "position must be a tuple of 2 positive integers"

    def __init__(self, size, x=0, y=0, id=None):
        """ Function to initialize the square given the size """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns current size of Square """
        return self.width

    @size.setter
    def size(self, size):
        """ Sets size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates atributes to those of square """
        if args is not None and len(args) is not 0:
            argc = list(args)
            if len(args) > 1:
                argc.insert(1, args[1])
            super().update(*argc)
        else:
            super().update(**kwargs)
            if "size" in kwargs:
                self.width = kwargs['size']

    def __str__(self):
        """ Returns string representation of square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """ Returns dictionary representation of square """
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.width}
