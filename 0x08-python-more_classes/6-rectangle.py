#!/usr/bin/python3
"""Module that defines Rectangle class """


class Rectangle:
    """The class Rectangle

        Attributes:
            number_of_instances (int): the number of instances of Rectangle.
   """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization function

        Args:
            width (int): the width.
            height (int): the height.
        """
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
            self.__height = height
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the triangle"""
        return (self.__width)

    @property
    def height(self):
        """gets the height of the triangle"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """Sets the value of the width

            Args:
                value (int): an integer.
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Set height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Creates a string representation of Rectangle using '#' character"""
        shape = ''
        if (self.__width == 0 or self.__height == 0):
            return (shape)
        for h in range(self.__height):
            shape += '#' * self.__width
            if h < self.__height - 1:
                shape += '\n'
        return (shape)

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        number_of_instances -= 1
