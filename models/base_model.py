#!/usr/bin/python3
"""
Custom base class for the entire project
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """base model class that create all objects
    
    Attributes:
        id(str): a universally unique id for each user
        created_at: the time user or object was created
        updated_at: the time changes were last made
    
    Methods:
        __str__: prints string representation of our object
        save(self): updates updated_at variable
        to_dict(self): returns a dictionary of all instance variables
    
    """

    def __init__(self, *args, **kwargs):
        """constructor class"""
        if kwargs:
            for key, value in kwargs.items():
                if (key == "created_at"):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == "updated_at"):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == "id"):
                    self.id = value
                elif (key == "__class__"):
                    pass
                else:
                    self.__setattr__(key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of an object"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

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

