#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = my_list[0]
    if len(my_list) == 0:
        return (None)
    for i in range(1, len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]
        else:
            continue
    return (biggest)
