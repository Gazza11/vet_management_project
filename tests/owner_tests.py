import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    
    
    def setUp(self):
        self.owner1 = Owner("Liam Morrice", 998234, "13 Thistle Drive", "AB34 6WB", True)

    def test_owner_name(self):
        self.assertEqual("Liam Morrice", self.owner1.name)

    def test_owner_number(self):
        self.assertEqual(998234, self.owner1.number)

    def test_owner_address(self):
        self.assertEqual("13 Thistle Drive", self.owner1.address)

    def test_owner_postcode(self):
        self.assertEqual("AB34 6WB", self.owner1.postcode)

    def test_owner_registered(self):
        self.assertEqual(True, self.owner1.registered)