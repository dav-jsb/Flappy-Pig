import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=None, image_path=None):
        super().__init__()
        if image_path: #alterei para poder receber tanto uma imagem quanto uma surface
            if isinstance(image_path, pygame.Surface):
                self.image = image_path
            elif isinstance(image_path, str):
                self.image = pygame.image.load(image_path).convert_alpha()
        else:
            self.image = pygame.Surface((width, height))
            if color:
                self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0

    def update(self, *args, **kwargs):
        """Método base para atualização do objeto"""
        pass

    def draw(self, surface):
        """Método para desenhar o objeto"""
        surface.blit(self.image, self.rect)
