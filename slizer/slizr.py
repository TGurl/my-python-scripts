#!/usr/bin/env python
import os
import random
import pygame
import numpy as np

# -----------------------------------
# --- Constants
# -----------------------------------
WIDTH, HEIGHT = 960, 960
COLS, ROWS = 8, 8
TILESIZE = WIDTH // COLS

TITLE = 'Slizr'
VERSION = '0.1a'
FPS = 60
DEBUG = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 0, 255)

# -----------------------------------
# --- The empty tile
# -----------------------------------
_path = os.path.join('images', 'empty.png')
_surface = pygame.image.load(_path)
_size = (TILESIZE, TILESIZE)
EMPTY_TILE = pygame.transform.scale(_surface, _size)


# ===================================
# === The tile class
# ===================================
class Tile:
    def __init__(self, x, y, surface, number):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.surface = surface
        self.number = number

    def __repr__(self):
        return self.number

# ===================================
# === The main game class
# ===================================
class Game:
    # -----------------------------------------
    # --- Initialisation
    # -----------------------------------------
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(f'{TITLE} {VERSION}')
        self.screen.fill(PINK)
        self.clock = pygame.time.Clock()
        self.mpos_x, self.mpos_y = 0, 0
        self.completed_list = []
    
    # -----------------------------------------
    # --- Initialize board list
    # -----------------------------------------
    def initialize_board(self):
        _surface = pygame.Surface((TILESIZE, TILESIZE))
        self.completed_list = [[Tile(col, row, _surface, '.') for row in range(ROWS)] for col in range(COLS)]

    # -----------------------------------------
    # --- Create a slize of the orignal image
    # -----------------------------------------
    def get_image_slice(self, x, y):
        _subsurface = self.complete_surface.subsurface(x, y, TILESIZE, TILESIZE)
        return _subsurface

    # -----------------------------------------
    # --- Populate board list
    # -----------------------------------------
    def pupulate_boardlist(self):
        # --- X means filled tile
        # --- . means empty tile
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                x = self.completed_list[col][row].x
                y = self.completed_list[col][row].y
                self.completed_list[col][row].surface = self.get_image_slice(x, y)
                self.completed_list[col][row].number = str(count)
                count += 1
        
        # --- now shuffle them around

    # -----------------------------------------
    # --- Show some debug info (DEBUG=True)
    # -----------------------------------------
    def show_debug_info(self, static=True):
        if static:
            print('--------------')
            print('- DEBUG INFO -')
            print('--------------')
            print('WIDTH, HEIGHT:', f'{WIDTH}, {HEIGHT}')
            print('COLS, ROWS:', f'{COLS}, {ROWS}')
            print('TILESIZE:', TILESIZE)
            print('FPS:', FPS)
            print('IMAGE:', self.the_chosen_one)
            print()
            print('COMPLETED BOARD:')
            for row in self.completed_list:
                print(row)

            print()
            print('GAME BOARD:')
            for row in self.board_list:
                print(row)

        #print('MOUSE POS:', f'{self.mpos_x, self.mpos_y}')

    # -----------------------------------------
    # --- Draw the dividing lines
    # -----------------------------------------
    def draw_lines(self):
        for row in range(ROWS):
            for col in range(COLS):
                x = (col * TILESIZE) - 1
                y = (row * TILESIZE) - 1
                pygame.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT), width=3)
                pygame.draw.line(self.screen, BLACK, (0, y), (WIDTH, y), width=3)
            

    # -----------------------------------------
    # --- Choose and load an image
    # -----------------------------------------
    def choose_and_load_image(self):
        collection = []
        valid = ['.jpg', '.png', '.webp']
        for image in os.listdir('images'):
            if os.path.splitext(image)[1] in valid and image != 'empty.png':
                collection.append(os.path.join('images', image))

        self.the_chosen_one = random.choice(collection)
        return pygame.image.load(self.the_chosen_one).convert()

    # -----------------------------------------
    # --- Event listener
    # -----------------------------------------
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mpos_x, self.mpos_y = event.pos
                self.mpos_x = self.mpos_x // TILESIZE
                self.mpos_y = self.mpos_y // TILESIZE

    # -----------------------------------------
    # --- The main loop
    # -----------------------------------------
    def run(self):
        # --- set the clock rate
        self.clock.tick(FPS)

        self.complete_surface = self.choose_and_load_image()
        self.initialize_board()
        
        # --- populate the board_list with slizes
        self.pupulate_boardlist()

        self.board_list = self.completed_list.copy()
        
        random.shuffle(self.board_list)
        for col in self.board_list:
            random.shuffle(col)

        self.board_list[-1][-1].surface = EMPTY_TILE
        self.board_list[-1][-1].number = 'X'

        while True:
            if DEBUG:
                # --- show the debug info
                self.show_debug_info(static=True)

            # --- listen to the events
            self.events()

            # --- draw the tiles
            for row in range(ROWS):
                for col in range(COLS):
                    position = (self.board_list[col][row].x, self.board_list[col][row].y)
                    self.screen.blit(self.board_list[col][row].surface, position)

            # --- draw the lines last
            self.draw_lines()

            # --- show it all
            pygame.display.flip()


if __name__ == '__main__':
    app = Game()
    app.run()
