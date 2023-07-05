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
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save data time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creation of new_dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['create_at'] = self.created_at.isoformat()
        new_dict['update_at'] = self.updated_at.isoformat()
        return new_dict
