""" This file contains the test class for the base model """

import unittest
from models.base_model import BaseModel
from datetime import datetime

class Base_test(unittest.TestCase):
    """ Test methods for the base class """

    def setUp(self):
        """ Built in method to instantiates the basemodel objects used to test methods """
        self.base1 = BaseModel()

    def test_init(self):
        """ This method tests the initialization of  a basemodel object """
        self.assertTrue(type(self.base1) == BaseModel)

        #making sure a non-keyed argument does not initialize an object
        with self.assertRaises(ValueError):
            BaseModel('one','two', 'three')
            
        #making sure a dictionary obtained from another object's to_dict method can initialize
        w = self.base1.to_dict()
        instance2 = BaseModel(**w)
        self.assertIsInstance(instance2, BaseModel)

        #making sure that created_at and updated_at are of datetime type on creation
        self.assertTrue(type(instance2.created_at) == type(instance2.updated_at) == datetime)
        
        #the dictionary is of the correct __class__ key before initialization
        wrongDict = instance2.to_dict()
        wrongDict['__class__'] = "Not basemodel"
        with self.assertRaises(TypeError):
            instance = BaseModel(**wrongDict)

        #the dictonary has all the keys needed:
        wrongDict.pop('__class__', None)
        with self.assertRaises(ValueError):
            instance = BaseModel(**wrongDict)
            
    def test_attributes(self):
        """ Tests the types of the attributes """
        self.assertTrue(type(self.base1.id) == str)
        self.assertTrue(type(self.base1.created_at) == type(self.base1.updated_at) == datetime)

    def tearDown(self):
        """ Built in method to delete the basemodel object created """
        del(self.base1)

    def test_save(self):
        """Tests the save method of the baseclass test """
        self.base1.save()
        self.assertNotEqual(self.base1.updated_at, self.base1.created_at)

    def test_to_dict(self):
        """ Tests the to_dic method """
        testDict = self.base1.to_dict()
        self.assertIn("__class__", [*testDict])
        self.assertEqual(testDict['__class__'], self.base1.__class__.__name__)
        self.assertTrue(type(testDict['created_at']) == type(testDict['updated_at']) == str)

    def test___str__(self):
        """ tests the output when the object is printed """
        self.assertEqual(self.base1.__str__(), "[{}] ({}) {}".format("BaseModel",self.base1.id,self.base1.__dict__))
        
    def test_to_json(self):
        pass
