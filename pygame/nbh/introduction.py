#!/usr/bin/env python

import os
import pygame


class Introduction:
    def __init__(self, screen):
        self.screen = screen
        self.cwd = os.getcwd()
        self.imagedir = os.path.join(self.cwd, "data", "images")
        self.musicdir = os.path.join(self.cwd, "data", "music")
        self.confdir = os.path.join(self.cwd, "data", "config")
        self.music = pygame.mixer.Sound(
            os.path.join(self.musicdir, 'Emotion2.ogg')
        )
        self.channel = pygame.mixer.Channel(0)

        self.imagelist = [
            'warning.png',
            'christmas.png',
            'story01.png',
            'story02.png',
            'story03.png',
            'last.png',
            'nbh.png',
            'bg.png'
        ]

    def fadein(self, imgSurf, pause=4):
        for x in range(255):
            imgSurf.set_alpha(x)
            self.screen.blit(imgSurf, (0, 0))
            pygame.display.flip()
            pygame.time.delay(pause)

    def fadeout(self, imgSurf, pause=4):
        for x in range(255):
            imgSurf.set_alpha(255 - x)
            self.screen.blit(imgSurf, (0, 0))
            pygame.display.flip()
            pygame.time.delay(pause)

    def start(self):
        imgSurf = pygame.image.load(
            os.path.join(self.imagedir, 'nbh.png')
        ).convert()

        self.music.set_volume(0.4)
        self.channel.play(self.music, loops=-1, fade_ms=1000)

        for image in self.imagelist:
            imgSurf = pygame.image.load(
                os.path.join(self.imagedir, image)
            ).convert()
            self.fadein(imgSurf)
            if image in ['warning.png']:
                wait = 0.2
            elif 'story' in image:
                wait = 10
            elif image in ['nbh.png']:
                wait = 8
            else:
                wait = 2

            pygame.time.wait(int(wait * 1000))
            if image == 'nbh.png':
                self.fadeout(imgSurf, pause=16)

            if image != 'bg.png':
                self.fadeout(imgSurf)

        self.channel.fadeout(4000)
        pygame.time.delay(4000)
        self.channel.stop()
