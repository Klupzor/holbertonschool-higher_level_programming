#!/usr/bin/python3
'''Rectangle
'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        ms = "[Rectangle] ({}) {}/{} - {}/{}"
        return ms.format(self.id, self.__x, self.__y,
                         self.__width, self.__height)

    def __validate_input(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(name + " must be > 0")
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(name + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.height

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @width.setter
    def width(self, value):
        self.__validate_input("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.__validate_input("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.__validate_input("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.__validate_input("y", value)
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def update(self, *args):
        arg = [self.id, self.__width, self.__height, self.__x, self.__y]
        aux = []
        for val in args:
            aux.append(val)
        aux.extend(arg[len(args):])
        self.id, self.__width, self.__height, self.__x, self.__y = aux
