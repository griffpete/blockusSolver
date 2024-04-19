import pygame
import game
import simulation

TITLE = "Blockus"
WINDOW_WIDTH  = 1250
WINDOW_HEIGHT = 800
DESIRED_RATE  = 100

class PygameApp(game.Game):
    def __init__(self, title, width, height, frame_rate):
        super().__init__(title, width, height, frame_rate)
        self.sim = simulation.Simulation(WINDOW_WIDTH, WINDOW_HEIGHT)

    def update(self, window):
        self.sim.update(window)

def main():
    pygame.init()
    pygame.font.init()
    game = PygameApp(TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE)
    game.main_loop()

if __name__ == "__main__":
    main()
