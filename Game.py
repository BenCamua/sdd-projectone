import random


# This is the player class, The player will have:
# HEALTH
# NAME
# INVENTORY
class Player:

    def __init__(self):
        self.health = 100
        self.name = ''
        self.inventory = []
        self.equipped = []
        self.item_achievement = ''

    def check_alive(self):  # Returns a value representing if the player is currently alive or dead.
        if self.health <= 0:
            return 'DEAD'
        else:
            return 'ALIVE'

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
            userChoice = input('')
            if userChoice.isnumeric():  # This prevents the code from breaking after invalid input
                userChoice = int(userChoice)
                if 0 < userChoice <= len(self.inventory):   # all '-1''s in the if statement are for indexing
                    room.add_dropped(self.inventory[userChoice - 1])
                    print('')
                    print(self.inventory[userChoice - 1] + ' has been dropped.')
                    del self.inventory[userChoice - 1]
                else:
                    print("\nThere's nothing there")
            else:
                print('\nInvalid Input')
        else:
            print('There is nothing to drop!')

    def hurt(self, dmg):    # This will subtract the int that was passed into the function from the health.
        print('')
        self.health = self.health - dmg
        dmg = str(dmg)
        print('You took ' + dmg + 'DMG.\n')

    def attack(self):   # This will output a damage value to the grue mob dependant on the equipped items of the player
        if 'Orcish Dagger' in self.equipped:    # with a dagger
            dmg = random.uniform(0, 5)
            dmg = int(round(dmg))
            if dmg == 7:
                print('You land a critical strike!!')
            grue.hurt(dmg)

        else:   # without
            dmg = random.uniform(0, 4)
            dmg = int(round(dmg))
            if dmg == 6:
                print('You land a critical strike!!')
            grue.hurt(dmg)
        return grue.check_alive()

    def equip(self, item):  # equips a passed in item, if already equipped, will print text.
        if len(self.equipped) == 0:
            self.equipped.append(item)
        else:
            print('Item already equipped')

    def equip_and_use(self):    # The interface the user interacts with to equip an item
        print('\nWhat item do you want to use or equip?')
        print("Type 'Close' to close this menu.\n")
        loop = 1
        while loop == 1:
            print(self.inventory)
            print('')
            choice = input('')
            print('')
            if choice == 'Close':
                loop = 0
            elif choice == "Orcish Dagger":
                if 'Orcish Dagger' in self.inventory:   # equips the weapon
                    if "Orcish Dagger" not in self.equipped:
                        print('Dagger equipped\n')
                        self.equipped.append('Orcish Dagger')
                    else:
                        print('You already have that equipped\n')
                else:
                    print('You do not have that item')
            elif choice == "Red Potion":    # Uses the potion if there is a potion
                if 'Red Potion' in self.inventory:
                    print('You drank the potion')
                    self.health = int(self.health) + 20
                    index = self.inventory.index('Red Potion')
                    del self.inventory[index]
                    if self.health > 100:
                        excess = self.health - 100
                        self.health = self.health - excess
                    print('You now have ' + str(self.health) + ' Health!\n')
                else:
                    print('You do not have that item')
            elif choice == "Brass Key":
                if "Brass Key" in self.inventory:
                    print('You cannot use that item right now!\n')
                else:
                    print('You do not have that item\n')

    def stat_readout(self):  # prints out the current stats of the player
        currenthealth = str(self.health)
        attack = str(self.equipped)
        inventory = str(self.inventory)
        print('\n=========================== ' + self.name + ' ===========================')
        print('HEALTH: ' + currenthealth)
        print('ATTACK: ' + attack)
        print('INVENTORY: ' + inventory)
        print('                                                                  ')
        if self.health > 50:
            print('                     You stand tall and brave                     ')
        else:
            print("                 Your stance is faltering                         ")
        print('                                                                  ')
        print('==================================================================\n')


# This is the Table class, it has an inventory and also the necessary functions to interact with it.
class Table:
    items = ["Brass Key", "Red Potion"]

    def check_table(self):  # This function returns a value depending if there is anything on the table.
        if len(self.items) > 0:
            return 1
        else:
            return 0

    def take_key(self):  # This removes the Brass Key from the Table's inventory
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


# This class holds the inventory of the first room, and also provide functions to interact with it.
class Room:

    def __init__(self):
        self.dropped = []

    def add_dropped(self, item):    # adds an item to the rooms inventory
        self.dropped.append(item)

    def picked_up(self, item):  # removes an item from the rooms inventory
        index = self.dropped.index(item)
        del self.dropped[index]

    def room_check(self):   # checks if there is anything in the room.
        if len(self.dropped) > 0:
            return 1
        else:
            return 0


