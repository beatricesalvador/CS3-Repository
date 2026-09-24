<img width="1100" height="213" alt="image" src="https://github.com/user-attachments/assets/519a6593-418c-4421-8dcc-73189dde3955" />

# CS3-Repository
Code Repository for **CS3** Activities
## Welcome
Hello! I am Beatrice D. Salvador from 9-Pinatubo.

### (FA 1) SG 2: Activity 1 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg2_a1.md)

### SG 2: Activity 2 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg2_a2.md)

### (FA 2) SG 2: Activity 3 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg2_a3.py)

### (FA 5) SG 5: Activity 1 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg5_a1_pinatubo_salvador.py)

### (FA 6) SG 6: Challenge 1 - [Click Here to Read](https://github.com/beatricesalvador/CS3-Repository/blob/main/q1/q1_sg6_pinatubo_salvador.py)

## Sample Codes: 
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
