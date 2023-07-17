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

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute.

            Args:
                *args : variable number of arguments.
                    1st argument : id
                    2nd argument : width
                    3rd argument : height
                    4th argument : x
                    5th argument : y
                **kwargs: key/value pairs of attributes
        """
        if args and len(args) != 0:
            if args[0] is None:
                self.__init__(self.width, self.height, self.x, self.y)
            else:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            if "id" in kwargs:
                if kwargs["id"] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """Returns string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
