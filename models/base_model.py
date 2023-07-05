#!/usr/bin/python3
"""AIRBNB The console. Base class."""

from uuid import uuid4
from datetime import datetime

class BaseModel():
    """Class for base model"""

    def __init__(self):
        """Init files function"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['update_at'] = self.update_at.isoformat()
        return new_dict
