#Bibliotecas
import pygame

# Arquivos do jogo

# Classe do Porco
class Pig(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(cor)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 0

    def update(self,gravidade,tela_altura):
        self.velocidade += gravidade
        self.rect.y += self.velocidade

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.velocidade = -7

        # Limites da tela
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= tela_altura:
            self.rect.bottom = tela_altura