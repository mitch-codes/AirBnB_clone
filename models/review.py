#!/user/bin/python3
"""
add review to json data
"""

from models.base_model import BaseModel
import json

class Review(BaseModel):
    """this is a subclass of BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
