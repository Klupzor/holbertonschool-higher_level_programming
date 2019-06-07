#!/usr/bin/python3
'''First Rectangle
'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
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
        self.__width = value
    @height.setter
    def height(self, value):
        self.__height = value
    @x.setter
    def x(self, value):
        self.__x = value
    @y.setter
    def y(self, value):
        self.__y = value
