
class user:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp


    def display_info(self):
       return f"sword: {self.name}, power: {self.power}, hp: {self.hp}"   
    
samus = user("Samus",37,108)
bowser = user("bowser",32,135)
link = user("link",29,104)

print(link.display_info())