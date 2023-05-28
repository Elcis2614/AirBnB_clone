#!/usr/bin/python3
""" This file contains the base_model class """


import uuid

from datetime import datetime as d


class BaseModel():
    """ This is the parent class of all the classes of this project """

    id_list = []

    def __init__(self):
        while (True):
            u_id = str(uuid.uuid4())
            if (u_id not in BaseModel.id_list):
                BaseModel.id_list.append(u_id)
                self.id = u_id
                break
        self.created_at = d.now()
        self.updated_at = d.now()

    def __str__(self):
        """This method print the object of the class as [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = d.now().isoformat("T")

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ in a given format and adds the key "class" """
        newDic = self.__dict__
        newDic['__class__'] = self.__class__.__name__
        newDic['created_at'] = self.created_at.isoformat("T")
        newDic['updated_at'] = self.updated_at.isoformat("T")
        return newDic
    

    def to_dic(self):
        pass

    def to_json(self):
        """ Converts the objects to json object """
