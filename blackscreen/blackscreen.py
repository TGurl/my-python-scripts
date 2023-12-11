#!/usr/bin/env python3

import pygame
from pygame.locals import *
import argparse
from time import sleep


def main(wait):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1600, 900), FULLSCREEN)

    mainloop = True

    while mainloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
        pygame.display.update()

        sleep(wait)
        mainloop = False

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--time", type=int, default=5, required=False)
    args = parser.parse_args()

    main(args.time)
