#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """class used to serialize and deserialize objects into files"""
    
    __file_path = ""
    __objects = {}
    
    def all(self):
        """return dictionary of objects"""
        return (__objects)
    
    def new(self, obj):
        """sets __object width object and object.id as key"""
        __objects[str(odj.id)] = obj
    
    def save(self):
        """write json data into file"""
        with open(__file_path, w) as f:
            data = json.dumps(__objects)
            f.write(data)

    def reload(self):
        """deserialize json data in file"""
        with open (__file_path, r) as f:
            data = f.read()
            __objects = json.loads(data)
