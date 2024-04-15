import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_rows = 20
        self.num_cols = 20
        self.cell_size = 25
        self.buffer = width / 2 - (self.cell_size * 20)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def getCoordinate(self, row, col):
        rect = pygame.Rect(self.buffer + col * self.cell_size, self.buffer + row * self.cell_size, self.cell_size, self.cell_size)
        return rect

    def draw(self, window):
        rect = pygame.Rect(self.buffer, self.buffer, self.cell_size * 20, self.cell_size * 20)
        pygame.draw.rect(window, self.white, rect, width=0)
        rect = pygame.Rect(self.buffer, self.buffer, self.cell_size * 20, self.cell_size * 20)
        pygame.draw.rect(window, self.black, rect, width=5)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                rect = pygame.Rect((i * self.cell_size + self.buffer, j * self.cell_size + self.buffer), (self.cell_size, self.cell_size))
                pygame.draw.rect(window, self.black, rect, 2)