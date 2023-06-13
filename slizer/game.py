from settings import *
import pygame
import random
import os


class Game:
    def __init__(self):
        pass

    def create_cells(self):
        cells = []
        rand_indexes = list(range(0, NUM_CELLS))
        for i in range(NUM_CELLS):
            row = i % ROWS
            col = i // COLS
            x = row * CELL_WIDTH
            y = col * CELL_HEIGHT
            rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
            rand_pos = random.choice(rand_indexes)
            rand_indexes.remove(rand_pos)
            cells.append({
                'coord': (col, row),
                'rect': rect,
                'border': BORDER_COLOR, 
                'order': i, 
                'pos': rand_pos,
                'selected': False,
                'locked': False})
        return cells

    def choose_an_image(self):
        images = []
        lc_path = os.path.join('images', 'last_used.txt')
        
        if os.path.exists(lc_path):
            with open(lc_path, 'r') as file:
                last_used = file.read().splitlines()
        else:
            last_used = []

        for file in os.listdir('images'):
            if os.path.splitext(file)[1].lower() in ['.jpg', '.png', '.webp']:
                images.append(os.path.join('images', file))

        chosen = random.choice(images)
        while chosen in last_used:
            chosen = random.choice(images)

        with open(lc_path, 'w') as file:
            file.write(chosen)

        return chosen
        
        
