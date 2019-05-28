# Python - Everything is object
0. What function would you use to print the type of an object?
1. How do you get the variable identifier (which is the memory address in the CPython implementation)?
2. In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100
3. In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89
4. In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a
5. In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a + 1
6. What do these 3 lines print?
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
7. What do these 3 lines print?
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
8. What do these 3 lines print?
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
9. What do these 3 lines print?
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
10. What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
11. What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
12. What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
13. What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
14. What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
15. What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
16. What does this script print?
def increment(n):
    n += 1

    a = 1
    increment(a)
	print(a)
17. What does this script print?
def increment(n):
    n.append(4)

	l = [1, 2, 3]
	increment(l)
	print(l)
18. What does this script print?
def assign_value(n, v):
    n = v

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assign_value(l1, l2)
	print(l1)
19. Write a function def copy_list(l): that returns a copy of a list.
20. Is a a tuple? Answer with Yes or No. a = ()
21. a = (1, 2) Is a a tuple? Answer with Yes or No.
22. a = (1) Is a a tuple? Answer with Yes or No.
23. a = (1, ) Is a a tuple? Answer with Yes or No.
24. What does this script print?
a = (1)
b = (1)
a is b
25. What does this script print?
a = (1, 2)
b = (1, 2)
a is b
26. What does this script print?
a = ()
b = ()
a is b
27. Will the last line of this script print 139926795932424? Answer with Yes or No.
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
28. >>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
29. Clear strings
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
* How many string objects are created by the execution of the first line of the script? (106-line1.txt)
* How many string objects are created by the execution of the second line of the script (106-line2.txt)
* After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
* After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
* How many string objects are created by the execution of the last line of the script (106-line5.txt)
