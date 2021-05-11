#!/usr/bin/python3
"""Inherits_from checks if object is of a class"""


def inherits_from(obj, a_class):
    """Returns true if obj is subclass"""
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    return False
