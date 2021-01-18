import pygame
import numpy as np
from time import sleep
from constant import *

class Board():
    def __init__(self):
        self.board = []
        pygame.init()
 #kann weg
        self.black = BLACK
        self.white = WHITE
        self.blue = BLUE
        self.green = GREEN

    def Grid(self, win_height, win_width):
        SCREEN = pygame.display.set_mode((win_height, win_width))
        CLOCK = pygame.time.Clock()
        pygame.display.set_caption("Auto-Completion | min-edit Distance")
        SCREEN.fill(GREY)
        return SCREEN, CLOCK

    def Matrix(self, row, col):
        grid = np.zeros((col+1,row+1), dtype=int)
        return grid

    def draw_squares(self, screen, clock, rows, cols, grid,sleeper=False):
        for row in range(rows):
            for col in range(cols):            
                color = GREY
                rect = pygame.Rect(col*BLOCKSIZE, row*BLOCKSIZE,
                               BLOCKSIZE-MARGIN, BLOCKSIZE-MARGIN)
                if grid[row][col] == 1:
                    color = GREEN
                elif grid[row][col] == 2:
                    color = RED
                elif grid[row][col] == 3:
                    color = BLUE
                pygame.draw.rect(screen, color, rect)
    

    def set_source(self, screen, clock, rows, cols, df, source, target, sleeper=False):
        white = (255, 255, 255) 
        green = (0, 255, 0) 
        blue = (0, 0, 128) 
        font = pygame.font.Font('freesansbold.ttf', 32)
        color = GREY
        for row in range(rows):
            source_character = source[row-1] 
            for col in range(cols):            
                target_character = target[col-1]
                set_rect = (col*BLOCKSIZE + 15, row*BLOCKSIZE + 10, BLOCKSIZE-MARGIN, BLOCKSIZE-MARGIN)
                rect = pygame.Rect(set_rect)
                if row == 0 and col == 0:
                    text = font.render('#', True, blue)
                    screen.blit(text, set_rect)
                elif col == 0:
                    text = font.render(source_character, True, green)
                    screen.blit(text, set_rect)
                elif row == 0:
                    text = font.render(target_character, True, green)
                    screen.blit(text, set_rect)

    
    def fill(self, screen, clock, rows, cols, tmp_d, source, target):        
        font = pygame.font.Font('freesansbold.ttf', 32)
        green = (0, 255, 0) 
        white = (255, 255, 255) 
        for d in tmp_d:
            max_val = np.amax(d)
            min_val = np.amin(d)
            c = sum(i for i in range(min_val, max_val))
            for row in range(rows):
                for col in range(cols):
                    set_rect = (col*BLOCKSIZE, row*BLOCKSIZE, BLOCKSIZE-MARGIN, BLOCKSIZE-MARGIN)
                    if row != 0 and col != 0:
                        cal = d[row][col] 
                        print(max_val, min_val,c,"ccccccc")
                        print(((c/max_val)))
                        color = (0,int((1-(max_val/c)**(1/cal)) * 255),0)
                        text = font.render(str(cal), True, white)
                        pygame.draw.rect(screen, color, set_rect)
                        m = (15,10,0,0)
                        set_rect = [a + b for a, b in zip(set_rect, m)]
                        screen.blit(text, set_rect)
                        sleep(0.3)
                        pygame.display.update()
                sleep(0.4)