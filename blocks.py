import pygame
import numpy

class Blocks:
    def __init__(self, color, start_row, start_col):
        self._bag = [straightFive(color), straightFour(color), straightThree(color), straightTwo(color), single(color), plus(color)] 
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
            valid_blocks = nextBlock.draw(window, board, row, col)

            for block in valid_blocks:
                row, col = block
                self.setNewAvailablePositions(row, col, board)
            self._bag.remove(nextBlock)
        else:
            print("error")

    def getRandom(self):
        #returns a random block from the bag, removes block
        pass
    
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

    
class Tile:
    def __init__(self, color, cubes, rotation, can_flip):
        self._color = color
        self._cubes = cubes
        self._rotation = rotation
        self._can_flip = can_flip
    
    def getCubes(self):
        return self._cubes
    def getRotation(self):
        return self._rotation
    def getCanFlip(self):
        return self._can_flip
    
    def rotate(self):
        self._rotation += 90


class straightFive(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        first_pos = row, col
        for i in range(5):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            board.setGrid(row, col, True)
            row += 1
        last_pos = row, col
        return [first_pos, last_pos]

class straightFour(Tile):
    def __init__(self, color):
        super().__init__(color, 4, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        first_pos = row, col
        for i in range(4):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            board.setGrid(row, col, True)
            row += 1
        last_pos = row, col
        return [first_pos, last_pos]

class straightThree(Tile):
    def __init__(self, color):
        super().__init__(color, 3, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        first_pos = row, col
        for i in range(3):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            board.setGrid(row, col, True)
            row += 1
        last_pos = row, col
        return [first_pos, last_pos]

class straightTwo(Tile):
    def __init__(self, color):
        super().__init__(color, 2, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        first_pos = row, col
        for i in range(2):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            board.setGrid(row, col, True)
            row += 1
        last_pos = row, col
        return [first_pos, last_pos]

class single(Tile):
    def __init__(self, color):
        super().__init__(color, 1, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
        board.setGrid(row, col, True)
        last_pos = row, col
        return [last_pos]

class plus(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        top_pos = row, col

        for i in range(3):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            board.setGrid(row, col, True)
            row -= 1
        bottom_pos = row, col

        row += 1
        col += 1
        pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
        board.setGrid(row, col, True)
        right_pos = row, col

        col -= 2
        pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
        board.setGrid(row, col, True)
        left_pos = row, col

        last_pos = row, col
        return [top_pos, left_pos, right_pos, bottom_pos]
