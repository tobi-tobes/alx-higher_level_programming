#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    elif my_list[0] == None:
        return (None)
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
