#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print("{} arguments.".format(args))
    else:
        print("{} arguments:".format(args))
        for c in range(1, args + 1):
            print("{}: {}".format(c, sys.argv[c]))
