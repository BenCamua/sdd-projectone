

# This is the player class, The player will have a health, a name and also an inventory.
class Player:

    def __init__(self):
        self.health = 100
        self.name = ''
        self.inventory = []

    def name_player(self):  # This function names the player
        self.name = input('\nEnter your name? ')

    def add_inventory(self, item):  # This function adds takes in an item and will add it to inventory
        self.inventory.append(item)

    def check_inventory(self):  # This function gives the user and interface to interact with their inventory
        print(self.name + "'s Inventory")
        print(self.inventory)
        print('\n1) Drop an Item')
        print('2) Use an Item')
        print('3) Close Inventory\n')
        choice = input('')
        print('')
        if choice == '1':
            self.drop_item()
        elif choice == '2':
            print("There's nothing to use! ")

    def drop_item(self):  # This function removes items from the player's inventory and adds them to room's inventory
        if len(self.inventory) >= 1:
            counter = 0
            print('What Item do you want to drop?')
            for l in self.inventory:
                counter = int(counter)
                counter += 1
                counter = str(counter)
                print(counter + ') ' + l)
            print('')
            userChoice = int(input(''))
            if 0 < userChoice <= len(self.inventory):   # all '-1''s in the if statement are for indexing
                room.add_dropped(self.inventory[userChoice - 1])
                print('')
                print(self.inventory[userChoice - 1] + ' has been dropped.')
                del self.inventory[userChoice - 1]
            else:
                print("\nThere's nothing there")
        else:
            print('There is nothing to drop!')


# This is the Table class, it has an inventory and also the necessary functions to interact with it.
class Table:
    items = ["Brass Key", "Red Potion"]

    def check_table(self):  # This function returns a value depending if there is anything on the table.
        if len(self.items) > 0:
            return 1
        else:
            return 0

    def take_key(self): # This removes the Brass Key from the Table's inventory
        keyIndex = self.items.index('Brass Key')
        del self.items[keyIndex]

    def take_pot(self):  # This removes the Red Potion for the Table's inventory
        potIndex = self.items.index("Red Potion")
        del self.items[potIndex]

    def show_table(self):   # This function shows what is on the table
        print('\nYou approach the metal table, it is awkwardly placed in the room and does not match')
        print('the style and decor of the room.')
        print('')
        if len(self.items) == 1:    # This test for number of items on table is no longer needed as feature was removed
            print('There is a ' + self.items[0] + ' on the table.')
        elif len(self.items) == 2:
            print('There is a ' + self.items[0] + ' and a ' + self.items[1] + ' on the table.')
        else:
            print('There is nothing on the table.')


class Room:

    def __init__(self):
        self.dropped = []

    def add_dropped(self, item):
        self.dropped.append(item)

    def picked_up(self, item):
        index = self.dropped.index(item)
        del self.dropped[index]

    def room_check(self):
        if len(self.dropped) > 0:
            return 1
        else:
            return 0


# ASCII title art
def title_art():
    print('''
    _________ _______  _        _______    _________          _______    _________ _______ _________ _______  _       
    \__   __/(  ___  )| \    /\(  ____ \   \__   __/|\     /|(  ____ \   \__   __/(  ____ )\__   __/(  ___  )( \      
       ) (   | (   ) ||  \  / /| (    \/      ) (   | )   ( || (    \/      ) (   | (    )|   ) (   | (   ) || (      
       | |   | (___) ||  (_/ / | (__          | |   | (___) || (__          | |   | (____)|   | |   | (___) || |      
       | |   |  ___  ||   _ (  |  __)         | |   |  ___  ||  __)         | |   |     __)   | |   |  ___  || |      
       | |   | (   ) ||  ( \ \ | (            | |   | (   ) || (            | |   | (\ (      | |   | (   ) || |      
       | |   | )   ( ||  /  \ \| (____/\      | |   | )   ( || (____/\      | |   | ) \ \_____) (___| )   ( || (____/\ 
       )_(   |/     \||_/    \/(_______/      )_(   |/     \|(_______/      )_(   |/   \__/\_______/|/     \|(_______/
    ''')


# function to start the game
def game_start():
    # Creates The Player
    title_art()
    print('\n\nA blinding white light fills your vision as the trials begin. ')
    print('Your vision takes a while to adjust but the familiar sterile smell')
    print('of a dentist fills your nose. ')
    print('')
    print('You find yourself in a cuboid room with nothing but the cold')
    print('hard steel chair that you are sat on and the similarly made table')
    print('in front of you. ')
    print('')
    input('Press enter to continue... ')
    print('\nA piece of paper with a wall of nonsensical text is written on it')
    print('A small area titled "Name?" ')
    player1.name_player()   # Names the player


# The First room First Choice.
def room_1():
    print('\nThe paper disappears from the table and so does the light.')
    print("An uncomfortable amount of time passes and suddenly everything appears.")
    print("Your now sat on a wooden chair in a new room. The room looks like it's")
    print('part of a wooden lodge. There is a table with various items on it and a')
    print('wooden door with a lock.')

    loop = 1
    firsttime = 1   # firstTime is to detect if the dagger on the wall
    while loop == 1:
        print('\nWhat will you do? ')
        print('1) Look Around')
        print('2) Check Inventory')
        print('3) Go to Table')
        print('4) Open the Door')
        userChoice = input("\n")
# Dagger pickup prompt
        if userChoice == '1':   # This is the 'Look Around' choice for room_1
            if firsttime == 1:  # firstTime is to detect if the dagger on the wall
                print('\nYou look around the various cabinets, dressers and crates around the room,')
                print('you do not find anything of interest except a Silver Orcish Dagger hanging ')
                print('from the wall.')
                x = input('Do you take it? \n 1) Yes \n 2) No\n\n')
                if x == '1':
                    player1.add_inventory("Orcish Dagger")
                    print('\nItem Added, Orcish Dagger')
                    firsttime = 0
                elif x == '2':
                    print('\nYou leave the dagger on the wall.')
            else:
                if room.room_check() == 0:
                    print("\nThe room looks like it's part of a wooden lodge. There is a table with various items")
                    print(" on it and a wooden door with a lock.")
                else:
                    if len(room.dropped) == 1:
                        print('\nYou trip over an item that you previously dropped.')
                        print('1) ' + room.dropped[0])
                        take = input('\nDo you pick it up?\n1) Yes\n2) No\n')
                        if take == '1':
                            print(room.dropped[0] + ' added to inventory.')
                            player1.add_inventory(room.dropped[0])
                            room.picked_up(room.dropped[0])
                    else:
                        print('You find a few items that you dropped onto the floor.')
                        print(room.dropped)
                        pickup = input('\nDo you pick them up?\n1) Yes\n2) No\n')
                        if pickup == '1':
                            for individualitems in room.dropped:
                                index = room.dropped.index(individualitems)
                                player1.add_inventory(room.dropped[index])
                                room.picked_up(room.dropped[index])


# Open inventory prompt
        elif userChoice == '2':
            print('')
            player1.check_inventory()

# Go to the table
        table = Table()
        if userChoice == '3':
            table.show_table()
            if table.check_table() == 1:
                take = input('\nDo you take the Key and the Red potion? \n1) Yes\n2) No\n')
                print('')
                if take == '1':
                    print('\nItems Added')
                    player1.add_inventory("Brass key")
                    player1.add_inventory("Red Potion")
                    table.take_key()
                    table.take_pot()
                else:
                    print('\nYou leave them on the table')


room = Room()
player1 = Player()
game_start()
room_1()


