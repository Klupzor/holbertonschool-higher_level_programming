#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return(None)
    n_list = []
    for v in my_list:
        if v % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return(n_list)
