#!/usr/bin/python3
"""
append_write module
This module contains the function append_write,
which appends a string at the end of a text
file (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, 'a', encoding="utf-8") as f:
        no_chars = f.write(text)
    return no_chars
