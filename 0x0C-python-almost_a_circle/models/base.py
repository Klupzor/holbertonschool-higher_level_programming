#!/usr/bin/python3
import json
'''Base class
'''


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
