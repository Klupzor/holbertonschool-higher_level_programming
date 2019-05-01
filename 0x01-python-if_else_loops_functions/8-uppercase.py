#!/usr/bin/python3
def uppercase(str):
    upp = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            upp += chr(ord(c) - 32)
        else:
            upp += c
    print("{}".format(upp))
