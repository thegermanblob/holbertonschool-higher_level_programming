#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    for item in nlist:
        if item == search:
            i = nlist.index(search)
            nlist.remove(search)
            nlist.insert(i, replace)
    return nlist
