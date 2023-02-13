#!/usr/bin/python3
""" This file contains the base_model class """


import uuid
import datetime as d


class BaseModel():
    """ This is the parent class of all the classes of this project """

    id_list = []

    def __init__(self):
        while (true):
            u_id = uuid.uuid4()
            if (u_id not in id_list):
                id_list.append(u_id)
                self.id = u_id
                break
        self.created_at = d.date.today
        self.updated_at.append(d.date.today)

    def save(self):
        """This method saves the baseModel object """
    def to_json(self):
        """ Converts the objects to json object """
