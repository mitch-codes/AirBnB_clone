#!/user/bin/python3
"""
add city information to json data
"""

from models.base_model import BaseModel
import json

class City(BaseModel):
    """this is a subclass of BaseModel"""

    state_id = ""
    name = ""
