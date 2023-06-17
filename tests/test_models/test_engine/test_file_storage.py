""" This file contains the test class for the engine"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from os.path import isfile

class testEngine(unittest.TestCase):
    """ Tests methods """
    
    def setUp(self):
        """ sets up the object(s) used for testing """
        self.instance1 = FileStorage()

    def test_CaseAttributes(self):
        """ test the class attributs of FileStorage """     
        self.assertTrue(type(FileStorage._FileStorage__objects) == dict)
        pass

    def test_methods(self):
        """ the all() method return a dictionary """
        self.assertIsInstance(self.instance1.all(), dict)

    def test_mew(self) :
        """ the new() method sets the correct object in __object """
        instanceBaseM = BaseModel()
        dictBaseM =  self.instance1.all()
        key = "BaseModel.{}".format(instanceBaseM.id)
        self.assertIn(key, dictBaseM)
        self.assertTrue(dictBaseM[key] == instanceBaseM)

    def tstSerial(self, obj): 
        """ tests the reload() and save method for the obj """
        obj.save()

        mDict = self.instance1.all()
        self.assertEqual(mDict["{}.{}".format(obj.__class__.__name__, obj.id)], obj)
        mDict["{}.{}".format(obj.__class__.__name__, obj.id)] = None
        self.assertIsNone(mDict["{}.{}".format(obj.__class__.__name__, obj.id)])
        self.instance1.reload()
        self.assertTrue(mDict["{}.{}".format(obj.__class__.__name__, obj.id)].to_dict() == obj.to_dict())

    def test_serialBaseModel(self):
        """ tests the reload() method and save """
        instanceBaseM = BaseModel()
        self.tstSerial(instanceBaseM)
        del(instanceBaseM)

    def test_serialUser(self):
        """ tests the serialization and deserialisation of User object """
        user = User()
        self.tstSerial(user)
        del(user)
        
    """def test_reload(self):
        the reload() method opens the file incase it exists but doesnt do anything incase the file is not present
        self.instance1.reload()
        objects = self.instance1.all()
        self.assertIsNotNone(objects)
        for obj_id in objects:
            self.assertIsInstance(objects[obj_id], BaseModel)"""
