#!/usr/bin/python3
"""A module that defines a class """


class MyList(list):
    """a devided class of list class"""
    def print_sorted(self):
        """Prints a list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
