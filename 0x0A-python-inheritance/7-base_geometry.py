#!/usr/bin/python3
"""
    Module that defines an empty class ''BaseGeomtry''
"""


class BaseGeometry:
    """
        An empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates the value, it must be an integer.

            Args:
                name (str): name
                value (int): value
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.name = value
