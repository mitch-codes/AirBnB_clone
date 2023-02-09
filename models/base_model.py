#!/usr/bin/python3
"""
Custom base class for the entire project
"""

import uuid
from datetime import datetime

class BaseModel:
    """base model class that create all objects"""

    def __init__(self):
        """constructor class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an object"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the updated at instance variable"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """create a new dictionary with the class name added to it"""
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict["__class__"] = __class__.__name__
        return (my_dict)

