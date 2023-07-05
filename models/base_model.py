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
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        to_add = {'__class__': self.__class__.__name__}
        new_dict.update(to_add)
        to_add = {'created_at': self.created_at.isoformat()}
        new_dict.update(to_add)