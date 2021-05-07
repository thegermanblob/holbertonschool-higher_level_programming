#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        comp = 0
        result = None
        for key, value in a_dictionary.items():
            if comp < value:
                comp = value
                result = key
        return(result)
    else:
        return(None)

