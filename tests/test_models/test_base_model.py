""" This file contains the test class for the base model """

import unittest
from models.base_model import BaseModel
from datetime import datetime
from tests.test_models.common_test import Com_test

class Base_test(Com_test, unittest.TestCase):
    """ Test methods for the base class """

    def test_init(self):
        #making sure a non-keyed argument does not initialize an object
        with self.assertRaises(ValueError):
            BaseModel('one','two', 'three')

        #making sure a dictionary obtained from another object's to_dict method can initialize
        instance = BaseModel()
        w = instance.to_dict()
        instance2 = BaseModel(**w)
        self.assertIsInstance(instance2, BaseModel)

        #making sure that created_at and updated_at are of datetime type on creation
        self.assertTrue(type(instance2.created_at) == type(instance2.updated_at) == datetime)
            
