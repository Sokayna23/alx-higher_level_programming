#!/usr/bin/python3
""" Module that defines Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class"""

    def __init__(self, width, height):
        """Instantiation """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns a description of rectangle"""
        description = "[" + str(self.__class__.__name__) + "] "
        description += str(self.__width) + "/" + str(self.__height)
        return (description)
