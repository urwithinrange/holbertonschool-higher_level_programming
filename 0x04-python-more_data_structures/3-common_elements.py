#!/usr/bin/python3
def common_elements(set_1, set_2):
    temp = set(set_2)
    match = [i for i, val in enumerate(set_1) if val in temp]
    return match
