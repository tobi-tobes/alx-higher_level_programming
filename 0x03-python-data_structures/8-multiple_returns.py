#!/usr/bin/python3
def multiple_returns(sentence):
    str_length = len(sentence)
    if str_length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    mul_returns = (str_length, first_char)
    return (mul_returns)
