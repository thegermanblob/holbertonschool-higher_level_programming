#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    i = nlist.index(search)
    nlist.remove(i)
    nlist.insert(i, replace)
    return nlist
