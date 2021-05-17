#!/usr/bin/python3
"""Class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square is a special Rectangle with 4 equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        new_list = ["id", "size", "x", "y"]
        if args:
            for x in range(len(args)):
                setattr(self, new_list[x], args[x])
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
	    """creates the dictionary representation of Square"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.width}
