import pygame
import pygame.locals
import sys

class Game:
    def __init__( self, name, width, height, frames_per_second ):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption( name )

    def update(self, surface):
        raise NotImplementedError( )
    
    def keyPress(self, key):
        raise NotImplementedError( )

    def main_loop( self ):        
        clock = pygame.time.Clock()
        running = True
        print("\n") #just for formating outputs
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.keyPress("pause")
                    elif event.key == pygame.K_UP:
                        self.keyPress("next")
                    elif event.key == pygame.K_RIGHT:
                        self.keyPress("step")
                    elif event.key == pygame.K_r:
                        self.keyPress("random")
                    elif event.key == pygame.K_q:
                        running = False
            
            self.update(self.screen)
            pygame.display.flip()
            clock.tick(self.frames_per_second)

        print("\n") #just for formating outputs
        pygame.quit()
        sys.exit()