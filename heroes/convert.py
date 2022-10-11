#!/usr/bin/env python

from math import floor
from datetime import date


class Convert:
    def __init__(self):
        pass

    def shoestous(self, shoesize):
        if shoesize == 0:
            return "Unknown", "Unknown"
        else:
            eu = f"{shoesize} eu"
            if shoesize == 35:
                us = "4"
            elif 35 < shoesize < 36:
                us = "5"
            elif shoesize == 36:
                us = "5.5"
            elif 36 < shoesize < 37:
                us = "6"
            elif shoesize == 37:
                us = "6.5"
            elif 37 < shoesize < 38:
                us = "7"
            elif shoesize == 38:
                us = "7.5"
            elif 38 < shoesize < 39:
                us = "8"
            elif shoesize == 39:
                us = "8.5"
            elif 39 < shoesize < 40:
                us = "9"
            elif shoesize == 40:
                us = "9.5"
            elif 40 < shoesize < 41:
                us = "10"
            elif shoesize == 41:
                us = "10.5"
            elif 41 < shoesize < 42:
                us = "11"
            elif shoesize == 42:
                us = "11.5"
            else:
                us = "Unkown"

            if us != "Unkown":
                us = f"{us} us"
            return eu, us

    def convertdob(self, birthdate):
        months = [
            'January', 'February', 'March',
            'April', 'Mai', 'June', 'July',
            'August', 'September', 'October',
            'November', 'December'
        ]
        year = birthdate.split('/')[0]
        month = birthdate.split('/')[1]
        month = months[int(month)]
        return year, month

    def csvtolist(self, line):
        return line.replace(",", ", ")

    def calculateage(self, year):
        age = date.today().year - int(year)
        return age

    def calculateagewhenstarted(self, started, stopped="0"):
        started = int(started)
        stopped = int(stopped)
        if stopped == 0:
            stopped = date.today().year
        return stopped - started

    def kgtopounds(self, kg):
        return round(kg * 2.205)

    def cmtofeet(self, cm):
        length = cm / 2.54
        feet = floor(length/12)
        inch = round(length - (12*feet))
        return f"{feet}ft {inch}in"

    def inchtocm(self, inch):
        return round(inch * 2.54)

    def cuptoeu(self, cup):
        eu = [
            'A', 'B', 'C',
            'D', 'E', 'E', 'F',
            'G', 'G', 'H',
            'J', 'K', 'L',
            'L', 'M'
        ]
        us = [
            'A', 'B', 'C',
            'D', 'DD', 'E', 'DDD',
            'DDDD', 'G', 'H', 
            'I', 'J', 'K',
            'L', 'M'
        ]
        idx = us.index(cup)
        return eu[idx]
