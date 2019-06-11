#!/usr/bin/python3
import json
'''Base class
'''


class Base:
    '''Instances '''
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert to json'''
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save to file'''
        filename = cls.__name__ + ".json"
        jlist = []
        with open(filename, 'w', encoding="utf-8") as f:
            for obj in list_objs:
                jlist.append(obj.to_dictionary())
            f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        '''Convert json to string'''
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Create a dictionary'''
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''load from json'''
        filename = cls.__name__ + '.json'
        with open(filename, encoding="UTF8") as f:
            strjson = cls.from_json_string(f.read())
            return list(map(lambda dic: cls.create(**dic), strjson))
