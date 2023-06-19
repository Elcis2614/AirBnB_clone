""" Test cases for the place class"""

from tests.test_models.common_test import Com_test
from models.place import Place
import unittest

class TestPlace(Com_test, unittest.TestCase):
    
    def setUp(self):
        """ Sets up the obj to be used for testings """
        self.obj = Place() 
