#!/usr/bin/python3
"""
"""


def inherits_from(obj, a_class):
    """
        Determines wether an object inherits from a specified class.
        Args:
            obj: object
            a_class: class

        Return:
            True if yes,
            False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
