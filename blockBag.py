import numpy
import random
import tiles

class BlockBag:
    def __init__(self, color, start_row, start_col, id):
        self._id = id
        self._bag = [tiles.straightFive(color, id), tiles.straightFour(color, id), tiles.straightThree(color, id), tiles.halfCross(color, id), tiles.gun(color, id), tiles.lightning(color, id)
                    ,tiles.straightTwo(color, id), tiles.single(color, id), tiles.bigT(color, id), tiles.littleT(color, id), tiles.plus(color, id)
                    ,tiles.square(color, id), tiles.utah(color, id), tiles.arch(color, id), tiles.bigL(color, id), tiles.littleL(color, id)
                    ,tiles.littleR(color, id), tiles.bigR(color, id), tiles.squigle(color, id), tiles.bigS(color, id), tiles.littleS(color, id)] 
        self.sortBag()
        #self._bag = [tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color)]
        self._start = start_row, start_col
        self._available_pos = []
        self._available_pos.append(self._start)
        self._is_done = False
    
    def getBagSize(self):
        return len(self._bag)

    def drawNext(self, window, board):
        #draws the biggest block in the bag, then removes it from bag
        if self.isEmpty():
            return False
        
        nextBlock = self._bag[-1]

        #keeps track of where blocks are placed, and points that can be placed on in future
        
        for i in range(len(self._bag)):
            placed = True
            nextPoint = self.getNextPoint(i)
            if nextPoint is not None:
                row, col = nextPoint
                current_block = nextBlock.draw(window, board, row, col)

                j = 0
                while current_block is None:
                    j += 1
                    if j >= len(self._bag): #prevents code from spiriling into an infinite loop
                        placed = False
                        break
                    nextBlock = self._bag[-j]
                    current_block = nextBlock.draw(window, board, row, col)
                    
                    
                if placed:
                    del self._bag[-j]
                    for block in current_block:
                        row, col = block
                        self.setNewAvailablePositions(row, col, board)
                    return
        
        self._is_done = True
        return
        
            
        
    def sortBag(self):
        not_changed = True
        random.shuffle(self._bag)
        while not_changed:
            not_changed = False
            for i in range(len(self._bag)):
                if i == len(self._bag) - 1:
                    continue
                if self._bag[i].getCubes() > self._bag[i + 1].getCubes():
                    self._bag[i], self._bag[i + 1] = self._bag[i + 1], self._bag[i]
                    not_changed = True
        
    def getIndex(self, item):
        i = 0
        for tile in self._bag:
            if tile == item:
                return i
            i += 1

    
    def getRandom(self):
        rand = random.randint(0, len(self._bag) - 1)
        return rand

    def getNextPoint(self, i):
        '''row, col = self._start
        if row == 0:
            row = 19
        else:
            row = 0
        if col == 0:
            col = 19
        else:
            col = 0'''
        try:
            self._available_pos[-i]
        except:
            return None
        else:
            return self._available_pos[-i]

       
    
    def setNewAvailablePositions(self, row, col, board):
        row += 1
        col -= 1
        if board.checkGrid(row, col, self._id):
            self._available_pos.append((row, col))

        col += 2
        if board.checkGrid(row, col, self._id):
            self._available_pos.append((row, col))

        row -= 2
        if board.checkGrid(row, col, self._id):
            self._available_pos.append((row, col))

        col -= 2
        if board.checkGrid(row, col, self._id):
            self._available_pos.append((row, col))

    
    def isEmpty(self):
        return len(self._bag) == 0
    
    def isDone(self):
        if self.isEmpty():
            return True
        return self._is_done