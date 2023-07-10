#!/usr/bin/python3
"""
    Module: defines a function that determines if an object is an instance
    of a specified class.
"""

def is_same_class(obj, a_class):
    """
        Function that determines wheither an object is an instance of a class 

        Returns:
            True: if yes,
            False: otherwise.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
