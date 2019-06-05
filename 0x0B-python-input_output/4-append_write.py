#!/usr/bin/python3
'''Write to a file
'''


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
