#!/usr/bin/python3
"""
    Module that defines a function
"""


def is_kind_of_class(obj, a_class):
    """
        Determines either an object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class.

        Args:
            obj: object
            a_class: class

        Return:
            True: if yes,
            False: otherwise.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
