import time

class Player:
    health = 100
    name = ''
    alignment = ''
    def name_Player(self):
        self.name = input('Enter your name? ')

def gamestart():
    # Creates The Player
    player1 = Player()
    print('')
    print('A blinding white light fills your vision as the trials begin. ')
    print('Your vision takes a while to adjust but the familiar sterile smell')
    print('of a dentist fills your nose. ')
    print('')
    input('Press enter to continue... ')
    print('')
    print('You find yourself in a cuboid room with nothing but the cold')
    print('hard steel chair that you are sat on and the similarly made table')
    print('in front of you. ')
    print('')
    input('Press enter to continue... ')
    print('')
    print('A piece of paper with a wall of nonsensical text is written on it')
    print('A small area titled "Name?" ')
    print('')
    player1.name_Player()
    print('')


gamestart()
# my_function
# myVar
# MYCOMST

