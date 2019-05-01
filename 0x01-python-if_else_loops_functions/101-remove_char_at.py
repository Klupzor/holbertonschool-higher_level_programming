#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        cp1 = str[:n]
        cp2 = str[n + 1:]
        return cp1 + cp2
