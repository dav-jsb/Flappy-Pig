import pygame
from TelaBase import TelaBase

class TelaMenu(TelaBase):
    def __init__(self, width, height, game_manager):
        super().__init__(width, height)
        self.manager = game_manager
        self.font = pygame.font.SysFont('Arial', 40)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.manager.reset()
                    return "game"
        return True
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("PIG FLAPPY", True, (255, 255, 255))
        start = self.font.render("Press SPACE to Start", True, (255, 255, 255))
        
        self.screen.blit(title, (self.width//2 - title.get_width()//2, self.height//3))
        self.screen.blit(start, (self.width//2 - start.get_width()//2, self.height//2))