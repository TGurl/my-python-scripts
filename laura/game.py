import os
import pygame
from settings import *


class Game:
    def __init__(self):
        pass

    def load_location_bg(self, location):
        if '.webp' not in location:
            location += '.webp'
        path = os.path.join('data', 'images', location)
        return pygame.image.load(path).convert()

    def draw_location_bg(self, location, screen):
        surface = self.load_location_bg(location)
        screen.blit(surface, (0,0))

