from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.vet import Vet
from models.owner import Owner

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

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
    owners = owner_repository.select_all()
    return render_template("animals/new.html", vets = vets, owners=owners)


# Saving new animal record
@animals_blueprint.route("/animals", methods=['POST'])
def create_animal_record():
    name = request.form["name"]
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    owner_id = request.form['owner_details']
    owner = owner_repository.select_by_id(owner_id)
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['current_vet_id']
    current_vet = vet_repository.select_by_id(vet_id)
    new_animal = Animal(name, date_of_birth, animal_type, owner, treatment_notes, current_vet)
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
    owners = owner_repository.select_all()
    return render_template('animals/edit.html', animal=animal, vets=vets, owners=owners)


# Update animal record
@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form["name"]
    date_of_birth = request.form['date_of_birth']
    animal_type = request.form['animal_type']
    owner_id = request.form['owner_details']
    owner = owner_repository.select_by_id(owner_id)
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['current_vet_id']
    current_vet = vet_repository.select_by_id(vet_id)
    animal = Animal(name, date_of_birth, animal_type, owner, treatment_notes, current_vet, id)
    animal_repository.update(animal)
    return redirect("/animals")

@animals_blueprint.route("/search")
def search_index():
    animals = animal_repository.select_all_animals()
    return render_template("search/index.html", animals=animals)

@animals_blueprint.route("/search/name")
def search_form():
    animals = animal_repository.select_all_animals()
    return render_template("search/name.html", animals=animals)

# Search by name form
@animals_blueprint.route("/search/name", methods=['POST'])
def search_by_name():
    name = request.form["name"]
    return redirect(f"/search/name/{name}")

# Search by animal name - result
@animals_blueprint.route("/search/name/<name>")
def search_by_name_result(name):
    animals = animal_repository.select_by_name(name)
    return render_template("search/results.html", animals = animals)



@animals_blueprint.route("/search/type")
def search_form_type():
    animals = animal_repository.select_all_animals()
    return render_template("search/type.html", animals = animals)

@animals_blueprint.route("/search/type", methods=['POST'])
def search_by_type():
    search_type = request.form["search_type"]
    return redirect(f"/search/type/{search_type}")

@animals_blueprint.route("/search/type/<search_type>")
def search_by_type_results(search_type):
    animals = animal_repository.select_by_type(search_type)
    return render_template("search/results.html", animals=animals)


@animals_blueprint.route("/search/vet")
def search_form_vet():
    animals = animal_repository.select_all_animals()
    vets = vet_repository.select_all_vets()
    return render_template("search/vet.html", animals = animals, vets=vets)

@animals_blueprint.route("/search/vet", methods=['POST'])
def search_by_vet():
    vet = request.form["vet"]
    return redirect(f"/search/vet/{vet}")

@animals_blueprint.route("/search/vet/<vet>")
def search_by_vet_results(vet):
    animals = animal_repository.select_by_vet(vet)
    return render_template("search/results.html", animals = animals)