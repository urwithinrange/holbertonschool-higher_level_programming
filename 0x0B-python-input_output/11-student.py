#!/usr/bin/python3
"""class Student defines a student"""


class Student:
    """Student will recieve input to define instance attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return dict((key, value) for (key, value) in self.__dict__.items())
        else:
            return dict((key, value) for (key, value) in self.__dict__.items()
                        if key in attrs)

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
