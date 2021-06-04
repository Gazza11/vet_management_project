import unittest
from models.animal import Animal 
from models.vet import Vet

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal1 = Animal("Garfield", "12/06/2018", "cat", 555679,)
        self.animal2 = Animal("George", "11/02/2011", "monkey", 456722)

        self.vet1 = Vet("Troy", "Barker", "Mon, Tues, Weds, Fri", "06/09/1991")

    def test_animal_name(self):
        self.assertEqual("Garfield", self.animal1.name)

    def test_animal_date_of_birth(self):
        self.assertEqual("12/06/2018", self.animal1.date_of_birth)

    def test_animal_current_vet(self):
        self.assertEqual(None, self.animal1.current_vet)

    def test_animal_type(self):
        self.assertEqual("cat", self.animal1.animal_type)

    def test_animal_owner_number(self):
        self.assertEqual(555679, self.animal1.owner_number)

    def test_animal_treatment_notes__no_notes(self):
        self.assertEqual([], self.animal2.treatment_notes)

    def test_animal_adding_notes__already_notes(self):
        self.animal1.add_treatment_notes("Garfield now needs to lose 4KG.")
        self.assertEqual("Garfield now needs to lose 4KG.", self.animal1.treatment_notes[0])

    def test_animal_adding_notes__empty(self):
        self.animal2.add_treatment_notes("George is a curious boy.")
        self.assertEqual("George is a curious boy.", self.animal2.treatment_notes[0])

    def test_animal_adding_notes__add_multiple_notes(self):
        self.animal1.add_treatment_notes("Garfield needs to lose 2KG")
        self.animal1.add_treatment_notes("Garfield now needs to lose 4KG.")
        self.assertEqual("Garfield needs to lose 2KG", self.animal1.treatment_notes[0])
        self.assertEqual("Garfield now needs to lose 4KG.", self.animal1.treatment_notes[1])
