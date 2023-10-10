#!/usr/bin/python3
"""to JSON"""
import json
"""Serialize an object into JSON"""
def save_to_json_file(my_obj, filename):
    """Serialize an object into its JSON representation and save it to a text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
