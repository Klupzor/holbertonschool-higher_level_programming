#!/usr/bin/python3
'''Read n lines
'''


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="UTF8") as f:
        if not nb_lines <= 0:
            for c in range(nb_lines):
                ofile = f.readline()
                print(ofile, end="")
        else:
            ofile = f.read()
            print(ofile, end="")
