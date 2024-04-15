import pygame
import board, blocks


class Simulation:
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self.board = board.Board(width, height)
        self.redBlocks = blocks.Blocks((250, 27, 27))

    def update(self):
        pass
    
    def draw(self, window):
        window.fill((186, 186, 186))
        self.board.draw(window)
        self.redBlocks.getNext().draw(window, self.board.getCoordinate(1, 1))
        self.redBlocks.getNext().draw(window, self.board.getCoordinate(1, 2))
        self.redBlocks.getNext().draw(window, self.board.getCoordinate(1, 3))
        self.redBlocks.getNext().draw(window, self.board.getCoordinate(2, 2))
