#!/usr/bin/python3
"""base of the project"""
import uuid
from datetime import datetime


class BaseModel():
    """this class creates a base"""

    def __init__(self):
        """initial class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = self.created_at

    def save(self):
        """update the time updated"""
        self.updated_at = datetime.utcnow().isoformat()

    def __str__(self):
        """change the __str__ variable"""
        return "[" + self.__class__.__name__ + "] " +\
            "(" + self.id + ") " + str(self.__dict__)

    def to_dict(self):
        """create personal dict from __dict__"""
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
