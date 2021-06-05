import pdb
from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

animal_repository.delete_all()
vet_repository.delete_all()


vet1 = Vet('Troy', 'Barker', "Mon, Tues", "06/07/1987")
vet_repository.save_vet(vet1)
vet2 = Vet('Britta', 'Perry', 'Fri, Sat, Sun', '01/03/1992')
vet_repository.save_vet(vet2)

animal1 = Animal('Garfield', "09/09/2009", "cat", 567, vet1)
animal_repository.save_animal(animal1)
animal2 = Animal("George", "05/05/2017", "monkey", 9987, vet2)
animal_repository.save_animal(animal2)
animal1.assign_vet(vet2)
animal1.add_treatment_notes("George is a curious boy.")
animal1.add_treatment_notes("Still curious!!")
animal_repository.update(animal1)

# print(vet_repository.select_by_id(23))

# print(animal_repository.select_by_id(45).treatment_notes)

# for animal in animal_repository.select_all_animals():
#     print(animal.__dict__)


pdb.set_trace()