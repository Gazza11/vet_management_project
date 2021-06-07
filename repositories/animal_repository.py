from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet
from models.owner import Owner

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

# Create animal profile
def save_animal(animal):
    sql = "INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.animal_type, animal.owner_details.id, animal.treatment_notes, animal.current_vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


# Select all animal profiles
def select_all_animals():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select_by_id(row['current_vet_id'])
        owner = owner_repository.select_by_id(row['owner_details'])
        animal = Animal(row['name'], row['date_of_birth'], row['animal_type'], owner, row['treatment_notes'], vet, row['id'])
        animals.append(animal)
    return animals


# Select animal profile by id
def select_by_id(id):
    animal = None

    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        vet = vet_repository.select_by_id(results['current_vet_id'])
        owner = owner_repository.select_by_id(results['owner_details'])
        animal = Animal(results['name'], results['date_of_birth'], results['animal_type'], owner, results['treatment_notes'], vet, results['id'])
    return animal


# Delete all animal profiles
def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)


# Delete animal profile by id
def delete_by_id(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Update animal profile
def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.animal_type, animal.owner_number, animal.treatment_notes, animal.current_vet.id, animal.id]
    run_sql(sql, values)
