import pygame
import board, blocks


class Simulation:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._NewRun = True

        self.board = board.Board(width, height)
        self.redBlocks = blocks.Blocks((250, 27, 27), 0, 0)
        self.greenBlocks = blocks.Blocks((0, 163, 15), 19, 19)


    def update(self, window):
        if self._NewRun:            #this resets board 
            self.drawBoard(window)
            self.board.resetGrid()
            self._NewRun = False
        
        self.placeNextPiece(window)

        if self.redBlocks.isEmpty() and self.greenBlocks.isEmpty():
            #self._NewRun = True
            pass

    def placeNextPiece(self, window):
        self.redBlocks.drawNext(window, self.board)
        self.greenBlocks.drawNext(window, self.board)

    def drawBoard(self, window):
        window.fill((186, 186, 186))
        self.board.draw(window)
        
    
