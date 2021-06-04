#!/usr/bin/python3
""" Module that contains student class """


class Student:
    """ CLass that represents a student """

    def __init__(self, first_name, last_name, age):
        """ initilizatation method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves dict representation of class """
        return self.__dict__
