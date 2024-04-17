from tileParent import Tile

'''
class newTileBlueprint(Tile):
    def __init__(self, color, id):
        super().__init__(color, num_cubes, can_rotate)
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
        super().__init__(color, 5, True)
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
        super().__init__(color, 4, True)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for i in range(4):
            coordinates.append((row, col))
            row += 1

        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None

class straightThree(Tile):
    def __init__(self, color, id):
        super().__init__(color, 3, True)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = []
        for i in range(3):
            coordinates.append((row, col))
            row += 1

        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None

class straightTwo(Tile):
    def __init__(self, color, id):
        super().__init__(color, 2, True)
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
            return coordinates
        return None

class single(Tile):
    def __init__(self, color, id):
        super().__init__(color, 1, False)
        self._color = color
        self._id = id

    def draw(self, window, board, row, col):
        coordinates = [(row, col)]
        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None
        

class bigT(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5, True)
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

        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None
    

class littleT(Tile):
    def __init__(self, color, id):
        super().__init__(color, 4, True)
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

        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None
    
class plus(Tile):
    def __init__(self, color, id):
        super().__init__(color, 5, False)
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

        if self.placeTile(window, board, coordinates, self._id):
            return coordinates
        return None
