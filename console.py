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


for vet in vet_repository.select_all_vets():
    print(vet.__dict__)





pdb.set_trace()