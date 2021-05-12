#!/usr/bin/python3
"""
write_file writes a string to a text file and
returns the numbmber of characters written
"""


def write_file(filename="", text=""):
    """write_file writes a string into a file

        - filename is the name of the file being written to
        - text is the string to be written into filename
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
