#!/usr/bin/python3
def magic_string(cont=[0]):
    cont[0] += 1
    return ("Holberton, " * cont[0])[:-2]
