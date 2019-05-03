#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    result = 0
    for c in range(1, args + 1):
        result = result + int(sys.argv[c])
    print(result)
