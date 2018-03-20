class Player:
    health = 100
    name = ''
    inventory = []

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


player1 = Player
while True:
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



