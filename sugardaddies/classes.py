#!/usr/bin/env python

class person(object):
    def __init__(self, firstname, lastname, age, sex, job, locked):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.job = job
        self.locked = locked

    @property
    def name(self):
        return f"{self.firstname} {self.lastname}"


class room(object):
    def __init__(self, name, north, east, south, west, exit):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.exit = exit
