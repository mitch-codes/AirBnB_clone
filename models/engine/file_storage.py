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
    
    def all(self):
        """return dictionary of objects"""
        return (self.__objects)
    
    def new(self, obj):
        """sets __object width object and object.id as key"""
        myId = obj.__class__.__name__ + "." + obj.id
        #self.__objects[myId] = obj.to_dict()
	self.__objects[myId] = obj
    
    def save(self):
        """write json data into file"""
        """with open(self.__file_path, "w+") as f:
            data = json.dumps(self.__objects)
            f.write(data)
	"""
	my_obj_dict = {}
        for key in self.__objects:
            my_obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_obj_dict, f)

    def reload(self):
        """deserialize json data in file"""
        """try:
            with open(self.__file_path, "r") as f:
                dict = json.loads(f.read())
                self.__objects.update(dict)
        except:
            pass
	"""
	my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])

