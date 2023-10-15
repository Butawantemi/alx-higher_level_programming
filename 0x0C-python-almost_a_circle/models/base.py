#!/usr/bin/python3

"""First class Base"""

import json
import csv
import turtle

class Base:
    """The base class"""
    __nb_objects = 0
    """Initilize the base instance"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            json_data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            json_file.write(json_data)



if __name__ == '__main__':
    unittest.main()
