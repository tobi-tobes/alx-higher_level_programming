#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_args = len(sys.argv) - 1
    if no_args == 0:
        print("0 arguments.")
    elif no_args == 1:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(no_args))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
