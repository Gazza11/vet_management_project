from flask import Flask, render_template, request, redirect, Blueprint

from models.owner import Owner

import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)


@owners_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select_by_id(id)
    return render_template("owners/show.html", owner = owner)


@owners_blueprint.route('/owners/new')
def new_owner():
    return render_template("owners/new.html")


@owners_blueprint.route("/owners", methods=['POST'])
def create_owner():
    name = request.form['name']
    number = request.form['number']
    address = request.form['address']
    postcode = request.form['postcode']
    registered = True
    new_owner = Owner(name, number, address, postcode, registered)
    owner_repository.save_owner(new_owner)
    return redirect("/owners")