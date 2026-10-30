<img width="1100" height="213" alt="image" src="https://github.com/user-attachments/assets/519a6593-418c-4421-8dcc-73189dde3955" />

# CS3-Repository
Code Repository for **CS3** Activities
## Welcome
Hello! I am Beatrice D. Salvador from 9-Pinatubo.

## Quarter 1
### (FA 1) SG 2: Activity 1 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg2_a1.md)

### SG 2: Activity 2 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg2_a2.md)

### (FA 2) SG 2: Activity 3 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg2_a3.py)

### (FA 5) SG 5: Activity 1 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg5_a1_pinatubo_salvador.py)

### (FA 6) SG 6: Challenge 1 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg6_pinatubo_salvador.py)

### (FA 7) SG 7: Code the Lab Inventory Hierarchy - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg7_pinatubo_salvador.py)

## Quarter 2
### (FA 1) SG 8 & 9: Encapsulation and Inheritance - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q2/fa1_pinatubo_salvador.py)
### (FA 2) SG 10: Method Overriding - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q2/fa2_pinatubo_salvador.py)

## Sample Codes: 
### Quarter 1
```
class Car:
    def __init__(self,brand,model,battery=35):
        self.brand = brand
        self.model = model
        self.battery = battery
        print("You've created a",self.brand,self.model)
    def go(self, distance):
        self.battery -=distance/20
        print("You've travelled", distance,"KM")
        print("You have", self.battery, "wH left")
    def charge(self, wH):
        self.battery += wH
        print("You charged", wH, "wH")
car = Car("Geely", "EX5")
while car.battery > 0:
    act = input("What do you want to do? (g or c) ")
    if act == "g":
        distance = int(input("How far? "))
        car.go(distance)
    elif act == "c":
        wH = int(input("How much to charge? "))
        car.charge(wH)
    else:
        print("Invalid action.")
print("Game over. YOu ran out of batteries.")
```
```
# INFLUENCE
class Vehicle:
    def __init__(self,kindofvehicle):
        self.kindofvehicle = kindofvehicle
        print(self.kindofvehicle,"created")
    def move(self,distance):
        print(self.kindofvehicle,"moved",distance,end="")

class Car(Vehicle):
    def __init__(self,kindofvehicle,brand,model):
        self.brand = brand; self.model = model
        super().__init__(kindofvehicle)
        print("It is a",brand,model)
    def move(sef,distance):
        super().move(distance)
        print("KM")

class Boat(Vehicle):
    def __init__(self,kindofvehicle,model):
        self.model = model
        super().__init__(kindofvehicle)
        print("It is a",self.model)
    def move(self,distance):
        super().move(distance)
        print("Nm")

class Plane(Vehicle):
    def __init__(self,kindofvehicle,model):
        self.model = model
        super().__init__(kindofvehicle)
        print("It is a",self.model)
    def move(self,distance):
        super().move(distance)
        print("Nm")
    

vios = Car("car","Toyota","Vios")
vios.move(10)
ferry = Boat("ferry","SuperFerry")
ferry.move(20)
yacht = Boat("yacht","Subic Yacht")
yacht.move(25)
airplane = Plane("airplane","Philippine Airlines")
airplane.move(50)


# COMPOSITION
class Nucleus:
    def __init__(self):
        print("Nucleus created")
    def __del__(self):
        print("Nucleus is gone")

class Mitochondria:
    def __init__(self):
        print("Mitochondria created")
    def powerTheCell(self):
        print("Mitochondria is providing energy")
    def __del__(self):
        print("Mitochondria is gone")

class Cell:
    def __init__(self):
        print("Cell created")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()
    def exist(self):
        print("Cell is existing")
        self.mitochondria.powerTheCell()
    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell is gone")

cellAtWork = Cell()
cellAtWork.exist()
del cellAtWork


# AGGREGATION
class Sauce:
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste
        print(self.name,"is cooked")
    def __del__(self):
        print(self.name,"is goners")
    def __str__(self):
        return "This is "+self.name+" and it tastes "+self.taste
class Tusoktusok:
    def __init__(self,name,sauce):
        self.name = name
        self.sauce = sauce
        print(self.name,"is cooked and dipped in",self.sauce.name)
    def eat(self):
        print("I am eating",self.name,"and it tastes",self.sauce.taste)
    def __del__(self):
        print(self.name,"was thrown away")

vinegar = Sauce("vinegar","sour")
fishball = Tusoktusok("fishball",vinegar)
fishball.eat()
del fishball
print(vinegar)
```
### Quarter 2
```
#ENCAPSULATION    
class Student:
    __name: str
    __age = 0
    def __init__(self, name):
        self.__name = name
    def set_age(self,age):
        if age > 0:
            self.__age = age
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def greet(self):
        return f"Hi! My name is {self.__name}"
    def set_name(self,name):
        self.__name = name

student1 = Student("Josef")
student1.set_age(-16)
student1.set_name("JM")
print("Student name: ", student1.get_name())
print("Student age: ", student1.get_age())

student1.set_age(16)
print("Student age: ", student1.get_age())
print(student1.greet())
```
```
#INHERITANCE
class Father:
    eyes = "blue eyes"

class Mother:
    hair = "black hair"

class You(Father, Mother):
    def describeYourself(self):
        print("I have", self.eyes, "and", self.hair)

you = You()
you.describeYourself()
```
```
#POLYMORPHISM
class Bill:
    amount = 0
    def __init__(self, amount):
        self.amount = amount
    def pay(self, payment):
        self.amount -= payment.amount
        print("Payment made using", payment.mode)
        print("Balance: ", self.amount)

class Payment:
    amount = 0
    mode = "Cash"
    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    def __init__(self, name, amount):
        self.mode = name
        self.amount = amount

bigBeautifulBill = Bill(100)
bayad = Payment(67)
bigBeautifulBill.pay(bayad)

gcash = Ewallet("PisayCash", 33)
bigBeautifulBill.pay(gcash)
```
```
#POLYMORPHISM
class Patient:
    patient_type = "Regular Patient"
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
        print(f"\nPatient Name: {self.name}\nPatient Type: {self.patient_type}\nOriginal Bill: ₱{self.bill_amount: .2f} \nFinal Bill: ₱{self.bill_amount: .2f}")

    def display_patient_type(self):
        return patient_type

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount = 0.00, s_discount = 0.20, patient_type = "Regular Patient"):
        super().__init__(name, bill_amount)
        self.patient_type = "Senior Patient"
        self.s_discount = s_discount

    def calculate_bill(self):
        super().calculate_bill()
        discount_amt = self.bill_amount*self.s_discount
        print(f"\nPatient Name: {self.name}\nPatient Type: {self.patient_type}\nOriginal Bill: ₱{self.bill_amount: .2f} \nFinal Bill: ₱{(self.bill_amount - discount_amt): .2f}")

    def display_patient_type(self):
        super().display_patient_type()
        self.patient_type = "Senior Patient"
    
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount = 0.00, p_discount = 0.15, patient_type = "Regular Patient"):
        super().__init__(name, bill_amount)
        self.p_discount = p_discount
        self.patient_type = "PhilHealth Member"

    def calculate_bill(self):
        super().calculate_bill()
        discount_amt = self.bill_amount*self.p_discount
        print(f"\nPatient Name: {self.name}\nPatient Type: {self.patient_type}\nOriginal Bill: ₱{self.bill_amount: .2f} \nFinal Bill: ₱{(self.bill_amount - discount_amt): .2f}")

    def display_patient_type(self):
        super().display_patient_type()
        self.patient_type = "PhilHealth Member"
        
regular_patient = Patient("Juan Dela Cruz", 15000)
patient_2 = SeniorPatient("Maria Santos", 15000)
patient_3 = PhilHealthPatient("Pedro Reyes", 15000)

print(f"Hospital Billing System\n-----------------------")
regular_patient.calculate_bill()
patient_2.calculate_bill()
patient_3.calculate_bill()
```
```class Vehicle:
    color = "Gray"
    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers

    def move(self):
        print("Vehicle", self.color, self.name, "is moving")
        print("It has", self.passengers, "passengers")

class Car(Vehicle):
    def move(self):
        print("The car", self.color, self.name, "is travelling along the road")
        print("It has", self.passengers, "passengers")

class Boat(Vehicle):
    def move(self):
        print("The boat", self.color, self.name, "is sailing along the water")
        print("It has", self.passengers, "passengers")

class Skateboard:
    def move(self):
        print(f"The skateboard is moving")
    
car1 = Car("Toyota Altis", 5)
car1.color = "Red"
car2 = Car("BYD Sealion 5", 5)
car2.color = "Blue"
boat = Boat("Yacht", 10)
boat.color = "White"
skbd = Skateboard()

vehicles = [car1, car2, boat, skbd]
for v in vehicles:
    v.move()
```
