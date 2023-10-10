#!/usr/bin/python3
"""write the class"""
class Student:
    """A class representing a student with first_name, last_name, and age attributes"""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            res = {}
            for attr in attrs:
                if hasattr(self, attr):
                    res[attr] = getattr(self, attr)
            return res
