#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if(my_list is None):
        return(None)
    idx = 1
    en = len(my_list)
    while(idx <= en):
        print("{:d}".format(my_list[-idx]))
        idx += 1
