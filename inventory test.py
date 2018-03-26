class Player:
    def __init__(self):
        self.health = 100
        self.name = ''
        self.inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)


def play():
        player1.add_inventory(Player, "pickaxe")


def drop():
    for b in player1.inventory:
        print(b)
        input('')


def name():
    player1.name_player()


player1 = Player
player1


