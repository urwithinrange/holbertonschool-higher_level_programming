#!/usr/bin/python3
"""Class Rectangle will take deminsions"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle will utilize class BaseGeometry"""

    def __init__(self, width, height):
        """Values passed in for the size of rectangle"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[{:s}] {:d}/{:d}".format((type(self).__name__),
                                        self.__width, self.__height))
