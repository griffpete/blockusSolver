import pygame

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

    def placeTile(self, window, board, coordinates, id):
        for pos in coordinates:
            row, col = pos
            if not board.checkGrid(row, col):
                return False
            
        for pos in coordinates:
            row, col = pos
            self.drawCube(window, board, row, col)
            board.setGrid(row, col, True)
        return True
        

    def drawCube(self, window, board, row, col):
        pygame.draw.rect(window, self._color, board.getCoordinate(row, col))
        
        r,g,b = self._color
        r -= 30
        g -= 30
        b - 30
        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
        
        rect = board.getCoordinate(row, col)
        rect.inflate(-2, -2)
        pygame.draw.rect(window, (r,g,b), rect, 4)
        board.setGrid(row, col, True)
'''
class newTileBlueprint(Tile):
    def __init__(self, color, id):
        super().__init__(color, num_cubes, rotation, can_be_flipped)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        
        #edit coordinates to place other blocks and append them to the coordinates list

        #any edge tiles will be returned in a list, to be delt with by the grid class

        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None
        
'''

class straightFive(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for i in range(5):
            coordinates.append((row, col))
            row += 1
        
        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None

class straightFour(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        first_pos = row, col
        coordinates = []
        for i in range(4):
            coordinates.append((row, col))
            row += 1
        last_pos = row, col

        if self.placeTile(window, board, coordinates, self._id):
            return [first_pos, last_pos]
        return None

class straightThree(Tile):
    def __init__(self, color, id):
        super().__init__(color, 3, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        first_pos = row, col
        coordinates = []
        for i in range(3):
            coordinates.append((row, col))
            row += 1
        last_pos = row, col

        if self.placeTile(window, board, coordinates, self._id):
            return [first_pos, last_pos]
        return None

class straightTwo(Tile):
    def __init__(self, color, id):
        super().__init__(color, 2, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        first_pos = row, col
        coordinates = []
        for i in range(2):
            coordinates.append((row, col))
            row += 1
        last_pos = row, col

        if self.placeTile(window, board, coordinates, self._id):
            return [first_pos, last_pos]
        return None

class single(Tile):
    def __init__(self, color, id):
        super().__init__(color, 1, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        if self.placeTile(window, board, [(row, col)], self._id):
            return [(row, col)]
        return None
        

class bigT(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for i in range(3):
            coordinates.append((row, col))
            row -= 1
        bottom_pos = row, col

        row += 1
        col += 1
        coordinates.append((row, col))
        right_pos = row, col

        col -= 2
        coordinates.append((row, col))
        left_pos = row, col

        if self.placeTile(window, board, coordinates, self._id):
            return [left_pos, right_pos, bottom_pos]
        return None
    

class plus(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5, 0, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        top_pos = row, col
        coordinates = []
        for i in range(3):
            coordinates.append((row, col))
            row -= 1
        bottom_pos = row, col

        row += 1
        col += 1
        coordinates.append((row, col))
        right_pos = row, col

        col -= 2
        coordinates.append((row, col))
        left_pos = row, col

        if self.placeTile(window, board, coordinates, self._id):
            return [top_pos, left_pos, right_pos, bottom_pos]
        return None
