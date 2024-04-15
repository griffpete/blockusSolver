import pygame


class Blocks:
    def __init__(self, color):
        self._bag = [straightFive(color)] #fill with all 21 block types
    
    def getNext(self):
        #returns the next biggest in the bag of blocks, removes block
        if self.isEmpty():
            return False
        
        biggest = self._bag[0]

        for tile in self._bag:
            if tile.getCubes() > biggest.getCubes():
                biggest = tile

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
    
    def drawCube(self, row, rect):
        pass


class straightFive(Tile):
    def __init__(self, color):
        super().__init__(color, 5, 2, 0, False)
        self._color = color

    def draw(self, window, rect):
        #self.drawCube(row, column)
        #self.drawCube(row + 1, column)
        pygame.draw.rect(window, self._color, rect)