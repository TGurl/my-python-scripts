#!/usr/bin/env python

import os
import pygame
from time import sleep


class Splash:
    def __init__(self):
        cwd = os.getcwd()
        pygame.init()
        imgdir = os.path.join(cwd, 'data', 'images')
        self.splashscreen = pygame.display.set_mode(
            (1600, 900),
            depth=32
        )
        self.img = pygame.image.load(
            os.path.join(imgdir, 'splash.png')
        ).convert()

    def show_splash(self):
        self.splashscreen.blit(self.img, (0, 0))
        pygame.display.update()
        sleep(5)
        pygame.display.quit()
