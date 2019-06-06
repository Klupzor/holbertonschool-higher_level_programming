#!/usr/bin/python3
'''Student to JSON with filter
'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            ndict = {}
            for key in attrs:
                if type(key) != str:
                    return self.__dict__
                if key in self.__dict__.keys():
                    ndict[key] = self.__dict__[key]
            return ndict
        else:
            return self.__dict__
