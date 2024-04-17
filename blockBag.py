import numpy
import random
import tiles

class BlockBag:
    def __init__(self, color, start_row, start_col, id):
        self._id = id
        self._bag = [tiles.straightFive(color, id), tiles.straightFour(color, id), tiles.straightThree(color, id)
                    ,tiles.straightTwo(color, id), tiles.single(color, id), tiles.bigT(color, id), tiles.littleT(color, id), tiles.plus(color, id)] 
        
        #self._bag = [tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color)]
        self._start = start_row, start_col
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
        

    def getIndex(self, item):
        i = 0
        for tile in self._bag:
            if tile == item:
                return i
            i += 1

    
    def getRandom(self):
        rand = random.randint(0, len(self._bag) - 1)
        return rand

    
    def getNextPoint_Legacy(self):
        for row in range(20):
            for col in range(20):
                if self._available_pos[row][col]:
                    self._available_pos[row][col] = False
                    return row, col
        return None

    def getNextPoint(self):
        s_row, s_col = self._start
        if self._available_pos[s_row][s_col]:       # checks if start is open before doing reverse loop
            self._available_pos[s_row][s_col] = False
            return s_row, s_col

        row, col = self._start
        if row == 0:
            row = 19
            r_offset = -1
        else:
            row = 0
            r_offset = 1
        if col == 0:
            col = 19
            c_offset = -1
        else:
            col = 0
            c_offset = 1

        for i in range(19):
            for j in range(i * r_offset, (i + 1) * r_offset, r_offset):
                new_row = row + j
                if 0 <= new_row < 20 and self._available_pos[new_row][col]:
                    self._available_pos[new_row][col] = False
                    return new_row, col
            for j in range(i * c_offset, (i + 1) * c_offset, c_offset):
                new_col = col + j
                if 0 <= new_col < 20 and self._available_pos[row][new_col]:
                    self._available_pos[row][new_col] = False
                    return row, new_col
            for j in range(i * r_offset, (i + 1) * r_offset, r_offset):
                new_row = row - j
                if 0 <= new_row < 20 and self._available_pos[new_row][col]:
                    self._available_pos[new_row][col] = False
                    return new_row, col

            
        #loop going to 20
            #set new start with either just row or col at point i
            #loop traversing (down or up) and over number of i
                #check if pos is available
    
    def setNewAvailablePositions(self, row, col, board):
        row += 1
        col -= 1
        
        if board.checkGrid(row, col, self._id):
            self._available_pos[row][col] = True

        col += 2
        if board.checkGrid(row, col, self._id):
            self._available_pos[row][col] = True

        row -= 2
        if board.checkGrid(row, col, self._id):
            self._available_pos[row][col] = True

        col -= 2
        if board.checkGrid(row, col, self._id):
            self._available_pos[row][col] = True

    
    def isEmpty(self):
        return len(self._bag) == 0