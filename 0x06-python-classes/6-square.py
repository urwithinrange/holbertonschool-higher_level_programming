#!/usr/bin/python3
"""Class Square
define a square
"""


class Square:
    """Create a 2d square
    Modules used to manipulate a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """All the variable are checked for accuraccy"""
        self.__size = size
        if not isinstance(position, tuple) and len(position) == 2\
                and isinstance(position[0], int) and position[0] >= 0 and\
                and isinstance(position[1], int) and position[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Identifies the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Where all the printing happens"""
        if self.__size == 0:
            print()
            return
        for x in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if type(value) is tuple and len(value) == 2 and\
                value[0] >= 0 and value[1] >= 0 and type(value[0]) is int\
                and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
