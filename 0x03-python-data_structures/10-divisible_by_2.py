#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    li = []
    for idx in my_list:
        if idx % 2 == 0:
            li.append(True)
        else:
            li.append(False)
    return li
