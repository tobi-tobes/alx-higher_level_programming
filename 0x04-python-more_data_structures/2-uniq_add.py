#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return (None)
    elif len(my_list) == 0:
        return (0)
    res = 0
    prev = 0
    my_list.sort()
    for i in my_list:
        if i == prev:
            continue
        else:
            prev = i
            res += i
    return (res)
