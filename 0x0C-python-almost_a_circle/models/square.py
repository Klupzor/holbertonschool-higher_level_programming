#!/usr/bin/python3
'''Square inherits from Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ms = "[Square] ({}) {}/{} - {}"
        return ms.format(self.id, self.x, self.y,
                self.width)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)
