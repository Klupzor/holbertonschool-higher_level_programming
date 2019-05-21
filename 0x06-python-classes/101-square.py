#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        msg = ""
        if self.size == 0:
            return ""
        for e in range(self.position[1]):
            msg = msg + "\n"
        for i in range(self.size):
            for s in range(self.position[0]):
                msg = msg + " "
            for j in range(self.size):
                msg = msg + "#"
            if i < self.size - 1:
                msg = msg + "\n"
        return msg

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
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for e in range(self.position[1]):
                print()
            for i in range(self.size):
                for s in range(self.position[0]):
                    print("", end=" ")
                for j in range(self.size):
                    print("#", end="")
                print()
