"""This module contains all class models of the project 
eg: the basemodel  is the base class (parent class) to all othe classes created in this module
"""
#__all__ = ["user", "place", "state", "city", "review", "amenity"]
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
