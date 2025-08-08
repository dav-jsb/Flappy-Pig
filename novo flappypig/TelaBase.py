import pygame

class TelaBase:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def handle_events(self):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)