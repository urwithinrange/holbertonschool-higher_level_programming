#!/usr/bin/python3
"""Is_same_class - a function that returns true or false"""


def is_same_class(obj, a_class):
    """Checking a_class to determine its type"""
    if type(obj) is a_class:
        return True
    else:
        return False
