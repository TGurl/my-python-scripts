import os
import random
from re import split
import pygame
from settings import *
from PIL import Image


class Images:
    def __init__(self) -> None:
        self.valid = ['.jpg', '.png']

    def initialize_grid(self):
        image = ''
        type = '.'
        board_list = []
        for row in range(ROWS):
            for col in range(COLS):
                column = [ row, col, image, type ]
                board_list.append(column)
        return board_list

    def collect_all_images(self):
        images = []
        for file in os.listdir('images'):
            _, ext = os.path.splitext(file)
            if ext in self.valid:
                images.append(file)
        return images

    def choose_an_image(self):
        image = random.choice(self.collect_all_images())
        path = os.path.join('images', image)
        image_surf = pygame.image.load(path).convert()
        return image, image_surf

    def slize_it_up(self, image):
        board_list = self.initialize_grid()
        save_path = os.path.join('images', 'tiles')
        img_path = os.path.join('images', image)
        im = Image.open(img_path)
        imgwidth, imgheight = im.size
        rows = int(imgheight / TILESIZE)
        cols = int(imgwidth / TILESIZE)
        for i in range(rows):
            for j in range(cols):
                box = (j*TILESIZE, i*TILESIZE, (j+1)*TILESIZE, (i+1)*TILESIZE)
                im1 = im.crop(box)
                path = os.path.join(save_path, f'tile_{i}_{j}.png')
                im1.save(path)
                tile_surf = pygame.image.load(path)
                board_list[i][j].image = tile_surf
        return board_list
