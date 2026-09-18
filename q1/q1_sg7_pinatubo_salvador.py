class Glassware:
    def __init__(self, type):
        self.type = type
        print(self.type, "created.")
    
class Beaker(Glassware):
    def __init__(self, type, material):
        self.material = material
        super().__init__(type)
        print(f'The {self.type} is primarily made of {self.material}.')
class Tray:
    def __init__(self, glassware):
        self. glassware = glassware
        self.glassware = []
        print("Tray has been created.")
    def add_glassware(self, glassware):
        if len(self.glassware) <= 5:
            glasswares = int(input("How much glasswares would you like to add to your tray? "))
            self.glassware.append(glasswares)
            if len(self.glassware) <= 5:
                print(f'The tray is holding {glasswares} glassware(s).')
            elif len(self.glassare) > 5:
                print(f'{glasswares} glasswares is too much for the Tray.')
                def __del__(self, glassware):
                    print(f'{self.glassware} is now lost in the system.')
            else:
                print("Invalid Input. Type an integer.")

        
            
philips = Beaker("Philips Beaker", "borosilicate glass")
testTube = Glassware("Test Tube")
testTube = Tray("Test Tube")
testTube.add_glassware("Test Tube")


