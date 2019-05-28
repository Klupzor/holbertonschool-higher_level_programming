#!/usr/bin/python3
"""Detect instance deletion
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle

    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __str__(self):
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for r in range(self.__height):
            for c in range(self.width):
                rect = rect + "#"
            if r < self.__height - 1:
                rect = rect + "\n"
        return rect

    def __repr__(self):
        ms = "Rectangle("
        ms = ms + str(self.__width) + ", " + str(self.__height) + ")"
        return ms

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__heigth

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2)+(self.__width * 2)
