#!/usr/bin/python3
""" Square class """


class Square:
    """ Square class definition """
    def __init__(self, size=0):
        """
        Initialization

        Args:
            size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square

        Returns:
            The square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Gets the seize of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the value of the size

        Args:
            value (int): the value of the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Prints the square """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
