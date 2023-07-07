#!/usr/bin/python3
"""AIRBNB The console. Base class."""
import json


class FileStorage:
    """Stoarge of files class. Serialization and desearlization."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Creating a new obj"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialization of objects to JSON File"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as new_file:
            json.dump(data, new_file)

    def reload(self):
        from models.base_model import BaseModel
        """Deserialization of objects to JSON File"""
        try:
            with open(FileStorage.__file_path, mode="r") as my_file:
                objects = json.load(my_file)
                for key, value in objects.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
