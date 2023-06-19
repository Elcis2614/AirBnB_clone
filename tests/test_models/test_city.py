""" Test cases for the city class"""


import unittest
from models.city import City
from tests.test_models.common_test import Com_test

class TestCity(Com_test, unittest.TestCase):
    """ Methods for the tests """

    def setUp(self):
        self.obj = City()
