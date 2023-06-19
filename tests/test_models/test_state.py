""" Contains test class for the state class """


import unittest
from tests.test_models.common_test import Com_test
from models.state import State


class TestState(Com_test ,unittest.TestCase):
    """ Contains methods to perform the tests"""

    def setUp(self):
        """ sets up the object to be used """
        self.obj = State()
        
