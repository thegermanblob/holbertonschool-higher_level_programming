#!/usr/bin/python3
def print_list_integer(my_list=[]):
    idx = 0
    en = len(my_list)
    while(idx < en):
        print("{:d}".format(my_list[idx]))
        idx += 1

