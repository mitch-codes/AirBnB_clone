#!/user/bin/python3
"""
add state information to json data
"""

from models.base_model import BaseModel
import json

class State(BaseModel):
    """this is a subclass of BaseModel"""

    name = ""
