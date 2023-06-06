"""This module contains all class models of the project 
eg: the basemodel  is the base class (parent class) to all othe classes created in this module
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
