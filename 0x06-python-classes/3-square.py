#!/usr/bin/python3
"""
Square class that defines a square by its size
"""


class Square:
    """
    The class Square definition
    """

    def __init__(self, size):
        """
        Initialization

        Args:
            size (int): the size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
