#!/usr/bin/env python
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from screens import UIElement
from settings import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    uielement = UIElement(
            center_position=(WIDTH // 2, HEIGHT // 2),
            font_size=42,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text='Easy - (3x3 grid)',
            bg_img='gui/bg.png'
            )

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        # screen.fill(BLUE)

        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
