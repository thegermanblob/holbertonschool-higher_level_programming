#!/usr/bin/python3
def element_at(my_list, idx):
    en = len(my_list)
    if(idx > en or idx < 0):
        return(None)
    elif (my_list == None):
        return(None)
    else:
        return(my_list[idx])
