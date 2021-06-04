import unittest
from models.animal import Animal 

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal1 = Animal("Garfield", "12/06/2018", current_vet, "cat", 555679, "Too heavy, must diet to lose 2KG.")

        self.vet1 = Vet("Troy", "Barker", "Mon, Tues, Weds, Fri", "06/09/1991")

    def test_animal_name(self):
        self.assertEqual("Garfield", self.animal1.name)

    def test_animal_date_of_birth(self):
        self.assertEqual("12/06/2018", self.animal1.date_of_birth)

    def test_animal_current_vet(self):
        self.assertEqual(None, self.animal1.current_vet)

    def test_animal_type(self):
        self.assertEqual("cat", self.animal1.type)

    def test_animal_owner_number(self):
        self.assertEqual(555679, self.animal1._owner_number)

    def test_animal_treatment_notes(self):
        self.assertEqual("Too heavy, must diet to lose 2KG.", self.animal1.treatment_notes)

