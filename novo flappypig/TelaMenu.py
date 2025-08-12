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
        menu = pygame.image.load("novo flappypig/assets/menu_com_texto.png")
        self.screen.blit(menu, (0,0))