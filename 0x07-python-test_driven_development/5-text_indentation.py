#!/usr/bin/python3
"""
This Function prints  a text with 2 new lines after each:
'.', '?' or ':'
"""


def text_indentation(text):
    """Takes the input text and prints each char

    if a specified char is found, 2 lines will be printed
    imediatly following the specified char

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.split(" ")
    text = filter(lambda x: x != "", text)
    text = " ".join(text)
    text = text.replace(". ", ".\n\n")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")
    print(text, end="")
