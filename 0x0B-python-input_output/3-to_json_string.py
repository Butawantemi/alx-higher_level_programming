#!/usr/bin/python3
"""to json string"""
import json
"""serialize an object int json"""
def to_json_string(my_obj):
    """Serialize an object into its JSON representation and return it as a string"""
    return json.dumps(my_obj)
