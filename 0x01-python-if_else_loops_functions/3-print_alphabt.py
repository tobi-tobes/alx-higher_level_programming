#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == 'e':
        continue
    elif chr(i) == 'q':
        continue
    else:
        print(chr(i), end="")
