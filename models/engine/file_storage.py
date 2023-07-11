#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """class used to serialize and deserialize objects into files"""
    
    __file_path = "file.json"
    __objects = {}
    __myobjects = {}
    
    def all(self):
        """return dictionary of objects"""
        return (self.__objects)
    
    def new(self, obj):
        """sets __object width object and object.id as key"""
        myId = obj.__class__.__name__ + "." + obj.id
        #self.__objects[myId] = obj
        self.__objects[myId] = obj
        self.__myobjects[myId] = obj.to_dict()
    
    def save(self):
        """write json data into file"""
        data = json.dumps(self.__myobjects)
        with open(self.__file_path, 'w') as f:
            f.write(data)

    def destroy(self, objId):
        """write json data into file"""
        del self.__objects[objId]

    def reload(self):
        """deserialize json data in file"""
        try:
            with open(self.__file_path, "r") as f:
                dict = json.loads(f.read())
                self.__objects = {}
                for key in dict:
                    self.__objects[key] = BaseModel(**dict[key])
        except:
            pass
