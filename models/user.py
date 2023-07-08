#!/usr/bin/python3
"""AIRBNB The console. Base class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Args:
        BaseModel (_type_): _description_
    """
    email = ""
    password = ""
    fist_name = ""
    last_name = ""
