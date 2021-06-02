#!/usr/bin/python3
""" Module that contains inherits_from function """


def inherits_from(obj, a_class):
    """ Function that verifies if obj is inherited from a_class """
    if type(obj) != a_class:
        return issubclass(obj.__class__, a_class)
    else:
        return False
