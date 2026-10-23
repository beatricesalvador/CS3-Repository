class Patient:
    def __init__(self, name, bill_amount = 0.00):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self, bill_amount):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        print(f"\nPatient Name: {self.name}\nOriginal Bill: ₱{self.bill_amount: .2f} \nFinal Bill: ₱{self.bill_amount: .2f}")


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount = 0.00, s_discount = 0.20):
        super().__init__(name, bill_amount)
        self.s_discount = s_discount

    def calculate_bill(self):
        super().calculate_bill()
        discount_amt = self.bill_amount*self.s_discount
        print(f"\nPatient Name: {self.name}\nOriginal Bill: ₱{self.bill_amount: .2f} \nFinal Bill: ₱{(self.bill_amount - discount_amt): .2f}")

    
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount = 0.00, p_discount = 0.15):
        super().__init__(name, bill_amount)
        self.p_discount = p_discount

    def calculate_bill(self):
        super().calculate_bill()
        discount_amt = self.bill_amount*self.p_discount
        print(f"\nPatient Name: {self.name}\nOriginal Bill: ₱{self.bill_amount: .2f} \nFinal Bill: ₱{(self.bill_amount - discount_amt): .2f}")

regular_patient = Patient("Juan Dela Cruz", 15000)
patient_2 = SeniorPatient("Maria Santos", 15000)
patient_3 = PhilHealthPatient("Pedro Reyes", 15000)

print(f"Hospital Billing System\n-----------------------")
regular_patient.calculate_bill()
patient_2.calculate_bill()
patient_3.calculate_bill()


