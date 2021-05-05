#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    en = len(new_list) - 1
    if(idx > en or idx < 0):
        return(my_list)
    elif(my_list is None):
        return(None)
    elif(element is None):
        return(None)
    else:
        new_list[idx] = element
        return(new_list)
