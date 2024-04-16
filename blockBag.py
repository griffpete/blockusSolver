import numpy
import random
import tiles

class BlockBag:
    def __init__(self, color, start_row, start_col, id):
        self._id = id
        self._bag = [tiles.straightFive(color, id), tiles.straightFour(color, id), tiles.straightThree(color, id)
                    ,tiles.straightTwo(color, id), tiles.single(color, id), tiles.bigT(color, id), tiles.plus(color, id)] 
        
        #self._bag = [tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color)]
        self._available_pos = numpy.full((20, 20), False)
        self._available_pos[start_row][start_col] = True

    def drawNext(self, window, board):
        #draws the biggest block in the bag, then removes it from bag
        if self.isEmpty():
            return False
        
        nextBlock = self._bag[0]
        for tile in self._bag:
            if tile.getCubes() > nextBlock.getCubes():
                nextBlock = tile

        #keeps track of where blocks are placed, and points that can be placed on in future
        nextPoint = self.getNextPoint()
        if nextPoint is not None:
            row, col = nextPoint
            i = 0
            
            current_block = nextBlock.draw(window, board, row, col)
            while current_block is None:
                nextBlock = self._bag[self.getRandom()]
                i += 1
                if i >= len(self._bag): #prevents code from spiriling into an infinite loop
                    return None
                current_block = nextBlock.draw(window, board, row, col)
            
            del self._bag[self.getIndex(nextBlock)]
            for block in current_block:
                row, col = block
                self.setNewAvailablePositions(row, col, board)
            
        else:
            print("error")

    def getIndex(self, item):
        i = 0
        for tile in self._bag:
            if tile == item:
                return i
            i += 1

    
    def getRandom(self):
        rand = random.randint(0, len(self._bag) - 1)
        return rand

    
    def getNextPoint(self):
        for row in range(20):
            for col in range(20):
                if self._available_pos[row][col]:
                    self._available_pos[row][col] = False
                    return row, col
        return None
    
    def setNewAvailablePositions(self, row, col, board):
        row += 1
        col -= 1
        
        if board.checkGrid(row, col):
            self._available_pos[row][col] = True

        col += 2
        if board.checkGrid(row, col):
            self._available_pos[row][col] = True

        row -= 2
        if board.checkGrid(row, col):
            self._available_pos[row][col] = True

        col -= 2
        if board.checkGrid(row, col):
            self._available_pos[row][col] = True

    
    def isEmpty(self):
        return len(self._bag) == 0