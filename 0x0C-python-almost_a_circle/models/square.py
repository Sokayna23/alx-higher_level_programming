#!/usr/bin/python3
"""Module that defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor.

            Args:
                size (int): the size of the square.
                x (int): a postion.
                y (int): a postion.
                id (int): id of the newly created Square.
        """
        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """Gets the size of a square."""
            return self.width

        @size.setter
        def size(self, value):
            """Sets the value of size.

                Args:
                    value (int): the value of size.
            """
            self.width = value
            self.height = value

        def __str__(self):
            """Returns string representation of the square."""
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
