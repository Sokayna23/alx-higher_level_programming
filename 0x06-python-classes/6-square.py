#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Definition of the class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializion of a new square

        Args:
            size (int): size of the square
            position (int): the position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the value to the size variable

            Args:
                value (int): the value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Gets the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value of position

            Args:
                value (int): the value of the position
        """
        if (not (isinstance(value, tuple)) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * 2)

    def my_print(self):
        """Prints a square wthi #"""
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
