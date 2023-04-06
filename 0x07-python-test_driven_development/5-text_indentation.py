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
    if text is None:
        raise TypeError("text must be a string")
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif len(text) == 0:
        raise ValueError("string can't be empty")
    i = 0
    while text[i] == " ":
        i += 1
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i], end="")
            print()
            print()
            i += 1
        elif text[i] == " " and text[i - 1] == " " and text[i + 1] == " ":
            print("", end="")
            i += 1
        elif text[i] == " " and (text[i - 1] == " " or text[i + 1] == " "):
            print("", end="")
            i += 1
        elif text[i] == " " and (text[i - 1] == "." or text[i - 1] == "?"
                                 or text[i - 1] == ":"):
            print("", end="")
            i += 1
        else:
            print(text[i], end="")
            i += 1
