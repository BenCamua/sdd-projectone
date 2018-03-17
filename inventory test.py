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



def play():
        player1.add_inventory(Player, "pickaxe")


def drop():
    for b in player1.inventory:
        print(b)
        input('')


player1 = Player
player1.name_player()
play()
player1.add_inventory(Player, "coin")
drop()

