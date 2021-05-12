#!/usr/bin/python3
"""append_write adds a string to the end of an existing file"""


def append_write(filename="", text=""):
    """
    append_write adds strings to the end of a file
        - filename to determine file to be modified
        - text is the string to be added to the file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return(f.write(text))
