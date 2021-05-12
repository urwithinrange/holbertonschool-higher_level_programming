#!/usr/bin/python3
"""from_json_string returns and object"""
import json


def from_json_string(my_str):
    """Creates an object represented by a JSON string"""
    return json.loads(my_str)