# This class contains the functions necessary for the mob to attack, get hurt and die.
class Grue:

    def __init__(self):
        self.health = 15

    def check_alive(self):  # Returns a value that represents the current state of the mob, dead or alive
        if self.health <= 0:
            return 'DEAD'
        else:
            return 'ALIVE'

    def attack(self):   # allows for the mob to hurt the player.
        print('')
        dmg = random.uniform(10, 25)
        if dmg <= 15:
            print('The Grue slices at you but only manages to scrape you.')
        elif dmg >= 20:
            print('The Grue takes a quick stab and finds its mark on you.')
        else:
            print('The Grue lunges forward and swipes at your chest.')
        player1.hurt(int(round(dmg)))

    def hurt(self, dmg):    # allows for the mob to be hurt by player
        self.health = self.health - dmg
        dmg = str(dmg)
        print('\nThe Grue took ' + dmg + ' damage!\n')

    def stat_readout(self):  # prints out the stats of the mob
        currenthealth = str(self.health)
        print('\n============================ THE GRUE ============================')
        print('HEALTH: ' + currenthealth)
        print('DEFENSE: SHADOW ARMOUR, EXTREMELY RESISTANT TO PHYSICAL ATTACKS   ')
        print('ATTACK: CLAWS OF DARKNESS, UNPREDICTABLE AND HAS A MIND OF ITS OWN')
        print('                                                                  ')
        if self.health > 5:
            print('                   It stares menacingly at you                    ')
        else:
            print("                  Its gaze is faltering                          ")
        print('                                                                  ')
        print('==================================================================\n')


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
    print('Your vision takes a while to adjust and the familiar sterile smell')
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
                print('from the wall.\n')
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
        if userChoice == '2':
            print(' ')
            player1.check_inventory()

# Go to the table
        if userChoice == '3':
            table.show_table()
            if table.check_table() == 1:
                take = input('Do you take the Key and the Red potion? \n1) Yes\n2) No\n')
                print('')
                if take == '1':
                    print('\nItems Added')
                    player1.add_inventory("Brass Key")
                    player1.add_inventory("Red Potion")
                    table.take_key()
                    table.take_pot()
                else:
                    print('\nYou leave them on the table')

# Go to the LOCKED door
        if userChoice == '4':
            if "Brass Key" in player1.inventory:
                print('\nYou approach the wooden door')
                print('The door looks to be very sturdy and has a large brass lock.\n')
                print('Do you use your Brass key to unlock the door?')
                print('1) Yes\n2) No\n')
                unlock = input('')
                if unlock == '1':
                    loop = 0
            else:
                print('\nYou approach the wooden door')
                print('The door looks to be very sturdy and has a large brass lock.\n')
                print('You will need a Key to open this door.')


def score_updater():    # Solely for the achievement system that will add to the final score.
    if len(player1.inventory) == 3:
        player1.item_achievement = 'ACHIEVED'


def room_2():   # room2 logic and prints
    print('\nYou unlock the door and open it.')
    print('This room follows the same decor as the previous. It is similarly sized with another metal table with a')
    print('black glowing box with red inscriptions on it. As you approach the table the door behind you locks shut')
    print('and the the box starts shaking violently. The lights in the room dim and the box morphs into what looks')
    print('to be a Grue')
    input('\nPress enter to start encounter...\n')
    battle()
    ending_seq()


def battle():   # Battle Logic
    grue.stat_readout()
    while grue.check_alive() == player1.check_alive():
        print('What will you do?')
        print('1) Attack\n2) Use and Item\n3) View your Stats\n4) Inspect the Grue\n')
        choice = input('')
        if choice == '1':
            gruestate = player1.attack()    # important. Grue can only attack if its alive after attack.
            if gruestate == 'ALIVE':
                grue.attack()
        elif choice == '2':
            player1.equip_and_use()
        elif choice == '3':
            player1.stat_readout()
        elif choice == '4':
            grue.stat_readout()


def ending_seq():   # END sequence. Adds up scores and prints out sum text.
    score = 0
    if grue.check_alive() == 'DEAD':
        score += 100
    if player1.item_achievement == 'ACHIEVED':
        score += 30
    score += player1.health
    if grue.check_alive() == 'DEAD':
        print('The Grue crumbles after your last attack. Its face deforms and melts back into the box that it morphed')
        print('out as. The rooms light goes out and the moons light from a window to your left dims to blackness.')
        print('After a while, your back where it all started.\n')
    else:
        print('You collapse under the might of the Grue. Your vision blackens as it opens its jaws to consume you.')
        print('After a while, your back where it all started.\n')
    print('GAME COMPLETED')
    print('YOUR HIGH SCORE: ' + str(score))
    input('')


table = Table()
room = Room()
player1 = Player()
game_start()
room_1()
score_updater()
grue = Grue()
room_2()
