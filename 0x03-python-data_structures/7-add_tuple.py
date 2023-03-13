#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        xa, ya = 0, 0
    elif len(tuple_a) == 1:
        xa, ya = tuple_a[0], 0
    elif len(tuple_a) > 2:
        xa, ya = tuple_a[0], tuple_a[1]
    else:
        xa, ya = tuple_a
    if len(tuple_b) == 0:
        xb, yb = 0, 0
    elif len(tuple_b) == 1:
        xb, yb = tuple_b[0], 0
    elif len(tuple_b) > 2:
        xb, yb = tuple_b[0], tuple_b[1]
    else:
        xb, yb = tuple_b
    sum_tuple = (xa + xb, ya + yb)
    return (sum_tuple)
