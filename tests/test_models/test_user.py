""" Contains test class for the user class """


from tests.test_models.common_test import Com_test
from models.user import User
import unittest


class TestUser(unittest.TestCase, Com_test):
    """ Contains methods to perform the tests"""
    
    def setUp(self) :
        """ Sets up the object used to test """
        self.obj = User()

    def test_attributes(self):
        """ Test the attributes on object creation """

        self.assertTrue(self.obj.email == self.obj.password == self.obj.first_name == self.obj.last_name == "")
