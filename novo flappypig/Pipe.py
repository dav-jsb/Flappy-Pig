import pygame
from GameObject import GameObject
from Consts import Panela


class Pipe(GameObject):
    def create_composite_pipe(self, width, height):
        #Cria um sprite de pipe composto por três partes usando imagens
        #
        #width: Largura do pipe
        #height: Altura total desejada
        #top_img_path: Caminho para a imagem do topo
        #middle_img_path: Caminho para a imagem do meio
        #bottom_img_path: Caminho para a imagem da base
        
        # Carrega as imagens
        top_sprite = pygame.image.load(Panela.TOP).convert_alpha()
        middle_sprite = pygame.image.load(Panela.MIDDLE).convert_alpha()
        bottom_sprite = pygame.image.load(Panela.BOTTOM).convert_alpha()

        # Obtém as alturas das partes
        top_height = top_sprite.get_height()
        bottom_height = bottom_sprite.get_height()
        middle_height = middle_sprite.get_height()

        # Calcula quantas repetições do meio são necessárias
        available_height = height - top_height - bottom_height
        middle_repeats = max(0, available_height // middle_height)
        # Cria superfície final
        composite = pygame.Surface((width, height), pygame.SRCALPHA)
        
        current_y = 0
        
        # Parte superior
        composite.blit(top_sprite, (-3, current_y))
        current_y += top_height
        
        # Parte do meio (repetida)
        for _ in range(middle_repeats):
            composite.blit(middle_sprite, (0, current_y))
            current_y += middle_height
        
        # Parte inferior
        composite.blit(bottom_sprite, (0, current_y))
        
        return composite
    
    def __init__(self, x, ymin, ymax, speed, color=None):
        # Cria o sprite composto antes de chamar o construtor pai
        composite_sprite = self.create_composite_pipe(115,ymax-ymin)
        
        super().__init__(
            x=x,
            y=(ymax+ymin)//2,
            width=115,
            height=ymax-ymin,
            image_path=composite_sprite  # Passa a superfície composta
        )
        self.speed = speed
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
