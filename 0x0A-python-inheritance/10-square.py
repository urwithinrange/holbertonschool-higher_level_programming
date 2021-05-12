#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry does something using area soon"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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


class Square(Rectangle):
    """Square takes a sigle dimension"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
