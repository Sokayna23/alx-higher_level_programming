#!/usr/bin/python3
"""Defines a subclass Square of the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initialization of Square

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
