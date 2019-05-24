#!/usr/bin/python3
"""Text identation
This script prints a text with 2 new lines after each of these characters:
. ? :

"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each characters

    Parameters
    ----------
    text : str
        The text to be printed

    Raises
    ----------
    TypeError
        text must be str

    """
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        while i < len(text):
            c = text[i]
            print(c, end="")
            if c == "." or c == "?" or c == ":":
                print()
                print()
                if text[i + 1] == " ":
                    i += 1
            i += 1
