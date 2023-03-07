#!/usr/bin/python3
for i in range(90):
    if i != 89:
        if i % 10 == 0:
            continue
        elif i % 10 == i // 10:
            continue
        elif i % 10 < i // 10:
            continue
        print("{:02d}".format(i), end=", ")
    else:
        print("{}".format(i))
