import random
import tiles

class BlockBag:
    def __init__(self, color, start_row, start_col, sort_variable, id):
        self._id = id
        self._bag = [tiles.straightFive(color, id), tiles.straightFour(color, id), tiles.straightThree(color, id), tiles.halfCross(color, id), tiles.gun(color, id), tiles.lightning(color, id)
                    ,tiles.straightTwo(color, id), tiles.single(color, id), tiles.bigT(color, id), tiles.littleT(color, id), tiles.plus(color, id)
                    ,tiles.square(color, id), tiles.utah(color, id), tiles.arch(color, id), tiles.bigL(color, id), tiles.littleL(color, id)
                    ,tiles.littleR(color, id), tiles.bigR(color, id), tiles.squigle(color, id), tiles.bigS(color, id), tiles.littleS(color, id)] 
        random.seed(sort_variable)
        self.sortBag()
        #self._bag = [tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color),tiles.single(color)]
        self._start = start_row, start_col
        self._available_pos = []
        self._available_pos.append(self._start)
        self._is_done = False
    
    def getBagSize(self):
        return len(self._bag)

    def drawNext(self, window, board):
        if self.isEmpty():
            return False
                
        for i in range(len(self._bag)):
            placed = False
            nextPoint = self.getNextPoint(i)
            if nextPoint is not None:
                row, col = nextPoint
                for i in range(len(self._bag) - 1, -1, -1):
                    current_block = self._bag[i]
                    block_coordinates = current_block.draw(window, board, row, col)
                    if block_coordinates != None:
                        placed = True
                        break 
                    
                if placed:
                    del self._bag[i]
                    for coords in block_coordinates:
                        row, col = coords
                        self.setNewAvailablePositions(row, col, board)
                    return
        
        self._is_done = True
        return
        
            
        
    def sortBag(self):
        random.shuffle(self._bag)
        not_changed = True
        while not_changed:
            not_changed = False
            for i in range(len(self._bag)):
                if i == len(self._bag) - 1:
                    continue
                if self._bag[i].getCubes() > self._bag[i + 1].getCubes():
                    self._bag[i], self._bag[i + 1] = self._bag[i + 1], self._bag[i]
                    not_changed = True
        
    
    def getRandom(self):
        rand = random.randint(0, len(self._bag) - 1)
        return rand

    def getNextPoint(self, i):
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