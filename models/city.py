#!/usr/bin/python3
"""AIRBNB The console. Base class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class
    """
    state_id = ""
    name = ""
