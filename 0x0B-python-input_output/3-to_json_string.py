#!/usr/bin/python3
"""Module that defines to_json_string() function"""
import json


def to_json_string(my_obj):
    """
        Function that returns JSON representation of an object.

        Args:
            my_obj (str): string.

        Returns:
            JSON object.
    """
    return (json.dumps(my_obj))
