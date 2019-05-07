#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    r=[0, 0]
    a.append(0)
    a.append(0)
    b.append(0)
    b.append(0)
    for c in range(0, 2):
        r[c] = a[c] + b[c]
    return (tuple(r))
