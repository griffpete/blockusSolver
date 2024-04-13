import pygame
import board, blocks


class Simulation:
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self.board = board.Board(width, height)
        self.block = bocksBlocks()

    def update(self):
        pass
    
    def draw(self, window):
        window.fill((186, 186, 186))
        self.board.draw(window)
        self.block.draw(window)
