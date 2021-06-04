#!/usr/bin/python3
""" Module contains class_to_json function """


def class_to_json(obj):
    """ make a dict about obj in json format """
    return obj.__dict__
