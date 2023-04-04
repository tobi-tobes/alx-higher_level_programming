#!/usr/bin/python3
"""
text_indentation module
This module contains the function text_indentation,
 which prints a text with 2 new lines after each
of these characters: ., ? and :.
"""


def text_indentation(text):
    """prints a text with 2 new lines after
 each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i], end="")
            print()
            print()
            i += 2
        else:
            print(text[i], end="")
            i += 1
