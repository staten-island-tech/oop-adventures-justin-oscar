class gamemode():
    def main_menu(self):
        print("1.) Smash")

        
    def Smash_menu(self):
        print("1.) Smash")
        print("2.) Tourney")
        print("3.) Squad Strike")
        print("4.) Special Strike")
        print("5.) Back")
    def Smashsmashmenu(self):
        print("1.) Create Ruleset")
        print("2.) Use Existing Ruleset")
        print("3.) Back")
main = gamemode()
def mainfunction():
    main.main_menu()
    choice = int(input("Enter option 1: "))

    match choice:
        case 1:
            main.Smash_menu()
            smashmenuoptions()
def smashmenuoptions():
    choice1 = int(input("Enter option 1-5: "))
    match choice1:
        case 1:
            main.Smashsmashmenu()
        case 2:
            main.Tourneymenu()
        case 3:
            main.specialsmashmenu()
        case 4:
            main.main_menu()
        case 5:
            mainfunction()
            return choice1
mainfunction()