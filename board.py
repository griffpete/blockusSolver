import pygame
import numpy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_rows = 20
        self.num_cols = 20
        self.cell_size = 25
        self.buffer = width / 2 - (self.cell_size * 20)
        self.border = 5
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grid = numpy.full((20, 20), 0)

    def getCoordinate(self, row, col):
        rect = pygame.Rect(self.buffer + col * self.cell_size, self.buffer + row * self.cell_size, self.cell_size, self.cell_size)
        return rect

    def checkGrid(self, row, col, id):
        #returns true if it is open, false if coordinates are out of bounds or already occupied
        if self.invalidIndex(row, col):
            return False
        elif self.grid[row][col] != 0:
            return False
        elif self.checkSides(row, col, id):
            return False
        else:
            return True

    def invalidIndex(self, row, col):
        #true if invalid, false if valid
        return row >= 20 or col >= 20 or row < 0 or col < 0
    
    def checkSides(self, row, col, id):
        sides = 0
        col += 1
        if not self.invalidIndex(row, col):
            if self.grid[row][col] == id:
                sides += 1
        
        col -= 2
        if not self.invalidIndex(row, col):
            if self.grid[row][col] == id:
                sides += 1

        col += 1
        row += 1
        if not self.invalidIndex(row, col):
            if self.grid[row][col] == id:
                sides += 1

        row -= 2
        if not self.invalidIndex(row, col):
            if self.grid[row][col] == id:
                sides += 1

        if sides != 0:
            return True
        return False
    
    def setGrid(self, row, col, newValue):
        if row < self.num_rows and col < self.num_cols:
            self.grid[row][col] = newValue
    
    def resetGrid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def draw(self, window):
        rect = pygame.Rect(self.buffer, self.buffer, self.cell_size * 20, self.cell_size * 20)
        pygame.draw.rect(window, self.white, rect, width=0)
        rect = pygame.Rect(self.buffer - self.border , self.buffer -self.border, self.cell_size * 20 + self.border * 2, self.cell_size * 20 + self.border * 2)
        pygame.draw.rect(window, self.black, rect, width=5)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                rect = pygame.Rect((i * self.cell_size + self.buffer, j * self.cell_size + self.buffer), (self.cell_size, self.cell_size))
                pygame.draw.rect(window, self.black, rect, 2)