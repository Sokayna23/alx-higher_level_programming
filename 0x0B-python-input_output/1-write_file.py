#!/usr/bin/python3
"""Module that defines write_file() function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
        
        Args:
            filename: name of the file.
            text: the text to write to the file.

        Returns:
            the numner of characters writtenb.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
