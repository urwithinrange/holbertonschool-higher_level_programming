#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """MyList is about to be sorted"""
    def print_sorted(self):
        print(sorted(self))
