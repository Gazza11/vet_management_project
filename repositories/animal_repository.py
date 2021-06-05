from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet

import repositories.vet_repository as vet_repository

def save_animal(animal):
    sql = "INSERT INTO animals (name, date_of_birth, animal_type, owner_number, current_vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.animal_type, animal.owner_number, animal.current_vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal




def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)