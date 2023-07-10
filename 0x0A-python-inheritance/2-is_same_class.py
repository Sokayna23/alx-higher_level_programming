#!/usr/bin/python3
"""
    Module: defines a function that determines if an object is an instance
    of a specified class.
"""

def is_same_class(obj, a_class):
    """
        Function that determines wheither an object is an instance of a class 
        Args:
            obj: object
            a_class: class
        Returns:
            True: if yes,
            False: otherwise.
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
