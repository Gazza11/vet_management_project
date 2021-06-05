class Animal:
    def __init__(self, name, date_of_birth, animal_type, owner_number, current_vet = None, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.owner_number = owner_number
        self.treatment_notes = []
        self.current_vet = current_vet
        self.id = id


# Function adds treatment notes to the animal profile
    def add_treatment_notes(self, notes):
        self.treatment_notes.append(notes)


# Function assigns a vet to the animal profile. Will override last.
    def assign_vet(self, vet):
        self.current_vet = vet