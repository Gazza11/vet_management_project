import unittest
from models.animal import Animal 
from models.vet import Vet

class TestAnimal(unittest.TestCase):

    def setUp(self):

        self.vet1 = Vet("Troy", "Barker", "Mon, Tues, Weds, Fri", "06/09/1991")
        self.vet2 = Vet("Karl", "Malone", "Mon, Tues, Weds, Thurs, Fri, Sat", "24/07/1963")
        self.animal1 = Animal("Garfield", "12/06/2018", "cat", 555679, "Garfield needs to lose 2KG", self.vet1)
        self.animal2 = Animal("George", "11/02/2011", "monkey", 456722, "George is a curious boy.", self.vet2)


    def test_animal_name(self):
        self.assertEqual("Garfield", self.animal1.name)

    def test_animal_date_of_birth(self):
        self.assertEqual("12/06/2018", self.animal1.date_of_birth)

    def test_animal_type(self):
        self.assertEqual("cat", self.animal1.animal_type)

    def test_animal_owner_number(self):
        self.assertEqual(555679, self.animal1.owner_number)

    def test_animal_adding_notes__empty(self):
        self.assertEqual("George is a curious boy.", self.animal2.treatment_notes)

    def test_animal_adding_notes__add_multiple_notes(self):
        self.animal1.add_treatment_notes("Garfield now needs to lose 4KG.")
        self.assertEqual("Garfield now needs to lose 4KG.", self.animal1.treatment_notes[1])

    def test_animal_adding_notes__add_multiple_notes_check_other_animal(self):
        self.animal1.add_treatment_notes("Garfield now needs to lose 4KG.")
        self.assertEqual("Garfield needs to lose 2KG", self.animal1.treatment_notes[0])
        self.assertEqual("Garfield now needs to lose 4KG.", self.animal1.treatment_notes[1])
        self.assertEqual("George is a curious boy.", self.animal2.treatment_notes)

    def test_animal_assign_to_vet__first_name_check(self):
        self.animal1.assign_vet(self.vet1)
        self.assertEqual("Troy", self.animal1.current_vet.first_name)

    def test_animal_assign_to_vet__working_days_check(self):
        self.animal1.assign_vet(self.vet1)
        self.assertEqual("Mon, Tues, Weds, Fri", self.animal1.current_vet.working_days)

    def test_animal_assign_to_vet__replace_with_new_vet(self):
        self.animal1.assign_vet(self.vet1)
        self.animal1.assign_vet(self.vet2)
        self.assertEqual("Karl", self.animal1.current_vet.first_name)

    def test_animal_assign_to_vet__multiple_assignings(self):
        self.animal1.assign_vet(self.vet1)
        self.animal2.assign_vet(self.vet2)
        self.assertEqual("Troy", self.animal1.current_vet.first_name)
        self.assertEqual("Karl", self.animal2.current_vet.first_name)
