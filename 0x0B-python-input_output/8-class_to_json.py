#!/usr/bin/python3
"""Module that defines class_to_json() function."""
import json


def class_to_json(obj):
    """Returns the dictionary descriptiom for JSON serialization of an object.

        Args:
            obj: object.

        Returns:
            a dictionary description.
    """
    return (obj.__dict__)
