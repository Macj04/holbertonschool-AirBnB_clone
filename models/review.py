#!/usr/bin/python3
"""AIRBNB The console. Base class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Args:
        BaseModel (_type_): _description_
    """
    place_id = ""
    user_id = ""
    text = ""
