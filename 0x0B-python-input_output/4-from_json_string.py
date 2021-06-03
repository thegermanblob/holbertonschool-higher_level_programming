#!/usr/bin/python3
""" Module that contains the from_json_string """


def from_json_string(my_str):
    """ Function that reads from a json string """
    import json
    return json.loads(my_str)
