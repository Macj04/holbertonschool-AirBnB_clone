#!/usr/bin/python3
"""AIRBNB The console. Base class."""

import json
import os.path
from uuid import uuid4
from datetime import datetime
from models import base_model


class FileStorage:
    """Stoarge of files class. Serialization and desearlization."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all dictionary"""
        return self.__objects
    
    def new(self, obj):
        """Creating a new obj"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialization of objects to JSON File"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        
        with open(self.__file_path, mode='a') as new_file:
            json.dump(data, new_file)

    def reload(self):
        """Deserialization of objects to JSON File"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as my_file:
                self.__objects = json.load(my_file)
        except:
            pass
