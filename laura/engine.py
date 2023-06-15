from settings import *
from girl import *

class GirlData:
    age = 18
    location = 'home'
    room = 'bedroom'
    bank = 100
    job = 'stripper'
    sexy = 0
    cup = 0
    stamina = 100
    birthday = False
    tired = False
    maxcup = False

class Girl():
    def __init__(self):
        pass

    def get_age(self):
        return GirlData.age
    
    def set_age(self):
        GirlData.age += 1
        GirlData.birthday = True

    def get_location(self):
        return GirlData.location.title()

    def set_location(self, newlocation):
        GirlData.location = newlocation

    def get_room(self):
        return GirlData.room.title()

    def set_room(self, newroom):
        GirlData.room = newroom

    def get_job(self):
        return GirlData.job.title()

    def set_job(self, newjob):
        GirlData.job = newjob

    def get_bank_balance(self):
        return f"${GirlData.bank}"

    def set_bank_balance(self, deposit):
        GirlData.bank += deposit

    def get_stamina(self):
        return f"{GirlData.stamina}%"

    def set_stamina(self, value):
        GirlData.stamina += value
        if GirlData.stamina < 10:
            GirlData.tired = True

    def get_cup(self):
        return CUPS[GirlData.cup].upper()

    def set_cup(self):
        if not GirlData.maxcup:
            GirlData.cup += 1
            if GirlData.cup > len(CUPS) - 1:
                GirlData.cup = len(CUPS) - 1
                GirlData.maxcup = True

    def get_sexy(self):
        return f"{GirlData.sexy}%"

    def set_sexy(self):
        GirlData.sexy = (GirlData.cup * 100) // (len(CUPS) - 1)
