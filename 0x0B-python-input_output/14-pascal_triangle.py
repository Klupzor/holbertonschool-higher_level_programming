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
    li = [1, 1]
    triangle.append(li)
    if n == 2:
        return triangle;

    for i in range(n - 2):
        for tr in triangle:
            size = len(tr)
            if size >= 2:
                li = [1]
                for cont in range(size):
                    print(cont)
                    if  cont == size - 1:
                        li.append(1)
                        break
                    else:
                        li.append(tr[cont] + tr[cont + 1])
                    print(li)
                triangle.append(li)
    return triangle;
            

print(pascal_triangle(3))
