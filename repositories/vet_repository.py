from db.run_sql import run_sql

from models.vet import Vet

def save_vet(vet):
    sql = "INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.working_days, vet.date_of_birth]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)