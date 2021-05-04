#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    en = len(my_list) - 1
    if(idx > en or idx < 0):
        return(my_list)
    elif(my_list is None):
        return(None)
    elif(element is None):
        return(None)
    else:
        my_list[idx] = element
        return(my_list)
