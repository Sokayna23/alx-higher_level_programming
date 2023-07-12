#!/usr/bin/python3
"""Module that defines load_from_json_file() function."""
import json


def load_from_json_file(filename):
    """
        Creates an Object from a JSON file.

        Args:
            filename: file name

        Returns:
            An Object.
    """
    with open(filename) as f:
        return (json.load(f))
