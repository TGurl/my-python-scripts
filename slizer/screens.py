#!/usr/bin/env python
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from settings import *

class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, bg_img):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background color) - tuple (r, g, b)
            text_rgb (foreground color) - tuple (r, g, b)
            bg_img - path to image for background
        """

        self.mouse_over = False

        topcenter = (WIDTH // 2, 150)

        self.bg_image = pygame.image.load(bg_img).convert_alpha()

        self.title_image = self.create_surface_with_text(
                text='Slizer', font_size=96, text_rgb=(255,255,255), bg_rgb=bg_rgb
                )
        self.title_rect = self.title_image.get_rect(center=topcenter)

        default_image = self.create_surface_with_text(
                text=text, font_size=font_size, text_rgb = text_rgb, bg_rgb=bg_rgb
                )

        highlighted_image = self.create_surface_with_text(
                text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
                )

        self.images = [default_image, highlighted_image]
        self.rects = [default_image.get_rect(center=center_position),
                      highlighted_image.get_rect(center=center_position)]

        super().__init__()
    
    def create_surface_with_text(self, text, font_size, text_rgb, bg_rgb):
        """ Retuns a surface with text written on """
        font = pygame.freetype.Font("fonts/grooven-shine.otf", font_size)
        # surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
        surface, _ = font.render(text=text, fgcolor=text_rgb)
        return surface.convert_alpha()
    
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]


    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element to a surface """
        surface.blit(self.bg_image, (0, 0))
        surface.blit(self.title_image, self.title_rect)
        surface.blit(self.image, self.rect)

