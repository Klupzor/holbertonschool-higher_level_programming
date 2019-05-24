#!/usr/bin/python3


def text_indentation(text):
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        while i < len(text):
            c = text[i]
            print(c, end="")
            if c == "." or c == "?" or c ==":":
                print()
                print()
                if text[i + 1] == " ":
                    i += 1
            i += 1

