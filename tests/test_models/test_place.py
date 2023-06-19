""" Test cases for the place class"""

from tests.test_models.common_test import Com_test
from models.place import Place
import unittest

class TestPlace(Com_test, unittest.TestCase):
    
    def setUp(self):
        """ Sets up the obj to be used for testings """
        self.obj = Place()

    def test_attributes(self):
        """ test the attributes of the obj """
        self.assertTrue(self.obj.name == self.obj.description == self.obj.city_id == self.obj.user_id == "")
        self.assertTrue(self.obj.number_rooms == self.obj.number_bathrooms == self.obj.max_guest == self.obj.price_by_night == 0)
        self.assertTrue(self.obj.latitude == self.obj.longitude == 0.0)
        self.assertTrue(self.obj.amenity_ids == [""])
