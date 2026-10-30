class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")
      
class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")
class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")
      
warrior = Warrior()
mage = Mage()
archer = Archer()
roles = [warrior, mage, archer]
for r in roles:
    r.special_move()

