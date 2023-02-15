#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """class used to serialize and deserialize objects into files"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return dictionary of objects"""
        return (self.__objects)
    
    def new(self, obj):
        """sets __object width object and object.id as key"""
        myId = obj.__class__.__name__ + "." + obj.id
        self.__objects[myId] = obj.to_dict()
    
    def save(self):
        """write json data into file"""
        with open(self.__file_path, "w") as f:
            data = json.dumps(self.__objects)
            f.write(data)

    def reload(self):
        """deserialize json data in file"""
        with open (self.__file_path, "r") as f:
            data = f.read()
            self.__objects = json.loads(data)
