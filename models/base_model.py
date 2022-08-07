#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """this class creates a base"""

    def __init__(self):
        """initial class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = self.created_at
        self.__dict__['__class__'] = __class__.__name__
        print(self.__str__)

    def save(self):
        """update the time updated"""
        self.updated_at = datetime.utcnow().isoformat()

    def __str__(self):
        """change the __str__ variable"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
