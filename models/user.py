#!/user/bin/python3
"""
add user information to json data
"""

from models.base_model import BaseModel
import json

class User(BaseModel):
    """this is a subclass of BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
