
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
# # # if opponent's health is less than 0 print(victory)

# # print(link.display_info())

# # if 
# import random
# import json
# characters = open("./characters.json")
# data = json.load(characters)
# lives = 3
# npc_lives = 3

# player = (input("which player")).capitalize()
# print(data[player]['moves'])

# player_health = (data[player]['hp'])
# npc = (input("which npc")).capitalize()
# npc_health = (data[npc]['hp'])
# print(player_health)



# while lives > 0 and npc_lives > 0:
#     attack = input('what attack')
#     damage = (data[player]['moves'][attack])
#     npc_health -= damage
#     npc_attack = random.choice(list(data[npc]['moves'].keys()))
#     print(npc_attack)
#     npc_damage = data[npc]['moves'][npc_attack]
#     player_health -= npc_damage
#     print(npc_health)("npc_health")
#     print(player_health)("player health")
#     if player_health < 0:
#         lives -= 1
#         player_health = data[player]['hp']
# if lives == 0:
#     print("game over")

#     if npc_health <0:
#         npc_lives-=1
#         npc_health = data[npc]['hp']
# if npc_lives == 0:
#     print("victory")

# import random
# import json
# characters = open("./characters.json")
# data = json.load(characters)

# player = (input("which player")).capitalize()

# print(data[player]['moves'])

# player_health = (data[player]['hp'])
# npc = (input("which npc")).capitalize()
# npc_health = (data[npc]['hp'])
# print(player_health)
# print("player health")



# while lives > 0 and npc_lives > 0:
#     if player_health < 0 or player_health == 0:
#         attack = input('What attack? ')
#         damage = (data[player]['moves'][attack])
#         npc_health -= damage


# import json
# characters = open("./characters.json")
# data = json.load(characters)

# player = (input("which player")).capitalize()
# <<<<<<< Updated upstream
# player = (input("which player")).capitalize()
# =======
# player = (input("which player")).capitalize()
# print(data[player]['moves'])

# player_health = (data[player]['hp'])
# npc = (input("which npc")).capitalize()
# npc_health = (data[npc]['hp'])
# print(player_health)
# print("player health")



# while lives > 0 and npc_lives > 0:
#     if player_health < 0 or player_health == 0:
#         attack = input('What attack? ')
#         damage = (data[player]['moves'][attack])
#         npc_health -= damage
import random
import json
characters = open("./characters.json")
data = json.load(characters)
lives = 3
npc_lives = 3

player = (input("which player")).capitalize()
print(data[player]['moves'])

player_health = (data[player]['hp'])
npc = (input("which npc")).capitalize()
npc_health = (data[npc]['hp'])
print(player_health)
print("player health")



while lives > 0 and npc_lives > 0:
        
        attack = input('What attack? ')
        damage = (data[player]['moves'][attack])
        npc_health -= damage
        npc_attack = random.choice(list(data[npc]['moves'].keys()))
        print(npc_attack)
   
        npc_damage = data[npc]['moves'][npc_attack]
        player_health -= npc_damage
        print("NPC Health:") 
        print(npc_health)
        
        print("npc: It's my turn now!!")
        print(npc_attack)
        print("Player Health:")
        print(player_health)
        
        print("Npc: Take that!")
        if player_health < 0:
            player_health == (data[player]['hp'])
            lives -= 1
            
        if lives == 0:
            print("game over")

        if npc_health < 0:
            npc_lives-=1
            npc_health == (data[player]['hp'])
        if npc_lives == 0:
            print("victory")