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
    current_vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

-- Below used for testing.
-- INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Troy', 'Barker', 'Mon, Tues', '07/09/1998');
-- INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Abed', 'Tanner', 'Mon, Weds', '07/09/1978');


-- INSERT INTO animals (name, date_of_birth, animal_type, owner_number) VALUES ('Garfield', '00', 'cat', 000);

-- SELECT * FROM vets;
-- SELECT * FROM animals;