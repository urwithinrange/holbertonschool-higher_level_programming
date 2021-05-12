#!/usr/bin/python3
"""Class Rectangle will take deminsions"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle will utilize class BaseGeometry"""

    def __init__(self, width, height):
        """Values passed in for the size of rectangle"""
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
