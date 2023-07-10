#!/usr/bin/python3
"""Module that defines add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """
        Adds new attribute to an object if it possible.

        Arhs:
            attr_name: attribute name.
            attr_value: attribute value.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
