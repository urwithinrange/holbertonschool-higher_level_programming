#!/usr/bin/python3
"""load_from_json_file creats and object"""
import json


def load_from_json_file(filename):
    """returns contents of filename"""
    with open(filename, mode="r", encoding='utf-8') as f:
        return json.loads(f.read())
