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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        jlist = []
        with open(filename, 'w', encoding="utf-8") as f:
            for obj in list_objs:
                jlist.append(obj.to_dictionary())
            f.write(str(jlist))

    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
