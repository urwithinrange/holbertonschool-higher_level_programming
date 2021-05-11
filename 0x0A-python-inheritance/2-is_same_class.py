#!/usr/bin/python3
"""Is_same_class - a function that returns true or false"""


def is_same_class(obj, a_class):
    """Checking a_class to determine its type"""
    if isinstance(obj, a_class):
        return 1
    else:
        return 0
