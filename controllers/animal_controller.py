from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all_animals()
    return render_template("animals/index.html", animals = animals)


@animals_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select_by_id(id)
    return render_template("animals/show.html", animal = animal)

@animals_blueprint.route("/animals/new")
def new_animal():
    vets = vet_repository.select_all_vets()
    return render_template("animals/new.html", vets = vets)


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
