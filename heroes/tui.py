#!/usr/bin/env python

import os
import sys

from time import sleep
from colors import Colors
from convert import Convert
from fileio import FileIO
from bigletters import BigLetters
from shutil import get_terminal_size

class TUI:
    def __init__(self):
        self.bl = BigLetters()
        self.colors = Colors()
        self.convert = Convert()
        self.fileio = FileIO()

    def clear(self):
        os.system('clear')

    def hide_cursor(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def show_cursor(self):
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        
    def userinput(self, msg):
        col = self.colors.green
        res = self.colors.reset
        if msg == "":
            prompt = f"{col}>{res} "
        else:
            prompt = f"{col}>{res} {msg} : "
        answer = input(prompt)
        if answer == "":
            answer = "unkown"
        return answer
    
    def yesno(self, msg):
        gre = self.colors.green
        res = self.colors.reset
        prompt = f"{gre}>{res} {msg} (y/n) : "

        subloop = True
        while subloop:
            answer = input(prompt).lower()
            if answer in ['y', 'n', 'yes', 'no']:
                subloop = False
            else:
                self.error("Please try that again..")
                sleep(2)
        
        return True if answer in ['y', 'yes'] else False

    def calculatewidth(self, line):
        cols = get_terminal_size().columns
        line = line.replace('{yel}', '')
        line = line.replace('{cyan}', '')
        line = line.replace('{res}', '')
        width = int((cols - len(line)) // 2)
        return width
        
    def rendersplash(self):
        splash = ""
        lines = self.fileio.readtext('splash')
        for line in lines:
            spaces = self.calculatewidth(line) * " "
            line = line.replace('*', ' ')
            line = line.replace('{yel}', self.colors.yellow)
            line = line.replace('{cyan}', self.colors.cyan)
            line = line.replace('{res}', self.colors.reset)
            splash += f"{spaces}{line}\n"
        return splash

    def rendermainmenu(self):
        title = self.rendername("My Heroes")
        items = ["Browse babes", "Search for a babe", "Add a babe", "Quit"]
        yellow = self.colors.yellow
        red = self.colors.red
        res = self.colors.reset
        menu = f"{title}\n\n"
        for item in items:
            letter = item[0]
            rest = item[1:]
            col = red if letter == "Q" else yellow
            menu += "\n" if letter == "Q" else ""
            menu += f"[{col}{letter}{res}]{rest}\n"
        return menu

    def renderbrowsemenu(self, data):
        # TODO -- Add a browse menu with max 10 babes per page
        #         sorted by rating
        data.sort()
        step = 10
        start = 0
        total = len(data)
        end = total if total < step else step

        # print(f">>> Step: {step}")
        subloop = True
        valid = ['q', 'quit', 'p', 'n', 'prev', 'next', 'previous']
        title = self.rendername("My Heroes")
        while subloop:
            self.clear()
            print(title, end='\n\n')
            self.message(f"Number of babes in the database : {total}")
            self.message("Please choose a babe you want to see.")
            print()
            babes = data[start:end]
            for c, babe in enumerate(babes):
                babe = babe.replace('_', ' ').title()
                print(f"{c + 1:3}. {babe}")
                valid.append(str(c + 1))
            print()
            self.message("Type 'prev' or 'next' to browse,")
            answer = self.userinput('or the number of who you want to see.')
            # answer = input("or the number of who you want to see. > ")
            if answer not in valid:
                self.error("Try that again..")
                sleep(2)
                valid = ['q', 'quit', 'p', 'n', 'prev', 'next', 'previous']
            elif answer in ['p', 'prev', 'previous']:
                start -= step
                end = step
                if start < 0:
                    start = 0
            elif answer in ['n', 'next']:
                start = end
                end += step
                if end > total:
                    end = total

            elif answer in ['q', 'quit']:
                id = "exit"
                subloop = False
            else:
                id = babes[int(answer) - 1]
                subloop = False

        return id
            
    def rendername(self, name):
        yel = self.colors.yellow
        res = self.colors.reset
        bigname = self.bl.titler(name)
        return f"{yel}{bigname}{res}"

    def renderrating(self, rating):
        yel = self.colors.yellow
        red = self.colors.red
        cya = self.colors.cyan
        res = self.colors.reset
        fullbar = rating * "♥"
        emptybar = (10 - len(fullbar)) * "∙"
        return f"{red}{fullbar}{yel}{emptybar}{cya} ({rating}/10){res}"

    def converttoname(self, line):
        return line.replace("_", " ").title()

    def message(self, msg):
        col = self.colors.green
        res = self.colors.reset
        prompt = ">"
        print(f"{col}{prompt}{res} {msg}")

    def error(self, msg):
        col = self.colors.red
        res = self.colors.reset
        prompt = ">>"
        print(f"{col}{prompt}{res} {msg}")

    def warning(self, msg):
        col = self.colors.yellow
        res = self.colors.reset
        prompt = ">>"
        print(f"{col}{prompt}{res} {msg}")

    # ----------------------------------------------------
    # ----- SHOW THE INFO
    # ----------------------------------------------------
    def showinfo(self, babeinfo):
        yel = self.colors.yellow
        red = self.colors.red
        gre = self.colors.green
        res = self.colors.reset

        name = self.rendername(babeinfo['name'])
        rating = self.renderrating(babeinfo['rating'])
        active = babeinfo['active']
        year, month = self.convert.convertdob(babeinfo['birthdate'])
        birthdate = f"{month} {year}"
        age = self.convert.calculateage(year)
        retired = babeinfo['retired']
        since = babeinfo['since']
        cup = babeinfo['cup']
        cupeu = self.convert.cuptoeu(cup)
        boobs = babeinfo['boobs']
        bust = babeinfo['bust']
        bustcm = self.convert.inchtocm(bust)
        waist = babeinfo['waist']
        waistcm = self.convert.inchtocm(waist)
        hips = babeinfo['hips']
        hipscm = self.convert.inchtocm(hips)
        height = babeinfo['height']
        feet = self.convert.cmtofeet(height)
        weight = babeinfo['weight']
        pounds = self.convert.kgtopounds(weight)
        ethnicity = babeinfo['ethnicity']
        eyecolor = babeinfo['eyecolor']
        haircolor = babeinfo['haircolor']
        devider = f"{res} / {yel}"
        imgdir = babeinfo['id']
        nationality = babeinfo['nationality']
        alias = self.convert.csvtolist(babeinfo['alias'])
        shoe_eu, shoe_us = self.convert.shoestous(babeinfo['shoesize'])
        shoesize = f"{shoe_eu}{devider}{shoe_us}"

        tattoos = "Unknown" if babeinfo['tattoos'] == "unkown" else babeinfo['tattoos']
        piercings = "Unkown" if babeinfo['piercings'] == "unkown" else babeinfo['piercings']

        tattoos = "None" if tattoos == "none" else tattoos
        piercings = "None" if piercings == "none" else piercings

        measurements = f"{bust}{cup}{devider}{waist}{devider}{hips}"
        measurementseu = f"{bustcm}{cupeu}{devider}{waistcm}{devider}{hipscm}"

        activecol = gre if active else red
        activestr = "Active" if active else "Retired"

        stopped = retired if not active else "0"
        activefor = self.convert.calculateagewhenstarted(since, stopped=stopped)
            
        subloop = True
        while subloop:
            self.clear()
            print(name, end='\n\n')
            
            print(f"Status         : {activecol}{activestr}{res}")
            print(f"Rating         : {rating}", end='\n\n')

            print(f"Alias          : {yel}{alias}{res}")
            print(f"Birthdate      : {yel}{birthdate}{res}")
            print(f"Age            : {yel}{age}{res}")
            print(f"Active since   : {yel}{since}{res}")
            if not active:
                print(f"Retired in     : {yel}{retired}{res}")
            print(f"Active for     : {yel}{activefor} years{res}")
            print(f"Ethnicity      : {yel}{ethnicity}{res}")
            print(f"Nationality    : {yel}{nationality}{res}")
            print(f"Eyecolor       : {yel}{eyecolor}{res}")
            print(f"Haircolor      : {yel}{haircolor}{res}")
            print(f"Measurements   : {yel}{measurements}{res}")
            print(f"Mesurements EU : {yel}{measurementseu}{res}")
            print(f"Cupsize        : {yel}{cup}{res}")
            print(f"Boobs          : {yel}{boobs}{res}")
            print(f"Tattoos        : {yel}{tattoos}{res}")
            print(f"Piercings      : {yel}{piercings}{res}")
            print(f"Height         : {yel}{height} Cm{devider}{feet}{res}")
            print(f"Weight         : {yel}{weight} Kg{devider}{pounds} Lbs{res}")
            print(f"Shoesize       : {yel}{shoesize}{res}")
            print()
            msg = f"[{gre}S{res}] Slideshow  "
            msg += f"[{gre}C{res}] Change  "
            msg += f"[{gre}Q{res}] Go back"
            # self.message("Type 'S' for a slideshow,")
            # self.message("or 'C' to change the data,")
            self.message(msg)
            #answer = input(f"{gre}>{res} or [ENTER] to return to the main menu > ")
            answer = self.userinput("")
            # valid = ['s', 'c', 'q', '']
            if answer.lower() in ['q', 'quit']:
                subloop = False
            elif answer.lower() in ['c', 'change']:
                self.changedata()
            elif answer.lower() in ['s', 'show', 'slideshow']:
                self.fileio.openimgdir(imgdir)
            else:
                self.error("That doesn't seem right somehow..")
                sleep(2)

    # ----------------------------------------------------
    # ----- ENTER DATA LOOP
    # ----------------------------------------------------
    def enterdataloop(self, name):
        yel = self.colors.yellow
        res = self.colors.reset
        subloop = True
        while subloop:
            self.clear()
            print(self.rendername(name), end='\n\n')
            id = name.replace(' ', '_').lower()
            name = name.title()

            active = self.yesno('Active')
            since = self.userinput('Active since')
            retired = "0"
            if not active:
                retired = self.userinput('Retired (yyyy)')
            birthdate = self.userinput('Birthdate (yyyy/mm)')
            aliases = self.userinput('Aliases')
            cup = self.userinput('Cupsize')
            bust = self.userinput('Bust size')
            waist = self.userinput("Waist size")
            hips = self.userinput('Hips')
            height = self.userinput('Height')
            weight = self.userinput('Weight')
            nationality = self.userinput('Nationality')
            ethnicity = self.userinput('Ethnicity')
            eyecolor = self.userinput('Eyecolor')
            haircolor = self.userinput('Haircolor')
            boobs = self.userinput('Boobs (natural/fake)')
            tattoos = self.userinput('Tattoos (none / description)')
            piercings = self.userinput('Piercings (none / description)')
            shoesize = self.userinput('Shoesize EU)')
            rating = self.userinput('Rating (out of 10)')

            measurements = f"{bust}{cup} / {waist} / {hips}"
            active = "true" if active else "false"

            self.clear()
            print(self.rendername(name), end='\n\n')
            print(f"Name         : {yel}{name}{res}")
            print(f"Aliases      : {yel}{aliases}{res}")
            print(f"Active       : {yel}{active}{res}")
            print(f"Active since : {yel}{since}{res}")
            print(f"Retired      : {yel}{retired}{res}")
            print(f"Nationality  : {yel}{nationality}{res}")
            print(f"Ethnicity    : {yel}{ethnicity}{res}")
            print(f"Birthdate    : {yel}{birthdate}{res}")
            print(f"Cup          : {yel}{cup}{res}")
            print(f"Boobs        : {yel}{boobs}{res}")
            print(f"Measurements : {yel}{measurements}{res}")
            print(f"Height       : {yel}{height}{res}")
            print(f"Weight       : {yel}{weight}{res}")
            print(f"Eyecolor     : {yel}{eyecolor}{res}")
            print(f"Haircolor    : {yel}{haircolor}{res}")
            print(f"Tattoos      : {yel}{tattoos}{res}")
            print(f"Piercings    : {yel}{piercings}{res}")
            print(f"Shoesize     : {yel}{shoesize}{res}")
            print(f"Rating       : {yel}{rating}{res}")            
            print()

            correct = self.yesno('Is this correct?')
            if correct:
                subloop = False
            else:
                self.warning('Okay, trying that again...')
                sleep(2)
        
        # ----- preparing the date to store
        self.fileio.makedir(id)
        self.data['pornstars'].append(id)
        babeinfo = []
        babeinfo.append(f"[{id}]")
        babeinfo.append(f"id = '{id}'")
        babeinfo.append(f"name = '{name}'")
        babeinfo.append(f"alias = '{aliases}'")
        babeinfo.append(f"active = {active}")
        babeinfo.append(f"since = '{since}'")
        babeinfo.append(f"retired = {retired}")
        babeinfo.append(f"nationality = '{nationality}'")
        babeinfo.append(f"ethnicity = '{ethnicity}'")
        babeinfo.append(f"birthdate = '{birthdate}'")
        babeinfo.append(f"cup = '{cup}'")
        babeinfo.append(f"boobs = '{boobs}'")
        babeinfo.append(f"bust = {bust}")
        babeinfo.append(f"waist = {waist}")
        babeinfo.append(f"hips = {hips}")
        babeinfo.append(f"height = {height}")
        babeinfo.append(f"weight = {weight}")
        babeinfo.append(f"eyecolor = '{eyecolor}'")
        babeinfo.append(f"haircolor = '{haircolor}'")
        babeinfo.append(f"tattoos = '{tattoos}'")
        babeinfo.append(f"piercings = '{piercings}'")
        babeinfo.append(f"shoesize = {shoesize}")
        babeinfo.append(f"rating = {rating}")
        self.fileio.appendtotoml(babeinfo, self.data['pornstars'])