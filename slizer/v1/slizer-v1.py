#!/usr/bin/env python
from pygame.time import delay
from settings import *
from game import *
import pygame


class Slizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.game = Game()

        self.bg = pygame.image.load(self.game.choose_an_image())

        self.selected_count = 0
        self.correct_count = 0
        self.selected_cells = []


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_col = pygame.mouse.get_pos()[0] // CELL_WIDTH
                selected_row = pygame.mouse.get_pos()[1] // CELL_HEIGHT
                selected_coord = (selected_row, selected_col)

                cell_pos = -1
                for i in range(NUM_CELLS):
                    if self.cells[i]['coord'] == selected_coord and not self.cells[i]['locked']:
                        cell_pos = i

                if cell_pos > -1:
                    if self.cells[cell_pos]['selected']:
                        self.cells[cell_pos]['border'] = BORDER_COLOR
                        self.cells[cell_pos]['selected'] = False
                        self.selected_count -= 1
                    else:
                        self.cells[cell_pos]['border'] = GREEN
                        self.cells[cell_pos]['selected'] = True
                        self.selected_count += 1
                    self.selected_cells.append(self.cells[cell_pos])
                    cell_pos = -1

                if self.selected_count == 2:
                    # --- Swap the two selected
                    for cell in self.selected_cells:
                        print(cell)
                    idx1 = self.cells.index(self.selected_cells[0])
                    idx2 = self.cells.index(self.selected_cells[1])

                    temp = self.cells[idx1]['pos']
                    self.cells[idx1]['pos'] = self.cells[idx2]['pos']
                    self.cells[idx2]['pos'] = temp
                    del temp
                        
                    self.selected_cells = []

                    self.selected_count = 0
                    for i in range(NUM_CELLS):
                        self.cells[i]['border'] = BORDER_COLOR
                        self.cells[i]['selected'] = False

                    for i in range(NUM_CELLS):
                        if self.cells[i]['pos'] == self.cells[i]['order']:
                            self.cells[i]['locked'] = True
                            self.correct_count += 1


    def draw_cells(self):
        for i, _ in enumerate(self.cells):
            pos = self.cells[i]['pos']
            x = self.cells[pos]['rect'].x
            y = self.cells[pos]['rect'].y
            img_area = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
            self.screen.blit(self.bg, self.cells[i]['rect'], img_area)
            if not self.cells[i]['locked']:
                pygame.draw.rect(self.screen, self.cells[i]['border'], self.cells[i]['rect'], 4)

    def run(self):
        self.cells = self.game.create_cells()

        # ---- main game loop
        while True:

            self.clock.tick(FPS)
            self.events()
            self.draw_cells()
            
            pygame.display.flip()


if __name__ == "__main__":
    app = Slizer()
    app.run()
