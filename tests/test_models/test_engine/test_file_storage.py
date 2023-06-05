""" This file contains the test class for the engine"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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
        #the all() method return a dictionary
        self.assertIsInstance(self.instance1.all(), dict)

        #the new() method sets the correct object in __object
        instanceBaseM = BaseModel()
        key = "BaseModel.{}".format(instanceBaseM.id)
        self.assertIn(key, self.instance1.all())

        #the save() method 
        if isfile(FileStorage._FileStorage__file_path):
            self.instance1.save()
            with open(FileStorage._FileStorage__file_path,'r', encoding = 'utf-8') as mFile:
                #the save() method() saved a string in the file
                if (self.instance1.all() != []):
                    self.assertIsNotNone(mFile.read())

        #the reload() method opens the file incase it exists but doesnt do anything incase the file is not present
        FileStorage._FileStorage__objects = []
        self.instance1.reload()
        self.assertIsNotNone(self.instance1.all())
        
