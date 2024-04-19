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
        
        #edit coordinates to place other blocks and append them to the coordinates list

        #any edge tiles will be returned in a list, to be delt with by the grid class

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
        for i in range(5):
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
        for i in range(4):
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
        for i in range(3):
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
        for i in range(2):
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
        for i in range(3):
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
        for i in range(2):
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
        for i in range(3):
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
