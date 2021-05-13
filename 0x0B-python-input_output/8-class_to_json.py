#!/usr/bin/python3
"""class_to_json returns a dictionary description"""


def class_to_json(obj):
    """class_to_json uses ojb to find a description"""
    return vars(obj)
