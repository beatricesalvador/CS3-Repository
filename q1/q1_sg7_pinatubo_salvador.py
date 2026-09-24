class Glassware:
    def __init__(self,glassware_type):
        self.glassware_type = glassware_type
        print(f"You created a {self.glassware_type}.")

class Beaker(Glassware):
    def __init__(self,material,glassware_type):
        super().__init__(glassware_type)
        self.material = material
        print(f"The {self.glassware_type} is primarily made of {self.material}.")

class Tray:
    def __init__(self, beaker_material):
        self.beakers = [Beaker("Beaker", beaker_material) for _ in range(5)]
        print(f"Tray has been created and filled with {len(self.beakers)} beakers.")
        
    def del_tray(self):
        print("The tray has been deleted. All beakers are now lost to the system.")

my_tray = Tray("borosilicate glass")
del my_tray
