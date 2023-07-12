#!/usr/bin/python3
"""Module that defines append_after() function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line
        containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as f1:
        for line in f1:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f2:
        f2.write(text)
