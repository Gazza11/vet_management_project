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
    treatment_notes TEXT,
    current_vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

-- Below used for testing.
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Troy', 'Barker', 'Mon, Tues', '07/09/1998');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Abed', 'Tanner', 'Mon, Weds', '07/09/1978');


INSERT INTO animals (name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet_id) VALUES ('Garfield', '07/08/2019', 'cat', 589668, 'Garfield needs to lose weight.', 1);
INSERT INTO animals (name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet_id) VALUES ('George', '14/07/2020', 'monkey', 789422, 'George is very Curious.', 1);
INSERT INTO animals (name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet_id) VALUES ('Gregor', '02/03/2008', 'dog', 889026, 'Gregor needs a course of anti-biotics.', 2);
INSERT INTO animals (name, date_of_birth, animal_type, owner_number, treatment_notes, current_vet_id) VALUES ('Emily', '23/09/2009', 'cat', 778009, 'In good health.', 1);


SELECT * FROM vets;
SELECT * FROM animals;