#!/usr/bin/python3
counter = 1
for i in range(122, 96, -1):
    if counter % 2 == 0:
        c = chr(i - 32)
    else:
        c = chr(i)
    print("{}".format(c), end="")
    counter += 1
