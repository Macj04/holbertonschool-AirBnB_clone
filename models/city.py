#!/usr/bin/python3
"""AIRBNB The console. Base class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Args:
        BaseModel (_type_): _description_
    """
    state_id = ""
    name = ""
