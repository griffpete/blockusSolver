import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, window):
        CELL_SIZE = 25
        for x in range(0, self.width, CELL_SIZE):
            pygame.draw.line(window, (0, 0, 0), (x, 0), (x, self.height))
        for y in range(0, self.height, CELL_SIZE):
            pygame.draw.line(window, (0, 0, 0), (0, y), (self.width, y))