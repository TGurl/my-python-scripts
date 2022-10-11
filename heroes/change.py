#!/usr/bin/env python

import os
import toml

from tui import TUI
from colors import Colors
from fileio import FileIO

class ChangeData:
    # TODO: Move showinfo to TUI and use it here
    # TODO: rename folder in image folder
    # TODO: move saving data to fileio and
    #       enable saving data here

    def __init__(self):
        self.colors = Colors()
        self.tui = TUI()
        self.fileio = FileIO()

        cwd = os.path.dirname(__file__)
        self.tomldir = os.path.join(cwd, 'data', 'toml')
        self.textdir = os.path.join(cwd, 'data', 'text')
        self.imgdir = os.path.join(cwd, 'data', 'img')

        self.data = self.readdata()
        self.title = "my heroes"

    def readdata(self):
        return self.fileio.readtoml('pornstars')

    def changeid(self):
        old_id = self.data[id]['id']
        answer = self.tui.userinput('What is the new id?')
        answer = answer.replace(" ", "_").lower()
        self.data[id]['id'] = answer

    def changename(self, id):
        answer = self.tui.userinput('What is the new name?')
        answer = self.data[id]['name'] if answer == "" else answer
        self.data[id]['name'] = answer.title()

    def changealias(self, id):
        answer = self.tui.userinput('What are the new aliases?')
        alias = "none" if answer == "" else answer
        self.data[id]['alias'] = answer

    def changerating(self, id):
        answer = self.tui.userinput('What is the new rating out of 10?')
        answer = "0" if answer == "" else answer
        self.data[id]['rating'] = answer

    def changeretired(self, id):
        answer = self.tui.userinput('Retired in')
        answer = '0' if answer == "" else answer
        self.data[id]['retired'] = answer
    
    def toggleactive(self, id):
        if self.data[id]['active']:
            self.data[id]['active'] = False
            self.changeretired(id)
        else:
            self.data[id]['active'] = True

    def changebirthdate(self, id):
        answer = self.tui.userinput('What is the new birthdate?')
        answer = "unknown" if answer == "" else answer
        self.data[id]['birthdate'] = answer
        
    def changecupsize(self,id):
        answer = self.tui.userinput("What is the new cupsize?")
        answer = "unknown" if answer == "" else answer
        self.data[id]['cup'] = answer

    def changeboobs(self, id):
        answer = self.tui.userinput('Are they Natural or Fake?')
        answer = "0" if answer == "" else answer
        self.data[id]['boobs'] = answer

    def changebust(self, id):
        answer = self.tui.userinput('What is the new bust size?')
        answer = "0" if answer == "" else answer
        self.data[id]['bust'] = answer

    def changewaist(self, id):
        answer = self.tui.userinput('What is the new waist size?')
        answer = "0" if answer == "" else answer
        self.data[id]['waist'] = answer

    def changehips(self, id):
        answer = self.tui.userinput('What is the new hip size?')
        answer = "0" if answer == "" else answer
        self.data[id]['hips'] = answer

    def changenationality(self, id):
        answer = self.tui.userinput('What is the new nationality?')
        answer = "unknown" if answer == "" else answer
        self.data[id]['nationality'] = answer

    def changeethnicity(self, id):
        answer = self.tui.userinput('What is the new ethnicity?')
        answer = "unknown" if answer == "" else answer
        self.data[id]['ethnicity'] = answer

    def changeshoesize(self, id):
        answer = self.tui.userinput('What is the new shoe size?')
        answer = "0" if answer == "" else answer
        self.data[id]['shoesize'] = answer

    def changeheight(self, id):
        answer = self.tui.userinput('What is the new height?')
        answer = "0" if answer == "" else answer
        self.data[id]['height'] = answer

    def changeweight(self, id):
        answer = self.tui.userinput('What is the new weight?')
        answer = "0" if answer == "" else answer
        self.data[id]['weight'] = answer

    def change(self, id):
        answer = self.tui.userinput('What is the new ?')
        answer = "unknown" if answer == "" else answer
        self.data[id][''] = answer
    