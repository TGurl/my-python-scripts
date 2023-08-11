import os
from settings import *
from tui import TUI

class Screens(TUI):
    def __init__(self):
        super().__init__()

    # -------------------------------------------------------------------
    # --- Helper functions
    # -------------------------------------------------------------------
    def __determine_cupsize(self):
        return CUPS[CONFIG['cup']].upper()

    def __calculate_sexyness(self):
        return (CONFIG['cup'] * 100) // len(CUPS)

    def generate_info_bars(self):
        topbar = ''
        botbar = ''

        cupsize = self.__determine_cupsize()
        sexyness = self.__calculate_sexyness()

        topbar += f"%cDay:%R {CONFIG['day']}  "
        topbar += f"%cAge:%R {CONFIG['age']}  "
        topbar += f"%cCup:%R {cupsize}  "
        topbar += f"%cSexy:%R {sexyness}%  "
        topbar += f"%cEnergy:%R {CONFIG['energy']}%"

        botbar += f"%cLocation:%R {CONFIG['location'].capitalize()}  "
        botbar += f"%cBank:%R ${CONFIG['bank']:6}  "
        if CONFIG['job'] is not None:
            botbar += f"%cJob:%R {CONFIG['job']}  "
            botbar += f"%cWage:%R ${CONFIG['wage']:4}  "
        botbar += f"%cRent:%R ${CONFIG['rent']:4}"

        return topbar, botbar


    def draw_header(self, options):
        topbar, botbar = self.generate_info_bars()
        os.system('clear')
        self.myprint('%yLAURA%R', center=True)
        self.drawline()
        self.myprint(topbar, center=True)
        self.myprint(botbar, center=True)
        self.drawline()
        
        if CONFIG['location'] == 'home':
            if 'quit' not in options:
                options.append('quit')
        
        valid = []
        option_bar = ''
        for count, option in enumerate(options, start=1):
            col = '%r' if option == 'quit' else '%y'
            option_bar += f"%c[{col}{option[0].upper()}%c]%R{option[1:]}"
            if count < len(options):
                option_bar += '  '
            valid.append(option[0].lower())
        self.myprint(option_bar, center=True, nl=True)
        return valid

    # -------------------------------------------------------------------
    # --- Home screen
    # -------------------------------------------------------------------
    def home_screen(self):
        valid = self.draw_header(HOME)
        return valid

    # -------------------------------------------------------------------
    # --- Town square screen
    # -------------------------------------------------------------------
    def town_square_screen(self):
        valid = self.draw_header(TOWN)
        return valid

    # -------------------------------------------------------------------
    # --- Job center screen
    # -------------------------------------------------------------------
    def job_center_screen(self):
        valid = self.draw_header(JOBCENTER)
        return valid

    # -------------------------------------------------------------------
    # --- Medical center screen
    # -------------------------------------------------------------------
    def medical_center_screen(self):
        valid = self.draw_header(MEDICALCENTER)
        return valid

    # -------------------------------------------------------------------
    # --- Back streets screen
    # -------------------------------------------------------------------
    def back_streets_screen(self):
        valid = self.draw_header(BACKSTREETS)
        return valid

    def shopping_center_screen(self):
        valid = self.draw_header(MALL)
        return valid
    
    def club_screen(self):
        valid = self.draw_header(CLUB)
        return valid
