class Animal:
    def __init__(self, name, date_of_birth, animal_type, owner_details, treatment_notes, current_vet, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.owner_details = owner_details
        self.treatment_notes = treatment_notes
        self.current_vet = current_vet
        self.id = id


# Function adds treatment notes to the animal profile
    def add_treatment_notes(self, notes):
        new_list = []
        new_list.append(self.treatment_notes)
        new_list.append(notes)
        self.treatment_notes = new_list


# Function assigns a vet to the animal profile. Will override last.
    def assign_vet(self, vet):
        self.current_vet = vet