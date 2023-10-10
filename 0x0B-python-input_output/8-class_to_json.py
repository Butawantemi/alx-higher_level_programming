#!/usr/bin/python3
"""Class to JSON"""
def class_to_json(obj):
    """Serialize an object into a dictionary with a simple data structure for JSON"""
    return obj.__dict__
