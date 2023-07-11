#!/usr/bin/python3
"""
    Module that defines a script that adds all arguments to a Python list
    then save them to a file.
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    filename = "add_item.json"

    try:
        my_item = load_from_json_file(filename)
    except FileNotFoundError:
        my_item = []

    for arg in argv[1:]:
        my_item.append(arg)

    save_to_json_file(my_item, filename)
