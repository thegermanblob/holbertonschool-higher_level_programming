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
