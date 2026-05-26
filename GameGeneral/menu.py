class gamemode():
    def main_menu(self):
        print ("1.) Smash")
        print ("2.) Vault")
    def Smash_menu(self):
        print ("1.) Smash")
        print ("2.) Tourney")
        print ("3.) Squad Strike")
        print ("4.) Special Strike")
        print ("5.) Back")

    def VaultMenu(self):
        print ("1.) Sounds")
        print ("2.) Replays")
        print ("3.) Records")
        print ("4.) Challenges")
        print ("5.) Tips")
        print ("6.) Movies")
        print ("7.) Shop")
        print ("8.) Back")
    def Smashsmashmenu(self):
        ""
main = gamemode()
main.main_menu
choice = input("Enter option 1-3")
match choice: 
    case "1":
        main.Smash_menu
    case "2":
        main.VaultMenu