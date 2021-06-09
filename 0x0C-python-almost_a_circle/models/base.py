#!/usr/bin/python3
""" Module contains class Base """

class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method """

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Imports a list of dictionaries to json """

        import json

        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save json string of list of objects to file """

        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as myFile:
            list_dictionaries = []
            if list_objs is None:
                myFile.write("[]")
            else:
                list_dictionaries = [
                    iter.to_dictionary() for iter in list_objs]
            myFile.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Return list of the JSON string from json_string """

        import json

        if json_string is None or len(json_string) is 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates base instance with all attributes set from dictionary """

        dict_cls = cls(**dictionary)
        dict_cls.update(**dictionary)
        return dict_cls

    @classmethod
    def load_from_file(cls):
        """ Returns lists of instances dependent on class """

        filename = cls.__name__ + ".json"
        try:
            with open(filename) as myfile:
                list_json = cls.from_json_string(myfile.read())
        except FileNotFoundError:
            return []
        return [cls.create(**kwargs) for kwargs in list_json]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves to file in csv format """

        import csv

        filename = cls.__name__ + ".csv"
        dict_list = []
        for item in list_objs:
            itemdict = item.to_dictionary()
            dict_list.append(itemdict)
        if cls.__name__ is "Square":
            fields = ['x', 'y', 'id', 'size']
        else:
            fields = ['x', 'y', 'id', 'height', 'width']
        with open(filename, "w") as myfile:
            csv_writer = csv.DictWriter(myfile, fieldnames=fields)

            csv_writer.writeheader()
            csv_writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """ loads objects from csv file """
        import csv

        dict_list = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r') as myfile:
            csv_reader = csv.DictReader(myfile)

            for lines in csv_reader:
                dict_list.append(lines)

        return [cls.create(**kwargs) for kwargs in dict_list]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws objs """
        import turtle
        import random


        for rec in list_rectangles:
            turtle.penup()
            turtle.setpos(rec.x , rec.y)
            turtle.pencolor((random.random(), random.random(),
                random.random()))
            turtle.pd()
            for i in range(0,2):
                turtle.forward(rec.width)
                turtle.right(90)
                turtle.forward(rec.height)
                turtle.right(90)
        for rec in list_squares:
            turtle.penup()
            turtle.pensize(5)
            turtle.setpos(rec.x , rec.y)
            turtle.pencolor((random.random(), random.random(),
                random.random()))
            turtle.pd()
            for i in range(0,4):
                turtle.forward(rec.width)
                turtle.right(90)
        turtle.exitonclick()


