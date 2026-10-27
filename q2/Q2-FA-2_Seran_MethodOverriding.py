
class Patient:

    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = 0
        self.set_bill_amount(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.strip() != "":
            self.__name = name
        else:
            print("Name cannot be empty.")

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            print("Bill amount cannot be negative.")

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):

    def calculate_bill(self):
        discount = self.get_bill_amount() * 0.20
        return self.get_bill_amount() - discount

class PhilHealthPatient(Patient):

    def calculate_bill(self):
        discount = self.get_bill_amount() * 0.15
        return self.get_bill_amount() - discount

regular_patient = Patient("Aiah Arceta", 15000)
senior_patient = SeniorPatient("Mr. Lead", 15000)
philhealth_patient = PhilHealthPatient("Mikha Lim", 15000)


print("HOSPITAL BILLING SYSTEM")


print("\nRegular Patient")
print("Name:", regular_patient.get_name())
print("Original Bill: PHP", format(regular_patient.get_bill_amount(), ",.2f"))
print("Final Bill: PHP", format(regular_patient.calculate_bill(), ",.2f"))

print("\nSenior Patient")
print("Name:", senior_patient.get_name())
print("Original Bill: PHP", format(senior_patient.get_bill_amount(), ",.2f"))
print("Final Bill: PHP", format(senior_patient.calculate_bill(), ",.2f"))

print("\nPhilHealth Patient")
print("Name:", philhealth_patient.get_name())
print("Original Bill: PHP", format(philhealth_patient.get_bill_amount(), ",.2f"))
print("Final Bill: PHP", format(philhealth_patient.calculate_bill(), ",.2f"))