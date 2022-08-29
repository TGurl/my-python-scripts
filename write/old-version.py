#!/usr/bin/env python

import os
import sys
import random

from time import sleep

CURSOR = True
HOMEDIR = os.path.expanduser("~")


class Colors:
    res = "\033[0m"
    red = "\033[31;1m"
    gre = "\033[32;1m"
    yel = "\033[33;1m"
    blu = "\033[34;1m"
    pin = "\033[35;1m"
    cya = "\033[36;1m"
    whi = "\033[37;1m"


def read_text(filename):
    global HOMEDIR
    if ".txt" not in filename:
        filename += ".txt"
    filename = os.path.join(f"{HOMEDIR}/Dev/python/write/data/{filename}")
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def cursor_off():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def cursor_on():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def toggle_cursor():
    global CURSOR
    if CURSOR:
        # Turn cursor off
        CURSOR = False
        cursor_off()
    else:
        # Turn cursor on
        CURSOR = True
        cursor_on()


def read_csv(filename):
    global HOMEDIR
    if ".csv" not in filename:
        filename += ".csv"
    path = os.path.join(f"{HOMEDIR}/Dev/python/write/data", filename)
    with open(path, "r") as f:
        data = f.read().replace("\n", "").replace("\n", "").split(",")
    return data


def wait_for_enter():
    answer = input(f"")
    del answer


def show_name(name):
    os.system("clear")
    res = "\033[0m"
    col = "\033[33;1m"
    print(f" {col}{name}{res}")


def choose_girl_name():
    data = read_csv("girlnames.csv")
    toggle_cursor()
    show_name(random.choice(data))
    wait_for_enter()
    toggle_cursor()


def choose_boy_name():
    data = read_csv("boynames.csv")
    toggle_cursor()
    show_name(random.choice(data))
    wait_for_enter()
    toggle_cursor()


def choose_town_name():
    global HOMEDIR
    colors = Colors()
    toggle_cursor()

    res = colors.res
    blu = colors.blu
    gre = colors.gre
    filename = "data/citynames.txt"
    writedir = f"{HOMEDIR}/Dev/python/write"

    with open(os.path.join(writedir, filename), "r") as f:
        data = f.readlines()
    name = random.choice(data)
    name = name.replace("\n", "").split(",")
    town = name[0]
    state = name[1]
    os.system("clear")
    print(f"{gre}{town}{res}\n{blu}{state}{res}")
    wait_for_enter()
    toggle_cursor()


def show_photo():
    global HOMEDIR
    os.system("clear")
    toggle_cursor()
    photos = []
    path = f"{HOMEDIR}/Dev/python/write/data/photos"
    for file in os.listdir(path):
        photos.append(os.path.join(path, file))
    photo = random.choice(photos)
    os.system(f"viu {photo}")
    wait_for_enter()
    toggle_cursor()


def show_laura():
    os.system("clear")
    filename = "laura.txt"
    data = read_text(filename)
    # width = get_terminal_size().columns
    cols = ["{res}", "{yel}", "{gre}"]
    code = ["\033[0m", "\033[33;1m", "\033[32;1m"]
    toggle_cursor()

    for line in data:
        if line.startswith("#"):
            continue
        else:
            line = line.replace("\n", "")
            # t = line
            for remove in cols:
                # t = t.replace(remove, "")
                idx = cols.index(remove)
                line = line.replace(remove, code[idx])
            # sp = (width - len(t)) // 2 * " "
            if line == "---":
                line = " "
            # print(f"{sp}{line}")
            print(f"{line}")
    wait_for_enter()
    toggle_cursor()


def print_menu():
    os.system("clear")
    colors = Colors()
    yel = colors.yel
    res = colors.res
    pin = colors.pin
    cya = colors.cya
    blu = colors.blu
    gre = colors.gre
    red = colors.red
    whi = colors.whi

    # print(f"-> Writing Help <-")
    # print()
    print(f" {yel}L{res}aura")
    print(f" {cya}P{res}hoto")
    print()
    print(f" {pin}G{res}irl name")
    print(f" {blu}B{res}oy name")
    print(f" {gre}T{res}own name")
    print()
    print(f" {yel}K{res}m <-> M")
    print(f" Kg <-> Lb{cya}s{res}")
    print(f" {pin}M{res} <-> Ft")
    print(f" Cm <-> {blu}I{res}nch")
    print(f" {gre}C{res} <-> F")
    print()
    print(f" {red}Q{res}uit")
    print()
    # options = ["l", "p", "q", "g", "b", "t", "s"]
    # return options


