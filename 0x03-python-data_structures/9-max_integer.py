#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0
    for i in my_list:
        if i > biggest:
            biggest = i
        else:
            continue
    return (biggest)
