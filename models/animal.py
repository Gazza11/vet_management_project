class Animal:
    def __init__(self, name, date_of_birth, animal_type, owner_number, current_vet = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.owner_number = owner_number
        self.treatment_notes = []
        self.current_vet = current_vet


    def add_treatment_notes(self, notes):
        self.treatment_notes.append(notes)