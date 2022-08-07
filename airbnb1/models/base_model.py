#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.__dict__['__class__'] = 'BaseModel'

    def save(self):
        self.updated_at = datetime.today().isoformat()
