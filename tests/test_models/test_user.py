""" Contains test class for the user class """


from models.base_model import BaseModel
from models.user import User
from models import storage
import unittest

class TestUser(unittest.TestCase):
    """ Contains methods to perform the tests"""
    
    def setUp(self) :
        """ Sets up the object used to test """
        self.user1 = User()

    def test_init(self) :
        """ tests the initialization of a User instance """
        self.assertIsInstance(self.user1, BaseModel)
        self.assertTrue(self.user1.email == self.user1.password == self.user1.first_name == self.user1.last_name == "")
        key = "User.{}".format(self.user1.id)
        self.assertIn(key, storage.all())

        """ tests initialiasation on an instance based on a dictionary """
        mDict = self.user1.to_dict()
        instance = User(**mDict)
        self.assertIsInstance(instance, User)

    def test_toDict(self) :
        """ Tests the format of the to_dict methof """
        mDict = self.user1.to_dict()
        self.assertIsInstance(mDict, dict)
        self.assertEqual(mDict['__class__'], 'User')
