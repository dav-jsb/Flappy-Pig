import pygame
from GameObject import GameObject

class Pig(GameObject):
    def __init__(self, x, y, gravity, pulo,image):
        super().__init__(x, y, 30, 30, image_path=None) #qunado inicializa, não pega nenhum arquivo ainda
        self.image = image
        self.gravity = gravity
        self.pulo = pulo

    def update(self, screen_height):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def jump(self):
        self.velocity = self.pulo

    def change_skin(self, new_image):
        self.image = new_image
