DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    working_days VARCHAR(255),
    date_of_birth VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    animal_type VARCHAR(255),
    owner_number INT,
    treatment_notes VARCHAR(255),
    current_vet_id SERIAL REFERENCES vets(id)
);