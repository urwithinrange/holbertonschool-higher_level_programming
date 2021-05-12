#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class Rectangle will take deminsions"""

class Rectangle(BaseGeometry):
    """Rectangle will utilize class BaseGeometry"""

    def __init__(self, width, height):
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
