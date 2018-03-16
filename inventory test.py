import time


class Player:
    health = 100
    name = ''
    alignment = ''
    inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)
        print('Item Added! ')
        print(self.inventory)


def play():
    player1.add_inventory(Player, "pickaxe")

player1 = Player

player1.name_player(Player)
play()
player1.add_inventory(Player, "coin")

