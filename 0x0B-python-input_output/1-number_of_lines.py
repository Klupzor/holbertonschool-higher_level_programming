#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, 'r', encoding="UTF8") as f:
        ofile = f.read()
        return ofile.count("\n")
