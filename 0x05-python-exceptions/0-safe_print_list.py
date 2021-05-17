#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    while(idx < x):
        try:
            print("{:d}".format(my_list[idx]), end='')
        except:
            break
        idx += 1
    print('')

    return idx
