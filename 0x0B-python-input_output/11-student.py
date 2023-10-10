#!/usr/bin/python3
""" A class representing a student with first_name, last_name, and age attributes"""
class Student:
    """Initializes a Student instance with first_name, last_name, and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """Retrieve a dictionary representation of a Student instance"""
    def to_json(self, attrs=None):
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
    """Replace all attributes of the Student instance based on a provided JSON dictionary"""
    def reload_from_json(self, json):
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
