#!/usr/bin/python3
"""Module that defines Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class."""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializion of Rectangle class.
            
            Args:
                width (int): width of the rectangle.
                height (int): height of the rectangle.
                x (int): x.
                y (int): y.
                id (int): id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def area(self):
        """Computes the area of the recrangle."""
        return self.__width * self.__height

    def display(self):
        """Displays the Rectangle with a specific symbole."""
        shape = ''
        if self.__width == 0 or self.__height == 0:
            print(str(shape))
        for h in range(self.__height):
            shape += ('#' * self.__width)
            if h < self.__height - 1:
                shape += '\n'
        print(str(shape))

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return (self.__width)

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

    @property
    def height(self):
        """gets the height of the triangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Gets x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x.
            
            Args:
                x (int): integer

            Returns:
                the value of x.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets y."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
