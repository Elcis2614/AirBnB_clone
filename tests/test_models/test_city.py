""" Test cases for the city class"""


import unittest
from models.city import City
from tests.test_models.common_test import Com_test

class TestCity(Com_test, unittest.TestCase):
    """ Methods for the tests """

    def setUp(self):
        """ sets up the object for testing """
        self.obj = City()

    def test_attributes(self):
        """ tests object attributes """
        self.assertTrue(self.obj.state_id == self.obj.name == "")
