#!/usr/bin/env python
import pygame
from settings import *
from images import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.initialize()

    def initialize(self):
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.playing = True
        self.images = Images()
        image, self.completed_surf = self.images.choose_an_image()
        self.board_list = self.images.slize_it_up(image)
        print(TILESIZE)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def draw(self):
        self.screen.fill(PINK)
        self.screen.blit(self.completed_surf, (0, 0))
        pygame.display.flip()

    def run(self):
        while self.playing:
            self.events()
            self.draw()


if __name__ == "__main__":
    app = Game()
    app.run()
