import pygame
from TelaBase import TelaBase

class TelaEnd(TelaBase):
    def __init__(self, width, height, game_manager):
        super().__init__(width, height)
        self.manager = game_manager
        self.big_font = pygame.font.SysFont('Arial', 40)
        self.small_font = pygame.font.SysFont('Arial', 20)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.manager.reset()
                    return "game"
                if event.key == pygame.K_ESCAPE:
                    return "menu"
        return True
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        game_over = self.big_font.render("GAME OVER", True, (255, 0, 0))
        score = self.small_font.render(f"Score: {self.manager.score}", True, (255, 255, 255))
        high_score = self.small_font.render(f"High Score: {self.manager.high_score}", True, (255, 255, 255))
        restart = self.small_font.render("Press SPACE to restart", True, (0, 255, 0))
        menu = self.small_font.render("Press ESC for menu", True, (200, 200, 200))
        
        self.screen.blit(game_over, (self.width//2 - game_over.get_width()//2, self.height//4))
        self.screen.blit(score, (self.width//2 - score.get_width()//2, self.height//2 - 30))
        self.screen.blit(high_score, (self.width//2 - high_score.get_width()//2, self.height//2))
        self.screen.blit(restart, (self.width//2 - restart.get_width()//2, self.height*3//4))
        self.screen.blit(menu, (self.width//2 - menu.get_width()//2, self.height*3//4 + 30))