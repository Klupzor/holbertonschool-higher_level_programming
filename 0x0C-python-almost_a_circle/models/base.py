#!/usr/bin/python3
'''Base class
'''
import json
import csv


class Base:
    '''Instances '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''init'''
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert to json'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save to file'''
        filename = cls.__name__ + ".json"
        jlist = []
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is not None:
                for obj in list_objs:
                    jlist.append(obj.to_dictionary())
            f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        '''Convert json to string'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Create a dictionary'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''load from json'''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, encoding="UTF8") as f:
                strjson = cls.from_json_string(f.read())
                return list(map(lambda dic: cls.create(**dic), strjson))
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        '''save file csv'''
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', encoding="UTF8") as f:
                strcsv = csv.DictReader(f)
                dictlist = list(map(lambda dic: dic, strcsv))
                intList = [dict([key, int(val)]
                                for key, val in y.items()) for y in dictlist]
                return list(map(lambda dic: cls.create(**dic), intList))
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Save to file'''
        filename = cls.__name__ + ".csv"
        jlist = []
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is not None:
                for obj in list_objs:
                    jlist.append(obj.to_dictionary())
            keys = jlist[0].keys()
            new_dic = csv.DictWriter(f, keys)
            new_dic.writeheader()
            new_dic.writerows(jlist)
