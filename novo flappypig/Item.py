
import pygame
from GameObject import GameObject

class Item(GameObject):
    COLORS = {
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "white": (255, 255, 255),
        "yellow": (255,255,0),
        "green": (0,255,0)
    }

    def __init__(self, x, y, tipo, image_item, size=(30, 30)):
        width, height = size
        color = None if image_item else self.COLORS.get(tipo, (255,255,255))
        super().__init__(x, y, width, height, color, image_item)
        if image_item:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.tipo = tipo
        self.surface = self.image  # guarda a surface para troca de skin

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
