import board, blockBag


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
            self._NewRun = False
        
        self.placeNextPiece(window)

        if self.redBlocks.isEmpty() and self.greenBlocks.isEmpty():
            #self._NewRun = True
            pass

    def placeNextPiece(self, window):
        self.redBlocks.drawNext(window, self.board)
        self.greenBlocks.drawNext(window, self.board)
        self.yellowBlocks.drawNext(window, self.board)
        self.BlueBlocks.drawNext(window, self.board)

    def drawBoard(self, window):
        window.fill((186, 186, 186))
        self.board.draw(window)
        
    
