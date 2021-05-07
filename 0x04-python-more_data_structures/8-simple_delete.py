#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    n_dic = a_dictionary
    removed_val = n_dic.pop(key, "no key")
    return(n_dic)
