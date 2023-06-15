#!/usr/bin/env python
from settings import *
from engine import Girl


# -----------------------------------------
# --- Class MainGame
# -----------------------------------------

class MainGame:
    
    # -----------------------------------------
    # The main game loop
    # -----------------------------------------

    def __init__(self):
        self.girl = Girl()

    def run(self):
        print(self.girl.get_age())
        print(self.girl.get_sexy())

# -----------------------------------------
# --- An to make it all work...
# -----------------------------------------
if __name__ == "__main__":
    app = MainGame()
    app.run()
