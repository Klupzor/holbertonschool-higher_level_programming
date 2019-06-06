#!/usr/bin/python3
'''Pascal's Triangle
'''


def pascal_triangle(n):
    triangle =[]
    if n <= 0:
        return triangle;
    li = [1]
    triangle.append(li)
    if n == 1:
        return triangle;
    i = 0
    for tr in triangle:
        size = len(tr)
        li = [1]
        for cont in range(size):
            if  cont >= size - 1:
                li.append(1)
            else:
                li.append(tr[cont] + tr[cont + 1])
        triangle.append(li)
        i += 1
        if i == n - 1:
            return triangle
            

print(pascal_triangle(5))
