#!/usr/bin/python3
"""AIRBNB The console. Base class."""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        from models import storage
        """Init files function"""
        if len(kwargs) > 0:
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, iso_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, iso_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        """Save data time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Creation of new_dict"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
