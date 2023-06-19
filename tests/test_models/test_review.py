""" Contains TestReview class """


import unittest
from models.review import Review
from tests.test_models.common_test import Com_test


class TestReview(Com_test, unittest.TestCase):
    """ Contains methods to perform the tests"""

    def setUp(self):
        """ Sets up the obj used for testing """
        self.obj = Review()

    def test_attributes(self):
        """ tests the attribute of the object """
        self.assertTrue(self.obj.place_id == self.obj.user_id == self.obj.text == "")
