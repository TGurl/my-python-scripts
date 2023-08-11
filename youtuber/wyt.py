#!/usr/bin/env python
from settings import *
from utils import Utils


class wyt:
    def __init__(self):
        self.utils = Utils()

    def run(self):
        plid = self.utils.get_playlist_id('vintagebeef', 'From Flames')
        print(plid)


if __name__ == '__main__':
    app = wyt()
    app.run()
