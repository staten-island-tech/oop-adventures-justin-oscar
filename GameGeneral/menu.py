class gamemode():
    def main_menu(self):
        print("1.) Smash")
        print("2.) Vault")

        
    def Smash_menu(self):
        print("1.) Smash")
        print("2.) Tourney")
        print("3.) Squad Strike")
        print("4.) Special Strike")
        print("5.) Back")
        
    def VaultMenu(self):
        print("1.) Sounds")
        print("2.) Replays")
        print("3.) Records")
        print("4.) Challenges")
        print("5.) Tips")
        print("6.) Movies")
        print("7.) Shop")
        print("8.) Back")
    def Smashsmashmenu(self):
        print("1.) Create Ruleset")
        print("2.) Use Existing Ruleset")
        print("3.) Back")
main = gamemode()
main.main_menu()
choice = int(input("Enter option 1-2: ")) 
    
a = 1
while a == 1:
    match choice:
        case 1:
            main.Smash_menu()
            choice1 = int(input("Enter option 1-5: "))
            a=2
        case 2:
            main.VaultMenu()
            choice2 = int(input("Enter option 1-8: ")) 
            a=3
        case _:
            print("Invalid option. Please try again.")
            a=1
            break
while a == 2:
    choice1 = int(input("Enter option 1-8: ")) 
    match choice1:
        case 1:
            main.Smashsmashmenu()
        case 2:
            main.Tourneymenu()
        case 3:
            main.main_menu
        case 4:
            main.main_menu
        case 5:
            a=1
while a == 3:
    match choice2:
        case 1:
            Volume = int(input("Set Volume 1-100"))
            if Volume >= 0 and Volume <= 100:
                print (Volume)
                a=2
            
            
        
            