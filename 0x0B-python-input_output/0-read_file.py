#!/usr/bin/python3
""" Module that defines read_file() function"""
def read_file(filename=""):
    """Function that reads a text file (UTF8)
        and prints it to stdout

        Args:
            filename: name of the file to be read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
