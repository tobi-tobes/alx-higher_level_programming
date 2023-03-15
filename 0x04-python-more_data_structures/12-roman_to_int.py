#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    elif isinstance(roman_string) is False:
        return (0)
    roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    i, integer, less_than = 0, 0, 0
    while i < len(roman_string):
        current = roman_dict[roman_string[i]]
        if i != len(roman_string) - 1:
            nxt = roman_dict[roman_string[i + 1]]
            if current < nxt:
                less_than = nxt - current
                integer += less_than
                i += 2
                continue
            else:
                integer += current
                i += 1
                continue
        else:
            integer += current
            break
    return (integer)
