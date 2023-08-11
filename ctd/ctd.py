#!/usr/bin/env python
from settings import *
import pygame
import random


def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    clock = pygame.time.Clock()
    bg = pygame.image.load(BACKGROUND).convert()
    bg = pygame.transform.scale(bg, RESOLUTION)

    cock = pygame.image.load(COCK).convert_alpha()
    cock_rect = cock.get_rect()
    cock_rect.top = 0
    cock_rect.left = random.randint(0 + cock.get_width(), WIDTH - cock.get_width())

    speed = 5
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_q:
                    running = False


        screen.blit(bg, (0, 0))
        screen.blit(cock, cock_rect)

        cock_rect.top += round(speed)
        if cock_rect.top > HEIGHT + cock.get_height():
            cock_rect.top = -cock.get_height()
            cock_rect.left = random.randint(0 + cock.get_width(), WIDTH - cock.get_width())
            speed += 0.2

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
