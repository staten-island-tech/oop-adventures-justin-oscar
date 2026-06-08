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
        print("1.) Use Existing Ruleset")
        print("2.) Suggest a new ruleset to the developers")
        print("3.) Back")
    def ruleset(self):
        print("1.) Three Stock")
        print("2.) Timed battle")
        print("3.) Back")
main = gamemode()
def mainfunction():
    main.main_menu()
    choice = int(input("Enter option 1: "))

    match choice:
        case 1:
            main.Smash_menu()
            smashmenuoptions()
def smashsmashmenu():
    main.Smashsmashmenu()
    choice2 = int(input("Enter option 1-3"))
    match choice2:
        case 1:
            main.ruleset()
            choice3 = int(input("Enter option 1-3"))
            match choice3:
                case 1:
                    character_screen()

        case 2:
            Suggestion = input("Suggestions?")
            print("Thank you for the suggestion")
            smashmenuoptions()
            return Suggestion
        case 3:
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