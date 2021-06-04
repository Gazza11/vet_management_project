import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet("Troy", "Barker", "Mon, Tues, Weds, Fri", "06/09/1991")

    def test_vet_first_name(self):
        self.assertEqual("Troy", self.vet1.first_name)

    def test_vet_last_name(self):
        self.assertEqual("Barker", self.vet1.last_name)

    def test_vet_working_days(self):
        self.assertEqual("Mon, Tues, Weds, Fri", self.vet1.working_days)

    def test_vet_date_of_birth(self):
        self.assertEqual("06/09/1991", self.vet1.date_of_birth)