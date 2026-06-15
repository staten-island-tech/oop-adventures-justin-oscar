class User:
    def __init__(self, name, power, hp, moves):
        self.name = name
        self.power = power
        self.hp = hp
        self.moves = moves

    def display_info(self):
        return self.name + " Power: " + str(self.power) + " HP: " + str(self.hp)


class Shooter(User):
    def __init__(self, name, power, hp, moves):
        super().__init__(name, power, hp, moves)


class Tank(User):
    def __init__(self, name, power, hp, moves):
        super().__init__(name, power, hp, moves)


class Sword(User):
    def __init__(self, name, power, hp, moves):
        super().__init__(name, power, hp, moves)

    
