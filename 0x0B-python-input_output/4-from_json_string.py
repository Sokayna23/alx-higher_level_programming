#!/usr/bin/python3
"""Module that defines from_json_string() function."""
import json


def from_json_string(my_str):
    """
        Returns an object (Python data structure) represented by JSON string.

        Args:
            my_str: a string.

        Returns:
            JSON object.
    """
    return (json.loads(my_str))
