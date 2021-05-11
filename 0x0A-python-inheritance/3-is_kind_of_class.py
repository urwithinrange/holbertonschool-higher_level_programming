#!/usr/bin/python3
"""is_kind_of_class returns true of false"""


def is_kind_of_class(obj, a_class):
    """Determines if obj is of type class"""
    if isinstance(obj, a_class):
        return True
    return False
