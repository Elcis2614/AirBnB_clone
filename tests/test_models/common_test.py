""" This file contains the test class for common test methods """

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from os.path import isfile

class Com_test():
    """ Commom test methods for base models and its instances """
    obj = BaseModel()
    def set_Up(self, obj = None):
        """ Built in method to instantiates the basemodel objects used to test methods """
        if not obj:
            self.obj = BaseModel()
        else: 
            self.obj = obj

    def test_init(self):
        """ This method tests the initialization of the models module and of the basemodel object """
        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(storage, FileStorage)
 
        #newly create obj is in the dictionary
        self.assertIn("{}.{}".format(self.obj.__class__.__name__,self.obj.id), storage.all())

        
        #making sure the file is loaded in __object
        if isfile(FileStorage._FileStorage__file_path) :
            self.assertIsNotNone(FileStorage._FileStorage__objects)

            
    def test_attributes(self):
        """ Tests the types of the attributes """
        self.assertTrue(type(self.obj.id) == str)
        self.assertTrue(type(self.obj.created_at) == type(self.obj.updated_at) == datetime)

    def test_save(self):
        """Tests the save method of the baseclass test """
        self.obj.save()
        self.assertNotEqual(self.obj.updated_at, self.obj.created_at)
        self.assertTrue(self.obj.updated_at > self.obj.created_at )
        
        try :
            with open(FileStorage._FileStorage__file_path, 'r', encoding = 'utf-8') as mFile:
                self.assertIsNotNone(mFile.read())
        except FileNotFoundError :
            pass

    def test_to_dict(self):
        """ Tests the to_dic method """
        testDict = self.obj.to_dict()
        self.assertIn("__class__", [*testDict])
        self.assertEqual(testDict['__class__'], self.obj.__class__.__name__)
        self.assertTrue(type(testDict['created_at']) == type(testDict['updated_at']) == str)

    def test___str__(self):
        """ tests the output when the object is printed """
        self.assertEqual(self.obj.__str__(), "[{}] ({}) {}".format(self.obj.__class__.__name__, self.obj.id,self.obj.__dict__))
        
    def test_to_json(self):
        pass
