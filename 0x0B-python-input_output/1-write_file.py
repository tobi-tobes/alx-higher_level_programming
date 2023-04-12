#!/usr/bin/python3
"""
write_file module
This module contains the function write_file,
which writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        no_chars = f.write(text)
    return no_chars
