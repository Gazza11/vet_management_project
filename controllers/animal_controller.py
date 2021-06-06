from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

# Show all animal records
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all_animals()
    return render_template("animals/index.html", animals = animals)


# Show specific animal record
@animals_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select_by_id(id)
    return render_template("animals/show.html", animal = animal)


# Form for new animal record
@animals_blueprint.route("/animals/new")
def new_animal():
    vets = vet_repository.select_all_vets()
    return render_template("animals/new.html", vets = vets)


# Saving new animal record
@animals_blueprint.route("/animals", methods=['POST'])
def create_animal_record():
    name = request.form["name"]
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    owner_number = request.form['owners_number']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['current_vet_id']
    current_vet = vet_repository.select_by_id(vet_id)
    new_animal = Animal(name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet)
    animal_repository.save_animal(new_animal)
    return redirect("/animals")


# Delete specific animal record
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete_by_id(id)
    return redirect("/animals")


# Edit animal record
@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repository.select_by_id(id)
    vets = vet_repository.select_all_vets()
    return render_template('animals/edit.html', animal=animal, vets=vets)


# Update animal record
@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form["name"]
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    owner_number = request.form['owners_number']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['current_vet_id']
    current_vet = vet_repository.select_by_id(vet_id)
    animal = Animal(name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet, id)
    animal_repository.update(animal)
    return redirect("/animals")

