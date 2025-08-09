import pygame
from GameObject import GameObject

### pra quem for resolver isso, acho que talvez ao inves de criar um tubo pra cima
#e depois outro menor e inverter (como esta agora) seja melhor criar um grante tubo
# e abrir um espaço no meio

class Pipe(GameObject): ### talvez mudar a estrutura dessa classe tbm ajude
    def __init__(self, x, y, is_top, speed,color): 
        ### x e y acho q são o centro do tubo
        # is_top é uma variavel pra inverter se ele for pro lado de cima
        # speed é a velocidade do mapa, e color é a cor do tubo
        height = 300
        gap = 150
        
        if is_top:
            super().__init__(x, y - gap, 60, height, color) 
            # usa o construtor da classe mãe (GameObject) pra completar
            self.image = pygame.transform.flip(self.image, False, True)
             # inverte se for top
        else:
            super().__init__(x, y + gap, 60, height, color)
            #faz a mesma coisa mas sem inverter
        self.speed = speed
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()