
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
import random
import json
characters = open("./characters.json")
data = json.load(characters)
lives = 3
npc_lives = 3
player = (input("which player")).capitalize()
print(data(player)['moves'])

player_health = (data(player)['hp'])
npc = (input("which npc")).capitalize()
npc_health = (data(npc)['hp'])
print(player_health)



while lives != 0:
    attack = input('what attack')
damage = (data(attack)['moves'])
npc_health -= damage
npc_attack = random.choice(data('move'))
print(npc_health)

for life in lives:
    if player_health < 0:
        lives -= 1
if lives == 0:
    print("game over")
for npc_life in npc_lives:
    if npc_health <0:
        npc_lives-=1
if npc_lives == 0:
    print("victory")