#!/usr/bin/env python

import os
import pygame


class Database:
    def __init__(self):
        pygame.init()
        width = 1920
        height = 1080
        self.screen = pygame.display.set_mode(
            (width, height),
            pygame.FULLSCREEN
        )
        self.imgdir = os.path.join(os.getcwd(), 'data', 'images')
        self.fontdir = os.path.join(os.getcwd(), 'data', 'fonts')

        self.font = pygame.font.Font(
            os.path.join(self.fontdir, 'Anja.ttf'),
            64
        )
        self.inputrect = pygame.Rect(200, 200, 140, 32)

    def run(self):
        self.screen.fill((0, 0, 0))
        splash = pygame.image.load(
            os.path.join(self.imgdir, 'splash.png')
        ).convert()
        bg = pygame.image.load(
            os.path.join(self.imgdir, 'bg.png')
        ).convert()
        self.screen.blit(splash, (160, 90))
        pygame.display.update()
        pygame.time.wait(5000)
        self.screen.blit(bg, (0, 0))
        text = self.font.render(
            "I want a big black cock!",
            True,
            'fuchsia'
            )
        text_rect = text.get_rect(
            center = self.screen.get_rect().center
            )
        self.screen.blit(text, text_rect)

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
            pygame.display.update()

        pygame.quit()
