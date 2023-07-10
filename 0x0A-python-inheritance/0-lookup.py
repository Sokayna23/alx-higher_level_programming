#!/usr/bin/python3
"""Module that defines a lookup function that returns
    the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list object of attributes and methodes.

        Args:
            obj (list): a list object.
    """
    return (dir(obj))
