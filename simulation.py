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

        self.seeds = self.getSeeds()
        self.recurring_seed = 0
        self.score = 0


    def update(self, window):
        if self._NewRun:            #this resets board 
            self.drawBoard(window)
            self.board.resetGrid()
            self.resetBags()
            self._NewRun = False
            
        
        self.placeNextPiece(window)

        if self.redBlocks.isDone() and self.greenBlocks.isDone() and self.yellowBlocks.isDone() and self.BlueBlocks.isDone():
            if self.redBlocks.isEmpty() and self.greenBlocks.isEmpty() and self.yellowBlocks.isEmpty() and self.BlueBlocks.isEmpty():
                time.sleep(1000000000000)
            
            
            self._NewRun = True
            self.recordSeed()
            self.calculateScore()
            self.updateTerminal()
            #time.sleep(1)

    def placeNextPiece(self, window):
        global TURN
        
        if TURN == 0:
            self.redBlocks.drawNext(window, self.board)
        if TURN == 1:
            self.yellowBlocks.drawNext(window, self.board)
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
    
    def recordSeed(self):
        board = self.board.getGrid()
        filename = "blockusSeeds.txt"
        seed = ""
        for row in range(20):
            for col in range(20):
                seed += str(board[row][col])
        
        with open(filename, 'r') as file:
            for line in file:
                if seed == line:
                    self.recurring_seed += 1
                    return

        with open(filename, 'a') as file:
            file.write(seed + '\n') 
        self.seeds += 1
        return

    def updateTerminal(self):
        print("Total seeds:", self.seeds, " | Duplicates:", self.recurring_seed, " | Highest Score:", self.score, "%", end="\r")
    
    def getSeeds(self):
        filename = "blockusSeeds.txt"
        i = 0
        with open(filename, 'r') as file:
            for _ in file:
                i += 1
        return i
    
    def calculateScore(self):
        r = self.redBlocks.getBagSize()
        g = self.greenBlocks.getBagSize()
        b = self.BlueBlocks.getBagSize()
        y = self.yellowBlocks.getBagSize()

        score = r + g + b +y
        total = 84
        total_score = round(score / total * 100, 1)
        if total_score > self.score:
            self.score = total_score