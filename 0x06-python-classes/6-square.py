#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
            return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value
        if value < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    @position.setter
    def position(self, value):
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        for e in range(self.position[1]):
            print()
        for i in range(self.size):
            for s in range(self.position[0]):
                print("", end=" ")
            for j in range(self.size):
                print("#", end="")
            print()
