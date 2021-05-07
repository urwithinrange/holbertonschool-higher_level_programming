#!/usr/bin/python3
"""add_integer adds integers"""


def add_integer(a, b=98):
    """add_integer adds a + b"""
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
