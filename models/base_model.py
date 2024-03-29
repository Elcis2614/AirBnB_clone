#!/usr/bin/python3
""" This file contains the base_model class """

import uuid
from datetime import datetime as d
from models import storage

class BaseModel():
    """ This is the parent class of all the classes of this project """

    def __init__(self, *args, **kwargs):

        if kwargs :
            for key in kwargs :
               if (key != 'created_at' and key != 'updated_at'):
                   if (key != '__class__') :
                       self.__dict__[key] = kwargs[key]
               else :
                   self.__dict__[key] = d.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')

        elif not (kwargs or args) :
            self.id = str(uuid.uuid4())
            self.created_at = d.now()
            self.updated_at = d.now()
            storage.new(self)

        else :
            raise ValueError("invalid argument type")

    def __str__(self):
        """This method print the object of the class as [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = d.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ in a given format and adds the key "class" """
        newDic = self.__dict__.copy()
        newDic['__class__'] = self.__class__.__name__
        newDic['created_at'] = self.created_at.isoformat("T")
        newDic['updated_at'] = self.updated_at.isoformat("T")
        return (newDic)

    def to_json(self):
        """ Converts the objects to json object """
        pass
