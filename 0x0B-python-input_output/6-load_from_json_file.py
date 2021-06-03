#!/usr/bin/python3
""" Module that contains the load_from_json_file function """


def load_from_json_file(filename):
    """ Loads a dict obj from json file """

    import json
    with open(filename) as file:
        return json.load(file)
