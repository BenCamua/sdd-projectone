import random
import time
import cmd
import textwrap
import os

## Player Creation##


class Occupation(object):
    # race for all characters
    health = 0
    attack = 0
    occupation = ""
    name = ""

    def __init__(self, health, attack, occupation, name):
        self.health = health
        self.attack = attack
        self.occupation = occupation
        self.name = name
        print ("self = ", self)


class Fireman:
    health = 70
    attack = 20
    name = ''
    inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)


# Intro
def displayIntro():
    time.sleep(3)
    print("Hello there")
    time.sleep(3)
    print("Welcome to....")
    time.sleep(3)
    print("  ___   _  _                _____                                 ")
    print(" / _ \ | |(_)              |  ___|                                ")
    print("/ /_\ \| | _   ___  _ __   | |__   ___   ___   __ _  _ __    ___  ")
    print("|  _  || || | / _ \| '_ \  |  __| / __| / __| / _` || '_ \  / _ \ ")
    print("| | | || || ||  __/| | | | | |___ \__ \| (__ | (_| || |_) ||  __/ ")
    print("\_| |_/|_||_| \___||_| |_| \____/ |___/ \___| \__,_|| .__/  \___| ")
    print("                                                    | |           ")
    print("                                                    |_|           ")




displayIntro()
