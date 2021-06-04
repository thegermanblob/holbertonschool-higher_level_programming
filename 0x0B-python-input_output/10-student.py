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
        if attrs == None:
            return self.__dict__
        elif type(attrs) == list:
            i = 0
            res_list =[]
            temp_list = self.__dict__
            for item in temp_list:
                if item == attrs[i]:
                    res_list.append(item)
                i += 1

