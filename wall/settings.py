#!/usr/bin/env python3
import os

class Config:
    def __init__(self):
        self.wallpath = os.path.join('/', 'data', 'pictures', 'walls')
        self.maincat = None
        self.subcat = None
        self.current = None
        self.oldlist = []

        self.savefile = os.path.expanduser(
                os.path.join('~', '.local', 'share', 'wallpaper', 'walls.pickle')
                )
