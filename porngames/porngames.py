#!/usr/bin/env python
import sys, os
import argparse
from utils import Utils

class PornGames(Utils):
    def __init__(self):
        super().__init__()

    def run(self, args):
        running = not args.multiple

        while running:
            target = 'TransGirlNeedsABigBlackCockInHerAss'
            match args.destination:
                case 'todo': target = os.path.join('~', 'Games', 'todo')
                case 'playing': target = os.path.join('~', 'Games', 'playing')
                case _ : 
                    self.myprint('%r!%R Unknown destination chosen')
                    sys.exit()
        
            game = self.select_game()
            if game is not None:
                self.install_game(game, target, keep=args.keep)
            else:
                running = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--destination',
                        required=False,
                        default='playing',
                        help='Target destination for the game (playing)')

    parser.add_argument('-k', '--keep',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Keep the game in archives (FALSE)')

    parser.add_argument('-m', '--multiple',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Install multiple')

    app = PornGames()
    app.run(parser.parse_args())
