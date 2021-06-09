DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    working_days VARCHAR(255),
    date_of_birth VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    number VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    animal_type VARCHAR(255),
    owner_details INT REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    current_vet_id INT REFERENCES vets(id)
);

--Below is used for populating the database for example purposes.
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Troy', 'Barker', 'Mon, Tues', '1998-07-09');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Abed', 'Tanner', 'Mon, Weds', '1978-08-11');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Britta', 'Perry', 'Weds, Thurs, Fri', '1987-11-11');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Anthony', 'Rendon', 'Mon, Weds', '1978-08-11');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Karl', 'Malone', 'Mon, Tues, Weds, Thurs, Fri, Sat', '1964-09-18');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('David', 'Fletcher', 'Tues, Weds, Thurs', '1997-08-11');
INSERT INTO vets (first_name, last_name, working_days, date_of_birth) VALUES ('Jasmine', 'Fuller', 'Mon, Weds, Fri, Sun', '1978-08-11');


INSERT INTO owners (name, number, address, postcode, registered) VALUES ('Liam Morrice', 998667, '13 Thistle Drive', 'AB43 6WB', true);
INSERT INTO owners (name, number, address, postcode, registered) VALUES ('Doug Fraser', 909667, '9 Pencil Road', 'AB83 6MB', true);
INSERT INTO owners (name, number, address, postcode, registered) VALUES ('Stu Christie', 998999, '78 Ember Drive', 'AB9 6WB', true);
INSERT INTO owners (name, number, address, postcode, registered) VALUES ('Mike Trout', 272727, '27 Thistle Drive', 'AB27 6WB', false);
INSERT INTO owners (name, number, address, postcode, registered) VALUES ('Farmer McGhee', 900432, 'The Farm Drive', 'EIE0 6WB', true);
INSERT INTO owners (name, number, address, postcode, registered) VALUES ('Marcus Semien', 232466, '6 Toronto Avenue', 'AB27 6MS', true);


INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Garfield', '2019-08-07', 'cat', 1, 'Garfield needs to lose weight.', 1);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('George', '2020-07-14', 'monkey', 2, 'George is very Curious.', 1);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Gregor', '2008-03-02', 'dog', 4, 'Gregor needs a course of anti-biotics.', 2);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Silvester', '2009-03-02', 'cat', 3, 'Obsessed with mice.', 4);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Emily', '2009-03-02', 'cat', 3, 'In good health.', 5);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Ol Yella', '1999-03-02', 'dog', 1, 'Does not look good', 1);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Woody', '2003-03-02', 'dog', 6, 'Chases his tail too much.', 2);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Buzz', '2003-12-02', 'dog', 6, 'Space Cadet.', 1);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Thumper', '2011-03-02', 'rabbit', 3, 'In good health.', 7);
INSERT INTO animals (name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet_id) VALUES ('Tiny', '2009-03-02', 'Guinea Pig', 5, 'Has a temper.', 6);


-- SELECT * FROM vets;
-- SELECT * FROM animals;
-- SELECT * FROM animals WHERE animal_type = 'cat';