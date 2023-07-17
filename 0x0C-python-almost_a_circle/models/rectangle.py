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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    def area(self):
        """Computes the area of the recrangle."""
        return self.__width * self.__height

    def display(self):
        """Displays the Rectangle with a specific symbole."""
        shape = ''
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

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
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        elif kwargs and len(kwargs) != 0:
            if "id" in kwargs:
                if kwargs["id"] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def __str__(self):
        """Returns a string representation of Rectangle."""
        rectangle = "[Rectangle] "
        rectangle += "(" + str(self.id) + ") " + str(self.__x) + "/"
        rectangle += str(self.__y) + " - " + str(self.__width) + "/"
        rectangle += str(self.__height)
        return rectangle

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

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
