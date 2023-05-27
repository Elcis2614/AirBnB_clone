""" This file contains the test class for the base model """

import unittest
from models.base_model import BaseModel


class Base_test(unittest.TestCase):
    """ Test methods for the base class """

    def setUp(self):
        """ Built in method to instantiates the basemodel objects used to test methods """
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_save(self):
        """Tests the save method of the baseclass test """
        self.base1.save()
        self.assertNotEqual(self.base1.updated_at, self.base1.created_at)

    def to_dict(self):
        """ Tests the to_dic method """
        testDict = self.base1.to_diict()
        self.assertIn("__class__", [*testDict])
        self.assertEqual(testDict['__class__'], self.base1.__classs__.__name__)
        assertTrue(type(testDict['created_at']) == type(testDict['updated_at']) == str)

    def test_to_json(self):
        pass
