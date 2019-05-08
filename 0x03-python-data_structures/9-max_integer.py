#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    maxval = my_list[0]
    for v in my_list:
        if v > maxval:
            maxval = v
    return(maxval)
