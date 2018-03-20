
class Player:

    def __init__(self):
        self.health = 100
        self.name = ''
        self.inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def check_inventory(self):
        print(self.name + "'s Inventory")
        print(self.inventory)
        print('')
        print('1) Drop an Item')
        print('2) Use an Item')
        print('3) Close Inventory')
        choice = input('')
        print('')
        if choice == '1':
            self.drop_item()
        elif choice == '2':
            print("There's nothing to use! ")

    def drop_item(self, item):
        if len(self.inventory) > 1:
            for l in self.inventory:
                x = 0
                x += 1
                x = str(x)
                print('What Item do you want to drop?')
                print(x + ') ' + l)
        userChoice = input('')
        userChoice = int(userChoice)
        if 0 < userChoice <= len(self.inventory):
            del self.inventory[userChoice - 1]
            room.add_dropped(self.inventory(userChoice))


class Table:
    items = ["Brass Key", "Red Potion"]

    def take_key(self):
        keyIndex = self.items.index('Brass Key')
        del self.items[keyIndex]

    def take_pot(self):
        potIndex = self.items.index("Red Potion")
        del self.items[potIndex]

    def show_table(self):
        print('You approach the metal table, it is awkwardly placed in the room and does not match')
        print('the style and decor of the room.')
        print('')
        if len(self.items) == 1:
            print('There is a ' + self.items[0] + ' on the table.')
        elif len(self.items) == 2:
            print('There is a ' + self.items[0] + ' and a ' + self.items[1] + ' on the table.')
        else:
            print('There is nothing on the table.')


class Room:
    dropped = []

    def add_dropped(self, item):
        self.dropped.append(item)

    def picked_up(self, item):
        index = self.dropped.index(item)
        del self.dropped[index]


# ASCII title art
def title_art():
    print('')
    print('_________ _______  _        _______   _________          _______   _________ _______ _________ _______  _       ')
    print('\__   __/(  ___  )| \    /\(  ____ \   \__   __/|\     /|(  ____ \   \__   __/(  ____ )\__   __/(  ___  )( \      ')
    print('   ) (   | (   ) ||  \  / /| (    \/      ) (   | )   ( || (    \/      ) (   | (    )|   ) (   | (   ) || (      ')
    print('   | |   | (___) ||  (_/ / | (__          | |   | (___) || (__          | |   | (____)|   | |   | (___) || |      ')
    print('   | |   |  ___  ||   _ (  |  __)         | |   |  ___  ||  __)         | |   |     __)   | |   |  ___  || |      ')
    print('   | |   | (   ) ||  ( \ \ | (            | |   | (   ) || (            | |   | (\ (      | |   | (   ) || |      ')
    print("   | |   | )   ( ||  /  \ \| (____/\      | |   | )   ( || (____/\      | |   | ) \ \_____) (___| )   ( || (____/\ ")
    print('   )_(   |/     \||_/    \/(_______/      )_(   |/     \|(_______/      )_(   |/   \__/\_______/|/     \|(_______/')
    print('')


# function to start the game
def game_start():
    # Creates The Player
    title_art()
    input('')
    print('')
    print('A blinding white light fills your vision as the trials begin. ')
    print('Your vision takes a while to adjust but the familiar sterile smell')
    print('of a dentist fills your nose. ')
    print('')
    print('You find yourself in a cuboid room with nothing but the cold')
    print('hard steel chair that you are sat on and the similarly made table')
    print('in front of you. ')
    print('')
    input('Press enter to continue... ')
    print('')
    print('')
    print('A piece of paper with a wall of nonsensical text is written on it')
    print('A small area titled "Name?" ')
    print('')
# Names the player
    player1.name_player()
    print('')
    print('')


# The First room First Choice.
def room_1():
    print('The paper disappears from the table and so does the light.')
    print('')
    print("An uncomfortable amount of time passes and suddenly everything appears.")
    print("Your now sat on a wooden chair in a new room. The room looks like it's")
    print('part of a wooden lodge. There is a table with various items on it and a')
    print('wooden door with a lock.')
    print('')

    loop = 1
    dagger = 0
    while loop == 1:
        userChoice = 0
        print('')
        print('What will you do? ')
        print('1) Look Around')
        print('2) Check Inventory')
        print('3) Go to Table')
        print('4) Open the Door')
        print('')
        userChoice = input("")
# Dagger pickup prompt
        if userChoice == '1':
            if dagger == 0:
                print('You look around the various cabinets, dressers and crates around the room,')
                print('you do not find anything of interest except a Silver Orcish Dagger hanging ')
                print('from the wall.')
                x = input('Do you take it? \n 1) Yes \n 2) No\n')
                if x == '1':
                    player1.add_inventory("Orchish Dagger")
                    print('Item Added, Orcish Dagger')
                    dagger = 1
                elif x == '2':
                    print('You leave the dagger on the wall.')
                    print('')
            elif dagger == 2:
                print('You trip over the dagger that you dropped earlier.')
                x2 = input('Do you take it? \n 1) Yes \n 2) No\n')
                if x2 == '1':
                    player1.add_inventory("Orchish Dagger")
                    print('Item Added, Orcish Dagger')
                    dagger = 1
                elif x2 == '2':
                    print('You leave the dagger on the floor')
                    print('')
            else:
                print('')
                print("The room looks like it's part of a wooden lodge. There is a table with various items on it and ")
                print("a wooden door with a lock.")
                print('')
# Open inventory prompt
        elif userChoice == '2':
            player1.check_inventory()

# Go to the table
        table = Table()
        if userChoice == '3':
            table.show_table()
            take = input('Do you take the Key? \n1) Yes\n2) No\n')
            print('')
            if take == '1':
                print('You took the Key! ')
                player1.add_inventory("Brass key")
                table.take_key()

            else:
                print('You leave the key on the table')


room = Room()
player1 = Player
game_start()
room_1()

# my_function
# myVar
# MYCOMST

