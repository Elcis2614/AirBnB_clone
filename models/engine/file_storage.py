#!/usr/bin/python3
""" This file contains, only the FileStorage class """

import json
from os.path import isfile
from os.path import getsize

class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON file to instances """

    __file_path = "models/engine/file.json"
    __objects = {}

    def all(self):
        """ returns the __object dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        try :
            with open(FileStorage.__file_path, "w", encoding='utf-8') as mFile :
                dict_copy = {}
                for key in FileStorage.__objects.keys() :
                    dict_copy[key] = FileStorage.__objects[key].to_dict()
                json.dump(dict_copy, mFile)
        except FileNotFoundError:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file exits and non-empty """
        if isfile(FileStorage.__file_path) and getsize(FileStorage.__file_path) > 1:

            with  open(FileStorage.__file_path, "r", encoding='utf-8') as mFile :
                m_objects = json.load(mFile)
                for obj_id in m_objects.keys():
                    base_object = m_objects[obj_id]

                    if ('BaseModel' in obj_id.split(".")):
                        from models.base_model import BaseModel
                        FileStorage.__objects[obj_id] = BaseModel(**base_object)

                    elif ('User' in obj_id.split(".")):
                        from models.user import User
                        FileStorage.__objects[obj_id] = User(**base_object)
