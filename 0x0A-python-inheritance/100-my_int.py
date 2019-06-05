#!/usr/bin/python3


class MyInt(int):
    def __eq__(self, other):
        return int(self) == int(other)
