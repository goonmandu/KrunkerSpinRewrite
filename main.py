# Created by GoonMandu: https://www.github.com/goonmandu
# Discord: goonmandu#4897
# Twitter: @goonmandu_
# First party code is published under the MIT License.
# All other assets are copyright of their respective owners.
# Based on Krunker Version v4.2.1

# SNIPER 1, AK 2, PISTOL 3, SMG 4, REV 5, SHOTTY 6, LMG 7, SEMI 8, RPG 9, UZI 10, DEAGLE 11, ALIEN 12, CROSSY 14,
# FAMAS 15, SAWEDOFF 16, AUTOPISTOL 17, BLASTER 19.
# TODO: ASSIGN CLASS NAMES TO WEAPON ID FOR PRINTING

import json
import random
from termcolor import colored, cprint
import time

num_of_spins = 0
delay = 0
CURRENT_SEASON = 4
available_skins = None

print("Welcome to the Krunker Heroic Spin Simulator.\n")


def set_spins():
    global num_of_spins
    try:
        num_of_spins = int(input("Enter an integer number of spins - "))
    except ValueError:
        print("Please enter an integer.")
        set_spins()


def set_delay():
    global delay
    try:
        delay = float(input("Time, in seconds, between each spin - "))
    except ValueError:
        print("Please enter an integer.")
        set_delay()


def load_and_print_available_skins(rarity_number, rarity_color):
    global available_skins
    available_skins = [item for item in data if item["rarity"] == rarity_number and item["seas"] == CURRENT_SEASON]
    if rarity_number == 6:
        unob_skin_name = ""
        char_position = 0
        for char in random.choice(available_skins)["name"]:
            if char_position % 6 == 0:
                unob_skin_name += colored(char, "red", attrs=["bold", "dark"])
            elif char_position % 6 == 1:
                unob_skin_name += colored(char, "yellow", attrs=["bold", "dark"])
            elif char_position % 6 == 2:
                unob_skin_name += colored(char, "green", attrs=["bold", "dark"])
            elif char_position % 6 == 3:
                unob_skin_name += colored(char, "cyan", attrs=["bold", "dark"])
            elif char_position % 6 == 4:
                unob_skin_name += colored(char, "blue", attrs=["bold", "dark"])
            else:
                unob_skin_name += colored(char, "magenta", attrs=["bold", "dark"])
            char_position += 1
        cprint(unob_skin_name)
    else:
        cprint(f"{random.choice(available_skins)['name']}", rarity_color, attrs=["bold", "dark"])


file = open("items.json")
data = json.load(file)

set_spins()
set_delay()

for i in range(num_of_spins):
    result = random.randint(1, 10000)
    if result == 1:
        load_and_print_available_skins(6, None)
    elif 2 <= result <= 51:
        load_and_print_available_skins(5, "grey")
    elif 52 <= result <= 300:
        load_and_print_available_skins(4, "red")
    elif 301 <= result <= 1700:
        load_and_print_available_skins(3, "yellow")
    elif 1701 <= result <= 5200:
        load_and_print_available_skins(2, "magenta")
    else:
        load_and_print_available_skins(1, "blue")
    time.sleep(delay)

