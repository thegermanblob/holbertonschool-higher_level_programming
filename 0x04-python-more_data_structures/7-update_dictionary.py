#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key is not None and value is not None:
        a_dictionary[key] = value
        return(a_dictionary)
