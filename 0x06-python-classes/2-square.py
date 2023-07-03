#!/usr/bin/python3
"""
Square class defines a square
"""


class Square:
    """
    Square class definition
    """
    def __init__(self, size=0):
        """
        Initialization

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
