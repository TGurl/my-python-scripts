#!/usr/bin/env python
import argparse
from utils import MyUtils


class WP(MyUtils):
    def __init__(self, args):
        super().__init__()
        self.args = args


    def run(self):
        changed = False
        if self.check_configpath():
            self.load_config()

        if self.args.next:
            self.goto_next_wallpaper()
            changed = True
        elif self.args.previous:
            self.goto_previous_wallpaper()
            changed = True
        elif self.args.random:
            self.choose_random_wallpaper()
            changed = True
        else:
            self.wallpaper_menu()
   
        if changed:
            self.set_wallpaper()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--next',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Set next wallpaper')
    parser.add_argument('-p', '--previous',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Set previous wallpaper')
    parser.add_argument('-r', '--random',
                        action='store_true',
                        required=False,
                        default=False,
                        help='Set a random wallpaper')
    args = parser.parse_args()
    app = WP(args)
    app.run()
