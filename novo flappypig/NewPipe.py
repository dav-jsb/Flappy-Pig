import pygame
from GameObject import GameObject

### pra quem for resolver isso, acho que talvez ao inves de criar um tubo pra cima
#e depois outro menor e inverter (como esta agora) seja melhor criar um grante tubo
# e abrir um espaço no meio

class Pipe(GameObject): ### talvez mudar a estrutura dessa classe tbm ajude
    def __init__(self, y_baixo,y_alto,tela_largura, speed,color): 
        super().__init__(tela_largura+50, (y_baixo+y_alto)//2, 60, y_alto-y_baixo, color)
        
        self.speed = speed
    
    def update(self): # esse aqui ta certo
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()