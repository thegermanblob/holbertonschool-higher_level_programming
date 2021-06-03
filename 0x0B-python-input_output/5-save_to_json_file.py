#!/usr/bin/python3
""" Module that contains the save_to_json_file function """


def save_to_json_file(my_obj, filename):
    """ Function that save json into file """
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
