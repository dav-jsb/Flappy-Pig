import pygame
from GameObject import GameObject

        # top_pipe = Pipe(self.width + 60, gap_center, True, speed, color, self.height)
        # bottom_pipe = Pipe(self.width + 60, gap_center, False, speed, color, self.height)
        
        #
        # top_pipe = Pipe(self.width + 60, gap_center+self.espaco_tubo//2, self.height, self.map_speed, self.color_pipe, self.height)
        # bottom_pipe = Pipe(self.width + 60, 0,gap_center+self.espaco_tubo//2, self.map_speed, self.color_pipe, self.height)
        # 

class Pipe(GameObject):
    def __init__(self, x, ymin,ymax, speed, color):
        super().__init__(x, (ymax+ymin)//2, 60, ymax-ymin, color)
        ## x é a posição do centro em x, (ymax+ymin)//2 é o centro em y (a media)
        ## 60 a largura, ymax-ymin é a altura color é a cor
        self.speed = speed
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
