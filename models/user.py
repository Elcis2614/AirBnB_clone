#!/usr/bin/python3
""" The user class represents the user """

from models.base_model import BaseModel


class User(BaseModel):
    """ Inherits from the Basemodel class"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
