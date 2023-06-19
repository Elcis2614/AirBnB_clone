"""Test case for the amenity class"""


import unittest
from models.amenity import Amenity
from tests.test_models.common_test import Com_test

class TestAmenity(Com_test, unittest.TestCase):
    """ nethods to perform the tests"""
    
    def setUp(self):
        self.obj = Amenity()

    def test_attributes(self):
        """ test the attribute of the object """
        self.assertTrue(self.obj.name == "")
