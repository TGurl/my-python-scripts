#!/usr/bin/env python

import os
import random
import pygame as pg



class Slider:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([1600, 900], pg.FULLSCREEN)
        cwd = os.getcwd()
        self.background = os.path.join(
            cwd,
            "images",
            "image001.jpg"
        )
        self.imgpath = os.path.join(
            cwd,
            'images'
        )
        self.images = []
        self.cols = 8
        self.rows = 8
        self.slides = []

    def create_image_list(self):
        for f in os.listdir(self.imgpath):
            if os.path.isfile(os.path.join(self.imgpath, f)):
                self.images.append(os.path.join(self.imgpath, f))

    def slice_it_up(self, img):
        imgw = img.get_width()
        imgh = img.get_height()
        blocksize = int((imgw / self.cols) + (imgh / self.rows))
        print(blocksize)

        for x in range(self.cols + 1):
            for y in range(self.rows + 1):
                slice_area = pg.


    def start_game(self):
        self.create_image_list()
        chosen_img = random.choice(self.images)
        img_bg = pg.image.load(chosen_img).convert()
        self.slice_it_up(img_bg)

        running = True
        while running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            self.screen.fill((255, 255, 255))
            self.screen.blit(img_bg, (0,0))

            pg.display.flip()

        pg.quit()