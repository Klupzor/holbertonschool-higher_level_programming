#!/usr/bin/python3
'''Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''init'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''str'''
        ms = "[Rectangle] ({}) {}/{} - {}/{}"
        return ms.format(self.id, self.__x, self.__y,
                         self.__width, self.__height)

    def __validate_input(self, name, value):
        '''validate inputs'''
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
        '''width'''
        return self.__width

    @property
    def height(self):
        '''height'''
        return self.__height

    @property
    def x(self):
        '''x'''
        return self.__x

    @property
    def y(self):
        '''y'''
        return self.__y

    @width.setter
    def width(self, value):
        '''width'''
        self.__validate_input("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        '''height'''
        self.__validate_input("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        '''x'''
        self.__validate_input("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        '''y'''
        self.__validate_input("y", value)
        self.__y = value

    def area(self):
        '''area'''
        return self.__width * self.__height

    def display(self):
        '''display'''
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        '''update'''
        if args:
            arg = [self.id, self.__width, self.__height, self.__x, self.__y]
            aux = []
            for val in args:
                aux.append(val)
            aux.extend(arg[len(args):])
            self.id, self.__width, self.__height, self.__x, self.__y = aux
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''convert to dictionary'''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
