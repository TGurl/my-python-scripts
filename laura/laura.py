#!/usr/bin/env python
import pygame
from settings import *
from topbar import *
from game import *


class LauraTheGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(GAMETITLE)
        self.clock = pygame.time.Clock()
        self.topbar = TopBar()
        self.game = Game()


    def events(self):
        for event in pygame.event.get():
            # Quit the application
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def run(self):
        while True:
            # Set the frames per second
            self.clock.tick(FPS)

            # Listen to the events
            self.events()
            
            # Set a nice background color
            self.screen.fill(BGCOLOR)

            # show the location
            self.game.draw_location_bg(LOCATION, self.screen)

            # draw the topbar
            self.topbar.draw(self.screen)


            # update the screen
            pygame.display.update()



if __name__ == "__main__":
    app = LauraTheGame()
    app.run()
