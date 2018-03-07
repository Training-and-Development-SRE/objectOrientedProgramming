class Patient(object):
    def __init__(self,id,name,allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = "none"

class Hospital(object):
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
    def admit(self,patient):
        if len(self.patients) >= self.capacity:
            print patient.name + " not admitted -- " + self.name + " Hospital full."
        else:
            if patient.bed == "none":
                self.patients.append(patient)
                patient.bed = self.patients.index(patient)
                print patient.name + " has been admitted to the " + self.name + " Hospital."
            else:
                print patient.name + " already admitted to the " + self.name + " Hospital."
    def discharge(self,patient):
        if patient.bed == "none":
            print patient.name + " has not been admitted to the " + self.name + " Hospital yet and cannot check out."
        else:
            self.patients.pop(patient.bed)
            patient.bed = "none"
            print patient.name + " checked out of the " + self.name + " Hospital."

# Tests:
# grey = Hospital("Grey's Anatomy", 2)
# john = Patient(0,"John","none")
# joe = Patient(1,"Joe","none")
# jay = Patient(2,"Jay","none")
# grey.admit(john)
# grey.admit(joe)
# grey.admit(jay)
# grey.discharge(jay)
# print joe.bed
# grey.discharge(joe)
# print joe.bed
# grey.admit(jay)
# print jay.bed