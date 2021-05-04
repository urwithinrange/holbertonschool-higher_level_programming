#!/usr/bin/python3
"""Class Square
define a square
"""


class Square:
    """Create a 2d square"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
