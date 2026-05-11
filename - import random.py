
class user:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp
class shooter(user):
    def __init__(self, name, power, hp):
      super().__init__(name, power, hp)
        

class tank(user):
    def __init__(self, name, power, hp):
      super().__init__(name, power, hp)
     
class sword(user):
    def __init__(self, name, power, hp):
      super().__init__(name, power, hp)       

    def display_info(self):
       return f"sword: {self.name}, power: {self.power}, hp: {self.hp}"   
    
samus = shooter("Samus",150,50)
bowser = tank("bowser",50,150)
link = sword("link","100",100)

print(sword.display_info())