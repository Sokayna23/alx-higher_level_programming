#!/usr/bin/python3
"""Module that defines append_write() functio"""


def append_write(filename="", text=""):
    """
        Appends a string at the end of a text file (UTF8).

        Args:
            filename: file name.
            text: the text to append to the file.

        Returns:
            the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write)
