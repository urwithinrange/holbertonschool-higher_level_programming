#!/usr/bin/python3
"""Square Class
define a square
"""


class Square:
    """ Form a 2d square """
    def __init__(self, size=0):
        """confirms valid input before setting size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
