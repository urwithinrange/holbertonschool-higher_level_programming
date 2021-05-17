#!/usr/bin/python3
"""Class Rectangle defines the dimensions of a rectangle"""
from models.base import Base


class Rectangle(Base):
    """contains private instance attributes for rectangle"""
    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.w_h_integer_validator("width", width)
        self.w_h_integer_validator("height", height)
        self.x_y_integer_validator("x", x)
        self.x_y_integer_validator("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.w_h_integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.w_h_integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.x_y_integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.x_y_integer_validator("y", value)
        self.__y = value

    def area(self):
        """area returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the a rectangle height x width"""
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        new_list = ["id", "width", "height", "x", "y"]
        if args:
            for x in range(len(args)):
                setattr(self, new_list[x], args[x])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
	"""creates the dictionary representation of Rectangle"""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
