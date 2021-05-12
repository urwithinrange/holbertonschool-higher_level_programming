#!/usr/bin/python3
"""save_to_json_file - function that writes to file"""
import json


def save_to_json_file(my_obj, filename):
    """saving my_obj into the filename"""
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
