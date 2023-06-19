#!/usr/bin/python3
""" The Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Inherits from the BaseModel """
    place_id = ""
    user_id = ""
    text = ""
