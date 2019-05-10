#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    num = sum(list(map(lambda t: t[0] * t[1], my_list)))
    den = sum(list(map(lambda t: t[1], my_list)))
    return num / den
