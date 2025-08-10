import pygame
from GameObject import GameObject

class Pipe(GameObject):
    def __init__(self, x, gap_center, is_top, speed, color, screen_height):
        # Altura proporcional da tela (pode ajustar a porcentagem)
        total_height = screen_height
        pipe_width = 60
        pipe_height = total_height  # desenhamos o cano comprido e depois só mostramos a parte visível
        super().__init__(x, gap_center, pipe_width, pipe_height, color)
        # Define onde vai cortar para criar o gap
        gap_size = int(screen_height * 0.25)  # 25% da altura como abertura
        if is_top:
            # Posiciona o topo
            self.rect.bottom = gap_center - gap_size // 2
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            # Posiciona o de baixo
            self.rect.top = gap_center + gap_size // 2
        self.speed = speed
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
