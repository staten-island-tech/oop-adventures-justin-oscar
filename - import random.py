
# class user:
#     def __init__(self, name, power, hp):
#         self.name = name
#         self.power = power
#         self.hp = hp


#     def display_info(self):
#        return f"sword: {self.name}, power: {self.power}, hp: {self.hp}"   
    


# # three lives for each  character
# # # select character
# select npc
# # if character's health is 0, print(game over)'
# # if opponent's health is less than 0 print(victory)

# print(link.display_info())

# if 

import json
characters = open("./characters.json")
data = json.load(characters)
lives = 3

player = (input("which player")).capitalize()
print(characters[player]['moves'])

player_health = (characters[player]['hp'])
npc = (input("which npc")).capitalize()
npc_health = (characters[npc]['hp'])
print(player_health)



while lives != 0:
    attack = input('what attack')
damage = (characters['moves'][attack])
npc_health -= damage
for life in lives:
    if "hp" < 0:
        lives -= 1
if lives == 0:
    print("game over")