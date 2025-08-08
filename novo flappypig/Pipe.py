import pygame
from GameObject import GameObject

class Pipe(GameObject):
    def __init__(self, x, y, is_top, speed,color):
        height = 300
        gap = 150
        
        if is_top:
            super().__init__(x, y - gap, 60, height, color)
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            super().__init__(x, y + gap, 60, height, color)
        
        self.speed = speed
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()