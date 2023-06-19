""" Contains TestReview class """


import unittest
from models.review import Review
from tests.test_models.common_test import Com_test


class TestReview(Com_test, unittest.TestCase):
    """ Contains methods to perform the tests"""

    def setUp(self):
        """ Sets up the obj used for testing """
        self.obj = Review()
