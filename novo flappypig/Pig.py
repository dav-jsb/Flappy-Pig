from GameObject import GameObject

class Pig(GameObject):
    def __init__(self, x, y,gravity,pulo):
        super().__init__(x, y, 30, 30, image_path="novo flappypig/assets/pig/vanilla pig.png") #alterei a imagem padrão do porco
        self.gravity = gravity
        self.pulo = pulo
        
    def update(self, screen_height):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        
        # Limites da tela
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
    
    def jump(self):
        self.velocity = self.pulo