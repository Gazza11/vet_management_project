import pdb
from models.vet import Vet
from models.animal import Animal
from models.owner import Owner

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

# animal_repository.delete_all()
# vet_repository.delete_all()
# owner_repository.delete_all()


vet1 = Vet('Troy', 'Barker', "Mon, Tues", "06/07/1987")
vet_repository.save_vet(vet1)
# vet2 = Vet('Britta', 'Perry', 'Fri, Sat, Sun', '01/03/1992')
# vet_repository.save_vet(vet2)
# vet2 = Vet('Britta', 'Tanner', 'Fri, Sat, Sun', '01/03/1992')
# vet_repository.update(vet2)

owner1 = Owner("Liam Morrice", 998234, "13 Thistle Drive", "AB34 6WB", True)
owner_repository.save_owner(owner1)
# owner2 = Owner("Mike Trout", 998234, "27 Thistle Drive", "AB34 6WB", True)
# owner_repository.save_owner(owner2)

# owner1.name = "Liam Anderson"
# owner_repository.update(owner1)
# print(owner_repository.select_by_id(7).number)

# for owner in owner_repository.select_all():
#     print(owner.__dict__)

animal1 = Animal('Garfield', "09/09/2009", "cat", owner1, "Note 1", vet1)
animal_repository.save_animal(animal1)
# animal2 = Animal("George", "05/05/2017", "monkey", owner1, "Note2", vet2)
# animal_repository.save_animal(animal2)


# animal1.assign_vet(vet2)
# animal1.add_treatment_notes("George is a curious boy.")
# animal1.add_treatment_notes("Still curious!!")
# animal_repository.update(animal1)

# for vet in vet_repository.select_all_vets():
#     print(vet.__dict__)

# for animal in animal_repository.select_all_animals():
#     print(animal.__dict__)

# animal1 = animal_repository.search_name("Garfield")

# print(animal1.__dict__)
# animal1 = animal_repository.select_by_name("Garfield")
for animal in animal_repository.select_by_vet(2):
    print(animal.__dict__)


# for searched_animal in animal_repository.search_name("Garfield"):
#     print(searched_animal.__dict__)





pdb.set_trace()