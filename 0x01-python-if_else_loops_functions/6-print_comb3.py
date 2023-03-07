#!/usr/bin/python3
for i in range(90):
    if i < 10:
        print(f"0{i}", end=", ")
    elif i >= 10 and i != 89:
        if i % 10 == 0:
            continue
        elif i % 10 == i // 10:
            continue
        elif i % 10 < i // 10:
            continue
        print(i, end=", ")
    elif i == 89:
        print(i)
