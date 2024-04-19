import board, blockBag
import time

TURN = 0
class Simulation:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._NewRun = True

        self.board = board.Board(width, height)
        self.redBlocks = blockBag.BlockBag((255, 59, 72), 0, 0, 1)
        self.greenBlocks = blockBag.BlockBag((65, 250, 65), 19, 19, 2)
        self.yellowBlocks = blockBag.BlockBag((237, 255, 79), 0, 19, 3)
        self.BlueBlocks = blockBag.BlockBag((65, 145, 250), 19, 0, 4)


    def update(self, window):
        if self._NewRun:            #this resets board 
            self.drawBoard(window)
            self.board.resetGrid()
            self.resetBags()
            self._NewRun = False
            
        
        self.placeNextPiece(window)

        if self.redBlocks.isDone() and self.greenBlocks.isDone() and self.yellowBlocks.isDone() and self.BlueBlocks.isDone():
            self._NewRun = True
            time.sleep(1)

    def placeNextPiece(self, window):
        global TURN
        '''
        if TURN == 0:
            self.redBlocks.drawNext(window, self.board)
        if TURN == 1:
            self.yellowBlocks.drawNext(window, self.board)'''
        if TURN == 2:
            self.greenBlocks.drawNext(window, self.board)
        if TURN == 3:
            self.BlueBlocks.drawNext(window, self.board)
        
        TURN = (TURN + 1) % 4
        

    def drawBoard(self, window):
        window.fill((186, 186, 186))
        self.board.draw(window)

    def resetBags(self):
        self.redBlocks = blockBag.BlockBag((255, 59, 72), 0, 0, 1)
        self.greenBlocks = blockBag.BlockBag((65, 250, 65), 19, 19, 2)
        self.yellowBlocks = blockBag.BlockBag((237, 255, 79), 0, 19, 3)
        self.BlueBlocks = blockBag.BlockBag((65, 145, 250), 19, 0, 4)
        
    
