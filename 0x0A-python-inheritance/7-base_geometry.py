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
