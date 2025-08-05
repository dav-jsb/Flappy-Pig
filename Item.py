# Bibliotecas 
import pygame

# Classe dos Itens
class Item(pygame.sprite.Sprite):

    def __init__(self, x, y, cor,velocidade):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(cor)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = velocidade

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()