#!/usr/bin/python3
"""Read_file reads a txt file and prints to stdout"""

def read_file(filename=""):
    """filename is the file to be read by read_file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
