
class Player:
    health = 100
    name = ''
    alignment = ''
    inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)


# ASCII title art
def title_art():
    print('')
    print('_________ _______  _        _______   _________          _______   _________ _______ _________ _______  _       ')
    print('\__   __/(  ___  )| \    /\(  ____ \  \__   __/|\     /|(  ____ \  \__   __/(  ____ )\__   __/(  ___  )( \      ')
    print('   ) (   | (   ) ||  \  / /| (    \/     ) (   | )   ( || (    \/     ) (   | (    )|   ) (   | (   ) || (      ')
    print('   | |   | (___) ||  (_/ / | (__         | |   | (___) || (__         | |   | (____)|   | |   | (___) || |      ')
    print('   | |   |  ___  ||   _ (  |  __)        | |   |  ___  ||  __)        | |   |     __)   | |   |  ___  || |      ')
    print('   | |   | (   ) ||  ( \ \ | (           | |   | (   ) || (           | |   | (\ (      | |   | (   ) || |      ')
    print("   | |   | )   ( ||  /  \ \| (____/\     | |   | )   ( || (____/\     | |   | ) \ \_____) (___| )   ( || (____/\ ")
    print('   )_(   |/     \||_/    \/(_______/     )_(   |/     \|(_______/     )_(   |/   \__/\_______/|/     \|(_______/')
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
            print(player1.inventory)
            print('')
            print(player1.name + "'s Inventory.")
            print('1) Drop an Item')
            print('2) Use an Item')
            print('3) Close Inventory')
            y = input('')
            if y == '1':
                if len(player1.inventory) == 0:
                    print('')
                    print('You have nothing to drop!')
                    print('')
                else:
                    print('What item do you want to drop?' )
                    for b in player1.inventory:
                        num = 0
                        num += 1
                        num = str(num)
                        print(num+') ' + b)
                        num = int(num)
                    dropchoice = input('')
                    dropchoice = int(dropchoice)
                    if dropchoice > len(player1.inventory):
                        print('')
                        print('There is nothing there!')
                    elif dropchoice < len(player1.inventory):
                        print('')
                        print('There is nothing there!')
                    else:
                        dropchoice -= 1
                        del player1.inventory[dropchoice]
                        print('')
                        print('You drop the dagger onto the floor.')
                        dagger = 2
            elif y == '2':
                print('')
                print('You have no item to use!')
            elif y == '3':
                print('')
                print('Inventory Closed.')

# Go to the table
        if userChoice == '3':
            print('You got to the table and on it are 2 items, A cast iron Key and a Red Potion')
            take = input('Do you take the items? \n1) Yes\n2) No')
            if take == 1:
                print('')
                take1 = input('Which items do you take')



player1 = Player()
game_start()
room_1()

# my_function
# myVar
# MYCOMST

