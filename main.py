# Created by GoonMandu: https://www.github.com/goonmandu
# Discord: goonmandu#4897
# Twitter: @goonmandu_
# First party code is published under the MIT License.
# All other assets are copyright of their respective owners.
# Based on Krunker Version v4.2.1

# SNIPER 1, AK 2, PISTOL 3, SMG 4, REV 5, SHOTTY 6, LMG 7, SEMI 8, RPG 9, UZI 10, DEAGLE 11, ALIEN 12, CROSSY 14,
# FAMAS 15, SAWNOFF 16, AUTOPISTOL 17, BLASTER 19.
# TODO: GUI (ADVANCED SHIT)

import json
import random
from termcolor import colored, cprint
import time

num_of_spins = 0
delay = 0
CURRENT_SEASON = 4
LAST_UPDATE = "Sept 2 2021"
KRUNKER_VERSION = "4.2.1"

print(f"Welcome to the Krunker Heroic Spin Simulator.\nLast updated: {LAST_UPDATE} for version {KRUNKER_VERSION}")


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
    available_skins = []
    for skin in data:
        if ("reqT" and "limT" and "noSale") not in skin and skin["seas"] == CURRENT_SEASON and skin["rarity"] == rarity_number:
            available_skins.append(skin)
    chosen_skin = random.choice(available_skins)
    if rarity_number == 6:
        unob_skin_name = ""
        char_position = 0
        for char in chosen_skin["name"]:
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
        if "weapon" in chosen_skin:
            if chosen_skin["weapon"] == 1:
                cprint(f"{unob_skin_name} [Sniper]")
            elif chosen_skin["weapon"] == 2:
                cprint(f"{unob_skin_name} [AK]")
            elif chosen_skin["weapon"] == 3:
                cprint(f"{unob_skin_name} [Pistol]")
            elif chosen_skin["weapon"] == 4:
                cprint(f"{unob_skin_name} [SMG]")
            elif chosen_skin["weapon"] == 5:
                cprint(f"{unob_skin_name} [Revolver]")
            elif chosen_skin["weapon"] == 6:
                cprint(f"{unob_skin_name} [Shotgun]")
            elif chosen_skin["weapon"] == 7:
                cprint(f"{unob_skin_name} [Machine Gun]")
            elif chosen_skin["weapon"] == 8:
                cprint(f"{unob_skin_name} [Semi-Auto]")
            elif chosen_skin["weapon"] == 9:
                cprint(f"{unob_skin_name} [Rocket Launcher]")
            elif chosen_skin["weapon"] == 10:
                cprint(f"{unob_skin_name} [Micro Uzi]")
            elif chosen_skin["weapon"] == 11:
                cprint(f"{unob_skin_name} [Desert Eagle]")
            elif chosen_skin["weapon"] == 12:
                cprint(f"{unob_skin_name} [Alien Blaster]")
            elif chosen_skin["weapon"] == 14:
                cprint(f"{unob_skin_name} [Crossbow]")
            elif chosen_skin["weapon"] == 15:
                cprint(f"{unob_skin_name} [FAMAS]")
            elif chosen_skin["weapon"] == 16:
                cprint(f"{unob_skin_name} [Sawed-Off]")
            elif chosen_skin["weapon"] == 17:
                cprint(f"{unob_skin_name} [Auto Pistol]")
            elif chosen_skin["weapon"] == 19:
                cprint(f"{unob_skin_name} [Blaster]")
            else:
                cprint(f"{unob_skin_name} [Other Weapon]")
        else:
            if chosen_skin["type"] == 1:
                cprint(f"{unob_skin_name} [Hat]")
            elif chosen_skin["type"] == 2:
                cprint(f"{unob_skin_name} [Back]")
            elif chosen_skin["type"] == 3:
                cprint(f"{unob_skin_name} [Melee]")
            elif chosen_skin["type"] == 4:
                cprint(f"{unob_skin_name} [Spray]")
            elif chosen_skin["type"] == 5:
                cprint(f"{unob_skin_name} [Dye]")
            elif chosen_skin["type"] == 6:
                cprint(f"{unob_skin_name} [Waist]")
            elif chosen_skin["type"] == 7:
                cprint(f"{unob_skin_name} [Face]")
            elif chosen_skin["type"] == 8:
                cprint(f"{unob_skin_name} [Shoes]")
            else:
                cprint(f"{unob_skin_name} [Other Clothing]")
    else:
        cprint(f"{chosen_skin['name']}", rarity_color, attrs=["bold", "dark"], end="")
        if "weapon" in chosen_skin:
            if chosen_skin["weapon"] == 1:
                print(" [Sniper]")
            elif chosen_skin["weapon"] == 2:
                print(" [AK]")
            elif chosen_skin["weapon"] == 3:
                print(" [Pistol]")
            elif chosen_skin["weapon"] == 4:
                print(" [SMG]")
            elif chosen_skin["weapon"] == 5:
                print(" [Revolver]")
            elif chosen_skin["weapon"] == 6:
                print(" [Shotgun]")
            elif chosen_skin["weapon"] == 7:
                print(" [Machine Gun]")
            elif chosen_skin["weapon"] == 8:
                print(" [Semi Auto]")
            elif chosen_skin["weapon"] == 9:
                print(" [Rocket Launcher]")
            elif chosen_skin["weapon"] == 10:
                print(" [Micro Uzi]")
            elif chosen_skin["weapon"] == 11:
                print(" [Desert Eagle]")
            elif chosen_skin["weapon"] == 12:
                print(" [Alien Blaster]")
            elif chosen_skin["weapon"] == 14:
                print(" [Crossbow]")
            elif chosen_skin["weapon"] == 15:
                print(" [FAMAS]")
            elif chosen_skin["weapon"] == 16:
                print(" [Sawed Off]")
            elif chosen_skin["weapon"] == 17:
                print(" [Auto Pistol]")
            elif chosen_skin["weapon"] == 19:
                print(" [Blaster]")
            else:
                print(" [Other Weapon]")
        else:
            if chosen_skin["type"] == 1:
                print(" [Hat]")
            elif chosen_skin["type"] == 2:
                print(" [Back]")
            elif chosen_skin["type"] == 3:
                print(" [Melee]")
            elif chosen_skin["type"] == 4:
                print(" [Spray]")
            elif chosen_skin["type"] == 5:
                print(" [Dye]")
            elif chosen_skin["type"] == 6:
                print(" [Waist]")
            elif chosen_skin["type"] == 7:
                print(" [Face]")
            elif chosen_skin["type"] == 8:
                print(" [Shoes]")
            else:
                print(" [Other Clothing]")


file = open("items.json")
data = json.load(file)

set_spins()
set_delay()
print()

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
