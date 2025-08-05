#Bibliotecas
import pygame

# Classe dos Tubos
class Tubo(pygame.sprite.Sprite):
    
    def __init__(self, x, y, invertido,cor,velocidade):
        super().__init__()
        self.image = pygame.Surface((60, 300))
        self.image.fill(cor)
        self.velocidade = velocidade
        if invertido:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midbottom=(x, y - 100))
        else:
            self.rect = self.image.get_rect(midtop=(x, y + 100))

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()