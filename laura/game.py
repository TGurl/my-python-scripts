#!/usr/bin/env python

from fileio import FileIO
from dataclasses import dataclass


@dataclass
class Laura:
    age: int
    cup: int
    sexy: int
    health: int
    day: int
    year: int
    daycount: int
    bank: float
    wage: float
    maxtip: float
    job: str
    location: str
    room: str
    tips: bool
    tipcup: bool
    illegal: bool
    std: bool
    pregnant: bool
    arrested: bool
    worked: bool
    wearing: list
    inventory: list
    partners: list


class Game:
    def __init__(self):
        self.fileio = FileIO()

    def default_settings(self):
        Laura.age = 18
        Laura.cup = 0
        Laura.sexy = 0
        Laura.health = 100
        Laura.bank = 1000.0
        Laura.wage = 0.0
        Laura.maxtip = 0.0
        Laura.day = 1
        Laura.year = 2010
        Laura.daycount = 0
        Laura.job = "none"
        Laura.location = "home"
        Laura.room = "bedroom"
        Laura.tips = False
        Laura.tipcup = False
        Laura.illegal = False
        Laura.std = False
        Laura.pregnant = False
        Laura.arrested = False
        Laura.worked = False
        Laura.wearing = ['bra', 'panties']
        Laura.inventory = []
        Laura.partners = []

    def savegame(self):
        self.fileio.savegame(Laura)
