import pygame
from TelaBase import TelaBase
from Consts import Cores

class TelaMenu(TelaBase):
    def __init__(self, width, height, game_manager):
        super().__init__(width, height)
        self.manager = game_manager
        self.font = pygame.font.SysFont('Arial', 40)
    
    def handle_events(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.manager.reset()
                    return "game"
        return True
    
    def draw(self):
        self.screen.fill(Cores.PRETO)
        title = self.font.render("PIG FLAPPY", True, Cores.BRANCO)
        start = self.font.render("Press SPACE to Start", True, Cores.BRANCO)
        
        self.screen.blit(title, (self.width//2 - title.get_width()//2, self.height//3))
        self.screen.blit(start, (self.width//2 - start.get_width()//2, self.height//2))