#!/usr/bin/python3
""" Module contains class Base """


class Base:
    """ Base class """
    __nb_objects = 0
    def __init__(self, id=None):
        """ init method """
        if id != None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects
