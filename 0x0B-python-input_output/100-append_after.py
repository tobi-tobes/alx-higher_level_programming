#!/usr/bin/python3
"""
append_after module
This module contains the function append_after,
which inserts a line of text to a file, after
each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after
 each line containing a specific string"""
    if len(filename) == 0 or len(search_string) == 0:
        return
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if search_string in lines[i]:
            if (i + 1) < len(lines) - 1:
                lines.insert(i + 1, new_string)
            else:
                lines.append(new_string)
        else:
            continue
    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(lines)
