class Clinic:
    max_patients = 3

    def __init__(self, name):
        self.name = name
        self.patients = []
        self.waiting_list = []
    
    def add_patient(self, patient):
        if len(self.patients) >= Clinic.max_patients:
            self.waiting_list.append(patient)
        else:
            self.patients.append(patient)

my_clinic = Clinic('theme park')
my_clinic.add_patient('Danny')
print(my_clinic.name)
print(my_clinic.patients)
print(my_clinic.waiting_list)