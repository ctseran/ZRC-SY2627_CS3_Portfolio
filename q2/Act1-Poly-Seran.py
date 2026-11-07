
class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


regular = Patient("Aiah Arceta", 15000)
senior = SeniorPatient("Mr. Lead", 15000)
philhealth = PhilhealthPatient("Mikha Lim", 15000)

patients = [regular, senior, philhealth]

print("Hospital Billing System")
print("-----------------------")

for patient in patients:
    print("Patient Name:", patient.name)
    patient.display_patient_type()
    print("Original Bill: ₱" + format(patient.bill_amount, ".2f"))
    print("Final Bill: ₱" + format(patient.calculate_bill(), ".2f"))
    print()