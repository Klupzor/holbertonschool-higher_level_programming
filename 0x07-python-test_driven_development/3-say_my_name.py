#!/usr/bin/python3
"""Say my name

This script print My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Function that divides all elements of a matrix

    Parameters
    ----------
    first_name : str
        The first name
    last_name : str
        The last name

    Raises
    ----------
    TypeError
        first_name and last_name must be a string

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
