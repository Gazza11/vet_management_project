import pdb
from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository

vet1 = Vet('Troy', 'Barker', "Mon, Tues", "06/07/1987")
vet_repository.save_vet(vet1)




pdb.set_trace()