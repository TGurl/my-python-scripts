#!/usr/bin/env python
import pygame
from settings import *
from uielements import UIElements


class LauraTheGame:
    def __init__(self):
        self.init_game()

    def init_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.elements = UIElements()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def mainloop(self):
        while True:
            self.clock.tick(FPS)
            self.events()

            self.elements.draw()

            pygame.display.flip()


if __name__ == "__main__":
    app = LauraTheGame()
    app.mainloop()
