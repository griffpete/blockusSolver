import pygame

class Tile:
    def __init__(self, color, cubes): 
        self._color = color
        self._cubes = cubes
    
    def getCubes(self):
        return self._cubes
    def getRotation(self):
        return self._rotation
    def getCanFlip(self):
        return self._can_flip

    def placeTile(self, window, board, coordinates, id):
        #print("new shape")
        valid = True
        for i in range(4):
            valid = True
            for pos in coordinates:
                row, col = pos
                if not board.checkGrid(row, col, id):
                        valid = False
            if self._cubes > 1 and not valid:
                coordinates = self.rotate90(coordinates)
        
        if not valid:
            return False
                    
        
        #print("size" ,self._cubes, "(r1, g2, y3, b4) id:",id, "coordinates", coordinates)
        for pos in coordinates:
            row, col = pos
            self.drawCube(window, board, row, col)
            board.setGrid(row, col, id)
        return True
    
    def rotate90(self, coordinates):
        new_cords = []
        first_row, first_col = coordinates[0]
        second_row, second_col = coordinates[1]

        if first_row == second_row:
            for pos in coordinates:
                row, col = pos
                dis = first_col - col
                dif = first_row - row
                new_cords.append((first_row + dis, first_col - dif))
        else:
            for pos in coordinates:
                row, col = pos
                dis = first_row - row
                dif = first_col - col
                new_cords.append((first_row + dif, first_col - dis))
        return new_cords 
     
        

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
        