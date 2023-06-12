import os
import pygame
from settings import *

class TopBar:
    def __init__(self):
        pass

    def draw(self, screen):
        self.topbar_surface = pygame.Surface((topbar_width, topbar_height))
        self.topbar_surface.set_alpha(240)
        self.topbar_surface.fill(DARKBROWN)
        
        path = os.path.join('data', 'fonts', 'ramyoon.ttf')
        title_font = pygame.font.Font(path, 42)
        title_text = title_font.render('< LAURA >', True, WHITE)
        title_shadow = title_font.render('< LAURA >', True, BLACK)
        title_text_rect = title_text.get_rect()
        title_shadow_rect = title_shadow.get_rect()

        offset = 3
        center_x = topbar_width // 2
        center_y = topbar_height // 2
        title_text_rect.center = (center_x, center_y)
        title_shadow_rect.center = (center_x + offset, center_y + offset)
        self.topbar_surface.blit(title_shadow, title_shadow_rect)
        self.topbar_surface.blit(title_text, title_text_rect)

        # show the topbar
        screen.blit(self.topbar_surface, (0,0))

