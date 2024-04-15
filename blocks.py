import pygame


class Blocks:
    def __init__(self, color):
        self._bag = [straightFive(color), straightFour(color), straightThree(color), straightTwo(color), single(color)] 
    
    def getNext(self):
        #returns the next biggest in the bag of blocks, removes block
        if self.isEmpty():
            return False
        
        biggest = self._bag[0]
        for tile in self._bag:
            if tile.getCubes() > biggest.getCubes():
                biggest = tile

        
        self._bag.remove(biggest)
        return biggest

    def getRandom(self):
        #returns a random block from the bag, removes block
        pass
    
    def isEmpty(self):
        return len(self._bag) == 0

    
class Tile:
    def __init__(self, color, cubes, PoA, rotation, can_flip):
        self._color = color
        self._cubes = cubes
        self._PoA = PoA
        self._rotation = rotation
        self._can_flip = can_flip
    
    def getCubes(self):
        return self._cubes
    def getPoA(self):
        return self._PoA
    def getRotation(self):
        return self._rotation
    def getCanFlip(self):
        return self._can_flip
    
    def rotate(self):
        self._rotation += 90


class straightFive(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 2, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        for i in range(5):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            row += 1

class straightFour(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 2, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        for i in range(4):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            row += 1

class straightThree(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 2, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        for i in range(3):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            row += 1

class straightTwo(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 2, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        for i in range(2):
            pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
            row += 1

class single(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 2, 0, False)
        self._color = color

    def draw(self, window, board, row, col):
        pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
