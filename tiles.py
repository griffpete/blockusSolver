from tileParent import Tile

'''
class newTileBlueprint(Tile):
    def __init__(self, color, id):
        super().__init__(color, num_cubes)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None
        
'''

class straightFive(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(5):
            coordinates.append((row, col))
            row += 1
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class straightFour(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(4):
            coordinates.append((row, col))
            row += 1

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class straightThree(Tile):
    def __init__(self, color, id):
        super().__init__(color, 3)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(3):
            coordinates.append((row, col))
            row += 1

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class straightTwo(Tile):
    def __init__(self, color, id):
        super().__init__(color, 2)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(2):
            coordinates.append((row, col))
            row += 1

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class single(Tile):
    def __init__(self, color, id):
        super().__init__(color, 1)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = [(row, col)]
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None
        

class bigT(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(3):
            coordinates.append((row, col))
            row += 1

        row -= 1
        col -= 1
        coordinates.append((row, col))

        col += 2
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None
    

class littleT(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(2):
            coordinates.append((row, col))
            row += 1

        row -= 1
        col -= 1
        coordinates.append((row, col))

        col += 2
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None
    
class plus(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(3):
            coordinates.append((row, col))
            row += 1

        row -= 2
        col -= 1
        coordinates.append((row, col))

        col += 2
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class square(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        
        coordinates.append((row, col))
        row += 1
        coordinates.append((row, col))
        col -= 1
        coordinates.append((row, col))
        row -= 1
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class utah(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        
        coordinates.append((row, col))
        row += 1
        coordinates.append((row, col))
        col -= 1
        coordinates.append((row, col))
        row -= 1
        coordinates.append((row, col))
        row -= 1
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class arch(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        col += 1
        for _ in range(3):
            coordinates.append((row, col))
            row += 1
        row -= 1
        col -= 1
        coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class bigL(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(4):
            coordinates.append((row, col))
            row += 1
        row -= 1
        col += 1
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class littleL(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(3):
            coordinates.append((row, col))
            row += 1
        row -= 1
        col += 1
        coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class littleR(Tile):
    def __init__(self, color, id):
        super().__init__(color, 3)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(2):
            coordinates.append((row, col))
            row += 1
        row -= 1
        col += 1
        coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class bigR(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(3):
            coordinates.append((row, col))
            row += 1
        row -= 1
        for _ in range(2):
            col += 1
            coordinates.append((row, col))
                    
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class squigle(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        for i in range(4):
            if i % 2 == 0:
                row += 1
            else:
                col += 1
            coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class bigS(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        col += 1
        for _ in range(3):
            coordinates.append((row, col))
            row += 1
        row -= 1
        col += 1
        coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class littleS(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        col += 1
        coordinates.append((row, col))
        row -= 1
        coordinates.append((row, col))
        col += 1
        coordinates.append((row, col))
        
        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None
    
class halfCross(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(4):
            coordinates.append((row, col))
            row += 1
        row -= 2
        col += 1
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None
    
class gun(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        coordinates.append((row, col))
        row += 1
        coordinates.append((row, col))
        col -= 1
        coordinates.append((row, col))
        row += 1
        coordinates.append((row, col))
        row -= 1
        col -= 1
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None

class lightning(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5)
        self._color = color
        self._id = id
    
    def draw(self, window, board, row, col):
        coordinates = []
        for _ in range(3):
            coordinates.append((row, col))
            row += 1
        row -= 1
        col += 1
        coordinates.append((row, col))
        row += 1
        coordinates.append((row, col))

        coordinates = self.placeTile(window, board, coordinates, self._id)
        if coordinates:
            return coordinates
        return None