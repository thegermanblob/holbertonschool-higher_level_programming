#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for idx, item in enumerate(my_list):
        try:
            print("{:d}".format(my_list[idx]), end='')
        except:
            print("",end='')
            
        idx += 1
    print('')

    return idx
