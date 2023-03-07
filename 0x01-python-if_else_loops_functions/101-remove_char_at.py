#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if n < 0:
        index = n % len(str)
    else:
        index = n
    for i in range(len(str)):
        if i != index:
            new_str += str[i]
    return (new_str)
