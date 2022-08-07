#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """this class creates a base"""

    def __init__(self):
        """initial class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()
        self.__dict__['__class__'] = __class__.__name__
        print(self.__dict__)

    def save(self):
        """update the time updated"""
        self.updated_at = datetime.today().isoformat()


m = BaseModel()
