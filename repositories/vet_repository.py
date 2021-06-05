from db.run_sql import run_sql

from models.vet import Vet


# Create vet profile
def save_vet(vet):
    sql = "INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.working_days, vet.date_of_birth]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


# Select single vet by id
def select_by_id(id):
    vet = None
    
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        vet = Vet(results['first_name'], results['last_name'], results['working_days'], results['date_of_birth'], results['id'])
    
    return vet


# Select all vets
def select_all_vets():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['working_days'], row['date_of_birth'], row['id'])
        vets.append(vet)
    return vets


# Delete all vets
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)


# Delete a vet by id
def delete_by_id(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values) 


# Update vet profile
def update(vet):
    sql = "UPDATE vets SET (first_name, last_name, working_days, date_of_birth) = (%s, %s, %s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.working_days, vet.date_of_birth]
    run_sql(sql, values)
