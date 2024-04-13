import pygame
import pygame.locals

class Game:
    def __init__( self, name, width, height, frames_per_second ):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption( name )

    def paint(self, surface):
        raise NotImplementedError( )

    def main_loop( self ):        
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.update()
            self.paint(self.screen)
            pygame.display.flip()
            clock.tick(self.frames_per_second)

        pygame.quit()
        sys.exit()