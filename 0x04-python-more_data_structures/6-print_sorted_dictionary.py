#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dict = a_dictionary.copy()
    for key, value in sorted(b_dict.items()):
        print(key, ':', value)
