#!/usr/bin/python3
import json
""" MOdule that contains the to_json_string function """


def to_json_string(my_obj):
    """ Function that makes json strings from given obj """

    return json.dumps(my_obj)
