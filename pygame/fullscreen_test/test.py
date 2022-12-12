#!/usr/bin/env python

import pygame, sys
from pygame.locals import *
from pygame import mixer

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1920,1080), FULLSCREEN)
BG = pygame.image.load('bg.jpg')
HEADER = pygame.image.load('header.png')
MAP = pygame.image.load('citymap.png')

mixer.init()
mixer.music.load('./Home.ogg')
mixer.music.play()
mixer.music.pause()

MAPMUSIC = mixer.Sound("./Overworld.ogg")
    
SHOWMAP = False
BGMUSIC = True
PLAY_MAPMUSIC = False
mainloop = True

while mainloop:
    DISPLAYSURF.blit(BG, (0,0))
    DISPLAYSURF.blit(HEADER,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                mainloop = False
            elif event.key == pygame.K_m:
                BGMUSIC = not BGMUSIC
                SHOWMAP = not SHOWMAP
                PLAY_MAPMUSIC = not PLAY_MAPMUSIC
        elif event.type == pygame.QUIT:
            mainloop = False

    if BGMUSIC:
        mixer.music.unpause()
    else:
        mixer.music.pause()

    if PLAY_MAPMUSIC:
        mixer.Sound.play(MAPMUSIC)
    else:
        mixer.Sound.stop(MAPMUSIC)

    if SHOWMAP:
        DISPLAYSURF.blit(MAP, (0,0))
    else:
        DISPLAYSURF.blit(BG, (0,0))

    pygame.display.update()

pygame.quit()
