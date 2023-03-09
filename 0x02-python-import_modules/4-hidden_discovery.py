#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4, sys
    list = dir(hidden_4)
    for i in list:
        if i[0] == "_":
            continue
        else:
            print(i)
