#!/usr/bin/python3
"""AIRBNB The console. Base class."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        """Init files function"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """Return string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save data time"""
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creation of new_dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
