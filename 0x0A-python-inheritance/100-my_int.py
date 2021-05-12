#!/usr/bin/python3
"""MyInt compares object to int"""


class MyInt(int):
    """Reversing the operators"""
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
