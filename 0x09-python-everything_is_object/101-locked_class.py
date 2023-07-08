#!/usr/bin/python3
""" LockedClass definition"""


class LockedClass:
    """ This class is to prevent the user from creating new instance
        attributes, except if the new instance attribute is 
        called first_name
    """
    __slots__ = ["first_name"]
