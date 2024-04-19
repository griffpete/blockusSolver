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

        self.seeds = 0
        self.recurring_seed = 0


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
        seed = self.board.getGrid()
        
        filename = "blockusSeeds.txt"
    
        delimiter = "#"  # Delimiter to separate seeds
    
        # Check if the seed already exists in the file
        with open(filename, 'r') as file:
            existing_seeds = file.read().split(delimiter)
            seed_str = delimiter.join([''.join(map(str, row)) for row in seed])
            if seed_str in existing_seeds:
                self.recurring_seed += 1
                return

        # Add the new seed to the file
        with open(filename, 'a') as file:
            seed_str = delimiter.join([''.join(map(str, row)) for row in seed])
            file.write(seed_str + delimiter + "\n")
        self.seeds += 1
        return

    def updateTerminal(self):
        #print("\rTotal seeds:", self.seeds)
        #print("Duplicates:", self.recurring_seed)
        pass
        
    
