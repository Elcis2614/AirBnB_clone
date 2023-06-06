""" tests the init file of the model module """

import unittest
from os.path import getsize

class test_init(unittest.TestCase):
    """ contains test casese """

    def test_init(self) :
        """ test if the file storage module class is importd """
        import models
        self.assertIsNotNone(models.storage)
