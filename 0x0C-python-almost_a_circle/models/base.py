#!/usr/bin/python3
"""Module that defines Base class."""


class Base:
    """
        Base class definition.

        Attributes:
            nb_objects (int): number of objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation
            
            Args:
                id (int): id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
