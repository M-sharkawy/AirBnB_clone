#!/usr/bin/env python3
"""Module to create a FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Function returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Function sets in __objects
        the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Function that serializes __objects
        to the JSON file """
        obj_serialized = {}
        class_obj = FileStorage.__objects

        for key, val in class_obj.items():
            obj_serialized[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            file.write(json.dumps(obj_serialized))

    def reload(self):
        """Function deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                content = file.read()
                obj_deserialized = json.loads(content)

                for key, val in obj_deserialized.items():
                    class_name = key.split(".")[0]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**val)
        except Exception:
            pass
