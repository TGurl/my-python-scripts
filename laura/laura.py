#!/usr/bin/env python
from screens import Screens
from settings import *
from time import sleep


class GameLoop(Screens):
    def __init__(self):
        super().__init__()

    def move_to(self, location):
        match location:
            case 'h': CONFIG['location'] = 'home'
            case 't': CONFIG['location'] = 'town'
            case 'j': CONFIG['location'] = 'jobcenter'
            case 'm': CONFIG['location'] = 'medicalcenter'
            case 'b': CONFIG['location'] = 'backstreets'
            case 'c': CONFIG['location'] = 'club'
            case 's': CONFIG['location'] = 'shoppingcenter'
            case _: pass

    def run(self):
        valid = []
        while True:
            match CONFIG['location']:
                case 'home': valid = self.home_screen()
                case 'town': valid = self.town_square_screen()
                case 'jobcenter': valid = self.job_center_screen()
                case 'medicalcenter': valid = self.medical_center_screen()
                case 'backstreets': valid = self.back_streets_screen()
                case 'shoppingcenter': valid = self.shopping_center_screen()
                case 'club': valid = self.club_screen()
                case _: pass
            response = input('> ').lower()
            if response not in valid:
                print('Ooops....')
                sleep(1)
            elif response == 'q':
                break
            else:
                self.move_to(response)

if __name__ == "__main__":
    app = GameLoop()
    app.run()