def cmtoinch():
    rate = 2.54
    colors = Colors()
    res = colors.res
    red = colors.red
    gre = colors.gre
    yel = colors.yel

    os.system("clear")
    reply = input(f"{yel}Cm:{res} ").lower()
    convertcm = True
    if reply == "":
        os.system("clear")
        reply = input(f"{yel}Inch:{res} ").lower()
        convertcm = False
    if convertcm:
        os.system("clear")
        answer = round(float(reply) / rate)
        print(f"{gre}{reply} Cm{res} = {red}{answer} Inch{res}")
    else:
        os.system("clear")
        answer = round(float(reply) * rate)
        print(f"{red}{reply} Inch{res} = {gre}{answer} Cm{res}")
    toggle_cursor()
    wait_for_enter()
    toggle_cursor()


def kgtolbs():
    rate = 2.20462
    colors = Colors()
    res = colors.res
    red = colors.red
    gre = colors.gre
    yel = colors.yel

    os.system("clear")
    reply = input(f"{yel}Kg:{res} ").lower()

    convertkg = True
    if reply == "":
        os.system("clear")
        reply = input(f"{yel}Lbs:{res} ").lower()
        convertkg = False
    if convertkg:
        os.system("clear")
        answer = round(float(reply) * rate)
        print(f"{gre}{reply} Kg{res} = {red}{answer} Lbs{res}")
    else:
        os.system("clear")
        answer = round(float(reply) / rate)
        print(f"{red}{reply} Lbs{res} = {gre}{answer} Kg{res}")
    toggle_cursor()
    wait_for_enter()
    toggle_cursor()


def meterstofeet():
    rate = 3.28084
    colors = Colors()
    res = colors.res
    red = colors.red
    gre = colors.gre
    yel = colors.yel

    os.system("clear")
    reply = input(f"{yel}M:{res} ").lower()
    convertm = True
    if reply == "":
        os.system("clear")
        reply = input(f"{yel}Ft:{res} ").lower()
        convertm = False
    if convertm:
        os.system("clear")
        answer = round(float(reply) * rate)
        print(f"{gre}{reply} M{res} = {red}{answer} Ft{res}")
    else:
        os.system("clear")
        answer = round(float(reply) / rate)
        print(f"{red}{reply} Ft{res} = {gre}{answer} M{res}")
    toggle_cursor()
    wait_for_enter()
    toggle_cursor()


def kmtom():
    rate = 0.621371
    os.system("clear")
    reply = input("Km: ").lower()
    convertkm = True
    if reply == "":
        os.system("clear")
        reply = input("M: ").lower()
        convertkm = False
    if convertkm:
        answer = round(float(reply) / rate)
        print(f"{reply} Km = {answer} M")
    else:
        answer = round(float(reply) * rate)
        print(f"{reply} M = {answer} Km")
    toggle_cursor()
    wait_for_enter()
    toggle_cursor()


def ctof():
    # (10°C × 9/5) + 32 = 50°F
    # (10°F − 32) × 5/9 = -12,22°C
    colors = Colors()
    res = colors.res
    yel = colors.yel
    red = colors.red
    gre = colors.gre

    os.system("clear")
    reply = input(f"{yel}C:{res} ").lower()
    convertc = True
    if reply == "":
        os.system("clear")
        reply = input(f"{yel}F: {res}").lower()
        convertc = False
    if convertc:
        # Convert C to F
        rate = 9 / 5
        answer = round((float(reply) * rate) + 32)
        os.system("clear")
        print(f"{gre}{reply}°C{res} = {red}{answer}°F{res}")
    else:
        # Convert F to C
        rate = 5 / 9
        answer = round((float(reply) - 32) * rate)
        os.system("clear")
        print(f"{red}{reply}°F{res} = {gre}{answer}°C{res}")
    toggle_cursor()
    wait_for_enter()
    toggle_cursor()


def try_again():
    print("Please try again...")
    sleep(0.6)


def main():
    loop = True

    while loop:
        # options = print_menu()
        print_menu()

        cursor_on()
        reply = input("> ").lower()
        match reply:
            case "l":
                show_laura()
            case "p":
                show_photo()
            case "g":
                choose_girl_name()
            case "b":
                choose_boy_name()
            case "t":
                choose_town_name()
            case "m":
                meterstofeet()
            case "k":
                kmtom()
            case "s":
                kgtolbs()
            case "c":
                ctof()
            case "i":
                cmtoinch()
            case "q":
                loop = False
            case _:
                try_again()

    os.system("clear")
    cursor_on()
    print("Bye..")
    print()


if __name__ == "__main__":
    main()
