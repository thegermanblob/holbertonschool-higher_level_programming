#!/usr/bin/python3
""" Module that contains the save_to_json_file function """


def save_to_json_file(my_obj, filename):
    """ Function that save json into file """
    import json
    with open(filename) as file:
        file.write(json.dumps(my_obj))
