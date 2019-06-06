#!/usr/bin/python3
'''Student to disk and reload
'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            ndict = {}
            for key in attrs:
                if key in self.__dict__.keys():
                    ndict[key] = self.__dict__[key]
            return ndict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json.keys():
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]
