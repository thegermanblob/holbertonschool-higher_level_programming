#!/usr/bin/python3
""" Module that contains student class """


class Student:
    """ CLass that represents a student """

    def __init__(self, first_name, last_name, age):
        """ initilizatation method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves dict representation of class """

        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            self.key = json[key]
