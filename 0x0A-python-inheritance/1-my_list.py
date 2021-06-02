#!/usr/bin/python3
""" module that contains the Mylist class """


class MyList(list):
    """ New list based class """

    def print_sorted(self):
        print(sorted(self))
