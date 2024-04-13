import pygame
import game
import board

TITLE = "Blockus"
NUM_ROWS = 20
NUM_COLS = 20
CELL_SIZE = 25
WINDOW_WIDTH  = NUM_COLS * CELL_SIZE
WINDOW_HEIGHT = NUM_ROWS * CELL_SIZE
DESIRED_RATE  = 60

class PygameApp(game.Game):
    def __init__(self, title, width, height, frame_rate):
        super().__init__(title, width, height, frame_rate)
        self.board = board.Board(width, height)

    def paint(self, surface):
        surface.fill((255, 255, 255))
        self.board.draw(surface)

def main():
    pygame.init()
    pygame.font.init()
    game = PygameApp(TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE)
    game.main_loop()

if __name__ == "__main__":
    main()
