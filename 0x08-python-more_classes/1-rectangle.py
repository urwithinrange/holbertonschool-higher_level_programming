#!/usr/bin/python3
"""
This Class Rectangle will create a rectangle
"""


class Rectangle:
    """
    Rectangle contains all the functions and \
    modules to create rectangle
    """

    def __init__(self, width=0, height=0):
        """Values for the height and width of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def heignt(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
