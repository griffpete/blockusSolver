import pygame
import board, blocks


class Simulation:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._NewRun = True

        self.board = board.Board(width, height)
        self.redBlocks = blocks.Blocks((250, 27, 27))

    def update(self, window):
        if self._NewRun:            #this resets board 
            self.drawBoard(window)
            self.board.resetGrid()
            self._NewRun = False
        
        self.placeNextPiece(window)

    def placeNextPiece(self, window):
        row = col = 0

        for i in range(5):
            block = self.redBlocks.getNext()
            if block:
                print("draw a block")
                block.draw(window, self.board, row, col)
                col += 2
            else:
                print("block == false")
    
    def drawBoard(self, window):
        window.fill((186, 186, 186))
        self.board.draw(window)
        
    
