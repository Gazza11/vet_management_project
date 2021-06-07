from db.run_sql import run_sql

from models.owner import Owner

# Create Owner
def save_owner(owner):
    sql = "INSERT INTO owners (name, number, address, postcode, registered) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [owner.name, owner.number, owner.address, owner.postcode, owner.registered]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

# Select all owners
def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['name'], row['number'], row['address'], row['postcode'], row['registered'], row['id'])
        owners.append(owner)
    return owners


# Select owner by id
def select_by_id(id):
    owner = None

    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        owner = Owner(results['name'], results['number'], results['address'], results['postcode'], results['registered'], results['id'])

    return owner

# Delete all owners
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

# Delete by id
def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (name, number, address, postcode, registered) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.number, owner.address, owner.postcode, owner.registered, owner.id]
    run_sql(sql, values)