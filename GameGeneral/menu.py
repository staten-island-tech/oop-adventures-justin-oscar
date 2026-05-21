""" 
gamemode = input("Smash, Spirits, Games & More, Vault, or Online?")
if gamemode == "Smash":
    smash_gamemode = input("Smash, Squad Strike, Tourney, or Special Smash?")
    if smash_gamemode == "Smash":
        smash_set = input("Use existing ruleset or create a new one?")
        if smash_set == "Existing ruleset":
            maps = input("What map would you like to use?")
            if maps in Whatever map is:
                characters = input("What character would you like to use")
                if characters in Whatever character is:
                    Start = input("Change character, otherwise say READY TO FIGHT")
        if smash_set == "Create a new set"
    elif smash_gamemode == "Squad Strike":
        three_five = int(input("3 or 5"))
        if three_five == 5:
            for i in range(5):
                characters = input("What character would you like to use")
            Start = input("Change character, otherwise say READY TO FIGHT")
        elif three_five == 3:
            for i in range(3):
                characters = input("What character would you like to use")
            Start = input("Change character, otherwise say READY TO FIGHT")

    elif smash_gamemode == "Tourney":
        participants = int(input("How many participants would you like"))
        if participants < 4 or participants > 32:
            print ("Invalid, Please pick something between 4 and 32")
        else:
            CPU_num = int(input("How many CPUs would you like"))
            if CPU_num > participants:
                print ("Please choose a number lower than your amount of participants")
            else: 
                Start = input("Please choose what character you would like the CPUs to use. Otherwise, say READY TO FIGHT")
    elif smash_gamemode == "Special Smash":
        special_smash = input("")
elif gamemode == "Spirits":
    spirit_gamemode = input("Adventure, Spirit Board, or Collection?")
    if spirit_gamemode == "Adventure":
        op = input("Welcome to World of Light, would you like to load or start a new game")
        if op == "New Game":
            Difficulty = input("Very Easy, Easy, Normal, or Hard?")
elif gamemode == "Games & More":
    games_gamemode = input("Classic, Training, Mob Smash, Home-Run Contest, Stage Builder, amiibo, or Mii Fighter")
elif gamemode == "Vault":
    Vault_mode = input("Sounds, Replays, Records, Challenges, Tips, Movies, or Shop")
elif gamemode == "Online":
    h
while Start == "READY TO FIGHT":
    h """

""" class gamemode:
    def __init__(self, mode, mode2, mode3, mode4, mode5, mode6, mode7):
        self.mode = mode
        self.mode2 = mode2
        self.mode3 = mode3
        self.mode4 = mode4
        self.mode5 = mode5
        self.mode6 = mode6
        self.mode7 = mode7
Overall = gamemode("Smash", "Spirits", "Games & More", "Vault", "Online", ".", ".")
Smash = gamemode("Smash", "Tourney", "Squad Strike", "Special Smash", ".", ".", ".")
GamesAndMore = gamemode("Classic Mode", "Training", "Mob Smash", "Home-Run Contest", "Stage Builder", "amiibo", "Mii Fighter")
Spirits = gamemode("Adventure", "Spirit Board", "Collection", ".", ".", ".", ".") """
class gamemode():
    def main_menu():
        print ("1.) Smash")
        print ("2.) Spirits")
        print ("3.) Vault")
        print ("4.) Games & More")
        print ("5.) Online")
        print ("6.) Back")
    def Smash_menu():
        print ("1.) Smash")
        print ("2.) Tourney")
        print ("3.) Squad Strike")
        print ("4.) Special Strike")
        print ("5.) Back")
    def GamesAndMoreMenu():
        print ("1.) Classic")
        print ("2.) Training")
        print ("3.) Mob Smash")
        print ("4.) Home-Run Contest")
        print ("5.) Stage Builder")
        print ("6.) amiibo")
        print ("7.) Mii Fighter")
        print ("8.) Back")
    def SpiritsMenu():
        print ("1.) Adventure")
        print ("2.) Spirit Board")
        print ("3.) Collection")
        print ("4.) Back")
    def VaultMenu():
        print ("1.) Sounds")
        print ("2.) Replays")
        print ("3.) Records")
        print ("4.) Challenges")
        print ("5.) Tips")
        print ("6.) Movies")
        print ("7.) Shop")
        print ("8.) Back")
    def Smashsmashmenu():
        ""
main = gamemode()

Menu = input("NUM")
