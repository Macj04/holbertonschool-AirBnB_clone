#!/usr/bin/python3
"""AIRBNB The console. Base class."""

import json
import os.path
from uuid import uuid4
from datetime import datetime


class FileStorage:
    """"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """"""
        return self.__objects
    
    def new(self, obj):
        """"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode='w') as new_file:
            json.dump(self.__objects, new_file)

    def reload(self):
        try:
            with open(self.__file_path, mode="r") as my_file:
                json.dump(self.__objects, my_file)
        except:
            pass
