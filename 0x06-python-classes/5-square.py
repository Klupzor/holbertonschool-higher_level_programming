#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
            return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value
        if value < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
